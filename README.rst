Thamos
------

A CLI tool and library for communicating with Thoth backend.


Using Thamos as a CLI tool
==========================

Thamos is released on `PyPI <https://pypi.org/project/thamos>`_. See
installation instructions bellow to setup Thoth/Thamos for your repository:

.. code-block:: console

  # Install Thamos CLI tool:
  $ pip3 install thamos  # keep in mind: requires Python 3.6+!!
  # Go to repository that should be managed by Thoth which already has Pipfile present:
  $ cd ~/git/repo/
  # Setup Thamos configuration:
  $ thamos config
  # Ask Thoth for software stack recommendations:
  $ thamos advise
  # Retrieve logs of the last analysis:
  $ thamos log


As Thamos notes analysis ids for better UX of ``thamos log``, it's recommended to
add ``.thoth_last_analysis_id`` file to ``.gitignore``.


Adjusting configuration based on environment variables
======================================================

You can adjust content of configuration file each time Thamos CLI or Thamos
library loads it by expanding entries with environment variables. This can be
handy if you would like to parameterize some of the options at
runtime (e.g. in deployment).

This behaviour is (due to security reasons) explicitly turned off by default.
However you can turn it on by setting ``THAMOS_CONFIG_EXPAND_ENV`` environment
variable to ``1`` (``0`` explicitly turns this behaviour off, default value):


.. code-block:: console

    THOTH_HOST=test.thoth-station.ninja THAMOS_CONFIG_EXPAND_ENV=1 thamos advise
    2019-03-13 11:22:59,562 [18639] INFO     thamos.config: Expanding configuration file based on environment variables

Entries which should be expanded have environment variables in curly braces
like the following example:

.. code-block:: yaml

   host: {THOTH_HOST}


Note the expansion is done by replacing these values directly with values of
environment variable, this means types need to be taken into account
(environment variable with value ``"true"`` is put into configuration file as
``true``).


Using custom configuration file template
========================================

You can use your own custom configuration file as a template. This is
especially useful if you want to have some configuration entries constant and
let expand only some of the configuration options. In other words, you can
parametrize configuration file.

An example of configuration file template can be:

.. code-block:: yaml

  host: {THOTH_SERVICE_HOST}
  tls_verify: true
  requirements_format: {requirements_format}

  runtime_environments:
    - name: '{os_name}:{os_version}'
      operating_system:
        name: {os_name}
        version: '{os_version}'
      hardware:
        cpu_family: {cpu_family}
        cpu_model: {cpu_model}
      python_version: '{python_version}'
      cuda_version: {cuda_version}
      recommendation_type: stable
      platform: '{platform}'

Then, you need to supply this configuration file to the following command:

.. code-block:: console

  thamos config --template template.yaml

Listing of automatically expanded configuration options which are supplied the
config sub-command (these options are optional and will be expanded based on HW
or SW discovery):

+------------------------+--------------------------------+-----------------+
| Configuration option   | Explanation                    | Example         |
+========================+================================+=================+
| `os_name`              | name of operating system       | fedora          |
+------------------------+--------------------------------+-----------------+
| `os_version`           | version of operating system    |  30             |
+------------------------+--------------------------------+-----------------+
| `cpu_family`           | CPU family identifier          |  6              |
+------------------------+--------------------------------+-----------------+
| `cpu_model`            | CPU model identifier           |  94             |
+------------------------+--------------------------------+-----------------+
| `python_version`       | Python version (major.minor)   |  3.6            |
+------------------------+--------------------------------+-----------------+
| `cuda_version`         | CUDA version (major.minor)     |  9.0            |
+------------------------+--------------------------------+-----------------+
| `platform`             | Platform used.                 |  linux-x86_64   |
+------------------------+--------------------------------+-----------------+
| `requirements_format`  | Requirements format.           |  pipenv         |
+------------------------+--------------------------------+-----------------+

Platform corresponds to ``sysconfig.get_platform()`` call.

These configuration options are optional and can be mixed with adjustment based
on environment variables (see ``THOTH_SERVICE_HOST`` example above). Note the
environment variables are not expanded on `thamos config` call but rather on
other sub-commands issued (e.g. ``thamos advise`` or others).

