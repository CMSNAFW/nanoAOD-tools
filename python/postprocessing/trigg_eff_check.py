import ROOT
import math
from array import array
#from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *
import sys
import os
import copy

folder = 'Trigger_v0'
inputpath = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Tprime/nosynch/' + folder + '/'
plotpath = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Tprime/nosynch/' + folder + '/plot/'

if not os.path.exists(plotpath):
    os.makedirs(plotpath)

period = sys.argv[1]

def printh(filename, period, h, plotpath):
    c = ROOT.TCanvas(filename + '_' + period + '_' + h.GetName(), filename + '_' + period + '_' + h.GetName())
    if 'Eff' in h.GetName():
        h.SetMaximum(1.)
    h.Draw("COLZTEXTE")
    c.Print(plotpath + c.GetName() + '.png')
    c.Print(plotpath + c.GetName() + '.pdf')

inpfiles = {#"muon_16":["DataMu_2016", "DataEle_2016", "DataPh_2016", "TT_dilep_2016"],
            #"electron_16":["DataMu_2016", "DataEle_2016", "DataPh_2016", "TT_dilep_2016"],
            "muon_17":["DataMu_2017","DataEle_2017","DataPh_2017","DataHT_2017","TT_dilep_2017"],
            "electron_17":["DataMu_2017","DataEle_2017","DataPh_2017","DataHT_2017","TT_dilep_2017"],
            "jet_17":["DataMu_2017","DataEle_2017","DataPh_2017","DataHT_2017","TT_Mtt_2017","QCD_2017","WJets_2017","ST_2017"],
            "muon_18":["DataMu_2018","DataEle_2018","DataHT_2018","TT_dilep_2018"],
            "electron_18":["DataMu_2018", "DataEle_2018", "DataHT_2018","TT_dilep_2018"],
            "jet_18":["DataMu_2018","DataEle_2018","DataHT_2018","TT_Mtt_2018","QCD_2018","WJets_2018","ST_2018"],
        }

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.TH1.SetDefaultSumw2()
ROOT.TGaxis.SetMaxDigits(4)
ROOT.gStyle.SetPaintTextFormat('4.3f')


edges_mux = array.array('f', [0.0,0.8,1.444,1.566,2.0,2.5])
nbins_mux = len(edges_mux)-1
edges_muy = array.array('f', [30.,50.,100.,200.,500.])
nbins_muy = len(edges_muy)-1

edges_muy1D = array.array('f', [10.,20.,30.,40.,50.,75.,100.,150.,200.,350.,500.])
nbins_muy1D = len(edges_muy1D)-1

#edges_muxjet = array.array('f', [150.,500.,700,900.,1200.])
edges_muxjet = array.array('f', [10.,20.,30.,40.,50.,75.,100.,150.,200.,350.,500.])
nbins_muxjet = len(edges_muxjet)-1
edges_muyjet = array.array('f', [0.,20.,40.,60.,90.,120.,150.,220.])
nbins_muyjet = len(edges_muyjet)-1

if 'muon' in period:
    edges_mux = array.array('f', [0.0,0.9,1.2,2.1,2.4])
    nbins_mux = len(edges_mux)-1
    edges_muy = array.array('f', [30.,50.,100.,200.,500])
    nbins_muy = len(edges_muy)-1
if 'jet' in period:
    edges_mux = array.array('f', [150.,500.,700,900.,1200.])
    nbins_mux = len(edges_mux)-1
    edges_muy = array.array('f', [60.,90.,120.,150.,220.])
    nbins_muy = len(edges_muy)-1

