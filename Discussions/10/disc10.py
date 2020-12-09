

# Question 1

def merge_majors(df1, df2):
    '''
    Merge the two input dataframes on major code number
    >>> df1 = pd.read_csv('data/majors-list.csv')
    >>> df2 = pd.read_csv('data/majors-data.csv')
    >>> merged = merge_majors(df1, df2)
    >>> len(merged) == len(df1)
    True
    >>> len(merged.columns)
    10
    >>> 'FOD1P' in merged.columns
    False
    '''
    return ...


def best_majors(df):
    '''
    Return a list of "best" majors
    >>> df1 = pd.read_csv('data/majors-list.csv')
    >>> df2 = pd.read_csv('data/majors-data.csv')
    >>> merged = merge_majors(df1, df2)
    >>> best = best_majors(merged)
    >>> len(best)
    4
    >>> all(pd.Series(best).isin(merged.Major_Category.unique()))
    True
    '''
        
    return ...


# Question 2


def null_and_statistic():
    """
    answers to the two multiple-choice
    questions listed above.

    :Example:
    >>> out = null_and_statistic()
    >>> isinstance(out, list)
    True
    >>> out[0] in [1,2,3]
    True
    >>> out[1] in [1,2]
    True
    """
    
    return ...


def simulate_null(data):
    """
    simulate_null takes in a dataframe like default, 
    and returns one instance of the test-statistic 
    (difference of means) under the null hypothesis.

    :Example:
    >>> default_fp = os.path.join('data', 'default.csv')
    >>> default = pd.read_csv(default_fp)
    >>> out = simulate_null(default)
    >>> isinstance(out, float)
    True
    >>> 0 <= out <= 1.0
    True
    """

    return ...


def pval_default(data):
    """
    pval_default takes in a dataframe like default, 
    and calculates the p-value for the permutation 
    test using 1000 trials.
    
    :Example:
    >>> default_fp = os.path.join('data', 'default.csv')
    >>> default = pd.read_csv(default_fp)
    >>> out = pval_default(default)
    >>> isinstance(pval, float)
    True
    >>> 0 <= pval <= 0.1
    True
    """
    
    return ...


# Question 3


def identifications():
    """
    Multiple choice response for question X
    >>> out = identifications()
    >>> ans = ['MD', 'MCAR', 'MAR', 'NMAR']
    >>> len(out) == 5
    True
    >>> set(out) <= set(ans)
    True
    """
    
    return ...


# Question 4


def impute_years(cars):
    """
    impute_years takes in a DataFrame of car data
    with missing values and imputes them using the scheme in
    the question.
    :Example:
    >>> fp = os.path.join('data', 'cars.csv')
    >>> df = pd.read_csv(fp)
    >>> out = impute_years(df)
    >>> out['car_year'].dtype == int
    True
    >>> out['car_year'].min() == df['car_year'].min()
    True
    """
    return ...

# Question 5


def impute_colors(cars):
    """
    impute_colors takes in a DataFrame of car data
    with missing values and imputes them using the scheme in
    the question.
    :Example:
    >>> fp = os.path.join('data', 'cars.csv')
    >>> df = pd.read_csv(fp)
    >>> out = impute_colors(df)
    >>> out.loc[out['car_make'] == 'Toyota'].nunique() == 19
    True
    >>> 'Crimson' in out.loc[out['car_make'] == 'Austin']['car_color'].unique()
    False
    """
    return ...


# Question 7

def match(robots):
    """
    >>> robots1 = "User-Agent: *\\nDisallow: /posts/\\nDisallow: /posts?\\nDisallow: /amzn/click/\\nDisallow: /questions/ask/\\nAllow: /"
    >>> match(robots1)
    False
    >>> robots2 = "User-Agent: *\\nAllow: /"
    >>> match(robots2)
    True
    >>> robots3 = "User-agent: Googlebot-Image\\nDisallow: /*/ivc/*\\nUser-Agent: *\\nAllow: /"
    >>> match(robots3)
    True
    """
    return ...


# Question 8

def extract(text):
    """
    extracts all phone numbers from given 
    text and return the findings as a 
    list of strings
    :Example:
    >>> text1 = "Contact us\\nFinancial Aid and Scholarships Office\\nPhone: (858)534-4480\\nFax: (858)534-5459\\nWebsite: fas.ucsd.edu\\nEmail: finaid@ucsd.edu\\nMailing address:\\n9500 Gilman Drive, Mail Code 0013\\nLa Jolla, CA 92093-0013"
    ['(858)534-4480','(858)534-5459']
    >>> text2 = "Contact us\\nPhone: 858-534-4480\\nFax: 858-534-5459\\nMailing address:\\n9500 Gilman Drive, Mail Code 0013\\nLa Jolla, CA 92093-00130"
    ['858-534-4480','858-534-5459']
    """
    return ...


# Question 9


def tfidf_data(sentences):
    """
    tf-idf of the word 'data' in a list of `sentences`.
    """
    return ...


# Question 10

def vectorize(df):
    """
    Create a vector, indexed by the distinct words, with counts of the words in that entry.
    """
    return ...

# Question 11


def qualitative_columns():
    """
    >>> isinstance(qualitative_columns(), list)
    True
    >>> len(qualitative_columns()) == 4
    True
    """
    return ...


# Question 12

def false_consequences():
    """
    
    >>> false_consequences() in range(1, 5)
    True
    """
    
    return ...


def blocked_malicious():
    """
    
    >>> out = blocked_malicious()
    >>> set(out[0]) <= set(range(5))
    True
    >>> 0 <= out[1] <= 1
    True
    """
    
    return ...


def fairness_claims():
    """
    
    >>> out = fairness_claims()
    >>> set(out[0]) <= set(range(5))
    True
    >>> 0 <= out[1] <= 1
    True
    """
    
    return ...
    
# Question 13


def parameters():
    """
    >>> isinstance(parameters(), dict)
    True
    """
    
    return ...


def parameter_search(X, y, pl):

    return ...


# Question 14

def age_pairity(X, y, pl, scoring, k):
        
    return ...
