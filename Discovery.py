import sys
from os.path import dirname as opd, realpath as opr
import os
import time
basedir = opd(opr(__file__))
sys.path.append(basedir)
import sqlite3

class Discovery:
	"""
		Class for fetching details of a micro-service
	"""
	@staticmethod
	def discovery(service_name):
		"""
			Function to fetch details of a micro-services from Service R/D
			@params: service_name: Unique service name of the micro-service

			@return: A tuple containing ip and port of the active micro-service instance
		"""
		#delete all services with given service name and whose reporting time deadline is over
		
		conn = sqlite3.connect('./radar-service.db')
		current_time_epoch = time.time()
		conn.execute("""DELETE FROM SERVICE_RD WHERE SERVICE_NAME  = ? AND ?  - TIME_STAMP > HEALTH_INTERVAL""", (service_name, current_time_epoch))
		conn.commit()

		#find all row from database with given service name 
		service_instances = conn.execute("""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""", (service_name, )).fetchall()
		conn.close()

		len_ = len(service_instances)

		#weights assigned to different parameters
		mem_usage_wt = 4.0
		cpu_usage_wt = 4.0
		nw_tput_bw_ratio_wt = 3.0
		req_active_ratio_wt = 2.0
		success_rate_wt = 1.0
		sum_of_weights = 100.00*(mem_usage_wt + cpu_usage_wt + nw_tput_bw_ratio_wt + req_active_ratio_wt + success_rate_wt)
		
		priority_list = []
		if len_ > 0:
			#PRIORITY BASED ALGO
			for i in range(0, len_):

				single_instance = {}
				single_instance['ip'] = service_instances[i][1]
				single_instance['port'] = service_instances[i][2]

				score = 0.0
				score = float(nw_tput_bw_ratio_wt*service_instances[i][5] + success_rate_wt*service_instances[i][7] + mem_usage_wt*(100.00 - service_instances[i][3]) + cpu_usage_wt*(100.00 - service_instances[i][4]) + req_active_ratio_wt*(100.00 - service_instances[i][6]))
				score = float(score/sum_of_weights)
				single_instance['score'] = score
				priority_list.append(single_instance)
			priority_list.sort(key = lambda x: x['score'], reverse = True)
			res = priority_list[0]
			res_tuple = (str(res['ip']), str(res['port']))
			return res_tuple

		else:
			return ("", "")

		 


