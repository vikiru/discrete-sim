# sysc4005 project - group 26
# author: visakan kirubakaran
# year of completion: 2022

import simpy
from scipy import stats
from workstation import *
from inspector import *


# little's law (l) = throughtput (# of products / unit time) * lead time (workstation idle time)
def little_law_calc(throughput, avg_time_in_buffer):
    avg_buffer_occupancy = throughput * avg_time_in_buffer
    return str(avg_buffer_occupancy)


# save the results of each simulation run to a text file
def save_output_to_file(output_text, policy_num):
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


# returns the average of the data with ci as a string
def return_avg_with_ci(data):
    mean = numpy.mean(data)
    ci = calculate_confidence_interval(data)
    return str(mean) + " +/- " + str(ci)


# calculate the 95% confidence interval for each list of data passed
def calculate_confidence_interval(data):
    std_dev = numpy.std(data)
    degrees_of_freedom = len(data) - 1
    confidence_interval = 0.95

    return std_dev * stats.t.ppf((1 + confidence_interval) / 2.0, degrees_of_freedom)


# the function which handles a single simulation for a given sim_time
def run_simulation(sim_time, policy_num):
    # define some dictionaries to store simulation results
    model_inspect_times = {
        "inspector1_c1": [],
        "inspector2_c2": [],
        "inspector2_c3": [],
    }
    model_inspector_block_times = {
        "inspector1_c1": [],
        "inspector2_c2": [],
        "inspector2_c3": [],
    }
    model_products_created = {"p1": 0, "p2": 0, "p3": 0}
    model_workstation_process_times = {"w1": [], "w2": [], "w3": []}
    model_workstation_idle_times = {"w1": [], "w2": [], "w3": []}

    # initialize all inspectors & workstations
    env_variable = simpy.environment()

    w1 = workstation1(env_variable)
    w2 = workstation2(env_variable)
    w3 = workstation3(env_variable)
    i1 = inspector1(env_variable, [w1, w2, w3], policy_num)
    i2 = inspector2(env_variable, [w2, w3])

    # start simulation
    output_text = ""
    env_variable.run(until=sim_time)

    # results
    # inspector service times for each component
    model_inspect_times["inspector1_c1"].extend(i1.service_time[0])
    model_inspect_times["inspector2_c2"].extend(i2.service_time[0])
    model_inspect_times["inspector2_c3"].extend(i2.service_time[1])

    # inspector blocked times for each component
    model_inspector_block_times["inspector1_c1"].extend(i1.blocked_time[0])
    model_inspector_block_times["inspector2_c2"].extend(i2.blocked_time[0])
    model_inspector_block_times["inspector2_c3"].extend(i2.blocked_time[1])

    # workstation products created
    model_products_created["p1"] = w1.products_created
    model_products_created["p2"] = w2.products_created
    model_products_created["p3"] = w3.products_created

    # workstation process times
    model_workstation_process_times["w1"].extend(w1.process_time[0])
    model_workstation_process_times["w2"].extend(w2.process_time[0])
    model_workstation_process_times["w3"].extend(w3.process_time[0])

    # workstation idle times
    model_workstation_idle_times["w1"].extend(w1.idle_time[0])
    model_workstation_idle_times["w2"].extend(w2.idle_time[0])
    model_workstation_idle_times["w3"].extend(w3.idle_time[0])

    # compute averages and ci

    # inspector inspect and blocked times
    inspect_c1 = return_avg_with_ci(model_inspect_times["inspector1_c1"])
    inspect_c2 = return_avg_with_ci(model_inspect_times["inspector2_c2"])
    inspect_c3 = return_avg_with_ci(model_inspect_times["inspector2_c3"])

    blocked_c1 = return_avg_with_ci(model_inspector_block_times["inspector1_c1"])
    blocked_c2 = return_avg_with_ci(model_inspector_block_times["inspector2_c2"])
    blocked_c3 = return_avg_with_ci(model_inspector_block_times["inspector2_c3"])

    # products created
    p1total = str(model_products_created["p1"])
    p2total = str(model_products_created["p2"])
    p3total = str(model_products_created["p3"])

    # workstation process and idle times
    process_w1 = return_avg_with_ci(model_workstation_process_times["w1"])
    process_w2 = return_avg_with_ci(model_workstation_process_times["w2"])
    process_w3 = return_avg_with_ci(model_workstation_process_times["w3"])

    idle_w1 = return_avg_with_ci(model_workstation_idle_times["w1"])
    idle_w2 = return_avg_with_ci(model_workstation_idle_times["w2"])
    idle_w3 = return_avg_with_ci(model_workstation_idle_times["w3"])

    # output results & save to text file
    operating_policies = {
        0: "original policy",
        1: "random policy, less probability for w1",
        2: "random policy, more probability for w1",
        3: "random policy, equal probability for w1",
        4: "reverse priority policy",
    }
    output_text += (
        "results of simulation for the " + operating_policies[policy_num] + ":\n"
    )
    output_text += "inspector 1 avg. inspection time (c1): " + inspect_c1 + "\n"
    output_text += "inspector 2 avg. inspection time (c2): " + inspect_c2 + "\n"
    output_text += "inspector 2 avg. inspection time (c3): " + inspect_c3 + "\n"

    output_text += "inspector 1 avg. blocked time (c1): " + blocked_c1 + "\n"
    output_text += "inspector 2 avg. blocked time (c2): " + blocked_c2 + "\n"
    output_text += "inspector 2 avg. blocked time (c3): " + blocked_c3 + "\n"

    output_text += "workstation 1 avg. process time: " + process_w1 + "\n"
    output_text += "workstation 2 avg. process time: " + process_w2 + "\n"
    output_text += "workstation 3 avg. process time: " + process_w3 + "\n"

    output_text += "workstation 1 avg. idle time: " + idle_w1 + "\n"
    output_text += "workstation 2 avg. idle time: " + idle_w2 + "\n"
    output_text += "workstation 3 avg. idle time: " + idle_w3 + "\n"

    output_text += "total p1 produced: " + p1total + "\n"
    output_text += "total p2 produced: " + p2total + "\n"
    output_text += "total p3 produced: " + p3total + "\n"

    # calculate throughput (products / unit time)
    throughput_w1 = numpy.mean(model_products_created["p1"] / sim_time)
    throughput_w2 = numpy.mean(model_products_created["p2"] / sim_time)
    throughput_w3 = numpy.mean(model_products_created["p3"] / sim_time)

    # calculate avg time spent in queue using workstation idle time
    avg_time_in_buffer_w1 = numpy.mean(model_workstation_idle_times["w1"])
    avg_time_in_buffer_w2 = numpy.mean(model_workstation_idle_times["w2"])
    avg_time_in_buffer_w3 = numpy.mean(model_workstation_idle_times["w3"])

    # output little law results for all workstations
    output_text += (
        "avg. buffer occupancy using little's law for w1: "
        + little_law_calc(throughput_w1, avg_time_in_buffer_w1)
        + "\n"
    )
    output_text += (
        "avg. buffer occupancy using little's law for w2: "
        + little_law_calc(throughput_w2, avg_time_in_buffer_w2)
        + "\n"
    )
    output_text += (
        "avg. buffer occupancy using little's law for w3: "
        + little_law_calc(throughput_w3, avg_time_in_buffer_w3)
        + "\n"
    )

    # output all of the output_text that has been saved till this point
    print(output_text)

    # save result of simulation to alternate_results/
    save_output_to_file(output_text, policy_num)


# define total # of replications and how long each replication simulates for
sim_time = 50000

# in order to analyse the alternate policies,
# the alternate_simulator will run each policay for a simulation time of t = 50000
# once and then repeat for the remaining policies

print("starting simulation for original policy, t = 50000...")
run_simulation(sim_time, 0)
print("starting simulation for random policy, less probability for w1, t = 50000...")
run_simulation(sim_time, 1)
print("starting simulation for random policy, more probability for w1, t = 50000...")
run_simulation(sim_time, 2)
print("starting simulation for random policy, equal probability, t = 50000...")
run_simulation(sim_time, 3)
print("starting simulation for reverse priority policy, t = 50000...")
run_simulation(sim_time, 4)
