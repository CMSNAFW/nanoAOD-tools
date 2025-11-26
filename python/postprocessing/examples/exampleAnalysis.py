
#!/usr/bin/env python
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopcandidate_v2 import nanoTopcand
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoprepro import nanoprepro
from PhysicsTools.NanoAODTools.postprocessing.modules.common.GenPart_MomFirstCp import GenPart_MomFirstCp
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopEvaluate_MultiScore_v2 import nanoTopevaluate_MultiScore
import numpy as np
from array import array
from importlib import import_module
import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(False)
n_comb=[]
comb=[]
girare = True
#nTopRes=[]
preselection = "Jet_pt[0] > 250"
files=["/eos/user/o/oiorio/tDM/PFNano/nano_mcRun3_ttsl1.root"] 
#files = [" root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/2CE738F9-C212-E811-BD0E-EC0D9A8222CE.root"]


class ExampleAnalysis(Module):

    def __init__(self):
        self.writeHistFile = True
        self.roc_curves = {}
        

    def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)

        self.sumpt = ROOT.TH1F('sumpt', 'sumpt', 100, 0, 1000)
        self.n_jet = ROOT.TH1F('n_jet', 'n_jet', 10, 0, 10)

        self.n_comb = ROOT.TH1F('n_comb', 'n_comb', 1000, 0, 1000)
        self.n_top = ROOT.TH1F('n_top', 'n_top', 1000, 0, 1000)
        self.top_res_score_bkg = ROOT.TH1F('top_res_score_bkg', 'top_res_score_bkg', 100, 0, 1)
        self.top_mix_score_bkg = ROOT.TH1F('top_mix_score_bkg', 'top_mix_score_bkg', 100, 0, 1)
        self.top_res_score_sig = ROOT.TH1F('top_res_score_sig', 'top_res_score_sig', 100, 0, 1)
        self.top_mix_score_sig = ROOT.TH1F('top_mix_score_sig', 'top_mix_score_sig', 100, 0, 1)

        self.top_res_score_pt300_bkg = ROOT.TH1F('top_res_score_pt300_bkg', 'top_res_score_pt300_bkg', 100, 0, 1)
        self.top_mix_score_pt300_bkg = ROOT.TH1F('top_mix_score_pt300_bkg', 'top_mix_score_pt300_bkg', 100, 0, 1)
        self.top_res_score_pt300_sig = ROOT.TH1F('top_res_score_pt300_sig', 'top_res_score_pt300_sig', 100, 0, 1)
        self.top_mix_score_pt300_sig = ROOT.TH1F('top_mix_score_pt300_sig', 'top_mix_score_pt300_sig', 100, 0, 1)

        self.top_res_score_eff1_bkg = ROOT.TH1F('top_res_score_eff1_bkg', 'n_top_res_eff1 bkg', 10, -0.5, 10.5)
        self.top_mix_score_eff1_bkg = ROOT.TH1F('top_mix_score_eff1_bkg', 'n_top_mix_eff1 bkg', 20, -0.5, 20.5)
        self.top_res_score_eff1_sig = ROOT.TH1F('top_res_score_eff1_sig', 'n_top_res_eff1_sig', 10, -0.5, 10.5)
        self.top_mix_score_eff1_sig = ROOT.TH1F('top_mix_score_eff1_sig', 'n_top_mix_eff1_sig', 20, -0.5, 20.5)

        self.top_res_score_pt300_eff1_bkg = ROOT.TH1F('top_res_score_pt300_eff1_bkg', 'n_top_res_pt300_eff1_bkg ', 10, -0.5, 10.5)
        self.top_mix_score_pt300_eff1_bkg = ROOT.TH1F('top_mix_score_pt300_eff1_bkg', 'n_top_mix_pt300_eff1_bkg ', 20, -0.5, 20.5)
        self.top_res_score_pt300_eff1_sig = ROOT.TH1F('top_res_score_pt300_eff1_sig', 'n_top_res_pt300_eff1_sig', 10, -0.5, 10.5)
        self.top_mix_score_pt300_eff1_sig = ROOT.TH1F('top_mix_score_pt300_eff1_sig', 'n_top_mix_pt300_eff1_sig', 20, -0.5, 20.5)

        self.top_res_score_eff5_bkg = ROOT.TH1F('top_res_score_eff5_bkg', 'n_top_res_eff5_bkg ', 20, -0.5, 20.5)
        self.top_mix_score_eff5_bkg = ROOT.TH1F('top_mix_score_eff5_bkg', 'n_top_mix_eff5_bkg ', 40, -0.5, 40.5)
        self.top_res_score_eff5_sig = ROOT.TH1F('top_res_score_eff5_sig', 'n_top_res_eff5_sig', 20, -0.5, 20.5)
        self.top_mix_score_eff5_sig = ROOT.TH1F('top_mix_score_eff5_sig', 'n_top_mix_eff5_sig', 40, -0.5, 40.5)

        self.top_res_score_pt300_eff5_bkg = ROOT.TH1F('top_res_score_pt300_eff5_bkg', 'n_top_res_pt300_eff5_bkg ', 10, -0.5, 10.5)
        self.top_mix_score_pt300_eff5_bkg = ROOT.TH1F('top_mix_score_pt300_eff5_bkg', 'n_top_mix_pt300_eff5_bkg ', 40, -0.5, 40.5)
        self.top_res_score_pt300_eff5_sig = ROOT.TH1F('top_res_score_pt300_eff5_sig', 'n_top_res_pt300_eff5_sig', 10, -0.5, 10.5)
        self.top_mix_score_pt300_eff5_sig = ROOT.TH1F('top_mix_score_pt300_eff5_sig', 'n_top_mix_pt300_eff5_sig', 40, -0.5, 40.5)

        self.top_res_score_eff10_bkg = ROOT.TH1F('top_res_score_eff10_bkg', 'n_top_res_eff10_bkg', 30, -0.5, 30.5)
        self.top_mix_score_eff10_bkg = ROOT.TH1F('top_mix_score_eff10_bkg', 'n_top_mix_eff10_bkg', 100, -0.5, 100.5)
        self.top_res_score_eff10_sig = ROOT.TH1F('top_res_score_eff10_sig', 'n_top_res_eff10_sig', 30, -0.5, 30.5)
        self.top_mix_score_eff10_sig = ROOT.TH1F('top_mix_score_eff10_sig', 'n_top_mix_eff10_sig', 100, -0.5, 100.5)

        self.top_res_score_pt300_eff10_bkg = ROOT.TH1F('top_res_score_pt300_eff10_bkg', 'n_top_res_pt300_eff10_bkg', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff10_bkg = ROOT.TH1F('top_mix_score_pt300_eff10_bkg', 'n_top_mix_pt300_eff10_bkg', 50, -0.5, 50.5)
        self.top_res_score_pt300_eff10_sig = ROOT.TH1F('top_res_score_pt300_eff10_sig', 'n_top_res_pt300_eff10_sig', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff10_sig = ROOT.TH1F('top_mix_score_pt300_eff10_sig', 'n_top_mix_pt300_eff10_sig', 50, -0.5, 50.5)

        self.top_res_score_eff_0_5_bkg = ROOT.TH1F('top_res_score_eff_0_5_bkg', 'n_top_res_eff_0_5_bkg', 30, -0.5, 30.5)
        self.top_mix_score_eff_0_5_bkg = ROOT.TH1F('top_mix_score_eff_0_5_bkg', 'n_top_mix_eff_0_5_bkg', 100, -0.5, 100.5)
        self.top_res_score_eff_0_5_sig = ROOT.TH1F('top_res_score_eff_0_5_sig', 'n_top_res_eff_0_5__sig', 30, -0.5, 30.5)
        self.top_mix_score_eff_0_5_sig = ROOT.TH1F('top_mix_score_eff_0_5_sig', 'n_top_mix_eff_0_5_sig', 100, -0.5, 100.5)

        self.top_res_score_pt300_eff_0_5_bkg = ROOT.TH1F('top_res_score_pt300_eff_0_5_bkg', 'n_top_res_pt300_eff_0_5_bkg', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff_0_5_bkg = ROOT.TH1F('top_mix_score_pt300_eff_0_5_bkg', 'n_top_mix_pt300_eff_0_45_bkg', 100, -0.5, 100.5)
        self.top_res_score_pt300_eff_0_5_sig = ROOT.TH1F('top_res_score_pt300_eff_0_5_sig', 'n_top_res_pt300_eff_0_5__sig', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff_0_5_sig = ROOT.TH1F('top_mix_score_pt300_eff_0_5_sig', 'n_top_mix_pt300_eff_0_45_sig', 100, -0.5, 100.5)

        self.top_res_score_eff_0_1_bkg = ROOT.TH1F('top_res_score_eff_0_1_bkg', 'n_top_res_eff_0_1_bkg', 30, -0.5, 30.5)
        self.top_mix_score_eff_0_1_bkg = ROOT.TH1F('top_mix_score_eff_0_1_bkg', 'n_top_mix_eff_0_1_bkg', 100, -0.5, 100.5)
        self.top_res_score_eff_0_1_sig = ROOT.TH1F('top_res_score_eff_0_1_sig', 'n_top_res_eff_0_1__sig', 30, -0.5, 30.5)
        self.top_mix_score_eff_0_1_sig = ROOT.TH1F('top_mix_score_eff_0_1_sig', 'n_top_mix_eff_0_1_sig', 100, -0.5, 100.5)

        self.top_res_score_pt300_eff_0_1_bkg = ROOT.TH1F('top_res_score_pt300_eff_0_1_bkg', 'n_top_res_pt300_eff_0_1_bkg', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff_0_1_bkg = ROOT.TH1F('top_mix_score_pt300_eff_0_1_bkg', 'n_top_mix_pt300_eff_0_2_bkg', 100, -0.5, 100.5)
        self.top_res_score_pt300_eff_0_1_sig = ROOT.TH1F('top_res_score_pt300_eff_0_1_sig', 'n_top_res_pt300_eff_0_1__sig', 30, -0.5, 30.5)
        self.top_mix_score_pt300_eff_0_1_sig = ROOT.TH1F('top_mix_score_pt300_eff_0_1_sig', 'n_top_mix_pt300_eff_0_2_sig', 100, -0.5, 100.5)








        self.n_top_mix_res_eff1= ROOT.TH2F("n_top_mix_res_eff1", "n_top_mix_res_eff1", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_eff5= ROOT.TH2F("n_top_mix_res_eff5", "n_top_mix_res_eff5", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_eff10= ROOT.TH2F("n_top_mix_res_eff10", "n_top_mix_res_eff10", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_eff_0_5= ROOT.TH2F("n_top_mix_res_eff_0_5", "n_top_mix_res_eff_0_5", 30, -0.5, 10.5, 30, -0.5, 10.5) 
        self.n_top_mix_res_eff_0_1= ROOT.TH2F("n_top_mix_res_eff_0_1", "n_top_mix_res_eff_0_1", 30, -0.5, 10.5, 30, -0.5, 10.5) 

        self.n_top_mix_res_pt300_eff1= ROOT.TH2F("n_top_mix_res_pt300_eff1", "n_top_mix_res_pt300_eff1", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_pt300_eff5= ROOT.TH2F("n_top_mix_res_pt300_eff5", "n_top_mix_res_pt300_eff5", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_pt300_eff10= ROOT.TH2F("n_top_mix_res_pt300_eff10", "n_top_mix_res_pt300_eff10", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_pt300_eff_0_5= ROOT.TH2F("n_top_mix_res_pt300_eff_0_5", "n_top_mix_res_pt300_eff_0_45_0_5", 30, -0.5, 10.5, 30, -0.5, 10.5)  
        self.n_top_mix_res_pt300_eff_0_1= ROOT.TH2F("n_top_mix_res_pt300_eff_0_1", "n_top_mix_res_pt300_eff_0_2_0_1", 30, -0.5, 10.5, 30, -0.5, 10.5)  



        self.top_res_score_eff1 = ROOT.TH1F('top_res_score_eff1', 'n_top_res_eff1', 20, -0.5, 20.5)
        self.top_mix_score_eff1 = ROOT.TH1F('top_mix_score_eff1', 'n_top_mix_eff1', 40, -0.5, 40.5)
        self.top_res_score_eff5 = ROOT.TH1F('top_res_score_eff5', 'n_top_res_eff5', 20, -0.5, 20.5)
        self.top_mix_score_eff5 = ROOT.TH1F('top_mix_score_eff5', 'n_top_mix_eff5', 40, -0.5, 40.5)
        self.top_res_score_eff10 = ROOT.TH1F('top_res_score_eff10', 'n_top_res_eff10', 20, -0.5, 20.5)
        self.top_mix_score_eff10 = ROOT.TH1F('top_mix_score_eff10', 'n_top_mix_eff10', 40, -0.5, 40.5)
        self.top_res_score_eff_0_5 = ROOT.TH1F('top_res_score_eff_0_5', 'n_top_res_eff_0_5', 20, -0.5, 20.5)
        self.top_mix_score_eff_0_5 = ROOT.TH1F('top_mix_score_eff_0_5', 'n_top_mix_eff_0_5', 40, -0.5, 40.5)
        self.top_res_score_eff_0_1 = ROOT.TH1F('top_res_score_eff_0_1', 'n_top_res_eff_0_1', 20, -0.5, 20.5)
        self.top_mix_score_eff_0_1 = ROOT.TH1F('top_mix_score_eff_0_1', 'n_top_mix_eff_0_1', 40, -0.5, 40.5)


        self.top_res_score_pt300_eff1 = ROOT.TH1F('top_res_score_pt300_eff1', 'n_top_res_eff1', 20, -0.5, 20.5)
        self.top_mix_score_pt300_eff1 = ROOT.TH1F('top_mix_score_pt300_eff1', 'n_top_mix_eff1', 40, -0.5, 40.5)
        self.top_res_score_pt300_eff5 = ROOT.TH1F('top_res_score_pt300_eff5', 'n_top_res_eff5', 20, -0.5, 20.5)
        self.top_mix_score_pt300_eff5 = ROOT.TH1F('top_mix_score_pt300_eff5', 'n_top_mix_eff5', 40, -0.5, 40.5)
        self.top_res_score_pt300_eff10 = ROOT.TH1F('top_res_score_pt300_eff10', 'n_top_res_eff10', 20, -0.5, 20.5)
        self.top_mix_score_pt300_eff10 = ROOT.TH1F('top_mix_score_pt300_eff10', 'n_top_mix_eff10', 40, -0.5, 40.5)
        self.top_res_score_pt300_eff_0_5 = ROOT.TH1F('top_res_score_pt300_eff_0_5', 'n_top_res_eff_0_5', 20, -0.5, 20.5)
        self.top_mix_score_pt300_eff_0_5 = ROOT.TH1F('top_mix_score_pt300_eff_0_5', 'n_top_mix_eff_0_5', 40, -0.5, 40.5)
        self.top_res_score_pt300_eff_0_1 = ROOT.TH1F('top_res_score_pt300_eff_0_1', 'n_top_res_eff_0_1', 20, -0.5, 20.5)
        self.top_mix_score_pt300_eff_0_1 = ROOT.TH1F('top_mix_score_pt300_eff_0_1', 'n_top_mix_eff_0_1', 40, -0.5, 40.5)


        self.addObject(self.sumpt)
        self.addObject(self.n_jet)
        self.addObject(self.n_comb)
        self.addObject(self.n_top)

        self.addObject(self.top_res_score_bkg)
        self.addObject(self.top_mix_score_bkg)
        self.addObject(self.top_res_score_sig)
        self.addObject(self.top_mix_score_sig)

        self.addObject(self.top_res_score_pt300_bkg)
        self.addObject(self.top_mix_score_pt300_bkg)
        self.addObject(self.top_res_score_pt300_sig)
        self.addObject(self.top_mix_score_pt300_sig)

        self.addObject(self.top_res_score_eff1_bkg)
        self.addObject(self.top_mix_score_eff1_bkg)
        self.addObject(self.top_res_score_eff1_sig)
        self.addObject(self.top_mix_score_eff1_sig)

        self.addObject(self.top_res_score_pt300_eff1_bkg)
        self.addObject(self.top_mix_score_pt300_eff1_bkg)
        self.addObject(self.top_res_score_pt300_eff1_sig)
        self.addObject(self.top_mix_score_pt300_eff1_sig)

        self.addObject(self.top_res_score_eff5_bkg)
        self.addObject(self.top_mix_score_eff5_bkg)
        self.addObject(self.top_res_score_eff5_sig)
        self.addObject(self.top_mix_score_eff5_sig)

        self.addObject(self.top_res_score_pt300_eff5_bkg)
        self.addObject(self.top_mix_score_pt300_eff5_bkg)
        self.addObject(self.top_res_score_pt300_eff5_sig)
        self.addObject(self.top_mix_score_pt300_eff5_sig)

        self.addObject(self.top_res_score_eff10_bkg)
        self.addObject(self.top_mix_score_eff10_bkg)
        self.addObject(self.top_res_score_eff10_sig)
        self.addObject(self.top_mix_score_eff10_sig)

        self.addObject(self.top_res_score_pt300_eff10_bkg)
        self.addObject(self.top_mix_score_pt300_eff10_bkg)
        self.addObject(self.top_res_score_pt300_eff10_sig)
        self.addObject(self.top_mix_score_pt300_eff10_sig)

        self.addObject(self.top_res_score_eff_0_5_bkg)
        self.addObject(self.top_mix_score_eff_0_5_bkg)
        self.addObject(self.top_res_score_eff_0_5_sig)
        self.addObject(self.top_mix_score_eff_0_5_sig)

        self.addObject(self.top_res_score_pt300_eff_0_5_bkg)
        self.addObject(self.top_mix_score_pt300_eff_0_5_bkg)
        self.addObject(self.top_res_score_pt300_eff_0_5_sig)
        self.addObject(self.top_mix_score_pt300_eff_0_5_sig)

        self.addObject(self.top_res_score_eff_0_1_bkg)
        self.addObject(self.top_mix_score_eff_0_1_bkg)
        self.addObject(self.top_res_score_eff_0_1_sig)
        self.addObject(self.top_mix_score_eff_0_1_sig)

        self.addObject(self.top_res_score_pt300_eff_0_1_bkg)
        self.addObject(self.top_mix_score_pt300_eff_0_1_bkg)
        self.addObject(self.top_res_score_pt300_eff_0_1_sig)
        self.addObject(self.top_mix_score_pt300_eff_0_1_sig)

        self.addObject(self.n_top_mix_res_eff1)
        self.addObject(self.n_top_mix_res_eff5)
        self.addObject(self.n_top_mix_res_eff10)
        self.addObject(self.n_top_mix_res_eff_0_5)
        self.addObject(self.n_top_mix_res_eff_0_1)

        self.addObject(self.n_top_mix_res_pt300_eff1)
        self.addObject(self.n_top_mix_res_pt300_eff5)
        self.addObject(self.n_top_mix_res_pt300_eff10)
        self.addObject(self.n_top_mix_res_pt300_eff_0_5)
        self.addObject(self.n_top_mix_res_pt300_eff_0_1)

        self.addObject(self.top_res_score_eff10)
        self.addObject(self.top_mix_score_eff10)
        self.addObject(self.top_res_score_eff5)
        self.addObject(self.top_mix_score_eff5)
        self.addObject(self.top_res_score_eff1)
        self.addObject(self.top_mix_score_eff1)
        self.addObject(self.top_res_score_eff_0_5)
        self.addObject(self.top_mix_score_eff_0_5)
        self.addObject(self.top_res_score_eff_0_1)
        self.addObject(self.top_mix_score_eff_0_1)

        self.addObject(self.top_res_score_pt300_eff10)
        self.addObject(self.top_mix_score_pt300_eff10)
        self.addObject(self.top_res_score_pt300_eff5)
        self.addObject(self.top_mix_score_pt300_eff5)
        self.addObject(self.top_res_score_pt300_eff1)
        self.addObject(self.top_mix_score_pt300_eff1)
        self.addObject(self.top_res_score_pt300_eff_0_5)
        self.addObject(self.top_mix_score_pt300_eff_0_5)
        self.addObject(self.top_res_score_pt300_eff_0_1)
        self.addObject(self.top_mix_score_pt300_eff_0_1)


        
        

        
        
    def conta_entries_in_range(self,istogramma, min_range, max_range):
        bin_min = istogramma.FindBin(min_range)  # Trova il bin corrispondente a min_range
        bin_max = istogramma.FindBin(max_range)  # Trova il bin corrispondente a max_range
        conteggio = 0
        
        conteggio_totale = istogramma.GetEntries()

        # Somma il contenuto dei bin nel range
        for bin in range(bin_min, bin_max + 1):
            conteggio += istogramma.GetBinContent(bin)
        
                
        if conteggio_totale > 0:
            efficienza = conteggio / conteggio_totale
        else:
            efficienza = 0


        return efficienza
    
    def efficienza(self,istogramma,cut_min, cut_max,step):
        eff=[]
        # Funzione per stampare le efficienze in modo ordinato
        
            

        for var_cut in np.arange(cut_min,cut_max, step):
            eff.append( self.conta_entries_in_range(istogramma, var_cut, istogramma.GetXaxis().GetXmax()))


            
        return eff
    def print_efficiencies(self, label, eff_bkg, eff_sig, cut_min=0, cut_max=1, step=0.01):
        print(label)
        print("=" * 40)
        print(f"{'Taglio':<10}{'Eff. Bkg':<15}{'Eff. Sig':<15}")
        print("-" * 40)

        for i, eff in enumerate(eff_bkg):
            if eff <= 0.2:
                cut_value = cut_min + i * step
                print(f"{cut_value:<10.2f}{eff:<15.4f}{eff_sig[i]:<15.4f}")

        print("=" * 40)
    
    def roc_curve(self, hist_bkg, hist_sig, min_range, max_range, step, name, title=None):
    
        eff_bkg = self.efficienza(hist_bkg, min_range, max_range, step)
        eff_sig = self.efficienza(hist_sig, min_range, max_range, step)


        roc = ROOT.TGraph(len(eff_bkg), array('d', eff_bkg), array('d', eff_sig))
        roc.GetXaxis().SetTitle(" #varepsilon_{b}")
        roc.GetYaxis().SetTitle(" #varepsilon_{s}")
        
      
         
    
        if title:
            roc.SetTitle(title)
        else:
            roc.SetTitle("ROC curve")
    
    
        
        self.roc_curves[name] = roc  # Salva nel dizionario senza sovrascrivere
        self.addObject(roc)  

        if self.writeHistFile and self.histFile:
            self.histFile.cd()  
            roc.Write(name)  
            self.histFile.Write()

        return roc, eff_bkg, eff_sig



    def analyze(self, event):
        
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        eventSum = ROOT.TLorentzVector()
        top_res= Collection(event, "TopResolved")
        #print("ciao brutti", dir(top_res))
        top_mix= Collection(event, "TopMixed")

        n_top_res= len(top_res)
        n_comb=[]
        n_top_res_eff10_bkg = 0
        n_top_res_eff5_bkg = 0
        n_top_res_eff1_bkg = 0
        n_top_res_eff_0_5_bkg = 0
        n_top_res_eff_0_1_bkg = 0

        n_top_res_pt300_eff10_bkg = 0
        n_top_res_pt300_eff5_bkg = 0
        n_top_res_pt300_eff1_bkg = 0
        n_top_res_pt300_eff_0_5_bkg = 0
        n_top_res_pt300_eff_0_1_bkg = 0

        n_top_res_eff10_sig = 0
        n_top_res_eff5_sig = 0
        n_top_res_eff1_sig = 0
        n_top_res_eff_0_5_sig = 0
        n_top_res_eff_0_1_sig = 0

        n_top_res_pt300_eff10_sig = 0
        n_top_res_pt300_eff5_sig = 0
        n_top_res_pt300_eff1_sig = 0
        n_top_res_pt300_eff_0_5_sig = 0
        n_top_res_pt300_eff_0_1_sig = 0

        n_top_mix_eff10_bkg = 0
        n_top_mix_eff5_bkg = 0
        n_top_mix_eff1_bkg = 0
        n_top_mix_eff_0_5_bkg = 0
        n_top_mix_eff_0_1_bkg = 0

        n_top_mix_pt300_eff10_bkg = 0
        n_top_mix_pt300_eff5_bkg = 0
        n_top_mix_pt300_eff1_bkg = 0
        n_top_mix_pt300_eff_0_5_bkg = 0
        n_top_mix_pt300_eff_0_1_bkg = 0

        n_top_mix_eff10_sig = 0
        n_top_mix_eff5_sig = 0
        n_top_mix_eff1_sig = 0
        n_top_mix_eff_0_5_sig = 0
        n_top_mix_eff_0_1_sig = 0

        n_top_mix_pt300_eff10_sig = 0
        n_top_mix_pt300_eff5_sig = 0
        n_top_mix_pt300_eff1_sig = 0
        n_top_mix_pt300_eff_0_5_sig = 0
        n_top_mix_pt300_eff_0_1_sig = 0

        n_top_res_eff10 = 0
        n_top_res_eff5 = 0
        n_top_res_eff1 = 0
        n_top_res_eff_0_5 = 0
        n_top_res_eff_0_1 =0

        n_top_res_pt300_eff10 = 0
        n_top_res_pt300_eff5 = 0
        n_top_res_pt300_eff1 = 0
        n_top_res_pt300_eff_0_5 = 0
        n_top_res_pt300_eff_0_1 = 0


        n_top_mix_eff10 = 0
        n_top_mix_eff5 = 0
        n_top_mix_eff1 = 0
        n_top_mix_eff_0_5 = 0
        n_top_mix_eff_0_1 = 0

        n_top_mix_pt300_eff10 = 0
        n_top_mix_pt300_eff5 = 0
        n_top_mix_pt300_eff1 = 0
        n_top_mix_pt300_eff_0_5 = 0
        n_top_mix_pt300_eff_0_1 = 0

        # select events with at least 2 muons
        if girare:

            for lep in muons:  # loop on muons
                eventSum += lep.p4()
            for lep in electrons:  # loop on electrons
                eventSum += lep.p4()
            
            n_jet = 0
            n_jet2 = 0
            for j in jets: 
                
                
                
                eventSum += j.p4()
                if j.pt >= 20:
                    
                    n_jet += 1
                else:
                     n_jet2 += 1
            
            for idx_j0 in range(len(jets)):         
                for idx_j1 in range(idx_j0 + 1, len(jets)):  
                    for idx_j2 in range(idx_j1 + 1, len(jets)):  
                        comb.append((jets[idx_j0], jets[idx_j1], jets[idx_j2]))
                        
            
            n_comb.append(len(comb))
            #print("nTop resolved",n_top_res, "numero combinazioni", n_comb)

            #print(f"sumpt filled with: {eventSum.Pt()}") 
            self.sumpt.Fill(eventSum.Pt())  # fill histogram
            self.n_jet.Fill(n_jet)
            self.n_comb.Fill(len(comb))
            
            self.n_top.Fill(n_top_res)
            for t_r in top_res:
                if t_r.truth == 0:
                    self.top_res_score_bkg.Fill(t_r.TopScore)
                    if t_r.TopScore >= 0.17:
                        n_top_res_eff10_bkg += 1
                        
                    if t_r.TopScore >= 0.27:
                        n_top_res_eff5_bkg += 1
                        
                    if t_r.TopScore >= 0.68:
                        n_top_res_eff1_bkg += 1
                    if t_r.TopScore >= 0.81:
                        #print("ciao")
                        n_top_res_eff_0_5_bkg += 1
                    if t_r.TopScore >= 0.91:
                        #print("hello")
                        n_top_res_eff_0_1_bkg += 1
                        
                    
                    if t_r.pt >= 300:
                        self.top_res_score_pt300_bkg.Fill(t_r.TopScore)
                        if t_r.TopScore >= 0.02:
                            n_top_res_pt300_eff10_bkg += 1
                            
                        if t_r.TopScore >= 0.07:
                            n_top_res_pt300_eff5_bkg += 1
                            
                        if t_r.TopScore >= 0.32:
                            n_top_res_pt300_eff1_bkg += 1
                        if t_r.TopScore >= 0.58:
                            n_top_res_pt300_eff_0_5_bkg += 1
                        if t_r.TopScore >= 0.86:
                            n_top_res_pt300_eff_0_1_bkg += 1
                            
                if t_r.truth == 1:
                    self.top_res_score_sig.Fill(t_r.TopScore)
                    if t_r.TopScore >= 0.17:
                        n_top_res_eff10_sig += 1
                        
                    if t_r.TopScore >= 0.27:
                        n_top_res_eff5_sig += 1
                        
                    if t_r.TopScore >= 0.68:
                        n_top_res_eff1_sig += 1

                    if t_r.TopScore >= 0.81:
                        n_top_res_eff_0_5_sig += 1
                    if t_r.TopScore >= 0.91:
                        n_top_res_eff_0_1_sig += 1
                        
            

            
                    
                    if t_r.pt >= 300:
                        self.top_res_score_pt300_sig.Fill(t_r.TopScore)
                        if t_r.TopScore >= 0.02:
                            n_top_res_pt300_eff10_sig += 1
                            
                        if t_r.TopScore >= 0.07:
                            n_top_res_pt300_eff5_sig += 1
                            
                        if t_r.TopScore >= 0.32:
                            n_top_res_pt300_eff1_sig += 1
                        if t_r.TopScore >= 0.58:
                            n_top_res_pt300_eff_0_5_sig += 1
                        if t_r.TopScore >= 0.86:
                            n_top_res_pt300_eff_0_1_sig += 1



    

            for t_m in top_mix:
                if t_m.truth == 0:
                    self.top_mix_score_bkg.Fill(t_m.TopScore)
                    if t_m.TopScore >= 0.26:
                        n_top_mix_eff10_bkg += 1
                        
                    if t_m.TopScore >= 0.56:
                        n_top_mix_eff5_bkg += 1
                        
                    if t_m.TopScore >= 0.91:
                        n_top_mix_eff1_bkg += 1
                    if t_m.TopScore >= 0.95:
                        #print("hola")
                        n_top_mix_eff_0_5_bkg += 1
                    if t_m.TopScore >= 0.98:
                        n_top_mix_eff_0_1_bkg += 1
                    
                        

                    
                    if t_m.pt >= 300:
                        self.top_mix_score_pt300_bkg.Fill(t_m.TopScore)
                        if t_m.TopScore >= 0.27:
                            n_top_mix_pt300_eff10_bkg += 1
                            
                        if t_m.TopScore >= 0.54:
                            n_top_mix_pt300_eff5_bkg += 1
                            
                        if t_m.TopScore >= 0.92:
                            n_top_mix_pt300_eff1_bkg += 1
                        if t_m.TopScore >= 0.96:
                            #print("salve")
                            n_top_mix_pt300_eff_0_5_bkg += 1
                        if t_m.TopScore >= 0.99:
                            n_top_mix_pt300_eff_0_1_bkg += 1
                        
                            
                if t_m.truth == 1:
                    self.top_mix_score_sig.Fill(t_m.TopScore)
                    if t_m.TopScore >= 0.26:
                        n_top_mix_eff10_sig += 1
                        
                    if t_m.TopScore >= 0.56:
                        n_top_mix_eff5_sig += 1
                        
                    if t_m.TopScore >= 0.91:
                        n_top_mix_eff1_sig += 1
                    if t_m.TopScore >= 0.95:
                        n_top_mix_eff_0_5_sig += 1
                    if t_m.TopScore >= 0.98:
                        n_top_mix_eff_0_1_sig += 1

                        

          

                    
                    if t_m.pt >= 300:
                        self.top_mix_score_pt300_sig.Fill(t_m.TopScore)
                        if t_m.TopScore >= 0.27:
                            n_top_mix_pt300_eff10_sig += 1
                            
                        if t_m.TopScore >= 0.54:
                            n_top_mix_pt300_eff5_sig += 1
                            
                        if t_m.TopScore >= 0.92:
                            n_top_mix_pt300_eff1_sig += 1
                        if t_m.TopScore >= 0.96:
                            #print("hello")
                            n_top_mix_pt300_eff_0_5_sig += 1
                        if t_m.TopScore >= 0.99:
                            #print("ciao")
                            n_top_mix_pt300_eff_0_1_sig += 1


            self.top_res_score_eff5_bkg.Fill( n_top_res_eff5_bkg)
            self.top_res_score_eff1_bkg.Fill( n_top_res_eff1_bkg)
            self.top_res_score_eff10_bkg.Fill( n_top_res_eff10_bkg)
            self.top_res_score_eff_0_5_bkg.Fill( n_top_res_eff_0_5_bkg)
            self.top_res_score_eff_0_1_bkg.Fill( n_top_res_eff_0_1_bkg)

            self.top_res_score_eff10_sig.Fill( n_top_res_eff10_sig)
            self.top_res_score_eff5_sig.Fill( n_top_res_eff5_sig)
            self.top_res_score_eff1_sig.Fill( n_top_res_eff1_sig)
            self.top_res_score_eff_0_5_sig.Fill( n_top_res_eff_0_5_sig)
            self.top_res_score_eff_0_1_sig.Fill( n_top_res_eff_0_1_sig)
            

            self.top_res_score_pt300_eff1_bkg.Fill(n_top_res_pt300_eff1_bkg)
            self.top_res_score_pt300_eff10_bkg.Fill( n_top_res_pt300_eff10_bkg)
            self.top_res_score_pt300_eff5_bkg.Fill( n_top_res_pt300_eff5_bkg)
            self.top_res_score_pt300_eff_0_5_bkg.Fill( n_top_res_pt300_eff_0_5_bkg)
            self.top_res_score_pt300_eff_0_1_bkg.Fill( n_top_res_pt300_eff_0_1_bkg)

            self.top_res_score_pt300_eff10_sig.Fill( n_top_res_pt300_eff10_sig)
            self.top_res_score_pt300_eff5_sig.Fill( n_top_res_pt300_eff5_sig)
            self.top_res_score_pt300_eff1_sig.Fill(n_top_res_pt300_eff1_sig)
            self.top_res_score_pt300_eff_0_5_sig.Fill(n_top_res_pt300_eff_0_5_sig)
            self.top_res_score_pt300_eff_0_1_sig.Fill(n_top_res_pt300_eff_0_1_sig)

            self.top_mix_score_eff1_bkg.Fill( n_top_mix_eff1_bkg)
            self.top_mix_score_eff5_bkg.Fill( n_top_mix_eff5_bkg)
            self.top_mix_score_eff10_bkg.Fill( n_top_mix_eff10_bkg) 
            self.top_mix_score_eff_0_5_bkg.Fill( n_top_mix_eff_0_5_bkg)
            self.top_mix_score_eff_0_1_bkg.Fill( n_top_mix_eff_0_1_bkg)
            
            self.top_mix_score_eff10_sig.Fill( n_top_mix_eff10_sig)
            self.top_mix_score_eff5_sig.Fill( n_top_mix_eff5_sig)
            self.top_mix_score_eff1_sig.Fill( n_top_mix_eff1_sig)
            self.top_mix_score_eff_0_5_sig.Fill( n_top_mix_eff_0_5_sig)
            self.top_mix_score_eff_0_1_sig.Fill( n_top_mix_eff_0_1_sig)
             

            self.top_mix_score_pt300_eff10_sig.Fill( n_top_mix_pt300_eff10_sig)
            self.top_mix_score_pt300_eff5_sig.Fill( n_top_mix_pt300_eff5_sig)
            self.top_mix_score_pt300_eff1_sig.Fill(n_top_mix_pt300_eff1_sig)
            self.top_mix_score_pt300_eff_0_5_sig.Fill(n_top_mix_pt300_eff_0_5_sig)
            self.top_mix_score_pt300_eff_0_1_sig.Fill(n_top_mix_pt300_eff_0_1_sig)

            self.top_mix_score_pt300_eff10_bkg.Fill( n_top_mix_pt300_eff10_bkg)
            self.top_mix_score_pt300_eff5_bkg.Fill( n_top_mix_pt300_eff5_bkg)
            self.top_mix_score_pt300_eff1_bkg.Fill(n_top_mix_pt300_eff1_bkg)
            self.top_mix_score_pt300_eff_0_5_bkg.Fill(n_top_mix_pt300_eff_0_5_bkg)
            self.top_mix_score_pt300_eff_0_1_bkg.Fill(n_top_mix_pt300_eff_0_1_bkg)
            
            n_top_mix_eff10=n_top_mix_eff10_sig+ n_top_mix_eff10_bkg
            n_top_mix_eff5=n_top_mix_eff5_sig+ n_top_mix_eff5_bkg
            n_top_mix_eff1=n_top_mix_eff1_sig+ n_top_mix_eff1_bkg
            n_top_mix_eff_0_5=n_top_mix_eff_0_5_sig+ n_top_mix_eff_0_5_bkg
            n_top_mix_eff_0_1=n_top_mix_eff_0_1_sig+ n_top_mix_eff_0_1_bkg
            self.top_mix_score_eff10.Fill(n_top_mix_eff10)
            self.top_mix_score_eff5.Fill( n_top_mix_eff5)
            self.top_mix_score_eff1.Fill(n_top_mix_eff1)
            self.top_mix_score_eff_0_5.Fill(n_top_mix_eff_0_5)
            self.top_mix_score_eff_0_1.Fill(n_top_mix_eff_0_1)

            n_top_mix_pt300_eff10=n_top_mix_pt300_eff10_sig+ n_top_mix_pt300_eff10_bkg
            n_top_mix_pt300_eff5=n_top_mix_pt300_eff5_sig+ n_top_mix_pt300_eff5_bkg
            n_top_mix_pt300_eff1=n_top_mix_pt300_eff1_sig+ n_top_mix_pt300_eff1_bkg
            n_top_mix_pt300_eff_0_5=n_top_mix_pt300_eff_0_5_sig+ n_top_mix_pt300_eff_0_5_bkg
            n_top_mix_pt300_eff_0_1=n_top_mix_pt300_eff_0_1_sig+ n_top_mix_pt300_eff_0_1_bkg
            self.top_mix_score_pt300_eff10.Fill( n_top_mix_pt300_eff10)
            self.top_mix_score_pt300_eff5.Fill( n_top_mix_pt300_eff5)
            self.top_mix_score_pt300_eff1.Fill(n_top_mix_pt300_eff1)
            self.top_mix_score_pt300_eff_0_5.Fill(n_top_mix_pt300_eff_0_5)
            self.top_mix_score_pt300_eff_0_1.Fill(n_top_mix_pt300_eff_0_1)

            #print("n_top_mix_pt300_eff_0_5", n_top_mix_pt300_eff_0_5)
            #print(self.top_mix_score_pt300_eff_0_5.Integral())
            n_top_res_eff10=n_top_res_eff10_sig+ n_top_res_eff10_bkg
            n_top_res_eff5=n_top_res_eff5_sig+ n_top_res_eff5_bkg
            n_top_res_eff1=n_top_res_eff1_sig+ n_top_res_eff1_bkg
            n_top_res_eff_0_5=n_top_res_eff_0_5_sig+ n_top_res_eff_0_5_bkg
            self.top_res_score_eff10.Fill( n_top_res_eff10)
            self.top_res_score_eff5.Fill(n_top_res_eff5)
            self.top_res_score_eff1.Fill(n_top_res_eff1)
            self.top_res_score_eff_0_5.Fill(n_top_res_eff_0_5)
            self.top_res_score_eff_0_1.Fill(n_top_res_eff_0_1)


            n_top_res_pt300_eff10=n_top_res_pt300_eff10_sig+ n_top_res_pt300_eff10_bkg
            n_top_res_pt300_eff5=n_top_res_pt300_eff5_sig+ n_top_res_pt300_eff5_bkg
            n_top_res_pt300_eff1=n_top_res_pt300_eff1_sig+ n_top_res_pt300_eff1_bkg
            n_top_res_pt300_eff_0_5=n_top_res_pt300_eff_0_5_sig+ n_top_res_pt300_eff_0_5_bkg
            n_top_res_pt300_eff_0_1=n_top_res_pt300_eff_0_1_sig+ n_top_res_pt300_eff_0_1_bkg
            self.top_res_score_pt300_eff10.Fill( n_top_res_pt300_eff10)
            self.top_res_score_pt300_eff5.Fill(n_top_res_pt300_eff5)
            self.top_res_score_pt300_eff1.Fill(n_top_res_pt300_eff1)
            self.top_res_score_pt300_eff_0_5.Fill(n_top_res_pt300_eff_0_5)
            self.top_res_score_pt300_eff_0_1.Fill(n_top_res_pt300_eff_0_1)

            self.n_top_mix_res_eff1.Fill(n_top_res_eff1,n_top_mix_eff1)
            self.n_top_mix_res_eff5.Fill(n_top_res_eff5,n_top_mix_eff5)
            self.n_top_mix_res_eff10.Fill(n_top_res_eff10,n_top_mix_eff10)
            self.n_top_mix_res_eff_0_5.Fill(n_top_res_eff_0_5,n_top_mix_eff_0_5)
            self.n_top_mix_res_eff_0_1.Fill(n_top_res_eff_0_1,n_top_mix_eff_0_1)



            self.n_top_mix_res_pt300_eff1.Fill(n_top_res_pt300_eff1,n_top_mix_pt300_eff1)
            self.n_top_mix_res_pt300_eff5.Fill(n_top_res_pt300_eff5,n_top_mix_pt300_eff5)
            self.n_top_mix_res_pt300_eff10.Fill(n_top_res_pt300_eff10,n_top_mix_pt300_eff10)
            self.n_top_mix_res_pt300_eff_0_5.Fill(n_top_res_pt300_eff_0_5,n_top_mix_pt300_eff_0_5)
            self.n_top_mix_res_pt300_eff_0_1.Fill(n_top_res_pt300_eff_0_1,n_top_mix_pt300_eff_0_1)


                            
            

        return True




    def endJob(self):
        eff_roc_top_res_bkg=[]
        eff_roc_top_res_sig=[]
        eff_roc_top_mix_bkg=[]
        eff_roc_top_mix_sig=[]
        eff_roc_top_mix_pt300_bkg=[]
        eff_roc_top_mix_pt300_sig=[]
        eff_roc_top_res_pt300_bkg=[]
        eff_roc_top_res_pt300_sig=[]
        self.roc_top_res,eff_roc_top_res_bkg, eff_roc_top_res_sig=self.roc_curve(self.top_res_score_bkg, self.top_res_score_sig,0, 1,0.01, "roc_top_res", title="ROC CURVE Top Resolved TopScore")
        self.roc_top_mix,eff_roc_top_mix_bkg, eff_roc_top_mix_sig=self.roc_curve(self.top_mix_score_bkg, self.top_mix_score_sig,0, 1,0.01,"roc_top_mix", title="ROC CURVE Top Mixed TopScore")
        self.roc_top_mix_pt300, eff_roc_top_mix_pt300_bkg, eff_roc_top_mix_pt300_sig=self.roc_curve(self.top_mix_score_pt300_bkg, self.top_mix_score_pt300_sig,0, 1,0.01,"roc_top_mix_pt300", title="ROC CURVE Top Mixed TopScore, pt >= 300")
        self.roc_top_res_pt300, eff_roc_top_res_pt300_bkg, eff_roc_top_res_pt300_sig=self.roc_curve(self.top_res_score_pt300_bkg, self.top_res_score_pt300_sig,0, 1,0.01,"roc_top_res_pt300", title="ROC CURVE Top Resolved TopScore, pt >= 300")
            # Stampa le efficienze in maniera ordinata con il valore del taglio corrispondente
        


        # Stampa delle efficienze
        self.print_efficiencies("ROC Top Resolved", eff_roc_top_res_bkg, eff_roc_top_res_sig)
        self.print_efficiencies("ROC Top Mixed", eff_roc_top_mix_bkg, eff_roc_top_mix_sig)
        self.print_efficiencies("ROC Top Mixed pt >= 300", eff_roc_top_mix_pt300_bkg, eff_roc_top_mix_pt300_sig)
        self.print_efficiencies("ROC Top Resolved pt >= 300", eff_roc_top_res_pt300_bkg, eff_roc_top_res_pt300_sig)

    # Aggiungi eventualmente altre efficienze se necessario

    
        



p = PostProcessor(".", files, cut=preselection,  modules=[
                  GenPart_MomFirstCp(), nanoprepro(),nanoTopcand(),nanoTopevaluate_MultiScore(year = 2022),ExampleAnalysis()], noOut=False, postfix="output",histFileName="histOut.root", histDirName="plots")
p.run()



def create_canvas(name, save_name, canvas_title, *histograms):
    c = ROOT.TCanvas(name, name, 800, 600)
        
    is_2D = isinstance(histograms[0], ROOT.TH2)

    if is_2D:
        # Imposta la palette di colori
        ROOT.gStyle.SetPalette(ROOT.kRainBow)
        histograms[0].Draw("COLZ")  # Disegna con la barra dei colori
        ROOT.gStyle.SetOptStat(0)  # Disabilita la statistica per istogrammi 2D
    else:
        # Colori per gli istogrammi (fino a 4 colori)
        colors = [ROOT.kGreen, ROOT.kBlue, ROOT.kRed, ROOT.kMagenta]

        # Disegna gli istogrammi 1D
        for i, hist in enumerate(histograms):
            is_histo = isinstance(hist,ROOT.TH1)
            if is_histo:
                hist.SetLineColor(colors[i % len(colors)])  # Cicla sui colori se ci sono più di 4 istogrammi
                hist.SetLineWidth(2)  # Imposta lo spessore della linea
                hist.SetMaximum(6000)  # Imposta il limite massimo dell'asse Y
            
                if i == 0:
                    hist.Draw()  
                else:
                    hist.Draw("same")
            else:
                print("non è un histo ma:", hist) 

        # Aggiungi la legenda per gli istogrammi 1D
        legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        for hist in histograms:
            is_histo = isinstance(hist,ROOT.TH1)
            if is_histo:
                legend.AddEntry(hist, hist.GetTitle(), "l")  # "l" indica che è una linea
        legend.Draw()

    # Aggiorna e salva il canvas
    c.Update()
    c.SaveAs(save_name)



file = ROOT.TFile.Open("histOut.root") 




 

# Ottieni gli istogrammi
n_top_mix_res_eff_0_1 = file.Get("n_top_mix_res_eff_0_1")
n_top_mix_res_eff_0_5 = file.Get("n_top_mix_res_eff_0_5")

top_mix_score_eff_0_1 = file.Get("top_mix_score_eff_0_1")
top_res_score_eff_0_1 = file.Get("top_res_score_eff_0_1")
top_mix_score_eff_0_5 = file.Get("top_mix_score_eff_0_5")
top_res_score_eff_0_5 = file.Get("top_res_score_eff_0_5")
n_top_mix_res_pt300_eff_0_1 = file.Get("n_top_mix_res_pt300_eff_0_1")
n_top_mix_res_pt300_eff_0_5 = file.Get("n_top_mix_res_pt300_eff_0_5")
top_res_score_pt300_eff_0_1 = file.Get("top_res_score_pt300_eff_0_1")
top_mix_score_pt300_eff_0_1 = file.Get("top_mix_score_pt300_eff_0_1")
top_res_score_pt300_eff_0_5 = file.Get("top_res_score_pt300_eff_0_5")
top_mix_score_pt300_eff_0_5 = file.Get("top_mix_score_pt300_eff_0_5")
top_res_score_eff_0_1_bkg = file.Get("top_res_score_eff_0_1_bkg")
top_res_score_eff_0_1_sig = file.Get("top_res_score_eff_0_1_sig")
top_res_score_pt300_eff_0_1_bkg = file.Get("top_res_score_pt300_eff_0_1_bkg")
top_res_score_pt300_eff_0_1_sig = file.Get("top_res_score_pt300_eff_0_1_sig")
top_res_score_eff_0_5_bkg = file.Get("top_res_score_eff_0_5_bkg")
top_res_score_eff_0_5_sig = file.Get("top_res_score_eff_0_5_sig")
top_res_score_pt300_eff_0_5_bkg = file.Get("top_res_score_pt300_eff_0_5_bkg")
top_res_score_pt300_eff_0_5_sig = file.Get("top_res_score_pt300_eff_0_5_sig")
top_mix_score_eff_0_1_bkg = file.Get("top_mix_score_eff_0_1_bkg")
top_mix_score_eff_0_1_sig = file.Get("top_mix_score_eff_0_1_sig")
top_mix_score_pt300_eff_0_1_bkg = file.Get("top_mix_score_pt300_eff_0_1_bkg")
top_mix_score_pt300_eff_0_1_sig = file.Get("top_mix_score_pt300_eff_0_1_sig")
top_mix_score_pt300_eff_0_1 = file.Get("top_mix_score_pt300_eff_0_1")
top_mix_score_eff_0_5_bkg = file.Get("top_mix_score_eff_0_5_bkg")
top_mix_score_eff_0_5_sig = file.Get("top_mix_score_eff_0_5_sig")
top_mix_score_pt300_eff_0_5_bkg = file.Get("top_mix_score_pt300_eff_0_5_bkg")
top_mix_score_pt300_eff_0_5_sig = file.Get("top_mix_score_pt300_eff_0_5_sig")
top_mix_score_pt300_eff_0_5 = file.Get("top_mix_score_pt300_eff_0_5")
top_mix_score_pt300_eff10 = file.Get("top_mix_score_pt300_eff10")
top_res_score_pt300_eff10 = file.Get("top_res_score_pt300_eff10")
top_mix_score_pt300_eff5 = file.Get("top_mix_score_pt300_eff5")
top_res_score_pt300_eff5 = file.Get("top_res_score_pt300_eff5")
top_mix_score_pt300_eff1 = file.Get("top_mix_score_pt300_eff1")
top_res_score_pt300_eff1 = file.Get("top_res_score_pt300_eff1")
top_mix_score_eff10 = file.Get("top_mix_score_eff10")
top_res_score_eff10 = file.Get("top_res_score_eff10")
n_top_mix_res_eff10 = file.Get("n_top_mix_res_eff10")
n_top_mix_res_eff5 = file.Get("n_top_mix_res_eff5")
n_top_mix_res_eff1 = file.Get("n_top_mix_res_eff1")
n_top_mix_res_pt300_eff10 = file.Get("n_top_mix_res_pt300_eff10")
n_top_mix_res_pt300_eff5 = file.Get("n_top_mix_res_pt300_eff5")
n_top_mix_res_pt300_eff1 = file.Get("n_top_mix_res_pt300_eff1")
top_res_score_pt300_eff10_sig = file.Get("top_res_score_pt300_eff10_sig")
top_res_score_pt300_eff10_bkg = file.Get("top_res_score_pt300_eff10_bkg")
top_res_score_eff10_sig = file.Get("top_res_score_eff10_sig")
top_res_score_eff10_bkg = file.Get("top_res_score_eff10_bkg")
top_res_score_eff1 = file.Get("top_res_score_eff1")
top_res_score_pt300_eff5_sig = file.Get("top_res_score_pt300_eff5_sig")
top_res_score_pt300_eff5_bkg = file.Get("top_res_score_pt300_eff5_bkg")
top_res_score_eff5_sig = file.Get("top_res_score_eff5_sig")
top_res_score_eff5_bkg = file.Get("top_res_score_eff5_bkg")
top_res_score_eff5 = file.Get("top_res_score_eff5")
top_res_score_pt300_eff1_sig = file.Get("top_res_score_pt300_eff1_sig")
top_res_score_pt300_eff1_bkg = file.Get("top_res_score_pt300_eff1_bkg")
top_res_score_eff1_sig = file.Get("top_res_score_eff1_sig")
top_res_score_eff1_bkg = file.Get("top_res_score_eff1_bkg")
top_mix_score_pt300_eff10_sig = file.Get("top_mix_score_pt300_eff10_sig")
top_mix_score_pt300_eff10_bkg = file.Get("top_mix_score_pt300_eff10_bkg")
top_mix_score_eff10_sig = file.Get("top_mix_score_eff10_sig")
top_mix_score_eff10_bkg = file.Get("top_mix_score_eff10_bkg")
top_mix_score_pt300_eff5_sig = file.Get("top_mix_score_pt300_eff5_sig")
top_mix_score_pt300_eff5_bkg = file.Get("top_mix_score_pt300_eff5_bkg")
top_mix_score_eff5_sig = file.Get("top_mix_score_eff5_sig")
top_mix_score_eff5_bkg = file.Get("top_mix_score_eff5_bkg")
top_mix_score_eff5 = file.Get("top_mix_score_eff5")
top_mix_score_pt300_eff1_sig = file.Get("top_mix_score_pt300_eff1_sig")
top_mix_score_pt300_eff1_bkg = file.Get("top_mix_score_pt300_eff1_bkg")
top_mix_score_eff1_sig = file.Get("top_mix_score_eff1_sig")
top_mix_score_eff1_bkg = file.Get("top_mix_score_eff1_bkg")
top_mix_score_eff1 = file.Get("top_mix_score_eff1")
n_top_mix_res_pt300_eff1 = file.Get("n_top_mix_res_pt300_eff1")
n_top_mix_res_pt300_eff5 = file.Get("n_top_mix_res_pt300_eff5")
n_top_mix_res_pt300_eff10 = file.Get("n_top_mix_res_pt300_eff10")
n_top_mix_res_eff1 = file.Get("n_top_mix_res_eff1")
n_top_mix_res_eff5 = file.Get("n_top_mix_res_eff5")
n_top_mix_res_eff10 = file.Get("n_top_mix_res_eff10")
top_res_score_sig = file.Get("top_res_score_sig")
top_res_score_bkg = file.Get("top_res_score_bkg")
top_mix_score_sig = file.Get("top_mix_score_sig")
top_mix_score_bkg = file.Get("top_mix_score_bkg")
n_top = file.Get("n_top")
n_comb = file.Get("n_comb")
n_jet = file.Get("n_jet")
sumpt = file.Get("sumpt")
roc_res = file.Get("roc_top_res")
roc_mix = file.Get("roc_top_mix")

roc_res_pt300 = file.Get("roc_top_mix_pt300")
roc_mix_pt300 = file.Get("roc_top_res_pt300")






fare_histo_iniziali= False
fare_roc =False

if fare_histo_iniziali: 

    c1 = ROOT.TCanvas("canvas", "events_pt", 800, 600) 
    histo.Draw()  
    c1.SetEditable(True) 
    c1.Update()
    c1.SaveAs("somma_p4.png")  

    # Disegna il secondo istogramma (n_jet)
    c2 = ROOT.TCanvas("canvas2", "n_jet", 800, 600) 
    histo2.Draw() 
    c2.SetEditable(True)  
    c2.Update()
    c2.SaveAs("n_jet.png")  


    c4 = ROOT.TCanvas("canvas4", "n_comb", 800, 600) 
    histo4.Draw()  
    c4.SetEditable(True) 
    c4.Update()
    c4.SaveAs("n_comb.png")  # Se vuoi salvare il grafico come immagine PNG

    c5 = ROOT.TCanvas("canvas5", "n_res", 800, 600) 
  
    histo5.Draw()
    c5.SetEditable(True) 
    c5.Update()
    c5.SaveAs("n_top.png")  # Se vuoi salvare il grafico come immagine PNG

    c6 = ROOT.TCanvas("canvas6", "top_res_score", 800, 600) 
  
    histo6.Draw()
    c6.SetEditable(True) 
    c6.Update()
    c6.SaveAs("top_res_score_bkg.png")  # Se vuoi salvare il grafico come immagine PNG

    c7 = ROOT.TCanvas("canvas7", "top_mix_score", 800, 600) 
  
    histo7.Draw()
    c7.Update()
    c7.SaveAs("top_res_score_sig.png")  # Se vuoi salvare il grafico come immagine PNG

create_canvas("canvas10_11", "plot10_11.png", "top resolved eff1", top_res_score_eff1, top_res_score_eff1_sig, top_res_score_eff1_bkg)
create_canvas("canvas12_13", "plot12_13.png", "top resolved pt300 eff1", top_res_score_pt300_eff1, top_res_score_pt300_eff1_sig, top_res_score_pt300_eff1_bkg)
create_canvas("canvas14_15", "plot14_15.png", "top resolved eff5", top_res_score_eff5, top_res_score_eff5_sig, top_mix_score_eff5_bkg)
create_canvas("canvas16_17", "plot16_17.png", "top resolved pt300 eff5", top_res_score_pt300_eff5, top_res_score_pt300_eff5_sig, top_res_score_pt300_eff5_bkg)
create_canvas("canvas18_19", "plot18_19.png", "top resolved eff10", top_res_score_eff10, top_res_score_eff10_sig, top_res_score_eff10_bkg)
create_canvas("canvas20_21", "plot20_21.png", "top resolved pt300 eff10", top_res_score_pt300_eff10, top_res_score_pt300_eff10_sig, top_res_score_pt300_eff10_bkg)

create_canvas("canvas22_23", "plot22_23.png", "top mix eff1", top_mix_score_eff1, top_mix_score_eff1_sig, top_mix_score_eff1_bkg)
create_canvas("canvas24_25", "plot24_25.png", "top mix pt300 eff1", top_mix_score_pt300_eff1, top_mix_score_pt300_eff1_sig, top_mix_score_pt300_eff1_bkg)
create_canvas("canvas26_27", "plot26_27.png", "top mix eff5", top_mix_score_eff5_sig, top_mix_score_eff5_bkg, top_mix_score_eff5)
create_canvas("canvas28_29", "plot28_29.png", "top mix pt300 eff5", top_mix_score_pt300_eff5, top_mix_score_pt300_eff5_sig, top_mix_score_pt300_eff5_bkg)
create_canvas("canvas30_31", "plot30_31.png", "top mix eff10", top_mix_score_eff10, top_mix_score_eff10_sig, top_mix_score_eff10_bkg)
create_canvas("canvas32_33", "plot32_33.png", "top mix pt300 eff10", top_mix_score_pt300_eff10, top_mix_score_pt300_eff10_sig, top_mix_score_pt300_eff10_bkg)

create_canvas("canvas34_35", "plot34_35.png", "top mix eff_0_5", top_mix_score_eff_0_5, top_mix_score_eff_0_5_sig, top_mix_score_eff_0_5_bkg)
create_canvas("canvas36_37", "plot36_37.png", "top mix pt300 eff_0_5", top_mix_score_pt300_eff_0_5, top_mix_score_pt300_eff_0_5_sig, top_mix_score_pt300_eff_0_5_bkg)

create_canvas("canvas38_39", "plot38_39.png", "top mix eff_0_1", top_mix_score_eff_0_1, top_mix_score_eff_0_1_sig, top_mix_score_eff_0_1_bkg)
create_canvas("canvas40_41", "plot40_41.png", "top mix pt300 eff_0_1", top_mix_score_pt300_eff_0_1, top_mix_score_pt300_eff_0_1_sig, top_mix_score_pt300_eff_0_1_bkg)

create_canvas("canvas42_43", "plot42_43.png", "top res eff_0_5", top_res_score_eff_0_5, top_res_score_eff_0_5_sig, top_res_score_eff_0_5_bkg)
create_canvas("canvas44_45", "plot44_45.png", "top res pt300 eff_0_5", top_res_score_pt300_eff_0_5, top_res_score_pt300_eff_0_5_sig, top_res_score_pt300_eff_0_5_bkg)

create_canvas("canvas46_47", "plot46_47.png", "top res eff_0_1", top_res_score_eff_0_1, top_res_score_eff_0_1_sig, top_res_score_eff_0_1_bkg)
create_canvas("canvas48_49", "plot48_49.png", "top res pt300 eff_0_1", top_res_score_pt300_eff_0_1, top_res_score_pt300_eff_0_1_sig, top_res_score_pt300_eff_0_1_bkg)

create_canvas("canvas34", "plot34.png", "numero top mix e pt300 resolved eff1", n_top_mix_res_pt300_eff1)
create_canvas("canvas35", "plot35.png", "numero top mix e pt300 resolved eff5", n_top_mix_res_pt300_eff5)
create_canvas("canvas36", "plot36.png", "numero top mix e pt300 resolved eff10", n_top_mix_res_pt300_eff10)
create_canvas("canvas37", "plot37.png", "numero top mix e resolved eff1", n_top_mix_res_eff1)
create_canvas("canvas38", "plot38.png", "numero top mix e resolved eff5", n_top_mix_res_eff5)
create_canvas("canvas39", "plot39.png", "numero top mix e resolved eff10", n_top_mix_res_eff10)

create_canvas("canvas40", "plot40.png", "numero top mix e resolved eff_0_5", n_top_mix_res_eff_0_5)
create_canvas("canvas41", "plot41.png", "numero top mix e resolved eff_0_1", n_top_mix_res_eff_0_1)

create_canvas("canvas42", "plot42.png", "numero top mix e resolved pt300 eff_0_5", n_top_mix_res_pt300_eff_0_5)
create_canvas("canvas43", "plot43.png", "numero top mix e resolved pt300 eff_0_1", n_top_mix_res_pt300_eff_0_1)

#ROC CURVE
if fare_roc:
    c_roc_top_res = ROOT.TCanvas()
    c_roc_top_res.Draw()
    roc_res.Draw()
    roc_res.Draw("APL")
    diagonal = ROOT.TGraph(2, array('d', [0, 1]), array('d', [0, 1]))
    diagonal.SetLineColor(ROOT.kGray)
    diagonal.SetLineStyle(2)
    diagonal.Draw("same")
 
    roc_res.SetMarkerStyle(20) 
    roc_res.SetMarkerSize(1)  
    roc_res.SetMarkerColor(ROOT.kBlue)  
 
    roc_res.SetLineColor(ROOT.kMagenta+1) 
    roc_res.SetLineWidth(2) 
    #c_roc_top_res.SetLogx() 
    c_roc_top_res.SetLogy() 
    c_roc_top_res.SetEditable(True) 
    c_roc_top_res.Update()
    c_roc_top_res.SaveAs("roc_top_res.png")  # Se vuoi salvare il grafico come immagine PNG 

    c_roc_top_mix = ROOT.TCanvas()
    roc_mix.Draw()
    roc_mix.Draw("APL")
    diagonal.Draw("same")
 
    roc_mix.SetMarkerStyle(20) 
    roc_mix.SetMarkerSize(1)  
    roc_mix.SetMarkerColor(ROOT.kBlue)  
 
    roc_mix.SetLineColor(ROOT.kMagenta+1) 
    roc_mix.SetLineWidth(2) 
    #c_roc_top_mix.SetLogx() 
    c_roc_top_mix.SetLogy() 
    c_roc_top_mix.SetEditable(True) 
    c_roc_top_mix.Draw()
    c_roc_top_mix.SaveAs("roc_top_mix.png")  # Se vuoi salvare il grafico come immagine PNG 

    c_roc_top_mix_pt300 = ROOT.TCanvas()
    c_roc_top_mix_pt300.Draw()
    roc_mix_pt300.Draw()
    roc_mix_pt300.Draw("APL")
    diagonal.Draw("same")
 
    roc_mix_pt300.SetMarkerStyle(20) 
    roc_mix_pt300.SetMarkerSize(1)  
    roc_mix_pt300.SetMarkerColor(ROOT.kBlue)  
 
    roc_mix_pt300.SetLineColor(ROOT.kMagenta+1) 
    roc_mix_pt300.SetLineWidth(2) 
    #c_roc_top_mix_pt300.SetLogx() 
    c_roc_top_mix_pt300.SetLogy() 
    c_roc_top_mix_pt300.SetEditable(True) 
    c_roc_top_mix_pt300.Update()
    c_roc_top_mix_pt300.SaveAs("roc_top_mix_pt300.png")  # Se vuoi salvare il grafico come immagine PNG 

    c_roc_top_res_pt300 = ROOT.TCanvas()
    c_roc_top_res_pt300.Draw()
    roc_res_pt300.Draw()
    roc_res_pt300.Draw("APL")
    diagonal.Draw("same")
    roc_res_pt300.SetMarkerStyle(20) 
    roc_res_pt300.SetMarkerSize(1)  
    roc_res_pt300.SetMarkerColor(ROOT.kBlue)  
 
    roc_res_pt300.SetLineColor(ROOT.kMagenta+1) 
    roc_res_pt300.SetLineWidth(2) 
    #c_roc_top_res_pt300.SetLogx() 
    c_roc_top_res_pt300.SetLogy() 
    c_roc_top_res_pt300.SetEditable(True)
    c_roc_top_res_pt300.Update()
    c_roc_top_res_pt300.SaveAs("roc_top_res_pt300.png")  # Se vuoi salvare il grafico come immagine PNG 

ROOT.gApplication.Run()  # Mantiene le finestre ROOT aperte
input("Premi Invio per chiudere tutte le finestre...")  # Aspetta l'input dell'utente
ROOT.gApplication.Terminate(0)  # Chiude tutte le finestre ROOT
