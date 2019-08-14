"""
API endpoints definition related functions for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os
import time
import json
from flask import Flask, request

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Util import sharkradarDbutils
from sharkradar.Service.Health import Health
from sharkradar.Service.Discovery import Discovery

sharkradarDbutils.createTableIfNotExists()
app = Flask(__name__)


@app.route("/health", methods=['PUT'])
def health():
    """
        API Endpoint to send health report of micro-services to Service R/D
        @method: PUT
        @params: A json body containing the following key-value pairs about a micro-service.
                     KEYS:                  VALUES:
               ---------            -------------
              i) ip                 ip address associated with micro-service
             ii) port               port associated with micro-service
            iii) service_name       unique name of the micro-service (But same for all instances of same microservice)
             iv) status             status (up/down) sent from the micro-service
              v) mem_usage          Current memory usage in %
             vi) cpu_usage          Current CPU usage in %
            vii) nw_tput_bw_ratio   Current network throughput in %
            viii) req_active_ratio  No. of requests currently being processed / Max.
                                    no. of request can be processed in %
             ix) success_rate       Fraction of requests successfully served in %
              x) health_interval    The time interval in seconds specified by the micro-service
                                    at which it will send health report to service
                                    R/D continuously
        @return: {"status" : "<BOOL>"} <BOOL>=True|False
    """
    response_objects = {"status": "False"}
    try:
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
    except Exception as e:
        return json.dumps(response_objects)


@app.route("/discovery/<service_name>", methods=['GET'])
def discovery(service_name):
    """
        API endpoint to fetch address of a service based on service name
        @method: GET
        @params: service_name (String)
        @return : {"ip" : "<value>", "port" : "<value>"}
    """
    response_objects = {"ip": "", "port": ""}
    respTuple = Discovery.discovery(service_name)
    response_objects["ip"] = respTuple[0]
    response_objects["port"] = respTuple[1]
    return json.dumps(response_objects)
