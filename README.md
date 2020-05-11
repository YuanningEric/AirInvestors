## Description
AirInvestors is a web-based decision support system that helps property investors interactively make decisions with Airbnb investment. Users can get accessed to property information, filter properties based on different attributes (e.g. year, list price, location, neighborhood etc.). AirInvestors also integrates a variety of machine learning models (such as NLP on property descriptions) to predict property rental price income.

## Demo
* Main page
<img src="https://github.com/YuanningEric/AirInvestors/blob/master/GIFs/Mainpage.gif" height = "350" width = "600"/>

* Predicted rental price
<img src="https://github.com/YuanningEric/AirInvestors/blob/master/GIFs/Predicted_rental_price.gif" height = "400" width = "600"/>

* Heat maps
<img src="https://github.com/YuanningEric/AirInvestors/blob/master/GIFs/Heatmaps.png" height = "400" width = "600"/>

## Product
We offer both online and local accesses to our product.

1. **Online access**
To use AirInvestors, you can go to
[https://online.tableau.com/] (https://online.tableau.com/)
**Username**: airinvestors.demo1@gmail.com          
**Password**: cse6242!

2. **Local access**
Install [Tableau Desktop] (https://www.tableau.com/products/desktop) on your computer.
Download *AirInvestors 20200419.twbx* from ./Tableau/ in this directory.


## Modules
The project consists of the following functional units:
1. Data collection and scraping: We collected Airbnb rental information from Inside Airbnb, information of properties on sale from Mashvisor API, census information from Census Bureau, and crime data from data.austintexas.gov.
2. Data cleaning and integration: We combined the census, crime data with Airbnb and Mashvisor data by zip code. All data cleaning procedures were done with R language.
3. Data analytics and prediction: We used a linear model with cross validation to analyze and predict the data.
4. Rental price predictions using NLP: We used the BERT (Bidirectional Encoder Representations from Transformers) to predict future rental price income based on house text description.
5. Visualization UI: We summarized all of the data and analyzed it through Tableau.


## Directory

* Data_Preprocessing
Merge_Mashvisor_InsiderAirbnb.R preprocesses the data from Mashvisor and InsiderAirbnb.

* Econometrics_Model
Predictive_ Model.R established an OLS model to predict the listing prices of properties in Airbnb,

* NLP
Contains codes that use house description to predict rental price income. See sections below.


## Installation
Downloading Mashvisor data:
* curl --location --request GET "https://api.mashvisor.com/v1.1/client/property?id=[YOUR_QUERYED_ID]&state=TX" --header "x-api-key: [YOUR_API_KEY]

Downloading Airbnb data:
* wget http://data.insideairbnb.com/united-states/tx/austin/2020-03-17/data/listings.csv.gz
Convert json file to csv:
* json2csv -i INPUT_JSON --flatten-objects  -v '.' --flatten-separator "_" --flatten-arrays
Merge Mashvisor and Airbnb dataset with R script:
* Rscript Merge_Mashvisor_InsiderAirbnb.R
(Feel free to see and download our data and code on  https://github.com/CancerGenome/CSE6242_GroupProject)

Predictive models for rental price and listing price:
* Rscript Predictive_ Model.R

## Rental price prediction using NLP:
* Run data_preprocessing_Airbnb.ipynb. This file is used to preprocess the training and evaluation data from Inside Airbnb, it generates preprocessed train and evaluation data for both classification and regression tasks.
* Run data_preprocessing_Mashvisor.ipynb. This file is used to preprocess the prediction data from Mashvisor.
* Run BERT_AIRBNB_cla.ipynb. This file is used to train and evaluate the BERT model for classification tasks and use the trained model to predict labeled price.  Running the file will output the fine-tuned model, evaluation results and prediction dataset. Users can specify a variety of hyperparameters for training the model, such as learning rate, number of training epoch and batch size.
* Run BERT_AIRBNB_reg.ipynb. This file is used to train and evaluate the BERT model for regression tasks and use the trained model to predict rental price.  Running the file will output the fine-tuned model, evaluation results and prediction dataset. Users can specify a variety of hyperparameters for training the model, such as learning rate, number of training epoch and batch size.
* Run word_cloud_visulization.ipynb. This file is used to preprocess the data for word cloud visualization. Running the file will output a list of word tokens.

## Running Tableau online:
1. The default landing page after login is the "Main Page" of AirInvestors, where users can select properties for most visualizations which use the same data source.
2. Users can use the search box, multiple filters or make selections on the map view to choose properties.
3. A tooltip will appear to show the detailed information of the property when hovering the mouse on top of a property on map.
4. Users can also select the properties on map or chart in any dashboard. The remaining visualizations in the same dashboard will synchronize with the same property selection.
5. Click the tab name on top of the webpage to switch to different dashboard and visualization.
