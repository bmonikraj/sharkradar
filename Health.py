import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opr(__file__))
sys.path.append(basedir)


class Health:
	"""
		Class for health check of micro-services
	"""

	@staticmethod
	def health(req_body):
		"""
			Function to register, unregister, send health report of micro-services to Service R/D
			@params: req_body: A json body containing the following key-value pairs about a micro-service.
							     KEYS:            VALUES:
							   ---------        -------------
							  i) ip 			  ip address associated with micro-service
							 ii) port			  port associated with micro-service
							iii) service_name	  unique name of the micro-service
							 iv) status			  status (up/down) sent from the micro-service
							  v) health_interval  The time interval specified by the micro-service at which it will send health report to service R/D continuously
			@return: True | False
		"""
		ip = req_body['ip']
		port = req_body['port']
		service_name = req_body['service_name']
		status = req_body['status']
		health_interval = req_body['health_interval']
		current_time_stamp = req_body['current_timestamp']

		if(service_name and ip and port):
			if(status == "up" ):
				# check in db for the record with the given service name
				cursor = conn.execute("SELECT * from SERVICE_RD WHERE SERVICE_NAME ="+ service_name + " AND IP = "+ ip +" PORT = "+ port);
				if(cursor.length > 0):
					#update report_time_stamp and health_interval in db
					conn.execute("UPDATE SERVICE_RD SET TIME_STAMP = current_time_stamp, HEALTH_INTERVAL = "+ health_interval +" WHERE SERVICE_NAME ="+ service_name + " AND IP = "+ ip +" PORT = "+ port);
					conn.commit()
					if(conn.total_changes > 0):
						return True
					else:
						return False
				else:
					#insert a record in db with all 5 parameters
					conn.execute("INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL) \
      				VALUES (service_name, ip, port, "+ current_time_stamp +", health_interval)");
					conn.commit()
					return True
		
			else:
				#If status == down, delete the record with given service_name, ip and port
				conn.execute("DELETE FROM SERVICE_RD WHERE SERVICE_NAME ="+ service_name + " AND IP = "+ ip +" PORT = "+ port);
				conn.commit()
				return True

				
		else:
			return False



