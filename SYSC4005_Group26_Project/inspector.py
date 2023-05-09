# SYSC4005 Project - Group 26
# Author: Vis Kirubakaran 

import random
from input_modeling import *
from workstation import *


class Inspector1:
    # Initialize Inspector
    def __init__(self, env, workStationList, policyNumber):
        self.env = env
        self.workStationList = workStationList
        self.policyNumber = policyNumber
        self.filename = "servinsp1.dat"  # C1 inspection time file
        self.inspectTimeC1 = getInputDataMeanTime(self.filename)
        self.action = env.process(self.run())
        self.serviceTime = {0: []}  # Index 0 for C1
        self.blockedTime = {0: []}  # Index 0 for C1

    # Used to identify the Inspector
    def getName(self):
        return "Inspector 1"

    # Inspector 1 will determine the best workstation buffer to send its C1
    # component to, based on the smallest size of the buffer and adhering to
    # a priority based scheduling and finally return that workstation's buffer
    def determineMinBuffer(self):
        W1Buffer = self.workStationList[0].C1Buffer
        W2Buffer = self.workStationList[1].C1Buffer
        W3Buffer = self.workStationList[2].C1Buffer

        # Determine the minBuffer based on the Priority Order:
        # W1 > W2 > W3
        if W1Buffer.level <= (W2Buffer.level or W3Buffer.level):
            return W1Buffer
        elif W2Buffer.level <= W3Buffer.level:
            return W2Buffer
        else:
            return W3Buffer

    ## Alternate scheduling ideas:
    # 0) Original scheduling
    # 1) W1: 20%, W2, W3: 40-40%
    # 2) w1: 60%, w2, w3: 20-20%
    # 3) W1, W2, W3: 33.33%
    # 4) W3 > W2 > W1

    # The first alternative policy to improve the performance of the system,
    # by generating a random number between 1 and 10 and if the number
    # is in a specific range, return that workstation's buffer to place C1 into
    # This alternate policy focuses on giving workstation 2 and 3 more
    # probability of getting C1 (both have 40% chance, for a total
    # of 80% chance)
    # This means that workstation only has a 20% chance of getting C1
    def randomSchedulingLessProbabilityW1(self):
        W1Buffer = self.workStationList[0].C1Buffer
        W2Buffer = self.workStationList[1].C1Buffer
        W3Buffer = self.workStationList[2].C1Buffer

        # 20% chance to place C1 into W1
        # 40% chance to place C1 into W2 or W3
        W1 = [1, 2]
        W2 = [3, 4, 5, 6]
        W3 = [7, 8, 9, 10]

        # Generate a random number and return
        # corresponding buffer based on number
        num = random.randint(1, 10)
        if num in W2:
            return W2Buffer
        elif num in W3:
            return W3Buffer
        elif num in W1:
            return W1Buffer

    # The second alternative policy to improve the performance of the system,
    # by generating a random number between 1 and 10 and if the number
    # is in a specific range, return that workstation's buffer to place C1 into
    # This alternate policy focuses on giving workstation 1 more probability
    # of getting C1 (60% chance) while workstation 2 and 3 only have 20% chance
    def randomSchedulingMoreProbabilityW1(self):
        W1Buffer = self.workStationList[0].C1Buffer
        W2Buffer = self.workStationList[1].C1Buffer
        W3Buffer = self.workStationList[2].C1Buffer

        # 60% chance to place C1 into W1
        # 20% chance to place C1 into W2 or W3
        W1 = [1, 2, 3, 4, 5, 6]
        W2 = [7, 8]
        W3 = [9, 10]

        # Generate a random number and return
        # corresponding buffer based on number
        num = random.randint(1, 10)
        if num in W1:
            return W1Buffer
        elif num in W2:
            return W2Buffer
        elif num in W3:
            return W3Buffer

    # The third alternative policy to improve the performance of the system,
    # by generating a random number between 0 and 2 and use that number,
    # to return a workstation's buffer from the list of workstations
    # This alternate policy focuses on giving all workstation's equal probability
    # of getting C1, 33.33% chance for all
    def randomSchedulingEqualProbability(self):
        # 0 coressponds to W1, 1 coressponds to W2 and 2 coressponds to W3
        num = random.randint(0, 2)
        # Return the workstation's buffer
        return self.workStationList[num].C1Buffer

    # The fourth alternative policy to improve the performance of the system
    # This policy is essentially the same as the original policy except that
    # instead of W1 having the highest priority, it now has the lowest priority
    # As such, W3 > W2 > W1 is the new order of priority
    def reversePriorityScheduling(self):
        W1Buffer = self.workStationList[0].C1Buffer
        W2Buffer = self.workStationList[1].C1Buffer
        W3Buffer = self.workStationList[2].C1Buffer

        # Determine which buffer to return based on reverse priority order
        # W3 > W2 > W1
        if W3Buffer.level <= (W2Buffer.level or W1Buffer.level):
            return W3Buffer
        elif W2Buffer.level <= W1Buffer.level:
            return W2Buffer
        else:
            return W1Buffer

    # This will allow the inspector to choose its operating policy
    # based on an input number and upon utilizing the policy,
    # will return the respective workstation's buffer according to that
    # policy
    def policySelector(self):
        num = self.policyNumber
        if num == 0:
            return self.determineMinBuffer()
        elif num == 1:
            return self.randomSchedulingLessProbabilityW1()
        elif num == 2:
            return self.randomSchedulingMoreProbabilityW1()
        elif num == 3:
            return self.randomSchedulingEqualProbability()
        elif num == 4:
            return self.reversePriorityScheduling()

    # Main process loop
    def run(self):
        while True:
            # Generate a service time based on mean from file and append to
            # list of service times for C1
            inspectTimeC1 = generateRandomMeanTime(self.filename)
            self.serviceTime[0].append(inspectTimeC1)

            # Inspector is 'inspecting' the component
            yield self.env.timeout(inspectTimeC1)

            # Current time after inspecting
            currTime = self.env.now

            # Inspector finishes inspection and puts C1 into the min buffer
            yield self.policySelector().put(1)

            # Determine blocked time total and append to blockedTime list
            totalTimeBlocked = self.env.now - currTime
            self.blockedTime[0].append(totalTimeBlocked)


