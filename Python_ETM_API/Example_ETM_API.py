# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:14:17 2018
Author: frank buters - frank.buters@data-quest.nl
Description: Example of how to use the ETM_API via python 
Status: Finished 
"""
from ETM_API import ETM_API, SessionWithUrlBase

# Create base url, note that beta engine is not as fast as production engine
base_url = 'https://beta-engine.energytransitionmodel.com/api/v3'
session = SessionWithUrlBase(base_url)

#set scenario id
scenario_id = "363119" # Keep using same ID, instead of creating many new ones

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

# Example of the user values you can change. 
# See: https://github.com/quintel/etsource/tree/master/inputs
user_values = {
              "number_of_energy_power_nuclear_gen3_uranium_oxide":10,
              "investment_costs_nuclear_nuclear_plant": 25
              }

# Create an ETM object to manipulate and querry. All information is stored
# within the object itself
ETM = ETM_API(session,scenario_id)
ETM.change_inputs(user_values,metrics)

# See the updated metrics:
ETM_metrics = ETM.current_metrics

# Get dataframe with templates
ETM.get_scenario_templates()
df_templates = ETM.df_templates
   
#KLAD
#scenario BAU Netherlands: 363119
#scenario 100% duurzaam: 155680