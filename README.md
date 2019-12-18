# Equity-In-Hollywood

### Background

The Bechdel Test is a measure of representation of women in fiction. It asks whether a work features at least two women who talk to each other about something other than a man. The test is used as an indicator for the active presence of women in the entire field of film and other fiction, and to call attention to gender inequality in fiction. It wasn’t until 2013 that media industry studies showed that films that pass the test financially outperform those who do not. These findings lead Hollywood to believe that the way to make more money might be to “put more women on screen”.

### Our Task
We decided to take this study into our own hands by analyzing film data from 1970 to 2013, focusing on the following questions:

1. Have more films passed the Bechdel test over time?
2. Which genres dominate or under perform in passing the Bechdel test?
3. Is the American public interested in diverse Hollywood titles?
4. Are Hollywood filmmakers investing in movies that pass the Bechdel test?
5. What are the trending topics of conversation in films that pass the third criteria of the test?

Our visualization includes a Python Flask-powered RESTful API, HTML/CSS, Javascript, and SQLite database. Our final project:

- A combination of web scraping and Plotly. 
- Includes one other JS library (Bideo.js)
- Powered by a dataset with at least 100 records
- Includes user-driven interaction (e.g., menus, dropdowns)
- At least three views in our final visualization

### Data Used 
We used a combination of CSV files and an API that we converted to CSV formatting for this study. The data included information from 1970 to 2013 with the following points of interest: Year, IMDB rating, Title, Test Results, Domestic Gross, International Gross, and Budget. We used a series of pandas functions in Jupyter Notebook to Extract and Transform this data and used SQL queries to Load it into a database for use on this site.

- [Bechdel Test API](http://bechdeltest.com/api/v1/doc)
- [FiveThirtyEight Repository](https://github.com/fivethirtyeight/data/blob/master/bechdel/movies.csv)
- [IMDB Datasets](https://datasets.imdbws.com/)

### Analysis Summary
In 2013, media industry studies showed that films that pass the test financially outperform those who do not. Our assumption was the more Bechdel criteria a movie meets, the greater the gross revenue. Our data, shows that general idea, but it also shows a budget trend line that moves with the gross. It could be the possible cause of the gross trend. The industry may have noticed the demand for equitable representation of women on screen and invested more in movies that pass the Bechdel Test.

For movies that did pass the Bechdel test in 2009 versus 2019, the topics of discussion (that were not about men), have become darker in tone. This could either reflect a change in cultural trends or simply reflect casting of more women in serious, complex roles.

### Copyright

Gender Equity in Hollywood © 2019. All Rights Reserved.
