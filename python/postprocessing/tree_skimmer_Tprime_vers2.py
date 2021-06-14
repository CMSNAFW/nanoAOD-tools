#!/bin/env python3
import os
##print(os.environ)
##print("**********************************************************************")
##print("**********************************************************************")
##print("**********************************************************************")
##print(str(os.environ.get('PYTHONPATH')))
##print(str(os.environ.get('PYTHON3PATH')))
import sys
##print("*************** This is system version info ***************************")
##print(sys.version_info)
#import platform
##print("*************** This is python version info ***************************")
##print(platform.python_version())
import ROOT
##print("Succesfully imported ROOT")
import math
import datetime
import copy
from array import array
from skimtree_utils import *
import xgboost as xgb
import numpy as np
from training import *

if sys.argv[4] == 'remote':
    from samples import *
    Debug = False
else:
    from samples.samples import *
    Debug = True

if sys.argv[5] == None: training = training_dict["BDT_Tprime"]
else: training = training_dict[sys.argv[5]]

sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))

MCReco = True
DeltaFilter = True
bjetSwitch = False # True #
startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

#leadingjet_ptcut = 150.

chain = ROOT.TChain('Events')

for infile in file_list: 
    print("Adding %s to the chain" %(infile))
    chain.Add(infile)
print("Number of events in chain " + str(chain.GetEntries()))
print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
tree = InputTree(chain)
isMC = True
scenarios = ["nominal", "jesUp", "jesDown", "jerUp", "jerDown"] 
if ('Data' in sample.label):
    isMC = False
    scenarios = ["nominal"]
MCReco = MCReco * isMC

#++++++++++++++++++++++++++++++++++
#++   branching the new trees    ++
#++++++++++++++++++++++++++++++++++
outTreeFile = ROOT.TFile(sample.label+"_part"+str(part_idx)+".root", "RECREATE") # output file
trees = []
for i in range(10):
    trees.append(None)
#systZero = systWeights()
# defining the operations to be done with the systWeights class
maxSysts = 0
addPDF = True
addQ2 = False
addTopPt = False
addVHF = False
addTTSplit = False
addTopTagging = False
addWTagging = False
addTrigSF = False
nPDF = 0

systTree = systWeights()
systTree.prepareDefault(True, addQ2, addPDF, addTopPt, addVHF, addTTSplit)

for scenario in scenarios:
    systTree.addSelection(scenario)

systTree.initTreesSysts(trees, outTreeFile)

