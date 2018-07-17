## Top performing country(Gold) 

Winning silver or bronze medals is a big achievement but winning gold is bigger.  

### Using the above created dataframe subsets, in this task we will find out which country has had the best performance with respect to the ratio between gold medals won and total medals won.


Write a function q06_golden_winner() that:
    
    a)Once again, takes the dataframe and the three above created lists(Top10Summer,Top10Winter, Top10) as parameters and subsets the dataframe based on the country names present in the list 
    b)creates a new list 'Gold_Ratio' that stores the ratio between gold medals won and total medals won for each country depending on the event
    c)returns the country having the highest ratio all the three scenarios 


Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable1  |pandas.DataFrame| compulsory    |               | dataframe to be loaded        |
| variable2  |list          | compulsory    |               | list that will help subset        |
| variable3  |list          | compulsory    |               | list that will help subset        |
| variable4  |list          | compulsory    |               | list that will help subset        |


Returns:

| returns  | dtype            | description                                |
|----------|------------------|--------------------------------------------|
| variable1 | string             | country name with the highest ratio                 |
| variable2 | string             | country name with the highest ratio                 |
| variable3 | string             | country name with the highest ratio                 |
