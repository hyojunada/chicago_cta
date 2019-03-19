# Helping business owners in Chicago

## Project Summary

Our project will help a business owner in Chicago to open his/her shop at a new location. For the new shop s/he is trying to open is a deli that sells sandwiches and coffee. To help our customer, we will focus on maximizing the expected profits by estimating the revenues and costs. After the primary analysis of the available data, we recommend the business owner to open Clark/Lake and Lake/State 'L' stations. 

The larger goal of the project is to have an algorithm that can provide small business owners with a recommendation of where to open stores with the estimated profit for a business of their interest using traffic information, real-estate values, raw material costs, labor costs. The interaction with the business owners will be mediated by a website or GUI similar to Zillow where they can search for the location and business type and get the estimated profits.

### Revenue
Revenue will come from the sales of products (sandwiches and coffee) which is the sum of prices for the items multiplied by how many each item is sold. The prices will be adjusted according to the cost within a reasonable range. The number of sales will be estimated using the traffic flow by public transit.

### Cost
The cost will come from many different factors. There will be fixed cost, such as rent and employee salary. The variable costs will be the cost of raw materials. For a quick assessment, we will mainly be using the rent the s/he has to pay. The cost of ingredients and paying the employees will be consistent regardless of the location, therefore we will delve more into it after we are done with the factors with higher impact.

## Project motivation

I propose to use Chicago neighborhood CTA transportation data, business activities, and property values to help small business owners to find the best location for their business.
First, due to the characteristics of those shops, they require a lot of foot traffic to be successful, often times near public transportation stations. Second, we need to check the business activities in the neighborhood, to see whether the neighborhood is already saturated with similar business and also see if there are other businesses that can help our customer's business. Thirdly, we need to look at the real-estate values of the neighborhood. Often times the largest expenses in running a business comes from the rent, therefore considering the rent will be an important factor in estimating the expected expenses and profits.

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

(Ideally, we would want data of all traffic, including foot and cars, and the density of the population in the area to estimate the potential number of customers and real estate data for retail stores with different square footage. Also, in addition to those data, to calculate the costs, we will need data on wage limit in Chicago, wage distribution, and costs of the raw material)

## Preliminary Analysis
### Warm-up
#### Stations with the highest average ridership
Station with the highest average ridership per day is Clark/Lake, with a mean of 13972.55(~13973)  people per day. 

#### What’s the standard deviation for the Washington/Wabash stop? What’s your hypothesis for why?

The standard deviation of the ridership for Washington/Wabash is 2831.97 (~2832). 

In the data set, Washington/Wabash which is the station hosting 5 lines (Green, Brown, Purple Express, Pink and Orange) has less than 100 customers per day until 8/30/2017 then surges up to thousands on 8/31/2017. From this observation, we can infer that Washington/Wabash was either under construction or closed.

