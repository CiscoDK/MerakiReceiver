
"""
Module Docstring
"""
from flask import *
import sys
import click



__author__ = "Nicholas Swiatecki"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import requests

app = Flask(__name__)
app.config.from_pyfile('MerakiReceiver.settings')

app.logger.info("Launching MerakiReceiver")
app.logger.debug("Secret key: " + app.config.get("SECRET_MERAKI_KEY"))
#app.config['secret'] = sys.argv[0]
#@app.cli.command()

@app.route("/", methods=["GET","POST"])
def main():
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info("Secret is " + "bla")


    if request.method == 'POST':
        logger.info(request.form['apMac'])

        return "OK"
    elif request.method == 'GET':
        return ""

@app.cli.command()
@click.argument('secret')
def start():
    pass

if __name__ == "__main__":
    #### THIS IS NOT EXECUTED WHEN RUNNING FROM FLASK!!!

    print("Run via flask")
    #main()