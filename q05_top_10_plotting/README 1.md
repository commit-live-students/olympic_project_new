## Plotting Top 10

### From the lists that you have created from the above task, plot the medal count of the countries present for better visualisation

## Write a function `q05_top_10_plotting()` that:
    
    a)takes the dataframe and the three above created lists(Top10Summer,Top10Winter, Top10) as parameters and subsets the dataframe based on the country names present in the list
    b)takes each subsetted dataframe and plots a bar graph between the country name and total medal count(according to the event)
   
    
Parameters :

| parameter | dtype          | Argument Type | default value | description                   |
|-----------|----------------|---------------|---------------|-------------------------------|
| variable1  |pandas.DataFrame| compulsory    |               | dataframe to be loaded        |
| variable2  |list          | compulsory    |               | list that will help subset        |
| variable3  |list          | compulsory    |               | list that will help subset        |
| variable4  |list          | compulsory    |               | list that will help subset        |



Returns:
There is no return parameter for the function. The plot should be similar to (link to be pasted)