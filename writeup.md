## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

After reviewing the data in the file labeled 'data/phase0.txt', there were instance in the file where there was missing vlaues or "NO DATA" in the data set. This could be mean that there was insufficent data, inaccuraties in capture or reporting, or the heart analysis device was not recording all of the information. 


A good rule of thumb, is that it better to have bad data in your files than to have no data at all. With that, there are risk when filtering out non-digit values from my dat set. It can cause the findings or results to be flawed or inaccurate, especially if there is lack of vialbe data avaliable in the data files. The less data you have can make it harder perfrom adequate analysis of datasets. 

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

After reviewing the descriptive statistics and visualizations, the phase in which sleep occurs is usually when the BPM is between 40 to 50 BPM. We can see that during the time phase of 0-40, sleep is usually occurring. We do see that some of the data shows that in some instances the BPM does exceed the 50 BPM mark during the usual sleep schedule. 

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

The phase(s) where exercise occurs is usually when the heart rate goes above 100 BPM when compared to a resting heart rate that is usually between 60 to 100 BPM. Based on our visualization, we can see that around the 20-40 time period is where the highest heart rate occurs. We do see a spike in the green and red lines during the time periods of 0-20 and 60-80 respectively. 

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Based on the information, we know that if the average is lower than 65 and the standard deviation is higher than 9.5 we can see that is usually the trend occurs. The phase that it demonstrated in the visualization is between the time phase of 20-60, where it dips lower than the heart rate of 60 BPMs.
