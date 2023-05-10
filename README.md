[![License](https://img.shields.io/badge/license-MIT-aqua)](./LICENSE)



<h1 align="center"> SYSC4005 <br> Discrete Simulation Project </h1>

## Project Description
<blockquote align="justify">
The manufacturing facility produces different products (P1, P2, P3) using different combinations of raw components (C1, C2, C3). The components are cleaned and repaired by two inspectors before being sent to workstations (W1, W2, W3) that have buffers for storing them. The inspectors may get blocked if the buffers are full. The workstations start assembling products when they have all the required components. Inspector 1 sends component C1 to the workstation with the shortest queue, while Inspector 2 sends components C2 and C3 randomly. To produce the three products, the following combinations of components are used: P1 is made from C1, P2 is made from C1 and C2, and P3 is made from C1 and C3.
</blockquote>

<p align="justify">
This repository showcases my term project for SYSC4005, in which I developed a discrete simulation model of a manufacturing facility based on the given problem statement. The purpose of this simulation study was to identify and evaluate an alternative operating policy that could enhance the system performance.
</p>
   
## Prerequisites

- [Python](https://www.python.org/downloads/)
   - [NumPy](https://numpy.org/install/)
   - [SciPy](https://scipy.org/install/)
   - [SimPy](https://pypi.org/project/simpy/)

## Setup Instructions

1. Clone this repository to your local machine.

```bash
git clone https://github.com/vikiru/discrete-sim.git
```

2. Install all required Python dependencies (NumPy, SciPy, SimPy)

```bash
pip install -r requirements.txt
```

# Running the Simulator

<p align="justify">
This repository contains two simulators that model the behavior of a manufacturing facility under different operating policies. The original simulator implements the current policy that the facility follows, while the alternate simulator tests the current policy against the alternative policies that I have devised based on various criteria. The original simulator runs for a fixed time period of t = 10000 units while the alternate simulator runs for a fixed time period of t = 50000 units. Every unique operating policy is repeated 10 times to obtain statistical estimates of the system performance in both simulators.
</p>

The original simulator can be started as follows:

```bash
python simulator.py
```

The alternate simulator can be started as follows:

```bash
python alternate_simulator.py
```

# Understanding the Results

<p align="justify">
The data folder contains the input data that is required for the simulation of the manufacturing facility. This data includes the servicing times of the inspectors who check the quality of the components, and the processing times of the workstations that assemble the components into products. 
</p>

<p align="justify">
The policy comparison folder contains a text files that compare the performance of the original policy and the four alternative policies that were proposed to improve the efficiency of the facility. Each policy was simulated for a time period of t = 50000 units, which represents the duration of the production cycle. 
</p>

<p align="justify">
The results folder contains sub-folders for each policy, where the simulation results are stored as .txt files. Each file contains information such as the number of products produced, the average waiting time of the workstations, and the utilization rate of the workstations.
</p>

## Acknowledgements
- Uses [NumPy](https://numpy.org/) for generating random values based on an exponential distribution.
- Uses [SciPy](https://scipy.org/) for statistical functions.
- Uses [SimPy](https://simpy.readthedocs.io/en/latest/) to simulate the manufacturing facility.

## License

The contents of this repository are licensed under the terms and conditions of the [MIT](https://choosealicense.com/licenses/mit/) license.

[MIT](https://github.com/vikiru/discrete-sim/blob/update-readme/LICENSE) © 2023 Visakan Kirubakaran.
