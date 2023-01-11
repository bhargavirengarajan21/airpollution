import numpy as np
import xgboost as xgb
import pickle

def custom_asymmetric_train(predt, dtrain) :
    y_true = dtrain.get_label()
    residual = (y_true - predt).astype("float")
    grad = np.where(residual<0, -2*10.0*residual, -2*residual)
    hess = np.where(residual<0, 2*10.0, 2.0)
    return grad, hess
    
def custom_asymmetric_model(X_train,y_train,X_test,y_test):    
	dtrain = xgb.DMatrix(data=X_train,label=y_train)
	dtest=xgb.DMatrix(data=X_test, label=y_test)
	print(dtrain,dtest)
	model =xgb.train({ 'seed':20,'nfold':100,'booster':'gbtree','gamma':5,'colsample_bytree': 0.7,'learning_rate': 0.3,'max_depth':5,'num_round':10,'early_stopping_rounds':50,'random_state':10}, 
		   dtrain=dtrain,
		   num_boost_round=1000,
		   obj = custom_asymmetric_train) 
	pickle.dump(model, open('csamodel1.pkl','wb'))
	

