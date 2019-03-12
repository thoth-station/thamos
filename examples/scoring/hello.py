#!/usr/bin/env python3

"""An example flask server for Thoth scoring example."""

from flask import Flask
from flask import __version__ as FLASK_VERSION
from yaml import __version__ as PYYAML_VERSION

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a hello string with Flask and YAML versions.."""
    msg = "Hello, Thoth! I'm using Flask in version %r and PyYaml in version %r" % (
        FLASK_VERSION,
        PYYAML_VERSION,
    )
    return msg
