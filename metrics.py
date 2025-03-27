def average(data: list) -> float:

    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list

    """
    
    average = 0

    if data == []: 
        return []
    for value in data:
        average += value

    return round(average/len(data),2)
           
#result = average([1, 2, 3, 4, 5, 6, 7]) 
       
...
def maximum(data: list) -> float:
    
    """ 
    Calculate maximum value of the list.
    
    Args:
        data (list[int]): list of integers representing heart rate samples.
    Returns:
        float: a floating point value representing the maxium of this list.

    """   
    max = 0
    for value in data: 
        if value > max:
            max = value
    if max == 0:
        return []
    return max


def variance(data: list) -> float:
  
    """
    Calculate variance of the list.
    
    Args:
        data (list[int]): list of integers representing heart rate samples.
    Returns:
        float: a floating point value representing the variance of this list.
    
    """
    if data == []: 
        return []
    
    variance = 0 
    for value in data:
        variance += (value-average(data))**2
  
    return round(variance / len(data),2)


def standard_deviation(data: list) -> float:
    """
     Calculates the population standard deviation of a list of numbers

    Args:
        data: A list of numerical data.

    Returns:
        The population variance of the data.
    """
    if not data: 
        return []

    return round(variance(data) ** 0.5,2) # returns standard deviation
    


