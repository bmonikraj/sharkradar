#!/usr/bin/python
import sys
from os.path import dirname as opd, realpath as opr
import os
import time

basedir = opd(opr(__file__))
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

@app.route("/health", methods=['PUT'])
def health():
	json_object = request.form['request_body']
	json_object['current_timestamp'] = time.time()
	# json_object['ip'] = request.form['ip']
	# json_object['port'] = request.form['port']
	# json_object['service_name'] = request.form['service_name']
	# json_object['status'] = request.form['status']
	# json_object['health_interval'] = request.form['health_interval']
	return Health.health(json_object)


@app.route("/discovery/<service_name>", methods = ['GET'])
def discovery(service_name):
	return Discovery.discovery(service_name)


if __name__ == '__main__':
   app.run(debug = True)

	