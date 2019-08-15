"""
Discovery related functions for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os
import sqlite3

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Util import sharkradarDbutils

class Health:
    """Class for health check of micro-services """

    @staticmethod
    def health(req_body):
        """
        Function to register, unregister, send health report of micro-services to Service R/D
        @params: req_body: A json body containing the following key-value pairs about a micro-service.
                     KEYS:            		VALUES:
               ---------        	-------------
              i) ip 			  	ip address associated with micro-service
             ii) port			  	port associated with micro-service
            iii) service_name	  	unique name of the micro-service
             iv) status			  	status (up/down) sent from the micro-service
              v) mem_usage		  	Current memory usage in %
             vi) cpu_usage		  	Current CPU usage in %
            vii) nw_tput_bw_ratio 	Current network throughput in %
       		viii) req_active_ratio 	No. of requests currently being processed / Max.
                                    no. of request can be processed in %
             ix) success_rate 		Fraction of requests successfully served in %
              x) health_interval  	The time interval in seconds specified by the micro-service
                                    at which it will send health report to service
                                    R/D continuously
             xi) current_time_stamp Current time stamp of receiving request
        @return: True | False
        """
        if (
            'ip' not in req_body.keys()) or (
            'port' not in req_body.keys()) or (
            'service_name' not in req_body.keys()) or (
                'mem_usage' not in req_body.keys()) or (
                    'cpu_usage' not in req_body.keys()) or (
                        'nw_tput_bw_ratio' not in req_body.keys()) or (
                            'req_active_ratio' not in req_body.keys()) or (
                                'status' not in req_body.keys()) or (
                                    'success_rate' not in req_body.keys()) or (
                                        'health_interval' not in req_body.keys()):
            return False

        ip = req_body['ip']
        port = req_body['port']
        service_name = req_body['service_name']
        status = req_body['status']
        mem_usage = round(float(req_body['mem_usage']), 2)
        cpu_usage = round(float(req_body['cpu_usage']), 2)
        nw_tput_bw_ratio = round(float(req_body['nw_tput_bw_ratio']), 2)
        req_active_ratio = round(float(req_body['req_active_ratio']), 2)
        success_rate = round(float(req_body['success_rate']), 2)
        health_interval = int(req_body['health_interval'])
        current_time_stamp = int(req_body['current_timestamp'])

        if(
        	(mem_usage >= 0.0 and mem_usage <= 100.0) and (
        		cpu_usage >= 0.0 and cpu_usage <= 100.0) and (
        		nw_tput_bw_ratio >= 0.0 and nw_tput_bw_ratio <= 100.0) and (
        		req_active_ratio >= 0.0 and req_active_ratio <= 100.0) and (
        		success_rate >= 0.0 and success_rate <= 100.0)):
            if(service_name != "" and ip != "" and port != ""):
                if status == "up":
                    response = sharkradarDbutils.findServiceByNameAndIpAndPort(
                        service_name, ip, port)
                    if len(response) > 0:
                        total_changes = sharkradarDbutils.updateServiceByAll(
                            current_time_stamp,
                            health_interval,
                            mem_usage,
                            cpu_usage,
                            nw_tput_bw_ratio,
                            req_active_ratio,
                            success_rate,
                            service_name,
                            ip,
                            port)
                        if total_changes > 0:
                            return True
                        return False
                    sharkradarDbutils.insertServiceByAll(
                        service_name,
                        ip,
                        port,
                        current_time_stamp,
                        health_interval,
                        mem_usage,
                        cpu_usage,
                        nw_tput_bw_ratio,
                        req_active_ratio,
                        success_rate)
                    return True
                sharkradarDbutils.deleteServiceByNameAndIpAndPort(
                    service_name, ip, port)
                return True
            return False
        return False