def reco(scenario, isMC, addPDF, training):
    isNominal = False
    if scenario == 'nominal':
        isNominal = True
    print(scenario)


    Top_pt1_nominal = array.array('f',[0.]) 
    Top_eta1_nominal = array.array('f',[0.]) 
    Top_phi1_nominal = array.array('f',[0.]) 
    Top_M1_nominal = array.array('f',[0.]) 
    Top_Score1_nominal = array.array('f',[0.]) 

    Top_pt2_nominal = array.array('f',[0.]) 
    Top_eta2_nominal = array.array('f',[0.]) 
    Top_phi2_nominal = array.array('f',[0.]) 
    Top_M2_nominal = array.array('f',[0.]) 
    Top_Score2_nominal = array.array('f',[0.]) 

    Top_pt3_nominal = array.array('f',[0.]) 
    Top_eta3_nominal = array.array('f',[0.]) 
    Top_phi3_nominal = array.array('f',[0.]) 
    Top_M3_nominal = array.array('f',[0.]) 
    Top_Score3_nominal = array.array('f',[0.]) 

    systTree.branchTreesSysts(trees, scenario,"Top_pt1_nominal",outTreeFile,Top_pt1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta1_nominal",outTreeFile,Top_eta1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi1_nominal",outTreeFile,Top_phi1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M1_nominal",outTreeFile,Top_M1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score1_nominal",outTreeFile,Top_Score1_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt2_nominal",outTreeFile,Top_pt2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta2_nominal",outTreeFile,Top_eta2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi2_nominal",outTreeFile,Top_phi2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M2_nominal",outTreeFile,Top_M2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score2_nominal",outTreeFile,Top_Score2_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt3_nominal",outTreeFile,Top_pt3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta3_nominal",outTreeFile,Top_eta3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi3_nominal",outTreeFile,Top_phi3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M3_nominal",outTreeFile,Top_M3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score3_nominal",outTreeFile,Top_Score3_nominal)

    for i in range(tree.GetEntries()):
        event = Event(tree,i)    
        jets = Collection(event, "Jet")             # jets[j1].btagDeepFlavB  ---> medium discriminant cut = 0.2783
        tops = Collection(event,"Top")
        met = Object(event, "MET")
        electron = Collection(event, "Electron")
        muon = Collection(event, "Muon")
        nelectron = len(electron)
        nmuon = len(muon)
        ntop = len (tops)
        
 
        all_coll=[]

        for train in training:
            new_coll=[]
            score=[]
            score_=-999
            clf = xgb.XGBClassifier()
            clf.load_model(train.files)
            if train.lepton == 1:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.cuts[0]) and (x.nu_pt<train.cuts[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.el_index != -1)
                                                ,tops))
                is_el=True
            else:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.cuts[0]) and (x.nu_pt<train.cuts[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.mu_index != -1)
                                                ,tops))
                is_el=False


            for top in good_top:
                lista=[]
                score_=-999
                for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                if is_el:
                    for el in train.var_lep:
                        if(el=='dxyerr') or (el=='dzerr'): lista.append(0.1)
                        else:lista.append(electron[int(top.el_index)][el])
                else:
                    for mu in train.var_lep: lista.append(muon[int(top.mu_index)][el])
                for t in train.var_top:
                    if (t== 'mT'): lista.append(0)
                    elif (t== 'electron_over_jet'): lista.append(electron[int(top.el_index)].pt/jets[int(top.bjet_index)].pt)
                    else: lista.append(top[t]) 
                    X= np.array([lista,])
  
                score_ = clf.predict_proba(X)[0, 1]
                
                score.append(score_)
                new_coll.append([top,score_])
            if(len(new_coll)>0): 
                new_coll =  [x for _,x in sorted(zip([new_coll[i][-1] for i in range(len(score))],new_coll))]
                new_coll.reverse()
            all_coll = all_coll + new_coll
            


        if(len(all_coll)==0): continue

        Top_pt1_nominal[0] = all_coll[0][0].nu_pt 
        Top_eta1_nominal[0] = all_coll[0][0].nu_eta 
        Top_phi1_nominal[0] = all_coll[0][0].nu_phi 
        Top_M1_nominal[0] = all_coll[0][0].nu_M 
        Top_Score1_nominal[0] = all_coll[0][1]

        if(len(all_coll)>1):
            Top_pt2_nominal[0] = all_coll[1][0].nu_pt 
            Top_eta2_nominal[0] = all_coll[1][0].nu_eta 
            Top_phi2_nominal[0] = all_coll[1][0].nu_phi 
            Top_M2_nominal[0] = all_coll[1][0].nu_M 
            Top_Score2_nominal[0] = all_coll[1][1]

        else:
            Top_pt2_nominal[0] = -999 
            Top_eta2_nominal[0] = -999 
            Top_phi2_nominal[0] = -999 
            Top_M2_nominal[0] = -999 
            Top_Score2_nominal[0] = -999

            Top_pt3_nominal[0] = -999 
            Top_eta3_nominal[0] = -999 
            Top_phi3_nominal[0] = -999 
            Top_M3_nominal[0] = -999 
            Top_Score3_nominal[0] = -999

        if(len(all_coll)>2):
            Top_pt3_nominal[0] = all_coll[2][0].nu_pt 
            Top_eta3_nominal[0] = all_coll[2][0].nu_eta 
            Top_phi3_nominal[0] = all_coll[2][0].nu_phi 
            Top_M3_nominal[0] = all_coll[2][0].nu_M 
            Top_Score3_nominal[0] = all_coll[2][1]

        else:
            Top_pt3_nominal[0] = -999 
            Top_eta3_nominal[0] = -999 
            Top_phi3_nominal[0] = -999 
            Top_M3_nominal[0] = -999 
            Top_Score3_nominal[0] = -999



        systTree.fillTreesSysts(trees, scenario)

 
    systTree.writeTreesSysts(trees, outTreeFile)


reco("nominal",isMC,addPDF, training)


endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
