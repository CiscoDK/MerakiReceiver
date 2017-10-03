
"""
Module Docstring
"""
from flask import *
import sys
import click
import datetime
import os # For enviroment stuff on Azure..

import sqlite3



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
            f.write('%s: %s \n\r' % (datetime.datetime.now(), txt))
        finally:
            f.close()


### Main entry point


print("Print from MerakiReceiver")
writelog("Log from MerakiReceiver")
sys.stdout.flush()
app.logger.info("Launching MerakiReceiver")
app.logger.debug("Secret key: " + app.config.get("SECRET_MERAKI_KEY"))





@app.route("/data/", methods=["GET","POST"])
def main():
    """ Main entry point of the app """
    logger.info("hello world")

    if request.method == 'POST':
        #logger.info(request.form['apMac'])
        app.logger.info("Got POST")
        a = request.get_json()
        writelog(a)
        print(json.dumps(a,indent=4))

        if a["type"] == "DevicesSeen": #WiFi (e.g. not BT)
            print(a["secret"])
            writelog(a["secret"])

            conn = sqlite3.connect('MerakiReceiver.db')
            c = conn.cursor()

            for o in a["data"]["observations"]:
                c.execute("INSERT INTO RawData VALUES ('" + a["data"]["apMac"] + "','"+ o["seenTime"] +"','"+ o["clientMac"] +"','"+ str(o["rssi"]) +"')")



            conn.commit()
            print(a["data"]["apMac"])

            conn.close()

        return "OK"

    elif request.method == 'GET':
        #return "Hello from the App"
        return app.config.get("SECRET_MERAKI_KEY")

@app.cli.command()
#@click.argument('secret')
def initdb():
    conn = sqlite3.connect('MerakiReceiver.db')

    c = conn.cursor()
    c.execute('''CREATE TABLE RawData
                 (apMac text, seenTime text, clientMac text, rssi real)''')

    conn.commit()

    conn.close()


if __name__ == "__main__":
    #app.run()
    #### THIS IS NOT EXECUTED WHEN RUNNING FROM FLASK LOCAL?!!!

    print("EXECUTED STANDALONE")
    #main()