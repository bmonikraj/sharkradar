"""
DB Utils functions for the project
"""
import sys
from os.path import dirname as opd, realpath as opr
import os

basedir = opd(opd(opd(opr(__file__))))
sys.path.append(basedir)


def weightedPriorityMemAndCPU(service_instances):
    """
            Algorithm to find highest priority based on weighted means
            with highest weight to Memory and CPU usage

            NOTE ** Tightly coupled with the order of the table columns
    """
    mem_usage_wt = 4.0
    cpu_usage_wt = 4.0
    nw_tput_bw_ratio_wt = 3.0
    req_active_ratio_wt = 2.0
    success_rate_wt = 1.0
    sum_of_weights = 100.00 * (mem_usage_wt + cpu_usage_wt + \
                               nw_tput_bw_ratio_wt + req_active_ratio_wt + success_rate_wt)
    priority_list = []
    for i in range(0, len(service_instances)):
        single_instance = {}
        single_instance['ip'] = service_instances[i][1]
        single_instance['port'] = service_instances[i][2]
        score = 0.0
        score = float(nw_tput_bw_ratio_wt *
                      service_instances[i][5] +
                      success_rate_wt *
                      service_instances[i][7] +
                      mem_usage_wt *
                      (100.00 -
                       service_instances[i][3]) +
                      cpu_usage_wt *
                      (100.00 -
                       service_instances[i][4]) +
                      req_active_ratio_wt *
                      (100.00 -
                       service_instances[i][6]))
        score = float(score / sum_of_weights)
        single_instance['score'] = score
        priority_list.append(single_instance)
    priority_list.sort(key=lambda x: x['score'], reverse=True)
    res = priority_list[0]
    return str(res['ip']), str(res['port'])

def weightedPriorityReqActiveAndSuccessRate(service_instances):
    """
            Algorithm to find highest priority based on weighted means
            with major weight to Success rate and Req active ratio

            NOTE ** Tightly coupled with the order of the table columns
    """
    mem_usage_wt = 3.0
    cpu_usage_wt = 3.0
    nw_tput_bw_ratio_wt = 2.0
    req_active_ratio_wt = 4.0
    success_rate_wt = 4.0
    sum_of_weights = 100.00 * (mem_usage_wt + cpu_usage_wt + \
                               nw_tput_bw_ratio_wt + req_active_ratio_wt + success_rate_wt)
    priority_list = []
    for i in range(0, len(service_instances)):
        single_instance = {}
        single_instance['ip'] = service_instances[i][1]
        single_instance['port'] = service_instances[i][2]
        score = 0.0
        score = float(nw_tput_bw_ratio_wt *
                      service_instances[i][5] +
                      success_rate_wt *
                      service_instances[i][7] +
                      mem_usage_wt *
                      (100.00 -
                       service_instances[i][3]) +
                      cpu_usage_wt *
                      (100.00 -
                       service_instances[i][4]) +
                      req_active_ratio_wt *
                      (100.00 -
                       service_instances[i][6]))
        score = float(score / sum_of_weights)
        single_instance['score'] = score
        priority_list.append(single_instance)
    priority_list.sort(key=lambda x: x['score'], reverse=True)
    res = priority_list[0]
    return str(res['ip']), str(res['port'])
