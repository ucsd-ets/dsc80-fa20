
import numpy as np
import os

def data2array(filepath):
    """
    data2array takes in the filepath of a 
    data file like `restaurant.csv` in 
    data directory, and returns a 1d array
    of data.

    :Example:
    >>> fp = os.path.join('data', 'restaurant.csv')
    >>> arr = data2array(fp)
    >>> isinstance(arr, np.ndarray)
    True
    >>> arr.dtype == np.dtype('float64')
    True
    >>> arr.shape[0]
    100000
    """

    result = np.genfromtxt(filepath)
    #get rid of first one since it is title
    return result[1:len(result)]


def ends_in_9(arr):
    """
    ends_in_9 takes in an array of dollar amounts 
    and returns the proprtion of values that end 
    in 9 in the hundredths place.

    :Example:
    >>> arr = np.array([23.04, 45.00, 0.50, 0.09])
    >>> out = ends_in_9(arr)
    >>> 0 <= out <= 1
    True
    """

    copy = arr
    copy = copy * 100
    #round to int
    copy = np.round(copy,0)
    left = copy % 10
    # count number of 9 in the array
    count = (left == 9).sum()
    # find total number in the array
    total = arr.shape[0]
    return count/total
