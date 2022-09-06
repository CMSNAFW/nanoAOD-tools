import ROOT
import math
import numpy as np
import xgboost as xgb
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *
from PhysicsTools.NanoAODTools.postprocessing.training_MultiClass import *

class scoring(Module):
    def __init__(self, train_set = "BDT_Tprime"):
    	self.training = training_dict[train_set]
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("Top_Score0","F", lenVar="nTop")
        self.out.branch("Top_Score1","F", lenVar="nTop")
        self.out.branch("Top_Score2","F", lenVar="nTop")

        self.out.branch("Top_TvsQCD","F", lenVar="nTop")
        self.out.branch("Top_TvsOth","F", lenVar="nTop")
        self.out.branch("Top_Region","I", lenVar="nTop")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        muon = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        electron = Collection(event, "Electron")
        MET = Object(event, "MET")
        tops = Collection(event,"Top")
        nTop = len(tops)
        Top_Score0= np.zeros(nTop)
        Top_Score1= np.zeros(nTop)
        Top_Score2= np.zeros(nTop)

        Top_TvsQCD = np.zeros(nTop)
        Top_TvsOth = np.zeros(nTop)

        Top_Region = np.zeros(nTop,dtype=int)
        
        goodTops = False

        for top_idx, top in enumerate(tops):
            score_ = [0.,0.,0.]
            region = 0
            for train in self.training:
                if(top.el_index!=-1):
                    if (train.lepton==1) and (top.Is_dR_merg == train.category) and (top.nu_pt>= train.pt_cut[0]) and (top.nu_pt<train.pt_cut[1]):
                        clf = xgb.Booster()
                        clf.load_model(train.files)
                        #print("loaded")
                        lista=[]
                        for m in train.var_MET: lista.append(met[m])
                        for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                        for el in train.var_lep: lista.append(electron[int(top.el_index)][el])
                        for t in train.var_top:  lista.append(top[t])
                        X = xgb.DMatrix(np.array([lista,]))
                        #print(clf.predict(X))
                        score_ = (clf.predict(X)).ravel()
                        if(score_[2]/(1-score_[1])>train.QCDcut):
                            if(score_[2]/(1-score_[0])>train.Tcut):
                                region = 2
                                goodTops = True
                            elif (score_[2]/(1-score_[0])>train.Lcut) :
                                region =1
                                goodTops = True

                if(top.mu_index!=-1):
                    if (train.lepton==0) and (top.Is_dR_merg == train.category) and (top.nu_pt>= train.pt_cut[0]) and (top.nu_pt<train.pt_cut[1]):
                        clf = xgb.Booster()
                        clf.load_model(train.files)
                        #print("loaded")
                        lista=[]
                        for m in train.var_MET: lista.append(met[m])
                        for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                        for mu in train.var_lep: lista.append(muon[int(top.mu_index)][mu])
                        for t in train.var_top:  lista.append(top[t])
                        X = xgb.DMatrix(np.array([lista,]))
                        #print(clf.predict(X))
                        #score_ = (clf.predict(X)).ravel()
                        if(score_[2]/(1-score_[1])>train.QCDcut):

                            if(score_[2]/(1-score_[0])>train.Tcut): 
                                region = 2
                                goodTops = True
                            elif (score_[2]/(1-score_[0])>train.Lcut) : 
                                region =1
                                goodTops = True

            Top_Score0[top_idx] = score_[0]
            Top_Score1[top_idx] = score_[1]
            Top_Score2[top_idx] = score_[2]

            
            Top_TvsOth[top_idx] = score_[2]/(1-score_[0])
            Top_TvsQCD[top_idx] = score_[2]/(1-score_[1])
            Top_Region[top_idx] = region

        self.out.fillBranch("Top_Score0",Top_Score0)
        self.out.fillBranch("Top_Score1",Top_Score1)
        self.out.fillBranch("Top_Score2",Top_Score2)
        self.out.fillBranch("Top_TvsOth",Top_TvsOth)
        self.out.fillBranch("Top_TvsQCD",Top_TvsQCD)
        self.out.fillBranch("Top_Region",Top_Region)
        tightMu = list(filter(lambda x : x.tightId and x.pt>30 , muon))
        tightEle = list(filter(lambda x : x.cutBased==4 and x.pt>30, electron))
        goodEvent = (len(tightMu)>0 or len(tightEle)>0) or goodTops
        
        return goodEvent
