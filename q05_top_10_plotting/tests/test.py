# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:09:30 2018

@author: nnair
"""

from unittest import TestCase
from greyatomlib.olympic_project_new.q05_top_10_plotting.build import q05_top_10_plotting, q04_find_top_10, q03_better_event,q02_country_operations, q01_rename_columns
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

      
    
