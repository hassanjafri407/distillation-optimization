## Overview

This project analyzes the trade-off between product purity and energy consumption in a benzene–toluene distillation column.

A sensitivity analysis was performed in Aspen Plus by varying the reflux ratio. The simulation results were exported to CSV and analyzed in Python to determine how energy requirements change with increasing product purity. The project also identifies an optimal operating region using knee point detection.

---

## Objectives

- Simulate a benzene–toluene distillation column in Aspen Plus
- Perform a sensitivity analysis by varying reflux ratio
- Export simulation results to CSV
- Analyze results using Python
- Calculate total energy consumption
- Visualize energy vs. purity
- Identify the optimal operating point using the KneeLocator algorithm

---

## Methodology

1. Built a benzene–toluene distillation column in Aspen Plus.
2. Performed a sensitivity analysis by varying the reflux ratio.
3. Recorded:
   - Reboiler duty
   - Condenser duty
   - Benzene purity
   - Toluene purity
4. Exported the results to CSV.
5. Used Python to:
   - Clean the data
   - Calculate total energy consumption
   - Plot energy versus benzene purity
   - Detect the knee point representing the best trade-off between purity and energy consumption

---

## Tools Used

- Aspen Plus V14
- Python 3
- Pandas
- NumPy
- Matplotlib
- kneed

---

## Results

The sensitivity analysis demonstrated the expected trade-off between product purity and energy consumption. Increasing the reflux ratio increased benzene purity but required substantially higher reboiler and condenser duties.

A knee point analysis was performed to identify an operating region where further increases in purity produced diminishing returns in energy efficiency.

The generated plots are available in the `figures/` folder.

The optimal purity was found to be 99.89% pure benzene 
