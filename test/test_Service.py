import time
import sqlite3
import json
import pytest
import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(os.path.join(basedir, "src"))

from sharkradar.Service.Discovery import Discovery
from sharkradar.Service.Health import Health
from sharkradar.Service.MonitorRealTime import MonitorRealTime
from sharkradar.Util import sharkradarDbutils
from sharkradar.Config.Config import Config


TEST_PARAMS = {
	"SERVICE_NAME_UNREGISTERED": "unregistered",
	"health_object_1": {
		"ip": "102.15.64.78",
		"port": "8079",
		"service_name": "test_service_1",
		"status": "up",
				"mem_usage": "91.2",
				"cpu_usage": "94.4",
				"nw_tput_bw_ratio": "70.1",
				"req_active_ratio": "48.1",
				"success_rate": "50.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_2": {
		"ip": "102.15.64.74",
		"port": "8079",
		"service_name": "test_service_2",
		"status": "up",
				"mem_usage": "41.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_2_down": {
		"ip": "102.15.64.74",
		"port": "8079",
		"service_name": "test_service_2",
		"status": "down",
				"mem_usage": "41.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_2_updated": {
		"ip": "102.15.64.74",
		"port": "8079",
		"service_name": "test_service_2",
		"status": "up",
				"mem_usage": "61.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_3_a": {
		"ip": "102.25.64.74",
		"port": "8079",
		"service_name": "test_service_3",
		"status": "up",
				"mem_usage": "41.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_3_b": {
		"ip": "102.25.64.75",
		"port": "8079",
		"service_name": "test_service_3",
		"status": "up",
				"mem_usage": "21.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_4": {
		"ip": "102.25.64.75",
		"port": "8072",
		"service_name": "test_service_4",
		"status": "up",
				"mem_usage": "21.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "11",
				"current_timestamp": time.time()
	},
	"health_object_5_a": {
		"ip": "102.25.64.75",
		"port": "8272",
		"service_name": "test_service_5",
		"status": "up",
				"mem_usage": "11.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "5",
				"current_timestamp": time.time()
	},
	"health_object_5_b": {
		"ip": "102.25.64.75",
		"port": "8172",
		"service_name": "test_service_5",
		"status": "up",
				"mem_usage": "21.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "10",
				"current_timestamp": time.time()
	},
	"health_object_6": {
		"ip": "",
		"port": "",
		"service_name": "test_service_5",
		"status": "up",
				"mem_usage": "21.2",
				"cpu_usage": "44.4",
				"nw_tput_bw_ratio": "74.1",
				"req_active_ratio": "48.1",
				"success_rate": "52.79",
				"health_interval": "10",
				"current_timestamp": time.time()
	}
}


@pytest.fixture(scope="function")
def foreach_test():
	print("Setup before test")
	""" Test Environment Setup for each test case """
	Config.setDbPath(os.path.join(basedir, "src/sharkradar/Util"))
	Config.setAlgorithm("wpmc")
	sharkradarDbutils.createTableIfNotExists()
	conn = sqlite3.connect(Config.getDbPath())
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_2"]["service_name"],
		 TEST_PARAMS["health_object_2"]["ip"],
		 TEST_PARAMS["health_object_2"]["port"],
		 TEST_PARAMS["health_object_2"]["current_timestamp"],
		 TEST_PARAMS["health_object_2"]["health_interval"],
		 TEST_PARAMS["health_object_2"]["mem_usage"],
		 TEST_PARAMS["health_object_2"]["cpu_usage"],
		 TEST_PARAMS["health_object_2"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_2"]["req_active_ratio"],
		 TEST_PARAMS["health_object_2"]["success_rate"]))
	conn.commit()
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_4"]["service_name"],
		 TEST_PARAMS["health_object_4"]["ip"],
		 TEST_PARAMS["health_object_4"]["port"],
		 TEST_PARAMS["health_object_4"]["current_timestamp"],
		 TEST_PARAMS["health_object_4"]["health_interval"],
		 TEST_PARAMS["health_object_4"]["mem_usage"],
		 TEST_PARAMS["health_object_4"]["cpu_usage"],
		 TEST_PARAMS["health_object_4"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_4"]["req_active_ratio"],
		 TEST_PARAMS["health_object_4"]["success_rate"]))
	conn.commit()
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_3_a"]["service_name"],
		 TEST_PARAMS["health_object_3_a"]["ip"],
		 TEST_PARAMS["health_object_3_a"]["port"],
		 TEST_PARAMS["health_object_3_a"]["current_timestamp"],
		 TEST_PARAMS["health_object_3_a"]["health_interval"],
		 TEST_PARAMS["health_object_3_a"]["mem_usage"],
		 TEST_PARAMS["health_object_3_a"]["cpu_usage"],
		 TEST_PARAMS["health_object_3_a"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_3_a"]["req_active_ratio"],
		 TEST_PARAMS["health_object_3_a"]["success_rate"]))
	conn.commit()
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_3_b"]["service_name"],
		 TEST_PARAMS["health_object_3_b"]["ip"],
		 TEST_PARAMS["health_object_3_b"]["port"],
		 TEST_PARAMS["health_object_3_b"]["current_timestamp"],
		 TEST_PARAMS["health_object_3_b"]["health_interval"],
		 TEST_PARAMS["health_object_3_b"]["mem_usage"],
		 TEST_PARAMS["health_object_3_b"]["cpu_usage"],
		 TEST_PARAMS["health_object_3_b"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_3_b"]["req_active_ratio"],
		 TEST_PARAMS["health_object_3_b"]["success_rate"]))
	conn.commit()
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_5_a"]["service_name"],
		 TEST_PARAMS["health_object_5_a"]["ip"],
		 TEST_PARAMS["health_object_5_a"]["port"],
		 TEST_PARAMS["health_object_5_a"]["current_timestamp"],
		 TEST_PARAMS["health_object_5_a"]["health_interval"],
		 TEST_PARAMS["health_object_5_a"]["mem_usage"],
		 TEST_PARAMS["health_object_5_a"]["cpu_usage"],
		 TEST_PARAMS["health_object_5_a"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_5_a"]["req_active_ratio"],
		 TEST_PARAMS["health_object_5_a"]["success_rate"]))
	conn.commit()
	conn.execute(
		"""INSERT INTO SERVICE_RD (SERVICE_NAME, IP, PORT, TIME_STAMP, HEALTH_INTERVAL, MEM_USAGE, CPU_USAGE, NW_TPUT_BW_RATIO, REQ_ACTIVE_RATIO, SUCCESS_RATE) \
						VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		(TEST_PARAMS["health_object_5_b"]["service_name"],
		 TEST_PARAMS["health_object_5_b"]["ip"],
		 TEST_PARAMS["health_object_5_b"]["port"],
		 TEST_PARAMS["health_object_5_b"]["current_timestamp"],
		 TEST_PARAMS["health_object_5_b"]["health_interval"],
		 TEST_PARAMS["health_object_5_b"]["mem_usage"],
		 TEST_PARAMS["health_object_5_b"]["cpu_usage"],
		 TEST_PARAMS["health_object_5_b"]["nw_tput_bw_ratio"],
		 TEST_PARAMS["health_object_5_b"]["req_active_ratio"],
		 TEST_PARAMS["health_object_5_b"]["success_rate"]))
	conn.commit()
	conn.close()
	yield ""
	print("Teardown after test")
	""" Test Environment Clean up for each test case """
	conn = sqlite3.connect(Config.getDbPath())
	conn.execute(
		"""DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_1"]["service_name"],))
	conn.commit()
	conn.execute(
		"""DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_2"]["service_name"],))
	conn.commit()
	conn.execute(
		"""DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_3_a"]["service_name"],))
	conn.commit()
	conn.execute(
		"""DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_4"]["service_name"],))
	conn.commit()
	conn.execute(
		"""DELETE FROM SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_5_a"]["service_name"],))
	conn.commit()
	conn.execute(
		"""DELETE FROM SERVICE_LOGS WHERE 1 = 1""")
	conn.execute(
		"""DELETE FROM DISCOVERY_LOGS WHERE 1 = 1""")
	conn.commit()
	conn.close()


def test_001_health_status_register(foreach_test):
	""" Register service """
	assert Health.health(TEST_PARAMS["health_object_1"]) == True


def test_002_health_status_deregister(foreach_test):
	""" Deregister service """
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_2"]["service_name"],
		 )).fetchall()
	conn.close()
	assert len(service_instances) > 0
	Health.health(TEST_PARAMS["health_object_2_down"])
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_2"]["service_name"],
		 )).fetchall()
	conn.close()
	assert len(service_instances) == 0


