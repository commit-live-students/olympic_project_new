# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
import pandas as pd
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)


def q03_better_event(q02_country_operations):
    df = OlympicsDF
    df['BetterEvent'] = np.where((df['Total_Summer']>df['Total_Winter']),'Summer',np.where(df['Total_Summer']<df['Total_Winter'],'Winter','Both'))
    return df
q03_better_event(q02_country_operations)

