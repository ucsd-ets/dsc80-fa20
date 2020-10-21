
import os
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# Question #1
# ---------------------------------------------------------------------


def get_assignment_names(grades):
    '''
    get_assignment_names takes in a dataframe like grades and returns 
    a dictionary with the following structure:

    The keys are the general areas of the syllabus: lab, project, 
    midterm, final, disc, checkpoint

    The values are lists that contain the assignment names of that type. 
    For example the lab assignments all have names of the form labXX where XX 
    is a zero-padded two digit number. See the doctests for more details.    

    :Example:
    >>> grades_fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(grades_fp)
    >>> names = get_assignment_names(grades)
    >>> set(names.keys()) == {'lab', 'project', 'midterm', 'final', 'disc', 'checkpoint'}
    True
    >>> names['final'] == ['Final']
    True
    >>> 'project02' in names['project']
    True
    '''

    key = ['lab','project','midterm','final','disc','checkpoint']
    #get all column name
    col = list(grades.columns)
    # loop through to get required assignment name
    hold = []
    result = {}
    for i in key:
        result[i] = []
        for x in col:
            #be careful of uppercase in exam
            z = x.lower()
            if (i in z) and ('-' not in z):
                #project not include checkpoint and free response
                if i == 'project':
                    if ('free' not in z) and ('check' not in z):
                        result[i].append(x)
                else:
                    result[i].append(x)
    return result


# ---------------------------------------------------------------------
# Question #2
# ---------------------------------------------------------------------


def projects_total(grades):
    '''
    projects_total that takes in grades and computes the total project grade
    for the quarter according to the syllabus. 
    The output Series should contain values between 0 and 1.
    
    :Example:
    >>> grades_fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(grades_fp)
    >>> out = projects_total(grades)
    >>> np.all((0 <= out) & (out <= 1))
    True
    >>> 0.7 < out.mean() < 0.9
    True
    '''

    #every thing contain proj
    col = grades.columns
    projAll = []
    for i in col:
        # get rid of checkpt
        if ('proj' in i) and ('check' not in i):
            projAll.append(i)
    projTB = grades[projAll]
    #replace nan to 0
    projTB = projTB.fillna(0)
    #find all max pt
    maxpt = []
    rest = []
    for i in projAll:
        if 'Max' in i:
            maxpt.append(i)
        else:
            #get rid of lateness
            if 'Late' not in i:
                rest.append(i)
    maxtb = projTB[maxpt]
    # find total maxpt can get
    total = maxtb.sum(axis = 1).iloc[0]

    #find student pt
    student_proj = projTB[rest]
    student_total = student_proj.sum(axis = 1)

    #find proportion compared with max pt
    return pd.Series(student_total / total)


# ---------------------------------------------------------------------
# Question # 3
# ---------------------------------------------------------------------


def last_minute_submissions(grades):
    """
    last_minute_submissions takes in the dataframe 
    grades and a Series indexed by lab assignment that 
    contains the number of submissions that were turned 
    in on time by the student, yet marked 'late' by Gradescope.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = last_minute_submissions(grades)
    >>> isinstance(out, pd.Series)
    True
    >>> np.all(out.index == ['lab0%d' % d for d in range(1,10)])
    True
    >>> (out > 0).sum()
    8
    """

    result = {}
    #using assignment name get key
    name = get_assignment_names(grades)
    key = name['lab']

    #find all lab related
    lab_relate = []
    late = []
    for i in grades.columns:
        if 'lab' in i:
            lab_relate.append(i)
            if 'Late' in i:
                late.append(i)
    labAll = grades[lab_relate]
    lateAll = labAll[late]

    for x in range(len(key)):
        count = 0
        splited = lateAll[late[x]].str.split(":")
        #set threshold at 7hrs
        hr = splited.str[0].astype(int)
        mints = splited.str[1].astype(int)
        sec = splited.str[2].astype(int)

        count = count + ((hr <= 7) & (hr > 0)).sum()
        count = count + ((mints > 0) & (hr == 0)).sum()
        count = count + ((sec > 0) & (hr == 0) & (mints == 0)).sum()

        #store in result
        result[key[x]] = count

    return pd.Series(result)


# ---------------------------------------------------------------------
# Question #4
# ---------------------------------------------------------------------

