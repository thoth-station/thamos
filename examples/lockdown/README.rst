A lockdown example for Thoth
----------------------------

Please follow instructions in `the relvant Jupyter Notebook
<https://github.com/thoth-station/notebooks/blob/master/notebooks/Thoth%200.5.0%20-%20Example%201%20Guided%20Notebook.ipynb>`_.
If you would like to try this scenario with Thamos CLI, run the following
commands:

.. code-block:: console

  # Make sure you have Thamos CLI and Pipenv installed:
  pip3 install --user thamos

  # Clone this repository so you have examples directory present:
  git clone https://github.com/thoth-station/thamos.git

  # Go to lockdown example:
  cd thamos/examples/lockdown/

  # Browse the content of the lockdown example, see relevant files:
  ls -a  # See .thoth.yaml configuration file, Pipfile and hello.py present
  cat .thoth.yaml Pipfile hello.py

  # Ask Thoth for advises, Thoth will respect .thoth.yaml configuration file
  # and your Pipfile and bring you Pipfile.lock:
  thamos advise

  # Check pinned down software stack in Pipfile.lock (previously this file was
  # not present):
  cat Pipfile.lock

  # Verify the recommended stack works by installing the stack and running
  # provided example application:
  pip3 install --user pipenv
  pipenv install
  FLASK_APP=hello.py pipenv run flask run


**Note:** You need to be connected to Red Hat VPN as Thoth is currently hosted internally only.

