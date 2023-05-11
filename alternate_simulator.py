# SYSC4005 Project - Group 26
# Author: Visakan Kirubakaran
# Year of Completion: Jan - Apr 2022

import simpy
from scipy import stats
from simulator import *
from workstation import *
from inspector import *

# define total # of replications
number_of_replications = 10

# define how long each replication simulates for
sim_time = 50000

if __name__ == "__main__":

    # In order to analyse the alternate policies, the alternate_simulator will run each policy for a 
    # simulation time of t = 50000 and then repeat for the remaining policies.

    print("Starting simulation for Original Policy, t = 50000...")
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, 0, i)

    print(
        "Starting simulation for Random Policy, Less Probability for W1, t = 50000..."
    )
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, 1, i)

    print(
        "Starting simulation for Random Policy, More Probability for W1, t = 50000..."
    )
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, 2, i)

    print(
        "Starting simulation for Random Policy, Equal Probability for W1, t = 50000..."
    )
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, 3, i)

    print("Starting simulation for Reverse Priority Policy, t = 50000...")
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, 4, i)
