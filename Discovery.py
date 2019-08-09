import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(basedir)


class Discovery:
	"""
		Class for fetching details of a micro-service
	"""
	@staticmethod
	def discovery(service_name):
		"""
			Function to fetch details of a micro-services from Service R/D
			@params: service_name: Unique name of the micro-service

			@return: A json object containing ip and port of the active micro-service instance
		"""
		#find all row from database with given service name 
		conn.execute("DELETE FROM SERVICE_RD WHERE SERVICE_NAME ="+ service_name + " AND " + CURRENT_TIMESTAMP() - int(TIME_STAMP) < int(HEALTH_INTERVAL));
		conn.commit()
		service_instances = conn.execute("SELECT * from SERVICE_RD WHERE SERVICE_NAME ="+ service_name);
		
		if service_instances.length > 0:
			#ROUND ROBIN ALGO

		else:
			return ("", "")

		 


