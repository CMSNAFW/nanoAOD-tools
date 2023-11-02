import os, commands
import sys
import optparse
import ROOT
import math
from variabile import variabile
from CMS_lumi import CMS_lumi
from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
#from skimtree_utils import deltaR
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils import *
from array import array
usage = 'python makeplot.py'
parser = optparse.OptionParser(usage)
parser.add_option('--merpart', dest='merpart', default = False, action='store_true', help='Default parts are not merged')
parser.add_option('--mertree', dest='mertree', default = False, action='store_true', help='Default make no file is merged')
parser.add_option('--lumi', dest='lumi', default = False, action='store_true', help='Default do not write the normalization weights')
parser.add_option('--mer2016', dest='mer2016', default = False, action='store_true', help='Default do not add pre and posty VFP 2016')
parser.add_option('--sel', dest='sel', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('-p', '--plot', dest='plot', default = False, action='store_true', help='Default make no plots')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default make no stacks')
parser.add_option('-N', '--notstacked', dest='tostack', default = True, action='store_false', help='Default make plots stacked')
parser.add_option('-L', '--lep', dest='lep', type='string', default = 'muon,electron', help='Default make muon analysis')
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'all', help='Default all systematics added')
parser.add_option('-C', '--cut', dest='cut', type='string', default = 'Top_M_nomimal>0.', help='Default no cut')
parser.add_option('-y', '--year', dest='year', type='string', default = 'all', help='Default 2016, 2017 and 2018 are included')
parser.add_option('-f', '--folder', dest='folder', type='string', default = 'v0', help='Default folder is v0')
parser.add_option('--fit', dest='fit', default = False, action='store_true', help='Default don\'t make plot for SF fit')
parser.add_option('-d', '--dat', dest='dat', type='string', default = 'all', help="")

(opt, args) = parser.parse_args()

folder = opt.folder

filerepo = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Tprime/nosynch/' + folder + '/'
plotrepo = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Tprime/nosynch/' + folder + '/'#_topjet/'#/only_Wpjetbtag_ev1btag/'


ROOT.gROOT.SetBatch() # don't pop up canvases
if not os.path.exists(plotrepo + 'plot/muon'):
     os.makedirs(plotrepo + 'plot/muon')
if not os.path.exists(plotrepo + 'plot/electron'):
     os.makedirs(plotrepo + 'plot/electron')
if not os.path.exists(plotrepo + 'stack'):
     os.makedirs(plotrepo + 'stack')

def mergepart(dataset):
     samples = []
     if hasattr(dataset, 'components'): # How to check whether this exists or not
          samples = [sample for sample in dataset.components]# Method exists and was used.
     else:
          samples.append(dataset)
     for sample in samples:
          add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + "_part*.root" 
          print add
          os.system(str(add))
          check = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root ")
          print "Number of entries of the file %s are %s" %(filerepo + sample.label + "/"  + sample.label + "_merged.root", (check.Get("events_nominal")).GetEntries())
          #print "Number of entries of the file %s are %s" %(filerepo + sample.label + "/"  + sample.label + "_merged.root", (check.Get("events_all")).GetEntries())

def mergetree(sample):
     if not os.path.exists(filerepo + sample.label):
          os.makedirs(filerepo + sample.label)
     if hasattr(sample, 'components'): # How to check whether this exists or not
          add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + ".root" 
          for comp in sample.components:
               add += " " + filerepo + comp.label + "/"  + comp.label + ".root" 
          print add
          os.system(str(add))

def merge2016(sample):
     label = sample.label#.replace("postVFP","")
     if not os.path.exists(filerepo + label):
          os.makedirs(filerepo + label)
     #if hasattr(sample, 'components'): # How to check whether this exists or not
     add = "hadd -f " + filerepo + label + "/"  + label + ".root"
     add += " " + filerepo + label + "preVFP/"  + label + "preVFP.root"
     add += " " + filerepo + label + "postVFP/"  + label + "postVFP.root"
     #for comp in sample.components:
     #     add += " " + filerepo + comp.label + "/"  + comp.label + ".root"
     #     add += " " + filerepo + comp.label.replace("post","pre") + "/"  + comp.label.replace("post","pre") + ".root"
     print add
     os.system(str(add))


def lumi_writer(dataset, lumi):
     samples = []
     if hasattr(dataset, 'components'): # How to check whether this exists or not
          samples = [sample for sample in dataset.components]# Method exists and was used.
     else:
          samples.append(dataset)
     for sample in samples:
          if not ('Data' in sample.label): # or 'TT_dilep' in sample.label):
               infile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root")
               tree = infile.Get('events_nominal')
               treejesup = infile.Get('events_jesUp')
               treejesdown = infile.Get('events_jesDown')
               treejerup = infile.Get('events_jerUp')
               treejerdown = infile.Get('events_jerDown')
               tree.SetBranchStatus('w_nominal', 0)
               tree.SetBranchStatus('w_PDF', 0)
               treejesup.SetBranchStatus('w_nominal', 0)
               treejesdown.SetBranchStatus('w_nominal', 0)
               treejerup.SetBranchStatus('w_nominal', 0)
               treejerdown.SetBranchStatus('w_nominal', 0)
               outfile = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root","RECREATE")
               tree_new = tree.CloneTree(0)
               treejesup_new = treejesup.CloneTree(0)
               treejesdown_new = treejesdown.CloneTree(0)
               treejerup_new = treejerup.CloneTree(0)
               treejerdown_new = treejerdown.CloneTree(0)
               tree.SetBranchStatus('w_pt', 1)
               treejesup.SetBranchStatus('w_pt', 1)
               treejesdown.SetBranchStatus('w_pt', 1)
               treejerup.SetBranchStatus('w_pt', 1)
               treejerdown.SetBranchStatus('w_pt', 1)
               tree.SetBranchStatus('w_nominal', 1)
               tree.SetBranchStatus('w_PDF', 1)
               treejesup.SetBranchStatus('w_nominal', 1)
               treejesdown.SetBranchStatus('w_nominal', 1)
               treejerup.SetBranchStatus('w_nominal', 1)
               treejerdown.SetBranchStatus('w_nominal', 1)
               print("Getting the histos from %s" %(infile))
               h_genw_tmp = ROOT.TH1F(infile.Get("h_genweight"))
               h_pdfw_tmp = ROOT.TH1F(infile.Get("h_PDFweight"))
               nbins = h_pdfw_tmp.GetXaxis().GetNbins()
               print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genw_tmp.GetBinContent(1), nbins))
               w_nom = array('f', [0.]) 
               w_nomjesup = array('f', [0.]) 
               w_nomjesdown = array('f', [0.]) 
               w_nomjerup = array('f', [0.]) 
               w_nomjerdown = array('f', [0.]) 
               w_PDF = array('f', [0.]*nbins)
               print(nbins)
               print(len(w_PDF))
               tree_new.Branch('w_nominal', w_nom, 'w_nominal/F')
               tree_new.Branch('w_PDF', w_PDF, 'w_PDF/F')
               treejesup_new.Branch('w_nominal', w_nomjesup, 'w_nominal/F')
               treejesdown_new.Branch('w_nominal', w_nomjesdown, 'w_nominal/F')
               treejerup_new.Branch('w_nominal', w_nomjerup, 'w_nominal/F')
               treejerdown_new.Branch('w_nominal', w_nomjerdown, 'w_nominal/F')
               for event in xrange(0, tree.GetEntries()):
                    tree.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/tree.GetEntries()))
                    w_nom[0] = tree.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    for i in xrange(1, nbins):
                         w_PDF[i] = h_pdfw_tmp.GetBinContent(i+1)/h_genw_tmp.GetBinContent(2) 
                    tree_new.Fill()
               outfile.cd()
               tree_new.Write()
               infile.cd()
               for event in xrange(0, treejesup.GetEntries()):
                    treejesup.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejesup.GetEntries()))
                    w_nomjesup[0] = treejesup.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    treejesup_new.Fill()
               outfile.cd()
               treejesup_new.Write()
               infile.cd()
               for event in xrange(0, treejesdown.GetEntries()):
                    treejesdown.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejesdown.GetEntries()))
                    w_nomjesdown[0] = treejesdown.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    treejesdown_new.Fill()
               outfile.cd()
               treejesdown_new.Write()
               infile.cd()
               for event in xrange(0, treejerup.GetEntries()):
                    treejerup.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejerup.GetEntries()))
                    w_nomjerup[0] = treejerup.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    treejerup_new.Fill()
               outfile.cd()
               treejerup_new.Write()
               infile.cd()
               for event in xrange(0, treejerdown.GetEntries()):
                    treejerdown.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejerdown.GetEntries()))
                    w_nomjerdown[0] = treejerdown.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    treejerdown_new.Fill()
               outfile.cd()
               treejerdown_new.Write()
               outfile.Close()
               print('\n')
          else:
               os.popen("mv " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + ".root")

