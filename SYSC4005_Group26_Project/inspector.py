# sysc4005 project - group 26
# author: vis kirubakaran

import random
from input_modeling import *
from workstation import *


class Inspector1:
    def __init__(self, env, work_station_list, policy_number):
        """Initialize Inspector1 with default values."""
        self.env = env
        self.work_station_list = work_station_list
        self.policy_number = policy_number
        self.filename = "servinsp1.dat"  # c1 inspection time file
        self.inspect_time_c1 = get_input_data_mean_time(self.filename)
        self.action = env.process(self.run())
        self.service_times = {0: []}  # index 0 for c1
        self.blocked_times = {0: []}  # index 0 for c1

    def get_name(self):
        """Used to identify Inspector1."""
        return "Inspector 1"

    def determine_min_buffer(self):
        """
        Inspector 1 will determine the best workstation buffer to send its c1
        component to, based on the smallest size of the buffer.Adhering to
        a priority-based scheduling and finally return that workstation's buffer.
        """
        w1_buffer = self.work_station_list[0].c1_buffer
        w2_buffer = self.work_station_list[1].c1_buffer
        w3_buffer = self.work_station_list[2].c1_buffer

        # determine the min_buffer based on the priority order:
        # w1 > w2 > w3
        if w1_buffer.level <= (w2_buffer.level or w3_buffer.level):
            return w1_buffer
        elif w2_buffer.level <= w3_buffer.level:
            return w2_buffer
        else:
            return w3_buffer

    # Alternate scheduling ideas:
    # 0) original scheduling
    # 1) w1: 20%, w2, w3: 40-40%
    # 2) w1: 60%, w2, w3: 20-20%
    # 3) w1, w2, w3: 33.33%
    # 4) w3 > w2 > w1

    def random_scheduling_less_probability_w1(self):
        """
        The first alternative policy to improve the performance of the system,
        by generating a random number between 1 and 10 and if the number
        is in a specific range, return that workstation's buffer to place C1 into.

        This alternate policy focuses on giving workstation 2 and 3 more
        probability of getting C1 (both have 40% chance, for a total of 80% chance),
        this means that workstation 1 only has a 20% chance of getting C1.
        """
        w1_buffer = self.work_station_list[0].c1_buffer
        w2_buffer = self.work_station_list[1].c1_buffer
        w3_buffer = self.work_station_list[2].c1_buffer

        # 20% chance to place c1 into w1
        # 40% chance to place c1 into w2 or w3
        w1 = [1, 2]
        w2 = [3, 4, 5, 6]
        w3 = [7, 8, 9, 10]

        # generate a random number and return corresponding buffer based on number
        num = random.randint(1, 10)
        if num in w2:
            return w2_buffer
        elif num in w3:
            return w3_buffer
        elif num in w1:
            return w1_buffer

    def random_scheduling_more_probability_w1(self):
        """
        The second alternative policy to improve the performance of the system,
        by generating a random number between 1 and 10 and if the number is
        in a specific range, return that workstation's buffer to place c1 into.

        This alternate policy focuses on giving workstation 1 more probability
        of getting C1 (60% chance) while workstation 2 and 3 only have 20% chance.
        """
        w1_buffer = self.work_station_list[0].c1_buffer
        w2_buffer = self.work_station_list[1].c1_buffer
        w3_buffer = self.work_station_list[2].c1_buffer

        # 60% chance to place c1 into w1
        # 20% chance to place c1 into w2 or w3
        w1 = [1, 2, 3, 4, 5, 6]
        w2 = [7, 8]
        w3 = [9, 10]

        # generate a random number and return
        # corresponding buffer based on number
        num = random.randint(1, 10)
        if num in w1:
            return w1_buffer
        elif num in w2:
            return w2_buffer
        elif num in w3:
            return w3_buffer

    def random_scheduling_equal_probability(self):
        """
        The third alternative policy to improve the performance of the system,
        by generating a random number between 0 and 2 and use that number,
        to return a workstation's buffer from the list of workstations.

        This alternate policy focuses on giving all workstation's equal probability
        of getting C1, 33.33% chance for all workstations.
        """
        # 0 coressponds to w1, 1 coressponds to w2 and 2 coressponds to w3
        num = random.randint(0, 2)
        # return the workstation's buffer
        return self.work_station_list[num].c1_buffer

    def reverse_priority_scheduling(self):
        """
        The fourth alternative policy to improve the performance of the system.

        This policy is essentially the same as the original policy except that
        instead of w1 having the highest priority, it now has the lowest priority
        as such, w3 > w2 > w1 is the new order of priority.
        """
        w1_buffer = self.work_station_list[0].c1_buffer
        w2_buffer = self.work_station_list[1].c1_buffer
        w3_buffer = self.work_station_list[2].c1_buffer

        # determine which buffer to return based on reverse priority order
        # w3 > w2 > w1
        if w3_buffer.level <= (w2_buffer.level or w1_buffer.level):
            return w3_buffer
        elif w2_buffer.level <= w1_buffer.level:
            return w2_buffer
        else:
            return w1_buffer

    def policy_selector(self):
        """
        Allow the inspector to choose its operating policy based on an input policy number.
        Based on given policy number, the corresponding workstation's buffer is returned.
        """
        num = self.policy_number
        if num == 0:
            return self.determine_min_buffer()
        elif num == 1:
            return self.random_scheduling_less_probability_w1()
        elif num == 2:
            return self.random_scheduling_more_probability_w1()
        elif num == 3:
            return self.random_scheduling_equal_probability()
        elif num == 4:
            return self.reverse_priority_scheduling()

    def run(self):
        """Main process loop for Inspector1 where it will simulate inspection of components and placing into respective workstations."""
        while True:
            # generate a service time based on mean from file and append to
            # list of service times for c1
            inspect_time_c1 = generate_random_mean_time(self.filename)
            self.service_times[0].append(inspect_time_c1)

            # inspector is 'inspecting' the component
            yield self.env.timeout(inspect_time_c1)

            # current time after inspecting
            curr_time = self.env.now

            # inspector finishes inspection and puts c1 into the min buffer
            yield self.policy_selector().put(1)

            # determine blocked time total and append to blocked_times list
            total_time_blocked = self.env.now - curr_time
            self.blocked_times[0].append(total_time_blocked)


