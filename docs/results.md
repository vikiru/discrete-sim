# Understanding the Results

## Folder Descriptions

<p align="justify">
The data folder contains the input data that is required for the simulation of the manufacturing facility. This data includes the servicing times of the inspectors who check the quality of the components, and the processing times of the workstations that assemble the components into products. 
</p>

<p align="justify">
The policy comparison folder contains a text files that compare the performance of the original policy and the four alternative policies that were proposed to improve the efficiency of the facility. Each policy was simulated for a time period of t = 50000 units, which represents the duration of the production cycle. 
</p>

<p align="justify">
The results folder contains sub-folders for each policy, where the simulation results are stored as .txt files. Each file contains information such as the number of products produced, the average waiting time of the workstations, and the utilization rate of the workstations.
</p>

## Example Results File

```text
Starting simulation [1 / 10] and running for time, t = 50000
Results of Simulation for the Reverse Priority Policy:
Inspector 1 Avg. Inspection time (C1): 10.575921476912242 +/- 19.773488343937714
Inspector 2 Avg. Inspection time (C2): 15.835667543288643 +/- 31.094128215868412
Inspector 2 Avg. Inspection time (C3): 21.34088124702354 +/- 42.678475201986686
Inspector 1 Avg. Blocked time (C1): 10.575921476912242 +/- 19.773488343937714
Inspector 2 Avg. Blocked time (C2): 15.835667543288643 +/- 31.094128215868412
Inspector 2 Avg. Blocked time (C3): 21.34088124702354 +/- 42.678475201986686
Workstation 1 Avg. Process time: 4.748336194888908 +/- 9.049655785423548
Workstation 2 Avg. Process time: 10.768314794798476 +/- 20.884083311157
Workstation 3 Avg. Process time: 8.983340218115243 +/- 16.91454863433984
Workstation 1 Avg. Idle time: 25.99831098712895 +/- 101.4478864559243
Workstation 2 Avg. Idle time: 28.37159739712838 +/- 81.18074177245032
Workstation 3 Avg. Idle time: 27.432906626100785 +/- 65.04508602887152
Total P1 produced: 1625
Total P2 produced: 1277
Total P3 produced: 1373
Avg. Buffer Occupancy Using Little's Law For W1: 0.8449451070816909
Avg. Buffer Occupancy Using Little's Law For W2: 0.7246105975226588
Avg. Buffer Occupancy Using Little's Law For W3: 0.7533076159527275
```

## Policy Comparion Folder

A comparison of each of the operating policies simulated at a time, t = 50000 units of time can be found [here](https://github.com/vikiru/discrete-sim/tree/main/policy_comparison/).

## Result Folders

- [Original Policy](https://github.com/vikiru/discrete-sim/results/tree/main/original_policy/)
- [Random Policy - Equal Probability for C1](https://github.com/vikiru/discrete-sim/tree/main/results/random_policy_equal_probability/)
- [Random Policy - Less Probability W1](https://github.com/vikiru/discrete-sim/tree/main/results/random_policy_equal_probability/)
- [Random Policy - More Probability W1](https://github.com/vikiru/discrete-sim/tree/main/results/random_policy_equal_probability/)
- [Reverse Priority](https://github.com/vikiru/discrete-sim/tree/main/results/reverse_priority/)
