A runtime environment advises in Thoth
--------------------------------------

Please follow instructions in `the relvant Jupyter Notebook
<https://github.com/thoth-station/notebooks/blob/master/notebooks/v0.5.0/Example%202%20Guided%20Notebook%20-%20runtime-environment.ipynb>`_.
If you would like to try this scenario with Thamos CLI, run the following
commands:

.. code-block:: console

  # Make sure you have Thamos CLI installed:
  pip3 install --user thamos

  # Clone this repository so you have examples directory present:
  git clone https://github.com/thoth-station/thamos.git

  # Go to runtimme-environment example:
  cd thamos/examples/runtime-environment/

  # Browse the content of the runtime-environment example, see relevant
  # files; see .thoth.yaml configuration file, Pipfile Pipfile.lock
  # and hello.py present:
  ls -a
  cat .thoth.yaml Pipfile Pipfile.lock hello.py

  # Ask Thoth for advises, Thoth will respect .thoth.yaml configuration file
  # and your Pipfile and recommend you Pipfile.lock. Pipfile.lock is sent with
  # the request to capture user's stacks:
  thamos advise

  # Check pinned down software stack in Pipfile.lock, also check Pipfile and pinned
  # down Python version to make sure your application runs on desired Python version.
  cat Pipfile.lock
  cat Pipfile
  # Note the TensorFlow build installed from AICoE index - an optimized TensorFlow
  # version for your environment as specified in .thoth.yaml.
  cat Pipfile  # see requires section

  # You can browse adviser logs if you would like to have more info
  # on what has been done on the background, the $ADVISER_ANALYSIS_ID is
  # reported by `thamos advise` command above, if you did not capture it, feel
  # free to rerun `thamos advise --no-wait` which will report back analysis id
  # without waiting the analysis to be finished (there will be used cached
  # results from the previous run based on cache configuration on Thoth backend):
  ADVISER_ANALYSIS_ID=`thamos advise --no-wait`
  thamos log $ADVISER_ANALYSIS_ID

  # Verify the recommended stack works by installing the stack and running
  # provided example application:
  pip3 install --user pipenv
  pipenv install
  pipenv run python3 ./hello.py


To automatically obtain information about your environment, run the following
Thamos commands before `pipenv install`:

.. code-block:: console

  # Or export THAMOS_NO_INTERACTIVE=1
  thamos config --no-interactive
  thamos advise
  pipenv install

**Note:** You need to be connected to Red Hat VPN as Thoth is currently hosted internally only.
