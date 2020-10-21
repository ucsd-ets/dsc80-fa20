import os

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def data_load(scores_fp):
    """
    follows different steps to create a dataframe
    :param scores_fp: file name as a string
    :return: a dataframe
    >>> scores_fp = os.path.join('data', 'scores.csv')
    >>> scores = data_load(scores_fp)
    >>> isinstance(scores, pd.DataFrame)
    True
    >>> list(scores.columns)
    ['attempts', 'highest_score']
    >>> isinstance(scores.index[0], int)
    False
    """
    # a
    tb_part = pd.read_csv(scores_fp,usecols = ['name','tries','highest_score','sex'])

    # b
    # remove sex column
    removed = tb_part.drop('sex',axis = 1)

    # c
    # rename columns
    renamed = removed.rename({'name':'firstname','tries':'attempts'},axis = 'columns')

    # d
    # turn fist name to index
    result = renamed.set_index('firstname')

    return result


def pass_fail(scores):
    """
    modifies the scores dataframe by adding one more column satisfying
    conditions from the write up.
    :param scores: dataframe from the question above
    :return: dataframe with additional column pass
    >>> scores_fp = os.path.join('data', 'scores.csv')
    >>> scores = data_load(scores_fp)
    >>> scores = pass_fail(scores)
    >>> isinstance(scores, pd.DataFrame)
    True
    >>> len(scores.columns)
    3
    >>> scores.loc["Julia", "pass"]=='Yes'
    True

    """


    scores.loc[((scores['attempts'] < 3) & (scores['highest_score'] >= 50)),'pass'] = 'Yes'
    scores.loc[((scores['attempts'] < 6) & (scores['highest_score'] >= 70)),'pass'] = 'Yes'
    scores.loc[((scores['attempts'] < 10) & (scores['highest_score'] >= 90)),'pass'] = 'Yes'
    #replace false with no
    scores = scores.replace(False,'No')
    return scores



def av_score(scores):
    """
    returns the average score for those students who passed the test.
    :param scores: dataframe from the second question
    :return: average score
    >>> scores_fp = os.path.join('data', 'scores.csv')
    >>> scores = data_load(scores_fp)
    >>> scores = pass_fail(scores)
    >>> av = av_score(scores)
    >>> isinstance(av, float)
    True
    >>> 91 < av < 92
    True
    """

    #only focus on passed student
    passed = scores[scores['pass'] == 'Yes']
    #find average score
    return passed['highest_score'].mean()



def highest_score_name(scores):
    """
    finds the highest score and people who received it
    :param scores: dataframe from the second question
    :return: dictionary where the key is the highest score and the value(s) is a list of name(s)
    >>> scores_fp = os.path.join('data', 'scores.csv')
    >>> scores = data_load(scores_fp)
    >>> scores = pass_fail(scores)
    >>> highest = highest_score_name(scores)
    >>> isinstance(highest, dict)
    True
    >>> len(next(iter(highest.items()))[1])
    3
    """
    # find max score
    max_score = scores['highest_score'].max()
    # find student with highest score
    student = scores[scores['highest_score'] == max_score].index.tolist()
    return {max_score:student}


def idx_dup():
    """
    Answers the question in the write up.
    :return:
    >>> ans = idx_dup()
    >>> isinstance(ans, int)
    True
    >>> 1 <= ans <= 6
    True
    """
    return 6



# ---------------------------------------------------------------------
# Question # 2
# ---------------------------------------------------------------------

def trick_me():
    """
    Answers the question in the write-up
    :return: a letter
    >>> ans =  trick_me()
    >>> ans == 'A' or ans == 'B' or ans == "C"
    True
    """
    return 'C'



def reason_dup():
    """
     Answers the question in the write-up
    :return: a letter
    >>> ans =  reason_dup()
    >>> ans == 'A' or ans == 'B' or ans == "C"
    True
    """
    return 'B'



