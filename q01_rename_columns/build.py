import pandas as pd

path = "../data/olympics.csv"

def q01_rename_columns(path):
    # Reads CSV file and converts CSV data to dataframe. the path for the file is `./data/olympics.csv'
    # Skips first row.
    df = pd.read_csv(path, skiprows=1)
    
    #Renames the first column of the newly created dataframe to "Country".
    df = df.rename(index=str, columns={'Unnamed: 0' : 'Country'})

    # Renames column containing 01, 02 and 03 to the Gold(_Event), Silver(_Event) and Bronze(_Event)
    df = df.rename(index=str, columns={
        '01 !' : 'Gold_Summer',
        '02 !' : 'Silver_Summer',
        '03 !' : 'Bronze_Summer',
        '01 !.1' : 'Gold_Winter',
        '02 !.1' : 'Silver_Winter',
        '03 !.1' : 'Bronze_Winter',
        '01 !.2' : 'Gold_Total',
        '02 !.2' : 'Silver_Total',
        '03 !.2' : 'Bronze_Total'
    })
    
    # Renames Total, Total.1, Combined Total to Total_Summer, Total_Winter, Total respectively
    df = df.rename(index=str, columns={
        'Total' : 'Total_Summer',
        'Total.1' : 'Total_Winter',
        'Combined total' : 'Total'
    })
    
    # Returns the updated dataframe
    return df


