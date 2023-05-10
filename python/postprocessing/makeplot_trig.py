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
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'all', help='Default all systematics added')
parser.add_option('-y', '--year', dest='year', type='string', default = 'all', help='Default 2016, 2017 and 2018 are included')
parser.add_option('-f', '--folder', dest='folder', type='string', default = 'v0', help='Default folder is v0')
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
          print "Number of entries of the file %s are %s" %(filerepo + sample.label + "/"  + sample.label + "_merged.root", (check.Get("events_all")).GetEntries())
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

def lumi_writer(dataset, lumi):
     samples = []
     if hasattr(dataset, 'components'): # How to check whether this exists or not
          samples = [sample for sample in dataset.components]# Method exists and was used.
     else:
          samples.append(dataset)
     for sample in samples:
          if not ('Data' in sample.label): # or 'TT_dilep' in sample.label):
               infile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root")
               tree = infile.Get('events_all')
               tree.SetBranchStatus('w_nominal', 1)
               outfile = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root","RECREATE")
               tree_new = tree.CloneTree(0)
               print("Getting the histos from %s" %(infile))
               h_genw_tmp = ROOT.TH1F(infile.Get("h_genweight"))
               w_nom = array('f', [0.]) 
               tree_new.Branch('w_nominal', w_nom, 'w_nominal/F')
               for event in xrange(0, tree.GetEntries()):
                    tree.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/tree.GetEntries()))
                    w_nom[0] = tree.w_nominal * sample.sigma * lumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    tree_new.Fill()
               outfile.cd()
               tree_new.Write()
               outfile.Close()
               print('\n')
          else:
               os.popen("mv " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + ".root")



dataset_dict = {'2016preVFP':[],'2016postVFP':[],'2017':[],'2018':[],'2018_nodata':[]} #Cambio 2016
lumi = {'2016preVFP':19.5,'2016postVFP':16.8, "2017": 41.48, "2018": 59.83,"2018_nodata":59.83}#Cambio 2016

if(opt.dat!= 'all'):
     if not(opt.dat in sample_dict.keys()):
          print sample_dict.keys()
     dataset_names = map(str, opt.dat.strip('[]').split(','))
     #print dataset_names.keys()
     samples = []
     [samples.append(sample_dict[dataset_name]) for dataset_name in dataset_names]
     print("Error in sample spificy which one, problem with 2016")
     [dataset_dict[str(sample.year)].append(sample) for sample in samples]
else:
     dataset_dict = {
          '2016preVFP':[ST_2016preVFP,WJets_2016preVFP, QCD_2016preVFP, TT_Mtt_2016preVFP,DataMu_2016preVFP,DataEle_2016preVFP,DataPh_2016preVFP,DataHT_2016preVFP],
          '2016postVFP':[ST_2016postVFP,WJets_2016postVFP, QCD_2016postVFP, TT_Mtt_2016postVFP,DataMu_2016postVFP,DataEle_2016postVFP,DataPh_2016postVFP,DataHT_2016postVFP],
          #'2016':[ST_2016,WJets_2016, QCD_2016, TT_Mtt_2016, Tprime_tHq_600LH_2016,Tprime_tHq_700LH_2016,Tprime_tHq_800LH_2016,Tprime_tHq_900LH_2016,Tprime_tHq_1000LH_2016,Tprime_tHq_1100LH_2016,Tprime_tHq_1200LH_2016,Tprime_tHq_1300LH_2016,Tprime_tHq_1400LH_2016,Tprime_tHq_1600LH_2016,Tprime_tHq_1700LH_2016,Tprime_tHq_1800LH_2016],
          '2017':[ST_2017,WJets_2017, QCD_2017, TT_Mtt_2017,DataMu_2017,DataEle_2017,DataPh_2017,DataHT_2017],
          '2018': [ST_2018,WJets_2018, QCD_2018, DataMu_2018, DataEle_2018, DataHT_2018, TT_Mtt_2018],
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



for year in years:
     for sample in dataset_dict[year]:
          if(opt.merpart):
               mergepart(sample)
          if(opt.lumi):
               lumi_writer(sample, lumi[year])
          if(opt.mertree):
               if not('Tprime' in sample.label):
                    mergetree(sample)
