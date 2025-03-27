def filter_nondigits(data: list) -> list:
    """  
Args: filters out strings that include non-digit characters
and creates a new list of data with just digits

Returns: a new list containing only integer values

Note: 
Check mark for 4+5 test: 
       new_list = []
    for data_a in data:
        if isinstance(data_a,int):
            new_list.append(data_a)   
    return new_list
    """
# filter out the strings within the dataset that do not include non-digit characters
    new_list = []
    for data_a in data:
        data_a = data_a.strip() # strips on non-digit charcaters in data set
        if data_a.isdigit():
            new_list.append(int(data_a))   
  
    return new_list
   