def cutToTag(cut):
     
     newstring=""
     if "(TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" in cut: newstring=newstring+"_LepIso"
     if "FatJet_M_nominal<50" in cut: newstring=newstring+"_FatJet_Low"
     if "FatJet_M_nominal>=50 && FatJet_M_nominal<110" in cut: newstring=newstring+"_FatJet_Medium"
     if "FatJet_M_nominal>=110" in cut: newstring=newstring+"_FatJet_Heavy"
     if "(TightMu_pt_nominal!=0 || TightEl_pt_nominal!=0)" in cut: newstring=newstring+"_TightLep"
     if "HLT_PFJet_nominal==0" in cut: newstring=newstring+"_NoHLTJet"
     if "top_region_nominal==-1" in cut: newstring=newstring+"_TopVeto"
     if "top_region_nominal==0" in cut: newstring=newstring+"_TopL"
     if "top_region_nominal==1" in cut:newstring=newstring+"_TopT"
     if "AK8_region_nominal==0" in cut:newstring=newstring+"_FatJetVeto"
     if "AK8_region_nominal==1" in cut:newstring=newstring+"_FatJetL"
     if "AK8_region_nominal==2" in cut:newstring=newstring+"_FatJetT"
     if "Fwd4_region_nominal==0"in cut: newstring=newstring+"_Fwd0"
     if"Fwd4_region_nominal==1"in cut:newstring=newstring+"_Fwd1"
     if "FatJet_M_nominal>=100 && FatJet_M_nominal<=140" in cut : newstring=newstring+"_HiggsMass"
     if "FatJet_M_nominal<100 || FatJet_M_nominal>140" in cut: newstring=newstring+"_NotHiggsMass"
     if "Top_isMerg_nominal==1" in cut: newstring=newstring+"_Merg"
     if"Top_isMerg_nominal==0" in cut:newstring=newstring+"_Res"
     if "Top_pt_nominal>=500" in cut: newstring=newstring+"_HighPt"
     if"Top_pt_nominal<500" in cut: newstring=newstring+"_LowPt"
     if"Top_M_nominal==0" in cut: newstring=newstring+"_noTop"
     if"Top_M_nominal>=80" in cut: newstring=newstring+"_TopM"
     if "FatJet_pt_nominal[0]>=500" in cut : newstring=newstring+"_AK8HighPt"
     #newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
     return newstring

###def plot(lep, reg, variable, sample, cut_tag, syst):
def plot(lep, reg, variable, sample, cut_tag, syst, f1, fout):
     print "plotting ", variable._name, " for sample ", sample.label, " with cut ", cut_tag, " ", syst,
     ROOT.TH1.SetDefaultSumw2()
     ###f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
     treename = "events_nominal"
     if(cut_tag == ""):
          if variable._name=='TightEl_pt_nominal+TightMu_pt_nominal':
               histoname = "h_" + "TightLep_pt_nominal"
          elif variable._name== 'WprAK8_tau3/WprAK8_tau2':
               histoname =  "h_" + "_WprAK8_tau32"
          else:
               histoname = "h_"  + variable._name
     else:
          if variable._name=='TightEl_pt_nominal+TightMu_pt_nominal':
               histoname = "h_" + "TightLep_pt_nominal" + cut_tag
          elif variable._name== 'WprAK8_tau3/WprAK8_tau2':
               histoname =  "h_"+ "_WprAK8_tau32_" + cut_tag
          else:
               histoname = "h_" + variable._name + "" + cut_tag
     if"/" in histoname: histoname =histoname.replace('/',"_over_")
     if"(" in histoname: histoname = "h_deltaR"+cut_tag
     nbins = 0
     h1 = ROOT.TH1F()
     if variable._nbins == None:
          nbins = len(variable._xarray)-1
          h1 = ROOT.TH1F(histoname, variable._name , nbins, variable._xarray)
     else:
          nbins = variable._nbins
          h1 = ROOT.TH1F(histoname, variable._name , variable._nbins, variable._xmin, variable._xmax)
     h1.Sumw2()
     cut= variable._taglio #change
     cut = cut+"*(HLT_Muon_nominal!=0 || HLT_Electron_nominal!=0 || HLT_Photon_nominal!=0 || HLT_PFJet_nominal!=0)*((N_muLoose_nominal[0]+N_elLoose_nominal[0])==0 && (Top_TvsQCD_nominal[0]>0.6 || top_region_nominal<0) && FatJet_pt_nominal[0]>400 && (top_region_nominal[0]<0 || Lep_pt_nominal[0]>30))"
     #print("Check trigSF")
     #if not "Data" in sample.label: cut = cut+"*trigSF*lepSF"     
     if 'muon' in lep: 
          # change cut = variable._taglio + '*isMu'
          lep_flav=13
     elif 'electron' in lep:
          #  changecut  = variable._taglio + '*isEle'
          lep_flav=11
          if 'MC' in variable._name:
               cut = cut + "*(" + str(variable._name) + "!=-100.)"
     print str(cut)
     ###foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep+".root"
     if not 'Data' in sample.label: 
          if(syst.startswith("jer") or syst.startswith("jes")):
               treename = "events_"+syst
               ###foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep + "_" + syst + ".root"
          elif(syst == ""):
               foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep + ".root"
          else:
               ###foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep + "_" + syst + ".root"
               if syst.endswith("Up"): normSF = syst.split("Up")[0]
               else:  normSF = syst.split("Down")[0]
               cut += '*'+syst+"/"+normSF+"SF"
     #print treename
     if not ("top_region_nominal==-1" in cut):
          if "muon" in lep:
               f1.Get(treename).Project(histoname,variable._name,cut+"*(abs(Top_flavour_nominal)=="+str(lep_flav)+" && Lep_pt_nominal>30)")
          else:
               f1.Get(treename).Project(histoname,variable._name,cut+"*(abs(Top_flavour_nominal)=="+str(lep_flav)+" && Lep_pt_nominal>35)")
     elif 'muon' in lep:
          f1.Get(treename).Project(histoname,variable._name,cut+"*(TightEl_pt_nominal==0 && TightMu_pt_nominal>30)")
     else:
          f1.Get(treename).Project(histoname,variable._name,cut+"*(TightMu_pt_nominal==0 && TightEl_pt_nominal>35)")
     #if not 'Data' in sample.label:
     #     h1.Scale((7.5)/35.89)
     #f1.Get(treename).Project(histoname,variable._name,cut)
     #if not 'Data' in sample.label:
     #     h1.Scale((7.5)/35.89)
     #h1.SetBinContent(1, h1.GetBinContent(0) + h1.GetBinContent(1))
     #h1.SetBinError(1, math.sqrt(pow(h1.GetBinError(0),2) + pow(h1.GetBinError(1),2)))
     #h1.SetBinContent(nbins, h1.GetBinContent(nbins) + h1.GetBinContent(nbins+1))
     #h1.SetBinError(nbins, math.sqrt(pow(h1.GetBinError(nbins),2) + pow(h1.GetBinError(nbins+1),2)))
     #for i in range(0, nbins+1):
     #     content = h1.GetBinContent(i)
     #     if(content<0.):
     #          h1.SetBinContent(i, 0.00001)
     #fout.cd()
     #h1.Write("", ROOT.TObject.kOverwrite)
     h1.SetBinContent(1, h1.GetBinContent(0) + h1.GetBinContent(1))
     h1.SetBinError(1, math.sqrt(pow(h1.GetBinError(0),2) + pow(h1.GetBinError(1),2)))
     h1.SetBinContent(nbins, h1.GetBinContent(nbins) + h1.GetBinContent(nbins+1))
     h1.SetBinError(nbins, math.sqrt(pow(h1.GetBinError(nbins),2) + pow(h1.GetBinError(nbins+1),2)))
     for i in range(0, nbins+1):
          content = h1.GetBinContent(i)
          if(content<0.):
               h1.SetBinContent(i, 0.)
     ####fout = ROOT.TFile.Open(foutput, "UPDATE")
     fout.cd()
     #h1.Write()
     h1.Write("", ROOT.TObject.kOverwrite)
     ###fout.Close()
     ###f1.Close()

