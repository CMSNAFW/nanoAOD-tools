import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.skimtree_utils import *
from PhysicsTools.NanoAODTools.postprocessing.tools import *

import correctionlib
import json
import os 
from correctionlib import _core
import gzip


class Selection(Module):
    def __init__(self):
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/jetvetomaps.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator = _core.CorrectionSet.from_string(data)
        self.jetveto_map = evaluator["Summer24Prompt24_RunBCDEFGHI_V1"]

        # jet ID TightLeptonVeto
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/jetid.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator_jetid_TightLeptonVeto = _core.CorrectionSet.from_string(data)
        self.jetid_TightLeptonVeto = evaluator_jetid_TightLeptonVeto["AK4PUPPI_TightLeptonVeto"]

        #Fatjet ID TightLeptonVeto
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/jetid.json.gz"
         
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator_fatjetid_TightLeptonVeto = _core.CorrectionSet.from_string(data)
        self.fatjetid_TightLeptonVeto = evaluator_fatjetid_TightLeptonVeto["AK8PUPPI_TightLeptonVeto"]

        # jet ID Tight
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/jetid.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator_jetid_Tight = _core.CorrectionSet.from_string(data)
        self.jetid_Tight = evaluator_jetid_Tight["AK4PUPPI_Tight"]


        # fatjet ID Tight
        fname = "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/jetid.json.gz"
        with gzip.open(fname, "rt") as f:
            data = f.read()
            evaluator_fatjetid_Tight = _core.CorrectionSet.from_string(data)
        self.fatjetid_Tight = evaluator_fatjetid_Tight["AK8PUPPI_Tight"]

        
    
    #Tight Lepton 
    def is_tight_muon(self,mu):
        if mu.pt < 26: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.06: return False
        return True

    def is_tight_electron(self,ele):
        eta = abs(ele.eta)
        reliso = ele.pfRelIso03_all
        if ele.pt < 35: return False
        if eta > 2.1: return False 
        if 1.44 < eta < 1.57: return False
        if not ele.mvaIso_WP90: return False
        if eta < 1.44 and reliso > 0.0588: return False
        if eta >= 1.57 and reliso > 0.0571: return False
        return True
    
    
    #Loose lepton
    def is_loose_muon(self,mu):
        if mu.pt < 10: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.2: return False      
        return True 


    
    def is_loose_electron(self,ele):
        if ele.pt < 15: return False
        if abs(ele.eta) > 2.5: return False
        if ele.pfRelIso03_all > 0.2: return False
        return True


    #
    def is_good_Jet(self,jet):
        
        if jet.pt < 30: return False
        if abs(jet.eta) > 2.4: return False
        return True        

    def is_good_FatJet(self,jet):
        
        if jet.pt < 30: return False
        if abs(jet.eta) > 2.4: return False
        return True   

    ##
    def is_btag(self,jet):
        if jet.pt < 40: return False
        if abs(jet.eta) > 2.4: return False
        if jet.btagUParTAK4B < 0.4648: return False
        return True
    
    """
    def is_fake_jet_gen(self, jet, genparts, dr_cut=0.4):
        for gp in genparts:
            abs_pdg = abs(gp.pdgId)
            if abs_pdg not in [11, 13, 15]:
                continue
            if gp.status != 1:
                continue
            if deltaR(jet.eta, jet.phi, gp.eta, gp.phi) < dr_cut:
                return True
        return False
    """
    
    """
    def is_fake_jet_reco(self,jet,tightlepton,dr_cut= 0.4):
        if deltaR(jet.eta, jet.phi, lepton.eta,lepton.phi) < dr_cut:
            return True 
        return False

    """






    #Begin job class
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("Jet_eventCategory","I") 
        self.out.branch("Lepton_eventCategory","I")
        self.out.branch("tightMuon_idx","I")
        self.out.branch("tightElectron_idx","I")
        #self.out.branch("goodJets_idx","I", lenVar="nGoodJets")
        self.out.branch("bJets_idx","I", lenVar="nBJets") 
        self.out.branch("Jet_jetIdTightLeptonVeto","F", lenVar="njets") 
        self.out.branch("FatJet_jetIdTightLeptonVeto","F", lenVar="nfatjets") 

        self.out.branch("Jet_jetIdTight","F", lenVar="njets") 
        self.out.branch("FatJet_jetIdTight","F", lenVar="nfatjets") 
        
   


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        eventCat = 0
        eventlepton = 0
        goodEvent = False
        #isVetoMu = False
        #isVetoEle = False
        jetCondition = False
        #FakeJets = False
        
        #Indx_for_Muon_Electron
        tightMuon_idx = -1
        tightElectron_idx = -1

        #Indx_for_Jet_and_bJet
        goodJets_idx = []
        bJets_idx = []

        jets_jetId_TightLeptonVeto =[]
        fatjets_jetId_TightLeptonVeto =[]

        jets_jetId_Tight =[]
        fatjets_jetId_Tight =[]


        #Module to select in the file only if we are in the 2j+1b or 3j+1b and 3+2b tag 
        electrons = Collection(event,"Electron")
        muons = Collection(event,"Muon")
        jets = Collection(event,"Jet")
        genparts = Collection(event,"GenPart")
        PV = Object(event,"PV")
        fatjets    = Collection(event,"FatJet")

        #nJets = len(jets)

        # 3 jets condition.
        #if nJets > 3:
        #    return False  

        isGoodPV = (PV.ndof > 4 and abs(PV.z) < 20 and math.hypot(PV.x,PV.y)<2)

        #Tight Selection of Leptons
        goodMu = list(filter(self.is_tight_muon,muons))
        goodEle = list(filter(self.is_tight_electron,electrons))
        looseMu = [m for m in muons if self.is_loose_muon(m) and m not in goodMu]
        looseEle = [e for e in electrons if self.is_loose_electron(e) and e not in goodEle]

        #Selection of Jets
        goodJets =list(filter(self.is_good_Jet,jets)) 

        """
        #goodJets = []
        for jet in jets:
            if self.is_good_Jet(jet):
                # Scarta se il Jet jet
                if not self.is_fake_jet_gen(jet, genparts):
                    goodJets.append(jet)
        """


        bJets = list(filter(self.is_btag,goodJets))

        nJets  = len(goodJets)
        njets  = len(jets)
        nBjets = len(bJets)
        #nfatjets = len(fatJets)

        #Jet condition  
        jetCondition = ((nJets == 2 and nBjets == 1) or (nJets == 3 and (nBjets == 1 or nBjets == 2)))


        #Tight and Loose Electron condition
        nGoodMu = len(goodMu)
        nGoodEle = len(goodEle)
        nLooseMu = len(looseMu)
        nLooseEle = len(looseEle)

        leptonCondition = False





        if (nGoodMu == 1 and nGoodEle == 0 and nLooseMu == 0):
            leptonCondition = True
            eventlepton = 1
            for i, mu in enumerate(muons):
                if mu == goodMu[0]:
                    tightMuon_idx = i
                    tightLepton = mu
                    break                        
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi) 
                if dR < 0.4:
                    return False




        if (nGoodEle == 1 and nGoodMu == 0 and nLooseEle == 0):
            leptonCondition = True
            eventlepton = 2
            for i, ele in enumerate(electrons):
                if ele == goodEle[0]:
                    tightElectron_idx = i
                    tightLepton = ele
                    break      
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi) 
                if dR < 0.4:
                    return False
 
                             


        goodEvent = leptonCondition and jetCondition and isGoodPV

        # Selezione jet con indici
        for i, j in enumerate(jets) :
            if self.is_good_Jet(j):
                goodJets_idx.append(i)
                if self.is_btag(j):
                    bJets_idx.append(i)
            





   
            #Apply the jetvetomap
            veto_val = self.jetveto_map.evaluate("jetvetomap", j.eta, j.phi)
        
            
            jetid_result_TightLeptonVeto = self.jetid_TightLeptonVeto.evaluate(
                    j.eta,
                    j.chHEF,
                    j.neHEF,
                    j.chEmEF,
                    j.neEmEF,
                    j.muEF,
                    j.chMultiplicity,
                    j.neMultiplicity,
                    j.chMultiplicity + j.neMultiplicity,
            )
            jets_jetId_TightLeptonVeto.append(jetid_result_TightLeptonVeto)
            #print("jetid_result_TightLeptonVeto", jetid_result_TightLeptonVeto)
            #fatjet
            fatjetid_result_TightLeptonVeto = self.fatjetid_TightLeptonVeto.evaluate(
                    j.eta,
                    j.chHEF,
                    j.neHEF,
                    j.chEmEF,
                    j.neEmEF,
                    j.muEF,
                    j.chMultiplicity,
                    j.neMultiplicity,
                    j.chMultiplicity + j.neMultiplicity,
            )
            fatjets_jetId_TightLeptonVeto.append(fatjetid_result_TightLeptonVeto)
            #print("fatjetid_result_TightLeptonVeto", fatjetid_result_TightLeptonVeto)


            #id Tight
            jetid_result_Tight = self.jetid_Tight.evaluate(
                    j.eta,
                    j.chHEF,
                    j.neHEF,
                    j.chEmEF,
                    j.neEmEF,
                    j.muEF,
                    j.chMultiplicity,
                    j.neMultiplicity,
                    j.chMultiplicity + j.neMultiplicity,
            )
            jets_jetId_Tight.append(jetid_result_Tight)
            #print("jetid_result_Tight", jetid_result_Tight)
            #fatjet
            fatjetid_result_Tight = self.fatjetid_Tight.evaluate(
                    j.eta,
                    j.chHEF,
                    j.neHEF,
                    j.chEmEF,
                    j.neEmEF,
                    j.muEF,
                    j.chMultiplicity,
                    j.neMultiplicity,
                    j.chMultiplicity + j.neMultiplicity,
            )
            fatjets_jetId_Tight.append(fatjetid_result_Tight)
            #print("fatjetid_result_Tight", fatjetid_result_Tight)


    
            


        if goodEvent:
            if nJets == 2 and nBjets == 1:
                eventCat = 1
            elif nJets == 3 and nBjets == 1:
                eventCat = 2
            elif nJets == 3 and nBjets == 2:
                eventCat = 3
        
        self.out.fillBranch("Jet_eventCategory", eventCat)
        self.out.fillBranch("Lepton_eventCategory",eventlepton)
        self.out.fillBranch("tightMuon_idx", tightMuon_idx)
        self.out.fillBranch("tightElectron_idx", tightElectron_idx)
        #self.out.fillBranch("goodJets_idx", goodJets_idx)
        self.out.fillBranch("bJets_idx", bJets_idx) 
        self.out.fillBranch("Jet_jetIdTightLeptonVeto", jets_jetId_TightLeptonVeto)    
        self.out.fillBranch("FatJet_jetIdTightLeptonVeto", fatjets_jetId_TightLeptonVeto) 

        self.out.fillBranch("Jet_jetIdTight", jets_jetId_Tight)    
        self.out.fillBranch("FatJet_jetIdTight", fatjets_jetId_Tight) 


        
        return goodEvent