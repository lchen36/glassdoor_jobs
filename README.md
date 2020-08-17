# Business Analyst Salary Estimator: Project Overview
* Scraped over 1000 job related information include: 'Job Title','Salary Estimate','Location',etc from glassdoor using Python and Selenium.
* Engineered features from the text of each 'job description' to quantify the value companies put on Python, Excel, SQL, Tableau.
* Summarized data instantly with Pivot Tables by comparing different variables(avg_salary, avg_salary,python etc).
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

<img width="394" alt="截屏2020-08-16 下午11 11 56" src="https://user-images.githubusercontent.com/68720881/90354016-ec343180-e015-11ea-96a9-063d172636b7.png">
<img width="397" alt="截屏2020-08-16 下午11 15 05" src="https://user-images.githubusercontent.com/68720881/90354133-54831300-e016-11ea-9307-4d2f923aa5c5.png">


