
<h1 align="center"> SYSC4005 <br> Discrete Simulation Project </h1>

## Project Description
<blockquote align="justify">
The manufacturing facility produces different products (P1, P2, P3) using different combinations of raw components (C1, C2, C3). The components are cleaned and repaired by two inspectors before being sent to workstations (W1, W2, W3) that have buffers for storing them. The inspectors may get blocked if the buffers are full. The workstations start assembling products when they have all the required components. Inspector 1 sends component C1 to the workstation with the shortest queue, while Inspector 2 sends components C2 and C3 randomly. To produce the three products, the following combinations of components are used: P1 is made from C1, P2 is made from C1 and C2, and P3 is made from C1 and C3.
</blockquote>

<p align="justify">
This repository showcases my term project for SYSC4005, in which I developed a discrete simulation model of a manufacturing facility based on the given problem statement. The purpose of this simulation study was to identify and evaluate an alternative operating policy that could enhance the system performance.
</p>
   
## Prerequisites

- [Python](https://www.python.org/downloads/).
   - [NumPy](https://numpy.org/install/)
   - [SciPy](https://scipy.org/install/)
   - [SimPy](https://pypi.org/project/simpy/)

## Setup & Install Instructions

1. Clone this repository to your local machine.

```bash
git clone https://github.com/vikiru/discrete-sim.git
```

2. Install all required Python dependencies (NumPy, SciPy, SimPy)

```bash
pip install -r requirements.txt
```

3. cd to project root 


# Running the Simulator

# Understanding the Results

## Acknowledgements
- Uses [NumPy](https://numpy.org/)
- Uses [SciPy](https://scipy.org/)
- Uses [SimPy](https://simpy.readthedocs.io/en/latest/)

## License
