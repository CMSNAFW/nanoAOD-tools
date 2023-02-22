import ROOT
from array import array
from samples.samples import *

folder = "/eos/home-f/fcarneva/Tprime/nosynch/UL/"

name = []
top = []
ak8 = []

h1 = ROOT.TH1F("h1","h1",13,550,1850)
h2 = ROOT.TH1F("h2","h2",13,550,1850)
i=0
for sig in range(600,1900,100):
    
    s = "Tprime_tHq_"+str(sig)+"LH_2018"
        
    file = ROOT.TFile.Open(folder+s+"/"+s+".root")
    
    tree = file.Get("events_nominal")
    N_tot = tree.GetEntries("Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0")

    N_TrueT = tree.GetEntries("Top_MC_nominal==1 && Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0")
    N_AK8_True = tree.GetEntries("FatJet_MC_nominal==1 && Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0")
    name.append(sig)
    top.append(N_TrueT/float(N_tot))
    ak8.append(N_AK8_True/float(N_tot))
    h1.SetBinContent(i+1,top[i])
    h2.SetBinContent(i+1,ak8[i])
    h1.SetBinError(i+1,ROOT.TMath.Sqrt(top[i]*(1-top[i])/float(N_tot)))
    h2.SetBinError(i+1,ROOT.TMath.Sqrt(ak8[i]*(1-ak8[i])/float(N_tot)))
    i=i+1
h1.GetXaxis().SetRangeUser(0,1)
h2.GetXaxis().SetRangeUser(0,1)
c = ROOT.TCanvas()
c.Divide(2)
c.cd(1)
#g1 = ROOT.TGraph(12,array('d',name),array('d',top))

h1.Draw("e")
h1.SetTitle("Precision Best Top")
h1.GetYaxis().SetRangeUser(0.5,1)
c.cd(2)
#g2 = ROOT.TGraph(12,array('d',name),array('d',ak8))
h2.Draw("e")
h2.SetTitle("Precision Best AK8")
h2.GetYaxis().SetRangeUser(0.5,1)
c.SaveAs("effiency.png")
