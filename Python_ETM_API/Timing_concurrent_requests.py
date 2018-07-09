# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:55:25 2018
Author: frank buters - frank.buters@data-quest.nl
Description: Small script to make concurrent calls to a single scenario_id. 
The scenario is reset, after which some user_values are changed and the resulting
metrics are recorded.  
Status: Finished 
"""
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor
import queue

from ETM_API import ETM_API, SessionWithUrlBase

def task(scenario_id):
    ETM = ETM_API(session,scenario_id) # connect to 
    ETM.reset_scenario()
    result = ETM.change_inputs(user_values,metrics)
    q.put(result)
    pass

def main(n_workers, n_tasks, scenario_id):
    #print("Starting ThreadPoolExecutor")
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        for i in range(n_tasks):
            executor.submit(task, (scenario_id))
             
    t1 = time.time()
    total_time = t1-t0
    #print("All tasks complete")
    
    return total_time

# Create base url, note that beta engine is not as fast as production engine
base_url = 'https://beta-engine.energytransitionmodel.com/api/v3'
session = SessionWithUrlBase(base_url)

#set scenario id
scenario_id_1 = "363691" # Keep using same ID, instead of creating many new ones
scenario_id_2 = "363690"
scenario_id_3 = "363689"
scenario_id_4 = "363688"

# These are the metrics Quintel use by default on their dashboard ribbon at the
# bottom, see: https://github.com/quintel/etsource/tree/master/gqueries/output_elements/dashboard
metrics = [
           "dashboard_energy_demand_primary_of_final_plus_export_losses", 
           "co2_emissions_of_final_demand_excluding_imported_electricity",
           "co2_emissions_of_imported_electricity",
           "dashboard_energy_import_netto",
           "dashboard_total_costs", 
           "dashboard_bio_footprint",
           "dashboard_renewability"
           ]

user_values = {
              "number_of_energy_power_nuclear_gen3_uranium_oxide":10,
              "investment_costs_nuclear_nuclear_plant": 25
              }

session = SessionWithUrlBase(base_url)

# Explore via threading how the performance of the API
# I am aware that the nested for loops look ugly!
size = 10
avgs = 10
result = np.zeros([size,size])
for i in range(0,size):
    print("Test with {} workers".format(i+1))
    for j in range(0,size):
        print("Test with {} tasks".format(j+1))
        lst_result = []
        for k in range(avgs):
            q = queue.Queue()
            proc_time = main(i+1,j+1, scenario_id_1)
            lst_result.append(proc_time)
        result[i,j] = np.mean(lst_result)

np.savetxt(r'.\Results\result.csv', result, delimiter=',')