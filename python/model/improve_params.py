#!/home/cmsuser/cmssw/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_9/external/slc6_amd64_gcc630/bin/python
# coding: utf-8


import ROOT
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
#import matplotlib.pyplot as plt
#plt.rcParams.update({'figure.max_open_warning': 0})
#plt.rcParams['figure.figsize'] = (14, 7)
import root_pandas
from sklearn.model_selection import train_test_split, GridSearchCV
import xgboost as xgb
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, f1_score, confusion_matrix, auc, roc_curve,mean_squared_error
from ML_config import fetch_configuration, pre_cut_el, pre_cut_mu, file_dir, fetch_file_list
import os
import json


class XGBoostRegressor():
    def __init__(self, num_boost_round=900,feature_names=None, **params):
        self.clf = None
        self.feature_names=feature_names
        self.num_boost_round = num_boost_round
        self.params = params
        
        
 
    def fit(self, X, y,**fit_params):
        num_boost_round = self.num_boost_round
        dtrain = xgb.DMatrix(data=X, label=y,feature_names=self.feature_names)
        self.clf = xgb.train(params=self.params, dtrain=dtrain,num_boost_round=num_boost_round,**fit_params)#, early_stopping_rounds=10, evals_result=self.evals_result,evals=watchlist)
 
    def predict(self, X):
        dtest = xgb.DMatrix(X,feature_names=self.feature_names)
        return self.clf.predict(dtest)
 
    def get_params(self, deep=True):
        return self.params
        
    def score(self, X, y):
        Y = self.predict(X)
        y_pred_label = np.zeros(len(X))
        for i in range(len(y)):
            val = max(Y[i].ravel())
            for j in range(3):
                if Y[i][j]== val : y_pred_label[i] = j
        return 1./np.sqrt(mean_squared_error(y, y_pred_label))
 
    def set_params(self, **params):
        if 'num_boost_round' in params:
            self.num_boost_round = params.pop('num_boost_round')
        if 'objective' in params:
            del params['objective']
        self.params.update(params)
        return self



def find_iperparams(config, config_dict, file_name, tree_name):
    
    n_estimators = [50,100,150]#np.arange(10,100,20)# [100,150,200]
    learning_rate = [.05]
    max_depth = [3]
    min_child_weight = [1,3]
    reg_alpha = [.1]
    min_split_loss=[0.1]
    

    

    hyperparameters = {
                       'n_estimators' : n_estimators,
                       'learning_rate': learning_rate,
                       'max_depth' : max_depth,
                       'min_child_weight' : min_child_weight,
                       'reg_alpha' : reg_alpha,
                       'objective' : ['multi:softmax'],
                       'num_class' :[3],
                       'n_gpus': [0],
                       'eval_metric':['mlogloss'],
                       'min_split_loss':min_split_loss    
                       }
    	
    data = pd.DataFrame()
    data_orig = pd.DataFrame()
    data = data.append(root_pandas.read_root(file_name, tree_name), ignore_index=True)
    data_orig = data_orig.append(root_pandas.read_root(file_name, tree_name), ignore_index=True)

    #Pt selection
    data = data.query(config_dict['bin'])
    data_orig = data_orig.query(config_dict['bin'])



    # preselection (maybe already done in unpacking module on Crab/ postprocessor)
    if(tree_name[:2]=='el'):
        data = data.query(pre_cut_el())
    if(tree_name[:2]=='mu'):
        data = data.query(pre_cut_mu())



    truth = 'Top_High_Truth'

    # Train and test creation
    X_train, X_test = train_test_split(data, test_size=0.3)

    X_train_all_variables, X_test_all_variables = X_train.query(config_dict['preselection_'+tree_name[:2]]), X_test.query(config_dict['preselection_'+tree_name[:2]])
    y_train, y_test = X_train_all_variables[truth], X_test_all_variables[truth]

    X_train, X_test = X_train_all_variables[config_dict['variables_'+tree_name]].values, X_test_all_variables[config_dict['variables_'+tree_name]].values

    #remapping 

    map_dict={0:2,1:0,2:1,3:1,4:1,5:1}
    y_train.replace(map_dict,inplace=True)
    y_test.replace(map_dict,inplace=True)
    y_train, y_test = y_train.values, y_test.values
    print(y_train)

    
    dtest = xgb.DMatrix(data=X_test, label=y_test)#,feature_names=config_dict['variables_'+tree_name])
    #training
    regressor=XGBoostRegressor(feature_names=config_dict['variables_'+tree_name])
    
    fit_params={"early_stopping_rounds":10,
                #"eval_metric":"mlogloss",
                "evals":[(dtest,"validation_1")],
                #"evals_result":dict()
    }


    #regressor.fit(X_train,y_train)
    grid = GridSearchCV(estimator=regressor, param_grid=hyperparameters, n_jobs=1, scoring="precision_weighted")
    print("beginning",len(X_train),len(y_train),config_dict['variables_'+tree_name])
    grid.fit(X_train, y_train,**fit_params)
    par=grid.best_params_

    with open(tree_name+"_"+config+".txt", 'w') as file:
        file.write(json.dumps(par))
        #file.write("done")


if __name__ == "__main__":
    config_dic = fetch_configuration()
    #config = "high_pt"
    file= "/eos/home-f/fcarneva/Tprime/nosynch/toTraining.root"
    for config in config_dic:
        if config_dic[config]['Electrons']:
            if config_dic[config]['enable_merged']:
                find_iperparams(config, config_dic[config], file, 'el_merged')
            if config_dic[config]['enable_resolved']:
                find_iperparams(config, config_dic[config], file, 'el_resolved')

        if config_dic[config]['Muons']:
            if config_dic[config]['enable_merged']:
                find_iperparams(config, config_dic[config], file, 'mu_merged')
            if config_dic[config]['enable_resolved']:
                find_iperparams(config, config_dic[config], file, 'mu_resolved')