def makestack(lep_, reg_, variabile_, samples_, cut_tag_, syst_, lumi):
     os.system('set LD_PRELOAD=libtcmalloc.so')
     f = open("integral_txt/Integral.txt", "a")
     if variabile_._name=='TightEl_pt_nominal+TightMu_pt_nominal':
          variabile_._name = 'TightLep_pt_nominal' 
     elif variabile_._name== 'TightEl_pt_nominal+TightMu_pt_nominal':
          variabile_._name = 'TightLep_pt_nominal'
     infile = {}
     histo = []
     tmp = ROOT.TH1F()
     h = ROOT.TH1F()
     hdata = ROOT.TH1F()
     nbins = 0
     xmin = 0.
     xmax = 100.
     if variabile_._nbins == None:
          nbins = len(variabile_._xarray)-1
          hdata = ROOT.TH1F('h','h', nbins, variabile_._xarray)
          xmin = variabile_._xarray[0]
          xmax = variabile_._xarray[-1]
     else:
          nbins = variabile_._nbins
          hdata = ROOT.TH1F('h','h', variabile_._nbins, variabile_._xmin, variabile_._xmax)
          xmin = variabile_._xmin
          xmax = variabile_._xmax
     h_sig = []
     h_err = ROOT.TH1F()
     h_bkg_err = ROOT.TH1F()
     blind = False
     print "Variabile:", variabile_._name
     ROOT.gROOT.SetStyle('Plain')
     ROOT.gStyle.SetPalette(1)
     ROOT.gStyle.SetOptStat(0)
     ROOT.TH1.SetDefaultSumw2()
     if(cut_tag_ == ""):
          histoname = "h_"  + variabile_._name
          stackname = "stack_"  + variabile_._name
          canvasname = "stack_"  + variabile_._name + "_" + lep_ + "_" + str(samples_[0].year)
     else:
          histoname = "h_"+variabile_._name+""+cut_tag_
          stackname = "stack_"+variabile_._name+""+cut_tag_
          canvasname = "stack_"+variabile_._name+""+cut_tag_+lep_ + "_" + str(samples_[0].year)
     if"/" in histoname: 
          histoname =histoname.replace('/',"_over_")
          cansvasname =canvasname.replace('/',"_over_")
          stackname =stackname.replace('/',"_over_")
     if"(" in histoname: 
          histoname = "h_deltaR"+cut_tag
          stack_name= "stack_deltaR"+cut_tag_
          cansvasname= "stack_deltaR"+cut_tag_+lep_+"_"+str(samples_[0].year)
     if(("top_region_nominal==1" in opt.cut or "top_region_nominal==0" in opt.cut) and "AK8_region_nominal==2" in opt.cut):
     #if("selection_AND_best_Wpjet_isbtag_AND_best_topjet_isbtag" in cut_tag_ ) or ("selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag" in cut_tag_ ) or  ("selection_AND_best_topjet_isbtag_EQ_0_AND_best_Wpjet_isbtag" in cut_tag_ ):
          blind = True
     if("AK8_region_nominal==0" in opt.cut ):
          blind = False
     stack = ROOT.THStack(stackname, variabile_._name)
     leg_stack = ROOT.TLegend(0.33,0.62,0.91,0.87)
     signal = False

     print samples_
     for s in samples_:
          if('Tprime' in s.label):
               signal = True
          if(syst_ == ""):
               outfile = plotrepo + "stack_" + str(lep_).strip('[]') + ".root"
               infile[s.label] = ROOT.TFile.Open(plotrepo + "plot/" + lep + "/" + s.label + "_" + lep + ".root")
          else:
               outfile = plotrepo + "stack_"+syst_+"_"+str(lep_).strip('[]')+".root"
               if not "Data" in s.label:infile[s.label] = ROOT.TFile.Open(plotrepo + "plot/" + lep + "/" + s.label + "_" + lep + "_" + syst_ + ".root")
               else:infile[s.label] = ROOT.TFile.Open(plotrepo + "plot/" + lep + "/" + s.label + "_" + lep + ".root")
     i = 0

     if variabile_._name == "Tprime_M_nominal": f.write(cut_tag_+"\n")
     for s in samples_:
          infile[s.label].cd()
          print "opening file: ", infile[s.label].GetName()
          if('Data' in s.label):
               if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                    continue
          tmp = (ROOT.TH1F)(infile[s.label].Get(histoname))
          tmp.SetLineColor(ROOT.kBlack)
          tmp.SetName(s.leglabel)
          if variabile_._name == "Tprime_M_nominal":f.write(s.label+" \t "+str(tmp.Integral())+"\n")
          if('Data' in s.label):
               if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                    continue
               hdata.Add(ROOT.TH1F(tmp.Clone("")))
               hdata.SetMarkerStyle(20)
               hdata.SetMarkerSize(0.9)
               if(i == 0 and not blind): # trick to add Data flag to legend only once
                    leg_stack.AddEntry(hdata, "Data", "ep")
               i += 1
          elif('Tprime' in s.label):
               #tmp.SetLineStyle(9)
               if opt.tostack:
                    tmp.SetLineColor(s.color)
               else:
                    tmp.SetLineColor(s.color)
               #tmp.SetLineWidth(3)
               tmp.SetMarkerSize(0.)
               tmp.SetMarkerColor(s.color)
               if('_600' in s.label) or ('_1200' in s.label) or ('_1800' in s.label): h_sig.append(ROOT.TH1F(tmp.Clone("")))
          else:
               tmp.SetOption("HIST SAME")
               tmp.SetTitle("")
               if opt.tostack:
                    tmp.SetFillColor(s.color)
               else:
                    tmp.SetLineColor(s.color)
               histo.append(tmp.Clone(""))
               stack.Add(tmp.Clone(""))
          tmp.Reset("ICES")
     for hist in reversed(histo):
          if not ('Data' in hist.GetName()):
               leg_stack.AddEntry(hist, hist.GetName(), "f")
     #style options
     print "Is it blind? " + str(blind)
     leg_stack.SetNColumns(2)
     leg_stack.SetFillColor(0)
     leg_stack.SetFillStyle(0)
     leg_stack.SetTextFont(42)
     leg_stack.SetBorderSize(0)
     leg_stack.SetTextSize(0.05)
     c1 = ROOT.TCanvas(canvasname,"c1",50,50,700,600)
     c1.SetFillColor(0)
     c1.SetBorderMode(0)
     c1.SetFrameFillStyle(0)
     c1.SetFrameBorderMode(0)
     c1.SetLeftMargin( 0.12 )
     c1.SetRightMargin( 0.9 )
     c1.SetTopMargin( 1 )
     c1.SetBottomMargin(-1)
     c1.SetTickx(1)
     c1.SetTicky(1)
     c1.cd()

     pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
     pad1.SetTopMargin(0.1)
     pad1.SetBottomMargin(0.02)
     pad1.SetLeftMargin(0.12)
     pad1.SetRightMargin(0.05)
     pad1.SetBorderMode(0)
     pad1.SetTickx(1)
     pad1.SetTicky(1)
     pad1.Draw()
     pad1.cd()
     if not blind:
          maximum = max(stack.GetMaximum(),hdata.GetMaximum())
     else:
          maximum = stack.GetMaximum()
     logscale =  True
     if(logscale):
          pad1.SetLogy()
          stack.SetMaximum(maximum*1000)
     else:
          stack.SetMaximum(maximum*1.6)
     stack.SetMinimum(0.01)
     if opt.tostack:
          stack.Draw("HIST")
     else:
          stack.Draw("HIST NOSTACK")
     if variabile_._nbins == None:
          ytitle = "Events / bin width"
     else:
          step = float(variabile_._xmax - variabile_._xmin)/float(variabile_._nbins)
          print str(step)
          if "GeV" in variabile_._title:
               if step.is_integer():
                    ytitle = "Events / %.0f GeV" %step
               else:
                    ytitle = "Events / %.2f GeV" %step
          else:
               if step.is_integer():
                    ytitle = "Events / %.0f units" %step
               else:
     
                    ytitle = "Events / %.2f units" %step
     
     stack.GetYaxis().SetTitle(ytitle)
     stack.GetYaxis().SetTitleFont(42)
     stack.GetXaxis().SetLabelOffset(1.8)
     stack.GetYaxis().SetTitleOffset(0.85)
     stack.GetXaxis().SetLabelSize(0.15)
     stack.GetYaxis().SetLabelSize(0.07)
     stack.GetYaxis().SetTitleSize(0.07)
     stack.SetTitle("")
     
     if(signal):
          for hsig in h_sig:
               #hsig.Scale(1000)
               hsig.Draw("same")
               leg_stack.AddEntry(hsig, hsig.GetName(), "l")
               print("Signal",hsig.GetName(),hsig.Integral())
     
     
     #f.write(hsig.GetName()+" "+str(hsig.Integral())+"\n")
     h_err = stack.GetStack().Last().Clone("h_err")
     h_err.SetLineWidth(100)
     h_err.SetFillStyle(3154)
     h_err.SetMarkerSize(0)
     h_err.SetFillColor(ROOT.kGray+2)
     h_err.Draw("e2same0")
     leg_stack.AddEntry(h_err, "Stat. Unc.", "f")
     if not blind: 
          print(hdata.Integral())
          hdata.Draw("eSAMEpx0")
     else:
          hdata = stack.GetStack().Last().Clone("h_data")
     leg_stack.Draw("same")

     CMS_lumi.writeExtraText = 1
     CMS_lumi.extraText = ""
     if str(lep_).strip('[]') == "muon":
          lep_tag = "#mu+"
     elif str(lep_).strip('[]') == "electron":
          lep_tag = "e+"
          
     lumi_sqrtS = "%s fb^{-1}  (13 TeV)"%(lumi)
     
     iPeriod = 0
     iPos = 11
     CMS_lumi(pad1, lumi_sqrtS, iPos, lep_tag+str(reg_))
     hratio = stack.GetStack().Last()
     
     c1.cd()
     pad2= ROOT.TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
     pad2.SetTopMargin(0.05)
     pad2.SetBottomMargin(0.45)
     pad2.SetLeftMargin(0.12)
     pad2.SetRightMargin(0.05)
     ROOT.gStyle.SetHatchesSpacing(2)
     ROOT.gStyle.SetHatchesLineWidth(2)
     c1.cd()
     pad2.Draw()
     pad2.cd()
     ratio = hdata.Clone("ratio")
     if ratio.Integral()!=0: print("Data MC Discrepancy: "+str((ratio.Integral()-hratio.Integral())/ratio.Integral()))
     ratio.SetLineColor(ROOT.kBlack)
     ratio.SetMaximum(1.5)
     ratio.SetMinimum(0.5)
     ratio.Sumw2()
     ratio.SetStats(0)
     
     ratio.Divide(hratio)
     ratio.SetMarkerStyle(20)
     ratio.SetMarkerSize(0.9)
     ratio.Draw("epx0e0")
     ratio.SetTitle("")
     
     h_bkg_err = hratio.Clone("h_err")
     h_bkg_err.Reset()
     h_bkg_err.Sumw2()
     for i in range(1,hratio.GetNbinsX()+1):
          h_bkg_err.SetBinContent(i,1)
          if(hratio.GetBinContent(i)):
               h_bkg_err.SetBinError(i, (hratio.GetBinError(i)/hratio.GetBinContent(i)))
          else:
               h_bkg_err.SetBinError(i, 10^(-99))
     h_bkg_err.SetLineWidth(100)

     h_bkg_err.SetMarkerSize(0)
     h_bkg_err.SetFillColor(ROOT.kGray+1)
     h_bkg_err.Draw("e20same")
     
     f1 = ROOT.TLine(xmin, 1., xmax,1.)
     f1.SetLineColor(ROOT.kBlack)
     f1.SetLineStyle(ROOT.kDashed)
     f1.Draw("same")
     
     ratio.GetYaxis().SetTitle("Data / MC")
     ratio.GetYaxis().SetNdivisions(503)
     ratio.GetXaxis().SetLabelFont(42)
     ratio.GetYaxis().SetLabelFont(42)
     ratio.GetXaxis().SetTitleFont(42)
     ratio.GetYaxis().SetTitleFont(42)
     ratio.GetXaxis().SetTitleOffset(1.1)
     ratio.GetYaxis().SetTitleOffset(0.35)
     ratio.GetXaxis().SetLabelSize(0.15)
     ratio.GetYaxis().SetLabelSize(0.15)
     ratio.GetXaxis().SetTitleSize(0.16)
     ratio.GetYaxis().SetTitleSize(0.16)
     ratio.GetYaxis().SetRangeUser(0.5,1.5)
     ratio.GetXaxis().SetTitle(variabile_._title)
     ratio.GetXaxis().SetLabelOffset(0.04)
     ratio.GetYaxis().SetLabelOffset(0.02)
     ratio.Draw("epx0e0same")

     c1.cd()
     #ROOT.TGaxis.SetMaxDigits(3)
     
     c1.RedrawAxis()
     pad2.RedrawAxis()
     c1.Update()
     if syst_=="":
          c1.Print(plotrepo + "stack/"+canvasname+".png")
          c1.Print(plotrepo + "stack/"+canvasname+".pdf")
     else:
          c1.Print(plotrepo + "stack/"+canvasname+"_"+syst_+".png")                                                                                                                              
          c1.Print(plotrepo + "stack/"+canvasname+"_"+syst_+".pdf")
     del histo
     tmp.Delete()
     h.Delete()
     del tmp
     del h
     del h_sig
     h_err.Delete()
     del h_err
     h_bkg_err.Delete()
     del h_bkg_err
     hratio.Delete()
     del hratio
     stack.Delete()
     del stack
     pad1.Delete()
     del pad1
     pad2.Delete()
     del pad2
     c1.Delete()
     del c1
     f.close()
     for s in samples_:
          infile[s.label].Close()
          infile[s.label].Delete()
     os.system('set LD_PRELOAD=libtcmalloc.so')


