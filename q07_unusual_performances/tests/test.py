# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:58:25 2018

@author: nnair
"""
from unittest import TestCase
from greyatomlib.olympic_project_new.q07_unusual_performances.build import q07_unusual_performances, q02_country_operations, q01_rename_columns
from inspect import getfullargspec

path = "./data/olympics.csv"
df=q01_rename_columns(path)    
df=q02_country_operations(df)

low=0.05
high=0.95

quant_df = df['Total'].quantile([low, high])

DFLow, DFHigh= q07_unusual_performances(df, quant_df.loc[low], quant_df.loc[high])

BetterTeams=['France',
 'Germany',
 'Great Britain',
 'Italy',
 'Soviet Union',
 'Sweden',
 'United States']


WorseTeams=['Bahrain',
 'Barbados',
 'Bermuda',
 'Botswana',
 'Burundi',
 'Ivory Coast',
 'Cyprus',
 'Djibouti',
 'Eritrea',
 'Gabon',
 'Grenada',
 'Guatemala',
 'Guyana',
 'Iraq',
 'Macedonia',
 'Mauritius',
 'Montenegro',
 'Netherlands Antilles',
 'Niger',
 'Paraguay',
 'Senegal',
 'Sudan',
 'Togo',
 'Tonga',
 'United Arab Emirates',
 'Virgin Islands']



class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q07_unusual_performances).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

                              
    def test__better_performance(self):
        self.assertListEqual(sorted(DFHigh), sorted(BetterTeams), "Top Unusual Country list not made properly. Expected " + str(sorted(BetterTeams)) + " but got " +str(sorted(DFHigh)))    
      
   
    def test__worse_performance(self):
        self.assertListEqual(sorted(DFLow), sorted(WorseTeams), "Bottom Unusual Country list not made properly. Expected " + str(sorted(WorseTeams)) + " but got " + str(sorted(DFLow)))
        