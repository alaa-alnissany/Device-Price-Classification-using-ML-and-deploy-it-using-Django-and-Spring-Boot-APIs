#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

class nan_the_none_real_zeros(BaseEstimator,TransformerMixin):
  def __init__(self,replaced_val=0):
    print('Initialising transformer...')
    self.replaced_val = replaced_val
  def fit(self,X,y=None):
    self.val = np.NaN
    return self
  def transform(self, X):
    if 'id' in X.columns:
      X.drop("id",axis =1, inplace = True)
    X.loc[X["px_height"]==self.replaced_val, "px_height"] = self.val
    X.loc[X["px_width"]==self.replaced_val, "px_width"] = self.val
    return X

class columns_selection (BaseException,TransformerMixin):
  def __init__(self,selected_features = ["ram","battery_power" ,"px_height","px_width"]):
    self.selected_features = selected_features
    self.all_columns = ['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
                        'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
                        'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']
  def fit(self,X,y=None):
    pass
    return self
  def transform(self, X):
    X = pd.DataFrame(X,columns =self.all_columns)
    X = X[self.selected_features]
    return X



def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DPC.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