def lateness_penalty(col):
    """
    lateness_penalty takes in a 'lateness' column and returns 
    a column of penalties according to the syllabus.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> col = pd.read_csv(fp)['lab01 - Lateness (H:M:S)']
    >>> out = lateness_penalty(col)
    >>> isinstance(out, pd.Series)
    True
    >>> set(out.unique()) <= {1.0, 0.9, 0.7, 0.4}
    True
    """

    #count corresponding hrs
    oneW = 24 * 7
    twoW = 2 * 24 * 7

    #split and count
    splited = col.str.split(":")
    #convert to right type
    hr = splited.str[0].astype(int)

    z = hr #make a copy
    # 7 is previous threshold
    z = z.apply(lambda x: 1 if x <= 7 else x)
    #check onw week deadline
    z = z.apply(lambda x: 0.9 if (x > 7) & (x <= oneW) else x)
    #check two week deadline
    z = z.apply(lambda x: 0.7 if (x > oneW) & (x <= twoW) else x)
    z = z.apply(lambda x: 0.4 if x > twoW else x)

    return pd.Series(z)


# ---------------------------------------------------------------------
# Question #5
# ---------------------------------------------------------------------

def process_labs(grades):
    """
    process_labs that takes in a dataframe like grades and returns
    a dataframe of processed lab scores. The output should:
      * share the same index as grades,
      * have columns given by the lab assignment names (e.g. lab01,...lab10)
      * have values representing the lab grades for each assignment, 
        adjusted for Lateness and scaled to a score between 0 and 1.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = process_labs(grades)
    >>> out.columns.tolist() == ['lab%02d' % x for x in range(1,10)]
    True
    >>> np.all((0.65 <= out.mean()) & (out.mean() <= 0.90))
    True
    """

    # get all lab names
    names = get_assignment_names(grades)['lab']
    all_labs = grades.loc[:,names]
    # get all lateness
    late_name = [x + ' - Lateness (H:M:S)' for x in names]
    all_lates = grades.loc[:,late_name]
    # get lateness penalty
    penalized = all_lates.apply(lateness_penalty)
    # find all max pt to calculate proportion
    max_pt = [ x + ' - Max Points' for x in names]
    all_max = grades.loc[:,max_pt]

    #scale it btw 0 and 1
    for i in range(len(names)):
        all_labs.loc[:,names[i]] = (all_labs[names[i]] * penalized[late_name[i]])/all_max[max_pt[i]]

    return all_labs


# ---------------------------------------------------------------------
# Question #6
# ---------------------------------------------------------------------

def lab_total(processed):
    """
    lab_total takes in dataframe of processed assignments (like the output of 
    Question 5) and computes the total lab grade for each student according to
    the syllabus (returning a Series). 
    
    Your answers should be proportions between 0 and 1.

    :Example:
    >>> cols = 'lab01 lab02 lab03'.split()
    >>> processed = pd.DataFrame([[0.2, 0.90, 1.0]], index=[0], columns=cols)
    >>> np.isclose(lab_total(processed), 0.95).all()
    True
    """

    toDrop = processed.min(axis = 1)
    dropped = processed.sum(axis = 1) - toDrop
    return dropped / (len(processed.columns) -1)


# ---------------------------------------------------------------------
# Question # 7
# ---------------------------------------------------------------------

def total_points(grades):
    """
    total_points takes in grades and returns the final
    course grades according to the syllabus. Course grades
    should be proportions between zero and one.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = total_points(grades)
    >>> np.all((0 <= out) & (out <= 1))
    True
    >>> 0.7 < out.mean() < 0.9
    True
    """

    #calculate lab
    names = get_assignment_names(grades)
    grades = grades.fillna(0)
    #process lab
    processed = process_labs(grades)
    #get lab total
    lab_final = lab_total(processed) * 0.2

    #calculate projects
    proj_final = projects_total(grades) * 0.3

    #calculate checkpt
    ckpt = names['checkpoint']
    raw_ckpt = grades.loc[:,ckpt].fillna(0).sum(axis = 1)
    #find sumed max check pt scores
    maxckpt = [x + " - Max Points" for x in ckpt]
    max_ckpt = grades.loc[:,maxckpt].sum(axis = 1)
    #calculate proportion
    ckpt_final = (raw_ckpt / max_ckpt) * 0.025

    #calculate discussion
    discpt = names['disc']
    raw_disc = grades.loc[:,discpt].fillna(0).sum(axis = 1)
    #find sumed max check pt scores
    maxdisc = [x + " - Max Points" for x in discpt]
    max_disc = grades.loc[:,maxdisc].sum(axis = 1)
    #calculate proportion
    disc_final = (raw_disc/ max_disc) * 0.025

    #calculate exams
    raw_mid = grades.loc[:,names['midterm']].fillna(0)
    raw_mid = raw_mid['Midterm']
    mid_final = (raw_mid /grades.loc[:,'Midterm - Max Points']) * 0.15

    #final
    raw_fin = grades.loc[:,names['final']].fillna(0)
    raw_fin = raw_fin['Final']
    fin_final = (raw_fin /grades.loc[:,'Final - Max Points']) * 0.3

    #combined all
    result = (lab_final + proj_final + ckpt_final + disc_final + mid_final + fin_final)
    return result


