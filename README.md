# Singapore-Exports-Data-Analysis

## Overview
A Python program that analyzes Singapore’s export data from 1998 to 2009. The program allows users to view export values for different regions, calculate average and maximum exports, identify significant increases or decreases (≥15%), and visualize trends using line and bar plots. Built using Python, CSV, NumPy, and Matplotlib.

## Technologies Used
Python • CSV • NumPy • Matplotlib • Data Analysis

## Features
- Display annual export values for a selected region.
- Calculate the average and maximum export value over a specific period.
- Identify years with export changes greater than ±15% compared to the previous year.
- Generate line plots to show trends for specific regions.
- Generate bar charts to display total export values across all regions.
- Menu-driven interface to easily select desired operations.

## How It Works
1. The program reads data from a CSV file (`sgexports_dataset.csv`) and stores it in arrays.
2. Users select an option from the menu.
3. Based on the option, the program performs calculations using NumPy and displays the results.
4. Visualization is done with Matplotlib to show trends over time.
5. Significant changes are detected by comparing consecutive yearly values.


## How to Run

1.make sure Python 3 is installed on your computer.

2.Install the required libraries:
```bash
pip install numpy matplotlib
```

3.choose a directory and create a folder.

4.go to the project directory.

5.clone the project on a new terminal with
```bash
git clone https://github.com/Pythonista-dev-cyber/Singapore-Exports-Data-Analysis.git

```


6.make sure both sg_exports_analysis.py and sgexports_dataset 2.csv are in the same folder.

7.run this 
```bash
python sg_exports_analysis.py
```
on the terminal.

5.Follow the on screen menu.

