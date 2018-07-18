# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:59:37 2018

@author: nnair
"""

from unittest import TestCase
from greyatomlib.olympic_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
from inspect import getfullargspec
import pandas


path = "./data/olympics.csv"
df=q01_rename_columns(path)    
df=q02_country_operations(df)

#Calling the function
df=q03_better_event(df)    
class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q03_better_event).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (147, 18), "The Expected return shape does not match with the given return shape")
      
    def test_values(self):
        self.assertEqual(df.BetterEvent.value_counts().max(),143, "The new column 'BetterEvent' hasn't been created properly. Following should be the value counts: Summer-143, Winter-3, Both-1")