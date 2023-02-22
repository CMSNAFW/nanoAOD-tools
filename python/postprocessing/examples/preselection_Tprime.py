import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *

class preselection_Tprime(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        goodEvent = False
        isVetoMu = False
        isVetoEle = False
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        met = Object(event, "MET")
        fatjets= Collection(event,"FatJet")

        looseEle = []
        looseMu = []
        looseFatJet=[]

        looseFatJet = list(filter(lambda x : (x.msoftdrop>=60 and x.msoftdrop<=220) or x.particleNetMD_Xbb>=0.8 or  weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8,fatjets))
        looseMu = list(filter(lambda x : x.looseId , muons))
        looseEle = list(filter(lambda x : x.mvaFall17V2noIso_WP90==1, electrons))
        goodEvent = (len(looseMu)>0 or len(looseEle)>0) and met.pt>25 and len(looseFatJet)>0

        return goodEvent

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
#MySelectorModuleConstr = lambda : exampleProducer(jetetaSelection= lambda j : abs(j.eta)<2.4) 
