A lockdown example for Thoth
----------------------------

Please follow instructions in `the relvant Jupyter Notebook
<https://github.com/thoth-station/notebooks/blob/master/notebooks/Thoth%200.5.0%20-%20Example%201%20Guided%20Notebook.ipynb>`_.
If you would like to try this scenario with Thamos CLI, run the following
commands:

.. code-block:: console

  # Make sure you have Thamos CLI installed:
  pip3 install --user thamos

  # Clone this repository so you have examples directory present:
  git clone https://github.com/thoth-station/thamos.git

  # Go to lockdown example:
  cd thamos/examples/lockdown/

  # Browse the content of the lockdown example, see relevant files;
  # see .thoth.yaml configuration file, Pipfile and hello.py present:
  ls -a
  cat .thoth.yaml Pipfile hello.py

  # Ask Thoth for advises, Thoth will respect .thoth.yaml configuration file
  # and your Pipfile and recommend you Pipfile.lock:
  thamos advise

  # Check pinned down software stack in Pipfile.lock (previously this file was
  # not present):
  cat Pipfile.lock

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
  FLASK_APP=hello.py pipenv run flask run


**Note:** You need to be connected to Red Hat VPN as Thoth is currently hosted internally only.

