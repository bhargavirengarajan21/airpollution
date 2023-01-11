import pandas as pd
import numpy as np
from sklearn import metrics
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import pyplot
from matplotlib.dates import DateFormatter
import numpy as np
from sklearn.impute import KNNImputer
import xgboost as xgb
from sklearn.metrics import accuracy_score,mean_squared_error
import numpy as np
from sklearn.model_selection import train_test_split
from randomForrest import randomForest_train
from xgboostmodel import xgboostModel
from customAnalysis import custom_asymmetric_model


data = pd.read_csv('delhi_imputed.csv')



air_cols = ['Date','BP (mmHg)', 'AT ()', 'RH (%)', 'WD','PM10 (ug/m3)','PM2.5 (ug/m3)','NO (ug/m3)','NO2 (ug/m3)','NH3 (ug/m3)','SO2 (ug/m3)','CO (mg/m3)','Ozone (ug/m3)']
data_cols = ['BP (mmHg)', 'AT ()', 'RH (%)', 'WD','PM10 (ug/m3)','PM2.5 (ug/m3)','NO (ug/m3)','NO2 (ug/m3)','NH3 (ug/m3)','SO2 (ug/m3)','CO (mg/m3)','Ozone (ug/m3)']
result_df= data[air_cols]
impute_df = data[data_cols]
imputer = KNNImputer(n_neighbors=2, weights="uniform")
data_filled = imputer.fit_transform(impute_df)
data_filled_df = pd.DataFrame(data_filled, columns=data_cols)
data_filled_df['Date']= data['Date']
data['PM10 (ug/m3)'].fillna(187.14 ,inplace=True)
data_filled_df[data_cols]

data_cols1= ['Date','BP (mmHg)', 'AT ()', 'RH (%)', 'WD','PM2.5 (ug/m3)','NO (ug/m3)','NO2 (ug/m3)','NH3 (ug/m3)','SO2 (ug/m3)','CO (mg/m3)','Ozone (ug/m3)']
air_cols= ['BP (mmHg)', 'AT ()', 'RH (%)', 'WD','PM2.5 (ug/m3)','NO (ug/m3)','NO2 (ug/m3)','NH3 (ug/m3)','SO2 (ug/m3)','CO (mg/m3)','Ozone (ug/m3)']
x1=data_filled_df[data_cols1]

x1['Date']= pd.to_datetime(x1['Date'])
x1['Date']=x1['Date'].astype(int)
print(x1['Date'])
y1=data_filled_df[['PM10 (ug/m3)']]
# print(x1['Date'])


X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.2, random_state=123)

randomForest_train(X_train,y_train,X_test,y_test)
xgboostModel(X_train,y_train,X_test,y_test)
custom_asymmetric_model(X_train,y_train,X_test,y_test)