class Inspector2:
    # Initialize Inspector
    def __init__(self, env, workStationList):
        self.env = env
        self.workStationList = workStationList
        self.filename1 = "servinsp22.dat"  # C2 inspection time file
        self.filename2 = "servinsp23.dat"  # C3 inspection time file
        self.inspectTimeC2 = getInputDataMeanTime(self.filename1)
        self.inspectTimeC3 = getInputDataMeanTime(self.filename2)
        self.action = env.process(self.run())
        self.serviceTime = {0: [], 1: []}  # Index 0 for C2, 1 for C3
        self.blockedTime = {0: [], 1: []}  # Index 0 for C2, 1 for C3

    # Used to identify the Inspector
    def getName(self):
        return "Inspector 2"

    def getRandomComponent(self):
        # 0 corresponds to C2, 1 corresponds to C3
        return random.randint(0, 1)

    # Main process loop
    def run(self):
        while True:
            if self.getRandomComponent() == 0:
                # Generate a service time based on mean from file and append to
                # list of service times for C2
                inspectTimeC2 = generateRandomMeanTime(self.filename1)
                self.serviceTime[0].append(inspectTimeC2)

                # Inspector is 'inspecting' the component
                yield self.env.timeout(inspectTimeC2)

                # Current time after inspecting
                currTime = self.env.now

                # Inspector finishes inspection and puts C2 into the buffer
                yield self.workStationList[0].C2Buffer.put(1)

                # Determine blocked time total and append to blockedTime list
                totalTimeBlocked = self.env.now - currTime
                self.blockedTime[0].append(totalTimeBlocked)
            else:
                # Generate a service time based on mean from file and append to
                # list of service times for C3
                inspectTimeC3 = generateRandomMeanTime(self.filename2)
                self.serviceTime[1].append(inspectTimeC3)

                # Inspector is 'inspecting' the component
                yield self.env.timeout(inspectTimeC3)

                # Current time after inspecting
                currTime = self.env.now

                # Inspector finishes inspection and puts C3 into the buffer
                yield self.workStationList[1].C3Buffer.put(1)

                # Determine blocked time total and append to blockedTime list
                totalTimeBlocked = self.env.now - currTime
                self.blockedTime[1].append(totalTimeBlocked)
