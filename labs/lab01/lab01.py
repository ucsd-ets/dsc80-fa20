import os
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# Question # 0
# ---------------------------------------------------------------------

def consecutive_ints(ints):
    """
    consecutive_ints tests whether a list contains two 
    adjacent elements that are consecutive integers.
    :param ints: a list of integers
    :returns: a boolean value if ints contains two 
    adjacent elements that are consecutive integers.
    :Example:
    >>> consecutive_ints([5,3,6,4,9,8])
    True
    >>> consecutive_ints([1,3,5,7,9])
    False
    """

    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False

# ---------------------------------------------------------------------
# Question # 1 
# ---------------------------------------------------------------------

def median_vs_average(nums):
    """
    median takes a non-empty list of numbers,
    returning a boolean of whether the median is
    greater or equal than the average
    If the list has even length, it should return
    the mean of the two elements in the middle.
    :param nums: a non-empty list of numbers.
    :returns: bool, whether median is greater or equal than average.
    
    :Example:
    >>> median_vs_average([6, 5, 4, 3, 2])
    True
    >>> median_vs_average([50, 20, 15, 40])
    False
    >>> median_vs_average([1, 2, 3, 4])
    True
    """
    
    #take a non-empty list
    if len(nums) == 0:
        return False

    #find the average of this list
    total = sum(nums)
    avg = total/len(nums)

    idx = len(nums)//2
    #check whether it is even length
    if len(nums) % 2 == 0:
        # find avg of median two element
        med = (nums[idx] + nums[idx-1])/2
    else:
        med = nums[idx]

    #comparision
    if med >= avg:
        return True
    else:
        return False


# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------
def same_diff_ints(ints):
    """
    same_diff_ints tests whether a list contains
    two list elements i places apart, whose distance 
    as integers is also i.
    :param ints: a list of integers
    :returns: a boolean value if ints contains two 
    elements as described above.
    :Example:
    >>> same_diff_ints([5,3,1,5,9,8])
    True
    >>> same_diff_ints([1,3,5,7,9])
    False
    """

    if len(ints) == 0:
        return False

    for i in range(len(ints)):
        val = ints[i]
        for y in range(i+1, len(ints)):
            real_diff= y - i;
            diff = abs(ints[y] - val)
            if real_diff == diff:
                return True
    return False


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def n_prefixes(s, n):
    """
    n_prefixes returns a string of n
    consecutive prefix of the input string.

    :param s: a string.
    :param n: an integer

    :returns: a string of n consecutive prefixes of s backwards.
    :Example:
    >>> n_prefixes('Data!', 3)
    'DatDaD'
    >>> n_prefixes('Marina', 4)
    'MariMarMaM'
    >>> n_prefixes('aaron', 2)
    'aaa'
    """

    result = ""
    for i in range(n-1,-1,-1):
        result = result + s[:i+1]
    return result

# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------
def exploded_numbers(ints, n):
    """
    exploded_numbers returns a list of strings of numbers from the
    input array each exploded by n.
    Each integer is zero padded.

    :param ints: a list of integers.
    :param n: a non-negative integer.

    :returns: a list of strings of exploded numbers. 
    :Example:
    >>> exploded_numbers([3, 4], 2) 
    ['1 2 3 4 5', '2 3 4 5 6']
    >>> exploded_numbers([3, 8, 15], 2)
    ['01 02 03 04 05', '06 07 08 09 10', '13 14 15 16 17']
    """

    #find width
    wid = len(str(max(ints) + n))

    result = []
    for i in ints:
        expanded = list(range(i-n, i+n+1, 1))
        hold = ""
        for y in expanded:
            hold = hold + (str(y).zfill(wid)) + ' '
        result.append(hold[:len(hold)-1])
    return result


# ---------------------------------------------------------------------
# Question # 5
# ---------------------------------------------------------------------

def last_chars(fh):
    """
    last_chars takes a file object and returns a 
    string consisting of the last character of the line.
    :param fh: a file object to read from.
    :returns: a string of last characters from fh
    :Example:
    >>> fp = os.path.join('data', 'chars.txt')
    >>> last_chars(open(fp))
    'hrg'
    """

    result = ''
    for line in fh:
        #get last char
        result = result + line[-1-1]
    fh.close()
    return result

# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------

def arr_1(A):
    """
    arr_1 takes in a numpy array and
    adds to each element the square-root of
    the index of each element.
    :param A: a 1d numpy array.
    :returns: a 1d numpy array.
    :Example:
    >>> A = np.array([2, 4, 6, 7])
    >>> out = arr_1(A)
    >>> isinstance(out, np.ndarray)
    True
    >>> np.all(out >= A)
    True
    """

    toadd = np.arange(len(A)) ** 0.5
    return A + toadd

def arr_2(A):
    """
    arr_2 takes in a numpy array of integers
    and returns a boolean array (i.e. an array of booleans)
    whose ith element is True if and only if the ith element
    of the input array is a perfect square.
    :param A: a 1d numpy array.
    :returns: a 1d numpy boolean array.
    :Example:
    >>> out = arr_2(np.array([1, 2, 16, 17, 32, 49]))
    >>> isinstance(out, np.ndarray)
    True
    >>> out.dtype == np.dtype('bool')
    True
    """

    root = np.sqrt(A)
    result = []
    for i in root:
        result.append(isinstance(i, np.int))
    return np.array(result)


