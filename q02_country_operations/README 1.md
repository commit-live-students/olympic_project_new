## 2. Cleaning Data

The second task is to make changes to Country column

## Write a function `q02_country_operations` that    
   
    a)Makes use of the previously created dataframe from q01_rename_columns.
    b)Removes unnecessary characters from the column 'Country'.
    c)Extracts country name from 'Country' and creates a new column called 'Country Name'.
    d)Removes unnecessary spaces from the newly created column
    e)Returns the updated dataframe
    
Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable  |pandas.DataFrame| compulsory    |               | Dataframe to be loaded        |

Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable | pandas.DataFrame | Dataframe with above operations inculcated |