The output format coming out of recommendations can be compatible with
`Pipenv <https://pipenv.kennethreitz.org/en/latest/>`__,
`raw pip <https://pip.pypa.io/en/stable/user_guide/>`__  or similar to the one
provided by `pip-tools <https://pypi.org/project/pip-tools/>`__ (actually same as for
``pip`` as these formats are interchangeable). The format is configured using
``requirements_format`` configuration option, available options are:

* ``requirements_format: pipenv`` for `Pipenv <https://pipenv.kennethreitz.org/en/latest/>`__ compatible output
* ``requirements_format: pip`` or ``requirements_format: pip-tools`` for `pip <https://pip.pypa.io/en/stable/user_guide/>`__ or `pip-tools <https://pypi.org/project/pip-tools/>`__ compatible output

Support for multiple runtime environments
=========================================

Thoth performs recommendations based on your hardware and software environment,
so called runtime environments. You can specify more than just one runtime
environment that should be targetted during recommendations. This might be
suitable if you would like to tweak some runtime environment specific
configuration options. An example could be a deployment of a machine learning
model to the cluster that uses CUDA, but you do not run CUDA locally (fast
iterative development locally, subsequently training a model in the cluster on
a large dataset). In such cases, you can specify two configuration entries in
``.thoth.yaml`` file:

.. code-block:: yaml

  host: {THOTH_SERVICE_HOST}
  tls_verify: true
  requirements_format: pipenv

  runtime_environments:
    - name: 'cuda'  # <<<
      operating_system:
        name: fedora
        version: '32'
      hardware:
        cpu_family: 6
        cpu_model: 94
      python_version: '3.8'
      cuda_version: '10.1'  # <<<
      recommendation_type: stable
      platform: 'linux-x86_64'

    - name: 'no_cuda'  # <<<
      operating_system:
        name: fedora
        version: '32'
      hardware:
        cpu_family: 6
        cpu_model: 94
      python_version: '3.8'
      cuda_version: null  # <<<
      recommendation_type: stable
      platform: 'linux-x86_64'

The two runtime environments stated in the ``.thoth.yaml`` differ in
``cuda_version`` configuration and their names.

To trigger advises for runtime environment named ``cuda``, issue:

.. code-block:: console

  thamos advise --runtime-environment cuda

To target the latter runtime environment named ``no_coda``, you can issue:

.. code-block:: console

  thamos advise --runtime-environment no_cuda

This option can be also supplied via environment variable using
``THAMOS_RUNTIME_ENVIRONMENT=no_cuda``.

If the runtime environment is not provided explictly, Thamos will take the
first runtime environment entry stated in the ``runtime_environment`` listing.
For the example showed above it will default to ``cuda`` environment:

.. code-block:: console

  # defaults to the first one - "cuda"
  thamos advise

Multiple runtime environments can be used in conjunction with the automatically
expanded configuration options and configuration file templating naturally.

Using Thoth and thamos in OpenShift's s2i
=========================================

Using configuration templates is especially useful for OpenShift builds where
you can specify your template in an s2i repository (omit ``Pipfile.lock`` to
enable call to ``thamos advise`` as shown in `this repository
<https://github.com/thoth-station/s2i-example-tensorflow>`_).

Then, you need to provide following environment variables:

