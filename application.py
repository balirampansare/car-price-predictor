from flask import Flask,render_template,request,redirect
import pickle
import pandas as pd
import numpy as np

#creating object/constructor of flask where we pass __name__ as argument
app=Flask(__name__)
model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv('cleaned_car.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()

    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type)


@app.route('/predict',methods=['POST'])
def predict():
    """ what ever data is filled in form, extracting that data """
    company = request.form.get('company') #here company means the name we had entered in the form, similar to below code
    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')

    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))

    return str(np.round(prediction[0],2))
    
if __name__=='__main__':
    app.run()