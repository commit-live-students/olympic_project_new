## Unusual Performances

### Some countries perform better than the others, some perform worse. In this task, we will try to identify which countries' performances have been exceptionally better or worse with respect to the other countries that participated with them

Create two new variables low and high, and set values 0.05 and 0.95 respectively.These two variables are the lower and upper bound of your quantile range

Write code for finding out the values at both the quantile range for the column 'Total' using DataFrame.quantile() 

Countries whose total medal counts is above or below the above calculated values, are the countries with unusually(good or bad) performances.

## Create a function 'q07_unusual_performances()' that:
    
    a)takes the dataframe , lower percentile value, higher percentile value as parameters and returns two dataframes filtered based on the two percentile values
    
    
Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable1  |pandas.DataFrame| compulsory    |               | dataframe to be loaded        |
| variable2  |float          | compulsory    |               | lower quantile value        |
| variable3  |float          | compulsory    |               | upper quantile value        |


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable1 | pandas.DataFrame             | Dataframe containing countries having total medal count lesser than the lower quantile value of the total medals                 |
| variable2 | pandas.DataFrame              | Dataframe containing countries having total medal count greater than the upper quantile value of the total medals                            |
    
    
    