h_HLT_TightLep_data_num = ROOT.TH2F("HLT_TightLep_data_num", "HLT_TightLep_data_num", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_TightLep_data_den = ROOT.TH2F("HLT_TightLep_data_den", "HLT_TightLep_data_den", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_TightLep_MC_num = ROOT.TH2F("HLT_TightLep_MC_num", "HLT_TightLep_MC_num", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_TightLep_MC_den = ROOT.TH2F("HLT_TightLep_MC_den", "HLT_TightLep_MC_den", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_TightLep_MC_Eff = ROOT.TH2F("h2D_HLT_TightLep_MC_Eff", "h_TightLep", nbins_mux, edges_mux, nbins_muy, edges_muy)

h1D_HLT_TightLep_data_num = ROOT.TH1F("h1D_HLT_TightLep_data_num", "h1D_HLT_TightLep_data_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLep_data_den = ROOT.TH1F("h1D_HLT_TightLep_data_den", "h1D_HLT_TightLep_data_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLep_MC_num = ROOT.TH1F("h1D_HLT_TightLep_MC_num", "h1D_HLT_TightLep_MC_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLep_MC_den = ROOT.TH1F("h1D_HLT_TightLep_MC_den", "h1D_HLT_TightLep_MC_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLep_MC_Eff = ROOT.TH1F("h1D_HLT_TightLep_MC_Eff", "h1D_TightLep",  nbins_muy1D, edges_muy1D)


h_HLT_TightLepJet_data_num = ROOT.TH2F("HLT_TightLepJet_data_num", "HLT_TightLepJet_data_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TightLepJet_data_den = ROOT.TH2F("HLT_TightLepJet_data_den", "HLT_TightLepJet_data_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TightLepJet_MC_num = ROOT.TH2F("HLT_TightLepJet_MC_num", "HLT_TightLepJet_MC_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TightLepJet_MC_den = ROOT.TH2F("HLT_TightLepJet_MC_den", "HLT_TightLepJet_MC_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TightLepJet_MC_Eff = ROOT.TH2F("h2D_HLT_TightLepJet_MC_Eff", "h_TightLepJet", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)

h1D_HLT_TightLepJet_data_num = ROOT.TH1F("h1D_HLT_TightLepJet_data_num", "h1D_HLT_TightLepJet_data_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLepJet_data_den = ROOT.TH1F("h1D_HLT_TightLepJet_data_den", "h1D_HLT_TightLepJet_data_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLepJet_MC_num = ROOT.TH1F("h1D_HLT_TightLepJet_MC_num", "h1D_HLT_TightLepJet_MC_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLepJet_MC_den = ROOT.TH1F("h1D_HLT_TightLepJet_MC_den", "h1D_HLT_TightLepJet_MC_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TightLepJet_MC_Eff = ROOT.TH1F("h1D_HLT_TightLepJet_MC_Eff", "h1D_TightLepJet",  nbins_muy1D, edges_muy1D)



h_HLT_Top_data_num = ROOT.TH2F("HLT_Top_data_num", "HLT_Top_data_num", nbins_mux, edges_mux, nbins_muy, edges_muy)                                                             
h_HLT_Top_data_den = ROOT.TH2F("HLT_Top_data_den", "HLT_Top_data_den", nbins_mux, edges_mux, nbins_muy, edges_muy)                                                          
h_HLT_Top_MC_num = ROOT.TH2F("HLT_Top_MC_num", "HLT_Top_MC_num", nbins_mux, edges_mux, nbins_muy, edges_muy)                                                                              
h_HLT_Top_MC_den = ROOT.TH2F("HLT_Top_MC_den", "HLT_Top_MC_den", nbins_mux, edges_mux, nbins_muy, edges_muy)                              
h_HLT_Top_MC_Eff = ROOT.TH2F("h2D_HLT_Top_MC_Eff", "h_Top", nbins_mux, edges_mux, nbins_muy, edges_muy)

h1D_HLT_Top_data_num = ROOT.TH1F("h1D_HLT_Top_data_num", "h1D_HLT_Top_data_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_Top_data_den = ROOT.TH1F("h1D_HLT_Top_data_den", "h1D_HLT_Top_data_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_Top_MC_num = ROOT.TH1F("h1D_HLT_Top_MC_num", "h1D_HLT_Top_MC_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_Top_MC_den = ROOT.TH1F("h1D_HLT_Top_MC_den", "h1D_HLT_Top_MC_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_Top_MC_Eff = ROOT.TH1F("h1D_HLT_Top_MC_Eff", "h1D_Top",  nbins_muy1D, edges_muy1D)


h_HLT_TopJet_data_num = ROOT.TH2F("HLT_TopJet_data_num", "HLT_TopJet_data_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)                                                                                                                                                             
h_HLT_TopJet_data_den = ROOT.TH2F("HLT_TopJet_data_den", "HLT_TopJet_data_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)                                                                                                                     
h_HLT_TopJet_MC_num = ROOT.TH2F("HLT_TopJet_MC_num", "HLT_TopJet_MC_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)                                                                                                                              
h_HLT_TopJet_MC_den = ROOT.TH2F("HLT_TopJet_MC_den", "HLT_TopJet_MC_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)                                                                                                                                 
h_HLT_TopJet_MC_Eff = ROOT.TH2F("h2D_HLT_TopJet_MC_Eff", "h_TopJet", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)                                                                                                                                                                             
 
h1D_HLT_TopJet_data_num = ROOT.TH1F("h1D_HLT_TopJet_data_num", "h1D_HLT_TopJet_data_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TopJet_data_den = ROOT.TH1F("h1D_HLT_TopJet_data_den", "h1D_HLT_TopJet_data_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TopJet_MC_num = ROOT.TH1F("h1D_HLT_TopJet_MC_num", "h1D_HLT_TopJet_MC_num",  nbins_muy1D, edges_muy1D)
h1D_HLT_TopJet_MC_den = ROOT.TH1F("h1D_HLT_TopJet_MC_den", "h1D_HLT_TopJet_MC_den",  nbins_muy1D, edges_muy1D)
h1D_HLT_TopJet_MC_Eff = ROOT.TH1F("h1D_HLT_TopJet_MC_Eff", "h1D_TopJet",  nbins_muy1D, edges_muy1D)


h_HLT_CR_data_num = ROOT.TH2F("HLT_CR_data_num", "HLT_CR_data_num", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_data_den = ROOT.TH2F("HLT_CR_data_den", "HLT_CR_data_den", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_MC_num = ROOT.TH2F("HLT_CR_MC_num", "HLT_CR_MC_num", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_MC_den = ROOT.TH2F("HLT_CR_MC_den", "HLT_CR_MC_den", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_MC_Eff = ROOT.TH2F("h2D_HLT_CR_MC_Eff", "h_CR", nbins_mux, edges_mux, nbins_muy, edges_muy)



fileout = ROOT.TFile(inputpath + period + ".root", "RECREATE")
for inpfile in inpfiles[period]:
    infile = ROOT.TFile.Open(inputpath +  inpfile + "/" + inpfile + ".root")
    print 'Opening ' + infile.GetName()
    tree = infile.Get("events_all")
    h_HLT_CR_num = ROOT.TH2F("HLT_CR_num", "HLT_CR_num", nbins_mux, edges_mux, nbins_muy, edges_muy)#nbins, edges)
    h_HLT_CR_den = ROOT.TH2F("HLT_CR_den", "HLT_CR_den", nbins_mux, edges_mux, nbins_muy, edges_muy) #nbins, edges)


    h_HLT_Top_num = ROOT.TH2F("HLT_Top_num", "HLT_Top_num", nbins_mux, edges_mux, nbins_muy, edges_muy)#nbins, edges)
    h_HLT_Top_den = ROOT.TH2F("HLT_Top_den", "HLT_Top_den", nbins_mux, edges_mux, nbins_muy, edges_muy) #nbins, edges)

    h_HLT_TightLep_num = ROOT.TH2F("HLT_TightLep_num", "HLT_TightLep_num", nbins_mux, edges_mux, nbins_muy, edges_muy)#nbins, edges)
    h_HLT_TightLep_den = ROOT.TH2F("HLT_TightLep_den", "HLT_TightLep_den", nbins_mux, edges_mux, nbins_muy, edges_muy) #nbins, edges)

    h1D_HLT_TightLep_num = ROOT.TH1F("h1D_HLT_TightLep_num", "h1D_HLT_TightLep_num", nbins_muy1D, edges_muy1D)
    h1D_HLT_TightLep_den = ROOT.TH1F("h1D_HLT_TightLep_den", "h1D_HLT_TightLep_den", nbins_muy1D, edges_muy1D)

    h1D_HLT_Top_num = ROOT.TH1F("h1D_HLT_Top_num", "h1D_HLT_Top_num", nbins_muy1D, edges_muy1D)
    h1D_HLT_Top_den = ROOT.TH1F("h1D_HLT_Top_den", "h1D_HLT_Top_den", nbins_muy1D, edges_muy1D)



    h_HLT_TopJet_num = ROOT.TH2F("HLT_TopJet_num", "HLT_TopJet_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)#nbins, edges)
    h_HLT_TopJet_den = ROOT.TH2F("HLT_TopJet_den", "HLT_TopJet_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet) #nbins, edges)

    h_HLT_TightLepJet_num = ROOT.TH2F("HLT_TightLepJet_num", "HLT_TightLepJet_num", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)#nbins, edges)
    h_HLT_TightLepJet_den = ROOT.TH2F("HLT_TightLepJet_den", "HLT_TightLepJet_den", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet) #nbins, edges)

    h1D_HLT_TightLepJet_num = ROOT.TH1F("h1D_HLT_TightLepJet_num", "h1D_HLT_TightLepJet_num", nbins_muy1D, edges_muy1D)
    h1D_HLT_TightLepJet_den = ROOT.TH1F("h1D_HLT_TightLepJet_den", "h1D_HLT_TightLepJet_den", nbins_muy1D, edges_muy1D)

    h1D_HLT_TopJet_num = ROOT.TH1F("h1D_HLT_TopJet_num", "h1D_HLT_TopJet_num", nbins_muy1D, edges_muy1D)
    h1D_HLT_TopJet_den = ROOT.TH1F("h1D_HLT_TopJet_den", "h1D_HLT_TopJet_den", nbins_muy1D, edges_muy1D)

    print("Add w_nominal* and change for different region of top_region_nominal!!! Ricordaaa quando fai l'efficiency con tutti i file aggiungi w_Dcount_nominal* per evitare il double counting di TT che invece non va aggiunto quando usi solo TT_dilep  Attenzione hai unito Top+Tight Regions per glie elettroni")
    if 'muon' in period:
        if 'Data' in infile.GetName():
            tree.Project("HLT_TightLep_num", "muon_pt:abs(muon_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_TightLep_den", "muon_pt:abs(muon_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_TightLep_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TightLep_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_Top_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_Top_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("HLT_Top_num", "muon_pt:abs(muon_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")                           
            tree.Project("HLT_Top_den", "muon_pt:abs(muon_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")



            tree.Project("HLT_TightLepJet_num", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("HLT_TightLepJet_den", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_TightLepJet_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("h1D_HLT_TightLepJet_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_TopJet_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("h1D_HLT_TopJet_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("HLT_TopJet_num", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("HLT_TopJet_den", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")




           

        elif "TT_dilep" in infile.GetName():
            tree.Project("HLT_TightLep_num", "muon_pt:abs(muon_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_TightLep_den", "muon_pt:abs(muon_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")
            
            tree.Project("h1D_HLT_TightLep_num", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TightLep_den", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_Top_num", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_Top_den", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("HLT_Top_num", "muon_pt:abs(muon_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_Top_den", "muon_pt:abs(muon_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")


            tree.Project("HLT_TightLepJet_num", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("HLT_TightLepJet_den", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_TightLepJet_num", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("h1D_HLT_TightLepJet_den", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]==-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("h1D_HLT_TopJet_num", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("h1D_HLT_TopJet_den", "muon_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

            tree.Project("HLT_TopJet_num", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0] || HLT_PFJet_nominal[0])")
            tree.Project("HLT_TopJet_den", "FatJet_msd_nominal:muon_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==0 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])")

    
    elif 'electron' in period:
        if 'Data' in infile.GetName():
            tree.Project("HLT_TightLep_num", "electron_pt:abs(electron_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_TightLep_den", "electron_pt:abs(electron_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")

            tree.Project("h1D_HLT_TightLep_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TightLep_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")


            tree.Project("h1D_HLT_Top_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_Top_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")


            tree.Project("HLT_Top_num", "electron_pt:abs(electron_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_Top_den", "electron_pt:abs(electron_eta)", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")
    

            tree.Project("HLT_TightLepJet_num", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_TightLepJet_den", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")

            tree.Project("h1D_HLT_TightLepJet_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TightLepJet_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")

            tree.Project("h1D_HLT_TopJet_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TopJet_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")

            tree.Project("HLT_TopJet_num", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_TopJet_den", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*w_nominal*PFSF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")


        elif "TT_dilep" in infile.GetName():
            tree.Project("HLT_TightLep_num", "electron_pt:abs(electron_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")                     
            tree.Project("HLT_TightLep_den", "electron_pt:abs(electron_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")            

            tree.Project("h1D_HLT_TightLep_num", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_TightLep_den", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")

            tree.Project("h1D_HLT_Top_num", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("h1D_HLT_Top_den", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")


            tree.Project("HLT_Top_num", "electron_pt:abs(electron_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0])*(HLT_Muon_nominal[0])")
            tree.Project("HLT_Top_den", "electron_pt:abs(electron_eta)", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")




            tree.Project("HLT_TightLepJet_num", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")                                  
            tree.Project("HLT_TightLepJet_den", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")

            tree.Project("h1D_HLT_TightLepJet_num", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")                      
            tree.Project("h1D_HLT_TightLepJet_den", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>=-1)*(HLT_Muon_nominal[0])")                                                                                                                                       
            tree.Project("h1D_HLT_TopJet_num", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")                          
            tree.Project("h1D_HLT_TopJet_den", "electron_pt", "PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")

            tree.Project("HLT_TopJet_num", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_PFJet_nominal[0])*(HLT_Muon_nominal[0])")         
            tree.Project("HLT_TopJet_den", "FatJet_msd_nominal:electron_pt", "(FatJet_pt_nominal<500)*PFSF*electron_SF*muon_SF*puSF*isdileptonic*w_pt*(isPromptEle[0]==1 && top_region_nominal[0]>-1)*(HLT_Muon_nominal[0])")


       
    else:
        if 'Data' in infile.GetName():
            tree.Project("HLT_CR_num", "FatJet_msd_nominal:FatJet_pt_nominal", "w_nominal*PFSF*puSF*(isdileptonic[0]==0)*w_pt*(top_region_nominal[0]==-1 && AK8_region_nominal[0]==0)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_Muon_nominal[0])*(HLT_PFJet_nominal[0])")
            tree.Project("HLT_CR_den", "FatJet_msd_nominal:FatJet_pt_nominal", "w_nominal*PFSF*puSF*(isdileptonic[0]==0)*w_pt*(top_region_nominal[0]==-1 && AK8_region_nominal[0]==0)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_Muon_nominal[0])")
        else:
            tree.Project("HLT_CR_num", "FatJet_msd_nominal:FatJet_pt_nominal", "w_nominal*PFSF*w_Dcount*max(electron_SF,muon_SF)*puSF*(isdileptonic[0]==0)*w_pt*(top_region_nominal[0]==-1 && AK8_region_nominal[0]==0)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_Muon_nominal[0])*(HLT_PFJet_nominal[0])")
            tree.Project("HLT_CR_den", "FatJet_msd_nominal:FatJet_pt_nominal", "w_nominal*PFSF*w_Dcount*max(electron_SF,muon_SF)*puSF*(isdileptonic[0]==0)*w_pt*(top_region_nominal[0]==-1 && AK8_region_nominal[0]==0)*(HLT_Electron_nominal[0] || HLT_Photon_nominal[0] || HLT_Muon_nominal[0])")
        
    print h_HLT_TightLep_num.Integral()
    print h_HLT_TightLep_den.Integral()
    if 'Data' in inpfile:        
        h_HLT_TightLep_data_num.Add(h_HLT_TightLep_num)
        h_HLT_TightLep_data_den.Add(h_HLT_TightLep_den)

        h1D_HLT_TightLep_data_num.Add(h1D_HLT_TightLep_num)
        h1D_HLT_TightLep_data_den.Add(h1D_HLT_TightLep_den)

        h1D_HLT_Top_data_num.Add(h1D_HLT_Top_num)
        h1D_HLT_Top_data_den.Add(h1D_HLT_Top_den)


        h_HLT_Top_data_num.Add(h_HLT_Top_num)
        h_HLT_Top_data_den.Add(h_HLT_Top_den)


        h_HLT_TightLepJet_data_num.Add(h_HLT_TightLepJet_num)
        h_HLT_TightLepJet_data_den.Add(h_HLT_TightLepJet_den)

        h1D_HLT_TightLepJet_data_num.Add(h1D_HLT_TightLepJet_num)
        h1D_HLT_TightLepJet_data_den.Add(h1D_HLT_TightLepJet_den)

        h1D_HLT_TopJet_data_num.Add(h1D_HLT_TopJet_num)
        h1D_HLT_TopJet_data_den.Add(h1D_HLT_TopJet_den)


        h_HLT_TopJet_data_num.Add(h_HLT_TopJet_num)
        h_HLT_TopJet_data_den.Add(h_HLT_TopJet_den)



        h_HLT_CR_data_num.Add(h_HLT_CR_num)
        h_HLT_CR_data_den.Add(h_HLT_CR_den)
    elif "TT_dilep" in infile.GetName():
        h_HLT_TightLep_MC_num.Add(h_HLT_TightLep_num)
        h_HLT_TightLep_MC_den.Add(h_HLT_TightLep_den)

        h1D_HLT_TightLep_MC_num.Add(h1D_HLT_TightLep_num)
        h1D_HLT_TightLep_MC_den.Add(h1D_HLT_TightLep_den)

        h1D_HLT_Top_MC_num.Add(h1D_HLT_Top_num)
        h1D_HLT_Top_MC_den.Add(h1D_HLT_Top_den)

        h_HLT_Top_MC_num.Add(h_HLT_Top_num)                                                                                                       
        h_HLT_Top_MC_den.Add(h_HLT_Top_den)




        h_HLT_TightLepJet_MC_num.Add(h_HLT_TightLepJet_num)
        h_HLT_TightLepJet_MC_den.Add(h_HLT_TightLepJet_den)

        h1D_HLT_TightLepJet_MC_num.Add(h1D_HLT_TightLepJet_num)
        h1D_HLT_TightLepJet_MC_den.Add(h1D_HLT_TightLepJet_den)

        h1D_HLT_TopJet_MC_num.Add(h1D_HLT_TopJet_num)
        h1D_HLT_TopJet_MC_den.Add(h1D_HLT_TopJet_den)

        h_HLT_TopJet_MC_num.Add(h_HLT_TopJet_num)
        h_HLT_TopJet_MC_den.Add(h_HLT_TopJet_den)



        fileout.mkdir("TT_dilep")
        fileout.cd("TT_dilep")
        h_HLT_TightLep_num.Write()
        h_HLT_TightLep_den.Write()

        h1D_HLT_TightLep_num.Write()
        h1D_HLT_TightLep_den.Write()

        h1D_HLT_Top_num.Write()
        h1D_HLT_Top_den.Write()

        h_HLT_Top_num.Write()                                                                                                                         
        h_HLT_Top_den.Write()




        h_HLT_TightLepJet_num.Write()
        h_HLT_TightLepJet_den.Write()

        h1D_HLT_TightLepJet_num.Write()
        h1D_HLT_TightLepJet_den.Write()

        h1D_HLT_TopJet_num.Write()
        h1D_HLT_TopJet_den.Write()

        h_HLT_TopJet_num.Write()
        h_HLT_TopJet_den.Write()



        #print h_HLT_Top_num.Integral()
        HLT_TightLep_Eff = ROOT.TEfficiency(h_HLT_TightLep_num, h_HLT_TightLep_den)
        HLT_Top_Eff = ROOT.TEfficiency(h_HLT_Top_num, h_HLT_Top_den)
        HLT_TightLep_Eff.SetLineColor(ROOT.kBlue)
        HLT_Top_Eff.SetLineColor(ROOT.kBlue)
        h_HLT_TightLep_MC_Eff.Divide(h_HLT_TightLep_num, h_HLT_TightLep_den, 1, 1, "B")
        h_HLT_Top_MC_Eff.Divide(h_HLT_Top_num, h_HLT_Top_den, 1, 1, "B")

        h1D_HLT_TightLep_Eff = ROOT.TEfficiency(h1D_HLT_TightLep_num, h1D_HLT_TightLep_den)
        h1D_HLT_TightLep_Eff.SetLineColor(ROOT.kBlue)
        h1D_HLT_TightLep_MC_Eff.Divide(h1D_HLT_TightLep_num, h1D_HLT_TightLep_den, 1, 1, "B")

        h1D_HLT_Top_Eff = ROOT.TEfficiency(h1D_HLT_Top_num, h1D_HLT_Top_den)
        h1D_HLT_Top_Eff.SetLineColor(ROOT.kBlue)
        h1D_HLT_Top_MC_Eff.Divide(h1D_HLT_Top_num, h1D_HLT_Top_den, 1, 1, "B")

        if 'muon' in period:
            h_HLT_TightLep_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            HLT_TightLep_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            h_HLT_Top_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            HLT_Top_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
        else:
            h_HLT_TightLep_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            HLT_TightLep_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            h_HLT_Top_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")                                        
            HLT_Top_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            
        h_HLT_TightLep_MC_Eff.Write()
        HLT_TightLep_Eff.Write()
        printh("TT_dilep", period, h_HLT_TightLep_num, plotpath)
        printh("TT_dilep", period, h_HLT_TightLep_den, plotpath)
        printh("TT_dilep", period, h_HLT_TightLep_MC_Eff, plotpath)

        h1D_HLT_TightLep_MC_Eff.Write()
        h1D_HLT_TightLep_Eff.Write()

        h1D_HLT_Top_MC_Eff.Write()
        h1D_HLT_Top_Eff.Write()

        h_HLT_Top_MC_Eff.Write()                                                                                                                                          
        HLT_Top_Eff.Write()                                                                                                              
        printh("TT_dilep", period, h_HLT_Top_num, plotpath)                                                                          
        printh("TT_dilep", period, h_HLT_Top_den, plotpath)                                                                                 
        printh("TT_dilep", period, h_HLT_Top_MC_Eff, plotpath)



        #print h_HLT_TopJet_num.Integral()
        HLT_TightLepJet_Eff = ROOT.TEfficiency(h_HLT_TightLepJet_num, h_HLT_TightLepJet_den)
        HLT_TopJet_Eff = ROOT.TEfficiency(h_HLT_TopJet_num, h_HLT_TopJet_den)
        HLT_TightLepJet_Eff.SetLineColor(ROOT.kBlue)
        HLT_TopJet_Eff.SetLineColor(ROOT.kBlue)
        h_HLT_TightLepJet_MC_Eff.Divide(h_HLT_TightLepJet_num, h_HLT_TightLepJet_den, 1, 1, "B")
        h_HLT_TopJet_MC_Eff.Divide(h_HLT_TopJet_num, h_HLT_TopJet_den, 1, 1, "B")

        h1D_HLT_TightLepJet_Eff = ROOT.TEfficiency(h1D_HLT_TightLepJet_num, h1D_HLT_TightLepJet_den)
        h1D_HLT_TightLepJet_Eff.SetLineColor(ROOT.kBlue)
        h1D_HLT_TightLepJet_MC_Eff.Divide(h1D_HLT_TightLepJet_num, h1D_HLT_TightLepJet_den, 1, 1, "B")

        h1D_HLT_TopJet_Eff = ROOT.TEfficiency(h1D_HLT_TopJet_num, h1D_HLT_TopJet_den)
        h1D_HLT_TopJet_Eff.SetLineColor(ROOT.kBlue)
        h1D_HLT_TopJet_MC_Eff.Divide(h1D_HLT_TopJet_num, h1D_HLT_TopJet_den, 1, 1, "B")

        if 'muon' in period:
            h_HLT_TightLepJet_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            HLT_TightLepJet_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            h_HLT_TopJet_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
            HLT_TopJet_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
        else:
            h_HLT_TightLepJet_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            HLT_TightLepJet_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            h_HLT_TopJet_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
            HLT_TopJet_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")

        h_HLT_TightLepJet_MC_Eff.Write()
        HLT_TightLepJet_Eff.Write()
        printh("TT_dilep", period, h_HLT_TightLepJet_num, plotpath)
        printh("TT_dilep", period, h_HLT_TightLepJet_den, plotpath)
        printh("TT_dilep", period, h_HLT_TightLepJet_MC_Eff, plotpath)

        h1D_HLT_TightLepJet_MC_Eff.Write()
        h1D_HLT_TightLepJet_Eff.Write()

        h1D_HLT_TopJet_MC_Eff.Write()
        h1D_HLT_TopJet_Eff.Write()

        h_HLT_TopJet_MC_Eff.Write()
        HLT_TopJet_Eff.Write()
        printh("TT_dilep", period, h_HLT_TopJet_num, plotpath)
        printh("TT_dilep", period, h_HLT_TopJet_den, plotpath)
        printh("TT_dilep", period, h_HLT_TopJet_MC_Eff, plotpath)


    else:
        h_HLT_CR_MC_num.Add(h_HLT_CR_num)
        h_HLT_CR_MC_den.Add(h_HLT_CR_den)


HLT_TightLep_data_Eff = ROOT.TEfficiency(h_HLT_TightLep_data_num, h_HLT_TightLep_data_den)
h_HLT_TightLep_data_Eff = ROOT.TH2F("h2D_HLT_TightLep_data_Eff", "h", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_TightLep_data_Eff.Clone(h_HLT_TightLep_data_num.GetName())
h_HLT_TightLep_data_Eff.Divide(h_HLT_TightLep_data_num, h_HLT_TightLep_data_den, 1, 1, "B")

h1D_HLT_TightLep_data_Eff = ROOT.TEfficiency(h1D_HLT_TightLep_data_num, h1D_HLT_TightLep_data_den)
h1D_HLT_TightLep_data_Eff = ROOT.TH1F("h1D_HLT_TightLep_data_Eff", "h", nbins_muy1D, edges_muy1D)
h1D_HLT_TightLep_data_Eff.Clone(h1D_HLT_TightLep_data_num.GetName())
h1D_HLT_TightLep_data_Eff.Divide(h1D_HLT_TightLep_data_num, h1D_HLT_TightLep_data_den, 1, 1, "B")



if 'muon' in period:
    HLT_TightLep_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_TightLep_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period:
    h_HLT_TightLep_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_TightLep_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")

    
h_HLT_TightLep_data_Eff.SetLineColor(ROOT.kBlack)
HLT_TightLep_data_Eff.SetLineColor(ROOT.kBlack)
fileout.mkdir("Data")
fileout.cd("Data")
h_HLT_TightLep_data_num.Write()
print h_HLT_TightLep_data_num.Integral()
h_HLT_TightLep_data_den.Write()
h_HLT_TightLep_data_Eff.Write()
HLT_TightLep_data_Eff.Write()
printh("Data", period, h_HLT_TightLep_data_num, plotpath)
printh("Data", period, h_HLT_TightLep_data_den, plotpath)
printh("Data", period, h_HLT_TightLep_data_Eff, plotpath)


#h1D_HLT_TightLep_data_Eff = ROOT.TEfficiency(h1D_HLT_TightLep_data_num, h1D_HLT_TightLep_data_den)
#h1D_HLT_TightLep_data_Eff = ROOT.TH1F("h1D_HLT_TightLep_data_Eff", "h", nbins_muy1D, edges_muy1D)
#h1D_HLT_TightLep_data_Eff.Clone(h1D_HLT_TightLep_data_num.GetName())
#h1D_HLT_TightLep_data_Eff.Divide(h1D_HLT_TightLep_data_num, h1D_HLT_TightLep_data_den, 1, 1, "B")

h1D_HLT_TightLep_data_num.Write()
h1D_HLT_TightLep_data_den.Write()
h1D_HLT_TightLep_data_Eff.Write()
#h1D_HLT_TightLep_data_Eff.Write()

SF_TightLep = ROOT.TH2F("h2D_SF_TightLep", "h_TightLep", nbins_mux, edges_mux, nbins_muy, edges_muy)# nbins, edges)
SF_TightLep.Sumw2()
#SF.Clone(h_HLT_TightLep_data_Eff.GetName())
SF_TightLep.Divide(h_HLT_TightLep_data_Eff, h_HLT_TightLep_MC_Eff, 1, 1)

h1D_SF_TightLep = ROOT.TH1F("h1D_SF_TightLep", "h1D_TightLep", nbins_muy1D, edges_muy1D)# nbins, edges)
h1D_SF_TightLep.Sumw2()
#SF.Clone(h_HLT_TightLep_data_Eff.GetName())
h1D_SF_TightLep.Divide(h1D_HLT_TightLep_data_Eff, h1D_HLT_TightLep_MC_Eff, 1, 1)

if 'muon' in period:
    SF_TightLep.SetTitle("Muon trigger scale factors; |#eta|; muon p_{T} [GeV]")
    #SF.GetXaxis().SetRangeUser(55, 1000)
elif  'electron':
    SF_TightLep.SetTitle("Electron trigger scale factors; #eta; electron p_{T} [GeV]")
else:
    SF_Tight.SetTitle("FatJet trigger scale factors; FatJet p_{T} [GeV]; FatJet M [GeV]")
    
printh("Data", period, SF_TightLep, plotpath)
fileout.cd()
SF_TightLep.Write()
h1D_SF_TightLep.Write()

#### New ###

HLT_TightLepJet_data_Eff = ROOT.TEfficiency(h_HLT_TightLepJet_data_num, h_HLT_TightLepJet_data_den)
h_HLT_TightLepJet_data_Eff = ROOT.TH2F("h2D_HLT_TightLepJet_data_Eff", "h", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TightLepJet_data_Eff.Clone(h_HLT_TightLepJet_data_num.GetName())
h_HLT_TightLepJet_data_Eff.Divide(h_HLT_TightLepJet_data_num, h_HLT_TightLepJet_data_den, 1, 1, "B")

h1D_HLT_TightLepJet_data_Eff = ROOT.TEfficiency(h1D_HLT_TightLepJet_data_num, h1D_HLT_TightLepJet_data_den)
h1D_HLT_TightLepJet_data_Eff = ROOT.TH1F("h1D_HLT_TightLepJet_data_Eff", "h", nbins_muy1D, edges_muy1D)
h1D_HLT_TightLepJet_data_Eff.Clone(h1D_HLT_TightLepJet_data_num.GetName())
h1D_HLT_TightLepJet_data_Eff.Divide(h1D_HLT_TightLepJet_data_num, h1D_HLT_TightLepJet_data_den, 1, 1, "B")



if 'muon' in period:
    HLT_TightLepJet_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_TightLepJet_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period:
    h_HLT_TightLepJet_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_TightLepJet_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")


h_HLT_TightLepJet_data_Eff.SetLineColor(ROOT.kBlack)
HLT_TightLepJet_data_Eff.SetLineColor(ROOT.kBlack)
fileout.mkdir("Data")
fileout.cd("Data")
h_HLT_TightLepJet_data_num.Write()
print h_HLT_TightLepJet_data_num.Integral()
h_HLT_TightLepJet_data_den.Write()
h_HLT_TightLepJet_data_Eff.Write()
HLT_TightLepJet_data_Eff.Write()
printh("Data", period, h_HLT_TightLepJet_data_num, plotpath)
printh("Data", period, h_HLT_TightLepJet_data_den, plotpath)
printh("Data", period, h_HLT_TightLepJet_data_Eff, plotpath)


#h1D_HLT_TightLepJet_data_Eff = ROOT.TEfficiency(h1D_HLT_TightLepJet_data_num, h1D_HLT_TightLepJet_data_den)
#h1D_HLT_TightLepJet_data_Eff = ROOT.TH1F("h1D_HLT_TightLepJet_data_Eff", "h", nbins_muy1D, edges_muy1D)
#h1D_HLT_TightLepJet_data_Eff.Clone(h1D_HLT_TightLepJet_data_num.GetName())
#h1D_HLT_TightLepJet_data_Eff.Divide(h1D_HLT_TightLepJet_data_num, h1D_HLT_TightLepJet_data_den, 1, 1, "B")

h1D_HLT_TightLepJet_data_num.Write()
h1D_HLT_TightLepJet_data_den.Write()
h1D_HLT_TightLepJet_data_Eff.Write()
#h1D_HLT_TightLepJet_data_Eff.Write()

SF_TightLepJet = ROOT.TH2F("h2D_SF_TightLepJet", "h_TightLepJet", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
SF_TightLepJet.Sumw2()
#SF.Clone(h_HLT_TightLepJet_data_Eff.GetName())
SF_TightLepJet.Divide(h_HLT_TightLepJet_data_Eff, h_HLT_TightLepJet_MC_Eff, 1, 1)

h1D_SF_TightLepJet = ROOT.TH1F("h1D_SF_TightLepJet", "h1D_TightLepJet", nbins_muy1D, edges_muy1D)# nbins, edges)
h1D_SF_TightLepJet.Sumw2()
#SF.Clone(h_HLT_TightLepJet_data_Eff.GetName())
h1D_SF_TightLepJet.Divide(h1D_HLT_TightLepJet_data_Eff, h1D_HLT_TightLepJet_MC_Eff, 1, 1)

if 'muon' in period:
    SF_TightLepJet.SetTitle("Muon trigger scale factors; |#eta|; muon p_{T} [GeV]")
    #SF.GetXaxis().SetRangeUser(55, 1000)
elif  'electron':
    SF_TightLepJet.SetTitle("Electron trigger scale factors; #eta; electron p_{T} [GeV]")
else:
    SF_Tight.SetTitle("FatJet trigger scale factors; FatJet p_{T} [GeV]; FatJet M [GeV]")

printh("Data", period, SF_TightLepJet, plotpath)
fileout.cd()
SF_TightLepJet.Write()
h1D_SF_TightLepJet.Write()


#######

HLT_Top_data_Eff = ROOT.TEfficiency(h_HLT_Top_data_num, h_HLT_Top_data_den)
h_HLT_Top_data_Eff = ROOT.TH2F("h2D_HLT_Top_data_Eff", "h", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_Top_data_Eff.Clone(h_HLT_Top_data_num.GetName())
h_HLT_Top_data_Eff.Divide(h_HLT_Top_data_num, h_HLT_Top_data_den, 1, 1, "B")

h1D_HLT_Top_data_Eff = ROOT.TEfficiency(h1D_HLT_Top_data_num, h1D_HLT_Top_data_den)
h1D_HLT_Top_data_Eff = ROOT.TH1F("h1D_HLT_Top_data_Eff", "h", nbins_muy1D, edges_muy1D)
h1D_HLT_Top_data_Eff.Clone(h1D_HLT_Top_data_num.GetName())
h1D_HLT_Top_data_Eff.Divide(h1D_HLT_Top_data_num, h1D_HLT_Top_data_den, 1, 1, "B")

if 'muon' in period:
    HLT_Top_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_Top_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period :
    h_HLT_Top_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_Top_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")

h_HLT_Top_data_Eff.SetLineColor(ROOT.kBlack)
HLT_Top_data_Eff.SetLineColor(ROOT.kBlack)
fileout.cd("Data")
h_HLT_Top_data_num.Write()
print h_HLT_Top_data_num.Integral()
h_HLT_Top_data_den.Write()
h_HLT_Top_data_Eff.Write()
HLT_Top_data_Eff.Write()
printh("Data", period, h_HLT_Top_data_num, plotpath)
printh("Data", period, h_HLT_Top_data_den, plotpath)
printh("Data", period, h_HLT_Top_data_Eff, plotpath)

h1D_HLT_Top_data_num.Write()
h1D_HLT_Top_data_den.Write()
h1D_HLT_Top_data_Eff.Write()


SF_Top = ROOT.TH2F("h2D_SF_Top", "h_Top", nbins_mux, edges_mux, nbins_muy, edges_muy)# nbins, edges)
SF_Top.Sumw2()
#SF.Clone(h_HLT_Top_data_Eff.GetName())
SF_Top.Divide(h_HLT_Top_data_Eff, h_HLT_Top_MC_Eff, 1, 1)

h1D_SF_Top = ROOT.TH1F("h1D_SF_Top", "h1D_Top", nbins_muy1D, edges_muy1D)# nbins, edges)
h1D_SF_Top.Sumw2()
#SF.Clone(h_HLT_Top_data_Eff.GetName())
h1D_SF_Top.Divide(h1D_HLT_Top_data_Eff, h1D_HLT_Top_MC_Eff, 1, 1)
if 'muon' in period:
    SF_Top.SetTitle("Muon trigger scale factors; |#eta|; muon p_{T} [GeV];")
    #SF.GetXaxis().SetRangeUser(55, 1000)
elif 'electron' in period:
    SF_Top.SetTitle("Electron trigger scale factors; #eta; electron p_{T} [GeV]")
else:
    SF_Top.SetTitle("FatJet trigger scale factors; FatJet p_{T} [GeV]; FatJet M [GeV]")

printh("Data", period, SF_Top, plotpath)
fileout.cd()
SF_Top.Write()
h1D_SF_Top.Write()

##### New

HLT_TopJet_data_Eff = ROOT.TEfficiency(h_HLT_TopJet_data_num, h_HLT_TopJet_data_den)
h_HLT_TopJet_data_Eff = ROOT.TH2F("h2D_HLT_TopJet_data_Eff", "h", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
h_HLT_TopJet_data_Eff.Clone(h_HLT_TopJet_data_num.GetName())
h_HLT_TopJet_data_Eff.Divide(h_HLT_TopJet_data_num, h_HLT_TopJet_data_den, 1, 1, "B")

h1D_HLT_TopJet_data_Eff = ROOT.TEfficiency(h1D_HLT_TopJet_data_num, h1D_HLT_TopJet_data_den)
h1D_HLT_TopJet_data_Eff = ROOT.TH1F("h1D_HLT_TopJet_data_Eff", "h", nbins_muy1D, edges_muy1D)
h1D_HLT_TopJet_data_Eff.Clone(h1D_HLT_TopJet_data_num.GetName())
h1D_HLT_TopJet_data_Eff.Divide(h1D_HLT_TopJet_data_num, h1D_HLT_TopJet_data_den, 1, 1, "B")

if 'muon' in period:
    HLT_TopJet_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_TopJet_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period :
    h_HLT_TopJet_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_TopJet_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")

h_HLT_TopJet_data_Eff.SetLineColor(ROOT.kBlack)
HLT_TopJet_data_Eff.SetLineColor(ROOT.kBlack)
fileout.cd("Data")
h_HLT_TopJet_data_num.Write()
print h_HLT_TopJet_data_num.Integral()
h_HLT_TopJet_data_den.Write()
h_HLT_TopJet_data_Eff.Write()
HLT_TopJet_data_Eff.Write()
printh("Data", period, h_HLT_TopJet_data_num, plotpath)
printh("Data", period, h_HLT_TopJet_data_den, plotpath)
printh("Data", period, h_HLT_TopJet_data_Eff, plotpath)

h1D_HLT_TopJet_data_num.Write()
h1D_HLT_TopJet_data_den.Write()
h1D_HLT_TopJet_data_Eff.Write()


SF_TopJet = ROOT.TH2F("h2D_SF_TopJet", "h_TopJet", nbins_muxjet, edges_muxjet, nbins_muyjet, edges_muyjet)
SF_TopJet.Sumw2()
#SF.Clone(h_HLT_TopJet_data_Eff.GetName())
SF_TopJet.Divide(h_HLT_TopJet_data_Eff, h_HLT_TopJet_MC_Eff, 1, 1)

h1D_SF_TopJet = ROOT.TH1F("h1D_SF_TopJet", "h1D_TopJet", nbins_muy1D, edges_muy1D)# nbins, edges)
h1D_SF_TopJet.Sumw2()
#SF.Clone(h_HLT_TopJet_data_Eff.GetName())
h1D_SF_TopJet.Divide(h1D_HLT_TopJet_data_Eff, h1D_HLT_TopJet_MC_Eff, 1, 1)
if 'muon' in period:
    SF_TopJet.SetTitle("Muon trigger scale factors; |#eta|; muon p_{T} [GeV];")
    #SF.GetXaxis().SetRangeUser(55, 1000)
elif 'electron' in period:
    SF_TopJet.SetTitle("Electron trigger scale factors; #eta; electron p_{T} [GeV]")
else:
    SF_TopJet.SetTitle("FatJet trigger scale factors; FatJet p_{T} [GeV]; FatJet M [GeV]")

printh("Data", period, SF_TopJet, plotpath)
fileout.cd()
SF_TopJet.Write()
h1D_SF_TopJet.Write()

####

HLT_CR_MC_Eff = ROOT.TEfficiency(h_HLT_CR_MC_num, h_HLT_CR_MC_den)
h_HLT_CR_MC_Eff = ROOT.TH2F("h2D_HLT_CR_MC_Eff", "h", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_MC_Eff.Clone(h_HLT_CR_MC_num.GetName())
h_HLT_CR_MC_Eff.Divide(h_HLT_CR_MC_num, h_HLT_CR_MC_den, 1, 1, "B")
if 'muon' in period:
    HLT_CR_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_CR_MC_Eff.SetTitle("MC Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period:
    h_HLT_CR_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_CR_MC_Eff.SetTitle("MC Electron trigger efficiency; #eta; electron p_{T} [GeV]")

else:
    h_HLT_CR_MC_Eff.SetTitle("MC FatJet trigger efficiency; FatJet p_{T} [GeV]; FatJet M [GeV]")
    HLT_CR_MC_Eff.SetTitle("MC FatJet trigger efficiency; FatJet p_{T} [GeV]; FatJet M [GeV]")
    

h_HLT_CR_MC_Eff.SetLineColor(ROOT.kBlack)
HLT_CR_MC_Eff.SetLineColor(ROOT.kBlack)
fileout.mkdir("MC")
fileout.cd("MC")
h_HLT_CR_MC_num.Write()
print h_HLT_CR_MC_num.Integral()
h_HLT_CR_MC_den.Write()
h_HLT_CR_MC_Eff.Write()
HLT_CR_MC_Eff.Write()
printh("MC", period, h_HLT_CR_MC_num, plotpath)
printh("MC", period, h_HLT_CR_MC_den, plotpath)
printh("MC", period, h_HLT_CR_MC_Eff, plotpath)


HLT_CR_data_Eff = ROOT.TEfficiency(h_HLT_CR_data_num, h_HLT_CR_data_den)
h_HLT_CR_data_Eff = ROOT.TH2F("h2D_HLT_CR_data_Eff", "h", nbins_mux, edges_mux, nbins_muy, edges_muy)
h_HLT_CR_data_Eff.Clone(h_HLT_CR_data_num.GetName())
h_HLT_CR_data_Eff.Divide(h_HLT_CR_data_num, h_HLT_CR_data_den, 1, 1, "B")
if 'muon' in period:
    HLT_CR_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
    h_HLT_CR_data_Eff.SetTitle("Data Muon trigger efficiency; |#eta| ;muon p_{T} [GeV]")
elif 'electron' in period:
    h_HLT_CR_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
    HLT_CR_data_Eff.SetTitle("Data Electron trigger efficiency; #eta; electron p_{T} [GeV]")
else:
    h_HLT_CR_data_Eff.SetTitle("Data FatJet trigger efficiency; FatJet p_{T} [GeV]; FatJet M [GeV]")
    HLT_CR_data_Eff.SetTitle("Data FatJet trigger efficiency; FatJet p_{T} [GeV]; FatJet M [GeV]")

h_HLT_CR_data_Eff.SetLineColor(ROOT.kBlack)
HLT_CR_data_Eff.SetLineColor(ROOT.kBlack)
fileout.cd("Data")
h_HLT_CR_data_num.Write()
print h_HLT_CR_data_num.Integral()
h_HLT_CR_data_den.Write()
h_HLT_CR_data_Eff.Write()
HLT_CR_data_Eff.Write()
printh("Data", period, h_HLT_CR_data_num, plotpath)
printh("Data", period, h_HLT_CR_data_den, plotpath)
printh("Data", period, h_HLT_CR_data_Eff, plotpath)

SF_CR = ROOT.TH2F("h2D_SF_CR", "h_CR", nbins_mux, edges_mux, nbins_muy, edges_muy)# nbins, edges)
SF_CR.Sumw2()
#SF.Clone(h_HLT_CR_data_Eff.GetName())
SF_CR.Divide(h_HLT_CR_data_Eff, h_HLT_CR_MC_Eff, 1, 1)
if 'muon' in period:
    SF_CR.SetTitle("Muon trigger scale factors; muon p_{T} [GeV]; #eta")
    #SF.GetXaxis().SetRangeUser(55, 1000)
elif 'electron' in period:
    SF_CR.SetTitle("Electron trigger scale factors; #eta; electron p_{T} [GeV]")
else:
    SF_CR.SetTitle("FatJet trigger scale factors; FatJet p_{T} [GeV]; FatJet M [GeV]")
 

printh("Data", period, SF_CR, plotpath)
fileout.cd()
SF_CR.Write()


print "DONE"
fileout.Close()
