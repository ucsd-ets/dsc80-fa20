
import os

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def car_null_hypoth():
    """
    Returns a list of valid null hypotheses.
    
    :Example:
    >>> set(car_null_hypoth()) <= set(range(1,11))
    True
    """
    return [1,4,7]


def car_alt_hypoth():
    """
    Returns a list of valid alternative hypotheses.
    
    :Example:
    >>> set(car_alt_hypoth()) <= set(range(1,11))
    True
    """
    return [2,5]


def car_test_stat():
    """
    Returns a list of valid test statistics.
    
    :Example:
    >>> set(car_test_stat()) <= set(range(1,5))
    True
    """
    return [3,2,4]


def car_p_value():
    """
    Returns an integer corresponding to the correct explanation.
    
    :Example:
    >>> car_p_value() in [1,2,3,4,5]
    True
    """
    return 3


# ---------------------------------------------------------------------
# Question #2
# ---------------------------------------------------------------------

def clean_apps(df):
    '''
    >>> fp = os.path.join('data', 'googleplaystore.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_apps(df)
    >>> len(cleaned) == len(df)
    True
    >>> cleaned.Reviews.dtype == int
    True
    '''

    #make a copy
    copy = df.copy(deep = True)

    #creat helper function for M and k
    def help_clean(x):
        if x[-1] == 'M':
            #convert M to kb
            return float(x[:len(x)-1]) * 1000
        else:
            #no need to convert
            return float(x[:len(x)-1])

    # strip letter from the end of size and convert
    copy.loc[:,'Size'] = copy['Size'].apply(help_clean)

    #strip + from installs
    noPlus = copy['Installs'].apply(lambda x: x[:len(x)-1])
    #strip comma
    instal = noPlus.apply(lambda x: x.replace(',',''))
    copy.loc[:,'Installs'] = instal.astype(np.int)


    #change type free to 1, paid to 0
    copy.loc[:,'Type'] = copy['Type'].replace({'Free': 1, "Paid":0})

    #strip dollar mark in price
    noD = copy['Price'].str.strip('$')
    #convert to float
    copy.loc[:,'Price'] = noD.astype(np.float)

    #strip all but last year in updated
    yr = copy['Last Updated'].apply(lambda x: (x.split())[-1])
    copy.loc[:,'Last Updated'] = yr.astype(np.int)

    return copy


def store_info(cleaned):
    '''
    >>> fp = os.path.join('data', 'googleplaystore.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_apps(df)
    >>> info = store_info(cleaned)
    >>> len(info)
    4
    >>> info[2] in cleaned.Category.unique()
    True
    '''


    return [2018,'Adults only 18+','FINANCE','DATING']

# ---------------------------------------------------------------------
# Question 3
# ---------------------------------------------------------------------

def std_reviews_by_app_cat(cleaned):
    """
    >>> fp = os.path.join('data', 'googleplaystore.csv')
    >>> play = pd.read_csv(fp)
    >>> clean_play = clean_apps(play)
    >>> out = std_reviews_by_app_cat(clean_play)
    >>> set(out.columns) == set(['Category', 'Reviews'])
    True
    >>> np.all(abs(out.select_dtypes(include='number').mean()) < 10**-7)  # standard units should average to 0!
    True
    """

    calculated = cleaned.groupby(['Category']).agg(['mean',np.std])['Reviews']

    #use hash
    mean_dic = {}
    std_dic = {}
    for i in calculated.index:
        mean_dic[i] = calculated.loc[i,'mean']
        std_dic[i] = calculated.loc[i,'std']

    subdf = cleaned.loc[:,['Category','Reviews']]
    #standardize review
    mean_col = subdf['Category'].apply(lambda x: mean_dic.get(x))
    std_col = subdf['Category'].apply(lambda x: std_dic.get(x))
    #calculated standardized value
    subdf.loc[:,'Reviews'] = (subdf['Reviews'] - mean_col)/std_col
    return subdf


def su_and_spread():
    """
    >>> out = su_and_spread()
    >>> len(out) == 2
    True
    >>> out[0].lower() in ['medical', 'family', 'equal']
    True
    >>> out[1] in ['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY',\
       'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION',\
       'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE',\
       'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME',\
       'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL',\
       'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS', 'TRAVEL_AND_LOCAL',\
       'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER',\
       'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION']
    True
    """
    return ['FAMILY','FAMILY']


# ---------------------------------------------------------------------
# Question #4
# ---------------------------------------------------------------------


def read_survey(dirname):
    """
    read_survey combines all the survey*.csv files into a singular DataFrame
    :param dirname: directory name where the survey*.csv files are
    :returns: a DataFrame containing the combined survey data
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> out = read_survey(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> len(out)
    5000
    >>> read_survey('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """

    suv1 = pd.read_csv(dirname + '/survey1.csv')
    #rearange survey1 column order
    key = ['first name', 'last name', 'current company', 'job title', 'email', 'university']
    suv1 = suv1[key]

    suv2 = pd.read_csv(dirname + '/survey2.csv')
    #lower survey2 column names
    suv2 = suv2.rename(str.lower,axis = 1)
    suv2 = suv2[key]

    suv3 = pd.read_csv(dirname + '/survey3.csv')
    #lower survey3 column names and strip _
    suv3 = suv3.rename(str.lower,axis = 1)
    suv3.columns = suv3.columns.str.replace('_',' ')
    suv3 = suv3[key]

    suv4 = pd.read_csv(dirname + '/survey4.csv')
    #similar work as survey3
    suv4.columns = suv4.columns.str.replace('_',' ')
    suv4 = suv4.rename(str.lower,axis = 1)
    suv4 = suv4[key]

    suv5 = pd.read_csv(dirname + '/survey5.csv')
    #similar work as survey4
    suv5.columns = suv5.columns.str.replace('_',' ')
    suv5 = suv5.rename(str.lower,axis = 1)
    suv5 = suv5[key]

    #combine all df together
    return pd.concat([suv1,suv2,suv3,suv4,suv5])

