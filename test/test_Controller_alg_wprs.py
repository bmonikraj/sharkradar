import time
import json
import sqlite3
import pytest
import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(os.path.join(basedir, "src"))

from sharkradar.Controller.Controller import app
from sharkradar.Service.Health import Health
from sharkradar.Service.Discovery import Discovery
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
        "service_name": "test_service_1",
        "status": "up",
                "mem_usage": "41.2",
                "cpu_usage": "44.4",
                "nw_tput_bw_ratio": "74.1",
                "req_active_ratio": "48.1",
                "success_rate": "52.79",
                "health_interval": "11",
                "current_timestamp": time.time()
    },
    "health_object_3": {
        "ip": "102.25.64.74",
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
    "health_object_4": {
        "ip": "102.25.84.74",
        "port": "8079",
        "service_name": "test_service_4",
        "status": "up",
                "mem_usage": "41.2",
                "cpu_usage": "44.4",
                "nw_tput_bw_ratio": "74.1",
                "req_active_ratio": "48.1",
                "success_rate": "52.79",
                "health_interval": "11",
    },
    "health_object_5": {
        "ip": "102.25.84.74",
        "port": "8079",
        "service_name": "test_service_5",
        "status": "up",
                "mem_usage": "415.2",
                "cpu_usage": "44.4",
                "nw_tput_bw_ratio": "74.1",
                "req_active_ratio": "48.1",
                "success_rate": "52.79",
                "health_interval": "11",
    },
    "health_object_6": {
        "ip": "102.25.84.74",
        "port": "8079",
        "service_name": "test_service_5",
        "status123": "up",
                "mem_usage": "415.2",
                "cpu_usage": "44.4",
                "nw_tput_bw_ratio": "74.1",
                "req_active_ratio": "48.1",
                "success_rate": "52.79",
                "health_interval": "11",
    }
}


@pytest.fixture(scope="function")
def foreach_test():
    print("Setup before test")
    """ Test Environment Setup for each test case """
    Config.setDbPath(os.path.join(basedir, "src/sharkradar/Util"))
    Config.setAlgorithm("wprs")
    sharkradarDbutils.createTableIfNotExists()
    Health.health(TEST_PARAMS["health_object_1"])
    Health.health(TEST_PARAMS["health_object_2"])
    Health.health(TEST_PARAMS["health_object_3"])
    app.testing = True
    client = app.test_client()
    yield client
    print("Teardown after test")
    """ Test Environment Clean up for each test case """
    sharkradarDbutils.deleteServiceByNameAndIpAndPort(
        TEST_PARAMS["health_object_1"]["service_name"],
        TEST_PARAMS["health_object_1"]["ip"],
        TEST_PARAMS["health_object_1"]["port"])
    sharkradarDbutils.deleteServiceByNameAndIpAndPort(
        TEST_PARAMS["health_object_2"]["service_name"],
        TEST_PARAMS["health_object_2"]["ip"],
        TEST_PARAMS["health_object_2"]["port"])
    sharkradarDbutils.deleteServiceByNameAndIpAndPort(
        TEST_PARAMS["health_object_3"]["service_name"],
        TEST_PARAMS["health_object_3"]["ip"],
        TEST_PARAMS["health_object_3"]["port"])
    sharkradarDbutils.deleteServiceByNameAndIpAndPort(
        TEST_PARAMS["health_object_4"]["service_name"],
        TEST_PARAMS["health_object_4"]["ip"],
        TEST_PARAMS["health_object_4"]["port"])
    conn = sqlite3.connect(Config.getDbPath())
    conn.execute(
        """DELETE FROM SERVICE_LOGS WHERE 1 = 1""")
    conn.execute(
        """DELETE FROM DISCOVERY_LOGS WHERE 1 = 1""")
    conn.commit()
    conn.close()


def test_001_search_unregistered(foreach_test):
    """ Search for a service, which is not available in registry """
    response = foreach_test.get("/discovery/start/" +
                                TEST_PARAMS["SERVICE_NAME_UNREGISTERED"])
    assert json.loads(response.data) == {"ip": "", "port": "", "retryid" : ""}


def test_002_search_registered(foreach_test):
    """ Search for a service, which is available in registry """
    response = foreach_test.get("/discovery/start/" +
                                TEST_PARAMS["health_object_3"]["service_name"])
    assert json.loads(response.data)["ip"] == TEST_PARAMS["health_object_3"]["ip"]
    assert json.loads(response.data)["port"] == TEST_PARAMS["health_object_3"]["port"]
    assert json.loads(response.data)["retryid"] != "start"

def test_003_search_registered_best(foreach_test):
    """ Search for a service, which is available in registry and the best one"""
    response = foreach_test.get("/discovery/start/" +
                                TEST_PARAMS["health_object_1"]["service_name"])
    assert json.loads(response.data)["ip"] == TEST_PARAMS["health_object_2"]["ip"]
    assert json.loads(response.data)["port"] == TEST_PARAMS["health_object_2"]["port"]
    assert json.loads(response.data)["retryid"] != "start"

def test_004_search_registered_best(foreach_test):
    """ Search for a service, with wrong paramters"""
    response = foreach_test.get("/discovery/")
    assert response.status.split(" ")[0] == "404"

def test_005_health_send(foreach_test):
    """ Send health for a service"""
    response = foreach_test.put("/health", data=TEST_PARAMS["health_object_4"])
    assert json.loads(response.data) == {"status": "True"}


def test_006_health_send_improper_mem_usage(foreach_test):
    """ Send health for a service"""
    response = foreach_test.put("/health", data=TEST_PARAMS["health_object_5"])
    assert json.loads(response.data) == {"status": "False"}

def test_007_health_send_improper_params(foreach_test):
    """ Send health for a service with wrong params"""
    response = foreach_test.put("/health", data=TEST_PARAMS["health_object_6"])
    assert json.loads(response.data) == {"status": "False"}

def test_008_get_real_time_monitor(foreach_test):
    """ API to fetch real time monitor"""
    response = foreach_test.get("/monitor-real-time/current/0")
    assert len(json.loads(response.data)) == 3

def test_009_get_real_time_monitor_serviceslogs(foreach_test):
    """ API to fetch real time monitor"""
    response = foreach_test.get("/monitor-real-time/service/250")
    assert len(json.loads(response.data)) == 3

def test_010_get_real_time_monitor_discoverylogs(foreach_test):
    """ API to fetch real time monitor"""
    Discovery.discovery(
        TEST_PARAMS["health_object_3"]["service_name"], "start")
    response = foreach_test.get("/monitor-real-time/discovery/250")
    assert len(json.loads(response.data)) == 1

def test_0011_real_time_monitor_bad_method(foreach_test):
    """ Search for a service, with wrong paramters"""
    response = foreach_test.get("/monitor-real-time/test/250")
    assert json.loads(response.data) == []