class Inspector2:
    def __init__(self, env, work_station_list):
        """Initialize Inspector2 with default values."""
        self.env = env
        self.work_station_list = work_station_list
        self.filename_1 = "servinsp22.dat"  # c2 inspection time file
        self.filename_2 = "servinsp23.dat"  # c3 inspection time file
        self.inspect_time_c2 = get_input_data_mean_time(self.filename_1)
        self.inspect_time_c3 = get_input_data_mean_time(self.filename_2)
        self.action = env.process(self.run())
        self.service_times = {0: [], 1: []}  # index 0 for c2, 1 for c3
        self.blocked_times = {0: [], 1: []}  # index 0 for c2, 1 for c3

    def get_name(self):
        """Used to identify Inspector2."""
        return "Inspector 2"

    def get_random_component(self):
        """Generate a random number between 0 and 1, 0 refers to a component C2 and 1 refers to a component C3."""
        return random.randint(0, 1)

    def run(self):
        """Main process loop for Inspector2 where it will simulate inspection of components and placing into respective workstations."""
        while True:
            if self.get_random_component() == 0:
                # generate a service time based on mean from file and append to
                # list of service times for c2
                inspect_time_c2 = generate_random_mean_time(self.filename_1)
                self.service_times[0].append(inspect_time_c2)

                # inspector is 'inspecting' the component
                yield self.env.timeout(inspect_time_c2)

                # current time after inspecting
                curr_time = self.env.now

                # inspector finishes inspection and puts c2 into the buffer
                yield self.work_station_list[0].c2_buffer.put(1)

                # determine blocked time total and append to blocked_times list
                total_time_blocked = self.env.now - curr_time
                self.blocked_times[0].append(total_time_blocked)
            else:
                # generate a service time based on mean from file and append to
                # list of service times for c3
                inspect_time_c3 = generate_random_mean_time(self.filename_2)
                self.service_times[1].append(inspect_time_c3)

                # inspector is 'inspecting' the component
                yield self.env.timeout(inspect_time_c3)

                # current time after inspecting
                curr_time = self.env.now

                # inspector finishes inspection and puts c3 into the buffer
                yield self.work_station_list[1].c3_buffer.put(1)

                # determine blocked time total and append to blocked_times list
                total_time_blocked = self.env.now - curr_time
                self.blocked_times[1].append(total_time_blocked)
