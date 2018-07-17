## Data Preprocessing

The data that we have is not clean. In the next couple of tasks, we will try to transform the data in a format that will make it easier to perform data operations.

    
## 1. Renaming Columns

The first task is to rename columns for better feature handling

Write a function q01_rename_columns that :
    
    a)Reads CSV file and converts CSV data to dataframe.
    b)Skips first row.
    c)Renames the first row of the newly created dataframe to "Country". 
    d)Renames column containing 01, 02 and 03 to the Gold(_Event), Silver(_Event) and Bronze(_Event)
    e)Renames Total, Total.1, Combined Total to Total_Summer, Total_Winter, Total respectively
    f)Returns the updated dataframe

Parameters :

| parameter | dtype  | Argument Type | default value | description                   |
|-----------|--------|---------------|---------------|-------------------------------|
| path      | string | compulsory    |               | path of the csv file location |

Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |


