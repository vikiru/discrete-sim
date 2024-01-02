<style>
    p {
        text-align: justify;
    }
</style>

## 🚀 Running the Simulator

<p align="justify">
This repository contains two simulators that model the behavior of a manufacturing facility under different operating policies. The original simulator implements the current policy that the facility follows, while the alternate simulator tests the current policy against the alternative policies that I have devised based on various criteria.
</p>

<p align="justify">
The original simulator runs for a fixed time period of t = 10000 units while the alternate simulator runs for a fixed time period of t = 50000 units. Every unique operating policy is repeated 10 times to obtain statistical estimates of the system performance in both simulators.
</p>

The original simulator can be started as follows:

```bash
python simulator.py
```

The alternate simulator can be started as follows:

```bash
python alternate_simulator.py
```

## 🔄 Alternate Simulator

<p align="justify">
The alternate simulator makes use of the simulator to run the original operating policy followed by the four alternative policies in succession.
</p>

<p align="justify">
The difference is that the simulation time is changed to t = 50000 from t = 10000 and each operating policy is run 10 times. The results of these simulations are stored within the results folder with sub-folders separating the results of each simulation run for each policy.
</p>
