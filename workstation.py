# SYSC4005 Project - Group 26
# Author: Visakan Kirubakaran
# Year of Completion: Jan - Apr 2022

import simpy
from input_modeling import *


class Workstation1:
    def __init__(self, env):
        """Initialize Workstation1 with default values."""
        
        self.env = env
        self.filename = "ws1.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.process_time = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_times = {0: []}  # index 0 for w1
        self.idle_times = {0: []}  # index 0 for W1

    def get_name(self):
        """Used to identify Workstation1."""
        
        return "W1"

    def run(self):
        """
        Main process loop, Workstation1 will try to get its required components, if it
        is able to get a component then it moves on to processing the component, updating
        both the idle and process time lists respectively.
        """
        
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_times[0].append(end_time)
            process_times = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_times)
            self.process_times[0].append(process_times)
            self.products_created += 1


class Workstation2:
    def __init__(self, env):
        """Initialize Workstation2 with default values."""
        
        self.env = env
        self.filename = "ws2.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.c2_buffer = simpy.Container(self.env, 2, 0)
        self.process_times = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_times = {0: []}  # index 0 for w2
        self.idle_times = {0: []}  # Index 0 for W2

    def get_name(self):
        """Used to identify Workstation2."""
        
        return "W2"

    def run(self):
        """
        Main process loop, Workstation2 will try to get its required components, if it
        is able to get a component then it moves on to processing the component, updating
        both the idle and process time lists respectively.
        """
        
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1) and self.c2_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_times[0].append(end_time)
            process_times = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_times)
            self.process_times[0].append(process_times)
            self.products_created += 1


class Workstation3:
    def __init__(self, env):
        """Initialize Workstation3 with default values."""
        
        self.env = env
        self.filename = "ws3.dat"
        self.c1_buffer = simpy.Container(self.env, 2, 0)
        self.c3_buffer = simpy.Container(self.env, 2, 0)
        self.process_times = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.products_created = 0
        self.process_times = {0: []}  # index 0 for w3
        self.idle_times = {0: []}  # Index 0 for W3

    def get_name(self):
        """Used to identify Workstation3."""
        
        return "W3"

    def run(self):
        """
        Main process loop, Workstation3 will try to get its required components, if it
        is able to get a component then it moves on to processing the component, updating
        both the idle and process time lists respectively.
        """
        
        while True:
            start_time = self.env.now
            yield self.c1_buffer.get(1) and self.c3_buffer.get(1)
            end_time = self.env.now - start_time
            self.idle_times[0].append(end_time)
            process_times = generate_random_mean_time(self.filename)
            yield self.env.timeout(process_times)
            self.process_times[0].append(process_times)
            self.products_created += 1