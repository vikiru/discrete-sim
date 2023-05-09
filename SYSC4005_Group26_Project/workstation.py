# SYSC4005 Project - Group 26
# Author: Visakan Kirubakaran
# Year of Completion: Jan - Apr 2022

import simpy
from input_modeling import *


class Workstation1:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws1.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.process_time = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_time = {0: []}  # index 0 for w1
        self.idle_time = {0: []}  # index 0 for W1

    # Used to identify the Workstation
    def get_name(self):
        return "W1"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_time[0].append(end_time)
            process_time = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_time)
            self.process_time[0].append(process_time)
            self.products_created += 1


class Workstation2:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws2.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.c2_buffer = simpy.Container(self.env, 2, 0)
        self.process_time = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_time = {0: []}  # index 0 for w2
        self.idle_time = {0: []}  # Index 0 for W2

    # Used to identify the Workstation
    def get_name(self):
        return "W2"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1) and self.c2_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_time[0].append(end_time)
            process_time = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_time)
            self.process_time[0].append(process_time)
            self.products_created += 1


class Workstation3:
    # Initialize Workstation
    def __init__(self, env):
        self.env = env
        self.filename = "ws3.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.c3_buffer = simpy.Container(self.env, 2, 0)
        self.process_time = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_time = {0: []}  # index 0 for w3
        self.idle_time = {0: []}  # Index 0 for W3

    # Used to identify the Workstation
    def get_name(self):
        return "W3"

    # Main process loop,
    # Workstation will try to get its required components, if it is able to get a component then
    # it moves on to processing the component, updating both the idle and process time
    # lists respectively
    def run(self):
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1) and self.c3_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_time[0].append(end_time)
            process_time = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_time)
            self.process_time[0].append(process_time)
            self.products_created += 1
