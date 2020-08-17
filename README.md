# Business Analyst Salary Estimator: Project Overview
* Scraped over 1000 job related information include: 'Job Title','Salary Estimate','Location'from glassdoor using Python and Selenium.
* Engineered features from the text of each 'job description' to quantify the value companies put on Python, Excel, SQL, Tableau.
* Summarized data instantly with Pivot Tables by comparing different variables.
* Created a WordCloud from the text of each 'job description', which represent the frequence and importance of each word. The key to being a Business Analyst.
* Optimized Linear Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Build a client facing API using flask

## Code and Resources Used
**Python Version:** 3.7 

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

**Scraper Tutorial:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905 by Ömer Sakarya

**Data Science Project from Scratch:** https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=1 by Ken Jee

## Web Scraping
Scraped 1000 job postings from glassdoor.com. Information included:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue

## Data Cleaning
Made the following changes and created the following variables so that it was usable for our model:
- Parsed numeric data out of salary
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
  - Python
  - Excel
  - SQL
  - Tableau
- Column for simplified job title and Seniority
- Column for description length

## EDA
After looking at the distribution of the data and the value counts for the various categorical variables. Below are a few highlights from the Pivot Table.

<img width="284" alt="截屏2020-08-16 下午11 24 09" src="https://user-images.githubusercontent.com/68720881/90354545-9fe9f100-e017-11ea-8fb7-97fb00dbba40.png"><img width="397" alt="截屏2020-08-16 下午11 15 05" src="https://user-images.githubusercontent.com/68720881/90354133-54831300-e016-11ea-9307-4d2f923aa5c5.png"><img width="284" alt="截屏2020-08-16 下午11 20 40" src="https://user-images.githubusercontent.com/68720881/90354385-32d65b80-e017-11ea-803f-5691cf32d49c.png">

## Model Building
Transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried two different models and evaluated them using Mean Absolute Error:
 
 - **Multiple Linear Regression:** Baseline for the model.
 
 - **Lasso Regression:** Because of the sparse data from the many categorical variables.
 
 - **Random Forest:** Because of the sparsity associated with the data.
 
 ## Model performance
The Lasso Regression model far outperformed the other approaches on the test and validation sets:

- **Lasso Regression:** MAE = 16.17

- **Linear Regression:** MAE = 65791326.18
