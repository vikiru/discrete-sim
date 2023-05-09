# sysc4005 project - group 26
# author: visakan kirubakaran
# year of completion: 2022

import simpy
from scipy import stats
from simulator import *
from workstation import *
from inspector import *

# save the results of each simulation run to a text file
def alt_save_output_to_file(output_text, policy_num):
    operating_policies = {
        0: "original_policy",
        1: "random_policy_less_probability_w1",
        2: "random_policy_more_probability_w1",
        3: "random_policy_equal_probability",
        4: "reverse_priority",
    }

    # filename is where the results will be stored
    file_name = "./alternate_results/" + operating_policies[policy_num] + ".txt"
    f = open(file_name, "w")
    f.write(output_text)
    f.close()


if __name__ == "__main__":
    # define total # of replications and how long each replication simulates for
    sim_time = 50000

    # in order to analyse the alternate policies,
    # the alternate_simulator will run each policay for a simulation time of t = 50000
    # once and then repeat for the remaining policies

    print("starting simulation for original policy, t = 50000...")
    run_simulation(sim_time, 0)
    print(
        "starting simulation for random policy, less probability for w1, t = 50000..."
    )
    run_simulation(sim_time, 1)
    print(
        "starting simulation for random policy, more probability for w1, t = 50000..."
    )
    run_simulation(sim_time, 2)
    print("starting simulation for random policy, equal probability, t = 50000...")
    run_simulation(sim_time, 3)
    print("starting simulation for reverse priority policy, t = 50000...")
    run_simulation(sim_time, 4)
