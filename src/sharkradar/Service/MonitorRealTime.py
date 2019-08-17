"""
Real time monitor of services
"""
import sys
from os.path import dirname as opd, realpath as opr
import os
import sqlite3
import time
import random

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

from sharkradar.Util import sharkradarDbutils
from sharkradar.Config.Config import Config

class MonitorRealTime:
	"""Class for fetching details of all micro-service """
	
	@staticmethod
	def getAllServices():
		"""
		Function to fetch details of a micro-services from Service R/D

		@return: List of all service instances
		"""
		services = sharkradarDbutils.getAllService()
		for i in range(0, len(services)):
			instance = {}
			instance["service_name"] = str(services[i][0])
			instance["ip"] = str(services[i][1])
			instance["port"] = str(services[i][2])
			instance["mem_usage"] = str(services[i][3])
			instance["cpu_usage"] = str(services[i][4])
			instance["nw_tput_bw_ratio"] = str(services[i][5])
			instance["req_active_ratio"] = str(services[i][6])
			instance["success_rate"] = str(services[i][7])
			instance["health_interval"] = str(services[i][8])
			instance["current_timestamp"] = str(services[i][9])
			services[i] = instance
		return services