def final_grades(total):
    """
    final_grades takes in the final course grades
    as above and returns a Series of letter grades
    given by the standard cutoffs.

    :Example:
    >>> out = final_grades(pd.Series([0.92, 0.81, 0.41]))
    >>> np.all(out == ['A', 'B', 'F'])
    True
    """

    def help_func(pt):
        if pt >= 0.9:
            return 'A'
        elif (pt < 0.9) & (pt >= 0.8):
            return 'B'
        elif (pt < 0.8) & (pt >= 0.7):
            return 'C'
        elif (pt < 0.7) & (pt >= 0.6):
            return 'D'
        else:
            return 'F'

    return total.apply(help_func)

def letter_proportions(grades):
    """
    letter_proportions takes in the dataframe grades 
    and outputs a Series that contains the proportion
    of the class that received each grade.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = letter_proportions(grades)
    >>> np.all(out.index == ['B', 'C', 'A', 'D', 'F'])
    True
    >>> out.sum() == 1.0
    True
    """

    #get final grade
    total = total_points(grades)
    #get letter
    letter = final_grades(total)
    #find proportion
    return letter.value_counts(normalize = True)

# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------

def simulate_pval(grades, N):
    """
    simulate_pval takes in the number of
    simulations N and grades and returns
    the likelihood that the grade of seniors
    was worse than the class under null hypothesis conditions
    (i.e. calculate the p-value).

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = simulate_pval(grades, 100)
    >>> 0 <= out <= 0.1
    True
    """

    #get observed data
    level = grades['Level'].to_frame()
    level['grades'] = total_points(grades)
    #calculate rest class avg
    avg = level[level['Level'] != 'SR'].mean().iloc[0]
    # find number of senior
    seniors = len(level[level['Level'] == 'SR'])
    #find senior avg
    se_avg = level[level['Level'] == 'SR'].mean().iloc[0]

    #random pick senior and find avg
    result = []
    for i in range(N):
        result.append(np.random.choice(level['grades'],size = seniors).mean())

    #calculate p
    return (pd.Series(result) < se_avg).mean()/10


# ---------------------------------------------------------------------
# Question # 9
# ---------------------------------------------------------------------


def total_points_with_noise(grades):
    """
    total_points_with_noise takes in a dataframe like grades, 
    adds noise to the assignments as described in notebook, and returns
    the total scores of each student calculated with noisy grades.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = total_points_with_noise(grades)
    >>> np.all((0 <= out) & (out <= 1))
    True
    >>> 0.7 < out.mean() < 0.9
    True
    """

    #get all assignment name to add or subtract
    names = get_assignment_names(grades)
    all_name = []
    for i in names.keys():
        all_name.extend(names[i])

    #find rows and cols number
    rows = len(grades)
    cols = len(all_name)
    events = np.random.normal(0, 2, size=(rows, cols))

    #make sure it is between 0 and 100
    grades.loc[:,all_name] = np.clip((grades.loc[:,all_name] + events),a_min = 0,
                                     a_max = 100)

    final_score = total_points(grades)
    return final_score


# ---------------------------------------------------------------------
# Question #10
# ---------------------------------------------------------------------

def short_answer():
    """
    short_answer returns (hard-coded) answers to the 
    questions listed in the notebook. The answers should be
    given in a list with the same order as questions.

    :Example:
    >>> out = short_answer()
    >>> len(out) == 5
    True
    >>> len(out[2]) == 2
    True
    >>> 50 < out[2][0] < 100
    True
    >>> 0 < out[3] < 1
    True
    >>> isinstance(out[4][0], bool)
    True
    >>> isinstance(out[4][1], bool)
    True
    """

    result = []
    result = ['On average, the differences between two'
              'groups is about the same, with very little differences']
    result.append(68.0374)
    Third = [63.55140186915889,71.58878504672896]
    result.append(Third)
    result.append(0.14766355140186915)
    result.append([True,False])
    return result

# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': ['get_assignment_names'],
    'q02': ['projects_total'],
    'q03': ['last_minute_submissions'],
    'q04': ['lateness_penalty'],
    'q05': ['process_labs'],
    'q06': ['lab_total'],
    'q07': ['total_points', 'final_grades', 'letter_proportions'],
    'q08': ['simulate_pval'],
    'q09': ['total_points_with_noise'],
    'q10': ['short_answer']
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
                In %s, part %s is missing" %(q, elt)
                raise Exception(stmt)

    return True
