"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt

def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
        
       Note to self: 
    cleaned_data = []
    with open ('/Users/vanessawilliams/Downloads/hr_monitoring_data_processing/data/phase0.txt', 'r') as file:
        for line in text_file:
        line = line.strip()
    if line.isdigit():
        cleaned_data.append(int(line))
        
    text_file.close()
    return cleaned_data

    """ 
    #r = Read
    #a = Append
    #w = Write
    #x = Create

# open file using file I/O and read it into the `data` l
    data = []
    with open (filename, 'r') as file:
        data = file.readlines()
        

# Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable   
# Filters through all of the text files to remove non-numerical values 
    filtered_data = filter_nondigits (data)


# plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.plot(filtered_data)
    plt.savefig('images/plot.png')
    plt.xlabel ('Time')
    plt.ylabel('Heart Rate') 
       

# calculate the average, maximum, and standard deviation of this file using the functions you've wrote

     
    avg_hr = average(filtered_data)


    max_hr = maximum(filtered_data)


    std_dev_hr = standard_deviation(filtered_data)

    # return all 3 values return avg_hr, max_hr, std_dev_hr
    return avg_hr,max_hr,std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
