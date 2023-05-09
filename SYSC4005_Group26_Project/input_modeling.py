# SYSC4005 Project - Group 26
# Author: Vis Kirubakaran 

import numpy

# The following functions will be called upon each Inspector & Workstation
# class in order to specify their actual mean and random mean time values

# Generate a random exponentially distributed random value based on meanTime
def generateRandomMeanTime(filename):
    meanTime = getInputDataMeanTime(filename)
    return numpy.random.exponential(meanTime)


# Get the actual mean time value obtained from the input data files
def getInputDataMeanTime(filename):
    # folderDir is where the .dat files are stored
    folderDir = "SYSC4005_Group26_Project/data/"

    # Append filename to the folderDir to retrieve the file
    filename = folderDir + filename

    # Sum all the lines of data and return the mean
    sumData = 0
    inputData = open(filename).read().splitlines()
    for i in range(0, 300):
        sumData += float(inputData[i])
    meanTime = sumData / 300
    return meanTime
