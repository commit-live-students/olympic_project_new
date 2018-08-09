# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)  
    
def remove_text_inside_brackets(text, brackets='()[]'):
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # : open, : close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars).replace('\xa0','')

def q02_country_operations(OlympicsDF):
    OlympicsDF['Country_Name']=OlympicsDF['Country']
    OlympicsDF['Country_Name']= OlympicsDF['Country_Name'].apply(remove_text_inside_brackets)
     
    return OlympicsDF
df=q02_country_operations(OlympicsDF)
df.iloc[100,16]