def trick_bool():
    """
     Answers the question in the write-up
    :return: a list with three letters
    >>> ans =  trick_bool()
    >>> isinstance(ans, list)
    True
    >>> isinstance(ans[1], str)
    True

    """
    return ['D','J','M']

def reason_bool():
    """
    Answers the question in the write-up
    :return: a letter
    >>> ans =  reason_bool()
    >>> ans == 'A' or ans == 'B' or ans == "C" or ans =="D"
    True

    """
    return 'D'


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------

def change(x):
    """
    Returns 'MISSING' when x is `NaN`,
    Otherwise returns x
    >>> change(1.0) == 1.0
    True
    >>> change(np.NaN) == 'MISSING'
    True
    """

    if np.isnan(x):
        return "MISSING"
    else:
        return x


def correct_replacement(nans):
    """
    changes all np.NaNs to "Missing"
    :param nans: given dataframe
    :return: modified dataframe
    >>> nans = pd.DataFrame([[0,1,np.NaN], [np.NaN, np.NaN, np.NaN], [1, 2, 3]])
    >>> A = correct_replacement(nans)
    >>> (A.values == 'MISSING').sum() == 4
    True

    """
    return nans.applymap(change)


# ---------------------------------------------------------------------
# Question # 4
# ---------------------------------------------------------------------

def population_stats(df):
    """
    population_stats which takes in a dataframe df
    and returns a dataframe indexed by the columns
    of df, with the following columns:
        - `num_nonnull` contains the number of non-null
          entries in each column,
        - `pct_nonnull` contains the proportion of entries
          in each column that are non-null,
        - `num_distinct` contains the number of distinct
          entries in each column,
        - `pct_distinct` contains the proportion of (non-null)
          entries in each column that are distinct from each other.

    :Example:
    >>> data = np.random.choice(range(10), size=(100, 4))
    >>> df = pd.DataFrame(data, columns='A B C D'.split())
    >>> out = population_stats(df)
    >>> out.index.tolist() == ['A', 'B', 'C', 'D']
    True
    >>> cols = ['num_nonnull', 'pct_nonnull', 'num_distinct', 'pct_distinct']
    >>> out.columns.tolist() == cols
    True
    >>> (out['num_distinct'] <= 10).all()
    True
    >>> (out['pct_nonnull'] == 1.0).all()
    True
    """
    #find number of non-null entries
    total = len(df)
    nonnull = (total - df.isna().sum()).tolist()
    # find proportion
    nn_pct = pd.Series(nonnull) / total

    #find disctinct number
    ndis = df.nunique().tolist()
    d_pct = pd.Series(ndis)/total
    result = pd.DataFrame({'num_nonnull':nonnull,'pct_nonnull':nn_pct.tolist(),'num_distinct':ndis,
                           'pct_distinct':d_pct.tolist()},index = df.columns.tolist())

    return result


def most_common(df, N=10):
    """
    `most_common` which takes in a dataframe df and returns
    a dataframe of the N most-common values (and their counts)
    for each column of df.

    :param df: input dataframe.
    :param N: number of most common elements to return (default 10)
.
    :Example:
    >>> data = np.random.choice(range(10), size=(100, 2))
    >>> df = pd.DataFrame(data, columns='A B'.split())
    >>> out = most_common(df, N=3)
    >>> out.index.tolist() == [0, 1, 2]
    True
    >>> out.columns.tolist() == ['A_values', 'A_counts', 'B_values', 'B_counts']
    True
    >>> out['A_values'].isin(range(10)).all()
    True
    """

    col = df.columns
    result = pd.DataFrame()

    for i in col:
        counted = df.groupby(i)[i].count().sort_values(ascending = False)
        val = counted.index.tolist()[:N]
        cou = counted.values[:N]
        form = pd.DataFrame({(str(i) + '_values'):val,(str(i) + '_counts'):cou})
        result = pd.concat([result,form],axis = 1)

    #check length
    if len(result) < N:
        #concat few more
        diff = N - len(result)

        d = [[np.nan]*len(result.columns)]*diff
        nans = pd.DataFrame(d,columns = result.columns.tolist())
        #concat them
        result = pd.concat([result,nans])
        #reset index
        result = result.reset_index(drop = True)
    return result