#def plot(lep, reg, variable, sample, cut_tag, syst, f1, fout):
#def fitplot(lep,variable, year,cut, syst):
def fitplot(lep,variable, year,cut, syst,f1):
          
     ROOT.TH1.SetDefaultSumw2()
     #f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
     treename = "events_nominal"
     h1 = ROOT.TH1F()

     if(cut == ""):
          if variable._name=='TightEl_pt_nominal+TightMu_pt_nominal':
               histoname = "h_" + "TightLep_pt_nominal"
          elif variable._name== 'WprAK8_tau3/WprAK8_tau2':
               histoname =  "h_" + "_WprAK8_tau32"
          else:
               histoname = "h_"  + variable._name
     else:
          if variable._name=='TightEl_pt_nominal+TightMu_pt_nominal':
               histoname = "h_" + "TightLep_pt_nominal"
          elif variable._name== 'WprAK8_tau3/WprAK8_tau2':
               histoname =  "h_"+ "_WprAK8_tau32_" 
          else:
               histoname = "h_" + variable._name + ""


     #histoname= "h_"+variable._name+""
     if "(TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" in cut: histoname=histoname+"_LepIso"
     if "FatJet_M_nominal<50" in cut: histoname=histoname+"_FatJet_Low"
     if "FatJet_M_nominal>=50 && FatJet_M_nominal<110" in cut: histoname=histoname+"_FatJet_Medium"
     if "FatJet_M_nominal>=110" in cut: histoname=histoname+"_FatJet_Heavy"
     if "top_region_nominal==-1" in cut: histoname=histoname+"_TopVeto"
     if "top_region_nominal==0" in cut: histoname=histoname+"_TopL"
     if "top_region_nominal==1" in cut: histoname=histoname+"_TopT"
     if "AK8_region_nominal==0" in cut: histoname=histoname+"_FatJetVeto"
     if"AK8_region_nominal==1" in cut: histoname=histoname+"_FatJetL"
     if"AK8_region_nominal==2" in cut: histoname=histoname+"_FatJetT"
     if"Top_isMerg_nominal==1" in cut: histoname=histoname+"_Merg"
     if"Top_isMerg_nominal==0" in cut: histoname=histoname+"_Res"
     if"Top_pt_nominal>=500" in cut: histoname=histoname+"_HighPt"
     if"Top_pt_nominal<500" in cut: histoname=histoname+"_LowPt"
     if"Top_M_nominal==0" in cut: histoname=histoname+"_noTop"
     if"Top_M_nominal>=80" in cut: histoname=histoname+"_TopM"
     if "FatJet_pt_nominal[0]>=500" in cut : histoname=histoname+"_AK8HighPt"

     
     if variable._nbins == None:
          nbins = len(variable._xarray)-1
          h1 = ROOT.TH1F(histoname, variable._name , nbins, variable._xarray)
     else:
          nbins = variable._nbins
          h1 = ROOT.TH1F(histoname, variable._name , variable._nbins, variable._xmin, variable._xmax)
     h1.Sumw2()
     cut= variable._taglio                                                                                                                                                                                      
     string_name=""
     if "FatJet_M_nominal<=20" in cut: string_name="_FatJetLowMass"
     if "FatJet_MC_nominal==1" in cut: string_name="_FatJet1b"
     if "FatJet_MC_nominal==11" in cut: string_name="_FatJet1b1l"
     if "FatJet_MC_nominal==101" in cut: string_name="_FatJet1b1q"
     if "FatJet_MC_nominal==201" in cut: string_name="_FatJet1b2q"
     if "FatJet_MC_nominal==200" in cut: string_name="_FatJet2q"
     if "FatJet_MC_nominal!=" in cut: string_name="_FatJetOth"
     if "Top_MC_nominal==1" in cut: string_name+="_TopTrue"
     if "Top_MC_nominal!=1" in cut: string_name+="_TopFake"
     if "Top_MC_nominal==0" in cut: string_name+="_Top0prompt"
     if "Top_MC_nominal>1" in cut: string_name+="_Top1prompt"     
     #if "FatJet_MC_nominal!=" in cut: string_name="_FatJetOth"
     print "plotting ", variable._name, " for sample ", string_name, " with cut ", cut, " ", syst
     if 'muon' in lep: lep_flav=13
     elif 'electron' in lep:  lep_flav=11
     foutput = plotrepo + "plot/" + lep + "/" + sample.label[:-9] + string_name+"_"+year+"_"+lep+".root"
     cut = cut+"*(HLT_Muon_nominal!=0 || HLT_Electron_nominal!=0 || HLT_Photon_nominal!=0 || HLT_PFJet_nominal!=0)*((N_muLoose_nominal[0]+N_elLoose_nominal[0])==0 && (Top_TvsQCD_nominal[0]>0.6 || top_region_nominal<0) && FatJet_pt_nominal[0]>400 && (top_region_nominal[0]<0 || Lep_pt_nominal[0]>30))"
     if not 'Data' in sample.label:
          if(syst.startswith("jer") or syst.startswith("jes")):
               treename = "events_"+syst
               foutput = plotrepo + "plot/" + lep + "/"+sample.label[:2] + string_name+"_"+year+"_"+lep + "_" + syst + ".root"
          elif(syst == ""):
               foutput = plotrepo + "plot/" + lep + "/" + sample.label[:2] + string_name+"_"+year+ "_" + lep + ".root"
          else:
               foutput = plotrepo + "plot/" + lep + "/" +  sample.label[:2] + string_name+"_"+year+"_" + lep + "_" + syst + ".root"
               if syst.endswith("Up"): normSF = syst.split("Up")[0]
               else:  normSF = syst.split("Down")[0]
               cut += '*'+syst+"/"+normSF+"SF"
     #f1.Get(treename).Project(histoname,variable._name,cut+"*(abs(Top_flavour_nominal)=="+str(lep_flav)+")")
     print(foutput +" \n")
     if not ("top_region_nominal==-1" in cut):
          if "muon" in lep:
               f1.Get(treename).Project(histoname,variable._name,cut+"*(abs(Top_flavour_nominal)=="+str(lep_flav)+" && Lep_pt_nominal>30)")
          else:
               f1.Get(treename).Project(histoname,variable._name,cut+"*(abs(Top_flavour_nominal)=="+str(lep_flav)+" && Lep_pt_nominal>35)")
     elif 'muon' in lep:
          f1.Get(treename).Project(histoname,variable._name,cut+"*(TightEl_pt_nominal==0 && TightMu_pt_nominal>30)")
     else:
          f1.Get(treename).Project(histoname,variable._name,cut+"*(TightMu_pt_nominal==0 && TightEl_pt_nominal>35)")
     h1.SetBinContent(1, h1.GetBinContent(0) + h1.GetBinContent(1))
     h1.SetBinError(1, math.sqrt(pow(h1.GetBinError(0),2) + pow(h1.GetBinError(1),2)))
     h1.SetBinContent(nbins, h1.GetBinContent(nbins) + h1.GetBinContent(nbins+1))
     h1.SetBinError(nbins, math.sqrt(pow(h1.GetBinError(nbins),2) + pow(h1.GetBinError(nbins+1),2)))
     for i in range(0, nbins+1):
          content = h1.GetBinContent(i)
          if(content<0.):
               h1.SetBinContent(i, 0.)
     fout = ROOT.TFile.Open(foutput, "UPDATE")
     fout.cd()
     h1.Write()
     fout.Close()
     #f1.Close()




