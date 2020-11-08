import os
import pandas as pd
import numpy as np
import requests
import bs4
import json


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------


def question1():
    """
    NOTE: You do NOT need to do anything with this function.

    The function for this question makes sure you
    have a correctly named HTML file in the right
    place. Note: This does NOT check if the supplementary files
    needed for your page are there!

    >>> os.path.exists('lab06_1.html')
    True
    """

    # Don't change this function body!
    # No python required; create the HTML file.

    return


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def extract_book_links(text):
    """
    :Example:
    >>> fp = os.path.join('data', 'products.html')
    >>> out = extract_book_links(open(fp, encoding='utf-8').read())
    >>> url = 'scarlet-the-lunar-chronicles-2_218/index.html'
    >>> out[1] == url
    True
    """
    return ...


def get_product_info(text, categories):
    """
    :Example:
    >>> fp = os.path.join('data', 'Frankenstein.html')
    >>> out = get_product_info(open(fp, encoding='utf-8').read(), ['Default'])
    >>> isinstance(out, dict)
    True
    >>> 'Category' in out.keys()
    True
    >>> out['Rating']
    'Two'
    """
    return ...


def scrape_books(k, categories):
    """
    :param k: number of book-listing pages to scrape.
    :returns: a dataframe of information on (certain) books
    on the k pages (as described in the question).

    :Example:
    >>> out = scrape_books(1, ['Mystery'])
    >>> out.shape
    (1, 11)
    >>> out['Rating'][0] == 'Four'
    True
    >>> out['Title'][0] == 'Sharp Objects'
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question 3
# ---------------------------------------------------------------------

def stock_history(ticker, year, month):
    """
    Given a stock code and month, return the stock price details for that month
    as a dataframe

    >>> history = stock_history('BYND', 2019, 6)
    >>> history.shape == (20, 13)
    True
    >>> history.label.iloc[0]
    'June 03, 19'
    """
    return ...


def stock_stats(history):
    """
    Given a stock's trade history, return the percent change and transactions
    in billion dollars.

    >>> history = stock_history('BYND', 2019, 6)
    >>> stats = stock_stats(history)
    >>> len(stats[0]), len(stats[1])
    (7, 6)
    >>> float(stats[0][1:-1]) > 30
    True
    >>> float(stats[1][:-1]) > 1
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def get_comments(storyid):
    """
    Returns a dataframe of all the comments below a news story
    >>> out = get_comments(18344932)
    >>> out.shape
    (18, 5)
    >>> out.loc[5, 'by']
    'RobAtticus'
    >>> out.loc[5, 'time'].day
    31
    """
    return ...


# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['question1'],
    'q02': ['extract_book_links', 'get_product_info', 'scrape_books'],
    'q03': ['stock_history', 'stock_stats'],
    'q04': ['get_comments']
}


def check_for_graded_elements():
    """
    >>> check_for_graded_elements()
    True
    """
    
    for q, elts in GRADED_FUNCTIONS.items():
        for elt in elts:
            if elt not in globals():
                stmt = "YOU CHANGED A QUESTION THAT SHOULDN'T CHANGE! \
                In %s, part %s is missing" % (q, elt)
                raise Exception(stmt)

    return True
