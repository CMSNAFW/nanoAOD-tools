#!/bin/env python
import optparse
from plots.plotUtils import *
usage = 'python plotPrePostFit.py -o fitfolder' #fit folder is the folder containing the fitDiagnostic.root file

signal = "Tprime_tHq_1800LH"
#samples_CR0B = ["QCD", "DDFitWJetsTT_MttST", signal]
#samples_CR0B = ["QCD", signal] # "DDFitWJetsTT_MttST"]
#samples_SRT = ["QCD", "DDFitWJetsTT_MttST", signal]
#samples_SRW = ["QCD", "DDFitWJetsTT_MttST", signal]
#samples_SR2B = ["QCD", "DDFitWJetsTT_MttST", signal]
samples = ["ST","WJets","QCD", "TT_Mtt",signal]

regions_mu = {
    "VR6":("h_FatJet_M_nominal_TopL_FatJetL_AK8HighPt", "VR6_muon", "AK8L,TopL mu"),
    "VR5":("h_FatJet_M_nominal_TopT_FatJetL_AK8HighPt", "VR5_muon", "AK8L,TopT mu"),
    #"VR2":("h_Tprime_M_nominal_TopL_FatJetL_AK8HighPt", "VR2_muon", "AK8L,TopL mu"),
    #"VR1":("h_Tprime_M_nominal_TopT_FatJetL_AK8HighPt", "VR1_muon", "AK8L,TopT mu"),
    "SRT":("h_jets_best_Wprime_m_SRT", "SRT_muon", "RT_{A} muon"),
    "SRW":("h_jets_best_Wprime_m_SRW", "SRW_muon", "RW\'_{A} muon"),
    "SR2B":("h_jets_best_Wprime_m_SR2B", "SR2B_muon", "R2B_{A} muon"),
    }
regions_ele = {
    "VR6":("h_FatJet_M_nominal_TopL_FatJetL_AK8HighPt", "VR6_electron", "AK8L,TopL el"),
    "VR5":("h_FatJet_M_nominal_TopT_FatJetL_AK8HighPt", "VR5_electron", "AK8L,TopT el"),
    #"VR2":("h_Tprime_M_nominal_TopL_FatJetL_AK8HighPt", "VR2_electron", "AK8L,TopL el"),
    #"VR1":("h_Tprime_M_nominal_TopT_FatJetL_AK8HighPt", "VR1_electron", "AK8L,TopT el"),
    "CR0B":("h_jets_best_Wprime_m_CR0B", "CR0B_electron", "R0_{A} electron"),
    "SRT":("h_jets_best_Wprime_m_SRT", "SRT_electron", "RT_{A} electron"),
    "SRW":("h_jets_best_Wprime_m_SRW", "SRW_electron", "RW\'_{A} electron"),
    "SR2B":("h_jets_best_Wprime_m_SR2B", "SR2B_electron", "R2B_{A} electron"),
    }

lep = ""
fitPhase = "prefit"
#fitPhase = "fit_b"
#fitPhase = "fit_s"
#fitfolder = "/afs/cern.ch/user/o/oiorio/public/xAgostino/Wprime_v22/fixed/an_v22explin_sigh/fitDiagnostics.root" # <--- SR
#fitfolder = "/afs/cern.ch/user/o/oiorio/public/xAgostino/Wprime_v22/an_v22explincr0b/fitDiagnostics.root" # <--- CR0B
#fitfolder = "/afs/cern.ch/user/f/fcarneva/CMSSW_10_2_5/src/Stat/Limits/test/fitValid_v6_2018/fitDiagnosticsTest.root"
fitfolder = "/afs/cern.ch/user/f/fcarneva/CMSSW_10_2_5/src/Stat/Limits/test/fitValid_NoBDTPN_2017/fitDiagnosticsTest.root"


#histfolder = "/eos/user/a/adeiorio/Wprime/nosynch/v18/plot_fit3Apr"
#histfolder = "/eos/user/f/fcarneva/Tprime/nosynch/UL_v18/plot/"
histfolder = "/eos/user/f/fcarneva/Tprime/nosynch/UL_v11/plot/"

print('hello! Starting now')
blind = False
lep = "muon"
if lep == "muon":
    plot(histfolder, fitfolder, fitPhase, regions_mu["VR6"], samples, blind)
    plot(histfolder, fitfolder, fitPhase, regions_mu["VR5"], samples, blind)
    #plot(histfolder, fitfolder, fitPhase, regions_mu["VR1"], samples, blind)
    #plot(histfolder, fitfolder, fitPhase, regions_mu["VR2"], samples, blind)
lep = "electron"
if lep == "electron":
    plot(histfolder, fitfolder, fitPhase, regions_ele["VR6"], samples, blind)
    plot(histfolder, fitfolder, fitPhase, regions_ele["VR5"], samples, blind)
    #plot(histfolder, fitfolder, fitPhase, regions_ele["VR1"], samples, blind)
    #plot(histfolder, fitfolder, fitPhase, regions_ele["VR2"], samples, blind)

#lep = "muele"
if lep == "muele":
    plot(histfolder, fitfolder, fitPhase, regions_mu["CR0B"], samples_CR0B, False)
    plot(histfolder, fitfolder, fitPhase, regions_ele["CR0B"], samples_CR0B, False)
    '''
    plot(histfolder, fitfolder, fitPhase, regions_mu["SR2B"], samples_CR0B, blind)
    plot(histfolder, fitfolder, fitPhase, regions_ele["SR2B"], samples_CR0B, blind)
    plot(histfolder, fitfolder, fitPhase, regions_mu["SRT"], samples_CR0B, blind)
    plot(histfolder, fitfolder, fitPhase, regions_ele["SRT"], samples_CR0B, blind)
    plot(histfolder, fitfolder, fitPhase, regions_mu["SRW"], samples_CR0B, blind)
    plot(histfolder, fitfolder, fitPhase, regions_ele["SRW"], samples_CR0B, blind)
    '''

