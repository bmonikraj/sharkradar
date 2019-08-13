import sys
from os.path import dirname as opd, realpath as opr
import os
import time
import sqlite3

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)

DB_PATH = './sharkradar-service.db'


def createTableIfNotExists():
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
               viii) req_active 		No. of requests currently being processed by
                                                                    the instance
                     ix) success_rate 		Fraction of requests successfully served
                      x) health_interval  	The time interval specified by the micro-service
                                                                    at which it will send health report to service
                                                                    R/D continuously
    """
    conn = sqlite3.connect(DB_PATH)
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


def findServiceByNameAndIpAndPort(service_name, ip, port):
    conn = sqlite3.connect(DB_PATH)
    response = conn.execute(
        """SELECT * FROM SERVICE_RD WHERE SERVICE_NAME = ? AND IP = ? AND PORT = ?""",
        (service_name,
         ip,
         port)).fetchall()
    conn.close()
    return response


def findServiceByName(service_name):
    conn = sqlite3.connect(DB_PATH)
    service_instances = conn.execute(
        """SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
        (service_name,
         )).fetchall()
    conn.close()
    return service_instances


def updateServiceByAll(
        current_time_stamp,
        health_interval,
        mem_usage,
        cpu_usage,
        nw_tput_bw_ratio,
        req_active_ratio,
        success_rate,
        service_name,
        ip,
        port):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """UPDATE SERVICE_RD SET  TIME_STAMP = ?, HEALTH_INTERVAL = ?, MEM_USAGE = ?, CPU_USAGE = ?, NW_TPUT_BW_RATIO = ?, REQ_ACTIVE_RATIO = ?, SUCCESS_RATE = ?  WHERE SERVICE_NAME = ? AND IP = ? AND PORT = ?""",
        (current_time_stamp,
         health_interval,
         mem_usage,
         cpu_usage,
         nw_tput_bw_ratio,
         req_active_ratio,
         success_rate,
         service_name,
         ip,
         port))
    conn.commit()
    total_changes = conn.total_changes
    conn.close()
    return total_changes


def insertServiceByAll(
        service_name,
        ip,
        port,
        current_time_stamp,
        health_interval,
        mem_usage,
        cpu_usage,
        nw_tput_bw_ratio,
        req_active_ratio,
        success_rate):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (service_name,
         ip,
         port,
         current_time_stamp,
         health_interval,
         mem_usage,
         cpu_usage,
         nw_tput_bw_ratio,
         req_active_ratio,
         success_rate))
    conn.commit()
    conn.close()


def deleteServiceByNameAndIpAndPort(service_name, ip, port):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ? AND IP = ? AND PORT = ?""",
        (service_name,
         ip,
         port))
    conn.commit()
    conn.close()


def deleteServiceByNameAndTimestampDifferenceWithHealthInterval(service_name):
    conn = sqlite3.connect(DB_PATH)
    current_time_epoch = time.time()
    conn.execute(
        """DELETE FROM SERVICE_RD WHERE SERVICE_NAME  = ? AND ?  - TIME_STAMP > HEALTH_INTERVAL""",
        (service_name,
         current_time_epoch))
    conn.commit()
    conn.close()
