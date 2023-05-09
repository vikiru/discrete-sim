# SYSC4005 Project - Group 26
# Author: Visakan Kirubakaran
# Year of Completion: Jan - Apr 2022

# The following functions will be called upon each Inspector & Workstation
# class in order to specify their actual mean and random mean time values

import numpy


def generate_random_mean_time(filename):
    """Generate a random exponentially distributed random value based on mean time."""

    mean_time = get_input_data_mean_time(filename)
    return numpy.random.exponential(mean_time)


def get_input_data_mean_time(filename):
    """Get the actual mean time value obtained from the input data files"""

    # folder_dir is where the .dat files are stored
    folder_dir = "SYSC4005_Group26_Project/data/"

    # Append filename to the folder_dir to retrieve the file
    filename = folder_dir + filename

    # Sum all the lines of data and return the mean
    sum_data = 0
    input_data = open(filename).read().splitlines()
    for i in range(0, 300):
        sum_data += float(input_data[i])
    mean_time = sum_data / 300
    return mean_time