# ---------------------------------------------------------------------
# Question 5
# ---------------------------------------------------------------------


def null_hypoth():
    """
    :Example:
    >>> isinstance(null_hypoth(), list)
    True
    >>> set(null_hypoth()).issubset({1,2,3,4})
    True
    """

    return [1]


def simulate_null():
    """
    :Example:
    >>> pd.Series(simulate_null()).isin([0,1]).all()
    True
    """

    # 1 means good, 0 means bad
    result = np.random.choice([1,0], p = [0.99,0.01])
    return result


def estimate_p_val(N):
    """
    >>> 0 < estimate_p_val(1000) < 0.1
    True
    """

    #hold random result
    hold = []
    for i in range(N):
        hold.append(simulate_null())

    #check p value
    return 1- (np.sum(hold))/N


# ---------------------------------------------------------------------
# Question 6
# ---------------------------------------------------------------------


def super_hero_powers(powers):
    """
    `super_hero_powers` takes in a dataframe like
    powers and returns a list with the following three entries:
        - The name of the super-hero with the greatest number of powers.
        - The name of the most common super-power among super-heroes whose names begin with 'M'.
        - The most popular super-power among those with only one super-power.

    :Example:
    >>> fp = os.path.join('data', 'superheroes_powers.csv')
    >>> powers = pd.read_csv(fp)
    >>> out = super_hero_powers(powers)
    >>> isinstance(out, list)
    True
    >>> len(out)
    3
    >>> all([isinstance(x, str) for x in out])
    True
    """

    #find hero with greatest number of power
    copy = powers
    setted = copy.set_index('hero_names')
    setted = setted.replace({True:1,False:0})
    common = setted.sum(axis = 1).sort_values(ascending = False)
    cmm_hero = common.index[0]

    #find all hero name begin with M
    Ms = setted[setted.index.str[0] == 'M']
    #find most common power
    m_common = Ms.sum().sort_values(ascending = False)
    m_power = m_common.index[0]

    #find heroes with only one power
    op = setted[setted.sum(axis = 1) == 1]
    #find most popular power
    opp = op.sum().sort_values(ascending = False)
    oppp = opp.index[0]

    return [cmm_hero,m_power,oppp]

# ---------------------------------------------------------------------
# Question 7
# ---------------------------------------------------------------------


def clean_heroes(heroes):
    """
    clean_heroes takes in the dataframe heroes
    and replaces values that are 'null-value'
    place-holders with np.NaN.

    :Example:
    >>> superheroes_fp = os.path.join('data', 'superheroes.csv')
    >>> heroes = pd.read_csv(superheroes_fp, index_col=0)
    >>> out = clean_heroes(heroes)
    >>> out['Skin color'].isnull().any()
    True
    >>> out['Weight'].isnull().any()
    True
    """

    #replace all - with null
    heroes = heroes.replace({'-':np.NaN})
    #change negative height
    heroes.loc[heroes['Height'] <= 0,['Height']] = np.NaN
    #cahneg negative weight
    heroes.loc[heroes['Weight'] <= 0,['Weight']] = np.NaN

    return heroes


def super_hero_stats():
    """
    Returns a list that answers the questions in the notebook.
    :Example:
    >>> out = super_hero_stats()
    >>> out[0] in ['Marvel Comics', 'DC Comics']
    True
    >>> isinstance(out[1], int)
    True
    >>> isinstance(out[2], str)
    True
    >>> out[3] in ['good', 'bad']
    True
    >>> isinstance(out[4], str)
    True
    >>> 0 <= out[5] <= 1
    True
    """

    return ['Marvel Comics',282,'Groot','bad','Onslaught',0.1512]

