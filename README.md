# chicago_cta

# Helping business owners in Chicago

## Project Summary

Our project will help a business owner in Chicago to open his/her shop at a new location. 
For the new shop s/he is trying to open is a deli that sells sandwiches and coffee.
To help our customer, we will focus on maximizing the expected profits by estimating the revenues and costs. 

### Revenue
Revenue will come from the sales of products (sandwiches and coffee) which is the sum of price the items multiplied by how many each items are sold. The prices will be adjusted according the cost within a reasonable range. The number of sales will be estimated using the traffic flow by the public transit. 

### Cost
Cost will come from many different factors. There will be fixed cost, such as rent and employee salary. The variable costs will be cost of raw materials. For a quick assessment, we will mainly be using the rent the s/he has to pay. The cost of ingredients and paying the employees will be consistent regardless of the location, therefore we will delve more into it after we are done with the factors with higher impact. 

## Project motivation

I propose to use Chicago neighborhood CTA transportation data, business activities, 
and property values to help small business owners to find the best location for their business.  
First, due to the characteristics of the those shops, they require a lot of foot traffic to be successful, 
often times near a public transportation stations. Second, we need to check the business activities in the neighborhood, 
to see whether the neighborhood is already saturated with similar business
and also see if there are other business that can help our customer's business. Thirdly, we need to look at the real-estate
values of the neighborhood. Often times the largest expenses in running a business comes from the rent, therefore considering the rent will be important factor in estimating the expected expenses and profits.  

## Project data

### Transit data
 - **CTA - Ridership - 'L' Station Entries - Daily Totals**
 
The database tracks the number of people to go through the turnstiles at every Chicago "L" station since 2001.

 - **[CTA - Ridership - Bus Routes - Daily Totals by Route](https://data.cityofchicago.org/Transportation/CTA-Ridership-Bus-Routes-Daily-Totals-by-Route/jyb9-n7fm)**
 
The database tracks the number of people to go through the turnstiles at every Chicago CTA bus station since 2001.
 
### Business data

- **[Business Licenses](https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses/r5kz-chrr)**

The database contains the business licenses issued by City of Chicago from 2001.

- **[Zillow Real Estate Data](https://www.zillow.com/research/data/)**

The database contains the medium residential property renting values for each zip code from 2010.

(Ideally, we would want data of all traffic, including foot and cars, and the density of the population in the area to estimate the potential number of customers, and real estate data for retail stores with differe square footage. Also, in addition to those data, to calculate the costs, we will need data on wage limit in Chicago, wage distribution, and costs of the raw material)

## Preliminary Analysis
### Warm up
#### Stations with the highest average ridership
Station with the highest average ridership per day is Clark/Lake, with mean of 13972.55(~13973)  people per day. 

#### What’s the standard deviation for the Washington/Wabash stop? What’s your hypothesis for why?

The standard deviation of the ridershp for Washington/Wabash is 2831.97 (~2832). 

In the data set, Washington/Wabash which is the staion hosting 5 lines (Green, Brown, Purple Express, Pink and Orange) has less than 100 customers per day until 8/30/2017, then surges up to thousands on 8/31/2017. From this observation, we can infer that Washington/Wabash was either under construction or closed.

By cross checking with [CTA news](https://www.transitchicago.com/washingtonwabash/) Washington/Wabash opened on August 31, 2017. From this information, we can conclude that ~100 customers per day until 8/30/2017 is probably operators or test users.

There are two other dates 2017-10-18 and 29 that have very low ridership (<100), which we can infer that the station was closed, however, since I could not find any other online data to confirm this, the two dates will be included in inferring the average ridership at Washington and Wabash.

For more detailed description, please check [this notebook](https://github.com/hyojunada/chicago_cta/blob/master/notebook/Warm_Up.ipynb) which explains step-by-step of the analysis. 

### Traffics

With the CTA 'L' ridershp data, we can estimate how many potential customers will be passing by the station of our interest, and which day of the week will have the highest customers. 
By visualizing CTA 'L' riderships at each stations we can get a general overview of which stations or areas have the highest foot traffic. It is 

![fig1](https://github.com/hyojunada/chicago_cta/blob/master/result/cta_l_ridership.png)
Magnified CTA ridership for the loop 
![fig1-1](https://github.com/hyojunada/chicago_cta/blob/master/result/loop_cta_l_ridership.png)


Then I looked at the changes in follower size (normalized over company's size) over time for individual companies in each industry
Shown below is the example for Investment Banking industry. From this I can identify which company's gaining more followers and whether it's growing faster or slower than the company norm. In [this notebook](https://github.com/hyojunada/data_incubator/blob/master/notebook/Section3-fig2_increase_of_followers_over_time.ipynb) you can do this for individual companies and see aggregated result for the entire industry. The aggregated result for the entire industry shows how much online interst the industry has compared to its size and whether the interest is growing or not. 

![fig2](https://github.com/hyojunada/data_incubator/blob/master/result/followers_size_over_time_Investment%20Banking.png)

## Next Steps
### Data aquisition and exploration
1. Use Glassdor reviews to measure employees and interviewees' opinions on the companys over time. 
2. Use the Job posting data to measure the expansion of a company as a measure of growth
3. Use the stock prices over time to measure the performance of a company.
## Build predictive model
After elementary analysis reveals an underlying trend that prompts further exploration. For my project I propose to expand these efforts by building a model that takes advantage of the underlying trend in four different data sets. I will combine LinkedIn and Glassdoor data as predictors and Job posting and stock prices as one target variable. The model will allow job seekers to be able to evaluate the potential growth of a company and this can be expanded to other groups of interests such as investorsin when evaluating a company.
