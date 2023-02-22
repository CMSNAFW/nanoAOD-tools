#!/home/cmsuser/cmssw/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_9/external/slc6_amd64_gcc630/bin/python
# coding: utf-8


import ROOT
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams['figure.figsize'] = (14, 7)
import root_pandas
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, f1_score, confusion_matrix, auc, roc_curve
from ML_config import fetch_configuration, pre_cut_el, pre_cut_mu, file_dir, fetch_file_list
import os
import json

"""
params= {
    'n_estimators': 150,
    'learning_rate': 0.1,
    'max_depth' : 8,
    #'min_child_weight': 2,
    #'reg_alpha' : .1,
    'objective' : 'multi:softprob',
    'num_class' : 3,
    'n_gpus': 0,
    #'early_stopping_rounds': 10,
    'eval_metric':'mlogloss'
    #'evals':["logloss"]
    }
"""
#u={"n_gpus": 0, "num_class": 3, "learning_rate": 0.15, "reg_alpha": 0.1, "min_child_weight": 5, "n_estimators": 50, "early_stopping_rounds": 15, "objective": "multi:softmax", "num_boost_round": 300, "max_depth": 10}

def boosted_decision_top_tagging(config, config_dict, file_name, tree_name):

	
    data = pd.DataFrame()
    data_orig = pd.DataFrame()
    data = data.append(root_pandas.read_root(file_name, tree_name), ignore_index=True)
    data_orig = data_orig.append(root_pandas.read_root(file_name, tree_name), ignore_index=True)

    #Pt selection
    data = data.query(config_dict['bin'])
    data_orig = data_orig.query(config_dict['bin'])

    f = open(tree_name+"_"+config+".txt", "r")
    params =json.loads(f.readlines()[0])
    params["objective"]='multi:softprob'
    
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

    #training
    dtrain = xgb.DMatrix(data=X_train, label=y_train, feature_names=config_dict['variables_'+tree_name])
    dtest = xgb.DMatrix(data=X_test, label=y_test, feature_names= config_dict['variables_'+tree_name])
    params["eval_metrics"]="mlogloss"
    params['n_estimators']= 150
    print("Inizo allenamento")
    evals_result={}
    watchlist=[(dtrain,"validation_0"),(dtest,"validation_1")]
    clf = xgb.train(params, dtrain,num_boost_round=900,evals=watchlist,evals_result=evals_result,early_stopping_rounds= 10)

    y_pred = clf.predict(dtest)

    y_pred_label = np.zeros(len(X_test))
    print(len(y_pred),len(y_test))
    for i in range(len(y_pred)):
        val = max(y_pred[i].ravel())
        for j in range(3):
                if y_pred[i][j]== val : y_pred_label[i] = j


    clf.save_model('JSON_MultiClass/' + config +'_'+ tree_name +'.json')
    rep = classification_report(y_test, y_pred_label)
    print(rep)
    print(y_pred,y_test)
    result=pd.DataFrame(np.array(clf.predict(dtrain)), columns={"Score0","Score1","Score2"})
    result["Truth"]=np.array(y_train)
    result["Train"]=np.ones(len(y_train))
    #result.to_root('scores.root', 'train')

    result1=pd.DataFrame(np.array(y_pred), columns={"Score0","Score1","Score2"})
    result1["Truth"]=np.array(y_test)
    result1["Train"]=np.zeros(len(y_test))
    result=result.append(result1)
    result.to_root('scores_'+tree_name+'_'+config+'.root', 'scores')
    results = evals_result
    #print results
    xran = len(results['validation_0']['mlogloss'])
    print('Training: ',results['validation_0']['mlogloss'][xran-1],'   Testing: ',results['validation_1']['mlogloss'][xran-1],'   OVERTRAINING: ',round((results['validation_1']['mlogloss'][xran-1]-results['validation_0']['mlogloss'][xran-1])/results['validation_0']['mlogloss'][xran-1],3))

if __name__ == "__main__":
    config_dic = fetch_configuration()
    file= "/eos/home-f/fcarneva/Tprime/nosynch/toTraining_new.root"
    for config in config_dic:
        if config_dic[config]['Electrons']:
            if config_dic[config]['enable_merged']:
                boosted_decision_top_tagging(config, config_dic[config], file, 'el_merged')
            if config_dic[config]['enable_resolved']:
                boosted_decision_top_tagging(config, config_dic[config], file, 'el_resolved')

        if config_dic[config]['Muons']:
            if config_dic[config]['enable_merged']:
                boosted_decision_top_tagging(config, config_dic[config], file, 'mu_merged')
            if config_dic[config]['enable_resolved']:
                boosted_decision_top_tagging(config, config_dic[config], file, 'mu_resolved')
    
