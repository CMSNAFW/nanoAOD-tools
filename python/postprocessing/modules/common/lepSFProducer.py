import ROOT
import os
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class lepSFProducer(Module):
    def __init__(self, SelectionTag, err_tag = "stat"):
        self.SelectionTag = SelectionTag
        self.err_tag = err_tag
        # histograms for the analysis
        mu_f = []
        mu_h = []
        el_f = []
        el_h = []


        # RECO

        # 2016preVFP
        if SelectionTag == "RECO_2016preVFP":
            mu_f = ["Mu_2016preVFP_medium_RECO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_abseta_pt_"+err_tag]

        if SelectionTag == "RECOEl_2016preVFP":
            el_f = ["El_2016preVFP_reco.root"]
            el_h = ["EGamma_SF2D"]

        #2016postVFP
        if SelectionTag == "RECO_2016postVFP":
            mu_f = ["Mu_2016postVFP_medium_RECO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_abseta_pt_"+err_tag]

        if SelectionTag == "RECOEl_2016postVFP":
            el_f = ["El_2016postVFP_reco.root"]
            el_h = ["EGamma_SF2D"]

        #2017
        if SelectionTag == "RECO_2017":
            mu_f = ["Mu_2017_medium_RECO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_abseta_pt_"+err_tag]

        if SelectionTag == "RECOEl_2017":
            el_f = ["El_2017_reco.root"]
            el_h = ["EGamma_SF2D"]


        #2018
        if SelectionTag == "RECO_2018":
            mu_f = ["Mu_2018_medium_RECO.root"]
            mu_h = ["NUM_TrackerMuon_DEN_genTracks_abseta_pt_"+err_tag]

        if SelectionTag == "RECOEl_2018":
            el_f = ["El_2018_reco.root"]
            el_h = ["EGamma_SF2D"]



        # WP Tight

        # 2016 preVFP
        if SelectionTag == "TightWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_ID.root"]
            mu_h = ["NUM_TightID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA80_2016preVFP":
            el_f = ["El_2016preVFP_wp80iso.root"]
            el_h = ["EGamma_SF2D"]

        
        # 2016 postVFP
        if SelectionTag == "TightWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_ID.root"]
            mu_h = ["NUM_TightID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA80_2016postVFP":
            el_f = ["El_2016postVFP_wp80iso.root"]
            el_h = ["EGamma_SF2D"]


        # 2017
        if SelectionTag == "TightWP_2017":
            mu_f = ["Mu_2017_ID.root"]
            mu_h = ["NUM_TightID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA80_2017":
            el_f = ["El_2017_wp80iso.root"]
            el_h = ["EGamma_SF2D"]


        # 2018
        if SelectionTag == "TightWP_2018":
            mu_f = ["Mu_2018_ID.root"]
            mu_h = ["NUM_TightID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA80_2018":
            el_f = ["El_2018_wp80iso.root"]
            el_h = ["EGamma_SF2D"]



        # Loose ID

        if SelectionTag == "LooseWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_ID.root"]
            mu_h = ["NUM_LooseID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "NoIsoMVA90_2016preVFP":
            el_f = ["El_2016preVFP_wp90noiso.root"]
            el_h = ["EGamma_SF2D"]

        if SelectionTag == "LooseWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_ID.root"]
            mu_h = ["NUM_LooseID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "NoIsoMVA90_2016postVFP":
            el_f = ["El_2016postVFP_wp90noiso.root"]
            el_h = ["EGamma_SF2D"]

        if SelectionTag == "LooseWP_2017":
            mu_f = ["Mu_2017_ID.root"]
            mu_h = ["NUM_LooseID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "NoIsoMVA90_2017":
            el_f = ["El_2017_wp90noiso.root"]
            el_h = ["EGamma_SF2D"]

        if SelectionTag == "LooseWP_2018":
            mu_f = ["Mu_2018_ID.root"]
            mu_h = ["NUM_LooseID_DEN_TrackerMuons_abseta_pt_"+err_tag]

        if SelectionTag == "NoIsoMVA90_2018":
            el_f = ["El_2018_wp90noiso.root"]
            el_h = ["EGamma_SF2D"]
            


        # TightIso

        if SelectionTag == "TightIso_2016preVFP":
            mu_f = ["Mu_2016preVFP_ISO.root"]
            mu_h = ["NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt_"+err_tag]

        if SelectionTag == "TightIso_2016postVFP":
            mu_f = ["Mu_2016postVFP_ISO.root"]
            mu_h = ["NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt_"+err_tag]

        if SelectionTag == "TightIso_2017":
            mu_f = ["Mu_2017_ISO.root"]
            mu_h = ["NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt_"+err_tag]

        if SelectionTag == "TightIso_2018":
            mu_f = ["Mu_2018_ISO.root"]
            mu_h = ["NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt_"+err_tag]


        #Loose Iso for Muon and Loose+Iso for electron

        if SelectionTag == "IsoLooseWP_2016preVFP":
            mu_f = ["Mu_2016preVFP_ISO.root"]
            mu_h = ["NUM_LooseRelIso_DEN_LooseID_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA90_2016preVFP":
            el_f = ["El_2016preVFP_wp90iso.root"]
            el_h = ["EGamma_SF2D"]

        if SelectionTag == "IsoLooseWP_2016postVFP":
            mu_f = ["Mu_2016postVFP_ISO.root"]
            mu_h = ["NUM_LooseRelIso_DEN_LooseID_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA90_2016postVFP":
            el_f = ["El_2016postVFP_wp90iso.root"]
            el_h = ["EGamma_SF2D"]

        if SelectionTag == "IsoLooseWP_2017":
            mu_f = ["Mu_2017_ISO.root"]
            mu_h = ["NUM_LooseRelIso_DEN_LooseID_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA90_2017":
            el_f = ["El_2017_wp90iso.root"]
            el_h = ["EGamma_SF2D"]


        if SelectionTag == "IsoLooseWP_2018":
            mu_f = ["Mu_2018_ISO.root"]
            mu_h = ["NUM_LooseRelIso_DEN_LooseID_abseta_pt_"+err_tag]

        if SelectionTag == "IsoMVA90_2018":
            el_f = ["El_2018_wp90iso.root"]
            el_h = ["EGamma_SF2D"]



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
        if ("RECOEl" in self.SelectionTag) or ("MVA" in self.SelectionTag):
            self._worker_el = ROOT.LeptonEfficiencyCorrector(self.el_f,self.el_h)
        else:
            self._worker_mu = ROOT.LeptonEfficiencyCorrector(self.mu_f,self.mu_h)
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        if ("RECOEl" in self.SelectionTag) or ("MVA" in self.SelectionTag):
            if "RECO" in self.SelectionTag:
                self.out.branch("Electron_RECOeffSF", "F", lenVar="nElectron")
                self.out.branch("Electron_RECOeffSF_Up", "F", lenVar="nElectron")
                self.out.branch("Electron_RECOeffSF_Down", "F", lenVar="nElectron")
            else:
                if not "80" in self.SelectionTag:
                    if "NoIso" in self.SelectionTag:
                        self.out.branch("Electron_LooseeffSF", "F", lenVar="nElectron")
                        self.out.branch("Electron_LooseeffSF_Up", "F", lenVar="nElectron")
                        self.out.branch("Electron_LooseeffSF_Down", "F", lenVar="nElectron")
                    else:
                        self.out.branch("Electron_IsoLooseeffSF", "F", lenVar="nElectron")
                        self.out.branch("Electron_IsoLooseeffSF_Up", "F", lenVar="nElectron")
                        self.out.branch("Electron_IsoLooseeffSF_Down", "F", lenVar="nElectron")
                else:
                    self.out.branch("Electron_TighteffSF", "F", lenVar="nElectron")
                    self.out.branch("Electron_TighteffSF_Up", "F", lenVar="nElectron")
                    self.out.branch("Electron_TighteffSF_Down", "F", lenVar="nElectron")
        elif ( self.err_tag== "stat"):
            if "RECO" in self.SelectionTag:
                self.out.branch("Muon_RECOeffSF", "F", lenVar="nMuon")
                self.out.branch("Muon_RECOeffSF_Up", "F", lenVar="nMuon")
                self.out.branch("Muon_RECOeffSF_Down", "F", lenVar="nMuon")
                
            else:
                
                if not "Tight" in self.SelectionTag:
                    if "Iso" in self.SelectionTag:
                        self.out.branch("Muon_IsoLooseeffSF", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoLooseeffSF_Up", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoLooseeffSF_Down", "F", lenVar="nMuon")
                    else:
                        self.out.branch("Muon_LooseeffSF", "F", lenVar="nMuon")
                        self.out.branch("Muon_LooseeffSF_Up", "F", lenVar="nMuon")
                        self.out.branch("Muon_LooseeffSF_Down", "F", lenVar="nMuon")
                else:
                    if "Iso" in self.SelectionTag:
                        self.out.branch("Muon_IsoTighteffSF", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoTighteffSF_Up", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoTighteffSF_Down", "F", lenVar="nMuon")
                    else:
                        self.out.branch("Muon_TighteffSF", "F", lenVar="nMuon")
                        self.out.branch("Muon_TighteffSF_Up", "F", lenVar="nMuon")
                        self.out.branch("Muon_TighteffSF_Down", "F", lenVar="nMuon")
        else:
            if "RECO" in self.SelectionTag:
                self.out.branch("Muon_RECOeffSF_SystUp", "F", lenVar="nMuon")
                self.out.branch("Muon_RECOeffSF_SystDown", "F", lenVar="nMuon")

            else:

                if not "Tight" in self.SelectionTag:
                    if "Iso" in self.SelectionTag:
                        self.out.branch("Muon_IsoLooseeffSF_SystUp", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoLooseeffSF_SystDown", "F", lenVar="nMuon")
                    else:
                        self.out.branch("Muon_LooseeffSF_SystUp", "F", lenVar="nMuon")
                        self.out.branch("Muon_LooseeffSF_SystDown", "F", lenVar="nMuon")
                else:
                    if "Iso" in self.SelectionTag:
                        self.out.branch("Muon_IsoTighteffSF_SystUp", "F", lenVar="nMuon")
                        self.out.branch("Muon_IsoTighteffSF_SystDown", "F", lenVar="nMuon")
                    else:
                        self.out.branch("Muon_TighteffSF_SystUp", "F", lenVar="nMuon")
                        self.out.branch("Muon_TighteffSF_SystDown", "F", lenVar="nMuon")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        muons = Collection(event, "Muon")
        electrons = Collection(event, "Electron")

        if ("RECOEl" in self.SelectionTag) or ("MVA" in self.SelectionTag):
            sf_el = [ self._worker_el.getSF(el.pdgId,el.pt,el.eta) for el in electrons ]
            sferr_el = [ self._worker_el.getSFErr(el.pdgId,el.pt,el.eta) for el in electrons ]
        else:
            sf_mu = [ self._worker_mu.getSF(mu.pdgId,mu.pt,mu.eta) for mu in muons ]
            sferr_mu = [ self._worker_mu.getSFErr(mu.pdgId,mu.pt,mu.eta) for mu in muons ]
        
        if ("RECOEl" in self.SelectionTag) or ("MVA" in self.SelectionTag):
            if "RECO" in self.SelectionTag:
                self.out.fillBranch("Electron_RECOeffSF", sf_el)
                self.out.fillBranch("Electron_RECOeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                self.out.fillBranch("Electron_RECOeffSF_Down", [sf - errsf for errsf, sf in zip(sf_el, sferr_el)])
            else:
                if not "80" in self.SelectionTag:
                    if "NoIso" in self.SelectionTag:
                        self.out.fillBranch("Electron_LooseeffSF", sf_el)
                        self.out.fillBranch("Electron_LooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                        self.out.fillBranch("Electron_LooseeffSF_Down", [sf - errsf for errsf, sf in zip(sf_el, sferr_el)])
                    else:
                        self.out.fillBranch("Electron_IsoLooseeffSF", sf_el)
                        self.out.fillBranch("Electron_IsoLooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                        self.out.fillBranch("Electron_IsoLooseeffSF_Down", [sf - errsf for errsf, sf in zip(sf_el, sferr_el)])
                else:
                    self.out.fillBranch("Electron_TighteffSF", sf_el)
                    self.out.fillBranch("Electron_TighteffSF_Up", [errsf + sf for errsf, sf in zip(sferr_el, sf_el)])
                    self.out.fillBranch("Electron_TighteffSF_Down", [sf - errsf for errsf, sf in zip(sf_el, sferr_el)])
        elif ( self.err_tag== "stat"):
            if "RECO" in self.SelectionTag:
                self.out.fillBranch("Muon_RECOeffSF", sf_mu)
                self.out.fillBranch("Muon_RECOeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                self.out.fillBranch("Muon_RECOeffSF_Down", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])

            else:

                if not "Tight" in self.SelectionTag:
                    if "Iso" in self.SelectionTag:
                        self.out.fillBranch("Muon_IsoLooseeffSF", sf_mu)
                        self.out.fillBranch("Muon_IsoLooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_IsoLooseeffSF_Down", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                    else:
                        self.out.fillBranch("Muon_LooseeffSF", sf_mu)
                        self.out.fillBranch("Muon_LooseeffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_LooseeffSF_Down", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                else:
                    if "Iso" in self.SelectionTag:
                        self.out.fillBranch("Muon_IsoTighteffSF", sf_mu)
                        self.out.fillBranch("Muon_IsoTighteffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_IsoTighteffSF_Down", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                    else:
                        self.out.fillBranch("Muon_TighteffSF", sf_mu)
                        self.out.fillBranch("Muon_TighteffSF_Up", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_TighteffSF_Down", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
        else:
            if "RECO" in self.SelectionTag:
                self.out.fillBranch("Muon_RECOeffSF_SystUp", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                self.out.fillBranch("Muon_RECOeffSF_SystDown", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])

            else:

                if not "Tight" in self.SelectionTag:
                    if "Iso" in self.SelectionTag:
                        self.out.fillBranch("Muon_IsoLooseeffSF_SystUp", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_IsoLooseeffSF_SystDown", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                    else:
                        self.out.fillBranch("Muon_LooseeffSF_SystUp", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_LooseeffSF_SystDown", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                else:
                    if "Iso" in self.SelectionTag:
                        self.out.fillBranch("Muon_IsoTighteffSF_SystUp", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_IsoTighteffSF_SystDown", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
                    else:
                        self.out.fillBranch("Muon_TighteffSF_SystUp", [errsf + sf for errsf, sf in zip(sferr_mu, sf_mu)])
                        self.out.fillBranch("Muon_TighteffSF_SystDown", [sf - errsf for errsf, sf in zip(sf_mu, sferr_mu)])
        
            
        return True
# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

RECOMuSF_2016preVFP_stat = lambda : lepSFProducer("RECO_2016preVFP") 
TightMuSF_2016preVFP_stat = lambda : lepSFProducer("TightWP_2016preVFP")
LooseMuSF_2016preVFP_stat =  lambda : lepSFProducer("LooseWP_2016preVFP")
TightIsoMuSF_2016preVFP_stat = lambda : lepSFProducer("TightIsoWP_2016preVFP")
LooseIsoMuSF_2016preVFP_stat = lambda : lepSFProducer("IsoLooseWP_2016preVFP")


RECOMuSF_2016preVFP_syst = lambda : lepSFProducer("RECO_2016preVFP", err_tag = "syst")
TightMuSF_2016preVFP_syst = lambda : lepSFProducer("TightWP_2016preVFP", err_tag = "syst")
LooseMuSF_2016preVFP_syst =  lambda : lepSFProducer("LooseWP_2016preVFP", err_tag = "syst")
TightIsoMuSF_2016preVFP_syst = lambda : lepSFProducer("TightIsoWP_2016preVFP", err_tag = "syst")
LooseIsoMuSF_2016preVFP_syst = lambda : lepSFProducer("IsoLooseWP_2016preVFP", err_tag = "syst")

RECOElSF_2016preVFP = lambda : lepSFProducer("RECOEl_2016preVFP")
LooseElSF_2016preVFP =  lambda : lepSFProducer("NoIsoMVA90_2016preVFP")
TightIsoElSF_2016preVFP = lambda : lepSFProducer("IsoMVA80_2016preVFP")
LooseIsoElSF_2016preVFP = lambda : lepSFProducer("IsoMVA90_2016preVFP")

# 2016 post


RECOMuSF_2016postVFP_stat = lambda : lepSFProducer("RECO_2016postVFP")
TightMuSF_2016postVFP_stat = lambda : lepSFProducer("TightWP_2016postVFP")
LooseMuSF_2016postVFP_stat =  lambda : lepSFProducer("LooseWP_2016postVFP")
TightIsoMuSF_2016postVFP_stat = lambda : lepSFProducer("TightIsoWP_2016postVFP")
LooseIsoMuSF_2016postVFP_stat = lambda : lepSFProducer("IsoLooseWP_2016postVFP")


RECOMuSF_2016postVFP_syst = lambda : lepSFProducer("RECO_2016postVFP", err_tag = "syst")
TightMuSF_2016postVFP_syst = lambda : lepSFProducer("TightWP_2016postVFP", err_tag = "syst")
LooseMuSF_2016postVFP_syst =  lambda : lepSFProducer("LooseWP_2016postVFP", err_tag = "syst")
TightIsoMuSF_2016postVFP_syst = lambda : lepSFProducer("TightIsoWP_2016postVFP", err_tag = "syst")
LooseIsoMuSF_2016postVFP_syst = lambda : lepSFProducer("IsoLooseWP_2016postVFP", err_tag = "syst")

RECOElSF_2016postVFP = lambda : lepSFProducer("RECOEl_2016postVFP")
LooseElSF_2016postVFP =  lambda : lepSFProducer("NoIsoMVA90_2016postVFP")
TightIsoElSF_2016postVFP = lambda : lepSFProducer("IsoMVA80_2016postVFP")
LooseIsoElSF_2016postVFP = lambda : lepSFProducer("IsoMVA90_2016postVFP")


# 2017

RECOMuSF_2017_stat = lambda : lepSFProducer("RECO_2017")
TightMuSF_2017_stat = lambda : lepSFProducer("TightWP_2017")
LooseMuSF_2017_stat =  lambda : lepSFProducer("LooseWP_2017")
TightIsoMuSF_2017_stat = lambda : lepSFProducer("TightIsoWP_2017")
LooseIsoMuSF_2017_stat = lambda : lepSFProducer("IsoLooseWP_2017")


RECOMuSF_2017_syst = lambda : lepSFProducer("RECO_2017", err_tag = "syst")
TightMuSF_2017_syst = lambda : lepSFProducer("TightWP_2017", err_tag = "syst")
LooseMuSF_2017_syst =  lambda : lepSFProducer("LooseWP_2017", err_tag = "syst")
TightIsoMuSF_2017_syst = lambda : lepSFProducer("TightIsoWP_2017", err_tag = "syst")
LooseIsoMuSF_2017_syst = lambda : lepSFProducer("IsoLooseWP_2017", err_tag = "syst")

RECOElSF_2017 = lambda : lepSFProducer("RECOEl_2017")
LooseElSF_2017 =  lambda : lepSFProducer("NoIsoMVA90_2017")
TightIsoElSF_2017 = lambda : lepSFProducer("IsoMVA80_2017")
LooseIsoElSF_2017 = lambda : lepSFProducer("IsoMVA90_2017")


# 2018

RECOMuSF_2018_stat = lambda : lepSFProducer("RECO_2018")
TightMuSF_2018_stat = lambda : lepSFProducer("TightWP_2018")
LooseMuSF_2018_stat =  lambda : lepSFProducer("LooseWP_2018")
TightIsoMuSF_2018_stat = lambda : lepSFProducer("TightIsoWP_2018")
LooseIsoMuSF_2018_stat = lambda : lepSFProducer("IsoLooseWP_2018")


RECOMuSF_2018_syst = lambda : lepSFProducer("RECO_2018", err_tag = "syst")
TightMuSF_2018_syst = lambda : lepSFProducer("TightWP_2018", err_tag = "syst")
LooseMuSF_2018_syst =  lambda : lepSFProducer("LooseWP_2018", err_tag = "syst")
TightIsoMuSF_2018_syst = lambda : lepSFProducer("TightIsoWP_2018", err_tag = "syst")
LooseIsoMuSF_2018_syst = lambda : lepSFProducer("IsoLooseWP_2018", err_tag = "syst")

RECOElSF_2018 = lambda : lepSFProducer("RECOEl_2018")
LooseElSF_2018 =  lambda : lepSFProducer("NoIsoMVA90_2018")
TightIsoElSF_2018 = lambda : lepSFProducer("IsoMVA80_2018")
LooseIsoElSF_2018 = lambda : lepSFProducer("IsoMVA90_2018")



