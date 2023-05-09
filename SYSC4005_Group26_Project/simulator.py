# SYSC4005 Project - Group 26
# Author: Vis Kirubakaran 

import simpy
from scipy import stats
from workstation import *
from inspector import *

# Little's Law (L) = Throughtput (# of products / unit time) * Lead Time (Workstation Idle Time)
def littleLawCalc(throughput, avgTimeInBuffer):
    avgBufferOccupancy = throughput * avgTimeInBuffer
    return str(avgBufferOccupancy)


# Save the results of each simulation run to a text file
def saveOutputToFile(outputText, i):
    # filename is where the results will be stored
    fileName = "SYSC4005_Group26_Project/results/sim_run_" + str(i) + ".txt"
    f = open(fileName, "w")
    f.write(outputText)
    f.close()


# Returns the average of the data with CI as a string
def returnAvgWithCI(data):
    mean = numpy.mean(data)
    CI = calculateConfidenceInterval(data)
    return str(mean) + " +/- " + str(CI)


# Calculate the 95% Confidence interval for each list of data passed
def calculateConfidenceInterval(data):
    stdDev = numpy.std(data)
    degreesOfFreedom = len(data) - 1
    confidenceInterval = 0.95

    return stdDev * stats.t.ppf((1 + confidenceInterval) / 2.0, degreesOfFreedom)