def test_003_health_status_update(foreach_test):
	""" Update service health data"""
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_2"]["service_name"],
		 )).fetchall()
	conn.close()
	assert service_instances[0][3] == 41.2
	Health.health(TEST_PARAMS["health_object_2_updated"])
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_2"]["service_name"],
		 )).fetchall()
	conn.close()
	assert service_instances[0][3] == 61.2


def test_004_discover_service(foreach_test):
	""" Discover service"""
	result = Discovery.discovery(
		TEST_PARAMS["health_object_4"]["service_name"], "start")
	assert TEST_PARAMS["health_object_4"]["ip"] == result[0]
	assert TEST_PARAMS["health_object_4"]["port"] == result[1]
	assert result[2] != "start"

def test_005_discover_service_retry(foreach_test):
	""" Discover service retry"""
	result = Discovery.discovery(
		TEST_PARAMS["health_object_4"]["service_name"], "start")
	assert TEST_PARAMS["health_object_4"]["ip"] == result[0]
	assert TEST_PARAMS["health_object_4"]["port"] == result[1]
	assert result[2] != "start"
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from DISCOVERY_LOGS WHERE SERVICE_NAME = ? AND IP = ? AND PORT = ?""",
		(TEST_PARAMS["health_object_4"]["service_name"],
		TEST_PARAMS["health_object_4"]["ip"],
		TEST_PARAMS["health_object_4"]["port"]
		 )).fetchall()
	conn.close()
	assert service_instances[0][4] == "SUCCESS"
	Discovery.discovery(
		TEST_PARAMS["health_object_4"]["service_name"], result[2])
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from DISCOVERY_LOGS WHERE RETRY_ID = ?""",
		(result[2],
		 )).fetchall()
	conn.close()
	assert service_instances[0][4] == "FAIL"


