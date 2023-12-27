import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MET_HLT_Filter(Module):
    def __init__(self, year):
        self.year = year
        pass
    def endJob(self):
        pass
    def beginJob(self):
        if self.year == 2017:
            self.out.branch("HLT_Ele32_WPTight_Gsf","B")
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        HLT = Object(event, "HLT")
        flag = Object(event, 'Flag')
        trigobj = Object(event, "TrigObj")
        electrons = Collection(event, "Electron")
        Ele32 = [False]

        if(self.year == 2016):
            good_HLT = HLT.IsoTkMu24 or HLT.TkMu50 or HLT.Mu50 or HLT.IsoMu24 or HLT.Ele27_WPTight_Gsf or HLT.Photon175 or HLT.AK8PFJet360_TrimMass30
            good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.eeBadScFilter and flag.BadPFMuonDzFilter
        elif(self.year == 2017):
            good_HLT = HLT.Mu50 or HLT.IsoMu27 or HLT.Ele35_WPTight_Gsf or HLT.Photon200 or HLT.AK8PFJet500 or HLT.OldMu100 or HLT.TkMu100
            good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.ecalBadCalibFilter and flag.eeBadScFilter and flag.BadPFMuonDzFilter
            if (good_MET) and (not good_HLT) and (HLT.Ele32_WPTight_Gsf_L1DoubleEG):
                for el in electrons:
                    for obj in trigobj:
                        dR = deltaR(obj.eta,obj.phi,el.deltaEtaSC + el.eta ,el.phi)
                        if dR < 0.1:
                            if bin(obj.filterBits)[10]=='1' : 
                                good_HLT = True
                                Ele32[0] = True
            Ele32[0] = Ele32[0] or HLT.Ele35_WPTight_Gsf
            self.out.fillBranch("HLT_Ele32_WPTight_Gsf", Ele32[0])
                
        elif(self.year == 2018):
            good_HLT = HLT.Mu50 or HLT.IsoMu24 or HLT.OldMu100 or HLT.TkMu100 or HLT.Ele32_WPTight_Gsf or HLT.Photon200 or HLT.AK8PFJet400_TrimMass30 or HLT.AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2 or HLT.AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4 or HLT.AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02
            good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.ecalBadCalibFilter and flag.eeBadScFilter and flag.BadPFMuonDzFilter
        else:
            print "Please specify the year: possible choices are 2016, 2017 or 2018"


        return good_MET and good_HLT


MET_HLT_Filter_2016 = lambda : MET_HLT_Filter(2016)
MET_HLT_Filter_2017 = lambda : MET_HLT_Filter(2017)
MET_HLT_Filter_2018 = lambda : MET_HLT_Filter(2018)
