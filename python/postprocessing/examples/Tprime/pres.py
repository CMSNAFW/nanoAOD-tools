
#!/usr/bin/env python
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopcandidate_v2 import nanoTopcand
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoprepro_v2 import nanoprepro
from PhysicsTools.NanoAODTools.postprocessing.modules.common.GenPart_MomFirstCp import GenPart_MomFirstCp
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopEvaluate_MultiScore_v2 import nanoTopevaluate_MultiScore
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from PhysicsTools.NanoAODTools.postprocessing.modules.common.MCweight_writer import MCweight_writer
from PhysicsTools.NanoAODTools.postprocessing.modules.common.Selection import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.preselection import *
from PhysicsTools.NanoAODTools.postprocessing.examples.TTto4Q.exampleAnalysis_TTto4Q import  ExampleAnalysis
from PhysicsTools.NanoAODTools.postprocessing.tools import *

import numpy as np

from importlib import import_module
import os
import optparse
import sys
import ROOT
import json
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(False)
from argparse import ArgumentParser


parser                      = ArgumentParser()
parser.add_argument("-d",                                   dest="dataset",                             default='',                 required=False,         type=str,       help="year of the dataset, to select the correct variables")


parser.add_argument("-l",                                   dest="label",                             default='',                 required=False,         type=str,       help="year of the dataset, to select the correct variables")
parser.add_argument("-n",                                   dest="indice",                             default='',                 required=False,         type=str,       help="year of the dataset, to select the correct variables")
parser.add_argument("-o",                                   dest="outname",                             default='',                 required=False,         type=str,       help="year of the dataset, to select the correct variables")

options                     = parser.parse_args()
### ARGS ###
data                        = options.dataset
label                  = options.label
indice                  = options.indice
outname              = options.outname
#print(data)
#print("")
#print("label", label)
#print(indice)


n_comb=[]
comb=[]
girare = True
#nTopRes=[]
#preselection = "Jet_pt[0] > 250"
#preselection = ""

file_list = data.split(',')
files=file_list
#print("file list", file_list)
from array import array

#files = [" root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/2CE738F9-C212-E811-BD0E-EC0D9A8222CE.root"]

