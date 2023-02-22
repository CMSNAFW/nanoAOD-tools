#!/bin/env python
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
print("ok \n")
import xgboost as xgb
import numpy as np
from training import *
from samples.samples import *

print("all import are ok \n")

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
outTreeFile = ROOT.TFile(str(sys.argv[4])+"/"+sample.label+"_part"+str(part_idx)+".root", "RECREATE") # output file
for infile in file_list: 
    print("Adding %s to the chain" %(infile))
    file = ROOT.TFile.Open(infile)
    tree1 = ROOT.TTree() 
    tree1 = file.Get("Events")
    chain.Add(infile)
#print("Number of events in chain " + str(chain.GetEntries()))
#print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
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

#systTree = systWeights()
#systTree.prepareDefault(True, addQ2, addPDF, addTopPt, addVHF, addTTSplit)


ntop = 0





def reco(scenario, isMC, addPDF, training):

    isNominal = False
    if scenario == 'nominal':
        isNominal = True
    print(scenario)
    outTreeFile.cd()
    tree2 = tree1.CloneTree()
    nTop=0
    tree2.SetBranchAddress("nTop",nTop)
    Top_wp90 = array.array('f',[0.]*131)
    #Top_wp90  = np.empty(nTop)
    br = tree2.Branch("Top_wp90", Top_wp90,"Top_wp90[nTop]/F")
    tree2.SetBranchAddress("Top_wp90",Top_wp90)


    for i in range(tree.GetEntries()):
        tree2.GetEntry(i)        
        event = Event(tree,i)    
        jets = Collection(event, "Jet")             # jets[j1].btagDeepFlavB  ---> medium discriminant cut = 0.2783
        tops = Collection(event,"Top")
        met = Object(event, "MET")
        electron = Collection(event, "Electron")
        muon = Collection(event, "Muon")
        nelectron = len(electron)
        nmuon = len(muon)
        ntop = len(tops)
        fatjets = Collection(event,"FatJet")
        #Top_wp90  = array.array('f',np.zeros(ntop))
        #Top_wp90.empty()
        #selected = fatjet_tag_tot(fatjets)
        #if(len(selected)<1): continue #  print(i,selected)
        if i%1000 == 0:
            print("Processed ", i+1, " out of ", tree.GetEntries(), " events")

        all_coll=[]
        all_coll_wp90=[]
        top_mer_res = list(filter(lambda x: x.Is_dR_merg>=0,tops))

        k=0
        f=0
        for top in tops:
            score = 0


            for train in training:
                if(top.el_index!=-1):
                    if (train.lepton==1) and (top.Is_dR_merg == train.category) and (top.nu_pt>= train.pt_cut[0]) and (top.nu_pt<train.pt_cut[1]):
                        clf = xgb.XGBClassifier()
                        clf.load_model(train.files)
                        lista=[]
                        for m in train.var_MET: lista.append(met[m])
                        for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                        for el in train.var_lep: lista.append(electron[int(top.el_index)][el])
                        for t in train.var_top:  lista.append(top[t]) 
                        X = np.array([lista,])
                        score_ = clf.predict_proba(X)[0, 1] 
                        if (score_>train.score_cut):score=1
                if(top.mu_index!=-1):
                    if (train.lepton==0) and (top.Is_dR_merg == train.category) and (top.nu_pt>= train.pt_cut[0]) and (top.nu_pt<train.pt_cut[1]):
                        clf = xgb.XGBClassifier()
                        clf.load_model(train.files)
                        lista=[]
                        for m in train.var_MET: lista.append(met[m])
                        for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                        for mu in train.var_lep: lista.append(muon[int(top.mu_index)][mu])
                        for t in train.var_top:  lista.append(top[t]) 
                        X = np.array([lista,])
                        score_ = clf.predict_proba(X)[0, 1] 
                        if (score_>train.score_cut):score=1
            Top_wp90[k] = score
            k= k+1
            
        #print(ntop,Top_wp90)
        #tree2.SetBranchAddress("Top_wp90",Top_wp90)
        #tree2.Fill()
        br.Fill()
    
    tree2.Write()
    #outTreeFile.Close()
    

  




for scenario in ["nominal"]:
    reco(scenario, isMC,addPDF, training)


endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
