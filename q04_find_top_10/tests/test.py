# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:22:23 2018

@author: nnair
"""

from unittest import TestCase
from greyatomlib.olympic_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event,q02_country_operations, q01_rename_columns
from inspect import getfullargspec
import pandas


path = "./data/olympics.csv"
df=q01_rename_columns(path)    
df=q02_country_operations(df)
df=q03_better_event(df)    

#Calling the function
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(df,'Total_Summer', 'Total_Winter','Total')

SummerList=['United States',
 'Soviet Union',
 'Great Britain',
 'France',
 'Germany',
 'Italy',
 'Sweden',
 'Hungary',
 'China',
 'Australia']

WinterList=['Norway',
 'United States',
 'Austria',
 'Germany',
 'Soviet Union',
 'Canada',
 'Finland',
 'Sweden',
 'Switzerland',
 'Russia']

Top= ['United States',
 'Soviet Union',
 'Great Britain',
 'Germany',
 'France',
 'Italy',
 'Sweden',
 'China',
 'East Germany',
 'Russia']

CommonElements= ['Germany', 'Sweden', 'United States', 'Soviet Union'] 


class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q04_find_top_10).args
        self.assertEqual(len(arg), 4, "Expected argument(s) %d, Given %d" % (4, len(arg)))

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")
      
    def test_df_summer_list_test(self):
        self.assertListEqual(sorted(Top10Summer), sorted(SummerList), "Top 10 Summer List not made properly")    
    
    def test_df_winter_list_test(self):
        self.assertListEqual(sorted(Top10Winter), sorted(WinterList), "Top 10 Winter List not made properly")
               
    def test_df_top_list_test(self):
        self.assertListEqual(sorted(Top10), sorted(Top), "Top 10 Overall List not made properly")
       
    def test_df_common_list_test(self):
        self.assertListEqual(sorted(Common), sorted(CommonElements), "Common elements are : " + str(sorted(Common)) + "and not" + str(sorted(CommonElements)))    