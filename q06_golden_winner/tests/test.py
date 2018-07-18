# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:27:31 2018

@author: nnair
"""

from unittest import TestCase
from greyatomlib.olympic_project_new.q06_golden_winner.build import q06_golden_winner, q04_find_top_10, q03_better_event,q02_country_operations, q01_rename_columns
from inspect import getfullargspec

path = "./data/olympics.csv"
df=q01_rename_columns(path)    
df=q02_country_operations(df)
df=q03_better_event(df)   
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(df,'Total_Summer', 'Total_Winter','Total')


SummerGoldRatio, WinterGoldRatio, TopGoldRatio =q06_golden_winner(df, Top10Summer, Top10Winter, Top10)    



class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q06_golden_winner).args
        self.assertEqual(len(arg), 4, "Expected argument(s) %d, Given %d" % (4, len(arg)))

                              
    def test_summer_gold(self):
        self.assertEqual(SummerGoldRatio, 'China', "Country with highest gold ratio for Summer events is China and not " + str(SummerGoldRatio))    
    
    def test_winter_gold(self):
        self.assertEqual(WinterGoldRatio,'Soviet Union' , "Country with highest gold ratio for Winter events is Soviet Union and not " + str(WinterGoldRatio))
               
    def test_top(self):
        self.assertEqual(TopGoldRatio, 'China', "Country with highest gold ratio overall is China and not " + str(TopGoldRatio))
       
    