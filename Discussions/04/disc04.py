
import numpy as np
import pandas as pd
import os


def combined_seasons(df1, df2):
    """
    Create a function that return, as a tuple, a dataframe combining
    the 2017 and 2018 MLB seasons as well as the team that hit the most
    homeruns between the two seasons.

    :Example:
    >>> mlb_2017 = pd.read_csv(os.path.join('data','mlb_2017.txt'))
    >>> mlb_2018 = pd.read_csv(os.path.join('data','mlb_2018.txt'))
    >>> result = combined_seasons(mlb_2017, mlb_2018)
    >>> result[0].shape
    (30, 56)
    >>> result[1] in result[0].index
    True
    """

    return ...


def seasonal_average(df1, df2):
    """
    Combines df1 and df2 and take the mean of each column 
    for each team.
    
    - The dataframe you return should be indexed by team name (Tm).
    - Each column should contain the average value between the 2017 
    and 2018 seasons for the given statistic for each team.

    :Example:
    >>> mlb_2017 = pd.read_csv(os.path.join('data','mlb_2017.txt'))
    >>> mlb_2018 = pd.read_csv(os.path.join('data','mlb_2018.txt'))
    >>> result = seasonal_average(mlb_2017, mlb_2018)
    >>> result.shape
    (30, 28)
    >>> result.index.nunique()
    30
    >>> result.loc['MIN']['HR']
    186.0
    """

    return ...