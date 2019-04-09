# Prediction of Energy Consumption

More information about the dataset is provided in the [UCI] repository and inside the jupyter notebook.

## Installation instructions
You have to install all the dependencies given in the **requirements.txt** file.

## Description

We use a variety of regression models to predict appliances consumption:

- Time Series (ARIMA) by using prophet library or scipy
- Linear Regression
- Support Vector Regression
- Random Forests
- XGBoost

## Deployment
The features that we used to predict energy consumption are the following:
* lights 
* RH_1
* RH_2
* T3 
* RH_3 
* T4
* T5
* RH_5
* RH_7
* T8
* RH_8
* RH_9
* T_out
* Press_mm_hg
* Windspeed
* Visibility
* Tdewpoint
* RH_out
* HI_1 (_Heat index: indicator which combines temperature and humidity_)

All features should be in a float format.

So,
for deploying this project you have to run the jupyter notebook **energy_prediction.ipynb**.

A .joblib file with name **load_forecasting_model_v010.joblib** is created in your environment.

After, just run in python or conda cell the below command:
```sh
python load_forecasting_web.py
```
After, open a new window in your browser and hit the link below with the endpoint provided with appropriate parameters.

http://127.0.0.1:9181/forecast?lights=-0.48035045386630404&RH_1=-0.946158466456135&RH_2=-1.4181979731110357&T3=2.458011612346191&RH_3=-0.5619405224513885&T4=0.9950453915906787&T5=0.6500783807977281&RH_5=-1.0030067622142276&RH_7=-0.9527938176980463&T8=0.6468936400268821&RH_8=-0.8174884778574232&RH_9=-0.9216520453837769&T_out=1.096153746249714&Press_mm_hg=0.27508014832402766&Windspeed=0.7147229546896305&Visibility=0.1412477328356142&Tdewpoint=0.24231369769579522&RH_out=-1.5504519649069635&HI_1=-1.2051606567664048

**_Please note that inserting unscaled features can be misleading_**.

You now have the prediction in your screen!


[UCI]: <https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction>
