import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(os.path.join(basedir, "src"))

from sharkradar.Config.Config import Config

def test_001_get_dbpath_without_set():
    """ Test blank DB Path """
    assert Config.getDbPath() == ""


def test_002_get_dbpath_with_set():
    """ Test blank DB Path """
    Config.setDbPath("ABC")
    assert Config.getDbPath() == "ABC/sharkradar_service.db"


def test_002_get_algo_without_set():
    """ Test blank Algo """
    assert Config.getAlgorithm() == ""


def test_002_get_algo_with_set():
    """ Test blank Algo """
    Config.setAlgorithm("ABC")
    assert Config.getAlgorithm() == "ABC"