#dataset_dict = {'2016':[],'2017':[],'2018':[],'2018_nodata':[]}
dataset_dict = {'2016':[],'2016preVFP':[],'2016postVFP':[],'2017':[],'2018':[],'2018_nodata':[]} #Cambio 2016
if(opt.dat!= 'all'):
     if not(opt.dat in sample_dict.keys()):
          print sample_dict.keys()
     dataset_names = map(str, opt.dat.strip('[]').split(','))
     #print dataset_names.keys()
     samples = []
     [samples.append(sample_dict[dataset_name]) for dataset_name in dataset_names]
     [dataset_dict[str(sample.year)].append(sample) for sample in samples]
     #print(dataset_names)
else:
     dataset_dict = {
          '2016preVFP':[ST_2016preVFP,WJets_2016preVFP, QCD_2016preVFP, TT_Mtt_2016preVFP,DataEle_2016preVFP,DataPh_2016preVFP,DataHT_2016preVFP,Tprime_tHq_1800LH_2016preVFP,Tprime_tHq_600LH_2016preVFP,Tprime_tHq_1200LH_2016preVFP,DataMu_2016preVFP],
          '2016postVFP':[ST_2016postVFP,WJets_2016postVFP, QCD_2016postVFP, TT_Mtt_2016postVFP,DataMu_2016postVFP,DataEle_2016postVFP,DataPh_2016postVFP,DataHT_2016postVFP,Tprime_tHq_1800LH_2016postVFP,Tprime_tHq_600LH_2016postVFP,Tprime_tHq_1200LH_2016postVFP],
          '2016':[ST_2016,WJets_2016, QCD_2016, TT_Mtt_2016, DataMu_2016,DataEle_2016,DataPh_2016,DataHT_2016,Tprime_tHq_1800LH_2016],#Tprime_tHq_600LH_2016,Tprime_tHq_1200LH_2016],# Tprime_tHq_600LH_2016,Tprime_tHq_700LH_2016,Tprime_tHq_800LH_2016,Tprime_tHq_900LH_2016,Tprime_tHq_1000LH_2016,Tprime_tHq_1100LH_2016,Tprime_tHq_1200LH_2016,Tprime_tHq_1300LH_2016,Tprime_tHq_1400LH_2016,Tprime_tHq_1600LH_2016,Tprime_tHq_1700LH_2016],
          #'2017':[ST_2017,WJets_2017, QCD_2017, TT_Mtt_2017, Tprime_tHq_600LH_2017,Tprime_tHq_700LH_2017,Tprime_tHq_800LH_2017,Tprime_tHq_900LH_2017,Tprime_tHq_1000LH_2017,Tprime_tHq_1100LH_2017,Tprime_tHq_1200LH_2017,Tprime_tHq_1300LH_2017,Tprime_tHq_1400LH_2017,Tprime_tHq_1600LH_2017,Tprime_tHq_1700LH_2017,Tprime_tHq_1800LH_2017],
          '2017':[ST_2017,WJets_2017, QCD_2017,TT_Mtt_2017,DataHT_2017,DataMu_2017,DataEle_2017,DataPh_2017,Tprime_tHq_1800LH_2017],#Tprime_tHq_600LH_2017,Tprime_tHq_1200LH_2017],
          '2018': [ST_2018,WJets_2018, QCD_2018,TT_Mtt_2018,DataHT_2018,DataMu_2018,DataEle_2018,Tprime_tHq_1800LH_2018],#Tprime_tHq_600LH_2018,Tprime_tHq_1200LH_2018],#TTVJets_2018,TTGammaJets_2018,TTH_2018,TGJets_2018],#Tprime_tHq_600LH_2018,Tprime_tHq_700LH_2018,Tprime_tHq_800LH_2018,Tprime_tHq_900LH_2018,Tprime_tHq_1000LH_2018,Tprime_tHq_1100LH_2018,Tprime_tHq_1200LH_2018,Tprime_tHq_1300LH_2018,Tprime_tHq_1400LH_2018,Tprime_tHq_1600LH_2018,Tprime_tHq_1700LH_2018,Tprime_tHq_1800LH_2018,DataMu_2018,Tprime_tHq_1500LH_2018, DataEle_2018, DataHT_2018, TT_Mtt_2018],
          #'2018':[ST_2018,WJets_2018, QCD_2018, Tprime_tHq_600LH_2018,Tprime_tHq_700LH_2018,Tprime_tHq_800LH_2018,Tprime_tHq_900LH_2018,Tprime_tHq_1000LH_2018,Tprime_tHq_1100LH_2018,Tprime_tHq_1200LH_2018,Tprime_tHq_1300LH_2018,Tprime_tHq_1400LH_2018,Tprime_tHq_1600LH_2018,Tprime_tHq_1700LH_2018,Tprime_tHq_1800LH_2018,Tprime_tHq_1500LH_2018, TT_Mtt_2018]
          '2018_nodata': [ST_2018,WJets_2018, QCD_2018, Tprime_tHq_600LH_2018,Tprime_tHq_700LH_2018,Tprime_tHq_800LH_2018,Tprime_tHq_900LH_2018,Tprime_tHq_1000LH_2018,Tprime_tHq_1100LH_2018,Tprime_tHq_1200LH_2018,Tprime_tHq_1300LH_2018,Tprime_tHq_1400LH_2018,Tprime_tHq_1600LH_2018,Tprime_tHq_1700LH_2018,Tprime_tHq_1800LH_2018,Tprime_tHq_1500LH_2018, #TT_Mtt_2018,
                          DataEle_2018, DataHT_2018]
     }