* ``THAMOS_CONFIG_TEMPLATE`` - holds path to template - use ``/tmp/src`` prefix to point to root of s2i repository (e.g. ``/tmp/src/template.yaml`` if ``template.yaml`` is the configuration template and is stored in root of your Git repository).
* ``THAMOS_NO_INTERACTIVE`` - set to `1` if you don't want to omit interactive thamos (suitable for automated s2i builds happening in the cluster).
* ``THAMOS_NO_PROGRESSBAR`` - set to `1` to disable progressbar while waiting for response from Thoth backend - it can cause annoying too verbose output printed to OpenShift console during the build.
* ``THAMOS_CONFIG_EXPAND_ENV`` - set to `1` to enable expansion based on environment variables when generating ``.thoth.yaml`` file - this needs to be explicitly turned on due to possible security implications.
* ``THAMOS_FORCE`` - set to `1` not use cached results, always force analysis on Thoth's side (note this option can be ignored by a Thoth operator based on deployment configuration).
* ``THAMOS_VERBOSE`` - set to `1` to run thamos in verbose mode to show what's going on (verbosity on client side).
* ``THAMOS_DEBUG`` - set to `1` to run analyzes (adviser, provenance checker, ...) on Thoth's backend side in debug mode, you can obtain logs by running ``thamos logs`` or directly on Thoth's user API; the analysis id gets printed into the console during the build process in OpenShift (verbosity on server side).
* ``THAMOS_DEV`` - set to `1` to consider also development dependencies, this flag defaults to `0` - by enabling development dependencies, adviser will need to browse larger space of software stacks possibly ending with a worse software stack advised (development dependencies are usually not used during application deployment)
* ``THAMOS_DISABLE_CUDA`` - set to `1` to disable CUDA detection
* ``THAMOS_NO_EMOJI`` - set to `1` to disable UTF-8 emojis (useful for dummy terminals)
* ``THAMOS_RETRY_ON_ERROR_COUNT`` - number of retries performed if the API server is responding with an error HTTP status (defaults to 3), this option is not usually needed to be adjusted
* ``THAMOS_RETRY_ON_ERROR_SLEEP`` - sleep time when an error on the API server is spotted (see ``THAMOS_RETRY_ON_ERROR_COUNT``), defaults to 3 seconds
* ``THAMOS_NO_PROGRESSBAR`` - disable progress bar visualization, useful for dummy terminals
* ``THAMOS_TIMEOUT`` - timeout period in seconds after which Thamos stops trying to fetch results
* ``THAMOS_DISABLE_LAST_ANALYSIS_ID_FILE`` - set to `1`  if you do not want to create a file that states last analysis id (used not to memorize the last analysis id across commands)
* ``THAMOS_REQUIREMENTS_FORMAT`` - style of requirements used for managing dependencies - one of ``pip``, ``pip-tools``, ``pipenv``, defaults to ``pipenv`` if not specified

See `OpenShift s2i documentation
<https://docs.openshift.com/container-platform/3.9/dev_guide/builds/advanced_build_operations.html#dev-guide-assigning-builds-to-nodes>`_
on how to pin build to a specific node in the cluster. This is needed if you
would like to perform automatic hardware discovery to get optimized stacks on
your hardware.

Using Thamos as a library
=========================


.. code-block:: python

   from thamos.lib import image_analysis
   from thamos.config import config

   # Set global context.
   # Host to Thoth's User API. API discovery will be done
   # transparently and the most appropriate API version will be used.
   config.explicit_host = "thoth-user-api.redhat.com"
   # TLS verification when communicating with Thoth API.
   config.tls_verify = True

   image_analysis(
     image="registry.redhat.com/fedora:29",
     registry_user="fridex",
     registry_password="secret!",
     # TLS verification when communicating with registry.
     verify_tls=True,
     nowait=False
   )

Disabling TLS related warnings
==============================

If you communicate with Thoth's user API without TLS (you have set the
``tls_verify`` configuration option to ``false`` in the ``.thoth.yaml`` file),
Thamos CLI and Thamos library issue a warning each time there is done
communication with the API server. To suppress this warning, set the
``THAMOS_DISABLE_TLS_WARNING`` environment variable to a non-zero value:

.. code-block:: console

  $ export THAMOS_DISABLE_TLS_WARNING=1
  $ thamos advise

Autogenerated client from OpenAPI
=================================

Most parts of Thamos consist of automatic generated code. You can update Thamos
by running the following command:

.. code-block:: console

  $ ./swagger-codegen.sh

The command above will download and run automatic code generation tool against
the most recent OpenAPI specification of `User API
<https://github.com/thoth-station/user-api/>`_. Results of the tool are
automatically placed into this repository in `thamos/swagger_client/` and
`Documentation/`. They consist of automatically generated code as well as
`documentation on how to use the code
<https://github.com/thoth-station/thamos/tree/master/Documentation>`_.  Thamos
itself provides routines built on top of this automated generated code to
simplify usage in ``thamos/lib``.
