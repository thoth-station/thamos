Thamos
------

A CLI tool and library for communicating with Thoth backend.


Using Thamos as a CLI tool
==========================

Thamos is released on `PyPI <https://pypi.org/project/thamos>`_. See
installation instructions bellow to setup Thoth/Thamos for your repository:

.. code-block:: console

  # Install Thamos CLI tool:
  $ pip3 install thamos
  # Go to repository that should be managed by Thoth:
  $ cd ~/git/repo/
  # Setup Thamos configuration:
  $ thamos config
  # Ask Thoth for software stack recommendations:
  $ thamos advise


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

