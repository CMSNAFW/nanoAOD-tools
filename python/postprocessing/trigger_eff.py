import ROOT
import math
from array import array
#from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *
import sys
import os
import copy

folder = 'vtrigger'
inputpath = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Wprime/nosynch/' + folder + '/'
plotpath = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Wprime/nosynch/' + folder + '/plot/'

if not os.path.exists(plotpath):
    os.makedirs(plotpath)

period = sys.argv[1]

def printh(filename, period, h, plotpath):
    c = ROOT.TCanvas(filename + '_' + period + '_' + h.GetName(), filename + '_' + period + '_' + h.GetName())
    c.Draw()
    h.Draw()
    c.Print(plotpath + c.GetName() + '.pdf')

inpfiles = {"muon_16":["DataMu_2016", "DataEle_2016", "TT_dilep_2016"],
            "electron_16":["DataMu_2016", "DataEle_2016", "TT_dilep_2016"],
            "muon_17":["DataMu_2017", "DataEle_2017", "TT_dilep_2017"],
            "electron_17":["DataMuF_2017", "DataEleF_2017", "TT_dilep_2017"],
            "muon_18":["DataMu_2018",  "DataEle_2018", "TT_dilep_2018"],
            "electron_18":["DataMu_2018", "DataEle_2018", "TT_dilep_2018"],
        }

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.TH1.SetDefaultSumw2()

