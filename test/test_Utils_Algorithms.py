import sys
from os.path import dirname as opd, realpath as opr
import os
basedir = opd(opd(opr(__file__)))
sys.path.append(os.path.join(basedir, "src"))

from sharkradar.Util import sharkradarAlgorithmutils

TEST_INSTANCE_LIST_1 = [
    ['S1', '103.154.11.20', '9488', 48.5, 47.0, 41.7, 30.2, 15.2, 94553997494, 5],
    ['S1', '103.154.11.21', '9481', 68.5, 67.0, 61.7, 60.2, 65.2, 94553997494, 5]
]

TEST_INSTANCE_LIST_2 = [
    ['S1', '103.154.11.20', '9488', 48.5, 47.0, 41.7, 30.2, 15.2, 94553997494, 5],
    ['S1', '103.154.11.21', '9481', 18.5, 17.0, 41.7, 30.2, 15.2, 94553997494, 5]
]


def test_001_verify_weighted_priority_memcpu():
    """ Verify algorithm """
    ip, port = sharkradarAlgorithmutils.weightedPriorityMemAndCPU(TEST_INSTANCE_LIST_1)
    assert ip == TEST_INSTANCE_LIST_1[0][1]
    assert port == TEST_INSTANCE_LIST_1[0][2]


def test_002_verify_weighted_priority_memcpu():
    """ Verify algorithm """
    ip, port = sharkradarAlgorithmutils.weightedPriorityMemAndCPU(TEST_INSTANCE_LIST_2)
    assert ip == TEST_INSTANCE_LIST_2[1][1]
    assert port == TEST_INSTANCE_LIST_2[1][2]

def test_003_verify_weighted_priority_reqsuc():
    """ Verify algorithm """
    ip, port = sharkradarAlgorithmutils.weightedPriorityReqActiveAndSuccessRate(TEST_INSTANCE_LIST_1)
    assert ip == TEST_INSTANCE_LIST_1[1][1]
    assert port == TEST_INSTANCE_LIST_1[1][2]


def test_004_verify_weighted_priority_reqsuc():
    """ Verify algorithm """
    ip, port = sharkradarAlgorithmutils.weightedPriorityReqActiveAndSuccessRate(TEST_INSTANCE_LIST_2)
    assert ip == TEST_INSTANCE_LIST_2[1][1]
    assert port == TEST_INSTANCE_LIST_2[1][2]