# Accedi all'albero principale (solitamente "Events")

 
class CR_norm_dati(Module):



    def __init__(self, isMC=1):
        self.writeHistFile = True
        self.isMC=isMC
        
        
        

    def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)
        i=0
        i= i+1
        #print("i", i)
        #genweights
        self.h_genweight = ROOT.TH1F('h_genweight', 'h_genweight', 10, 0, 9)
        self.h_q2weight = ROOT.TH1F('h_q2weight', 'h_q2weight', 8, 0, 7)
        self.h_psweight = ROOT.TH1F('h_psweight', 'h_psweight', 4, 0, 3)
        self.h_PDFweight = ROOT.TH1F()
        self.addObject(self.h_genweight)
        self.addObject(self.h_q2weight)
        self.addObject(self.h_psweight)
        self.addObject(self.h_PDFweight)

        #MET Pt
        self.met_pt = ROOT.TH1F("met_pt", "MET pt", 15, 250, 1000)
        self.met_pt_SRTopRes0fjets = ROOT.TH1F("met_pt_SRTopRes0fjets", "MET pt SRTopRes0fjets", 15, 250, 1000)
        self.met_pt_SRTopResatleast1fjets = ROOT.TH1F("met_pt_SRTopResatleast1fjets", "MET pt SRTopRes1fjets", 15, 250, 1000)

        self.met_pt_SRTopMix0fjets = ROOT.TH1F("met_pt_SRTopMix0fjets", "MET pt SRTopMix0fjets", 15, 250, 1000)
        self.met_pt_SRTopMixatleast1fjets = ROOT.TH1F("met_pt_SRTopMixatleast1fjets", "MET pt SRTopMixatleast1fjets", 15, 250, 1000)

        self.met_pt_SRTopMer0fjets = ROOT.TH1F("met_pt_SRTopMer0fjets", "MET pt SRTopMer0fjets", 15, 250, 1000)
        self.met_pt_SRTopMeratleast1fjets = ROOT.TH1F("met_pt_SRTopMeratleast1fjets", "MET pt SRTopMeratleast1fjets", 15, 250, 1000)

        self.met_pt_1merg = ROOT.TH1F("met_pt_1merg", "MET pt 1 top MERGED", 15, 250, 1000)

        self.met_pt_1merg_tight = ROOT.TH1F("met_pt_1merg_tight", "MET pt 1 top MERGED tight", 30, 250, 1000)
        self.met_pt_1mix_tight = ROOT.TH1F("met_pt_1mix_tight", "MET pt 1 top MIX tight", 30, 250, 1000)
        self.met_pt_1res_tight = ROOT.TH1F("met_pt_1res_tight", "MET pt 1 top RES tight", 30, 250, 1000)


        self.met_pt_1merg_tight_nopres = ROOT.TH1F("met_pt_1merg_tight_nopres", "MET pt 1 top MERGED tight no pres", 30, 250, 1000)
        self.met_pt_1mix_tight_nopres = ROOT.TH1F("met_pt_1mix_tight_nopres", "MET pt 1 top MIX tight no pres", 30, 250, 1000)
        self.met_pt_1res_tight_nopres = ROOT.TH1F("met_pt_1res_tight_nopres", "MET pt 1 top RES tight no pres", 30, 250, 1000)

        self.cut_flow = ROOT.TH1F("cut_flow", "cut flow", 10, 1, 11)
    

        self.met_pt_CRTopRes0fjets = ROOT.TH1F("met_pt_CRTopRes0fjets", "MET pt CRTopRes0fjets", 15, 250, 1000)
        self.met_pt_CRTopResatleast1fjets = ROOT.TH1F("met_pt_CRTopResatleast1fjets", "MET pt CRTopRes1fjets", 15, 250, 1000)

        self.met_pt_CRTopMix0fjets = ROOT.TH1F("met_pt_CRTopMix0fjets", "MET pt CRTopMix0fjets", 15, 250, 1000)
        self.met_pt_CRTopMixatleast1fjets = ROOT.TH1F("met_pt_CRTopMixatleast1fjets", "MET pt CRTopMixatleast1fjets", 15, 250, 1000)

        self.met_pt_CRTopMer0fjets = ROOT.TH1F("met_pt_CRTopMer0fjets", "MET pt CRTopMer0fjets", 15, 250, 1000)
        self.met_pt_CRTopMeratleast1fjets = ROOT.TH1F("met_pt_CRTopMeratleast1fjets", "MET pt CRTopMeratleast1fjets", 15, 250, 1000)


        self.top_mix_Score = ROOT.TH1F("top_mix_Score", " Top Mix Score", 100, 0, 1)
        self.top_res_Score = ROOT.TH1F("top_res_Score", " Top Res Score", 100, 0, 1)
        self.top_merg_Score = ROOT.TH1F("top_merg_Score", " Top Merg Score", 100, 0, 1)


        self.top_mix_Score_nopres = ROOT.TH1F("top_mix_Score_nopres", " Top Mix Score no pres", 100, 0, 1)
        self.top_res_Score_nopres = ROOT.TH1F("top_res_Score_nopres", " Top Res Score no pres", 100, 0, 1)
        self.top_merg_Score_nopres = ROOT.TH1F("top_merg_Score_nopres", " Top Merg Score no pres", 100, 0, 1)

        self.palazzo_regioni = ROOT.TH1F("palazzo_regioni", "palazzo regioni", 12, -0.5, 11.5)





        self.addObject(self.met_pt)
        self.addObject(self.met_pt_1merg)
        self.addObject(self.cut_flow)


        self.addObject(self.met_pt_SRTopRes0fjets)
        self.addObject(self.met_pt_SRTopResatleast1fjets)

        self.addObject(self.met_pt_SRTopMix0fjets)
        self.addObject(self.met_pt_SRTopMixatleast1fjets)

        self.addObject(self.met_pt_SRTopMer0fjets)
        self.addObject(self.met_pt_SRTopMeratleast1fjets)


        self.addObject(self.met_pt_CRTopRes0fjets)
        self.addObject(self.met_pt_CRTopResatleast1fjets)

        self.addObject(self.met_pt_CRTopMix0fjets)
        self.addObject(self.met_pt_CRTopMixatleast1fjets)

        self.addObject(self.met_pt_CRTopMer0fjets)
        self.addObject(self.met_pt_CRTopMeratleast1fjets)


        self.addObject(self.top_mix_Score)
        self.addObject(self.top_res_Score)
        self.addObject(self.top_merg_Score)


        self.addObject(self.top_mix_Score_nopres)
        self.addObject(self.top_res_Score_nopres)
        self.addObject(self.top_merg_Score_nopres)

        self.addObject(self.palazzo_regioni)

        self.addObject(self.met_pt_1merg_tight)
        self.addObject(self.met_pt_1mix_tight)
        self.addObject(self.met_pt_1res_tight)



        self.addObject(self.met_pt_1merg_tight_nopres)
        self.addObject(self.met_pt_1mix_tight_nopres)
        self.addObject(self.met_pt_1res_tight_nopres)



    def deltaPhi(self, phi1, phi2):
        # Catch if being called with two objects
        if type(phi1) != float and type(phi1) != int:
            phi1 = phi1.phi
        if type(phi2) != float and type(phi2) != int:
            phi2 = phi2.phi
        # Otherwise
        dphi = (phi1 - phi2)
        while dphi > pi:
            dphi -= 2 * pi
        while dphi < -pi:
            dphi += 2 * pi
        return dphi

    def closest_phi(self, obj, collection):
        dphiMin = float("inf")
        for x in collection:
            dphi = self.deltaPhi(obj, x)
            if abs(dphi) < abs(dphiMin):
                ret = x
                dphiMin = dphi
        return dphiMin       

    def is_VetoElectron(self, electrons):
        n_VetoElectrons = 0

        for e in electrons: 
            if e.cutBased >= 1:
                if abs(e.eta) < 2.4:
                    if(e.pt) > 30:
                        n_VetoElectrons += 1    
        return n_VetoElectrons   


    def is_VetoMuon(self, muons):
        n_VetoMuons = 0

        for m in muons:
            if m.looseId == 1:
                if abs(m.eta) < 2.5:
                    if(m.pt) > 30:
                        n_VetoMuons +=1    
        return n_VetoMuons     
        
    def btag(self, jets, WP):
        nbjets = 0
        for j in jets:
            if j.btagUParTAK4B > WP:
                nbjets+=1
        return nbjets

    def forward_jet(self,jets):
        n_fwd_jet= 0
        for j in jets:
            if j.pt > 30:
                if abs(j.eta) > 2.4:
                    if j.jetIdTightLeptonVeto == 1 and j.jetIdTight == 1:
                        n_fwd_jet += 1
                        
        return n_fwd_jet             




    def preselection(self, jets, MET, electrons, muons, goodjets, goodfatjets):
        pres = False
        
        n_VetoMuons = self.is_VetoMuon(muons)
        n_VetoElectrons = self.is_VetoElectron(electrons)
        dphi_min=self.closest_phi(MET, jets)
        nbjets = self.btag(jets, 0.0246)
        if (len(goodjets) < 3 and len(goodfatjets) < 1): 
            #self.cut_flow.Fill(2)
            return False
        self.cut_flow.Fill(2)
        if (MET.pt < 250): 
            #self.cut_flow.Fill(3)
            return False
        self.cut_flow.Fill(3)
        
        if n_VetoElectrons != 0: 
            #self.cut_flow.Fill(4)
            return False
        self.cut_flow.Fill(4)
        if n_VetoMuons != 0: 
            #self.cut_flow.Fill(5)
            return False
        self.cut_flow.Fill(5)
        if dphi_min <= 0.6: 
            #self.cut_flow.Fill(6)
            return False
        self.cut_flow.Fill(6)
        if nbjets <= 1: 
            #self.cut_flow.Fill(7)

            return False
        self.cut_flow.Fill(7)
    
                                
        return True



    def top_selection(self, top, WP, top_merg=None):
        n_top = 0
        is_top_merg = (top_merg is not None and top is top_merg)
        for t in top:
            if is_top_merg:
                if t.particleNetWithMass_TvsQCD >= WP:
                    n_top += 1
            else:
                if t.TopScore >= WP:
                    n_top +=1 

        return n_top
                            





                             
                                                

                    






            





    
    
    def analyze(self, event):
        # Itera sulle collezioni disponibili in 'event'
        passes = False
        if(self.isMC==1):
            if not(
                    label == "QCD_PT15to30_2022" or
                    label == "QCD_PT30to50_2022" or
                    label == "QCD_PT50to80_2022" or
                    label == "QCD_PT80to120_2022" or
                    label == "QCD_PT120to170_2022" or
                    label == "QCD_PT170to300_2022" or
                    label == "QCD_PT300to470_2022" or
                    label == "QCD_PT470to600_2022" or
                    label == "QCD_PT600to800_2022" or
                    label == "QCD_PT800to1000_2022" or
                    label == "QCD_PT1000to1400_2022" or
                    label == "QCD_PT1400to1800_2022" or
                    label == "QCD_PT1800to2400_2022" or
                    label == "QCD_PT2400to3200_2022" or
                    label == "QCD_PT3200_2022"                
            ):      
            

                
                LHEPdfWeight = Collection(event, 'LHEPdfWeight')
                LHEScaleWeight = Collection(event, 'LHEScaleWeight')
                PSWeight = Collection(event, 'PSWeight')
                if not len(LHEPdfWeight) == 0:
                    self.h_PDFweight.SetNameTitle('h_PDFweight', 'h_PDFweight')
                    self.h_PDFweight.SetBins(len(LHEPdfWeight), 0, len(LHEPdfWeight))
                    for pdfw, i in zip(LHEPdfWeight, range(1, len(LHEPdfWeight)+1)):
                        self.h_PDFweight.GetXaxis().SetBinLabel(i, 'pdf['+str(i)+']')
                        self.h_PDFweight.AddBinContent(i, pdfw.__getattr__(""))
                if not len(LHEScaleWeight) == 0: #LHE scale variation weights (w_var / w_nominal); [0] is muR=0.5 muF=0.5 hdamp=mt=272.7225 ; [1] is muR=0.5 muF=1 hdamp=mt=272.7225 ; [2] is muR=0.5 muF=2 hdamp=mt=272.7225 ; [3] is muR=1 muF=0.5 hdamp=mt=272.7225 ; [4] is muR=1 muF=1 hdamp=mt=272.7225 ; [5] is muR=1 muF=2 hdamp=mt=272.7225 ; [6] is muR=2 muF=0.5 hdamp=mt=272.7225 ; [7] is muR=2 muF=1 hdamp=mt=272.7225 ; [8] is muR=2 muF=2 hdamp=mt=272.7225
                    self.h_q2weight.Fill('muR=0.5 muF=0.5', LHEScaleWeight[0].__getattr__(""))
                    self.h_q2weight.Fill('muR=0.5 muF=1', LHEScaleWeight[1].__getattr__(""))
                    self.h_q2weight.Fill('muR=0.5 muF=2', LHEScaleWeight[2].__getattr__(""))
                    self.h_q2weight.Fill('muR=1 muF=0.5', LHEScaleWeight[3].__getattr__(""))
                    if len(LHEScaleWeight) == 9:
                        self.h_q2weight.Fill('muR=1 muF=2', LHEScaleWeight[5].__getattr__(""))
                        self.h_q2weight.Fill('muR=2 muF=0.5', LHEScaleWeight[6].__getattr__(""))
                        self.h_q2weight.Fill('muR=2 muF=1', LHEScaleWeight[7].__getattr__(""))
                        self.h_q2weight.Fill('muR=2 muF=2', LHEScaleWeight[8].__getattr__(""))
                    else:
                        self.h_q2weight.Fill('muR=1 muF=2', LHEScaleWeight[4].__getattr__(""))                 
                        self.h_q2weight.Fill('muR=2 muF=0.5', LHEScaleWeight[5].__getattr__(""))                    
                        self.h_q2weight.Fill('muR=2 muF=1', LHEScaleWeight[6].__getattr__(""))               
                        self.h_q2weight.Fill('muR=2 muF=2', LHEScaleWeight[7].__getattr__(""))
                if len(PSWeight) > 1: #PS weights (w_var / w_nominal); [0] is ISR=0.5 FSR=1; [1] is ISR=1 FSR=0.5; [2] is ISR=2 FSR=1; [3] is ISR=1 FSR=2
                    self.h_psweight.Fill('ISRdown', PSWeight[0].__getattr__(""))
                    self.h_psweight.Fill('FSRdown', PSWeight[1].__getattr__(""))
                    self.h_psweight.Fill('ISRup', PSWeight[2].__getattr__(""))
                    self.h_psweight.Fill('FSRup', PSWeight[3].__getattr__(""))
                else:
                    self.h_psweight.Fill('ISRdown', PSWeight[0].__getattr__(""))
                    self.h_psweight.Fill('FSRdown', PSWeight[0].__getattr__(""))
                    self.h_psweight.Fill('ISRup', PSWeight[0].__getattr__(""))
                    self.h_psweight.Fill('FSRup', PSWeight[0].__getattr__(""))
            Generator = Object(event, "Generator")
            self.h_genweight.Fill("SumEvents", 1)
            self.h_genweight.Fill("GenWeights", Generator.weight)
            self.cut_flow.Fill(1)

        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        fatjets = Collection(event, "FatJet")
        eventSum = ROOT.TLorentzVector()
        top_res= Collection(event, "TopResolved")
        top_merg = Collection(event, "FatJet")
        top_mix= Collection(event, "TopMixed")
        MET = Object(event, "PuppiMET")
        hlt = Object(event, "HLT")
        #goodJets =list(filter(self.is_good_Jet,jets))
        #goodFatJets =list(filter(self.is_good_FatJet,jets))
        for t in top_merg:
            self.top_merg_Score_nopres.Fill(t.particleNetWithMass_TvsQCD)
        for t in top_mix:
            self.top_mix_Score_nopres.Fill(t.TopScore)
        for t in top_res:
            self.top_res_Score_nopres.Fill(t.TopScore)
        
        goodjets, goodfatjets = presel(jets, fatjets)


        ngoodJets = len(goodjets)
        ngoodFatJets = len(goodfatjets)

        goodJets_idx =[]
        goodFatJets_idx =[]

        n_top_res_tight = self.top_selection(top_res, 0.29, top_merg)
        n_top_mix_tight = self.top_selection(top_mix, 0.85, top_merg)
        n_top_merg_tight = self.top_selection(top_merg, 0.9, top_merg)


        n_top_res_loose = self.top_selection(top_res, 0.14, top_merg)
        n_top_mix_loose = self.top_selection(top_mix, 0.72, top_merg)
        n_top_merg_loose = self.top_selection(top_merg, 0.8, top_merg)

        passed = self.preselection(jets, MET, electrons, muons, goodjets, goodfatjets)
        if n_top_res_tight >= 1:
            self.met_pt_1res_tight_nopres.Fill(MET.pt)
        if n_top_mix_tight >= 1:
            self.met_pt_1mix_tight_nopres.Fill(MET.pt)
        if n_top_merg_tight >= 1:
            self.met_pt_1merg_tight_nopres.Fill(MET.pt)

        if passed == False:
            return False
        
        for t in top_merg:
            self.top_merg_Score.Fill(t.particleNetWithMass_TvsQCD)
        for t in top_mix:
            self.top_mix_Score.Fill(t.TopScore)
        for t in top_res:
            self.top_res_Score.Fill(t.TopScore)

        self.cut_flow.Fill(8)
        self.met_pt.Fill(MET.pt)
        if len(top_merg) == 1:
            self.met_pt_1merg.Fill(MET.pt)
            self.cut_flow.Fill(9)



                   

            
        """
        n_top_res_tight = self.top_selection(top_res, 0.29, top_merg)
        n_top_mix_tight = self.top_selection(top_mix, 0.85, top_merg)
        n_top_merg_tight = self.top_selection(top_merg, 0.9, top_merg)


        n_top_res_loose = self.top_selection(top_res, 0.14, top_merg)
        n_top_mix_loose = self.top_selection(top_mix, 0.72, top_merg)
        n_top_merg_loose = self.top_selection(top_merg, 0.8, top_merg)
        """

        n_fwd_jet=self.forward_jet(jets)

        if n_top_res_tight >= 1:
            self.met_pt_1res_tight.Fill(MET.pt)
        if n_top_mix_tight >= 1:
            self.met_pt_1mix_tight.Fill(MET.pt)

        if n_top_merg_tight >= 1:
            self.met_pt_1merg_tight.Fill(MET.pt)
            
            

        #SRTopRes0fjets e SRTopResatleast1fjets
        if n_top_res_tight == 1:
            if n_top_mix_tight==0:
                if n_top_merg_tight == 0:
                    if n_fwd_jet == 0:
                        self.met_pt_SRTopRes0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(0)
                    if n_fwd_jet >= 1:
                        self.met_pt_SRTopResatleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(1)
                    


        #SRTopMix0fjets e SRTopMixatleast1fjets
        if n_top_res_tight <= 1:
            if n_top_mix_tight==1:
                if n_top_merg_tight == 0:
                    if n_fwd_jet == 0:
                        self.met_pt_SRTopMix0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(2)

                    if n_fwd_jet >= 1:
                        self.met_pt_SRTopMixatleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(3)


        #SRTopMer0fjets e SRTopmergatleast1fjets
        if n_top_res_tight == 0:
            if n_top_mix_tight <= 1:
                if n_top_merg_tight == 1:
                    if n_fwd_jet == 0:
                        self.met_pt_SRTopMer0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(4)

                    if n_fwd_jet >= 1:
                        self.met_pt_SRTopMeratleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(5)




        #CRTopRes0fjets e CRTopResatleast1fjets                                                                                                                         
        if n_top_res_loose == 1 and n_top_res_tight == 0:
            if n_top_mix_loose==0 and n_top_mix_tight == 0:
                if n_top_merg_loose == 0 and n_top_merg_tight == 0:
                    if n_fwd_jet == 0:
                        self.met_pt_CRTopRes0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(6)
                    if n_fwd_jet >= 1:
                        self.met_pt_CRTopResatleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(7)




        
        #CRTopMix0fjets e CRTopMixatleast1fjets                                                                                                                         
        if n_top_res_loose <= 1 and n_top_res_tight == 0:
            if n_top_mix_loose == 1 and n_top_mix_tight == 0:
                if n_top_merg_loose == 0 and n_top_merg_tight == 0:
                    if n_fwd_jet == 0:
                        self.met_pt_CRTopMix0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(8)

                    if n_fwd_jet >= 1:
                        self.met_pt_CRTopMixatleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(9)




        #CRTopMer0fjets e SRTopmergatleast1fjets                                                                                                                        
        if n_top_res_loose == 0 and n_top_merg_tight==0:
            if n_top_mix_loose <= 1 and n_top_mix_tight == 0:
                if n_top_merg_loose == 1 and top_merg_tight==0:
                    if n_fwd_jet == 0:
                        self.met_pt_CRTopMer0fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(10)

                    if n_fwd_jet >= 1:
                        self.met_pt_CRTopMeratleast1fjets.Fill(MET.pt)
                        self.palazzo_regioni.Fill(11)

        







        










                

        

        






