from lhereader import readLHEF
from ROOT import TCanvas, TH1F, gROOT

gROOT.SetBatch()
#PROC_WEff_UFO_1/Events/run_01/unweighted_events_decayed.lhe
#folder=['schannel_OFF_LH', 'schannel_ON_LH', 'schannel_OFF']

hist_title = "W' boson mass"
canv_name = 'mass_Wp'
data=readLHEF('./cmsgrid_final.lhe')
parts=data.getParticlesByIDs([34]) # collect all botom and anti-bottom quarks
c=TCanvas()
hist=TH1F("pt", hist_title,100,500,1500)
for p in parts:
  #hist.Fill(p.pt)
  hist.Fill(p.p4.M())
hist.Draw()
c.SaveAs('plots/'+canv_name+'.png')
c.SaveAs('plots/'+canv_name+'.root')
hist.Delete()