#print(dataset_dict.keys())



years = []
if(opt.year!='all'):
     years = map(str,opt.year.strip('[]').split(','))
else:
     years = ['2018']
print(years)

leptons = map(str,opt.lep.split(',')) 

cut = opt.cut #default cut must be obvious, for example lepton_eta>-10.
#cut = "Top_M1_nominal>0"
cut_dict = {"muon":cut,"electron":cut}
cut_tag=cutToTag(opt.cut)
""" change
if opt.cut == "lepton_eta>-10." and not opt.sel:
     cut_dict = {'muon':"lepton_pt>55", #&&MET_pt>80",#&&best_topjet_isbtag==0&&best_Wpjet_isbtag==1&&nbjet_pt100==1", 
                 'electron':"lepton_pt>50&&abs(lepton_eta)<2.2"#&&MET_pt>80"#&&best_topjet_isbtag==0&&best_Wpjet_isbtag==1&&nbjet_pt100==1",
     }
     cut_tag = ""
else:
     if opt.sel:
          cut_dict = {'muon':"MET_pt>120&&lepton_pt>55&&leadingjet_pt>300&&subleadingjet_pt>150&&" + cut, 
                      'electron':"MET_pt>120&&lepton_pt>50&&leadingjet_pt>300&&subleadingjet_pt>150&&abs(lepton_eta)<2.2&&" + cut
          }
          #cut_dict = {'muon':"MET_pt>120&&lepton_pt>180&&leadingjets_pt>350&&best_top_pt>250&&" + cut, 
          #            'electron':"MET_pt>120&&lepton_pt>180&&leadingjets_pt>350&&best_top_pt>250&&" + cut
          #}
          if opt.cut != "lepton_eta>-10.":
               cut_tag = 'selection_AND_' + cutToTag(opt.cut) 
          else:
               cut_tag = 'selection' 
     else:
          cut_dict = {'muon':cut, 'electron':cut}
          cut_tag = cutToTag(opt.cut)
"""

#lumi = {'2016': 36.33, "2017": 41.48, "2018": 59.83,"2018_nodata":59.83}
#dataset_dict = {'2016preVFP':[],'2016postVFP':[],'2017':[],'2018':[],'2018_nodata':[]} #Cambio 2016
lumi = {'2016preVFP':19.5,'2016postVFP':16.8, "2017": 41.48, "2018": 59.83,"2018_nodata":59.83,"2016":36.3}#Cambio 2016
#
systematics = []
if opt.syst!="all" and opt.syst!="noSyst":
     for syst in (opt.syst).split(","):
          systematics.append(syst)
elif opt.syst!="all" and opt.syst=="noSyst":
    systematics.append("") #di default per syst="" alla variabile si applica il peso standard incluso nella macro macro_plot.C
else:
     systematics = ["", "jesUp",  "jesDown",  "jerUp",  "jerDown", "PFUp", "PFDown", "puUp", "puDown","lepUp", "lepDown", "trigUp", "trigDown"]#,"BDTUp","BDTDown","ParNetUp","ParNetDown"]#, "btagUp", "btagDown", "mistagUp", "mistagDown", "lepUp", "lepDown", "trigUp", "trigDown", "pdf_totalUp", "pdf_totalDown", "q2Up", "q2Down"]

for year in years:
     for sample in dataset_dict[year]:
          if(opt.merpart):
               mergepart(sample)
          if(opt.lumi):
               lumi_writer(sample, lumi[year])
          if(opt.mertree):
               if not('Tprime' in sample.label):
                    mergetree(sample)
          if(opt.mer2016):
               merge2016(sample)