def com_stats(df):
    """
    com_stats 
    :param df: a DataFrame containing the combined survey data
    :returns: a hardcoded list of answers to the problems in the notebook
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> df = read_survey(dirname)
    >>> out = com_stats(df)
    >>> len(out)
    4
    >>> isinstance(out[0], int)
    True
    >>> isinstance(out[2], str)
    True
    """

    return [5,253,'VP Sales',369]


# ---------------------------------------------------------------------
# Question #5
# ---------------------------------------------------------------------

def combine_surveys(dirname):
    """
    combine_surveys takes in a directory path 
    (containing files favorite*.csv) and combines 
    all of the survey data into one DataFrame, 
    indexed by student ID (a value 0 - 1000).

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> out = combine_surveys(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.shape
    (1000, 6)
    >>> combine_surveys('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """

    name = os.listdir(dirname)
    df = pd.read_csv(dirname + '/favorite1.csv').head()
    for i in range(1,len(name)):
        hold = pd.read_csv(dirname + '/favorite' + str(i) + '.csv')
        df = pd.merge(df, hold, on = 'id', how = 'outer')

    df = df.set_index('id')
    return df


def check_credit(df):
    """
    check_credit takes in a DataFrame with the 
    combined survey data and outputs a DataFrame 
    of the names of students and how many extra credit 
    points they would receive, indexed by their ID (a value 0-1000)

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> df = combine_surveys(dirname)
    >>> out = check_credit(df)
    >>> out.shape
    (1000, 2)
    """

    threshold = 4 * 0.25
    notAnswer = df.isna().sum(axis = 1)

    checked = notAnswer <= threshold
    ex = checked.replace({True:5,False:0})

    #check class extra credit
    student_thresh = len(df) * 0.1

    overall = (df[['movie','genre','animal','plant']].isna().sum() <= student_thresh).sum() >= 1
    if overall == True:
        ex = ex + 1

    df = df.assign(extra = ex)
    return df[['name_y','extra']]

# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------


def most_popular_procedure(pets, procedure_history):
    """
    What is the most popular Procedure Type for all of the pets we have in our `pets` dataset?
​
    :Example:
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = most_popular_procedure(pets, procedure_history)
    >>> isinstance(out,str)
    True
    """

    return 'VACCINATIONS'


def pet_name_by_owner(owners, pets):
    """
    pet names by owner

    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> out = pet_name_by_owner(owners, pets)
    >>> len(out) == len(owners)
    True
    >>> 'Sarah' in out.index
    True
    >>> 'Cookie' in out.values
    True
    """

    owners_ss = owners[['OwnerID','Name']]
    owners_ss = owners_ss.rename({'Name':'Owner'},axis = 1)
    pets_ss = pets[['OwnerID','Name']]
    merged = pd.merge(owners_ss,pets_ss,on = 'OwnerID',how = 'outer')


    #get duplicateds owner id
    more = merged[merged['OwnerID'].duplicated()]
    ids = more['OwnerID'].value_counts().index.tolist()

    #drop duplicates
    merged = merged.drop_duplicates(subset = ['OwnerID'])

    for i in ids:
        hold = []
        #find first occurance
        hold.append(merged[merged['OwnerID'] == i]['Name'].iloc[0])
        #find other names
        hold.extend(more[more['OwnerID'] == i ]['Name'].values.tolist())

        #convert to string
        hold = [', '.join(x for x in hold)][0]

        #find idx
        idx = merged[merged['OwnerID'] == i].index[0]
        #change it
        merged[merged['OwnerID'] == i].loc[idx,'Name']= hold

    return merged.set_index('Owner')['Name']



def total_cost_per_city(owners, pets, procedure_history, procedure_detail):
    """
    total cost per city
​
    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_detail_fp = os.path.join('data', 'pets', 'ProceduresDetails.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')
    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_detail = pd.read_csv(procedure_detail_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = total_cost_per_city(owners, pets, procedure_history, procedure_detail)
    >>> set(out.index) <= set(owners['City'])
    True
    """

    #only care ownerid and city
    own = owners[['OwnerID','City']]
    #only care petid and owner id
    pet_s = pets[['OwnerID','PetID']]
    #combine owner and pet
    pet_own = own.merge(pet_s,on='OwnerID')

    #conly care petID and procedure code
    pc = procedure_history[['PetID','ProcedureSubCode']]
    #only care subcode and price
    pd = procedure_detail[['ProcedureSubCode','Price']]

    #combine all
    fin = pc.merge(pet_own,on = 'PetID')
    fini = pd.merge(fin, on = 'ProcedureSubCode')

    #only care price and city
    subset = fini[['Price','City']]
    return subset.groupby('City').sum()


# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!


GRADED_FUNCTIONS = {
    'q01': [
        'car_null_hypoth', 'car_alt_hypoth',
        'car_test_stat', 'car_p_value'
    ],
    'q02': ['clean_apps', 'store_info'],
    'q03': ['std_reviews_by_app_cat','su_and_spread'],
    'q04': ['read_survey', 'com_stats'],
    'q05': ['combine_surveys', 'check_credit'],
    'q06': ['most_popular_procedure', 'pet_name_by_owner', 'total_cost_per_city']
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
