import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class lepSFProducer(Module):
    def __init__(self, muonSelectionTag, electronSelectionTag):
        self.muonSelectionTag = muonSelectionTag
        self.electronSelectionTag = electronSelectionTag
        # histograms for the analysis

        # Tight WP (with Iso)
        if muonSelectionTag == "TightWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_RECO.root","Mu_2016preVFP_ID.root", "Mu_2016preVFP_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_TightID_DEN_TrackerMuons_abseta_pt", "NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"]

        if electronSelectionTag == "IsoMVA80_2016preVFP":
            el_f = ["El_2016preVFP_reco.root", "El_2016preVFP_wp80iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "TightWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_RECO.root","Mu_2016postVFP_ID.root", "Mu_2016postVFP_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_TightID_DEN_TrackerMuons_abseta_pt", "NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"]

        if electronSelectionTag == "IsoMVA80_2016postVFP":
            el_f = ["El_2016postVFP_reco.root", "El_2016postVFP_wp80iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "TightWP_2017":
            mu_f = ["Mu_2017_RECO.root","Mu_2017_ID.root", "Mu_2017_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_TightID_DEN_TrackerMuons_abseta_pt", "NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"]

        if electronSelectionTag == "IsoMVA80_2017":
            el_f = ["El_2017_reco.root", "El_2017_wp80iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "TightWP_2018":
            mu_f = ["Mu_2018_RECO.root","Mu_2018_ID.root", "Mu_2018_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_TightID_DEN_TrackerMuons_abseta_pt", "NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"]

        if electronSelectionTag == "IsoMVA80_2018":
            el_f = ["El_2018_reco.root", "El_2018_wp80iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        #Loose WP


        if muonSelectionTag == "LooseWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_RECO.root","Mu_2016preVFP_ID.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt"]

        if electronSelectionTag == "NoIsoMVA90_2016preVFP":
            el_f = ["El_2016preVFP_reco.root", "El_2016preVFP_wp90noiso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "LooseWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_RECO.root","Mu_2016postVFP_ID.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt"]

        if electronSelectionTag == "NoIsoMVA90_2016postVFP":
            el_f = ["El_2016postVFP_reco.root", "El_2016postVFP_wp90noiso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "LooseWP_2017":
            mu_f = ["Mu_2017_RECO.root","Mu_2017_ID.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt"]

        if electronSelectionTag == "NoIsoMVA90_2017":
            el_f = ["El_2017_reco.root", "El_2017_wp90noiso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "LooseWP_2018":
            mu_f = ["Mu_2018_RECO.root","Mu_2018_ID.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt"]
            #mu_f = ["Mu_2018_ID.root"]
            #mu_h = ["NUM_LooseID_DEN_TrackerMuons_abseta_pt"]
        
        if electronSelectionTag == "NoIsoMVA90_2018":
            el_f = ["El_2018_reco.root", "El_2018_wp90noiso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]
            #el_f = ["El_2018_wp90noiso.root"]
            #el_h = ["EGamma_SF2D"]        

        # LooseIso WP

        if muonSelectionTag == "IsoLooseWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_RECO.root","Mu_2016preVFP_ID.root", "Mu_2016preVFP_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt", "NUM_LooseRelIso_DEN_LooseID_abseta_pt"]

        if electronSelectionTag == "IsoMVA90_2016preVFP":
            el_f = ["El_2016preVFP_reco.root", "El_2016preVFP_wp90iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "IsoLooseWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_RECO.root","Mu_2016postVFP_ID.root", "Mu_2016postVFP_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt", "NUM_LooseRelIso_DEN_LooseID_abseta_pt"]

        if electronSelectionTag == "IsoMVA90_2016postVFP":
            el_f = ["El_2016postVFP_reco.root", "El_2016postVFP_wp90iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "IsoLooseWP_2017":
            mu_f = ["Mu_2017_RECO.root","Mu_2017_ID.root", "Mu_2017_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt", "NUM_LooseRelIso_DEN_LooseID_abseta_pt"]

        if electronSelectionTag == "IsoMVA90_2017":
            el_f = ["El_2017_reco.root", "El_2017_wp90iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        if muonSelectionTag == "IsoLooseWP_2018":
            mu_f = ["Mu_2018_RECO.root","Mu_2018_ID.root", "Mu_2018_ISO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_LooseID_DEN_TrackerMuons_abseta_pt", "NUM_LooseRelIso_DEN_LooseID_abseta_pt"]

        if electronSelectionTag == "IsoMVA90_2018":
            el_f = ["El_2018_reco.root", "El_2018_wp90iso.root"]
            el_h = ["EGamma_SF2D", "EGamma_SF2D"]

        # histograms for the trigger studies
        if muonSelectionTag == "mutrg_2016":
            mu_f = ["muon_16.root"]
            mu_h = ["h2D_SF"]

        if electronSelectionTag == "eletrg_2016":
            el_f = ["electron_16.root"]
            el_h = ["h2D_SF"]

        if muonSelectionTag == "mutrg_2017":
            mu_f = ["muon_17.root"]
            mu_h = ["h2D_SF"]

        if electronSelectionTag == "eletrg_2017":
            el_f = ["electron_17.root"]
            el_h = ["h2D_SF"]

        if muonSelectionTag == "mutrg_2018":
            mu_f = ["muon_18.root"]
            mu_h = ["h2D_SF"]

        if electronSelectionTag == "eletrg_2018":
            el_f = ["electron_18.root"]
            el_h = ["h2D_SF"]


        mu_f = ["%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/leptonSF/" % os.environ['CMSSW_BASE'] + f for f in mu_f]
        el_f = ["%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/leptonSF/" % os.environ['CMSSW_BASE'] + f for f in el_f]

        self.mu_f = ROOT.std.vector(str)(len(mu_f))
        self.mu_h = ROOT.std.vector(str)(len(mu_f))
        for i in range(len(mu_f)): self.mu_f[i] = mu_f[i]; self.mu_h[i] = mu_h[i];
        self.el_f = ROOT.std.vector(str)(len(el_f))
        self.el_h = ROOT.std.vector(str)(len(el_f))
        for i in range(len(el_f)): self.el_f[i] = el_f[i]; self.el_h[i] = el_h[i];

        #        if "/LeptonEfficiencyCorrector_cc.so" not in ROOT.gSystem.GetLibraries():
        #            print "Load C++ Worker"
        #            ROOT.gROOT.ProcessLine(".L %s/src/PhysicsTools/NanoAODTools/python/postprocessing/helpers/LeptonEfficiencyCorrector.cc+" % os.environ['CMSSW_BASE'])
        #for library in "libPhysicsToolsNanoAODTools":
        #    if library not in ROOT.gSystem.GetLibraries():
        #        print("Load Library '%s'" % library.replace("lib", ""))
        #        ROOT.gSystem.Load(library)

    def beginJob(self):
        self._worker_mu = ROOT.LeptonEfficiencyCorrector(self.mu_f,self.mu_h)
        self._worker_el = ROOT.LeptonEfficiencyCorrector(self.el_f,self.el_h)
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        if 'trg' in self.electronSelectionTag or 'trg' in self.muonSelectionTag:
            self.out.branch("Muon_trigSF", "F", lenVar="nMuon")
            self.out.branch("Electron_trigSF", "F", lenVar="nElectron")
            self.out.branch("Muon_trigSF_Up", "F", lenVar="nMuon")
            self.out.branch("Electron_trigSF_Up", "F", lenVar="nElectron")
            self.out.branch("Muon_trigSF_Down", "F", lenVar="nMuon")
            self.out.branch("Electron_trigSF_Down", "F", lenVar="nElectron")
        else:
            if not "Tight" in self.muonSelectionTag:
                if "Iso" in self.muonSelectionTag:
                    self.out.branch("Muon_IsoLooseeffSF", "F", lenVar="nMuon")
                    self.out.branch("Electron_IsoLooseeffSF", "F", lenVar="nElectron")
                    self.out.branch("Muon_IsoLooseeffSF_Up", "F", lenVar="nMuon")
                    self.out.branch("Electron_IsoLooseeffSF_Up", "F", lenVar="nElectron")
                    self.out.branch("Muon_IsoLooseeffSF_Down", "F", lenVar="nMuon")
                    self.out.branch("Electron_IsoLooseeffSF_Down", "F", lenVar="nElectron")
                else:
                    self.out.branch("Muon_LooseeffSF", "F", lenVar="nMuon")
                    self.out.branch("Electron_LooseeffSF", "F", lenVar="nElectron")
                    self.out.branch("Muon_LooseeffSF_Up", "F", lenVar="nMuon")
                    self.out.branch("Electron_LooseeffSF_Up", "F", lenVar="nElectron")
                    self.out.branch("Muon_LooseeffSF_Down", "F", lenVar="nMuon")
                    self.out.branch("Electron_LooseeffSF_Down", "F", lenVar="nElectron")
            else:
                self.out.branch("Muon_TighteffSF", "F", lenVar="nMuon")
                self.out.branch("Electron_TighteffSF", "F", lenVar="nElectron")
                self.out.branch("Muon_TighteffSF_Up", "F", lenVar="nMuon")
                self.out.branch("Electron_TighteffSF_Up", "F", lenVar="nElectron")
                self.out.branch("Muon_TighteffSF_Down", "F", lenVar="nMuon")
                self.out.branch("Electron_TighteffSF_Down", "F", lenVar="nElectron")
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        muons = Collection(event, "Muon")
        electrons = Collection(event, "Electron")
        sf_el = [ self._worker_el.getSF(el.pdgId,el.pt,el.eta) for el in electrons ]
        sf_mu = [ self._worker_mu.getSF(mu.pdgId,mu.pt,mu.eta) for mu in muons ]
        sferr_el = [ self._worker_el.getSFErr(el.pdgId,el.pt,el.eta) for el in electrons ]
        sferr_mu = [ self._worker_mu.getSFErr(mu.pdgId,mu.pt,mu.eta) for mu in muons ]
        #print(sf_mu)
        if 'trg' in self.electronSelectionTag or 'trg' in self.muonSelectionTag:
            self.out.fillBranch("Muon_trigSF", sf_mu)
            self.out.fillBranch("Electron_trigSF", sf_el)
            self.out.fillBranch("Muon_trigSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
            self.out.fillBranch("Electron_trigSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
            self.out.fillBranch("Muon_trigSF_Down", [sf - errsf for errsf, sf in zip(sferr_mu, sf_mu)])
            self.out.fillBranch("Electron_trigSF_Down", [sf - errsf for errsf, sf in zip(sferr_el, sf_el)])
        else:
            if not "Tight" in self.muonSelectionTag:
                if "Iso" in self.muonSelectionTag:
                    self.out.fillBranch("Muon_IsoLooseeffSF", sf_mu)
                    self.out.fillBranch("Electron_IsoLooseeffSF", sf_el)
                    self.out.fillBranch("Muon_IsoLooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                    self.out.fillBranch("Electron_IsoLooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                    self.out.fillBranch("Muon_IsoLooseeffSF_Down", [sf - errsf for errsf, sf in zip(sferr_mu, sf_mu)])
                    self.out.fillBranch("Electron_IsoLooseeffSF_Down", [sf - errsf for errsf, sf in zip(sferr_el, sf_el)])
                else:
                    self.out.fillBranch("Muon_LooseeffSF", sf_mu)
                    self.out.fillBranch("Electron_LooseeffSF", sf_el)
                    self.out.fillBranch("Muon_LooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                    self.out.fillBranch("Electron_LooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                    self.out.fillBranch("Muon_LooseeffSF_Down", [sf - errsf for errsf, sf in zip(sferr_mu, sf_mu)])
                    self.out.fillBranch("Electron_LooseeffSF_Down", [sf - errsf for errsf, sf in zip(sferr_el, sf_el)])
            else:
                self.out.fillBranch("Muon_TighteffSF", sf_mu)
                self.out.fillBranch("Electron_TighteffSF", sf_el)
                self.out.fillBranch("Muon_TighteffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                self.out.fillBranch("Electron_TighteffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                self.out.fillBranch("Muon_TighteffSF_Down", [sf - errsf for errsf, sf in zip(sferr_mu, sf_mu)])
                self.out.fillBranch("Electron_TighteffSF_Down", [sf - errsf for errsf, sf in zip(sferr_el, sf_el)])
        return True
# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

TightlepSF_2016preVFP = lambda : lepSFProducer("TightWP_2016preVFP", "IsoMVA80_2016preVFP")
TightlepSF_2016postVFP = lambda : lepSFProducer("TightWP_2016postVFP", "IsoMVA80_2016postVFP")
TightlepSF_2017 = lambda : lepSFProducer("TightWP_2017", "IsoMVA80_2017")
TightlepSF_2018 = lambda : lepSFProducer("TightWP_2018", "IsoMVA80_2018")

LooselepSF_2016preVFP = lambda : lepSFProducer("LooseWP_2016preVFP", "NoIsoMVA90_2016preVFP")
LooselepSF_2016postVFP = lambda : lepSFProducer("LooseWP_2016postVFP", "NoIsoMVA90_2016postVFP")
LooselepSF_2017 = lambda : lepSFProducer("LooseWP_2017", "NoIsoMVA90_2017")
LooselepSF_2018 = lambda : lepSFProducer("LooseWP_2018", "NoIsoMVA90_2018")

IsoLooselepSF_2016preVFP = lambda : lepSFProducer("IsoLooseWP_2016preVFP", "IsoMVA90_2016preVFP")
IsoLooselepSF_2016postVFP = lambda : lepSFProducer("IsoLooseWP_2016postVFP", "IsoMVA90_2016postVFP")
IsoLooselepSF_2017 = lambda : lepSFProducer("IsoLooseWP_2017", "IsoMVA90_2017")
IsoLooselepSF_2018 = lambda : lepSFProducer("IsoLooseWP_2018", "IsoMVA90_2018")

trigSF_2016 = lambda : lepSFProducer("mutrg_2016", "eletrg_2016")
trigSF_2017 = lambda : lepSFProducer("mutrg_2017", "eletrg_2017")
trigSF_2018 = lambda : lepSFProducer("mutrg_2018", "eletrg_2018")
