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
    response_objects = {"ip": "", "port": ""}
    respTuple = Discovery.discovery(service_name)
    response_objects["ip"] = respTuple[0]
    response_objects["port"] = respTuple[1]
    return json.dumps(response_objects)
