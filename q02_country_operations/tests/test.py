# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:52:27 2018

@author: nnair
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:34:30 2018

@author: nnair
"""


from unittest import TestCase
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
from inspect import getfullargspec
import pandas



path = "./data/olympics.csv"
OlympicsDF=q01_rename_columns(path)
df = q02_country_operations(OlympicsDF)


class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q02_country_operations).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (147, 17), "The Expected return shape does not match with the given return shape")
      
    def test_values(self):
        self.assertEqual(df.iloc[100,16], 'Portugal', "The country names haven't been properly extracted. Expected Portugal , returned %s" %(df.iloc[100,16]) )     
    