def arr_3(A):
    """
    arr_3 takes in a numpy array of stock
    prices per share on successive days in
    USD and returns an array of growth rates.
    :param A: a 1d numpy array.
    :returns: a 1d numpy array.
    :Example:
    >>> fp = os.path.join('data', 'stocks.csv')
    >>> stocks = np.array([float(x) for x in open(fp)])
    >>> out = arr_3(stocks)
    >>> isinstance(out, np.ndarray)
    True
    >>> out.dtype == np.dtype('float')
    True
    >>> out.max() == 0.03
    True
    """
    lastday = A[:len(A)-1]
    nextday = A[1:]
    result = (nextday - lastday)/lastday
    return np.round(result,2)





def arr_4(A):
    """
    Create a function arr_4 that takes in A and 
    returns the day on which you can buy at least 
    one share from 'left-over' money. If this never 
    happens, return -1. The first stock purchase occurs on day 0
    :param A: a 1d numpy array of stock prices.
    :returns: the day on which you can buy at least one share from 'left-over' money
    :Example:
    >>> import numbers
    >>> stocks = np.array([3, 3, 3, 3])
    >>> out = arr_4(stocks)
    >>> isinstance(out, numbers.Integral)
    True
    >>> out == 1
    True
    """

    #every day has 20 dollars
    budget = np.array([20] * len(A))

    #calculate left over money
    left = budget - (budget // A) * A

    #sum left overs
    all_left = np.cumsum(left)

    for i in range(len(A)):
        if all_left[i] >= A[i]:
            return i
    return -1




# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------

def salary_stats(salary):
    """
    salary_stats returns a series as specified in the notebook.
    :param salary: a dataframe of NBA salaries as found in `salary.csv`
    :return: a series with index specified in the notebook.
    :Example:
    >>> salary_fp = os.path.join('data', 'salary.csv')
    >>> salary = pd.read_csv(salary_fp)
    >>> out = salary_stats(salary)
    >>> isinstance(out, pd.Series)
    True
    >>> 'total_highest' in out.index
    True
    >>> isinstance(out.loc['duplicates'], bool)
    True
    """

    result = []
    # find number of players
    result.append(salary['Player'].nunique())
    # find number of teams
    result.append(salary['Team'].nunique())
    # find total salary over the season
    result.append(np.sum(salary['Salary']))
    # find highest salary
    result.append(salary['Salary'].max())
    # find average salary of the Boston Celtics ('BOS')
    result.append(np.round(salary[salary['Team'] == 'BOS']['Salary'].mean(),2))
    # find 3rd lowest name and team name
    #find 3rd lowest salary
    x = salary['Salary'].unique()
    x.sort()
    thirdLow = x[2]
    LowTable = salary[salary['Salary'] == thirdLow]
    #sort player alphabetically
    fst = LowTable.sort_values(by = ['Player']).iloc[0]
    result.append(fst['Player'] + ',' + ' ' + fst['Team'])

    #test duplicate last name
    splited = salary['Player'].str.split(" ").str[1]
    salary['last_name'] = splited
    #check duplicate
    whether = salary.duplicated('last_name').sum()
    if whether > 1:
        result.append(True)
    else:
        result.append(False)

    #find highest salary employee's team's sum salary
    t = salary['Salary'].unique()
    t.sort()
    highest_salary = t[len(t)-1]
    highTable = salary[salary['Salary'] == highest_salary]
    highTeam = highTable['Team'].iloc[0]
    result.append(salary[salary['Team'] == highTeam]['Salary'].sum())

    key = ['num_players','num_teams','total_salary','highest_salary',
           'avg_bos','third_lowest','duplicates','total_highest']

    return pd.Series(result, index=key)

# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------

def parse_malformed(fp):
    """
    Parses and loads the malformed csv data into a 
    properly formatted dataframe (as described in 
    the question).
    :param fh: file handle for the malformed csv-file.
    :returns: a Pandas DataFrame of the data, 
    as specificed in the question statement.
    :Example:
    >>> fp = os.path.join('data', 'malformed.csv')
    >>> df = parse_malformed(fp)
    >>> cols = ['first', 'last', 'weight', 'height', 'geo']
    >>> list(df.columns) == cols
    True
    >>> df['last'].dtype == np.dtype('O')
    True
    >>> df['height'].dtype == np.dtype('float64')
    True
    >>> df['geo'].str.contains(',').all()
    True
    >>> len(df) == 100
    True
    >>> dg = pd.read_csv(fp, nrows=4, skiprows=10, names=cols)
    >>> dg.index = range(9, 13)
    >>> (dg == df.iloc[9:13]).all().all()
    True
    """

    key = ['first', 'last', 'weight', 'height', 'geo','geo1']
    result = []
    title = 0
    with open(fp) as fh:
        for line in fh:
            if title == 0:
                # skip table header
                title = 1
                continue
            #change abnormal part by replacing
            processed = line.replace(',',' ')
            processed = processed.replace('"','')
            splited = processed.split()
            diction = dict(zip(key, splited))
            result.append(diction)
        #using zipped dictionary creating table
        tb = pd.DataFrame(result)
    fh.close()
    tb['geo'] = tb['geo'] + ',' + tb['geo1']
    newone = tb.drop('geo1',axis = 1)
    # convert to proper type
    newone['weight'] = newone['weight'].astype(np.float)
    newone['height'] = newone['height'].astype(np.float)
    return newone


# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------

# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q00': ['consecutive_ints'],
    'q01': ['median_vs_average'],
    'q02': ['same_diff_ints'],
    'q03': ['n_prefixes'],
    'q04': ['exploded_numbers'],
    'q05': ['last_chars'],
    'q06': ['arr_%d' % d for d in range(1, 5)],
    'q07': ['salary_stats'],
    'q08': ['parse_malformed']
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