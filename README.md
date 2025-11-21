# Health Monitoring Data Processing

A prototype data-processing application for Seng-Links, a Taiwan-based wearable health-tech company.This project ingests 8 hours of user-submitted heart-rate data and performs basic analytics to help developers prototype a future sleep-quality evaluation system.

The goal of this prototype is to:

 - Clean and validate raw heart-rate samples recorded every 5 minutes

- Filter out erroneous data

- Compute descriptive statistics (average, max, variance, standard deviation)

- Identify patterns that correspond to sleep or exercise

- Visualize heart-rate changes over time

- Provide a foundation for future hardware/software integration


## Overview


Wearable devices often produce noisy or partially corrupted data. Before meaningful analysis can occur, the data must be validated and cleaned.

This project processes four provided heart-rate data files located in the data/ folder.
Each file contains 5-minute interval samples, but some contain invalid values such as strings with non-digit characters.

This application:

Cleans raw data using strict digit-validation

Calculates descriptive metrics using base Python (no external stats libraries)

Visualizes heart-rate trends using Matplotlib

Supports test-driven development via provided unit tests

Assists developers in simulating sleep/exercise detection logic for future products
## Installation

Install the follinwg dependencies: 

```bash
  pip install matplotlib
```
The file also includes the prefix test_ python notebooks to test your code to ensure that the project meets the need requirements. Do not modify the code in these files, as the you will not be able to check that your code is functioning properly. 
    
## Test Python Files

Vakudate each module in your terminal before continuing: 

**Test Cleaner**
```bash
  python test_clean.py
```

**Test Metrics**
```bash
  python test_metrics.py
```


**Test Main**
```bash
  python test_run.py
```


## Exploratory Data Analysis (EDA)

Possible key analytical questions to analyze your data:

 - Take a look at the file labeled data/phase0.txt. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?


 - During sleep, we expect maximum heart rate of a phase to be lower than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

- During exercise, we expect the maximum heart rate of a phase to be higher the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings.

- During regular periods of awake activity, we expect the average heart rate of a phase to be relatively lower than the average heart rate of other phases, but we also expect standard deviation to be higher. In which phase do we notice this trend?
