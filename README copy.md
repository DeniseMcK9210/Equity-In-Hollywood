# Equity-In-Hollywood

## Background

The Bechdel Test is a measure of the representation of women in fiction. It asks whether a work features at least two women who talk to each other about something other than a man. The test is used as an indicator for the active presence of women in the entire field of film and other fiction, and to call attention to gender inequality in fiction. It wasn’t until 2013 that media industry studies showed that films that pass the test financially out perform those who do not leading Hollywood to believe that the way to make more money might be to “put more women onscreen”. 
We decided to take this study into our own hands by analyzing film data from 1970 to 2013 to analyze the following questions:
1. Have more films passed the Bechdel test over time?
2. Which genre dominates or under-performs in passing the Bechdel test?
3. Is the American public interested in diverse Hollywood titles?
4. Are Hollywood film makers investing in movies that pass the Bechdel test?
5. Lets take a look! 

## The Data (ETL)
We used a combination of CSV files and an API that we converted to CSV format for this study. The data included information from 1970 to 2013 with the following points of interest: Year, IMDB rating, Title, Test Results, Domestic Gross, International Gross, and Budget. We used a series of pandas functions in Jupyter Notebook to Extract and Transform this data and used SQL queries to Load it into a database for use on this site.

## The Process (process summary)
After our data was loaded we were able to use it to create multiple visualizations in combination with HTML, JavaScript, D3.js, web-scraping, Plotly functions and more! 
1. HTML and CSS was used to create the framework and design of our site
2. JavaScript was used to allow functions like our drop down menu’s and filters to work properly while sorting the data. 
3. Bideo.js is an additional JavaScript library that allowed the background of our landing page to be a movie clip.
4. D3.js was used to create the liquid gauge charts at the top of our visualizations page
5. Web-scraping was used to review the comments of viewers on bechdeltest.com to determine what was discussed by two women. We created a word cloud using the extracted data with the help of requests, urllib, beautiful soup, WordCloud and matplotlib



### Copyright

Gender Equity in Hollywood © 2019. All Rights Reserved.
