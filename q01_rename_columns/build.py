# %load q01_rename_columns/build.py
# default imports
import pandas as pd
path = './data/olympics.csv'

def rename_col(header_list, start_string, end_string):
    updated_dict = {}
    
    if(start_string == '# Summer'):
        word_to_append = '_Summer'
    elif(start_string == '# Winter'):
        word_to_append = '_Winter'
    else:
        word_to_append = '_Total'
        
    start_index = header_list.index(start_string)
    end_index = header_list.index(end_string)
    for pos,col_name in enumerate(header_list):
        if(pos > start_index and pos < end_index):
            if('01' in col_name):
                updated_dict[pos] = 'Gold' + word_to_append
            elif('02' in col_name):
                updated_dict[pos] = 'Silver' + word_to_append                    
            elif('03' in col_name):
                updated_dict[pos] = 'Bronze' + word_to_append                            

    return updated_dict

def q01_rename_columns(path):
    df = pd.read_csv(path, skiprows=1)
    dataSet = pd.DataFrame(df)
    dataSet.rename(columns = {'Unnamed: 0' : 'Country', 'Total' : 'Total_Summer', 'Total.1' : 'Total_Winter', 'Combined total' : 'Total'}, inplace = True)
    #dataSet.columns.values[0] = 'Country'
    #print('After rename operation, column names are: ', dataSet.columns)
    header_list = list(dataSet)
    #print('Column header list is: ', header_list)
    dict_summer = rename_col(header_list, '# Summer', '# Winter')
    dict_winter = rename_col(header_list, '# Winter', '# Games')
    dict_total = rename_col(header_list, '# Games', 'Total')
    #print('Summer dict is: ', dict_summer)    
    #print('Winter dict is: ', dict_winter)
    for key in dict_summer.keys():
        dataSet.columns.values[key] = dict_summer[key]
    for key in dict_winter.keys():
        dataSet.columns.values[key] = dict_winter[key]
    for key in dict_total.keys():
        dataSet.columns.values[key] = dict_total[key]
    
    return dataSet
q01_rename_columns(path)


