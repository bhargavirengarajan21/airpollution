import numpy as np
import xgboost as xgb
import pandas as pd
from webscraper import scrapWeb
from flask import Flask, request, jsonify, render_template
import pickle
import emoji


application = Flask(__name__) #Initialize the flask App
model1 = pickle.load(open('csamodel1.pkl', 'rb'))
model2 = pickle.load(open('rmmodel.pkl', 'rb'))
model3 = pickle.load(open('xgbmodel.pkl', 'rb'))

def checkValue(value):
   if value < 50:
      return emoji.emojize(':grinning_face:')
   if value < 100:
      return emoji.emojize(':slightly_smiling_face:')
   if value < 150:
      return emoji.emojize(':neutral_face:')
   if value < 200:
      return emoji.emojize(':worried_face:')
   if value < 250:
      return emoji.emojize(':fearful_face:')
   if value < 300:
      return emoji.emojize(':hot_face:')
   return emoji.emojize(':face_with_medical_mask:')

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    air_cols = ['Date','BP (mmHg)', 'AT ()', 'RH (%)', 'WD','PM2.5 (ug/m3)','NO (ug/m3)','NO2 (ug/m3)','NH3 (ug/m3)','SO2 (ug/m3)','CO (mg/m3)','Ozone (ug/m3)']
    data = scrapWeb(request.form.get('street'))
    airData= pd.DataFrame([[data[x] for x in air_cols]], columns=air_cols, dtype="float")
    airData['Date'] = pd.to_datetime(airData['Date'])
    airData['Date'] = airData['Date'].astype(int)
    print(model1.predict(xgb.DMatrix(data=airData))[0])
    predict1 = round(model1.predict(xgb.DMatrix(data=airData))[0])
    predict2 = round(model2.predict(airData)[0])
    predict3 = round(model3.predict(airData)[0])
    output1 = checkValue(predict1)
    output2 = checkValue(predict2)
    output3 = checkValue(predict3)
    return render_template('index.html', prediction_text=' Air Pollution should be {}'.format([output1,predict1,output2,predict2,output3,predict3]))

if __name__ == "__main__":
    application.run(debug=True)