# The function which handles a single simulation for a given simTime
def runSimulation(simTime, policyNum):
    # Define some dictionaries to store simulation results
    modelInspectTimes = {
        "Inspector1_C1": [],
        "Inspector2_C2": [],
        "Inspector2_C3": [],
    }
    modelInspectorBlockTimes = {
        "Inspector1_C1": [],
        "Inspector2_C2": [],
        "Inspector2_C3": [],
    }
    modelProductsCreated = {"P1": 0, "P2": 0, "P3": 0}
    modelWorkstationProcessTimes = {"W1": [], "W2": [], "W3": []}
    modelWorkstationIdleTimes = {"W1": [], "W2": [], "W3": []}

    # Initialize all Inspectors & Workstations
    envVariable = simpy.Environment()

    W1 = Workstation1(envVariable)
    W2 = Workstation2(envVariable)
    W3 = Workstation3(envVariable)
    I1 = Inspector1(envVariable, [W1, W2, W3], policyNum)
    I2 = Inspector2(envVariable, [W2, W3])

    # Start simulation
    outputText = ""
    outputText += (
        "Starting simulation ["
        + str(i)
        + " / "
        + str(numberOfReplications)
        + "] and running for time, t = "
        + str(simTime)
    )
    envVariable.run(until=simTime)

    # Results
    # Inspector service times for each component
    modelInspectTimes["Inspector1_C1"].extend(I1.serviceTime[0])
    modelInspectTimes["Inspector2_C2"].extend(I2.serviceTime[0])
    modelInspectTimes["Inspector2_C3"].extend(I2.serviceTime[1])

    # Inspector blocked times for each component
    modelInspectorBlockTimes["Inspector1_C1"].extend(I1.blockedTime[0])
    modelInspectorBlockTimes["Inspector2_C2"].extend(I2.blockedTime[0])
    modelInspectorBlockTimes["Inspector2_C3"].extend(I2.blockedTime[1])

    # Workstation products created
    modelProductsCreated["P1"] = W1.productsCreated
    modelProductsCreated["P2"] = W2.productsCreated
    modelProductsCreated["P3"] = W3.productsCreated

    # Workstation process times
    modelWorkstationProcessTimes["W1"].extend(W1.processTime[0])
    modelWorkstationProcessTimes["W2"].extend(W2.processTime[0])
    modelWorkstationProcessTimes["W3"].extend(W3.processTime[0])

    # Workstation idle times
    modelWorkstationIdleTimes["W1"].extend(W1.idleTime[0])
    modelWorkstationIdleTimes["W2"].extend(W2.idleTime[0])
    modelWorkstationIdleTimes["W3"].extend(W3.idleTime[0])

    # Compute averages and CI

    # Inspector Inspect and Blocked Times
    inspectC1 = returnAvgWithCI(modelInspectTimes["Inspector1_C1"])
    inspectC2 = returnAvgWithCI(modelInspectTimes["Inspector2_C2"])
    inspectC3 = returnAvgWithCI(modelInspectTimes["Inspector2_C3"])

    blockedC1 = returnAvgWithCI(modelInspectorBlockTimes["Inspector1_C1"])
    blockedC2 = returnAvgWithCI(modelInspectorBlockTimes["Inspector2_C2"])
    blockedC3 = returnAvgWithCI(modelInspectorBlockTimes["Inspector2_C3"])

    # Products Created
    P1total = str(modelProductsCreated["P1"])
    P2total = str(modelProductsCreated["P2"])
    P3total = str(modelProductsCreated["P3"])

    # Workstation Process and Idle Times
    processW1 = returnAvgWithCI(modelWorkstationProcessTimes["W1"])
    processW2 = returnAvgWithCI(modelWorkstationProcessTimes["W2"])
    processW3 = returnAvgWithCI(modelWorkstationProcessTimes["W3"])

    idleW1 = returnAvgWithCI(modelWorkstationIdleTimes["W1"])
    idleW2 = returnAvgWithCI(modelWorkstationIdleTimes["W2"])
    idleW3 = returnAvgWithCI(modelWorkstationIdleTimes["W3"])

    # Output Results & Save to Text File
    outputText += "\nResults of Simulation:\n"
    outputText += "Inspector 1 Avg. Inspection Time (C1): " + inspectC1 + "\n"
    outputText += "Inspector 2 Avg. Inspection Time (C2): " + inspectC2 + "\n"
    outputText += "Inspector 2 Avg. Inspection Time (C3): " + inspectC3 + "\n"

    outputText += "Inspector 1 Avg. Blocked Time (C1): " + blockedC1 + "\n"
    outputText += "Inspector 2 Avg. Blocked Time (C2): " + blockedC2 + "\n"
    outputText += "Inspector 2 Avg. Blocked Time (C3): " + blockedC3 + "\n"

    outputText += "Workstation 1 Avg. Process Time: " + processW1 + "\n"
    outputText += "Workstation 2 Avg. Process Time: " + processW2 + "\n"
    outputText += "Workstation 3 Avg. Process Time: " + processW3 + "\n"

    outputText += "Workstation 1 Avg. Idle Time: " + idleW1 + "\n"
    outputText += "Workstation 2 Avg. Idle Time: " + idleW2 + "\n"
    outputText += "Workstation 3 Avg. Idle Time: " + idleW3 + "\n"

    outputText += "Total P1 Produced: " + P1total + "\n"
    outputText += "Total P2 Produced: " + P2total + "\n"
    outputText += "Total P3 Produced: " + P3total + "\n"

    # Calculate throughput (products / unit time)
    throughputW1 = numpy.mean(modelProductsCreated["P1"] / simTime)
    throughputW2 = numpy.mean(modelProductsCreated["P2"] / simTime)
    throughputW3 = numpy.mean(modelProductsCreated["P3"] / simTime)

    # Calculate avg time spent in queue using workstation idle time
    avgTimeInBufferW1 = numpy.mean(modelWorkstationIdleTimes["W1"])
    avgTimeInBufferW2 = numpy.mean(modelWorkstationIdleTimes["W2"])
    avgTimeInBufferW3 = numpy.mean(modelWorkstationIdleTimes["W3"])

    # Output Little Law Results for all Workstations
    outputText += (
        "Avg. Buffer Occupancy using Little's Law for W1: "
        + littleLawCalc(throughputW1, avgTimeInBufferW1)
        + "\n"
    )
    outputText += (
        "Avg. Buffer Occupancy using Little's Law for W2: "
        + littleLawCalc(throughputW2, avgTimeInBufferW2)
        + "\n"
    )
    outputText += (
        "Avg. Buffer Occupancy using Little's Law for W3: "
        + littleLawCalc(throughputW3, avgTimeInBufferW3)
        + "\n"
    )

    # Output all of the outputText that has been saved till this point
    print(outputText)

    # Save result of simulation[i] to /results/simRun_i.txt
    saveOutputToFile(outputText, i)


# Define total # of replications and how long each replication simulates for
numberOfReplications = 10
simTime = 10000
policyNumber = 0  # 0 is used here to use the original operating policy

# Main loop of simulator, will repeat each simulation until numberOfReplications
for i in range(1, numberOfReplications + 1):
    runSimulation(simTime, policyNumber)
