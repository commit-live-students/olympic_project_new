# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:34:30 2018

@author: nnair
"""

from unittest import TestCase
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
from inspect import getfullargspec
import pandas 



path = "./data/olympics.csv"

df = q01_rename_columns(path)

new_column_names=['Country', '# Summer', 'Gold_Summer', 'Silver_Summer',
       'Bronze_Summer', 'Total_Summer', '# Winter', 'Gold_Winter',
       'Silver_Winter', 'Bronze_Winter', 'Total_Winter', '# Games',
       'Gold_Total', 'Silver_Total', 'Bronze_Total', 'Total']

class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q01_rename_columns).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (147, 16), "The Expected return shape does not match with the given return shape")
        
    def test_read_csv_data_to_df_return_column_names(self):
        self.assertListEqual(sorted(list(df.columns.values)), sorted(new_column_names), "Expected column names not there" ) 
