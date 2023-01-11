import xgboost as xgb
import numpy as np
import pickle

def xgboostModel(X_train,y_train,X_test,y_test): 
	eval_set = [(X_test, y_test)]
	xg_reg = xgb.XGBRegressor(objective = 'reg:squarederror',num_round=100,early_stopping_rounds=50,nfold=500,colsample_bytree= 0.7
		                 ,random_state=12,silent=1,nthread=31  ,seed=200,learning_rate =0.1,max_depth =4,n_estimators=200,num_boost_round=10)
	xg_reg.fit(X_train,y_train,eval_metric="logloss",eval_set=eval_set)
	
	pickle.dump(xg_reg, open('xgbmodel.pkl','wb'))
