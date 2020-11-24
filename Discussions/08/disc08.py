from glob import glob
import pandas as pd
import numpy as np

from scipy.stats import linregress


def rmse(datasets):
    """
    Return the RMSE of each of the datasets.

    >>> datasets = {k:pd.read_csv('data/dataset_%d.csv' % k) for k in range(7)}    
    >>> out = rmse(datasets)
    >>> len(out) == 7
    True
    >>> isinstance(out, pd.Series)
    True
    """

    return ...


def heteroskedasticity(datasets):
    """
    Return a boolean series giving whether a dataset is
    likely heteroskedastic.

    >>> datasets = {k:pd.read_csv('data/dataset_%d.csv' % k) for k in range(7)}    
    >>> out = heteroskedasticity(datasets)
    >>> len(out) == 7
    True
    >>> isinstance(out, pd.Series)
    True
    """

    return ...
