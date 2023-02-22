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
print("ok \n")
import xgboost as xgb
import numpy as np
from training import *
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
systZero = systWeights()
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

h_cutFlow = ROOT.TH1D("h_cutFlow","h_cutFlow",10,-0.5,9.5)

h_nTop_type_0p5 = ROOT.TH2D("h_nTop_type_0p5","h_nTop_type_0p5",9,0.5,9.5,7,0.5,7.5)
h_nTop_type_wp90 = ROOT.TH2D("h_nTop_type_wp90","h_nTop_type_wp90",9,0.5,9.5,7,0.5,7.5)

def reco(scenario, isMC, addPDF, training):
    isNominal = False
    if scenario == 'nominal':
        isNominal = True
    print(scenario)
    w_PDF_nominal = array.array('f',[0.])

    HLT_Muon_nominal = array.array('f',[0.])
    HLT_Electron_nominal = array.array('f',[0.])
    HLT_Photon_nominal = array.array('f',[0.])
    HLT_PFJet_nominal = array.array('f',[0.])
     

    #Top_number_wp90_nominal = array.array('f',[0.,0.,0.,0.,0.,0.,0.,0.])
    #Top_number_0p5_nominal = array.array('f',[0.,0.,0.,0.,0.,0.,0.,0.])
    nZ_medium_nominal = array.array('f',[0.]) 

    Top_pt1_nominal = array.array('f',[0.]) 
    Top_eta1_nominal = array.array('f',[0.]) 
    Top_phi1_nominal = array.array('f',[0.]) 
    Top_M1_nominal = array.array('f',[0.]) 
    Top_Score1_nominal = array.array('f',[0.]) 
    Top_MC1_nominal = array.array('i',[0])
    Top_flavour1_nominal = array.array('i',[0]) #if isMC:
    Top_isMerg1_nominal = array.array('f',[0.])

    Top_pt2_nominal = array.array('f',[0.]) 
    Top_eta2_nominal = array.array('f',[0.]) 
    Top_phi2_nominal = array.array('f',[0.]) 
    Top_M2_nominal = array.array('f',[0.]) 
    Top_Score2_nominal = array.array('f',[0.]) 
    Top_MC2_nominal = array.array('i',[0])
    Top_flavour2_nominal = array.array('i',[0])
    Top_isMerg2_nominal = array.array('f',[0.])

    Top_pt3_nominal = array.array('f',[0.]) 
    Top_eta3_nominal = array.array('f',[0.]) 
    Top_phi3_nominal = array.array('f',[0.]) 
    Top_M3_nominal = array.array('f',[0.]) 
    Top_Score3_nominal = array.array('f',[0.])
    Top_MC3_nominal = array.array('i',[0])
    Top_flavour3_nominal = array.array('i',[0]) 
    Top_isMerg3_nominal = array.array('f',[0.])

    Top_pt4_nominal = array.array('f',[0.]) 
    Top_eta4_nominal = array.array('f',[0.]) 
    Top_phi4_nominal = array.array('f',[0.]) 
    Top_M4_nominal = array.array('f',[0.]) 
    Top_Score4_nominal = array.array('f',[0.]) 
    Top_MC4_nominal = array.array('i',[0])
    Top_flavour4_nominal = array.array('i',[0]) #if isMC:
    Top_isMerg4_nominal = array.array('f',[0.])

    Top_pt1_0p5_nominal = array.array('f',[0.]) 
    Top_eta1_0p5_nominal = array.array('f',[0.]) 
    Top_phi1_0p5_nominal = array.array('f',[0.]) 
    Top_M1_0p5_nominal = array.array('f',[0.]) 
    Top_Score1_0p5_nominal = array.array('f',[0.]) 
    Top_MC1_0p5_nominal = array.array('i',[0])
    Top_flavour1_0p5_nominal = array.array('i',[0])
    Top_isMerg1_0p5_nominal = array.array('f',[0.])

    Top_pt2_0p5_nominal = array.array('f',[0.]) 
    Top_eta2_0p5_nominal = array.array('f',[0.]) 
    Top_phi2_0p5_nominal = array.array('f',[0.]) 
    Top_M2_0p5_nominal = array.array('f',[0.]) 
    Top_Score2_0p5_nominal = array.array('f',[0.]) 
    Top_MC2_0p5_nominal = array.array('i',[0])
    Top_flavour2_0p5_nominal = array.array('i',[0])
    Top_isMerg2_0p5_nominal = array.array('f',[0.])

    Top_pt3_0p5_nominal = array.array('f',[0.]) 
    Top_eta3_0p5_nominal = array.array('f',[0.]) 
    Top_phi3_0p5_nominal = array.array('f',[0.]) 
    Top_M3_0p5_nominal = array.array('f',[0.]) 
    Top_Score3_0p5_nominal = array.array('f',[0.])
    Top_MC3_0p5_nominal = array.array('i',[0])
    Top_flavour3_0p5_nominal = array.array('i',[0]) 
    Top_isMerg3_0p5_nominal = array.array('f',[0.])

    Top_pt4_0p5_nominal = array.array('f',[0.]) 
    Top_eta4_0p5_nominal = array.array('f',[0.]) 
    Top_phi4_0p5_nominal = array.array('f',[0.]) 
    Top_M4_0p5_nominal = array.array('f',[0.]) 
    Top_Score4_0p5_nominal = array.array('f',[0.])
    Top_MC4_0p5_nominal = array.array('i',[0])
    Top_flavour4_0p5_nominal = array.array('i',[0]) 
    Top_isMerg4_0p5_nominal = array.array('f',[0.])

    Top_pt1_wp90_nominal = array.array('f',[0.]) 
    Top_eta1_wp90_nominal = array.array('f',[0.]) 
    Top_phi1_wp90_nominal = array.array('f',[0.]) 
    Top_M1_wp90_nominal = array.array('f',[0.]) 
    Top_Score1_wp90_nominal = array.array('f',[0.]) 
    Top_MC1_wp90_nominal = array.array('i',[0])
    Top_flavour1_wp90_nominal = array.array('i',[0])
    Top_isMerg1_wp90_nominal = array.array('f',[0.])

    Top_pt2_wp90_nominal = array.array('f',[0.]) 
    Top_eta2_wp90_nominal = array.array('f',[0.]) 
    Top_phi2_wp90_nominal = array.array('f',[0.]) 
    Top_M2_wp90_nominal = array.array('f',[0.]) 
    Top_Score2_wp90_nominal = array.array('f',[0.]) 
    Top_MC2_wp90_nominal = array.array('i',[0])
    Top_flavour2_wp90_nominal = array.array('i',[0])
    Top_isMerg2_wp90_nominal = array.array('f',[0.])

    Top_pt3_wp90_nominal = array.array('f',[0.]) 
    Top_eta3_wp90_nominal = array.array('f',[0.]) 
    Top_phi3_wp90_nominal = array.array('f',[0.]) 
    Top_M3_wp90_nominal = array.array('f',[0.]) 
    Top_Score3_wp90_nominal = array.array('f',[0.])
    Top_MC3_wp90_nominal = array.array('i',[0])
    Top_flavour3_wp90_nominal = array.array('i',[0])
    Top_isMerg3_wp90_nominal = array.array('f',[0.])

    Top_pt4_wp90_nominal = array.array('f',[0.]) 
    Top_eta4_wp90_nominal = array.array('f',[0.]) 
    Top_phi4_wp90_nominal = array.array('f',[0.]) 
    Top_M4_wp90_nominal = array.array('f',[0.]) 
    Top_Score4_wp90_nominal = array.array('f',[0.])
    Top_MC4_wp90_nominal = array.array('i',[0])
    Top_flavour4_wp90_nominal = array.array('i',[0])
    Top_isMerg4_wp90_nominal = array.array('f',[0.])

    #systTree.branchTreesSysts(trees, scenario,"Top_number_wp90_nominal", outTreeFile, Top_number_wp90_nominal)
    #systTree.branchTreesSysts(trees, scenario,"Top_number_0p5_nominal", outTreeFile, Top_number_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"nZ_medium_nominal",outTreeFile,nZ_medium_nominal)

    systTree.branchTreesSysts(trees, scenario,"HLT_Muon_nominal", outTreeFile,HLT_Muon_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_Electron_nominal", outTreeFile,HLT_Electron_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_Photon_nominal", outTreeFile,HLT_Photon_nominal)
    systTree.branchTreesSysts(trees, scenario,"HLT_PFJet_nominal", outTreeFile,HLT_PFJet_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt1_nominal",outTreeFile,Top_pt1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta1_nominal",outTreeFile,Top_eta1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi1_nominal",outTreeFile,Top_phi1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M1_nominal",outTreeFile,Top_M1_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score1_nominal",outTreeFile,Top_Score1_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC1_nominal",outTreeFile,Top_MC1_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt2_nominal",outTreeFile,Top_pt2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta2_nominal",outTreeFile,Top_eta2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi2_nominal",outTreeFile,Top_phi2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M2_nominal",outTreeFile,Top_M2_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score2_nominal",outTreeFile,Top_Score2_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC2_nominal",outTreeFile,Top_MC2_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt3_nominal",outTreeFile,Top_pt3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta3_nominal",outTreeFile,Top_eta3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi3_nominal",outTreeFile,Top_phi3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M3_nominal",outTreeFile,Top_M3_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score3_nominal",outTreeFile,Top_Score3_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC3_nominal",outTreeFile,Top_MC3_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt4_nominal",outTreeFile,Top_pt4_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta4_nominal",outTreeFile,Top_eta4_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi4_nominal",outTreeFile,Top_phi4_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M4_nominal",outTreeFile,Top_M4_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score4_nominal",outTreeFile,Top_Score4_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC4_nominal",outTreeFile,Top_MC4_nominal)


    systTree.branchTreesSysts(trees, scenario,"Top_pt1_0p5_nominal",outTreeFile,Top_pt1_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta1_0p5_nominal",outTreeFile,Top_eta1_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi1_0p5_nominal",outTreeFile,Top_phi1_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M1_0p5_nominal",outTreeFile,Top_M1_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score1_0p5_nominal",outTreeFile,Top_Score1_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC1_0p5_nominal",outTreeFile,Top_MC1_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt2_0p5_nominal",outTreeFile,Top_pt2_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta2_0p5_nominal",outTreeFile,Top_eta2_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi2_0p5_nominal",outTreeFile,Top_phi2_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M2_0p5_nominal",outTreeFile,Top_M2_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score2_0p5_nominal",outTreeFile,Top_Score2_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC2_0p5_nominal",outTreeFile,Top_MC2_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt3_0p5_nominal",outTreeFile,Top_pt3_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta3_0p5_nominal",outTreeFile,Top_eta3_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi3_0p5_nominal",outTreeFile,Top_phi3_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M3_0p5_nominal",outTreeFile,Top_M3_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score3_0p5_nominal",outTreeFile,Top_Score3_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC3_0p5_nominal",outTreeFile,Top_MC3_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt4_0p5_nominal",outTreeFile,Top_pt4_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta4_0p5_nominal",outTreeFile,Top_eta4_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi4_0p5_nominal",outTreeFile,Top_phi4_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M4_0p5_nominal",outTreeFile,Top_M4_0p5_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score4_0p5_nominal",outTreeFile,Top_Score4_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC4_0p5_nominal",outTreeFile,Top_MC4_0p5_nominal)


    systTree.branchTreesSysts(trees, scenario,"Top_pt1_wp90_nominal",outTreeFile,Top_pt1_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta1_wp90_nominal",outTreeFile,Top_eta1_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi1_wp90_nominal",outTreeFile,Top_phi1_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M1_wp90_nominal",outTreeFile,Top_M1_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score1_wp90_nominal",outTreeFile,Top_Score1_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC1_wp90_nominal",outTreeFile,Top_MC1_wp90_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt2_wp90_nominal",outTreeFile,Top_pt2_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta2_wp90_nominal",outTreeFile,Top_eta2_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi2_wp90_nominal",outTreeFile,Top_phi2_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M2_wp90_nominal",outTreeFile,Top_M2_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score2_wp90_nominal",outTreeFile,Top_Score2_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC2_wp90_nominal",outTreeFile,Top_MC2_wp90_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt3_wp90_nominal",outTreeFile,Top_pt3_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta3_wp90_nominal",outTreeFile,Top_eta3_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi3_wp90_nominal",outTreeFile,Top_phi3_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M3_wp90_nominal",outTreeFile,Top_M3_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score3_wp90_nominal",outTreeFile,Top_Score3_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC3_wp90_nominal",outTreeFile,Top_MC3_wp90_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_pt4_wp90_nominal",outTreeFile,Top_pt4_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_eta4_wp90_nominal",outTreeFile,Top_eta4_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_phi4_wp90_nominal",outTreeFile,Top_phi4_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_M4_wp90_nominal",outTreeFile,Top_M4_wp90_nominal) 
    systTree.branchTreesSysts(trees, scenario,"Top_Score4_wp90_nominal",outTreeFile,Top_Score4_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_MC4_wp90_nominal",outTreeFile,Top_MC4_wp90_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_flavour1_nominal", outTreeFile, Top_flavour1_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour2_nominal", outTreeFile, Top_flavour2_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour3_nominal", outTreeFile, Top_flavour3_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour4_nominal", outTreeFile, Top_flavour4_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_flavour1_0p5_nominal", outTreeFile, Top_flavour1_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour2_0p5_nominal", outTreeFile, Top_flavour2_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour3_0p5_nominal", outTreeFile, Top_flavour3_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour4_0p5_nominal", outTreeFile, Top_flavour4_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_flavour1_wp90_nominal", outTreeFile, Top_flavour1_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour2_wp90_nominal", outTreeFile, Top_flavour2_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour3_wp90_nominal", outTreeFile, Top_flavour3_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_flavour4_wp90_nominal", outTreeFile, Top_flavour4_wp90_nominal)


    systTree.branchTreesSysts(trees, scenario,"Top_isMerg1_nominal", outTreeFile, Top_isMerg1_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg2_nominal", outTreeFile, Top_isMerg2_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg3_nominal", outTreeFile, Top_isMerg3_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg4_nominal", outTreeFile, Top_isMerg4_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_isMerg1_0p5_nominal", outTreeFile, Top_isMerg1_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg2_0p5_nominal", outTreeFile, Top_isMerg2_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg3_0p5_nominal", outTreeFile, Top_isMerg3_0p5_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg4_0p5_nominal", outTreeFile, Top_isMerg4_0p5_nominal)

    systTree.branchTreesSysts(trees, scenario,"Top_isMerg1_wp90_nominal", outTreeFile, Top_isMerg1_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg2_wp90_nominal", outTreeFile, Top_isMerg2_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg3_wp90_nominal", outTreeFile, Top_isMerg3_wp90_nominal)
    systTree.branchTreesSysts(trees, scenario,"Top_isMerg4_wp90_nominal", outTreeFile, Top_isMerg4_wp90_nominal)

    
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
        h_cutFlow.GetXaxis().SetBinLabel(2,"PresEvents")
        h_cutFlow.GetXaxis().SetBinLabel(3,"n Z/H/A Medium > 0")
        h_cutFlow.GetXaxis().SetBinLabel(4,"nTop_wp90 > 0")
        h_cutFlow.GetXaxis().SetBinLabel(5,"Trigger All")
        h_cutFlow.GetXaxis().SetBinLabel(6,"Trigger No TrimMass30")
        


    for i in range(tree.GetEntries()):
        w_PDF_nominal[0]=1.
        HLT_Muon_nominal[0] = 0.
        HLT_Electron_nominal[0] = 0.
        HLT_Photon_nominal[0] = 0.
        HLT_PFJet_nominal[0] = 0.
        
        event = Event(tree,i) 

        if ("TT" in sample.label) and (not "Mtt" in sample.label):
            genpart = Collection(event,"GenPart")
            top = list(filter(lambda x: x.pdgId==6 ,genpart))[0]
            antitop = list(filter(lambda x: x.pdgId==-6 ,genpart))[0]
            Mtt = (top.p4() + antitop.p4()).M()
            if Mtt>=700:
                print(Mtt)
                continue

        jets = Collection(event, "Jet")             # jets[j1].btagDeepFlavB  ---> medium discriminant cut = 0.2783
        tops = Collection(event,"Top")
        met = Object(event, "MET")
        electron = Collection(event, "Electron")
        muon = Collection(event, "Muon")
        nelectron = len(electron)
        nmuon = len(muon)
        ntop = len(tops)
        fatjets = Collection(event,"FatJet")
        h_cutFlow.Fill("PresEvents",1)
        selected = list(filter(lambda x: x.particleNetMD_Xbb>=0.88,fatjets))#fatjet_tag_tot(fatjets)
        if(len(selected)<=0): continue # print(i,selected)
        h_cutFlow.Fill("n Z/H/A Medium > 0",1)
        HLT = Object(event,"HLT")

        HLT_Muon_nominal[0] = HLT.Mu50 or HLT.IsoMu24
        HLT_PFJet_nominal[0] = HLT.AK8PFJet360_TrimMass30 #change
        
        if sample.year== 2016:
            HLT_Electron_nominal[0] = HLT.Ele27_WPTight_Gsf 
            HLT_Photon_nominal[0] = HLT.Photon175 
        else:
            HLT_Electron_nominal[0] = HLT.Ele32_WPTight_Gsf 
            HLT_Photon_nominal[0] = HLT.Photon200

        nZ_medium_nominal = len(list(filter(lambda x:(x.msoftdrop>=60) and (x.msoftdrop<110) and x.deepTagMD_WvsQCD>=0.274,fatjets)))
        
        if i%100 == 0:
            print("Processed ", i+1, " out of ", tree.GetEntries(), " events")

        #chain.GetEntry(i) #this is needed for branches that are not compatible with the NANOAOD convention (e.g. )
        '''
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
        '''
        # this part take care of writing the variations of the MC weight relative to the LHE scale and the PDFs variations
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
 
        all_coll=[]
        all_coll_wp90=[]

        k=0

        for train in training:
            k = k +1
            new_coll=[]
            new_coll_wp90=[]
            score=[]
            score_=-999
            clf = xgb.XGBClassifier()
            clf.load_model(train.files)
            if train.lepton == 1:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.pt_cut[0]) and (x.nu_pt<train.pt_cut[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.el_index != -1)
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
                lista=[]
                score_=-999
                for m in train.var_MET: lista.append(met[m])
                for j in train.var_jet: lista.append(jets[int(top.bjet_index)][j])
                if is_el:
                    for el in train.var_lep: lista.append(electron[int(top.el_index)][el])
                else:
                    for mu in train.var_lep: lista.append(muon[int(top.mu_index)][mu])
                for t in train.var_top:  lista.append(top[t]) 
                
                X = np.array([lista,])

                score_ = clf.predict_proba(X)[0, 1]                
                score.append(score_)
                new_coll.append([top,score_])
                if (score_>train.score_cut): new_coll_wp90.append([top,score_])

            if(len(new_coll)>0): 
                new_coll =  [x for _,x in sorted(zip([new_coll[i][-1] for i in range(len(score))],new_coll))]
                new_coll.reverse()
                if(len(list(filter(lambda x: x[-1]>=0.5,new_coll)))>0): h_nTop_type_0p5.Fill(k,len(list(filter(lambda x: x[-1]>=0.5,new_coll)))) 
    
                if(len(new_coll_wp90)>0):
                    h_nTop_type_wp90.Fill(k,len(new_coll_wp90)) 
                    new_coll_wp90 =  [x for _,x in sorted(zip([new_coll_wp90[i][-1] for i in range(len(new_coll_wp90))],new_coll_wp90))]
                    new_coll_wp90.reverse()
                

            all_coll = all_coll + new_coll
            all_coll_wp90 = all_coll_wp90 + new_coll_wp90
            
            


        if(len(all_coll)==0): continue

        all_coll_0p5 = list(filter(lambda x: x[-1]>=0.5,all_coll))
        h_nTop_type_wp90.Fill(9, len(all_coll_wp90))
        h_nTop_type_0p5.Fill(9, len(all_coll_0p5))

        Top_pt1_nominal[0] = all_coll[0][0].nu_pt 
        Top_eta1_nominal[0] = all_coll[0][0].nu_eta 
        Top_phi1_nominal[0] = all_coll[0][0].nu_phi 
        Top_M1_nominal[0] = all_coll[0][0].nu_M 
        Top_isMerg1_nominal[0] = all_coll[0][0].Is_dR_merg
        Top_Score1_nominal[0] = all_coll[0][1]
        if(all_coll[0][0].High_Truth==0): Top_MC1_nominal[0] = 1
        else: Top_MC1_nominal[0] = 0

        if(all_coll[0][0].el_index!=-1): 
            Top_flavour1_nominal[0] = 11
            if(electron[int(all_coll[0][0].el_index)].charge==1): Top_flavour1_nominal[0] = - Top_flavour1_nominal[0]
        else: 
            Top_flavour1_nominal[0] = 13
            if(muon[int(all_coll[0][0].mu_index)].charge==1): Top_flavour1_nominal[0] = - Top_flavour1_nominal[0]

        if len(all_coll_0p5)>0:
            Top_pt1_0p5_nominal[0] = all_coll_0p5[0][0].nu_pt 
            Top_eta1_0p5_nominal[0] = all_coll_0p5[0][0].nu_eta 
            Top_phi1_0p5_nominal[0] = all_coll_0p5[0][0].nu_phi 
            Top_M1_0p5_nominal[0] = all_coll_0p5[0][0].nu_M 
            Top_isMerg1_0p5_nominal[0] = all_coll_0p5[0][0].Is_dR_merg
            Top_Score1_0p5_nominal[0] = all_coll_0p5[0][1]
            if(all_coll_0p5[0][0].High_Truth==0): Top_MC1_0p5_nominal[0] = 1
            else: Top_MC1_0p5_nominal[0] = 0
            if(all_coll_0p5[0][0].el_index!=-1): 
                Top_flavour1_0p5_nominal[0] = 11
                if(electron[int(all_coll_0p5[0][0].el_index)].charge==1): Top_flavour1_0p5_nominal[0] = - Top_flavour1_0p5_nominal[0]
            else: 
                Top_flavour1_0p5_nominal[0] = 13
                if(muon[int(all_coll_0p5[0][0].mu_index)].charge==1): Top_flavour1_0p5_nominal[0] = - Top_flavour1_0p5_nominal[0]

        else:
            Top_pt1_0p5_nominal[0] = -999 
            Top_eta1_0p5_nominal[0] = -999 
            Top_phi1_0p5_nominal[0] = -999
            Top_M1_0p5_nominal[0] = -999
            Top_isMerg1_0p5_nominal[0] = -999
            Top_Score1_0p5_nominal[0] = -999            
            Top_MC1_0p5_nominal[0] = 0
            Top_flavour1_0p5_nominal[0] = -999

            Top_pt2_0p5_nominal[0] = -999 
            Top_eta2_0p5_nominal[0] = -999 
            Top_phi2_0p5_nominal[0] = -999 
            Top_M2_0p5_nominal[0] = -999 
            Top_isMerg2_0p5_nominal[0] = -999
            Top_Score2_0p5_nominal[0] = -999
            Top_MC2_0p5_nominal[0] = 0
            Top_flavour2_0p5_nominal[0] = -999

            Top_pt3_0p5_nominal[0] = -999 
            Top_eta3_0p5_nominal[0] = -999 
            Top_phi3_0p5_nominal[0] = -999 
            Top_M3_0p5_nominal[0] = -999 
            Top_isMerg3_0p5_nominal[0] = -999
            Top_Score3_0p5_nominal[0] = -999
            Top_MC3_0p5_nominal[0] = 0
            Top_flavour3_0p5_nominal[0] = -999

            Top_pt4_0p5_nominal[0] = -999 
            Top_eta4_0p5_nominal[0] = -999 
            Top_phi4_0p5_nominal[0] = -999 
            Top_M4_0p5_nominal[0] = -999 
            Top_isMerg4_0p5_nominal[0] = -999
            Top_Score4_0p5_nominal[0] = -999
            Top_MC4_0p5_nominal[0] = 0
            Top_flavour4_0p5_nominal[0] = -999


        if len(all_coll_wp90)>0:
            h_cutFlow.Fill("nTop_wp90 > 0",1)
            if((HLT.Mu50) or (HLT.IsoMu24) or (HLT.Ele32_WPTight_Gsf) or (HLT.Photon200) or (HLT.AK8PFJet360_TrimMass30)):h_cutFlow.Fill("Trigger All",1)
            if((HLT.Mu50) or (HLT.IsoMu24) or (HLT.Ele32_WPTight_Gsf) or (HLT.Photon200) ):h_cutFlow.Fill("Trigger No TrimMass30",1)
            Top_pt1_wp90_nominal[0] = all_coll_wp90[0][0].nu_pt 
            Top_eta1_wp90_nominal[0] = all_coll_wp90[0][0].nu_eta 
            Top_phi1_wp90_nominal[0] = all_coll_wp90[0][0].nu_phi 
            Top_M1_wp90_nominal[0] = all_coll_wp90[0][0].nu_M 
            Top_isMerg1_wp90_nominal[0] = all_coll_wp90[0][0].Is_dR_merg
            Top_Score1_wp90_nominal[0] = all_coll_wp90[0][1]
            if(all_coll_wp90[0][0].High_Truth==0): Top_MC1_wp90_nominal[0] = 1
            else: Top_MC1_wp90_nominal[0] = 0

            if(all_coll_wp90[0][0].el_index!=-1): 
                Top_flavour1_wp90_nominal[0] = 11
                if(electron[int(all_coll_wp90[0][0].el_index)].charge==1): Top_flavour1_wp90_nominal[0] = - Top_flavour1_wp90_nominal[0]
            else: 
                Top_flavour1_wp90_nominal[0] = 13
                if(muon[int(all_coll_wp90[0][0].mu_index)].charge==1): Top_flavour1_wp90_nominal[0] = - Top_flavour1_wp90_nominal[0]

        else:
            Top_pt1_wp90_nominal[0] = -999 
            Top_eta1_wp90_nominal[0] = -999 
            Top_phi1_wp90_nominal[0] = -999
            Top_M1_wp90_nominal[0] = -999
            Top_isMerg1_wp90_nominal[0] = -999
            Top_Score1_wp90_nominal[0] = -999            
            Top_MC1_wp90_nominal[0] = 0
            Top_flavour1_wp90_nominal[0] = -999

            Top_pt2_wp90_nominal[0] = -999 
            Top_eta2_wp90_nominal[0] = -999 
            Top_phi2_wp90_nominal[0] = -999 
            Top_M2_wp90_nominal[0] = -999 
            Top_isMerg2_wp90_nominal[0] = -999
            Top_Score2_wp90_nominal[0] = -999
            Top_MC2_wp90_nominal[0] = 0
            Top_flavour2_wp90_nominal[0] = -999

            Top_pt3_wp90_nominal[0] = -999 
            Top_eta3_wp90_nominal[0] = -999 
            Top_phi3_wp90_nominal[0] = -999 
            Top_M3_wp90_nominal[0] = -999 
            Top_isMerg3_wp90_nominal[0] = -999
            Top_Score3_wp90_nominal[0] = -999
            Top_MC3_wp90_nominal[0] = 0
            Top_flavour3_wp90_nominal[0] = -999

            Top_pt4_wp90_nominal[0] = -999 
            Top_eta4_wp90_nominal[0] = -999 
            Top_phi4_wp90_nominal[0] = -999 
            Top_M4_wp90_nominal[0] = -999 
            Top_isMerg4_wp90_nominal[0] = -999
            Top_Score4_wp90_nominal[0] = -999
            Top_MC4_wp90_nominal[0] = 0
            Top_flavour4_wp90_nominal[0] = -999


        if(len(all_coll)>1):
            Top_pt2_nominal[0] = all_coll[1][0].nu_pt 
            Top_eta2_nominal[0] = all_coll[1][0].nu_eta 
            Top_phi2_nominal[0] = all_coll[1][0].nu_phi 
            Top_M2_nominal[0] = all_coll[1][0].nu_M 
            Top_isMerg2_nominal[0] = all_coll[1][0].Is_dR_merg
            Top_Score2_nominal[0] = all_coll[1][1]
            if(all_coll[1][0].High_Truth==0): Top_MC2_nominal[0] = 1
            else: Top_MC2_nominal[0] = 0
            if(all_coll[1][0].el_index!=-1): 
                Top_flavour2_nominal[0] = 11
                if(electron[int(all_coll[1][0].el_index)].charge==1): Top_flavour2_nominal[0] = - Top_flavour2_nominal[0]
            else: 
                Top_flavour2_nominal[0] = 13
                if(muon[int(all_coll[1][0].mu_index)].charge==1): Top_flavour2_nominal[0] = - Top_flavour2_nominal[0]


        else:
            Top_pt2_nominal[0] = -999 
            Top_eta2_nominal[0] = -999 
            Top_phi2_nominal[0] = -999 
            Top_M2_nominal[0] = -999 
            Top_isMerg2_nominal[0] = -999
            Top_Score2_nominal[0] = -999
            Top_MC2_nominal[0] = 0
            Top_flavour2_nominal[0] = -999

            Top_pt3_nominal[0] = -999 
            Top_eta3_nominal[0] = -999 
            Top_phi3_nominal[0] = -999 
            Top_M3_nominal[0] = -999 
            Top_isMerg3_nominal[0] = -999
            Top_Score3_nominal[0] = -999
            Top_MC3_nominal[0] = 0
            Top_flavour3_nominal[0] = -999

            Top_pt4_nominal[0] = -999 
            Top_eta4_nominal[0] = -999 
            Top_phi4_nominal[0] = -999 
            Top_M4_nominal[0] = -999 
            Top_isMerg4_nominal[0] = -999
            Top_Score4_nominal[0] = -999
            Top_MC4_nominal[0] = 0
            Top_flavour4_nominal[0] = -999




        if len(all_coll_0p5)>1:
            Top_pt2_0p5_nominal[0] = all_coll_0p5[1][0].nu_pt 
            Top_eta2_0p5_nominal[0] = all_coll_0p5[1][0].nu_eta 
            Top_phi2_0p5_nominal[0] = all_coll_0p5[1][0].nu_phi 
            Top_M2_0p5_nominal[0] = all_coll_0p5[1][0].nu_M 
            Top_isMerg2_0p5_nominal[0] = all_coll_0p5[1][0].Is_dR_merg
            Top_Score2_0p5_nominal[0] = all_coll_0p5[1][1]
            if(all_coll_0p5[1][0].High_Truth==0): Top_MC2_0p5_nominal[0] = 1
            else: Top_MC2_0p5_nominal[0] = 0
            if(all_coll_0p5[1][0].el_index!=-1): 
                Top_flavour2_0p5_nominal[0] = 11
                if(electron[int(all_coll_0p5[1][0].el_index)].charge==1): Top_flavour2_0p5_nominal[0] = - Top_flavour2_0p5_nominal[0]
            else: 
                Top_flavour2_0p5_nominal[0] = 13
                if(muon[int(all_coll_0p5[1][0].mu_index)].charge==1): Top_flavour2_0p5_nominal[0] = - Top_flavour2_0p5_nominal[0]

        else:

            Top_pt2_0p5_nominal[0] = -999 
            Top_eta2_0p5_nominal[0] = -999 
            Top_phi2_0p5_nominal[0] = -999 
            Top_M2_0p5_nominal[0] = -999 
            Top_isMerg2_0p5_nominal[0] = -999
            Top_Score2_0p5_nominal[0] = -999
            Top_MC2_0p5_nominal[0] = 0
            Top_flavour2_0p5_nominal[0] = -999

            Top_pt3_0p5_nominal[0] = -999 
            Top_eta3_0p5_nominal[0] = -999 
            Top_phi3_0p5_nominal[0] = -999 
            Top_M3_0p5_nominal[0] = -999 
            Top_isMerg3_0p5_nominal[0] = -999
            Top_Score3_0p5_nominal[0] = -999
            Top_MC3_0p5_nominal[0] = 0
            Top_flavour3_0p5_nominal[0] = -999

            Top_pt4_0p5_nominal[0] = -999 
            Top_eta4_0p5_nominal[0] = -999 
            Top_phi4_0p5_nominal[0] = -999 
            Top_M4_0p5_nominal[0] = -999 
            Top_isMerg4_0p5_nominal[0] = -999
            Top_Score4_0p5_nominal[0] = -999
            Top_MC4_0p5_nominal[0] = 0
            Top_flavour4_0p5_nominal[0] = -999


        if len(all_coll_wp90)>1:
            Top_pt2_wp90_nominal[0] = all_coll_wp90[1][0].nu_pt 
            Top_eta2_wp90_nominal[0] = all_coll_wp90[1][0].nu_eta 
            Top_phi2_wp90_nominal[0] = all_coll_wp90[1][0].nu_phi 
            Top_M2_wp90_nominal[0] = all_coll_wp90[1][0].nu_M 
            Top_isMerg2_wp90_nominal[0] = all_coll_wp90[1][0].Is_dR_merg
            Top_Score2_wp90_nominal[0] = all_coll_wp90[1][1]
            if(all_coll_wp90[1][0].High_Truth==0): Top_MC2_wp90_nominal[0] = 1
            else: Top_MC2_wp90_nominal[0] = 0
            if(all_coll_wp90[1][0].el_index!=-1): 
                Top_flavour2_wp90_nominal[0] = 11
                if(electron[int(all_coll_wp90[1][0].el_index)].charge==1): Top_flavour2_wp90_nominal[0] = - Top_flavour2_wp90_nominal[0]
            else: 
                Top_flavour2_wp90_nominal[0] = 13
                if(muon[int(all_coll_wp90[1][0].mu_index)].charge==1): Top_flavour2_wp90_nominal[0] = - Top_flavour2_wp90_nominal[0]

        else:

            Top_pt2_wp90_nominal[0] = -999 
            Top_eta2_wp90_nominal[0] = -999 
            Top_phi2_wp90_nominal[0] = -999 
            Top_M2_wp90_nominal[0] = -999 
            Top_isMerg2_wp90_nominal[0] = -999
            Top_Score2_wp90_nominal[0] = -999
            Top_MC2_wp90_nominal[0] = 0
            Top_flavour2_wp90_nominal[0] = -999

            Top_pt3_wp90_nominal[0] = -999 
            Top_eta3_wp90_nominal[0] = -999 
            Top_phi3_wp90_nominal[0] = -999 
            Top_M3_wp90_nominal[0] = -999 
            Top_isMerg3_wp90_nominal[0] = -999
            Top_Score3_wp90_nominal[0] = -999
            Top_MC3_wp90_nominal[0] = 0
            Top_flavour3_wp90_nominal[0] = -999

            Top_pt4_wp90_nominal[0] = -999 
            Top_eta4_wp90_nominal[0] = -999 
            Top_phi4_wp90_nominal[0] = -999 
            Top_M4_wp90_nominal[0] = -999 
            Top_isMerg4_wp90_nominal[0] = -999
            Top_Score4_wp90_nominal[0] = -999
            Top_MC4_wp90_nominal[0] = 0
            Top_flavour4_wp90_nominal[0] = -999

        if(len(all_coll)>2):
            Top_pt3_nominal[0] = all_coll[2][0].nu_pt 
            Top_eta3_nominal[0] = all_coll[2][0].nu_eta 
            Top_phi3_nominal[0] = all_coll[2][0].nu_phi 
            Top_M3_nominal[0] = all_coll[2][0].nu_M 
            Top_isMerg3_nominal[0] = all_coll[2][0].Is_dR_merg
            Top_Score3_nominal[0] = all_coll[2][1]
            if(all_coll[2][0].High_Truth==0): Top_MC3_nominal[0] = 1
            else: Top_MC3_nominal[0] = 0
            if(all_coll[2][0].el_index!=-1): 
                Top_flavour3_nominal[0] = 11
                if(electron[int(all_coll[2][0].el_index)].charge==1): Top_flavour3_nominal[0] = - Top_flavour3_nominal[0]
            else: 
                Top_flavour3_nominal[0] = 13
                if(muon[int(all_coll[2][0].mu_index)].charge==1): Top_flavour3_nominal[0] = - Top_flavour3_nominal[0]

        else:
            Top_pt3_nominal[0] = -999 
            Top_eta3_nominal[0] = -999 
            Top_phi3_nominal[0] = -999 
            Top_M3_nominal[0] = -999 
            Top_isMerg3_nominal[0] = -999
            Top_Score3_nominal[0] = -999
            Top_MC3_nominal[0] = 0
            Top_flavour3_nominal[0] = -999

            Top_pt4_nominal[0] = -999 
            Top_eta4_nominal[0] = -999 
            Top_phi4_nominal[0] = -999 
            Top_M4_nominal[0] = -999 
            Top_isMerg4_nominal[0] = -999
            Top_Score4_nominal[0] = -999
            Top_MC4_nominal[0] = 0
            Top_flavour4_nominal[0] = -999

        if len(all_coll_0p5)>2:
            Top_pt3_0p5_nominal[0] = all_coll_0p5[2][0].nu_pt 
            Top_eta3_0p5_nominal[0] = all_coll_0p5[2][0].nu_eta 
            Top_phi3_0p5_nominal[0] = all_coll_0p5[2][0].nu_phi 
            Top_M3_0p5_nominal[0] = all_coll_0p5[2][0].nu_M 
            Top_isMerg3_0p5_nominal[0] = all_coll_0p5[2][0].Is_dR_merg
            Top_Score3_0p5_nominal[0] = all_coll_0p5[2][1]
            if(all_coll_0p5[2][0].High_Truth==0): Top_MC3_0p5_nominal[0] = 1
            else: Top_MC3_0p5_nominal[0] = 0
            if(all_coll_0p5[2][0].el_index!=-1): 
                Top_flavour3_0p5_nominal[0] = 11
                if(electron[int(all_coll_0p5[2][0].el_index)].charge==1): Top_flavour3_0p5_nominal[0] = - Top_flavour3_0p5_nominal[0]
            else: 
                Top_flavour3_0p5_nominal[0] = 13
                if(muon[int(all_coll_0p5[2][0].mu_index)].charge==1): Top_flavour3_0p5_nominal[0] = - Top_flavour3_0p5_nominal[0]

        else:

            Top_pt3_0p5_nominal[0] = -999 
            Top_eta3_0p5_nominal[0] = -999 
            Top_phi3_0p5_nominal[0] = -999 
            Top_M3_0p5_nominal[0] = -999 
            Top_isMerg3_0p5_nominal[0] = -999
            Top_Score3_0p5_nominal[0] = -999
            Top_MC3_0p5_nominal[0] = 0
            Top_flavour3_0p5_nominal[0] = -999

            Top_pt4_0p5_nominal[0] = -999 
            Top_eta4_0p5_nominal[0] = -999 
            Top_phi4_0p5_nominal[0] = -999 
            Top_M4_0p5_nominal[0] = -999 
            Top_isMerg4_0p5_nominal[0] = -999
            Top_Score4_0p5_nominal[0] = -999
            Top_MC4_0p5_nominal[0] = 0
            Top_flavour4_0p5_nominal[0] = -999



        if len(all_coll_wp90)>2:
            Top_pt3_wp90_nominal[0] = all_coll_wp90[2][0].nu_pt 
            Top_eta3_wp90_nominal[0] = all_coll_wp90[2][0].nu_eta 
            Top_phi3_wp90_nominal[0] = all_coll_wp90[2][0].nu_phi 
            Top_M3_wp90_nominal[0] = all_coll_wp90[2][0].nu_M 
            Top_isMerg3_wp90_nominal[0] = all_coll_wp90[2][0].Is_dR_merg
            Top_Score3_wp90_nominal[0] = all_coll_wp90[2][1]
            if(all_coll_wp90[2][0].High_Truth==0): Top_MC3_wp90_nominal[0] = 1
            else: Top_MC3_wp90_nominal[0] = 0
            if(all_coll_wp90[2][0].el_index!=-1): 
                Top_flavour3_wp90_nominal[0] = 11
                if(electron[int(all_coll_wp90[2][0].el_index)].charge==1): Top_flavour3_wp90_nominal[0] = - Top_flavour3_wp90_nominal[0]
            else: 
                Top_flavour3_wp90_nominal[0] = 13
                if(muon[int(all_coll_wp90[2][0].mu_index)].charge==1): Top_flavour3_wp90_nominal[0] = - Top_flavour3_wp90_nominal[0]
        else:

            Top_pt3_wp90_nominal[0] = -999 
            Top_eta3_wp90_nominal[0] = -999 
            Top_phi3_wp90_nominal[0] = -999 
            Top_M3_wp90_nominal[0] = -999 
            Top_isMerg3_wp90_nominal[0] = -999
            Top_Score3_wp90_nominal[0] = -999
            Top_MC3_wp90_nominal[0] = 0
            Top_flavour3_wp90_nominal[0] = -999

            Top_pt4_wp90_nominal[0] = -999 
            Top_eta4_wp90_nominal[0] = -999 
            Top_phi4_wp90_nominal[0] = -999 
            Top_M4_wp90_nominal[0] = -999 
            Top_isMerg4_wp90_nominal[0] = -999
            Top_Score4_wp90_nominal[0] = -999
            Top_MC4_wp90_nominal[0] = 0
            Top_flavour4_wp90_nominal[0] = -999


        if(len(all_coll)>3):
            Top_pt4_nominal[0] = all_coll[3][0].nu_pt 
            Top_eta4_nominal[0] = all_coll[3][0].nu_eta 
            Top_phi4_nominal[0] = all_coll[3][0].nu_phi 
            Top_M4_nominal[0] = all_coll[3][0].nu_M 
            Top_isMerg4_nominal[0] = all_coll[3][0].Is_dR_merg
            Top_Score4_nominal[0] = all_coll[3][1]
            if(all_coll[3][0].High_Truth==0): Top_MC4_nominal[0] = 1
            else: Top_MC4_nominal[0] = 0
            if(all_coll[3][0].el_index!=-1): 
                Top_flavour4_nominal[0] = 11
                if(electron[int(all_coll[3][0].el_index)].charge==1): Top_flavour4_nominal[0] = - Top_flavour4_nominal[0]
            else: 
                Top_flavour4_nominal[0] = 13
                if(muon[int(all_coll[3][0].mu_index)].charge==1): Top_flavour4_nominal[0] = - Top_flavour4_nominal[0]

        else:
            Top_pt4_nominal[0] = -999 
            Top_eta4_nominal[0] = -999 
            Top_phi4_nominal[0] = -999 
            Top_M4_nominal[0] = -999 
            Top_isMerg4_nominal[0] = -999
            Top_Score4_nominal[0] = -999
            Top_MC4_nominal[0] = 0
            Top_flavour4_nominal[0] = -999



        if len(all_coll_0p5)>3:
            Top_pt4_0p5_nominal[0] = all_coll_0p5[3][0].nu_pt 
            Top_eta4_0p5_nominal[0] = all_coll_0p5[3][0].nu_eta 
            Top_phi4_0p5_nominal[0] = all_coll_0p5[3][0].nu_phi 
            Top_M4_0p5_nominal[0] = all_coll_0p5[3][0].nu_M 
            Top_isMerg4_0p5_nominal[0] = all_coll_0p5[3][0].Is_dR_merg
            Top_Score4_0p5_nominal[0] = all_coll_0p5[3][1]
            if(all_coll_0p5[3][0].High_Truth==0): Top_MC4_0p5_nominal[0] = 1
            else: Top_MC4_0p5_nominal[0] = 0
            if(all_coll_0p5[3][0].el_index!=-1): 
                Top_flavour4_0p5_nominal[0] = 11
                if(electron[int(all_coll_0p5[3][0].el_index)].charge==1): Top_flavour4_0p5_nominal[0] = - Top_flavour4_0p5_nominal[0]
            else: 
                Top_flavour4_0p5_nominal[0] = 13
                if(muon[int(all_coll_0p5[3][0].mu_index)].charge==1): Top_flavour4_0p5_nominal[0] = - Top_flavour4_0p5_nominal[0]

        else:

            Top_pt4_0p5_nominal[0] = -999 
            Top_eta4_0p5_nominal[0] = -999 
            Top_phi4_0p5_nominal[0] = -999 
            Top_M4_0p5_nominal[0] = -999 
            Top_isMerg4_0p5_nominal[0] = -999
            Top_Score4_0p5_nominal[0] = -999
            Top_MC4_0p5_nominal[0] = 0
            Top_flavour4_0p5_nominal[0] = -999




        if len(all_coll_wp90)>3:
            Top_pt4_wp90_nominal[0] = all_coll_wp90[3][0].nu_pt 
            Top_eta4_wp90_nominal[0] = all_coll_wp90[3][0].nu_eta 
            Top_phi4_wp90_nominal[0] = all_coll_wp90[3][0].nu_phi 
            Top_M4_wp90_nominal[0] = all_coll_wp90[3][0].nu_M 
            Top_isMerg4_wp90_nominal[0] = all_coll_wp90[3][0].Is_dR_merg
            Top_Score4_wp90_nominal[0] = all_coll_wp90[3][1]
            if(all_coll_wp90[3][0].High_Truth==0): Top_MC4_wp90_nominal[0] = 1
            else: Top_MC4_wp90_nominal[0] = 0
            if(all_coll_wp90[3][0].el_index!=-1): 
                Top_flavour4_wp90_nominal[0] = 11
                if(electron[int(all_coll_wp90[3][0].el_index)].charge==1): Top_flavour4_wp90_nominal[0] = - Top_flavour4_wp90_nominal[0]
            else: 
                Top_flavour4_wp90_nominal[0] = 13
                if(muon[int(all_coll_wp90[3][0].mu_index)].charge==1): Top_flavour4_wp90_nominal[0] = - Top_flavour4_wp90_nominal[0]
        else:

            Top_pt4_wp90_nominal[0] = -999 
            Top_eta4_wp90_nominal[0] = -999 
            Top_phi4_wp90_nominal[0] = -999 
            Top_M4_wp90_nominal[0] = -999 
            Top_isMerg4_wp90_nominal[0] = -999
            Top_Score4_wp90_nominal[0] = -999
            Top_MC4_wp90_nominal[0] = 0
            Top_flavour4_wp90_nominal[0] = -999




        #systTree.setWeightName("w",copy.deepcopy(w[0]))
        systTree.fillTreesSysts(trees, scenario)

    outTreeFile.cd()
    if scenario == 'nominal':
        trees[0].Write()
        h_nTop_type_wp90.Write()
        h_nTop_type_0p5.Write()
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


for scenario in ["nominal"]: # scenarios:
    reco(scenario, isMC,addPDF, training)


endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
