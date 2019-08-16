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
from sharkradar.Util import sharkradarAlgorithmutils
from sharkradar.Config.Config import Config

class Discovery:
	"""Class for fetching details of a micro-service """
	
	@staticmethod
	def discovery(service_name):
		"""
		Function to fetch details of a micro-services from Service R/D

		@params: service_name: Unique service name of the micro-service
		@return: A tuple containing ip and port of the active micro-service instance
		"""
		sharkradarDbutils.deleteServiceByNameAndTimestampDifferenceWithHealthInterval(
			service_name)
		service_instances = sharkradarDbutils.findServiceByName(service_name)	
		if len(service_instances) > 0:
			if Config.getAlgorithm() == "wpmc":
				ip, port = sharkradarAlgorithmutils.weightedPriorityMemAndCPU(service_instances)
				return (ip, port)
			if Config.getAlgorithm() == "wprs":
				ip, port = sharkradarAlgorithmutils.weightedPriorityReqActiveAndSuccessRate(service_instances)
				return (ip, port)
		return ("", "")