def test_006_discover_service_best(foreach_test):
	""" Discover best service"""
	result = Discovery.discovery(
		TEST_PARAMS["health_object_3_a"]["service_name"], "start")
	assert TEST_PARAMS["health_object_3_b"]["ip"] == result[0]
	assert TEST_PARAMS["health_object_3_b"]["port"] == result[1]
	assert result[2] != "start"

def test_007_discover_service_remove_dead(foreach_test):
	""" Remove dead service while discovering"""
	conn = sqlite3.connect(Config.getDbPath())
	service_instances = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_5_a"]["service_name"],
		 )).fetchall()
	conn.close()
	assert len(service_instances) == 2
	time.sleep(6)
	result = Discovery.discovery(
		TEST_PARAMS["health_object_5_a"]["service_name"],
		"start")
	conn = sqlite3.connect(Config.getDbPath())
	service_instance = conn.execute(
		"""SELECT * from SERVICE_RD WHERE SERVICE_NAME = ?""",
		(TEST_PARAMS["health_object_5_a"]["service_name"],
		 )).fetchall()
	conn.close()
	assert len(service_instance) == 1
	assert result[0] == TEST_PARAMS["health_object_5_b"]["ip"]
	assert result[1] == TEST_PARAMS["health_object_5_b"]["port"]
	assert result[2] != "start"

def test_008_health_status_register_improper_data(foreach_test):
	""" Register service with improper data """
	assert Health.health(TEST_PARAMS["health_object_6"]) == False

def test_009_health_status_register_check_logs(foreach_test):
	""" Register service and check service logs"""
	Health.health(TEST_PARAMS["health_object_1"])
	time.sleep(2)
	Health.health(TEST_PARAMS["health_object_1"])
	time.sleep(2)
	Health.health(TEST_PARAMS["health_object_1"])
	conn = sqlite3.connect(Config.getDbPath())
	service_instance = conn.execute(
		"""SELECT * from SERVICE_LOGS""").fetchall()
	conn.close()
	assert len(service_instance) == 3

def test_010_real_time_monitor(foreach_test):
	""" Real time monitor """
	result = MonitorRealTime.getAllServices()
	assert len(result) == 6