#!/bin/env python
import os
##print(os.environ)
##print("**********************************************************************")
##print("**********************************************************************")
##print("**********************************************************************")
##print(str(os.environ.get('PYTHONPATH')))
##print(str(os.environ.get('PYTHON3PATH')))
import sys
##print("*************** This is system version info ***************************")
##print(sys.version_info)
#import platform
##print("*************** This is python version info ***************************")
##print(platform.python_version())
import ROOT
##print("Succesfully imported ROOT")
import math
import datetime
import copy
from array import array
from skimtree_utils import *
from tools import *
print("ok \n")
import xgboost as xgb
import numpy as np
from training_MultiClass import *
from samples.samples import *

print("all import are ok \n")

if sys.argv[5] == None: training = training_dict["BDT_Tprime"]
else: training = training_dict[sys.argv[5]]

sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))

MCReco = True
DeltaFilter = True
bjetSwitch = False # True #
startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

#leadingjet_ptcut = 150.
outTreeFile = ROOT.TFile(str(sys.argv[4])+"/"+sample.label+"_part"+str(part_idx)+".root", "RECREATE")
chain = ROOT.TChain('Events')
#outTreeFile = ROOT.TFile(str(sys.argv[4])+"/"+sample.label+"_part"+str(part_idx)+".root", "RECREATE") # output file
for infile in file_list: 
    print("Adding %s to the chain" %(infile))
    chain.Add(infile)
print("Number of events in chain " + str(chain.GetEntries()))
print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
tree = InputTree(chain)
isMC = True
scenarios = ["nominal", "jesUp", "jesDown", "jerUp", "jerDown"] 
if ('Data' in sample.label):
    isMC = False
    scenarios = ["nominal"]
MCReco = MCReco * isMC

#++++++++++++++++++++++++++++++++++
#++   branching the new trees    ++
#++++++++++++++++++++++++++++++++++

trees = []
for i in range(10):
    trees.append(None)
#systZero = systWeights()
# defining the operations to be done with the systWeights class
maxSysts = 0
addPDF = True
addQ2 = False
addTopPt = False
addVHF = False
addTTSplit = False
addTopTagging = False
addWTagging = False
addTrigSF = False
nPDF = 0

systTree = systWeights()
systTree.prepareDefault(True, addQ2, addPDF, addTopPt, addVHF, addTTSplit)

for scenario in scenarios:
    systTree.addSelection(scenario)

systTree.initTreesSysts(trees, outTreeFile)

systTree.setWeightName("w_nominal",1.)
systTree.setWeightName("w_pt",1.)
systTree.setWeightName("LHESF", 1.)
systTree.setWeightName("LHEUp", 1.)
systTree.setWeightName("LHEDown", 1.)
systTree.setWeightName("puSF",1.)
systTree.setWeightName("puUp",1.)
systTree.setWeightName("puDown",1.)
systTree.setWeightName("lepSF",1.)
systTree.setWeightName("lepUp",1.)
systTree.setWeightName("lepDown",1.)
systTree.setWeightName("trigSF",1.)
systTree.setWeightName("trigUp",1.)
systTree.setWeightName("trigDown",1.)
systTree.setWeightName("PFSF",1.)
systTree.setWeightName("PFUp",1.)
systTree.setWeightName("PFDown",1.)
systTree.setWeightName("btagSF",1.)
systTree.setWeightName("btagUp",1.)
systTree.setWeightName("btagDown",1.)
systTree.setWeightName("mistagUp",1.)
systTree.setWeightName("mistagDown",1.)
systTree.setWeightName("pdf_totalUp", 1.)
systTree.setWeightName("pdf_totalDown", 1.)
systTree.setWeightName("ParNetSF", 1.)
systTree.setWeightName("ParNetUp", 1.)
systTree.setWeightName("ParNetDown", 1.)
systTree.setWeightName("BDTSF", 1.)
systTree.setWeightName("BDTUp", 1.)
systTree.setWeightName("BDTDown", 1.)

h_cutFlow = ROOT.TH1D("h_cutFlow","h_cutFlow",11,-0.5,10.5)

h_nTop_type_wp99 = ROOT.TH2D("h_nTop_type_wp99","h_nTop_type_wp99",9,0.5,9.5,7,0.5,7.5)
h_nTop_type_wp90 = ROOT.TH2D("h_nTop_type_wp90","h_nTop_type_wp90",9,0.5,9.5,7,0.5,7.5)

