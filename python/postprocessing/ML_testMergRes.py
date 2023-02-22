import ROOT
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams['figure.figsize'] = (14, 7)
import seaborn as sns
import root_pandas
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, f1_score, confusion_matrix, auc, roc_curve
#from sklearn.metrics import ConfusionMatrixDisplay   
from funzioni import compare_train_test,  compare_train_test_background_category, classreport, label


params= {
    'n_estimators': 130,
    'learning_rate': 0.1,
    'max_depth' : 4,
    'min_child_weight': 4,
    'reg_alpha' : .01,
    'objective' : 'multi:softprob',
    'num_class' : 4,
    'n_gpus': 0
    }
variables = [
		'mergres_fatjet_pt',
		'mergres_fatjet_eta',
		'mergres_fatjet_phi',
		'mergres_fatjet_mass',
		'mergres_fatjet_deeptagTvsQCD', 
		'mergres_fjet_pt',
		'mergres_fjet_eta',
		'mergres_fjet_phi',
		'mergres_fjet_mass',
		'mergres_sjet_pt',
		'mergres_sjet_eta',
		'mergres_sjet_phi',
		'mergres_sjet_mass',
		'mergres_tjet_pt',
		'mergres_tjet_eta',
		'mergres_tjet_phi',
		'mergres_tjet_mass',
		'mergres_top_pt',
		'mergres_top_eta',
		'mergres_top_phi',
		'mergres_top_mass',
		'mergres_jet_bestbtag',
		'mergres_deltaR'
		]

input_path = '/eos/user/a/acagnott/Tprime/ToTZ'
file_name = '/TprimeToTZ_2017/TprimeToTZ_2017.root'

n_classes = 4

data = root_pandas.read_root(input_path+file_name, "tree_mergres")
X = data[variables]
y = data['mergres_true']

new_data_bg = (data.query("mergres_true==0")).sample(n=(len(data.query("mergres_true==2"))))
new_data_merg = (data.query("mergres_true==1")).sample(n=(len(data.query("mergres_true==2"))))
new_data_sgn = data.query("mergres_true>1")
df = [ new_data_bg,new_data_merg, new_data_sgn]
df_new = pd.concat(df)


X_train, X_test = train_test_split(df_new, test_size = 0.3)
X_train_all_variables, X_test_all_variables = X_train, X_test
X_train, X_test = X_train_all_variables[variables].values, X_test_all_variables[variables].values
y_train, y_test = X_train_all_variables['mergres_true'].values, X_test_all_variables['mergres_true'].values

dtrain = xgb.DMatrix(data=X_train, label=y_train, feature_names=variables)
dtest = xgb.DMatrix(data=X_test, label=y_test, feature_names= variables)


clf = xgb.train(params, dtrain)
clf.save_model("ML_model/testmergres.json")

#clf = xgb.Booster()
#clf.load_model("ML_model/testmergres.json")

y_pred = clf.predict(dtest)

y_pred_label = np.zeros(len(X_test))
for i in range(len(y_pred)):
	val = max(y_pred[i].ravel())
	for j in range(n_classes):
		if y_pred[i][j]== val : y_pred_label[i] = j

rep = classification_report(y_test, y_pred_label)
print(rep)

cm = confusion_matrix(y_test, y_pred_label)
print(' confusion matrix', cm)

clf.feature_names = variables
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
importance_plot = xgb.plot_importance(clf, ax=ax)
ax.set_title('Importance Plot')
importance_plot.figure.savefig('importplot_mergres.png', format='png')

