
"""
Module Docstring
"""
from flask import *
import sys
import click
import datetime
import os # For enviroment stuff on Azure..




__author__ = "Nicholas Swiatecki"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import requests

app = Flask(__name__)
app.config.from_pyfile('MerakiReceiver.settings')






def writelog(txt):
    """Logs fatal errors to a log file if WSGI_LOG env var is defined"""
    log_file = os.environ.get('NS_LOG')
    if log_file:
        f = open(log_file, 'a+')
        try:
            f.write('%s: %s' % (datetime.datetime.now(), txt))
        finally:
            f.close()


### Main entry point


print("Print from MerakiReceiver")
writelog("Log from MerakiReceiver")
sys.stdout.flush()
app.logger.info("Launching MerakiReceiver")
app.logger.debug("Secret key: " + app.config.get("SECRET_MERAKI_KEY"))





@app.route("/", methods=["GET","POST"])
def main():
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info("Secret is " + "bla")


    if request.method == 'POST':
        logger.info(request.form['apMac'])
        writelog(request.form['apMac'])

        return "OK"
    elif request.method == 'GET':
        return "Hello from the App"

#@app.cli.command()
#@click.argument('secret')
#def start():
 #   pass

if __name__ == "__main__":
    #app.run()
    #### THIS IS NOT EXECUTED WHEN RUNNING FROM FLASK LOCAL?!!!

    print("Run via flask")
    sys.stdout.flush()
    #main()