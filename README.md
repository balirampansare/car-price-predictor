# Car Price Predictor
1. Car Price Predictor takes the parameters of an used car: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
2. It then predicts the possible price of the car with the help of linear regression.
 
Below image shows the graphical user interface (GUI) of the Car Price Predictor

![GUI of Car Price Predictor](static/images/gui.PNG)

The predicted price for the car Ford Endeavor 4x4 is shown below

![Predicted Car Price](static/images/predictedprice.PNG)

# The flow of the Car Price Predictor

1. The data file was scraped from the (https://quikr.com)

Link: [quikr_car Dataset](https://github.com/balirampansare/car-price-prediction/blob/main/quikr_car.csv)

2. The data was cleaned and analysed.

Link: [Cleaned Dataset](https://github.com/balirampansare/car-price-prediction/blob/main/cleaned_car.csv)

3. Then a Linear Regression model was built on top of it which had 0.88 R2_score.

Link: [Car Price Predictor](https://github.com/balirampansare/car-price-prediction/blob/main/Car%20Price%20Predictor.ipynb)

4. With the help of flask and we created the websiste where we used the Linear Regression model to perform predictions.
    1. Flask File: [application](https://github.com/balirampansare/car-price-prediction/blob/main/application.py)
    2. HTML File: [index]s(https://github.com/balirampansare/car-price-prediction/blob/main/templates/index.html)
