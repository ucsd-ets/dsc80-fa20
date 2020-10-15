
import numpy as np
import pandas as pd
import os


def question01(data, labels):
    """
    Returns a dataframe from the
    given data (a dictionary of lists),
    and list of labels.

    >>> data = {'column1': [0,3,5,6], 'column2': [1,3,2,4]}
    >>> labels = 'a b c d'.split()
    >>> out = question01(data, labels)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.index.tolist() == labels
    True
    """

    return ...


def question02(ser):
    """
    Given a Pandas Series, outputs the
    positions (an index or array) of 
    entries of ser that are multiples of 3.

    >>> ser = pd.Series([1, 3, 6, 9])
    >>> out = question02(ser)
    >>> out.tolist() == [1, 2, 3]
    True
    """

    return ...


