## Top 10
So we figured out which is a better event for each country. 
Let's move on to finding out the best performing countries across all events

So in this task we will try to find
 
- Which are the top 10 performing teams at summer event (with respect to total medals), winter event and overall?
- How many teams are present in all of the three lists above?

## Write a function `q04_find_top_10()` that:

    a)Makes use of the dataframe created from the previous task.
    b)Finds index of top 10 values of the three columns passed('Total_Summer', 'Total_Winter','Total') as parameters
    c)Creates a list of the country names from 'Country_Name' assosicated with that index for each column
    d)Finds the common elements between the three lists and stores it in a new list
    e)Returns the four above created lists

**Note that the last row of the dataframe hsa totals, and therefore you will have to remove the last row before performing any operations**


Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable1  |pandas.DataFrame| compulsory    |               | dataframe to be loaded        |
| variable2  |string          | compulsory    |               | column name        |
| variable3  |string          | compulsory    |               | column name        |
| variable4  |string          | compulsory    |               | column name        |


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable1 | list             | list of top 10 summer  countries                   |
| variable2 | list             | list of top 10 winter countries                   |
| variable3 | list             | list of top 10 countries                   |
| variable4 | list             | list of common countries                   |

