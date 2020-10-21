
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def plot_meal_by_day(tips):
    """
    Plots the counts of meals in tips by day.
    plot_meal_by_day returns an matplotlib.axes._subplots.AxesSubplot 
    object; your plot should look like the plot in the notebook.

    :Example:
    >>> tips = sns.load_dataset('tips')
    >>> ax = plot_meal_by_day(tips)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """

    return ...


def plot_bill_by_tip(tips):
    """
    Plots a seaborn scatterplot using the tips data by day.
    plot_bill_by_tip returns a matplotlib.axes._subplots.AxesSubplot object; 
    your plot should look like the plot in the notebook.

    - tip is on the x-axis.
    - total_bill is on the y-axis.
    - color of the dots are given by day.
    - size of the dots are given by size of the table.

    :Example:
    >>> tips = sns.load_dataset('tips')
    >>> ax = plot_bill_by_tip(tips)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """

    return ...


def plot_tip_percentages(tips):
    """
    Plots a figure with two subplots side-by-side. 
    The left plot should contain the counts of tips as a percentage of the total bill. 
    The right plot should contain the density plot of tips as a percentage of the total bill. 
    plot_tip_percentages should return a matplotlib.Figure object; 
    your plot should look like the plot in the notebook.

    :Example:
    >>> tips = sns.load_dataset('tips')
    >>> ax = plot_tip_percentages(tips)
    >>> type(ax)
    <class 'matplotlib.figure.Figure'>
    """

    return ...