def reco(scenario, isMC, addPDF, training):
    isNominal = False
    if scenario == 'nominal':
        isNominal = True
    print(scenario)
    BDTSF_nominal = array.array('f',[1.])
    BDTUp_nominal = array.array('f',[1.])
    BDTDown_nominal = array.array('f',[1.])

    ParNetSF_nominal = array.array('f',[1.])
    ParNetUp_nominal = array.array('f',[1.])
    ParNetDown_nominal = array.array('f',[1.])



    w_PDF_nominal = array.array('f',[0.])
    w_pt_nominal = array.array('f',[1.])
    w_nominal_nominal = array.array('f', [0.])
    HLT_Muon_nominal = array.array('f',[0.])
    HLT_Electron_nominal = array.array('f',[0.])
    HLT_Photon_nominal = array.array('f',[0.])
    HLT_PFJet_nominal = array.array('f',[0.])

    AK8_region_nominal = array.array('i',[0])
    top_region_nominal = array.array('i',[0])
    Fwd_region_nominal = array.array('i',[0])
    Fwd4_region_nominal = array.array('i',[0])
    N_top_nominal = array.array('i',[0])
    N_AK8_nominal = array.array('i',[0])

    N_muTop_nominal = array.array('i',[0])
    N_muVeryLoose_nominal = array.array('i',[0])
    N_muLoose_nominal = array.array('i',[0])

    N_elTop_nominal = array.array('i',[0])
    N_elVeryLoose_nominal = array.array('i',[0])
    N_elLoose_nominal = array.array('i',[0])

    N_bjet_nominal = array.array('i',[0])
    dR_bjet_AK8_nominal = array.array('f',[0.])
    M_bjet_AK8_nominal = array.array('f',[0.])
    N_jet_nominal = array.array('i',[0])
    dR_jet_AK8_nominal = array.array('f',[0.])

    MET_nominal= array.array('f',[0.])
    MET_phi_nominal= array.array('f',[0.])

    Top_pt_nominal = array.array('f',[0.]) 
    Top_eta_nominal = array.array('f',[0.]) 
    Top_phi_nominal = array.array('f',[0.]) 
    Top_M_nominal = array.array('f',[0.]) 
    Top_Score0_nominal = array.array('f',[0.])
    Top_Score1_nominal = array.array('f',[0.]) 
    Top_Score2_nominal = array.array('f',[0.])
    Top_TvsQCD_nominal = array.array('f',[0.])
    Top_TvsOth_nominal = array.array('f',[0.])
    Top_MC_nominal = array.array('i',[0])
    Top_flavour_nominal = array.array('i',[0]) #if isMC:
    Top_isMerg_nominal = array.array('f',[0.])
    
    Top_LepIdx_nominal = array.array('i',[0])
    Top_JetIdx_nominal = array.array('i',[0])

    SecTop_LepIdx_nominal = array.array('i',[0])
    SecTop_JetIdx_nominal = array.array('i',[0])

    SecTop_MC_nominal = array.array('i',[0])
    SecTop_flavour_nominal = array.array('i',[0]) 
    SecTop_isMerg_nominal = array.array('f',[0.])

    FatJet_pt_nominal = array.array('f',[0.])
    FatJet_eta_nominal = array.array('f',[0.])
    FatJet_phi_nominal = array.array('f',[0.])
    FatJet_M_nominal = array.array('f',[0.])
    FatJet_MC_nominal = array.array('f',[0.])
    FatJet_dRMC_nominal = array.array('f',[0.])
    FatJet_btagDeepB_nominal = array.array('f',[0.])
    FatJet_tau1_nominal = array.array('f',[0.])
    FatJet_tau2_nominal = array.array('f',[0.])

    FwdJet_pt_nominal = array.array('f',[0.])
    FwdJet_eta_nominal = array.array('f',[0.])
    FwdJet_phi_nominal = array.array('f',[0.])
    FwdJet_M_nominal = array.array('f',[0.])
    FwdJet_btag_nominal = array.array('f',[0.])    

    Tprime_pt_nominal = array.array('f',[0.])
    Tprime_eta_nominal = array.array('f',[0.])
    Tprime_phi_nominal = array.array('f',[0.])
    Tprime_M_nominal = array.array('f',[0.])


    Lep_dxy_nominal = array.array('f',[0.])
    Lep_dxyerr_nominal = array.array('f',[0.])
    Lep_dz_nominal = array.array('f',[0.])
    Lep_dzerr_nominal = array.array('f',[0.])
    Lep_Iso_nominal = array.array('f',[0.])
    Lep_MiniIso_nominal = array.array('f',[0.])
    Lep_pt_nominal = array.array('f',[0.])
    Lep_eta_nominal = array.array('f',[0.])
    Lep_phi_nominal = array.array('f',[0.])
    Lep_M_nominal = array.array('f',[0.])
    Lep_Id_nominal = array.array('f',[0.])

    Jet_pt_nominal = array.array('f',[0.])
    Jet_eta_nominal = array.array('f',[0.])
    Jet_phi_nominal = array.array('f',[0.])
    Jet_M_nominal = array.array('f',[0.])
    Jet_btag_nominal = array.array('f',[0.]) 
    FatJet_Xbb_nominal=array.array('f',[0.])
    FatJet_XbbVsQCD_nominal=array.array('f',[0.]) 
    Tprime_dR_nominal = array.array('f',[0.]) 

    othbJet_pt_nominal = array.array('f',[0.])
    othbJet_eta_nominal = array.array('f',[0.])
    othbJet_phi_nominal = array.array('f',[0.])
    othbJet_M_nominal = array.array('f',[0.])
    othbJet_btag_nominal = array.array('f',[0.])

    TightMu_dxy_nominal = array.array('f',[0.])
    TightMu_dxyerr_nominal = array.array('f',[0.])
    TightMu_dz_nominal = array.array('f',[0.])
    TightMu_dzerr_nominal = array.array('f',[0.])
    TightMu_Iso_nominal = array.array('f',[0.])
    TightMu_MiniIso_nominal = array.array('f',[0.])
    TightMu_pt_nominal = array.array('f',[0.])
    TightMu_eta_nominal = array.array('f',[0.])
    TightMu_phi_nominal = array.array('f',[0.])
    TightMu_M_nominal = array.array('f',[0.])
    TightMu_Id_nominal = array.array('f',[0.])

    TightEl_dxy_nominal = array.array('f',[0.])
    TightEl_dxyerr_nominal = array.array('f',[0.])
    TightEl_dz_nominal = array.array('f',[0.])
    TightEl_dzerr_nominal = array.array('f',[0.])
    TightEl_Iso_nominal = array.array('f',[0.])
    TightEl_MiniIso_nominal = array.array('f',[0.])
    TightEl_pt_nominal = array.array('f',[0.])
    TightEl_eta_nominal = array.array('f',[0.])
    TightEl_phi_nominal = array.array('f',[0.])
    TightEl_M_nominal = array.array('f',[0.])
    TightEl_Id_nominal = array.array('f',[0.])



    systTree.branchTreesSysts(trees, scenario,"FatJet_Xbb_nominal",outTreeFile, FatJet_Xbb_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_btagDeepB_nominal",outTreeFile, FatJet_btagDeepB_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_tau1_nominal",outTreeFile, FatJet_tau1_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_tau2_nominal",outTreeFile, FatJet_tau2_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_XbbVsQCD_nominal",outTreeFile, FatJet_XbbVsQCD_nominal)
    systTree.branchTreesSysts(trees, scenario,"Tprime_dR_nominal",outTreeFile, Tprime_dR_nominal)
        
    systTree.branchTreesSysts(trees, scenario,"MET_nominal",outTreeFile, MET_nominal)
    systTree.branchTreesSysts(trees, scenario,"MET_phi_nominal",outTreeFile, MET_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_Muon_nominal", outTreeFile, HLT_Muon_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_Electron_nominal", outTreeFile, HLT_Electron_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_Photon_nominal", outTreeFile, HLT_Photon_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_PFJet_nominal", outTreeFile, HLT_PFJet_nominal)
    systTree.branchTreesSysts(trees, scenario,"AK8_region_nominal", outTreeFile, AK8_region_nominal)
    systTree.branchTreesSysts(trees, scenario,"top_region_nominal", outTreeFile, top_region_nominal)
    systTree.branchTreesSysts(trees, scenario,"Fwd_region_nominal", outTreeFile, Fwd_region_nominal)
    systTree.branchTreesSysts(trees, scenario,"Fwd4_region_nominal", outTreeFile, Fwd4_region_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_pt_nominal", outTreeFile, Top_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_eta_nominal", outTreeFile, Top_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_phi_nominal", outTreeFile, Top_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_M_nominal", outTreeFile, Top_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_Score0_nominal", outTreeFile, Top_Score0_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_Score1_nominal", outTreeFile, Top_Score1_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_Score2_nominal", outTreeFile, Top_Score2_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_TvsQCD_nominal", outTreeFile, Top_TvsQCD_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_TvsOth_nominal", outTreeFile, Top_TvsOth_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC_nominal", outTreeFile, Top_MC_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour_nominal", outTreeFile, Top_flavour_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg_nominal", outTreeFile, Top_isMerg_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_pt_nominal", outTreeFile, FatJet_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_eta_nominal", outTreeFile, FatJet_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_phi_nominal", outTreeFile, FatJet_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_M_nominal", outTreeFile, FatJet_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_MC_nominal", outTreeFile, FatJet_MC_nominal)
    systTree.branchTreesSysts(trees, scenario,"FatJet_dRMC_nominal", outTreeFile, FatJet_dRMC_nominal)
    systTree.branchTreesSysts(trees, scenario,"FwdJet_pt_nominal", outTreeFile, FwdJet_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"FwdJet_eta_nominal", outTreeFile, FwdJet_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"FwdJet_phi_nominal", outTreeFile, FwdJet_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"FwdJet_M_nominal", outTreeFile, FwdJet_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"FwdJet_btag_nominal", outTreeFile, FwdJet_btag_nominal)
    systTree.branchTreesSysts(trees, scenario,"Tprime_pt_nominal", outTreeFile, Tprime_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"Tprime_eta_nominal", outTreeFile, Tprime_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"Tprime_phi_nominal", outTreeFile, Tprime_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"Tprime_M_nominal", outTreeFile, Tprime_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_dxy_nominal", outTreeFile, Lep_dxy_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_dxyerr_nominal", outTreeFile, Lep_dxyerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_dz_nominal", outTreeFile, Lep_dz_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_dzerr_nominal", outTreeFile, Lep_dzerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_Iso_nominal", outTreeFile, Lep_Iso_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_MiniIso_nominal", outTreeFile, Lep_MiniIso_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_pt_nominal", outTreeFile, Lep_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_eta_nominal", outTreeFile, Lep_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_phi_nominal", outTreeFile, Lep_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_M_nominal", outTreeFile, Lep_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"Lep_Id_nominal", outTreeFile, Lep_Id_nominal)
    systTree.branchTreesSysts(trees, scenario,"Jet_pt_nominal", outTreeFile, Jet_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"Jet_eta_nominal", outTreeFile, Jet_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"Jet_phi_nominal", outTreeFile, Jet_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"Jet_M_nominal", outTreeFile, Jet_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"Jet_btag_nominal", outTreeFile, Jet_btag_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_bjet_nominal", outTreeFile, N_bjet_nominal)
    systTree.branchTreesSysts(trees, scenario,"dR_bjet_AK8_nominal", outTreeFile, dR_bjet_AK8_nominal)
    systTree.branchTreesSysts(trees, scenario,"M_bjet_AK8_nominal", outTreeFile, M_bjet_AK8_nominal)


    systTree.branchTreesSysts(trees, scenario,"othbJet_pt_nominal", outTreeFile, othbJet_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"othbJet_eta_nominal", outTreeFile, othbJet_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"othbJet_phi_nominal", outTreeFile, othbJet_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"othbJet_M_nominal", outTreeFile, othbJet_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"othbJet_btag_nominal", outTreeFile, othbJet_btag_nominal)

    systTree.branchTreesSysts(trees, scenario,"N_jet_nominal", outTreeFile,N_jet_nominal)
    systTree.branchTreesSysts(trees, scenario,"dR_jet_AK8_nominal", outTreeFile, dR_jet_AK8_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_top_nominal", outTreeFile,N_top_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_AK8_nominal", outTreeFile,N_AK8_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_LepIdx_nominal", outTreeFile,Top_LepIdx_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_JetIdx_nominal", outTreeFile,Top_JetIdx_nominal)
    systTree.branchTreesSysts(trees, scenario,"SecTop_LepIdx_nominal", outTreeFile,SecTop_LepIdx_nominal) 
    systTree.branchTreesSysts(trees, scenario,"SecTop_JetIdx_nominal", outTreeFile,SecTop_JetIdx_nominal) 

    systTree.branchTreesSysts(trees, scenario,"SecTop_MC_nominal", outTreeFile,SecTop_MC_nominal) 
    systTree.branchTreesSysts(trees, scenario,"SecTop_flavour_nominal", outTreeFile,SecTop_flavour_nominal)
    systTree.branchTreesSysts(trees, scenario,"SecTop_isMerg_nominal", outTreeFile, SecTop_isMerg_nominal)

    systTree.branchTreesSysts(trees, scenario,"N_muTop_nominal", outTreeFile,N_muTop_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_muVeryLoose_nominal", outTreeFile,N_muVeryLoose_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_muLoose_nominal", outTreeFile,N_muLoose_nominal)


    systTree.branchTreesSysts(trees, scenario,"N_elTop_nominal", outTreeFile,N_elTop_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_elVeryLoose_nominal", outTreeFile,N_elVeryLoose_nominal)
    systTree.branchTreesSysts(trees, scenario,"N_elLoose_nominal", outTreeFile,N_elLoose_nominal)

    systTree.branchTreesSysts(trees, scenario,"TightMu_dxy_nominal", outTreeFile, TightMu_dxy_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_dxyerr_nominal", outTreeFile, TightMu_dxyerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_dz_nominal", outTreeFile, TightMu_dz_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_dzerr_nominal", outTreeFile, TightMu_dzerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_Iso_nominal", outTreeFile, TightMu_Iso_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_MiniIso_nominal", outTreeFile, TightMu_MiniIso_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_pt_nominal", outTreeFile, TightMu_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_eta_nominal", outTreeFile, TightMu_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_phi_nominal", outTreeFile, TightMu_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_M_nominal", outTreeFile, TightMu_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightMu_Id_nominal", outTreeFile, TightMu_Id_nominal)

    systTree.branchTreesSysts(trees, scenario,"TightEl_dxy_nominal", outTreeFile, TightEl_dxy_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_dxyerr_nominal", outTreeFile, TightEl_dxyerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_dz_nominal", outTreeFile, TightEl_dz_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_dzerr_nominal", outTreeFile, TightEl_dzerr_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_Iso_nominal", outTreeFile, TightEl_Iso_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_MiniIso_nominal", outTreeFile, TightEl_MiniIso_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_pt_nominal", outTreeFile, TightEl_pt_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_eta_nominal", outTreeFile, TightEl_eta_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_phi_nominal", outTreeFile, TightEl_phi_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_M_nominal", outTreeFile, TightEl_M_nominal)
    systTree.branchTreesSysts(trees, scenario,"TightEl_Id_nominal", outTreeFile, TightEl_Id_nominal)

    if(isMC and addPDF):
        systTree.branchTreesSysts(trees, scenario, "w_PDF", outTreeFile, w_PDF_nominal)

    ################################################################################################################################################################################################################################
    
    #++++++++++++++++++++++++++++++++++
    #++      taking MC weights       ++
    #++++++++++++++++++++++++++++++++++
    # This part of the code takes care of collecting the MC weight for the correct normalization of the MC samples and for the production of the PDF weights variations
    
    print("isMC: ", isMC)
    pdf_xsweight = 1.
    pdf_weight_sum = 0.
    isMC__ = False
    print("Attention isMC always setted false!!!!")
    if(isMC):
        h_genweight = ROOT.TH1F()
        h_genweight.SetNameTitle('h_genweight', 'h_genweight')
        h_PDFweight = ROOT.TH1F()
        h_PDFweight.SetNameTitle("h_PDFweight","h_PDFweight")
        for infile in file_list: 
            newfile = ROOT.TFile.Open(infile)
            dirc = ROOT.TDirectory()
            dirc = newfile.Get("plots")
            h_genw_tmp = ROOT.TH1F(dirc.Get("h_genweight"))
            if(dirc.GetListOfKeys().Contains("h_PDFweight")):
                h_pdfw_tmp = ROOT.TH1F(dirc.Get("h_PDFweight"))
                if(ROOT.TH1F(h_PDFweight).Integral() < 1.):
                    for i in range(1, h_pdfw_tmp.GetXaxis().GetNbins()+1):
                        pdf_weight_sum += h_pdfw_tmp.GetBinContent(i)
                    pdf_weight_sum /= h_pdfw_tmp.GetXaxis().GetNbins()
                    print(pdf_weight_sum)
                    h_PDFweight.SetBins(h_pdfw_tmp.GetXaxis().GetNbins(), h_pdfw_tmp.GetXaxis().GetXmin(), h_pdfw_tmp.GetXaxis().GetXmax())
                    print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(ROOT.TH1F(dirc.Get("h_genweight")).GetBinContent(1), ROOT.TH1F(dirc.Get("h_PDFweight")).GetNbinsX()))
                h_PDFweight.Add(h_pdfw_tmp)
            else:
                addPDF = False
            if(ROOT.TH1F(h_genweight).Integral() < 1.):
                h_genweight.SetBins(h_genw_tmp.GetXaxis().GetNbins(), h_genw_tmp.GetXaxis().GetXmin(), h_genw_tmp.GetXaxis().GetXmax())
            h_genweight.Add(h_genw_tmp)
        print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genweight.GetBinContent(1), h_PDFweight.GetNbinsX()))
        lheweight = h_genweight.GetBinContent(2)/h_genweight.GetBinContent(1)
        pdf_xsweight = pdf_weight_sum/h_genweight.GetBinContent(1)
        h_cutFlow.SetBinContent(1,h_genweight.GetBinContent(1))
        h_cutFlow.SetBinError(1,h_genweight.GetBinError(1))
        h_cutFlow.GetXaxis().SetBinLabel(1,"SumEvents")
        h_cutFlow.GetXaxis().SetBinLabel(2,"HLT_PresEvents")
        h_cutFlow.GetXaxis().SetBinLabel(3,"AK8 Tight 100<M<140")
        h_cutFlow.GetXaxis().SetBinLabel(4,"No LooseLep and Best TvsQCD>0.6")
        h_cutFlow.GetXaxis().SetBinLabel(5,"Best Top Loose")
        h_cutFlow.GetXaxis().SetBinLabel(6,"Best Top Loose Fwd0")
        h_cutFlow.GetXaxis().SetBinLabel(7,"Best Top Loose Fwd1")
        h_cutFlow.GetXaxis().SetBinLabel(8,"Best Top Tight")
        h_cutFlow.GetXaxis().SetBinLabel(9,"Best Top Tight Fwd0")
        h_cutFlow.GetXaxis().SetBinLabel(10,"Best Top Tight Fwd1")
        

        

    print(tree.GetEntries())
    for i in range(tree.GetEntries()):
        AK8_region_nominal[0]=0        
        top_region_nominal[0]=0        
        Fwd_region_nominal[0]=0        
        Fwd4_region_nominal[0]=0        
        N_top_nominal[0]=0        
        N_AK8_nominal[0]=0
        N_muTop_nominal[0]=0        
        N_muVeryLoose_nominal[0]=0        
        N_muLoose_nominal[0]=0
        N_elTop_nominal[0]=0        
        N_elVeryLoose_nominal[0]=0        
        N_elLoose_nominal[0]=0
        N_bjet_nominal[0]=0        
        dR_bjet_AK8_nominal[0]=0
        M_bjet_AK8_nominal[0]=0
        N_jet_nominal[0]=0        
        dR_jet_AK8_nominal[0]=0

        MET_nominal[0]=0
        MET_phi_nominal[0]=0

        Top_pt_nominal[0]=0 
        Top_eta_nominal[0]=0 
        Top_phi_nominal[0]=0 
        Top_M_nominal[0]=0 
        Top_Score0_nominal[0]=0
        Top_Score1_nominal[0]=0 
        Top_Score2_nominal[0]=0
        Top_TvsQCD_nominal[0]=0
        Top_TvsOth_nominal[0]=0
        Top_MC_nominal[0]=0        
        Top_flavour_nominal[0]=0#if isMC:
        Top_isMerg_nominal[0]=0
        
        Top_LepIdx_nominal[0]=0        
        Top_JetIdx_nominal[0]=0
        SecTop_LepIdx_nominal[0]=0        
        SecTop_JetIdx_nominal[0]=0
        SecTop_MC_nominal[0]=0        
        SecTop_flavour_nominal[0]=0
        SecTop_isMerg_nominal[0]=0

        FatJet_pt_nominal[0]=0
        FatJet_eta_nominal[0]=0
        FatJet_phi_nominal[0]=0
        FatJet_M_nominal[0]=0
        FatJet_MC_nominal[0]=0
        FatJet_dRMC_nominal[0]=0
        FatJet_btagDeepB_nominal[0]=0
        FatJet_tau1_nominal[0]=0
        FatJet_tau2_nominal[0]=0

        FwdJet_pt_nominal[0]=0
        FwdJet_eta_nominal[0]=0
        FwdJet_phi_nominal[0]=0
        FwdJet_M_nominal[0]=0
        FwdJet_btag_nominal[0]=0    

        Tprime_pt_nominal[0]=0
        Tprime_eta_nominal[0]=0
        Tprime_phi_nominal[0]=0
        Tprime_M_nominal[0]=0


        Lep_dxy_nominal[0]=0
        Lep_dxyerr_nominal[0]=0
        Lep_dz_nominal[0]=0
        Lep_dzerr_nominal[0]=0
        Lep_Iso_nominal[0]=0
        Lep_MiniIso_nominal[0]=0
        Lep_pt_nominal[0]=0
        Lep_eta_nominal[0]=0
        Lep_phi_nominal[0]=0
        Lep_M_nominal[0]=0
        Lep_Id_nominal[0]=0

        Jet_pt_nominal[0]=0
        Jet_eta_nominal[0]=0
        Jet_phi_nominal[0]=0
        Jet_M_nominal[0]=0
        Jet_btag_nominal[0]=0 
        FatJet_Xbb_nominal[0]=0        
        FatJet_XbbVsQCD_nominal[0]=0
        Tprime_dR_nominal[0]=0 

        othbJet_pt_nominal[0]=0
        othbJet_eta_nominal[0]=0
        othbJet_phi_nominal[0]=0
        othbJet_M_nominal[0]=0
        othbJet_btag_nominal[0]=0

        TightMu_dxy_nominal[0]=0
        TightMu_dxyerr_nominal[0]=0
        TightMu_dz_nominal[0]=0
        TightMu_dzerr_nominal[0]=0
        TightMu_Iso_nominal[0]=0
        TightMu_MiniIso_nominal[0]=0
        TightMu_pt_nominal[0]=0
        TightMu_eta_nominal[0]=0
        TightMu_phi_nominal[0]=0
        TightMu_M_nominal[0]=0
        TightMu_Id_nominal[0]=0

        TightEl_dxy_nominal[0]=0
        TightEl_dxyerr_nominal[0]=0
        TightEl_dz_nominal[0]=0
        TightEl_dzerr_nominal[0]=0
        TightEl_Iso_nominal[0]=0
        TightEl_MiniIso_nominal[0]=0
        TightEl_pt_nominal[0]=0
        TightEl_eta_nominal[0]=0
        TightEl_phi_nominal[0]=0
        TightEl_M_nominal[0]=0
        TightEl_Id_nominal[0]=0

        w_PDF_nominal[0]=1.
        HLT_Muon_nominal[0] = 0.
        HLT_Electron_nominal[0] = 0.
        HLT_Photon_nominal[0] = 0.
        HLT_PFJet_nominal[0] = 0.
        w_nominal_nominal[0]=1.
        w_pt_nominal[0]=1.
        BDTSF_nominal[0]=1.
        BDTUp_nominal[0]=1.
        BDTDown_nominal[0]=1.

        ParNetSF_nominal[0]=1.
        ParNetUp_nominal[0]=1.
        ParNetDown_nominal[0]=1.


        event = Event(tree,i) 
        
        if ("TT" in sample.label): 
            genpart = Collection(event,"GenPart")
            top = list(filter(lambda x: x.pdgId==6 ,genpart))[0]
            antitop = list(filter(lambda x: x.pdgId==-6 ,genpart))[0]
            Mtt = (top.p4() + antitop.p4()).M()
            SF_t = 0.973-0.000134*top.pt+0.103*math.exp(-0.0118*top.pt)
            SF_antit = 0.973-0.000134*antitop.pt+0.103*math.exp(-0.0118*antitop.pt)
            w_pt_nominal[0]=math.sqrt(SF_t*SF_antit)
            if (Mtt>=700) and (not "Mtt" in sample.label):
                print(Mtt)
                continue
        
        jets = Collection(event, "Jet")            
        tops = Collection(event,"Top")
        met = Object(event, "MET")
        electron = Collection(event, "Electron")
        muon = Collection(event, "Muon")
        nelectron = len(electron)
        nmuon = len(muon)
        ntop = len(tops)
        #print(ntop)
        #for top in tops:
        #    print(top.el_index, top.mu_index, top.nu_pt, top.Is_dR_merg, top.TvsQCD, top.TvsOth, top.Score0, top.Score1, top.Score2)
        #for top_idx, top in enumerate(tops): print(top.nu_pt, top_idx)

        fatjets = Collection(event,"FatJet")
        loosefatjets = Collection(event,"LooseFatJet")
        h_cutFlow.Fill("HLT_PresEvents",1)
        HLT = Object(event,"HLT")

        HLT_Muon_nominal[0] = HLT.Mu50 or HLT.IsoMu24
        if sample.year== 2016: HLT_PFJet_nominal[0] = HLT.AK8PFJet360_TrimMass30
        if sample.year== 2017: HLT_PFJet_nominal[0] = HLT.AK8PFJet500
        if sample.year== 2018: HLT_PFJet_nominal[0] = HLT.AK8PFJet400_TrimMass30

        if sample.year== 2016:
            HLT_Electron_nominal[0] = HLT.Ele27_WPTight_Gsf 
            HLT_Photon_nominal[0] = HLT.Photon175 
        else:
            HLT_Electron_nominal[0] = HLT.Ele32_WPTight_Gsf 
            HLT_Photon_nominal[0] = HLT.Photon200

        if(HLT_Muon_nominal[0]==0 and HLT_PFJet_nominal[0]==0 and HLT_Photon_nominal[0]==0 and HLT_Electron_nominal[0]==0): continue

        if(isMC):
            doublecounting = False
        else:
            doublecounting = True
        #Double counting removal
        if('DataMu' in sample.label and HLT_Muon_nominal[0]):
            doublecounting = False
        if('DataEle'  in sample.label and (not HLT_Muon_nominal[0] and HLT_Electron_nominal[0] )):
            doublecounting = False

        if('DataPh'  in sample.label and (not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0] and HLT_Photon_nominal[0]) and sample.year!=2018):
            doublecounting = False

        if('DataEle'  in sample.label and (not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0] and HLT_Photon_nominal[0]) and sample.year==2018):
            doublecounting = False

        if('DataHT' in sample.label and (HLT_PFJet_nominal[0] and not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0]  and not HLT_Photon_nominal[0])):
            doublecounting = False
                
        if doublecounting:
            continue


        fwdjets = list(filter(lambda x: abs(x.eta)>2.4 and x.pt>30 and (x.jetId==2 or x.jetId==3 or x.jetId==6 or x.jetId==7),jets))
        fwdjets4 = list(filter(lambda x: abs(x.eta)>2.4 and x.pt>30 and (x.jetId==2 or x.jetId==3 or x.jetId==6 or x.jetId==7) and abs(x.eta)<4,jets))
        if len(fwdjets)>0:
            Fwd_region_nominal[0]=1
            FwdJet_pt_nominal[0]=fwdjets[0].pt
            FwdJet_eta_nominal[0]=fwdjets[0].eta
            FwdJet_phi_nominal[0]=fwdjets[0].phi
            FwdJet_M_nominal[0]=fwdjets[0].mass
            FwdJet_btag_nominal[0] =fwdjets[0].btagDeepFlavB
        else:
            Fwd_region_nominal[0]=0
            FwdJet_pt_nominal[0]= -999.
            FwdJet_eta_nominal[0]= -999.
            FwdJet_phi_nominal[0]= -999.
            FwdJet_M_nominal[0]= -999.
            FwdJet_btag_nominal[0] = -999.
            
        if len(fwdjets4)>0:
            Fwd4_region_nominal[0]=1
            #FwdJet_pt_nominal[0]=fwdjets[0].pt
            #FwdJet_eta_nominal[0]=fwdjets[0].eta
            #FwdJet_phi_nominal[0]=fwdjets[0].phi
            #FwdJet_M_nominal[0]=fwdjets[0].mass
            #FwdJet_btag_nominal[0] =fwdjets[0].btagDeepFlavB
        else:
            Fwd4_region_nominal[0]=0
            #FwdJet_pt_nominal[0]= -999.
            #FwdJet_eta_nominal[0]= -999.
            #FwdJet_phi_nominal[0]= -999.
            #FwdJet_M_nominal[0]= -999.
            #FwdJet_btag_nominal[0] = -999.

        if i%100 == 0:
            print("Processed ", i+1, " out of ", tree.GetEntries(), " events")

        chain.GetEntry(i) #this is needed for branches that are not compatible with the NANOAOD convention (e.g. )
        print("Don't forget to change msdoftdrop from new JEC correction, _nom, ecc")
        if scenario == 'jesUp':
            MET = {'metPx': met.pt_jesTotalUp*ROOT.TMath.Cos(met.phi_jesTotalUp), 'metPy': met.pt_jesTotalUp*ROOT.TMath.Sin(met.phi_jesTotalUp)}
            for jet in jets:
                jet.pt = jet.pt_jesTotalUp
                jet.mass = jet.mass_jesTotalUp 
            for fatjet in fatjets:
                fatjet.pt = fatjet.pt_jesTotalUp
                fatjet.mass = fatjet.mass_jesTotalUp 
                fatjet.msoftdrop = fatjet.msoftdrop_jesTotalUp
        elif scenario == 'jesDown':
            MET = {'metPx': met.pt_jesTotalDown*ROOT.TMath.Cos(met.phi_jesTotalDown), 'metPy': met.pt_jesTotalDown*ROOT.TMath.Sin(met.phi_jesTotalDown)}
            for jet in jets:
                jet.pt = jet.pt_jesTotalDown
                jet.mass = jet.mass_jesTotalDown 
            for fatjet in fatjets:
                fatjet.pt = fatjet.pt_jesTotalDown
                fatjet.mass = fatjet.mass_jesTotalDown 
                fatjet.msoftdrop = fatjet.msoftdrop_jesTotalDown
        elif scenario == 'jerUp':
            MET = {'metPx': met.pt_jerUp*ROOT.TMath.Cos(met.phi_jerUp), 'metPy': met.pt_jerUp*ROOT.TMath.Sin(met.phi_jerUp)}
            for jet in jets:
                jet.pt = jet.pt_jerUp
                jet.mass = jet.mass_jerUp 
            for fatjet in fatjets:
                fatjet.pt = fatjet.pt_jerUp
                fatjet.mass = fatjet.mass_jerUp 
                fatjet.msoftdrop = fatjet.msoftdrop_jerUp
        elif scenario == 'jerDown':
            MET = {'metPx': met.pt_jerDown*ROOT.TMath.Cos(met.phi_jerDown), 'metPy': met.pt_jerDown*ROOT.TMath.Sin(met.phi_jerDown)}
            for jet in jets:
                jet.pt = jet.pt_jerDown
                jet.mass = jet.mass_jerDown 
            for fatjet in fatjets:
                fatjet.pt = fatjet.pt_jerDown
                fatjet.mass = fatjet.mass_jerDown 
                fatjet.msoftdrop = fatjet.msoftdrop_jerDown
        
        # this part take care of writing the variations of the MC weight relative to the LHE scale and the PDFs variations
        PU_SF=None
        PU_SFUp=None
        PU_SFDown=None
        MET_nominal[0]=met.pt 
        MET_phi_nominal[0]=met.phi
        if(isMC):
            runPeriod=None
        else:
            runPeriod=sample.runP

        passesMETHEMVeto = HEMveto(jets, electron)
        if(sample.year == 2018 and not passesMETHEMVeto):
            if(not isMC and chain.run > 319077.):
                continue
            elif(isMC):
                w_nominal_nominal[0] *= 0.354


        
        if(isMC):
            if not sample.year == 2018:
                PF_SF = chain.PrefireWeight
                PF_SFUp = chain.PrefireWeight_Up
                PF_SFDown = chain.PrefireWeight_Down
                systTree.setWeightName("PFSF", copy.deepcopy(PF_SF))
                systTree.setWeightName("PFUp", copy.deepcopy(PF_SFUp))
                systTree.setWeightName("PFDown", copy.deepcopy(PF_SFDown))

            PU_SF = chain.puWeight
            PU_SFUp = chain.puWeightUp
            PU_SFDown = chain.puWeightDown
            systTree.setWeightName("puSF", copy.deepcopy(PU_SF))
            systTree.setWeightName("puUp", copy.deepcopy(PU_SFUp))
            systTree.setWeightName("puDown", copy.deepcopy(PU_SFDown))
        

        if isMC:
            genpart = Collection(event, "GenPart")
            LHE = Collection(event, "LHEPart")
            LHEScaleWeight = Collection(event, 'LHEScaleWeight')
            lheSF = 1.
            lheUp = 1.
            lheDown = 1.
            pdf_totalUp = 1.
            pdf_totalDown = 1.
            if scenario == 'nominal':
                if len(LHEScaleWeight) > 1:
                    lhemin = min([LHEScaleWeight[g].__getattr__("") for g in range(len(LHEScaleWeight))])
                    lhemax = max([LHEScaleWeight[g].__getattr__("") for g in range(len(LHEScaleWeight))])
                    lheSF = lheweight * LHEScaleWeight[4].__getattr__("")
                    lheUp = lheweight * lhemax
                    lheDown = lheweight * lhemin
                if addPDF:
                    LHEPdfWeight = Collection(event, 'LHEPdfWeight')
                    mean_pdf = 0.
                    rms = 0.
                    for pdfw, i in zip(LHEPdfWeight, range(1, len(LHEPdfWeight)+1)):
                        mean_pdf += pdfw.__getattr__("")
                    mean_pdf /= len(LHEPdfWeight)
                    #print(mean_pdf)
                    for pdfw, i in zip(LHEPdfWeight, range(1, len(LHEPdfWeight)+1)):
                        rms += (pdfw.__getattr__("")-mean_pdf)**2
                    rms = math.sqrt(rms/len(LHEPdfWeight))
                    #print(rms)
                    pdf_totalUp = (1+rms)*pdf_xsweight
                    pdf_totalDown = (1-rms)*pdf_xsweight
                    #print(pdf_totalUp, pdf_totalDown)
                systTree.setWeightName("pdf_totalUp", copy.deepcopy(pdf_totalUp))
                systTree.setWeightName("pdf_totalDown", copy.deepcopy(pdf_totalDown))
                systTree.setWeightName("LHESF", copy.deepcopy(lheSF))
                systTree.setWeightName("LHEUp", copy.deepcopy(lheUp))
                systTree.setWeightName("LHEDown", copy.deepcopy(lheDown))

        #tightMu = list(filter(lambda x : x.tightId and x.pt>30 , muon))
        #tightEle = list(filter(lambda x : x.cutBased==4 and x.pt>30, electron))

        tightMu = list(filter(lambda x : x.tightId and x.pt>30 , muon))
        tightEle = list(filter(lambda x : x.mvaFall17V2Iso_WP80 and x.pt>30, electron))

        if(len(tightEle)>0):
            TightEl_dxy_nominal [0] = tightEle[0].dxy 
            TightEl_dxyerr_nominal [0] = tightEle[0].dxyErr 
            TightEl_dz_nominal [0] = tightEle[0].dz 
            TightEl_dzerr_nominal [0] = tightEle[0].dzErr 
            TightEl_Iso_nominal [0] = tightEle[0].pfRelIso03_all
            TightEl_MiniIso_nominal [0] = tightEle[0].miniPFRelIso_all
            TightEl_pt_nominal [0] = tightEle[0].pt 
            TightEl_eta_nominal [0] = tightEle[0].eta 
            TightEl_phi_nominal [0] = tightEle[0].phi 
            TightEl_M_nominal [0] = tightEle[0].mass 
            TightEl_Id_nominal [0] = tightEle[0].cutBased
        if(len(tightMu)>0): 
            TightMu_dxy_nominal [0] = tightMu[0].dxy 
            TightMu_dxyerr_nominal [0] = tightMu[0].dxyErr 
            TightMu_dz_nominal [0] = tightMu[0].dz 
            TightMu_dzerr_nominal [0] = tightMu[0].dzErr 
            TightMu_Iso_nominal [0] = tightMu[0].pfRelIso04_all
            TightMu_MiniIso_nominal [0] = tightMu[0].miniPFRelIso_all
            TightMu_pt_nominal [0] = tightMu[0].pt 
            TightMu_eta_nominal [0] = tightMu[0].eta 
            TightMu_phi_nominal [0] = tightMu[0].phi 
            TightMu_M_nominal [0] = tightMu[0].mass 
            if tightMu[0].looseId: TightMu_Id_nominal [0] = 1+int(tightMu[0].looseId)+int(tightMu[0].mediumId)+int(tightMu[0].tightId)
            else: TightMu_Id_nominal [0] = 0
 
        all_coll=[]
        all_coll_wp90=[]
        all_coll_wp99=[]

    
        k=0
        for train in training:
            k=k+1
            new_coll=[]
            new_coll_wp90=[]
            new_coll_wp99=[]
            score=[]
            score_=-999
            if train.lepton == 1:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.pt_cut[0]) and (x.nu_pt<train.pt_cut[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.el_index != -1) and electron[int(x.el_index)].mvaFall17V2noIso_WP90==1
                                                ,tops))
                is_el=True
            else:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.pt_cut[0]) and (x.nu_pt<train.pt_cut[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.mu_index != -1)
                                                ,tops))
                is_el=False


            for top in good_top:
                if top.TvsQCD>train.QCDcut:
                    new_coll.append(top)
                    if top.TvsOth>=train.Lcut: new_coll_wp90.append(top)
                    if top.TvsOth>=train.Tcut: new_coll_wp99.append(top)               
                
            if(len(new_coll)>0): 
                new_coll =  [x for _,x in sorted(zip([new_coll[i].TvsOth for i in range(len(new_coll))],new_coll))]
                new_coll.reverse()
    
                if(len(new_coll_wp90)>0):
                    h_nTop_type_wp90.Fill(k,len(new_coll_wp90)) 
                    new_coll_wp90 = [x for _,x in sorted(zip([new_coll_wp90[i].TvsOth for i in range(len(new_coll_wp90))],new_coll_wp90))] 
                    new_coll_wp90.reverse()
                    if(len(new_coll_wp99)>0):
                        h_nTop_type_wp99.Fill(k,len(new_coll_wp99)) 
                        new_coll_wp99 = [x for _,x in sorted(zip([new_coll_wp99[i].TvsOth for i in range(len(new_coll_wp99))],new_coll_wp99))] 
                        new_coll_wp99.reverse()
                

            all_coll = all_coll + new_coll
            all_coll_wp90 = all_coll_wp90 + new_coll_wp90
            all_coll_wp99 = all_coll_wp99 + new_coll_wp99
            
            


        if(len(all_coll)>0):
            lista= all_coll
        
            if(len(all_coll_wp99)): 
                top_region_nominal[0]=1
                lista = all_coll_wp99
            elif (len(all_coll_wp90)): 
                top_region_nominal[0]=0
                lista= all_coll_wp90

            Top_pt_nominal[0] = lista[0].nu_pt 
            Top_eta_nominal[0] = lista[0].nu_eta 
            Top_phi_nominal[0] = lista[0].nu_phi 
            Top_M_nominal[0] = lista[0].nu_M 
            Top_isMerg_nominal[0] = lista[0].Is_dR_merg

            Top_Score0_nominal[0] = lista[0].Score0
            Top_Score1_nominal[0] = lista[0].Score1
            Top_Score2_nominal[0] = lista[0].Score2
            
            Top_TvsQCD_nominal[0] = lista[0].TvsQCD
            Top_TvsOth_nominal[0] = lista[0].TvsOth

            top_vect= ROOT.TLorentzVector()
            top_vect.SetPtEtaPhiM(Top_pt_nominal[0],Top_eta_nominal[0],Top_phi_nominal[0],Top_M_nominal[0]) 
            
            """
            Not Here!!!
            fatjet_vect= ROOT.TLorentzVector()
            fatjet_vect.SetPtEtaPhiM(FatJet_pt_nominal[0],FatJet_eta_nominal[0],FatJet_phi_nominal[0],FatJet_M_nominal[0])

            Tprime_vect = fatjet_vect+top_vect

            Tprime_pt_nominal [0] =  Tprime_vect.Pt()
            Tprime_eta_nominal [0] =  Tprime_vect.Eta()
            Tprime_phi_nominal [0] =  Tprime_vect.Phi()
            Tprime_M_nominal [0] =  Tprime_vect.M()
            """
            Jet_pt_nominal [0] = jets[int(lista[0].bjet_index)].pt
            Jet_eta_nominal [0] = jets[int(lista[0].bjet_index)].eta
            Jet_phi_nominal [0] = jets[int(lista[0].bjet_index)].phi
            Jet_M_nominal [0] = jets[int(lista[0].bjet_index)].mass
            Jet_btag_nominal [0] = jets[int(lista[0].bjet_index)].btagDeepFlavB

            Top_JetIdx_nominal[0]= lista[0].bjet_index
            if len(all_coll_wp90)>1:
                SecTop_MC_nominal[0] = 0
                if("TT" in sample.label or "Tprime" in sample.label or "ST" in sample.label):
                    if(all_coll_wp90[1].High_Truth==0): SecTop_MC_nominal[0] = 1
                    elif (all_coll_wp90[1].High_Truth==1 ): SecTop_MC_nominal[0] = 0
                    else: SecTop_MC_nominal[0] = all_coll_wp90[1].High_Truth
                SecTop_JetIdx_nominal[0]= all_coll_wp90[1].bjet_index

                if(all_coll_wp90[1].el_index!=-1):
                    SecTop_flavour_nominal[0] = 11
                    SecTop_LepIdx_nominal[0] = all_coll_wp90[1].el_index
                else: 
                    SecTop_flavour_nominal[0] = 13
                    SecTop_LepIdx_nominal[0] = all_coll_wp90[1].mu_index
                SecTop_isMerg_nominal[0]= all_coll_wp90[1].Is_dR_merg
        
            Top_MC_nominal[0] = 0
            if("TT" in sample.label or "Tprime" in sample.label or "ST" in sample.label):
                if(lista[0].High_Truth==0): Top_MC_nominal[0] = 1
                elif lista[0].High_Truth==1 : Top_MC_nominal[0] = 0
                else: Top_MC_nominal[0] = lista[0].High_Truth
            if(lista[0].el_index!=-1): 
                Top_flavour_nominal[0] = 11
                if(electron[int(lista[0].el_index)].charge==1): Top_flavour_nominal[0] = - Top_flavour_nominal[0]
                Top_LepIdx_nominal[0] = lista[0].el_index
                Lep_dxy_nominal [0] = electron[int(lista[0].el_index)].dxy 
                Lep_dxyerr_nominal [0] = electron[int(lista[0].el_index)].dxyErr 
                Lep_dz_nominal [0] = electron[int(lista[0].el_index)].dz 
                Lep_dzerr_nominal [0] = electron[int(lista[0].el_index)].dzErr 
                Lep_Iso_nominal [0] = electron[int(lista[0].el_index)].pfRelIso03_all
                Lep_MiniIso_nominal [0] = electron[int(lista[0].el_index)].miniPFRelIso_all
                Lep_pt_nominal [0] = electron[int(lista[0].el_index)].pt 
                Lep_eta_nominal [0] = electron[int(lista[0].el_index)].eta 
                Lep_phi_nominal [0] = electron[int(lista[0].el_index)].phi 
                Lep_M_nominal [0] = electron[int(lista[0].el_index)].mass 
                Lep_Id_nominal [0] = electron[int(lista[0].el_index)].cutBased
            else: 
                Top_flavour_nominal[0] = 13
                if(muon[int(lista[0].mu_index)].charge==1): Top_flavour_nominal[0] = - Top_flavour_nominal[0]
                Top_LepIdx_nominal[0] = lista[0].mu_index
                Lep_dxy_nominal [0] = muon[int(lista[0].mu_index)].dxy 
                Lep_dxyerr_nominal [0] = muon[int(lista[0].mu_index)].dxyErr 
                Lep_dz_nominal [0] = muon[int(lista[0].mu_index)].dz 
                Lep_dzerr_nominal [0] = muon[int(lista[0].mu_index)].dzErr 
                Lep_Iso_nominal [0] = muon[int(lista[0].mu_index)].pfRelIso04_all
                Lep_MiniIso_nominal [0] = muon[int(lista[0].mu_index)].miniPFRelIso_all
                Lep_pt_nominal [0] = muon[int(lista[0].mu_index)].pt 
                Lep_eta_nominal [0] = muon[int(lista[0].mu_index)].eta 
                Lep_phi_nominal [0] = muon[int(lista[0].mu_index)].phi 
                Lep_M_nominal [0] = muon[int(lista[0].mu_index)].mass 
                if muon[int(lista[0].mu_index)].looseId: Lep_Id_nominal [0] = 1+int(muon[int(lista[0].mu_index)].looseId)+int(muon[int(lista[0].mu_index)].mediumId)+int(muon[int(lista[0].mu_index)].tightId)
                else: Lep_Id_nominal [0] = 0
            
        #for top in all_coll: print(top.TvsQCD,top.TvsOth,top.Is_dR_merg, top.pt, top.nu_pt, top.el_index)
        #print("len(tightEle) ",len(tightEle))
        #print("len(tightMu) ",len(tightMu))
        if(len(all_coll_wp90)>0): goodfatjets = list(filter(lambda x: deltaR(x.eta,x.phi,Top_eta_nominal[0],Top_phi_nominal[0])>1.2 and deltaR(x.eta,x.phi,Jet_eta_nominal[0],Jet_phi_nominal[0])>1.2 and deltaR(x.eta,x.phi,Lep_eta_nominal[0],Lep_phi_nominal[0])>0.8 and (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or (x.msoftdrop>=60 and x.msoftdrop<=220)),fatjets))
        elif(len(tightEle)>0 and len(tightMu)==0):
            goodfatjets = list(filter(lambda x: (deltaR(x.eta,x.phi,TightEl_eta_nominal[0],TightEl_phi_nominal[0])>0.8) and (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or (x.msoftdrop>=60 and x.msoftdrop<=220)),fatjets))
            top_region_nominal[0]=-1
        elif(len(tightEle)==0 and len(tightMu)>0):
            goodfatjets = list(filter(lambda x: (deltaR(x.eta,x.phi,TightMu_eta_nominal[0],TightMu_phi_nominal[0])>0.8)  and (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or (x.msoftdrop>=60 and x.msoftdrop<=220)),fatjets))
            top_region_nominal[0]=-1

        elif(len(tightEle)>0 and len(tightMu)>0):
            goodfatjets = []



        if len(goodfatjets)==0: continue
        goodfatjets.sort(key=lambda x:weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD),reverse=True)
        if weird_division(goodfatjets[0].particleNetMD_Xbb,goodfatjets[0].particleNetMD_Xbb+goodfatjets[0].particleNetMD_QCD)<0.8: AK8_region_nominal[0]=0
        elif weird_division(goodfatjets[0].particleNetMD_Xbb,goodfatjets[0].particleNetMD_Xbb+goodfatjets[0].particleNetMD_QCD)>=0.98:AK8_region_nominal[0]=2
        else: AK8_region_nominal[0]=1
            
        FatJet_pt_nominal[0]=goodfatjets[0].pt
        FatJet_eta_nominal[0]=goodfatjets[0].eta
        FatJet_phi_nominal[0]=goodfatjets[0].phi
        FatJet_M_nominal[0]=goodfatjets[0].msoftdrop
        FatJet_Xbb_nominal[0]=goodfatjets[0].particleNetMD_Xbb
        fatjet_vect= ROOT.TLorentzVector()
        fatjet_vect.SetPtEtaPhiM(FatJet_pt_nominal[0],FatJet_eta_nominal[0],FatJet_phi_nominal[0],FatJet_M_nominal[0])
        FatJet_XbbVsQCD_nominal[0]= weird_division(goodfatjets[0].particleNetMD_Xbb,goodfatjets[0].particleNetMD_Xbb+goodfatjets[0].particleNetMD_QCD)
        if(len(all_coll_wp90)>0):
            Tprime_dR_nominal[0] = deltaR(goodfatjets[0].eta,goodfatjets[0].phi,Top_eta_nominal[0],Top_phi_nominal[0])
            fatjet_vect= ROOT.TLorentzVector()
            fatjet_vect.SetPtEtaPhiM(FatJet_pt_nominal[0],FatJet_eta_nominal[0],FatJet_phi_nominal[0],FatJet_M_nominal[0])
            Tprime_vect = fatjet_vect+top_vect
            Tprime_pt_nominal [0] =  Tprime_vect.Pt()
            Tprime_eta_nominal [0] =  Tprime_vect.Eta()
            Tprime_phi_nominal [0] =  Tprime_vect.Phi()
            Tprime_M_nominal [0] =  Tprime_vect.M()

        FatJet_btagDeepB_nominal[0]=goodfatjets[0].btagDeepB
        FatJet_tau1_nominal[0]=goodfatjets[0].tau1
        FatJet_tau2_nominal[0]=goodfatjets[0].tau2
        FatJet_MC_nominal[0]=0

        if not "Data" in sample.label:
            genpart = Collection(event,"GenPart")
            """
            higgs = list(filter(lambda x: x.pdgId==25 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8,genpart))
            tops = list(filter(lambda x: abs(x.pdgId)==6 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8,genpart))
            Ws = list(filter(lambda x: abs(x.pdgId)<=5 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8 and x.genPartIdxMother>=0 and abs(genpart[x.genPartIdxMother].pdgId)==24,genpart))
            bs = list(filter(lambda x: abs(x.pdgId)==5 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8 and x.genPartIdxMother_prompt>=0 and abs(genpart[x.genPartIdxMother_prompt].pdgId)==6,genpart))
            """
            higgs = list(filter(lambda x: abs(x.pdgId)==5 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8 and x.genPartIdxMother>=0 and abs(genpart[x.genPartIdxMother].pdgId)==25,genpart))
            LHE = Collection(event,"LHEPart")
            bs = list(filter(lambda x: abs(x.pdgId)==5 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8  and x.status==1,LHE))
            Wh = list(filter(lambda x: abs(x.pdgId)<5 and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8  and x.status==1,LHE))
            Wl = list(filter(lambda x: (abs(x.pdgId)==11 or abs(x.pdgId)==13 or abs(x.pdgId)==15) and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)<0.8  and x.status==1,LHE))
            if len(higgs)>0: FatJet_MC_nominal[0]=FatJet_MC_nominal[0]+1000*len(higgs)
            #if (len(tops)>0): FatJet_MC_nominal[0]=FatJet_MC_nominal[0]+100
            if (len(Wh)>0 ): FatJet_MC_nominal[0]=FatJet_MC_nominal[0]+100*len(Wh)
            if (len(Wl)>0 ): FatJet_MC_nominal[0]=FatJet_MC_nominal[0]+10
            if (len(bs)>0 ): 
                FatJet_MC_nominal[0]=FatJet_MC_nominal[0]+1*len(bs)
                FatJet_dRMC_nominal[0]= closest(goodfatjets[0],LHE,presel=lambda y,x: x.status==1 and (abs(x.pdgId)<=5  or abs(x.pdgId)==11 or abs(x.pdgId)==13 or abs(x.pdgId)==15 ) and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)>=0.8) [1]
            else:
                FatJet_dRMC_nominal[0]=-1
            ParNetSF_nominal[0], ParNetUp_nominal[0], ParNetDown_nominal[0] = getPN_SF(sample.label, FatJet_MC_nominal[0])

  
            
        

        if top_region_nominal[0]>=0 :BDTSF_nominal[0], BDTUp_nominal[0], BDTDown_nominal[0] = getBDT_SF(sample.label, Top_isMerg_nominal[0], Top_pt_nominal[0], top_region_nominal[0], Top_flavour_nominal[0])

        

        alljets = list(filter(lambda x: x.pt>=-999,jets))
        allmuons = list(filter(lambda x: x.pt>=-999,muon))
        allelectrons = list(filter(lambda x: x.pt>=-999,electron))
        bjets, nobjets = bjet_filter(alljets, 'DeepFlv', 'M')
        if(len(all_coll)>0): other_bjet = list(filter(lambda x: alljets.index(x)!=int(lista[0].bjet_index) and deltaR(goodfatjets[0].eta,goodfatjets[0].phi,x.eta,x.phi)>1.2, bjets))
        else: other_bjet=[]
        N_bjet_nominal[0] =len(other_bjet)
        if N_bjet_nominal[0]>0:
            dR_bjet_AK8_nominal[0] = deltaR(goodfatjets[0].eta,goodfatjets[0].phi,other_bjet[0].eta,other_bjet[0].phi) 
            bjet_vect = ROOT.TLorentzVector()
            bjet_vect.SetPtEtaPhiM(other_bjet[0].pt,other_bjet[0].eta,other_bjet[0].phi,other_bjet[0].mass)
            M_bjet_AK8_nominal[0] =  (bjet_vect+fatjet_vect).M()
            othbJet_pt_nominal[0] = other_bjet[0].pt
            othbJet_eta_nominal[0] = other_bjet[0].eta
            othbJet_phi_nominal[0] = other_bjet[0].phi
            othbJet_M_nominal[0] = other_bjet[0].mass
            othbJet_btag_nominal[0] = other_bjet[0].btagDeepFlavB
        else:
            dR_bjet_AK8_nominal[0] = -999.
            M_bjet_AK8_nominal[0] = -999.
            othbJet_eta_nominal[0] = -999.
            othbJet_phi_nominal[0] = -999.
            othbJet_M_nominal[0] = -999.
            othbJet_btag_nominal[0] =-999.
        
        N_jet_nominal[0]= len(alljets)
        if(len(all_coll)>0):dR_jet_AK8_nominal[0] = deltaR(goodfatjets[0].eta,goodfatjets[0].phi,Jet_phi_nominal[0],Jet_eta_nominal[0])
        else:dR_jet_AK8_nominal[0]=-1
        N_top_nominal[0] = len(all_coll_wp90)
        N_AK8_nominal[0] = len(goodfatjets)

        if(len(all_coll_wp90)>0):
            N_muTop_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=int(lista[0].mu_index) and x.looseId and x.miniPFRelIso_all<4 and abs(x.dxy)<0.02, muon))) 
            N_muVeryLoose_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=int(lista[0].mu_index) and x.looseId and x.pfRelIso04_all<0.4, muon)))
            N_muLoose_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=int(lista[0].mu_index) and x.looseId and x.pfRelIso04_all<0.15 and x.pt>30, muon)))

            N_elTop_nominal[0]= len(list(filter(lambda x: allelectrons.index(x)!=int(lista[0].el_index) and x.mvaFall17V2noIso_WPL and abs(x.dxy)<0.05, electron)))
            N_elVeryLoose_nominal[0] = len(list(filter(lambda x: allelectrons.index(x)!=int(lista[0].el_index) and x.cutBased>=1  and x.pfRelIso03_all<0.4, electron)))
            N_elLoose_nominal[0] = len(list(filter(lambda x: allelectrons.index(x)!=int(lista[0].el_index) and x.mvaFall17V2Iso_WP90==1 and x.pt>30 , electron)))

        else:
            if(len(tightMu)>0):
                N_muTop_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=allmuons.index(tightMu[0]) and x.looseId and x.miniPFRelIso_all<4 and abs(x.dxy)<0.02, muon))) 
                N_muVeryLoose_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=allmuons.index(tightMu[0]) and x.looseId and x.pfRelIso04_all<0.4, muon)))
                N_muLoose_nominal[0] = len(list(filter(lambda x: allmuons.index(x)!=allmuons.index(tightMu[0]) and x.looseId and x.pfRelIso04_all<0.15 and x.pt>30, muon)))
            else:
                N_muTop_nominal[0] = len(list(filter(lambda x: x.looseId and x.miniPFRelIso_all<4 and abs(x.dxy)<0.02, muon))) 
                N_muVeryLoose_nominal[0] = len(list(filter(lambda x:  x.looseId and x.pfRelIso04_all<0.4, muon)))
                N_muLoose_nominal[0] = len(list(filter(lambda x:  x.looseId and x.pfRelIso04_all<0.15 and x.pt>30, muon)))

            if(len(tightEle)>0):
                N_elTop_nominal[0]= len(list(filter(lambda x: allelectrons.index(x)!=allelectrons.index(tightEle[0]) and x.mvaFall17V2noIso_WPL and abs(x.dxy)<0.05, electron)))
                N_elVeryLoose_nominal[0] = len(list(filter(lambda x: allelectrons.index(x)!=allelectrons.index(tightEle[0]) and x.cutBased>=1  and x.pfRelIso03_all<0.4, electron)))
                N_elLoose_nominal[0] = len(list(filter(lambda x: allelectrons.index(x)!=allelectrons.index(tightEle[0]) and x.mvaFall17V2Iso_WP90==1 and x.pt>30 , electron)))
            else:
                N_elTop_nominal[0]= len(list(filter(lambda x: x.mvaFall17V2noIso_WPL and abs(x.dxy)<0.05, electron)))
                N_elVeryLoose_nominal[0] = len(list(filter(lambda x: x.cutBased>=1 , electron)))
                N_elLoose_nominal[0] = len(list(filter(lambda x: x.mvaFall17V2Iso_WP90==1 and x.pt>30 , electron)))
        
        #check Iso or MiniIso N_ecc                            
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_nominal[0]))
        systTree.setWeightName("w_pt",copy.deepcopy(w_pt_nominal[0]))
        systTree.setWeightName("ParNetSF",copy.deepcopy(ParNetSF_nominal[0]))
        systTree.setWeightName("ParNetUp",copy.deepcopy(ParNetUp_nominal[0]))
        systTree.setWeightName("ParNetDown",copy.deepcopy(ParNetDown_nominal[0]))
        systTree.setWeightName("BDTSF",copy.deepcopy(BDTSF_nominal[0]))
        systTree.setWeightName("BDTUp",copy.deepcopy(BDTUp_nominal[0]))
        systTree.setWeightName("BDTDown",copy.deepcopy(BDTDown_nominal[0]))
        systTree.fillTreesSysts(trees, scenario)
        h_cutFlow.GetXaxis().SetBinLabel(4,"No LooseLep and Best TvsQCD>0.6")
        h_cutFlow.GetXaxis().SetBinLabel(5,"Best Top Loose")
        h_cutFlow.GetXaxis().SetBinLabel(6,"Best Top Loose Fwd0")
        h_cutFlow.GetXaxis().SetBinLabel(7,"Best Top Loose Fwd1")
        h_cutFlow.GetXaxis().SetBinLabel(8,"Best Top Tight")
        h_cutFlow.GetXaxis().SetBinLabel(9,"Best Top Tight Fwd0")
        h_cutFlow.GetXaxis().SetBinLabel(10,"Best Top Tight Fwd1")

        if AK8_region_nominal[0]==2 and  goodfatjets[0].msoftdrop<=140 and goodfatjets[0].msoftdrop>=100:
            h_cutFlow.Fill("AK8 Tight 100<M<140",1)
            if Top_TvsQCD_nominal[0]>0.6 and (N_elLoose_nominal[0]+N_muLoose_nominal[0]==0):
                h_cutFlow.Fill("No LooseLep and Best TvsQCD>0.6",1)
                if top_region_nominal[0]==0: 
                    h_cutFlow.Fill("Best Top Loose",1)
                    if Fwd4_region_nominal[0]==0:h_cutFlow.Fill("Best Top Loose Fwd0",1)
                    else: h_cutFlow.Fill("Best Top Loose Fwd1",1)
                else:
                    h_cutFlow.Fill("Best Top Tight",1)
                    if Fwd4_region_nominal[0]==0:h_cutFlow.Fill("Best Top Tight Fwd0",1)
                    else: h_cutFlow.Fill("Best Top Tight Fwd1",1)
            
    outTreeFile.cd()
    if scenario == 'nominal':
        trees[0].Write()
        h_nTop_type_wp90.Write()
        h_nTop_type_wp99.Write()
        if(isMC):
            h_cutFlow.Write()
            h_cutFlow_pc = ROOT.TH1D("h_cutFlow_pc","h_cutFlow_pc",10,-0.5,9.5)
            h_cutFlow_pc = h_cutFlow.Clone("h_cutFlow_pc")
            h_cutFlow_pc.Scale(1./h_cutFlow.GetBinContent(1))
            h_cutFlow_pc.Write()
            h_genweight.Write()
            h_PDFweight.Write()

    elif scenario == 'jesUp':
        trees[1].Write()
    elif scenario == 'jesDown':
        trees[2].Write()
    elif scenario == 'jerUp':
        trees[3].Write()
    elif scenario == 'jerDown':
        trees[4].Write()

    print("Number of events in output tree nominal " + str(trees[0].GetEntries()))
    if isMC:
        print("Number of events in output tree jesUp " + str(trees[1].GetEntries()))
        print("Number of events in output tree jesDown " + str(trees[2].GetEntries()))
        print("Number of events in output tree jerUp " + str(trees[3].GetEntries()))
        print("Number of events in output tree jerDown " + str(trees[4].GetEntries()))
    systTree.writeTreesSysts(trees, outTreeFile)


for scenario in scenarios:
    reco(scenario, isMC,addPDF, training)


endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
