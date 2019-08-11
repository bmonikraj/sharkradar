#!/usr/bin/python
import sys
from os.path import dirname as opd, realpath as opr
import os
import time
import json

basedir = opd(opr(__file__))
sys.path.append(basedir)

from flask import Flask, request

import sqlite3

conn = sqlite3.connect('./radar-service.db')

"""
Columns of Table
    	KEYS:            		VALUES:
	   ---------        	-------------
	  i) ip 			  	ip address associated with micro-service
	 ii) port			  	port associated with micro-service
	iii) service_name	  	unique name of the micro-service
	 iv) status			  	status (up/down) sent from the micro-service
	  v) mem_usage		  	Current memory usage
	 vi) cpu_usage		  	Current CPU usage
	vii) network_throughput Current network throughput 
   viii) req_active 		No. of requests currently being processed by the instance
   	 ix) success_rate 		Fraction of requests successfully served
	  x) health_interval  	The time interval specified by the micro-service at which it will send health report to service R/D continuously
"""
conn.execute('''CREATE TABLE IF NOT EXISTS SERVICE_RD
         (SERVICE_NAME  TEXT    NOT NULL,
         IP            TEXT     NOT NULL,
         PORT          TEXT NOT NULL,
         MEM_USAGE     	REAL NOT NULL,
         CPU_USAGE      REAL NOT NULL,
         NW_TPUT_BW_RATIO REAL NOT NULL,
         REQ_ACTIVE_RATIO REAL NOT NULL,
         SUCCESS_RATE REAL NOT NULL,
         TIME_STAMP     BIGINT NOT NULL,
         HEALTH_INTERVAL BIGINT NOT NULL);''')

conn.commit()
conn.close()

app = Flask(__name__)

from Health import Health
from Discovery import Discovery

@app.route("/health", methods=['PUT'])
def health():
	response_objects = {"status" : "False"}
	json_object = {}
	json_object['ip'] = request.form['ip']
	json_object['port'] = request.form['port']
	json_object['service_name'] = request.form['service_name']
	json_object['status'] = request.form['status']
	json_object['mem_usage'] = request.form['mem_usage']
	json_object['cpu_usage'] = request.form['cpu_usage']
	json_object['nw_tput_bw_ratio'] = request.form['nw_tput_bw_ratio']
	json_object['req_active_ratio'] = request.form['req_active_ratio']
	json_object['success_rate'] = request.form['success_rate']
	json_object['health_interval'] = request.form['health_interval']
	json_object['current_timestamp'] = time.time()
	respBool = Health.health(json_object)
	if respBool:
		response_objects["status"] = "True"
		return json.dumps(response_objects)
	return json.dumps(response_objects)


@app.route("/discovery/<service_name>", methods = ['GET'])
def discovery(service_name):
	response_objects = {"ip" : "", "port" : ""}
	respTuple = Discovery.discovery(service_name)
	if(respTuple[0]=="" and respTuple[1]==""):
		return json.dumps(response_objects)
	response_objects["ip"] = respTuple[0]
	response_objects["port"] = respTuple[1]
	return json.dumps(response_objects)


	