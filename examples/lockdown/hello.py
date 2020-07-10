# Commands to make this work with Thoth (in the same directory as this file):
#
#   thamos advise
#   pipenv install
#   FLASK_APP=hello.py pipenv run flask run
#
"""An example flask server for Thoth."""

from flask import Flask
import tensorflow as tf

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a hello string."""
    hello = tf.constant("Hello, TensorFlow!")
    sess = tf.Session()
    return sess.run(hello)
