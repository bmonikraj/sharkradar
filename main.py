#!/usr/bin/python
import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(basedir)
from flask import Flask


import sqlite3

conn = sqlite3.connect('radar-service.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE SERVICE_RD
         (ID INT PRIMARY KEY     NOT NULL,
         SERVICE_NAME  TEXT    NOT NULL,
         IP            TEXT     NOT NULL,
         PORT          TEXT NOT NULL,
         TIME_STAMP     TIMESTAMP NOT NULL
         HEALTH_INTERVAL TEXT NOT NULL);''')

app = Flask(__name__)

from Health import Health
from Discovery import Discovery

@app.route("/health/<json_object>", methods=['PUT'])
def health():
  Health.health(json_object)


@app.route("/discovery/<service_name>", methods = ['GET'])
def discovery(service_name):
	Discovery.discovery(service_name)


if __name__ == '__main__':
   app.run(debug = True)

	