By cross-checking with [CTA news](https://www.transitchicago.com/washingtonwabash/) Washington/Wabash opened on August 31, 2017. From this information, we can conclude that ~100 customers per day until 8/30/2017 is probably operators or test users.

There are two other dates 2017-10-18 and 29 that have very low ridership (<100), which we can infer that the station was closed, however, since I could not find any other online data to confirm this, the two dates will be included in inferring the average ridership at Washington and Wabash.

For a more detailed description, please check [this notebook](https://github.com/hyojunada/chicago_cta/blob/master/notebook/Warm_Up.ipynb) which explains step-by-step of the analysis. 

### Traffics

With the CTA 'L' ridership data, we can estimate how many potential customers will be passing by the station of our interest, and which day of the week will have the highest customers. 
By visualizing CTA 'L' ridership at each station we can get a general overview of which stations or areas have the highest foot traffic. It is 

<p align="center">
 <img  src="https://github.com/hyojunada/chicago_cta/blob/master/result/cta_l_ridership.png">
</p>

Magnified CTA ridership for the loop 
<p align="center">
 <img width="438/3" height="511/3"  src="https://github.com/hyojunada/chicago_cta/blob/master/result/loop_cta_l_ridership.png">
</p>

Next, we identify which stations actually have the highest ridership. Before we go into analysis, we have to decide what kind of deli/coffee shop the owner is interested in; is it going to be a fast-paced, take-out shop for business people, or is it going to have a more relaxed atmosphere for brunch and hanging out? In our case, the owner is interested in opening a fast-paced deli/coffee shop. The table below shows that the order of highest average ridership for the stations is indeed different for weekdays and holidays and therefore it is essential to consider the two-day types separately for our purpose. 

<p align="center">
  <img src="https://github.com/hyojunada/chicago_cta/blob/master/result/mean_ridership.png">
</p>

We look at the 5 stations with the highest traffic during the weekdays. 
<p align="center">
  <img src="https://github.com/hyojunada/chicago_cta/blob/master/result/highest_station_ridership_W.png">
</p>

From this simple scatter plot, we find that Clark/Lake and Lake/State stations have the highest ridership as well as steady growth in the ridership compared to the other three stations. Moreover, these two stations are close together, with only two and a half blocks apart. A fast take-out deli/coffee shop between these two stations would be ideal.

<p align="center">
  <img src="https://github.com/hyojunada/chicago_cta/blob/master/result/google_map.png">
</p>
Outline of zip code 60601 is drawn in pink in the figure.

(for more detailed step-by-step analysis, please checkout this [notebook](https://nbviewer.jupyter.org/github/hyojunada/chicago_cta/blob/master/notebook/Project-Traffic.ipynb))

### Business near the highest traffic stations

Since we have approximate locations (between Clark/Lake and Lake/State stations), we want to estimate whether the location is saturated with similar businesses or the existing businesses can bring synergy (if there are a lot of non-competing businesses in the area, the people who work there can be our potential customers). 

I first look at the current businesses that can be potential competitors. The below figure shows all the business licenses issued for retailers that sell perishable food (e.g. Subway, Starbucks) since 2016 without duplicates for multiple licenses issued for the same store. 

<p align="center">
  <img src="https://github.com/hyojunada/chicago_cta/blob/master/result/number_of_food_retailor.png">
</p>

The zip code for the two stations is 60601, and the number of perishable food stores is ranked at 33rd compared to other zip codes in Chicago. Compared to the foot traffic population, there are not as much perishable food retailers to other zip codes, and it is safe to assume that competitors are not at threatening numbers in this zip code.

(for more detailed step-by-step analysis, please checkout this [notebook](https://nbviewer.jupyter.org/github/hyojunada/chicago_cta/blob/master/notebook/Project-business.ipynb))

## Next Steps
### Data collection and analysis

-**Bus traffic**
Use the data from Chicago CTA for bus traffic, have a more concrete estimation of foot traffic in each area

-**Real-estate**
Use the data from Zillow to estimate the rent price for the store. Also, we need to acquire more accurate data regarding the retail shops instead of projecting the estimate of household rents. 
### Build a predictive model

-**Variable cost analysis**
Variable costs like raw materials and labor are essential to calculate the costs. 

-**Price adjustment**
Above analysis will enable us to estimate the appropriate prices for the products that are sold at the store. 

-**Predictive model for estimating profit and recommendation of the ideal location**
After elementary analysis reveals an underlying trend that prompts further exploration we will build a predictive model for a recommendation of the location for stores. For my project, I propose to expand these efforts by building a model that takes advantage of four different data sets. The model will allow small business owners to be able to evaluate the potential success of the store and this can be expanded to other business other than deli/coffee shops.

**Profit function**

<a href="https://www.codecogs.com/eqnedit.php?latex=Profit&space;(P)&space;=&space;Revenu(R)&space;-&space;Cost(C)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Profit&space;(P)&space;=&space;Revenu(R)&space;-&space;Cost(C)" title="Profit (P) = Revenu(R) - Cost(C)" /></a>

**Revenue function**

<a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;\sum&space;_{items}Customers(N_{items})&space;*&space;price(item)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R&space;=&space;\sum&space;_{item}Customers(N_{item})&space;*&space;price(item)" title="R = \sum _{item}Customers(N_{item}) * price(item)" /></a>

Here, the total number of customers is the sum of the customers who bought each item. 

<a href="https://www.codecogs.com/eqnedit.php?latex=N_{total}&space;&=\sum_{item}Customers(N_{item})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?N_{total}&space;&=\sum_{item}Customers(N_{item})" title="N_{total} &=\sum_{item}Customers(N_{item})" /></a>

For simplicity, we can use the average price of the items that are sold at the store multiplied by the total number of customers to substitute the revenue function. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;R&space;&=\sum_{item}Customers(N_{item})*price(x_{item})&space;&=N_{total}&space;*&space;price_{average}&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;R&space;&=\sum_{item}Customers(N_{item})*price(x_{item})&space;&=N_{total}&space;*&space;price_{average}&space;\end{align*}" title="\begin{align*} R &=\sum_{item}Customers(N_{item})*price(x_{item}) &=N_{total} * price_{average} \end{align*}" /></a>

**Cost function**

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{aligned}&space;C&space;&=&space;fixed\&space;costs&space;&plus;&space;variable\&space;costs&space;\\&space;&=&space;(rent&space;&plus;&space;labor&space;&plus;&space;etc)&space;&plus;&space;(\sum_{items}N_{items}&space;*&space;cost(raw\&space;materials)_{item})&space;\end{aligned}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{aligned}&space;C&space;&=&space;fixed\&space;costs&space;&plus;&space;variable\&space;costs&space;\\&space;&=&space;(rent&space;&plus;&space;labor&space;&plus;&space;etc)&space;&plus;&space;(\sum_{items}N_{items}&space;*&space;cost(raw\&space;materials)_{item})&space;\end{aligned}" title="\begin{aligned} C &= fixed\ costs + variable\ costs \\ &= (rent + labor + etc) + (\sum_{items}N_{items} * cost(raw\ materials)_{item}) \end{aligned}" /></a>

Similar to revenue, we can substitute the cost of individual items with the average of the entire inventory. Thus, the cost function will be simplified to:

<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;fixed\&space;costs&space;&plus;&space;N_{total}*cost_{average}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;fixed\&space;costs&space;&plus;&space;N_{total}*cost_{average}" title="C = fixed\ costs + N_{total}*cost_{average}" /></a>

In our predictive model, one of the most important steps is estimating the number of customers. To do so, I suggest using a multi-layer network, where each layer would account for CTA 'L' network, CTA bus route network and residence network. Using networks we can have a robust estimation of potential customers how neighboring nodes and different layers affect each other.


Next step is estimating the cost of making each item. The owner of the business has to provide us with this information. However, we can further simplify the problem by having a comparative goal, such as the cost of an individual item should be less than a certain percentage of the price. 

<a href="https://www.codecogs.com/eqnedit.php?latex=cost&space;\leq&space;p*price(x_{item})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?cost&space;\leq&space;p*price(x_{item})" title="cost \leq p*price(x_{item})" /></a>

Then the profit equation further reduces to 

<a href="https://www.codecogs.com/eqnedit.php?latex=P&space;\geq&space;(1-p)*price_{average}*N_{total}&space;-&space;fixed\&space;costs" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P&space;\geq&space;(1-p)*price_{average}*N_{total}&space;-&space;fixed\&space;costs" title="P \geq (1-p)*price_{average}*N_{total} - fixed\ costs" /></a>

Which leaves us with the fixed costs, which by large part is the rent. The rent is determined by the location and square footage, which I believe would be solvable with available real-estate data. To predict the cost of renting, we can use simple regression models, or k-nearest predictor by using neighboring listings for function ***f*** 

<a href="https://www.codecogs.com/eqnedit.php?latex=rent&space;=&space;f(location,&space;ft^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?rent&space;=&space;f(location,&space;ft^2)" title="rent = f(location, ft^2)" /></a>

And now we will have all the information to build a simple predictive model that can robustly estimate the price and profit for each location for different businesses. 