# ---------------------------------------------------------------------
# Question 8
# ---------------------------------------------------------------------


def bhbe_col(heroes):
    """
    `bhbe` ('blond-hair-blue-eyes') returns a boolean
    column that labels super-heroes/villains that
    are blond-haired *and* blue eyed.

    :Example:
    >>> superheroes_fp = os.path.join('data', 'superheroes.csv')
    >>> heroes = pd.read_csv(superheroes_fp, index_col=0)
    >>> out = bhbe_col(heroes)
    >>> isinstance(out, pd.Series)
    True
    >>> out.dtype == np.dtype('bool')
    True
    >>> out.sum()
    93
    """

    copy = heroes
    copy['bh'] = copy['Hair color'].apply(lambda x: True if "Blond" in x else False)

    copy['be'] = copy['Eye color'].apply(lambda x: True if "blue" in x else False)


    copy.loc[copy['Hair color'] == 'blond',['bh']] = True
    return ((copy['bh'] == True) & (copy['be'] == True))


def observed_stat(heroes):
    """
    observed_stat returns the observed test statistic
    for the hypothesis test.

    :Example:
    >>> superheroes_fp = os.path.join('data', 'superheroes.csv')
    >>> heroes = pd.read_csv(superheroes_fp, index_col=0)
    >>> out = observed_stat(heroes)
    >>> 0.5 <= out <= 1.0
    True
    """

    #find proportion of good heroes among bhbe
    checked = bhbe_col(heroes)
    good_bhbe = (heroes['Alignment'] == 'good') & checked
    gp = good_bhbe.sum()/checked.sum()

    return gp


def simulate_bhbe_null(n):
    """
    `simulate_bhbe_null` that takes in a number `n`
    that returns a `n` instances of the test statistic
    generated under the null hypothesis.
    You should hard code your simulation parameter
    into the function; the function should *not* read in any data.

    :Example:
    >>> superheroes_fp = os.path.join('data', 'superheroes.csv')
    >>> heroes = pd.read_csv(superheroes_fp, index_col=0)
    >>> out = simulate_bhbe_null(10)
    >>> isinstance(out, pd.Series)
    True
    >>> out.shape[0]
    10
    >>> ((0.45 <= out) & (out <= 1)).all()
    True
    """

    #find general good proportion and bhbe size for parameter
    g_pp = 496/734  #good hero /heroes in total
    sz = 93
    result = []
    for i in range(n):
        #random generate good under bhbe null assumption
        val = np.random.choice(['good','bad'],size = sz, p = [g_pp,1-g_pp])
        proportion = pd.Series(val).value_counts()['good']/sz
        result.append(proportion)

    return pd.Series(result)


def calc_pval():
    """
    calc_pval returns a list where:
        - the first element is the p-value for
        hypothesis test (using 100,000 simulations).
        - the second element is Reject if you reject
        the null hypothesis and Fail to reject if you
        fail to reject the null hypothesis.

    :Example:
    >>> out = calc_pval()
    >>> len(out)
    2
    >>> 0 <= out[0] <= 1
    True
    >>> out[1] in ['Reject', 'Fail to reject']
    True
    """

    return [0.00011, 'Reject']


# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------

# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['data_load', 'pass_fail', 'av_score',
            'highest_score_name', 'idx_dup'],
    'q02': ['trick_me', 'reason_dup', 'trick_bool', 'reason_bool'],
    'q03': ['change', 'correct_replacement'],
    'q04': ['population_stats', 'most_common'],
    'q05': ['null_hypoth', 'simulate_null', 'estimate_p_val'],
    'q06': ['super_hero_powers'],
    'q07': ['clean_heroes', 'super_hero_stats'],
    'q08': ['bhbe_col', 'observed_stat', 'simulate_bhbe_null', 'calc_pval']
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
