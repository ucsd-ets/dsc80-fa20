
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class LowStdColumnDropper(BaseEstimator, TransformerMixin):

    def __init__(self, thresh=0):
        '''
        Drops columns whose standard deviation is less than thresh.
        '''
        self.thresh = thresh

    def fit(self, X, y=None):
        """
        ...
        """

        self.columns_ = ...
        
        return self

    def transform(self, X, y=None):
        """
        >>> data = pd.read_csv('cars.csv').select_dtypes('number')
        >>> lvd = LowStdColumnDropper(thresh=10)
        >>> out = lvd.fit_transform(data)
        >>> out.shape[0] == data.shape[0]
        True
        >>> out.shape[1] <= data.shape[1]
        True
        """
        
        
        return ...
