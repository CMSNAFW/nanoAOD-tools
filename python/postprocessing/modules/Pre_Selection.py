import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *


class Pre_Selection(Module):
    def __init__(self):
        pass
    #
    
    #===============================
    #========Util class=============
    #===============================


    #=========Tight_Lepton =========

    #Muon
    def is_tight_muon(self,mu):
        if mu.pt < 26: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.06: return False
        return True

    #Electron
    def is_tight_electron(self,ele):
        eta = abs(ele.eta)
        reliso = ele.pfRelIso03_all
        if ele.corrected_pt < 35: return False
        if eta > 2.1: return False 
        if 1.44 < eta < 1.57: return False
        if not ele.mvaIso_WP90: return False
        if eta < 1.44 and reliso > 0.0588: return False
        if eta >= 1.57 and reliso > 0.0571: return False
        return True

    #==========Loose_Lepton=============

    #Loose Muon 
    def is_loose_muon(self,mu):
        if mu.pt < 10: return False
        if abs(mu.eta) > 2.4: return False
        if mu.pfRelIso03_all > 0.2: return False      
        return True 

    #Loose Electron 
    def is_loose_electron(self,ele):
        if ele.corrected_pt < 15: return False
        if abs(ele.eta) > 2.5: return False
        if ele.pfRelIso03_all > 0.2: return False
        return True

    #===========Jet class===============
    def is_good_Jet(self,jet):
        if jet.pt < 40: return False
        if abs(jet.eta) > 4.7: return False
        return True        

    ##
    def is_btag(self,jet):
        if jet.pt < 40: return False
        if abs(jet.eta) > 2.4: return False
        if jet.btagUParTAK4B < 0.4648: return False
        return True
    
    
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
        self.out.branch("goodJets_idx","I", lenVar="nGoodJets")
        self.out.branch("bJets_idx","I", lenVar="nBJets")
        self.out.branch("eventCount","I")

    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        
        #Varibale for the Selection.
        eventJet = 0
        eventLepton = 0
        LeptonCondition = False
        jetCondition = False 
        goodEvent = False
        isGoodPV = False

        #Indx_for_Muon_Electron
        tightMuon_idx = -1
        tightElectron_idx = -1

        #Indx_for_Jet_and_bJet
        goodJets_idx = []
        bJets_idx = []

        #Module to select in the file only if we are in the 2j+1b or 3j+1b and 3+2b tag 
        electrons = Collection(event,"Electron")
        muons = Collection(event,"Muon")
        jets = Collection(event,"Jet")
        #genparts = Collection(event,"GenPart")
        PV = Object(event,"PV")

        isGoodPV = (PV.ndof > 4 and abs(PV.z) < 20 and math.hypot(PV.x,PV.y)<2)
        #goodJets_veto = []
        
        #See if it's a JetVeto 
        if (event.Flag_JetVetoed != 0):
            return False

        #Tight Selection of Leptons
        goodMu = list(filter(self.is_tight_muon,muons))
        goodEle = list(filter(self.is_tight_electron,electrons))
        looseMu = [m for m in muons if self.is_loose_muon(m) and m not in goodMu]
        looseEle = [e for e in electrons if self.is_loose_electron(e) and e not in goodEle]

        #Selection of Jets
        goodJets =list(filter(self.is_good_Jet,jets)) 
        bJets = list(filter(self.is_btag,goodJets))

        nJets  = len(goodJets)
        nBjets = len(bJets)

        #Jet condition  
        jetCondition = ((nJets == 2 and nBjets == 1) or (nJets == 3 and (nBjets == 1 or nBjets == 2)))


        #Tight and Loose Electron condition
        nGoodMu = len(goodMu)
        nGoodEle = len(goodEle)
        nLooseMu = len(looseMu)
        nLooseEle = len(looseEle)

        LeptonCondition = False





        if (nGoodMu == 1 and nGoodEle == 0 and nLooseMu == 0 and nLooseEle == 0):
            LeptonCondition = True
            eventLepton = 1
            for i, mu in enumerate(muons):
                if mu == goodMu[0]:
                    tightMuon_idx = i
                    tightLepton = mu
                    break                        
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi) 
                if dR < 0.4:
                    return False




        if (nGoodEle == 1 and nGoodMu == 0 and nLooseEle == 0 and nLooseMu == 0):
            LeptonCondition = True
            eventLepton = 2
            for i, ele in enumerate(electrons):
                if ele == goodEle[0]:
                    tightElectron_idx = i
                    tightLepton = ele
                    break      
            for j in goodJets:
                dR = deltaR(j.eta, j.phi, tightLepton.eta, tightLepton.phi) 
                if dR < 0.4:
                    return False
 
                            
        goodEvent = LeptonCondition and jetCondition and isGoodPV

        # Selezione jet con indici
        for i, j in enumerate(jets) :
            if j in goodJets and self.is_good_Jet(j):
                goodJets_idx.append(i)
                if self.is_btag(j) and j in bJets:
                    bJets_idx.append(i)

        if goodEvent:
            if nJets == 2 and nBjets == 1:
                eventJet = 1
            elif nJets == 3 and nBjets == 1:
                eventJet = 2
            elif nJets == 3 and nBjets == 2:
                eventJet = 3
        
        self.out.fillBranch("Jet_eventCategory", eventJet)
        self.out.fillBranch("Lepton_eventCategory",eventLepton)
        self.out.fillBranch("tightMuon_idx", tightMuon_idx)
        self.out.fillBranch("tightElectron_idx", tightElectron_idx)
        self.out.fillBranch("goodJets_idx", goodJets_idx)
        self.out.fillBranch("bJets_idx", bJets_idx)


        return goodEvent
