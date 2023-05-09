# SYSC4005 Project - Group 26
# Author: Vis Kirubakaran 

import simpy
from input_modeling import *


class Workstation1:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws1.dat"
        self.C1Buffer = simpy.Container(self.env, 2, 0)
        self.processTime = getInputDataMeanTime(self.filename)
        self.action = env.process(self.run())
        self.productsCreated = 0
        self.processTime = {0: []}  # Index 0 for W1
        self.idleTime = {0: []}  # Index 0 for W1

    # Used to identify the Workstation
    def getName(self):
        return "W1"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            startTime = self.env.now
            yield self.C1Buffer.get(1)
            endTime = self.env.now - startTime
            self.idleTime[0].append(endTime)
            processTime = generateRandomMeanTime(self.filename)
            yield self.env.timeout(processTime)
            self.processTime[0].append(processTime)
            self.productsCreated += 1


class Workstation2:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws2.dat"
        self.C1Buffer = simpy.Container(self.env, 2, 0)
        self.C2Buffer = simpy.Container(self.env, 2, 0)
        self.processTime = getInputDataMeanTime(self.filename)
        self.action = env.process(self.run())
        self.productsCreated = 0
        self.processTime = {0: []}  # Index 0 for W2
        self.idleTime = {0: []}  # Index 0 for W2

    # Used to identify the Workstation
    def getName(self):
        return "W2"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            startTime = self.env.now
            yield self.C1Buffer.get(1) and self.C2Buffer.get(1)
            endTime = self.env.now - startTime
            self.idleTime[0].append(endTime)
            processTime = generateRandomMeanTime(self.filename)
            yield self.env.timeout(processTime)
            self.processTime[0].append(processTime)
            self.productsCreated += 1


class Workstation3:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws3.dat"
        self.C1Buffer = simpy.Container(self.env, 2, 0)
        self.C3Buffer = simpy.Container(self.env, 2, 0)
        self.processTime = getInputDataMeanTime(self.filename)
        self.action = env.process(self.run())
        self.productsCreated = 0
        self.processTime = {0: []}  # Index 0 for W3
        self.idleTime = {0: []}  # Index 0 for W3

    # Used to identify the Workstation
    def getName(self):
        return "W3"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            startTime = self.env.now
            yield self.C1Buffer.get(1) and self.C3Buffer.get(1)
            endTime = self.env.now - startTime
            self.idleTime[0].append(endTime)
            processTime = generateRandomMeanTime(self.filename)
            yield self.env.timeout(processTime)
            self.processTime[0].append(processTime)
            self.productsCreated += 1
