# SYSC4005 Project - Group 26
# Author: Visakan Kirubakaran
# Year of Completion: Jan - Apr 2022

import simpy
from scipy import stats
from workstation import *
from inspector import *


def little_law_calc(throughput, avg_time_in_buffer):
    """
    Little's law (l) = throughtput (# of products / unit time) * lead time (workstation idle time).
    """

    avg_buffer_occupancy = throughput * avg_time_in_buffer
    return str(avg_buffer_occupancy)


def return_avg_with_ci(data):
    """Returns the average of the data along with the confidence interval as a string."""

    mean = numpy.mean(data)
    ci = calculate_confidence_interval(data)
    return str(mean) + " +/- " + str(ci)


def calculate_confidence_interval(data):
    """Calculate the 95% confidence interval for each list of data passed."""

    std_dev = numpy.std(data)
    degrees_of_freedom = len(data) - 1
    confidence_interval = 0.95

    return std_dev * stats.t.ppf((1 + confidence_interval) / 2.0, degrees_of_freedom)


def save_output_to_file(output_text, policy_number, i):
    """Save the results of each simulation run to a text file."""

    operating_policies = {
        0: "original_policy",
        1: "random_policy_less_probability_w1",
        2: "random_policy_more_probability_w1",
        3: "random_policy_equal_probability",
        4: "reverse_priority",
    }

    # filename is where the results will be stored
    file_name = (
        "./results/"
        + operating_policies[policy_number]
        + "/"
        + "sim_run_"
    )

    if i < 10:
        file_name += "0" + str(i)
    else:
        file_name += str(i)

    file_name += ".txt"
    f = open(file_name, "w")
    f.write(output_text)
    f.close()


def run_simulation(sim_time, policy_num, i):
    """
    Run a simulation of the system for given simulation time and policy number. Print the
    results of the simulation and save the results to their corresponding files.
    """

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
    env_variable = simpy.Environment()

    w1 = Workstation1(env_variable)
    w2 = Workstation2(env_variable)
    w3 = Workstation3(env_variable)
    i1 = Inspector1(env_variable, [w1, w2, w3], policy_num)
    i2 = Inspector2(env_variable, [w2, w3])

    # start simulation
    output_text = ""
    output_text += (
        "Starting simulation ["
        + str(i)
        + " / "
        + str(number_of_replications)
        + "] and running for time, t = "
        + str(sim_time)
    )
    env_variable.run(until=sim_time)

    # results
    # inspector service times for each component
    model_inspect_times["inspector1_c1"].extend(i1.service_times[0])
    model_inspect_times["inspector2_c2"].extend(i2.service_times[0])
    model_inspect_times["inspector2_c3"].extend(i2.service_times[1])

    # inspector blocked times for each component
    model_inspector_block_times["inspector1_c1"].extend(i1.service_times[0])
    model_inspector_block_times["inspector2_c2"].extend(i2.service_times[0])
    model_inspector_block_times["inspector2_c3"].extend(i2.service_times[1])

    # workstation products created
    model_products_created["p1"] = w1.products_created
    model_products_created["p2"] = w2.products_created
    model_products_created["p3"] = w3.products_created

    # workstation process times
    model_workstation_process_times["w1"].extend(w1.process_times[0])
    model_workstation_process_times["w2"].extend(w2.process_times[0])
    model_workstation_process_times["w3"].extend(w3.process_times[0])

    # workstation idle times
    model_workstation_idle_times["w1"].extend(w1.idle_times[0])
    model_workstation_idle_times["w2"].extend(w2.idle_times[0])
    model_workstation_idle_times["w3"].extend(w3.idle_times[0])

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
        0: "Original Policy",
        1: "Random Policy, Less Probability for W1",
        2: "Random Policy, More Probability for W1",
        3: "Random Policy, Equal Probability for W1",
        4: "Reverse Priority Policy",
    }
    output_text += (
        "\nResults of Simulation for the " + operating_policies[policy_num] + ":\n"
    )
    output_text += "Inspector 1 Avg. Inspection time (C1): " + inspect_c1 + "\n"
    output_text += "Inspector 2 Avg. Inspection time (C2): " + inspect_c2 + "\n"
    output_text += "Inspector 2 Avg. Inspection time (C3): " + inspect_c3 + "\n"

    output_text += "Inspector 1 Avg. Blocked time (C1): " + blocked_c1 + "\n"
    output_text += "Inspector 2 Avg. Blocked time (C2): " + blocked_c2 + "\n"
    output_text += "Inspector 2 Avg. Blocked time (C3): " + blocked_c3 + "\n"

    output_text += "Workstation 1 Avg. Process time: " + process_w1 + "\n"
    output_text += "Workstation 2 Avg. Process time: " + process_w2 + "\n"
    output_text += "Workstation 3 Avg. Process time: " + process_w3 + "\n"

    output_text += "Workstation 1 Avg. Idle time: " + idle_w1 + "\n"
    output_text += "Workstation 2 Avg. Idle time: " + idle_w2 + "\n"
    output_text += "Workstation 3 Avg. Idle time: " + idle_w3 + "\n"

    output_text += "Total P1 produced: " + p1total + "\n"
    output_text += "Total P2 produced: " + p2total + "\n"
    output_text += "Total P3 produced: " + p3total + "\n"

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
        "Avg. Buffer Occupancy Using Little's Law For W1: "
        + little_law_calc(throughput_w1, avg_time_in_buffer_w1)
        + "\n"
    )
    output_text += (
        "Avg. Buffer Occupancy Using Little's Law For W2: "
        + little_law_calc(throughput_w2, avg_time_in_buffer_w2)
        + "\n"
    )
    output_text += (
        "Avg. Buffer Occupancy Using Little's Law For W3: "
        + little_law_calc(throughput_w3, avg_time_in_buffer_w3)
        + "\n"
    )

    # output all of the output_text that has been saved till this point
    print(output_text)

    # save result of simulation[i] to respective folder
    save_output_to_file(output_text, policy_num, i)


# define total # of replications and how long each replication simulates for
number_of_replications = 10
sim_time = 10000

if __name__ == "__main__":

    policy_number = 0  # 0 is used here to use the original operating policy

    # main loop of simulator, will repeat each simulation until number_of_replications
    for i in range(1, number_of_replications + 1):
        run_simulation(sim_time, policy_number, i)