if label == "DataJetMETC_2022" or label == "DataJetMETD_2022" or label == "DataJetMETE_2022" or label == "DataJetMETF_2022" or label == "DataJetMETG_2022":
    p = PostProcessor("/eos/user/f/fscrivan/faseII/prova", files, cut="",   modules=[Selection(), preselection(),  nanoTopcand(isMC=0),nanoTopevaluate_MultiScore(year = 2022, isMC=0),CR_norm_dati(isMC=0)], noOut=False, haddFileName=f"/eos/user/f/fscrivan/faseII/prova/output_prova_{label}_{indice}.root", histFileName=f"/eos/user/f/fscrivan/faseII/prova/hist_regioni_prova_{label}_{indice}.root", histDirName="./")
    p.run()
else:
    p = PostProcessor("/eos/user/f/fscrivan/faseII/prova", files, cut="", modules=[Selection(), preselection(),  GenPart_MomFirstCp(), nanoprepro(),nanoTopcand(),nanoTopevaluate_MultiScore(year = 2022),CR_norm_dati(isMC=1) ], noOut=False, haddFileName=f"/eos/user/f/fscrivan/faseII/prova/output_prova_{label}_{indice}.root", histFileName=f"/eos/user/f/fscrivan/faseII/prova/hist_regioni_prova_{label}_{indice}.root", histDirName="./")
    p.run()




