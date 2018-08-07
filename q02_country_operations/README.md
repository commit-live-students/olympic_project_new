## 2. Cleaning Data

The second task is to make changes to Country column

## Write a function `q02_country_operations` that    
   
    a)Makes use of the previously created dataframe from q01_rename_columns.
    b)Extracts country name from 'Country' and creates a new column called 'Country_Name'.
    c)Removes unnecessary spaces from the newly created column
    d)Returns the updated dataframe
    
Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               | Dataframe to be loaded        |

Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |
