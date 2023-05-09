def little_law_calc(throughput, avg_time_in_buffer):
    """
    little's law (l) = throughtput (# of products / unit time) * lead time (workstation idle time).
    """
    avg_buffer_occupancy = throughput * avg_time_in_buffer
    return str(avg_buffer_occupancy)


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