edges = array.array('f', [0., 10., 20., 30., 40., 42., 44., 46.,  48., 50., 52., 55., 60., 65., 80., 100., 130.])#, 160., 190., 230., 270., 320., 360., 700.])
#edges = array.array('f',[0., 200., 400., 600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400., 2800., 3400., 4000.])
nbins = len(edges)-1
h_HLT_data_num = ROOT.TH1F("HLT_data_num", "HLT_data_num", nbins, edges)
h_HLT_data_den = ROOT.TH1F("HLT_data_den", "HLT_data_den", nbins, edges)
h_HLT_MC_Eff = ROOT.TH1F("h_HLT_MC_Eff", "h", nbins, edges)
fileout = ROOT.TFile(inputpath + period + ".root", "RECREATE")
for inpfile in inpfiles[period]:
    infile = ROOT.TFile.Open(inputpath +  inpfile + "/" + inpfile + ".root")
    print 'Opening ' + infile.GetName()
    tree = infile.Get("events_all")
    h_HLT_num = ROOT.TH1F("HLT_num", "HLT_num", nbins, edges)
    h_HLT_den = ROOT.TH1F("HLT_den", "HLT_den", nbins, edges)
    if 'muon' in period:
        if 'Data' not in infile.GetName():
            tree.Project("HLT_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*muon_SF*passed_ele*(passed_mu||passed_ht)")
            tree.Project("HLT_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*muon_SF*passed_ele")
            #tree.Project("HLT_num", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_ele*(passed_mu||passed_ht)")
            #tree.Project("HLT_den", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_ele")
        else:
            tree.Project("HLT_num", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*passed_ele*(passed_mu||passed_ht)")
            tree.Project("HLT_den", "muon_pt", "w_nominal*PFSF*puSF*isdileptonic*passed_ele")
            #tree.Project("HLT_num", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_ele*(passed_mu||passed_ht)")
            #tree.Project("HLT_den", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_ele")
    else:
        if 'Data' not in infile.GetName():
            tree.Project("HLT_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*electron_SF*passed_mu*(passed_ele||passed_ht)")
            tree.Project("HLT_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*electron_SF*passed_mu")
            #tree.Project("HLT_num", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_mu*(passed_ele||passed_ht)")
            #tree.Project("HLT_den", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_mu")
        else:
            tree.Project("HLT_num", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*passed_mu*(passed_ele||passed_ht)")
            tree.Project("HLT_den", "electron_pt", "w_nominal*PFSF*puSF*isdileptonic*passed_mu")
            #tree.Project("HLT_num", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_mu*(passed_ele||passed_ht)")
            #tree.Project("HLT_den", "Event_HT", "w_nominal*PFSF*puSF*isdileptonic*passed_mu")
    #print h_HLT_num.Integral()
    #print h_HLT_den.Integral()
    if 'Data' in inpfile:
        h_HLT_data_num.Add(h_HLT_num)
        h_HLT_data_den.Add(h_HLT_den)
    else:
        fileout.mkdir("TT_dilep")
        fileout.cd("TT_dilep")
        h_HLT_num.Write()
        h_HLT_den.Write()
        HLT_Eff = ROOT.TEfficiency(h_HLT_num, h_HLT_den)
        HLT_Eff.SetLineColor(ROOT.kBlue)
        #h_HLT_MC_Eff.Clone(h_HLT_num.GetName())
        h_HLT_MC_Eff.Divide(h_HLT_num, h_HLT_den, 1, 1, "B")
        if 'muon' in period:
            h_HLT_MC_Eff.SetTitle("MC Muon trigger efficiency; muon p_{T} [GeV];#epsilon")
            HLT_Eff.SetTitle("MC Muon trigger efficiency; muon p_{T} [GeV];#epsilon")
        else:
            h_HLT_MC_Eff.SetTitle("MC Electron trigger efficiency; electron p_{T} [GeV];#epsilon")
            HLT_Eff.SetTitle("MC Electron trigger efficiency; electron p_{T} [GeV];#epsilon")
        h_HLT_MC_Eff.Write()
        HLT_Eff.Write()
        printh("TT_dilep", period, h_HLT_num, plotpath)
        printh("TT_dilep", period, h_HLT_den, plotpath)
        printh("TT_dilep", period, h_HLT_MC_Eff, plotpath)

HLT_data_Eff = ROOT.TEfficiency(h_HLT_data_num, h_HLT_data_den)
h_HLT_data_Eff = ROOT.TH1F("h_HLT_data_Eff", "h", nbins, edges)
h_HLT_data_Eff.Clone(h_HLT_data_num.GetName())
h_HLT_data_Eff.Divide(h_HLT_data_num, h_HLT_data_den, 1, 1, "B")
if 'muon' in period:
    HLT_data_Eff.SetTitle("Data Muon trigger efficiency; muon p_{T} [GeV];#epsilon")
    h_HLT_data_Eff.SetTitle("Data Muon trigger efficiency; muon p_{T} [GeV];#epsilon")
else:
    h_HLT_data_Eff.SetTitle("Data Electron trigger efficiency; electron p_{T} [GeV];#epsilon")
    HLT_data_Eff.SetTitle("Data Electron trigger efficiency; electron p_{T} [GeV];#epsilon")
h_HLT_data_Eff.SetLineColor(ROOT.kBlack)
HLT_data_Eff.SetLineColor(ROOT.kBlack)
fileout.mkdir("Data")
fileout.cd("Data")
h_HLT_data_num.Write()
h_HLT_data_den.Write()
h_HLT_data_Eff.Write()
HLT_data_Eff.Write()
printh("Data", period, h_HLT_data_num, plotpath)
printh("Data", period, h_HLT_data_den, plotpath)
printh("Data", period, h_HLT_data_Eff, plotpath)

SF = ROOT.TH1F("h_SF", "h", nbins, edges)
if 'muon' in period:
    SF.SetTitle("Muon trigger scale factors; muon p_{T} [GeV]; Scale Factor")
else:
    SF.SetTitle("Electron trigger scale factors; electron p_{T} [GeV]; Scale Factor")
SF.Sumw2()
#SF.Clone(h_HLT_data_Eff.GetName())
SF.Divide(h_HLT_data_Eff, h_HLT_MC_Eff, 1, 1)
printh("Data", period, SF, plotpath)
fileout.cd()
SF.Write()
print "DONE"
fileout.Close()
