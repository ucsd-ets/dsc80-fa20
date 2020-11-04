import pandas as pd
import numpy as np


def impute_with_index(dg):
    """
    impute (i.e. fill-in) the missing values of column B 
    with the value of the index for that row.

    :Example:
    >>> dg = pd.read_csv('data.csv', index_col=0)
    >>> out = impute_with_index(dg)
    >>> isinstance(out, pd.Series)
    True
    >>> out.isnull().sum() == 0
    True
    """

    return ...


def impute_with_digit(dg):
    """
    impute (i.e. fill-in) the missing values of each column 
    using the last digit of the value of column A.

    :Example:
    >>> dg = pd.read_csv('data.csv', index_col=0)
    >>> out = impute_with_digit(dg)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.isnull().sum().sum() == 0
    True
    """

    return ...
