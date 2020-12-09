
This is a *summary* of the main points of the course. This is not comprehensive, but rather should help you organize the topics to better understand them!


# DSC 80 Topics: First Half

These first half topics are not organized chronologically, but instead grouped by "compute" and "statistics".

## Tabular Data Basics

* Pandas/Numpy performance considerations (run-time, memory)
* Structure of a table
* Selecting, appending, and modifying rows/columns
* Grouping and group-wise transformations
* Reshaping data (Pivot)
* Joining Data (left/right/inner/outer) and broadcast joins.
* Working with Time Series (datetime objects)

## Data Cleaning

* Differentiate different kinds of Data (Quantitative, Ordinal, Nominal) and impacts on descriptive analysis.
* Make appropriate cleaning choices: make the Dataset faithful to the Data Generating Process.

## Probabilistic Concepts

* Code empirical discrete (conditional) distributions with Pandas.
* Code the cumulative empirical distribution of a dataset.
* Handle continuous distributions through binning data.

## Statistical Tests

* Understand the anatomy and terms of hypothesis tests (null/alternative hypothesis, significance level, test-statistic, p-value).
* Design hypothesis tests using a dataset, and implement them using simulation.
* Understand and be able to code permutation tests to test if two distributions are likely different.
* Choose (and code) the best test-statistic for a permutation test: (absolute) difference in mean/median, total variation distance, KS-statistic.

## Understanding Missing Data

* Understand mechanisms of missing data: conditionally/unconditionally ignorable; non-ignorable; missing-by-design.
* Identifying mechanisms of missing data using critical reasoning about the data generating process.
* Use permutation tests to understand dependencies of attributes for conditionally ignorable missing data.

## Imputation

* Statistical consequences of dropping missing data for different mechanisms of missing data.
* Understand properties of (group-wise) single-valued imputation; know how to code it.
* Understand properties of (group-wise) probabilistic imputation; know how to code it (discrete; continuous with binning).
* Statistical implications of imputation for different missing-data types.
* Understand what multiple imputation is, and how it's useful.

# DSC 80 Topics: Second Half


## HTTP

* Request-Response Protocol
* Anatomy: request methods, headers; response status, body.
* What is `robots.txt`? Why is a retry/back-off necessary? How do you code it?
* What is JSON?

## HTML

* Parsing HTML into its DOM; the DOM is a tree!
* What are elements? tags? Which are common ones?
* Translate between a (1) the rendered HTML page, (2) the DOM tree, and (3) the HTML code.
* BeautifulSoup: Use `find` to extract elements of the DOM tree via tags.
* Data Design: converting tree-structured data into tabular data.

## Text Extraction (Regex) and Statistics on Text

* Canonicalization: what is it? How do regexes help?
* Regex: basic matching, text extraction (groups).

## Intro to Text Features (NLP)

* Bag of Words encoding: what is it? can you compute it (by hand)? what is the distance between two vectors?
* TFIDF:
    - Understand how TFIDF depends on both (1) the term, (2) the document, and (3) the corpus (document collection).
    - Compute (by hand) the term frequency, inverse-document-frequency, and TFIDF.
    - Understand how to best summarize a document given a single word.
* Understand what a Language Model is in terms of the terms: corpus, tokens, and (conditional) probability.
* How is an Ngram model calculated (by hand)?

## Feature Engineering

* Definition: quantitatively encoding measurements so that similarity between observations is reflected in the distance measure in the quantitative space.
* Quantitative Scaling: Why is this needed? Know examples where this is useful (standardization, log-scaling).
* Ordinal Encoding: know the definition, when it's appropriate to use (e.g. data type), and how to compute it by hand.
* One Hot Encoding: know the definition, when it's appropriate to use (e.g. data type), and how to compute it by hand.
* Polynomial Encoding: What notion does this capture?

## Modeling Definitions

* Prediction versus Statistical Inference
* Prediction: Classifiers vs Regression

## Model Building: Pipelines

* Basics of the Transformer and Estimator interfaces (e.g. fit/transform).
* Pipelines as computational graphs (using `Pipeline` and `ColumnTransformer`)

## Bias-Variance Trade-off

* Understand the definitions of the Bias and Variance of Predictors
* Know how to identify if a model is high/low bias, or high/low variance.
* Identify the cause of bias/variance for a given modeling-pipeline (model and/or feature complexity)

## Model Building Techniques (Handling Bias/Variance)

* What is train-test split and why is it needed?
* What is a holdout set? cross-validation? Why are they needed? What are their trade-offs?
* What is a parameter search? what is grid-search?

## Measures of Evaluation

* What are the measures of evaluating a classification/regression model? Understand how these measures depend on the problem being modeled.
* Know examples where False Positives and False Negatives have very different consequences.
* Understand accuracy, sensitivity, specificity, and precision -- and how to interpret them.
* How does evaluating a model trained on class-imbalanced data differ from a balanced dataset?

## Fairness

* Understand what parity measures, for different evaluation measures.
* Calculating the statistical significance of the difference in parity of model performance across two groups of the population.