for year in years:
     for lep in leptons:
          dataset_new = dataset_dict[year]
          variables = []
          #wzero = 'w_nominal*PFSF*puSF*w_pt*lepSF*trigSF*BDTSF*ParNetSF'               
          wzero = 'w_nominal*PFSF*puSF*w_pt*lepSF*trigSF'
          if year =="2017": 
               wzero=wzero+"*(FatJet_pt_nominal[0]>500)"
               print(wzero)
          print("No BDT and PN SF!!! Check")
          cut = cut_dict[lep]
          cut_tag_coll=[]
          #dR_jet_AK8_nominal
          #variables.append(variabile("dR_jet_AK8_nominal",'dR(jet,AK8)',wzero+'*('+cut+')',  40, 0, 3))
          #variables.append(variabile('N_jetHigh_nominal','N jet High',wzero+'*('+cut+')',  20,0,20))
          #variables.append(variabile('N_AK8_nominal','N AK8',wzero+'*('+cut+')',  10,1,11))
          #variables.append(variabile("deltaR(Jet_eta_nominal[0],Jet_phi_nominal[0],Lep_eta_nominal[0],Lep_phi_nominal[0])",'dR(jet,lep)',wzero+'*('+cut+')',  20, 0, 2))
          #variables.append(variabile("deltaR(Jet_eta_nominal[0],Jet_phi_nominal[0],Lep_eta_nominal[0],Lep_phi_nominal[0])",'dR(AK8,lep)',wzero+'*('+cut+')',  20, 0, 2))
          #variables.append(variabile("deltaR",'dR(jet,lep)',wzero+'*('+cut+')',  20, 0, 2))
          """
          variables.append(variabile('Lep_eta_nominal','Lep Eta',wzero+'*('+cut+')',  20, -5, 5))
          variables.append(variabile('Jet_eta_nominal','Jet Eta',wzero+'*('+cut+')',  20, -5, 5))
          
          variables.append(variabile('MET_phi_nominal','MET Phi',wzero+'*('+cut+')',  20, -3.14, 3.14))
          variables.append(variabile('Lep_phi_nominal','Lep Phi',wzero+'*('+cut+')',  20, -3.14, 3.14))
          variables.append(variabile('Jet_phi_nominal','Jet Phi',wzero+'*('+cut+')',  20, -3.14, 3.14))
          
          variables.append(variabile('MET_nominal','MET p_{T}',wzero+'*('+cut+')',  20, 25, 625))
          """
          #variables.append(variabile('Jet_eta_nominal','Jet Eta',wzero+'*('+cut+')',  20, -5, 5))
          #variables.append(variabile('FatJet_eta_nominal','FatJet Eta',wzero+'*('+cut+')',  20, -5, 5))
          #variables.append(variabile("sqrt((Jet_eta_nominal[0]-Lep_eta_nominal[0])**2+(Jet_phi_nominal[0]-Lep_phi_nominal[0])**2)",'dR(jet,lep)',wzero+'*('+cut+')',  20, 0, 2)) 
          #variables.append(variabile("sqrt((FatJet_eta_nominal[0]-Lep_eta_nominal[0])**2+(FatJet_phi_nominal[0]-Lep_phi_nominal[0])**2)",'dR(AK8,lep)',wzero+'*('+cut+')',  10, 0, 4))
          #variables.append(variabile("sqrt((FatJet_eta_nominal[0]-Lep_eta_nominal[0])**2)",'d_eta(AK8,lep)',wzero+'*('+cut+')',  10, 0, 4))
          ###variables.append(variabile('Tprime_M_nominal','Best T\' M',wzero+'*('+cut+')',  20, 600, 2600))
          ###variables.append(variabile('Tprime_M_nominal','Best T\' M',wzero+'*('+cut+')',  xarray=array('f',[600., 1000., 1500., 2000., 2500., 3000., 3500.])))
          #600., 1000., 1500., 2000., 2500., 3000., 3500.
          
          #variables.append(variabile('Top_pt_nominal','Best Top p_{T}',wzero+'*('+cut+')',  50, 50, 600))
          #variables.append(variabile('Top_TvsQCD_nominal','Best Top ScoreVsQCD',wzero+'*('+cut+')',  2, 0.6, 1))
          
          #variables.append(variabile('Top_TvsOth_nominal','Best Top ScoreVsOth',wzero+'*('+cut+')',  5, 0, 1))
          
          variables.append(variabile('FatJet_M_nominal','FatJet M',wzero+'*('+cut+')',  20, 0, 400))
          variables.append(variabile('FatJet_partM_nominal','FatJet M',wzero+'*('+cut+')',  20, 0, 400))
          #variables.append(variabile('FatJet_M_nominal','FatJet M new',wzero+'*('+cut+')',  80, 0, 400))
          
          ###variables.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD',wzero+'*('+cut+')',  20, 0, 1))
          #variables.append(variabile('FatJet_phi_nominal','FatJep Phi',wzero+'*('+cut+')',  20, -3.14, 3.14))                                                                                         
          #variables.append(variabile('FatJet_eta_nominal','FatJet Eta',wzero+'*('+cut+')',  20, -5, 5))
          #variables.append(variabile('FatJet_pt_nominal','FatJet p_{T}',wzero+'*('+cut+')',  20, 400, 1000))
          #variables.append(variabile('Top_M_nominal','Best Top M',wzero+'*('+cut+')',  20, 80, 480))
          #variables.append(variabile('MET_nominal','MET p_{T}',wzero+'*('+cut+')',  20, 25, 625))
         
          #variables.append(variabile('TightMu_pt_nominal','TightMu p_{T}',wzero+'*('+cut+')',  20, 35, 535))
          #variables.append(variabile('TightEl_pt_nominal','TightEl p_{T}',wzero+'*('+cut+')',  20, 35, 535))
          ###variables.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T}',wzero+'*('+cut+')',  20, 35, 635))
          """
          variables.append(variabile('TightMu_dxy_nominal','TightMu dxy',wzero+'*('+cut+')',  100, -2, 2))                                                                                      
          variables.append(variabile('TightMu_dxyerr_nominal','TightMu dxy err',wzero+'*('+cut+')',  50, 0, 2))                                                                                
          variables.append(variabile('TightMu_dz_nominal','TightMu dz',wzero+'*('+cut+')',  100, -2, 2))                                                                                        
          variables.append(variabile('TightMu_dzerr_nominal','TightMu dz err',wzero+'*('+cut+')',  50, 0, 2))                                                                                  
          variables.append(variabile('TightMu_Id_nominal','TightMu Id',wzero+'*('+cut+')',  6, -0.5, 5.5))                                                                                    
          variables.append(variabile('TightMu_pt_nominal','TightMu p_{T}',wzero+'*('+cut+')',  20, 25, 925))                                                                                   
          variables.append(variabile('TightMu_Iso_nominal','TightMu Iso',wzero+'*('+cut+')',  50, 0, 2))                                                                                       
          variables.append(variabile('TightMu_MiniIso_nominal','TightMu MiniIso',wzero+'*('+cut+')',  50, 0, 2))

          variables.append(variabile('TightEl_dxy_nominal','TightEl dxy',wzero+'*('+cut+')',  100, -2, 2))                                                                                      
          variables.append(variabile('TightEl_dxyerr_nominal','TightEl dxy err',wzero+'*('+cut+')',  50, 0, 2))                                                                                
          variables.append(variabile('TightEl_dz_nominal','TightEl dz',wzero+'*('+cut+')',  100, -2, 2))                                                                                        
          variables.append(variabile('TightEl_dzerr_nominal','TightEl dz err',wzero+'*('+cut+')',  50, 0, 2))                                                                                  
          variables.append(variabile('TightEl_Id_nominal','TightEl Id',wzero+'*('+cut+')',  6, -0.5, 5.5))                                                                                    
          variables.append(variabile('TightEl_pt_nominal','TightEl p_{T}',wzero+'*('+cut+')',  20, 25, 925))                                                                                   
          variables.append(variabile('TightEl_Iso_nominal','TightEl Iso',wzero+'*('+cut+')',  50, 0, 2))                                                                                       
          variables.append(variabile('TightEl_MiniIso_nominal','TightEl MiniIso',wzero+'*('+cut+')',  50, 0, 2))
          """
          #variables.append(variabile('Jet_pt_nominal','Jet p_{T}',wzero+'*('+cut+')',  20, 25, 925))
          #variables.append(variabile('Jet_M_nominal','Jet M',wzero+'*('+cut+')',  20, 25, 925))
          #variables.append(variabile('Jet_btag_nominal','Jet b-tag',wzero+'*('+cut+')',  20, 0, 1))
          #variables.append(variabile('Lep_dxy_nominal','Lep dxy',wzero+'*('+cut+')',  40, -2, 2))
          #variables.append(variabile('Lep_dxyerr_nominal','Lep dxy err',wzero+'*('+cut+')',  50, 0, 2))
          #variables.append(variabile('Lep_dz_nominal','Lep dz',wzero+'*('+cut+')',  40, -2, 2))
          #variables.append(variabile('Lep_dzerr_nominal','Lep dz err',wzero+'*('+cut+')',  50, 0, 2))
          #variables.append(variabile('Lep_Id_nominal','Lep Id',wzero+'*('+cut+')',  6, -0.5, 5.5))
          #variables.append(variabile('Lep_pt_nominal','Lep p_{T}',wzero+'*('+cut+')',  30, 30, 630))
          #variables.append(variabile('Lep_pt_nominal/Jet_pt_nominal','Lep p_{T}/Jet p_{T}',wzero+'*('+cut+')',  20, 0, 1))
          #variables.append(variabile('Lep_Iso_nominal','Lep Iso',wzero+'*('+cut+')',  20, 0, 2))
          #variables.append(variabile('Lep_MiniIso_nominal','Lep MiniIso',wzero+'*('+cut+')',  50, 0, 2))
          
          #variables.append(variabile('HLT_Muon_nominal','HLT Muon',wzero+'*('+cut+')',  2, -0.5, 1.5))
          #variables.append(variabile('HLT_Electron_nominal','HLT Electron',wzero+'*('+cut+')*(HLT_Muon_nominal==0)',  2, -0.5, 1.5))
          #variables.append(variabile('HLT_Photon_nominal','HLT Photon',wzero+'*('+cut+')*(HLT_Muon_nominal==0 && HLT_Electron_nominal==0)',  2, -0.5, 1.5))
          #variables.append(variabile('HLT_PFJet_nominal','HLT PFJet',wzero+'*('+cut+')*(HLT_Muon_nominal==0 && HLT_Electron_nominal==0 && HLT_Photon_nominal==0)',  2, -0.5, 1.5))
          #variables.append(variabile('Lep_pt_nominal','Lep p_{T}',wzero+'*('+cut+')',  20, 35, 535))
          cut_tag_coll=[cut_tag]*len(variables)

          for sample in dataset_new:
               if(opt.plot):
                    f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
                    for syst in systematics:
                         foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep+".root"
                         if syst!= "": foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep+ "_" + syst + ".root"
                         if "Data" in sample.label: foutput = plotrepo + "plot/" + lep + "/" + sample.label + "_" + lep+".root"
                         foption="UPDATE"
                         if(not os.path.exists(foutput)):foption="RECREATE"
                         fout = ROOT.TFile.Open(foutput, foption)
                         for var in variables:
                              if (("GenPart" in var._name) or ("MC_" in var._name)) and "Data" in sample.label:
                                   continue
                              plot(lep, 'jets', var, sample, cut_tag, syst, f1, fout)
                         fout.Close()
                    f1.Close()

               #for sample in dataset_new:

               #if(opt.plot):
               #     for syst in systematics:
               #          
               #          for var in variables:
               #               if (("GenPart" in var._name) or ("MC_" in var._name)) and "Data" in sample.label:
               #                    continue
                #              plot(lep, 'jets', var, sample, cut_tag_coll[variables.index(var)], syst)
               if(opt.fit) and (("TT" in sample.label) or ("ST" in sample.label)):
                    #if "TT" in sample.label:
                    #print("remember to change TT")
                    variables_fit = []
                    print(systematics)
                    ###variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag Top True',wzero+'*('+cut+')*(Top_MC_nominal==1)',  20, 0, 1))
                    ###variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag Top False',wzero+'*('+cut+')*(Top_MC_nominal!=1)',  20, 0, 1))

                    #variables.append(variabile('MET_nominal','MET p_{T}',wzero+'*('+cut+')',  20, 25, 625))
                    ###variables_fit.append(variabile('MET_nominal','MET Top True',wzero+'*('+cut+')*(Top_MC_nominal==1)',  20, 25, 625))
                    ###variables_fit.append(variabile('MET_nominal','MET Top False',wzero+'*('+cut+')*(Top_MC_nominal!=1)',  20, 25, 625))

                    """
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M Low Mass',wzero+'*('+cut+' && FatJet_M_nominal<=20)',  15, 0, 300))                             
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b',wzero+'*('+cut+' && FatJet_M_nominal>20 && FatJet_MC_nominal==1)',  15, 0, 300))                                 
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+1l',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==11)',  15, 0, 300))                              
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+1q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==101)',  15, 0, 300))                             
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==201)',  15, 0, 300))                             
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==200)',  15, 0, 300))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal!=200 && FatJet_MC_nominal!=1 && FatJet_MC_nominal!=11 && FatJet_MC_nominal!=101 && FatJet_MC_nominal!=201)',  15, 0, 300))
                    """

                    #variables.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T}',wzero+'*('+cut+')',  20, 35, 535))


                    ### OLD Variables
                    """
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201)',  20, 35, 635))


                    
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201)',  20, 0, 400))
                    

                    #variables_fit.append(variabile('MET_nominal','MET 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201)',  20, 0, 400))
                    #variables_fit.append(variabile('MET_nominal','MET 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200)',  20, 0, 400))
                    #variables_fit.append(variabile('MET_nominal','MET Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201)',  20, 0, 400))


                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201)',  20, 0, 1))
                    """
                    ### NEW Variables
                    """
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal==1)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal==1)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal==1)',  20, 35, 635))

                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal==1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal==1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal==1)',  20, 0, 400))

                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal==1)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal==1)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal==1)',  20, 0, 1))



                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal!=1)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal!=1)',  20, 35, 635))
                    variables_fit.append(variabile('TightEl_pt_nominal+TightMu_pt_nominal','TightLep p_{T} Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal!=1)',  20, 35, 635))

                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal!=1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal!=1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_M_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal!=1)',  20, 0, 400))

                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal!=1)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal!=1)',  20, 0, 1))
                    variables_fit.append(variabile('Jet_btag_nominal','Jet b-tag Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal!=1)',  20, 0, 1))

                    """

                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal==1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal==1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal==1)',  20, 0, 400))


                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M 1b+2q',wzero+'*('+cut+'&& FatJet_MC_nominal==201 && Top_MC_nominal!=1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M 2q',wzero+'*('+cut+'&& FatJet_MC_nominal==200 && Top_MC_nominal!=1)',  20, 0, 400))
                    variables_fit.append(variabile('FatJet_partM_nominal','FatJet M Oth',wzero+'*('+cut+'&& FatJet_MC_nominal!=200 && FatJet_MC_nominal!=201 && Top_MC_nominal!=1)',  20, 0, 400))

                    """
                    variables_fit.append(variabile('MET_nominal','Met Low Mass',wzero+'*('+cut+' && FatJet_M_nominal<=20)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met 1b',wzero+'*('+cut+' && FatJet_M_nominal>20 && FatJet_MC_nominal==1)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met 1b+1l',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==11)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met 1b+1q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==101)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met 1b+2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==201)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met 2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==200)',  30, 0, 300))
                    variables_fit.append(variabile('MET_nominal','Met Oth',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal!=200 && FatJet_MC_nominal!=1 && FatJet_MC_nominal!=11 && FatJet_MC_nominal!=101 && FatJet_MC_nominal!=201)',  30, 0, 300))


                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD Low Mass',wzero+'*('+cut+' && FatJet_M_nominal<=20)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD 1b',wzero+'*('+cut+' && FatJet_M_nominal>20 && FatJet_MC_nominal==1)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD 1b+1l',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==11)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD 1b+1q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==101)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD 1b+2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==201)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD 2q',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal==200)',  30, 0, 300))
                    variables_fit.append(variabile('FatJet_XbbVsQCD_nominal','FatJet XbbVsQCD Oth',wzero+'*('+cut+'&& FatJet_M_nominal>20 && FatJet_MC_nominal!=200 && FatJet_MC_nominal!=1 && FatJet_MC_nominal!=11 && FatJet_MC_nominal!=101 && FatJet_MC_nominal!=201)',  30, 0, 300))
                    


                    variables_fit.append(variabile('Top_TvsOth_nominal','Best Top ScoreVsOth True',wzero+'*('+cut+' && Top_MC_nominal==1)',  20, 0, 1))                                              
                    variables_fit.append(variabile('Top_TvsOth_nominal','Best Top ScoreVsOth 0prompt',wzero+'*('+cut+' && Top_MC_nominal==0)',  20, 0, 1))                                           
                    variables_fit.append(variabile('Top_TvsOth_nominal','Best Top ScoreVsOth 1prompt',wzero+'*('+cut+' && Top_MC_nominal>1)',  20, 0, 1))                                            
                    """


                    #variables_fit.append(variabile('Top_M_nominal','Best Top M True',wzero+'*('+cut+'&& Top_MC_nominal==1)',  25, 50, 300))
                    #variables_fit.append(variabile('MET_nominal','MET p_{T} True',wzero+'*('+cut+'&& Top_MC_nominal==1)',  20, 25, 625))

                    #variables_fit.append(variabile('Top_M_nominal','Best Top M 0prompt',wzero+'*('+cut+'&& Top_MC_nominal==0)',  25, 50, 300))
                    #variables_fit.append(variabile('MET_nominal','MET p_{T} 0prompt',wzero+'*('+cut+'&& Top_MC_nominal==0)',  20, 25, 625))

                    #variables_fit.append(variabile('Top_M_nominal','Best Top M 1prompt',wzero+'*('+cut+'&& Top_MC_nominal>1)',  25, 50, 300))
                    #variables_fit.append(variabile('MET_nominal','MET p_{T} 1prompt',wzero+'*('+cut+'&& Top_MC_nominal>1)',  20, 25, 625))

                    #for syst in systematics:
                    f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
                    for syst in systematics:
                         for var in variables_fit:
                              fitplot(lep, var,year, cut, syst,f1)
                    f1.Close()

          if(opt.stack):
               for var in variables:
                    os.system('set LD_PRELOAD=libtcmalloc.so')
                    for syst in [""]: makestack(lep, 'jets', var, dataset_new, cut_tag, syst, lumi[str(year)])
                    os.system('set LD_PRELOAD=libtcmalloc.so')

