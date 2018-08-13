# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:09:30 2018

@author: nnair
"""
import pandas 
from unittest import TestCase
from ..build import q05_top_10_plotting, q04_find_top_10, q03_better_event,q02_country_operations, q01_rename_columns

from inspect import getfullargspec


path = "./data/olympics.csv"
df=q01_rename_columns(path)    
df=q02_country_operations(df)
df=q03_better_event(df)   
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(df,'Total_Summer', 'Total_Winter','Total')
q05_top_10_plotting(df, Top10Summer, Top10Winter, Top10)     


class TestRead_csv_data_to_df(TestCase):

    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q05_top_10_plotting).args
        self.assertEqual(len(arg), 4, "Expected argument(s) %d, Given %d" % (4, len(arg))) 
    
    def summer_df_return_instance(self):
        self.assertIsInstance(Top10Summer, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")
    
    def summer_df_return_shape(self):
        self.assertEqual(Top10Summer.shape, (10, 18), "The Expected return shape does not match with the given return shape")
    
    def summer_df_return_value(self):
        self.assertEqual(Top10Summer.iloc[9,9], 84, "The Expected return value does not match with the given return value")
     
    def winter_df_return_instance(self):
        self.assertIsInstance(Top10Winter, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")
   
    def winter_df_return_shape(self):
        self.assertEqual(Top10Winter.shape, (10, 18), "The Expected return shape does not match with the given return shape")
    
    def winter_df_return_value(self):
        self.assertEqual(Top10Winter.iloc[4,9], 100, "The Expected return value does not match with the given return value")
    
    
    def total_df_return_instance(self):
        self.assertIsInstance(Top10, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")
    
    def total_df_return_shape(self):
        self.assertEqual(Top10.shape, (10, 18), "The Expected return shape does not match with the given return shape")
        
    
    def total_df_return_value(self):
        self.assertEqual(Top10.iloc[2,2], 174, "The Expected return value does not match with the given return value")
    



