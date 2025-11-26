import ROOT
import math
import numpy as np
from array import array
#from datetime import datetime
ROOT.PyConfig.IgnoreCommandLineOptions = True
#from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *
#from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *


def matching(genpart, gen, jet, sgn_top, dR = 0.4):
    b       = sgn_top*5
    w       = sgn_top*24
    sgn_u   = sgn_top
    sgn_d   = -sgn_top
    match   = False
    jet_out = None

    # Matching della b proveniente da un top con un jet/fatjet
    if (gen.pdgId == b and gen.genPartIdxMother_prompt > -1 and genpart[gen.genPartIdxMother_prompt].pdgId == sgn_top*6):
        #print('b quark cand ', gen.pdgId)
        j, dr =  closest_(gen, jet)
        if dr < dR:
            #print('found match b quark', j)
            jet_out = j
            match   = True
    # Matching di un u/c proveniente da una W proveniente dal top con un jet/fatjet      
    elif (gen.pdgId%2 == 0 and gen.pdgId/abs(gen.pdgId) == sgn_u and gen.genPartIdxMother_prompt > -1 and genpart[gen.genPartIdxMother_prompt].pdgId == w):
        # La W deve provenire da un top 
        if (genpart[genpart[gen.genPartIdxMother_prompt].genPartIdxMother_prompt].pdgId == sgn_top*6):
            #print('u quark cand', gen.pdgId)
            j, dr = closest_(gen, jet)
            if dr < dR:
                #print('found match up quark', j)
                jet_out = j
                match   = True
    # Matching di un d/s proveniente da una W proveniente dal top con un jet/fatjet            
    elif (gen.pdgId%2 != 0 and gen.pdgId/abs(gen.pdgId) == sgn_d and gen.genPartIdxMother_prompt > -1 and genpart[gen.genPartIdxMother_prompt].pdgId == w):
        # La W deve provenire da un to
        if (genpart[genpart[gen.genPartIdxMother_prompt].genPartIdxMother_prompt].pdgId == sgn_top*6):
            #print('d quark cand')
            j, dr =  closest_(gen, jet)
            if dr < dR:
                #print('found match down quark', j)
                jet_out = j
                match = True
    return match, jet_out




class genlevel_analysis(Module):
    def __init__(self, isMC=1):
        self.isMC = isMC
        pass
        
        
    def beginJob(self):
        pass
        
        
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        
        self.out.branch("nLepTop",      "I")
        self.out.branch("nHadTop",      "I")
        self.out.branch("nGenTop",      "I")
        self.out.branch("GenTop_idx",      "I", lenVar="nGenTop")
        self.out.branch("nPromptTop",      "I")
        self.out.branch("PromptTop_idx",      "I", lenVar="nPromptTop")

    def endFile(self, inputFile, outputFile, inputTree,wrappedOutputTree):
        pass


    def analyze(self, event):
        #t0 = datetime.now()
        """process event, return True (go to next module) or False (fail, go to next event)"""        
        jets       = Collection(event,"Jet")
        Njets      = len(jets)
        fatjets    = Collection(event,"FatJet")
        Nfatjets   = len(fatjets)
        muons      = Collection(event, "Muon")
        electrons  = Collection(event, "Electron")
        if self.isMC==1:
            genpart = Collection(event, "GenPart")


        nLepTop=0
        nHadTop=0
        nGenTop=0
        nPromptTop=0
        GenTopIdx=[]
        PromptTopIdx=[]
        print("initial nPromptTop", nPromptTop, "initila nGenTop", nGenTop)
        if self.isMC==1:
            #if (len(looseMu)>0 or len(looseEle)>0):# and met.pt>25:
            for n in range(len(genpart)):
                gen = genpart[n]
                # Trova i top nei tDM e TTbar
                if (gen.genPartIdxMother_prompt == -1 and abs(gen.pdgId)==6):
                    if (gen.genPartIdxMother == 0):
                        nGenTop+=1
                        # Trova  i top nei Tprime
                    elif (gen.genPartIdxMother_prompt != -1 and abs(gen.pdgId)==6):
                        if ((gen.genPartIdxMother == 0 or abs(genpart[gen.genPartIdxMother_prompt].pdgId) == 8000001)):
                            nGenTop+=1

            for gen in genpart: #cerco particelle figlie di W e nipoti di top
                momidx=-1
                if(gen.genPartIdxMother==-1):continue# controllo che la mamma esista (se no gli if dopo falliscono)
                if(gen.genPartIdxMother_prompt!=-1) :# se non e' la prima della catena prendo l'indice della prima con mother_idx_prompt 
                    if(abs(genpart[gen.genPartIdxMother_prompt].pdgId)==24):
                        momidx=gen.genPartIdxMother_prompt
                if(abs(genpart[gen.genPartIdxMother].pdgId)==24 and gen.genPartIdxMother_prompt==-1 and abs(gen.pdgId)!=24):# se e' la prima della catena prendo l'indice della madre vera e propria
                   momidx=gen.genPartIdxMother
                if(momidx>-1): #la particella e' figlia di una W: posso cercare la mamma della W
                    print("part id" , gen.pdgId, "mother prompt ", momidx , " Promptmother id ", genpart[momidx].pdgId)

                    if(abs(genpart[genpart[momidx].genPartIdxMother_prompt].pdgId)==6): #se la mamma della W e' un top
                        tidx = genpart[momidx].genPartIdxMother_prompt #prendo l'indice del top
                        print("top found at ", tidx)
                        if tidx in PromptTopIdx: continue #controllo che non l'ho gia' preso dalle particelle precedenti
                        nPromptTop+=1
                        PromptTopIdx.append(tidx)
                        print(" n prompt top ", nPromptTop, " nGenTop ",nGenTop)
                        if abs(gen.pdgId) in [1, 2, 3, 4, 5, 6]:
                            nHadTop += 1
                        if abs(gen.pdgId) in [11,12,13,14,15,16]:
                            nLepTop += 1
                        #controllare i processi semilep
                        



        print(" final n prompt top ",nPromptTop, "final n gen top ", nGenTop)
        print("nHadTop",nHadTop)
        print("nLepTop",nLepTop)
        self.out.fillBranch("nGenTop", nGenTop)
        self.out.fillBranch("nPromptTop", nPromptTop)

        self.out.fillBranch("nLepTop", nLepTop)
        self.out.fillBranch("nHadTop", nHadTop)

        self.out.fillBranch("GenTop_idx", GenTopIdx)
        self.out.fillBranch("PromptTop_idx", PromptTopIdx)
 
        return True
