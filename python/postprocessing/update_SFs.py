import os, commands
import sys
import optparse
import ROOT
import math
from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from PhysicsTools.NanoAODTools.postprocessing.skimtree_utils_final import *
from array import array
import json

usage = 'python update_SFs.py'
parser = optparse.OptionParser(usage)

parser.add_option('-y', '--year', dest='year', type='string', default = 'all', help='Default 2016, 2017 and 2018 are included')
parser.add_option('-d', '--dat', dest='dat', type='string', default = 'all', help="")
parser.add_option('-f', '--folder', dest='folder', type='string', default = 'v0', help='Default folder is v0')

(opt, args) = parser.parse_args()

folder = opt.folder
filerepo = '/eos/user/'+str(os.environ.get('USER')[0])+'/'+str(os.environ.get('USER'))+'/Tprime/nosynch/' + folder + '/'

def weight_writer(sample):
     if not ('Data' in sample.label):
          os.system("mv "+filerepo + sample.label + "/"  + sample.label + ".root "+filerepo + sample.label + "/"  + sample.label + "_backup.root ")
          infile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_backup.root")
          tree = infile.Get('events_nominal')
          treejesup = infile.Get('events_jesUp')
          treejesdown = infile.Get('events_jesDown')
          treejerup = infile.Get('events_jerUp')
          treejerdown = infile.Get('events_jerDown')

          tree.SetBranchStatus('BDTSF', 0)
          tree.SetBranchStatus('BDTUp', 0)
          tree.SetBranchStatus('BDTDown', 0)
          tree.SetBranchStatus('ParNetSF', 0)
          tree.SetBranchStatus('ParNetUp', 0)
          tree.SetBranchStatus('ParNetDown', 0)

          treejesup.SetBranchStatus('BDTSF', 0)
          treejesup.SetBranchStatus('BDTUp', 0)
          treejesup.SetBranchStatus('BDTDown', 0)
          treejesup.SetBranchStatus('ParNetSF', 0)
          treejesup.SetBranchStatus('ParNetUp', 0)
          treejesup.SetBranchStatus('ParNetDown', 0)

          treejesdown.SetBranchStatus('BDTSF', 0)
          treejesdown.SetBranchStatus('BDTUp', 0)
          treejesdown.SetBranchStatus('BDTDown', 0)
          treejesdown.SetBranchStatus('ParNetSF', 0)
          treejesdown.SetBranchStatus('ParNetUp', 0)
          treejesdown.SetBranchStatus('ParNetDown', 0)

          treejerup.SetBranchStatus('BDTSF', 0)
          treejerup.SetBranchStatus('BDTUp', 0)
          treejerup.SetBranchStatus('BDTDown', 0)
          treejerup.SetBranchStatus('ParNetSF', 0)
          treejerup.SetBranchStatus('ParNetUp', 0)
          treejerup.SetBranchStatus('ParNetDown', 0)

          treejerdown.SetBranchStatus('BDTSF', 0)
          treejerdown.SetBranchStatus('BDTUp', 0)
          treejerdown.SetBranchStatus('BDTDown', 0)
          treejerdown.SetBranchStatus('ParNetSF', 0)
          treejerdown.SetBranchStatus('ParNetUp', 0)
          treejerdown.SetBranchStatus('ParNetDown', 0)

          outfile = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root","RECREATE")
          tree_new = tree.CloneTree(0)
          treejesup_new = treejesup.CloneTree(0)
          treejesdown_new = treejesdown.CloneTree(0)
          treejerup_new = treejerup.CloneTree(0)
          treejerdown_new = treejerdown.CloneTree(0)
          
          wBDTSF = array('f', [0.])
          wBDTUp = array('f', [0.])
          wBDTDown = array('f', [0.])

          wParNetSF = array('f', [0.])
          wParNetUp = array('f', [0.])
          wParNetDown = array('f', [0.])
          
          tree_new.Branch('BDTSF', wBDTSF, 'BDTSF/F')
          tree_new.Branch('BDTUp', wBDTUp, 'BDTUp/F')
          tree_new.Branch('BDTDown', wBDTDown, 'BDTDown/F')

          tree_new.Branch('ParNetSF', wParNetSF, 'ParNetSF/F')
          tree_new.Branch('ParNetUp', wParNetUp, 'ParNetUp/F')
          tree_new.Branch('ParNetDown', wParNetDown, 'ParNetDown/F')


          treejesup_new.Branch('BDTSF', wBDTSF, 'BDTSF/F')
          treejesup_new.Branch('BDTUp', wBDTUp, 'BDTUp/F')
          treejesup_new.Branch('BDTDown', wBDTDown, 'BDTDown/F')

          treejesup_new.Branch('ParNetSF', wParNetSF, 'ParNetSF/F')
          treejesup_new.Branch('ParNetUp', wParNetUp, 'ParNetUp/F')
          treejesup_new.Branch('ParNetDown', wParNetDown, 'ParNetDown/F')

          
          treejesdown_new.Branch('BDTSF', wBDTSF, 'BDTSF/F')
          treejesdown_new.Branch('BDTUp', wBDTUp, 'BDTUp/F')
          treejesdown_new.Branch('BDTDown', wBDTDown, 'BDTDown/F')

          treejesdown_new.Branch('ParNetSF', wParNetSF, 'ParNetSF/F')
          treejesdown_new.Branch('ParNetUp', wParNetUp, 'ParNetUp/F')
          treejesdown_new.Branch('ParNetDown', wParNetDown, 'ParNetDown/F')


          treejerup_new.Branch('BDTSF', wBDTSF, 'BDTSF/F')
          treejerup_new.Branch('BDTUp', wBDTUp, 'BDTUp/F')
          treejerup_new.Branch('BDTDown', wBDTDown, 'BDTDown/F')

          treejerup_new.Branch('ParNetSF', wParNetSF, 'ParNetSF/F')
          treejerup_new.Branch('ParNetUp', wParNetUp, 'ParNetUp/F')
          treejerup_new.Branch('ParNetDown', wParNetDown, 'ParNetDown/F')


          treejerdown_new.Branch('BDTSF', wBDTSF, 'BDTSF/F')
          treejerdown_new.Branch('BDTUp', wBDTUp, 'BDTUp/F')
          treejerdown_new.Branch('BDTDown', wBDTDown, 'BDTDown/F')

          treejerdown_new.Branch('ParNetSF', wParNetSF, 'ParNetSF/F')
          treejerdown_new.Branch('ParNetUp', wParNetUp, 'ParNetUp/F')
          treejesdown_new.Branch('ParNetDown', wParNetDown, 'ParNetDown/F')



          for event in xrange(0, tree.GetEntries()):
               tree.GetEntry(event)
               if event%10000==1:
                    sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/tree.GetEntries()))
               wBDTSF[0], wBDTUp[0], wBDTDown[0]= getNewBDT_SF(sample.label, tree.top_region_nominal, tree.Top_flavour_nominal, tree.Top_MC_nominal)
               wParNetSF[0], wParNetUp[0], wParNetDown[0]= getNewPN_SF(sample.label, tree.AK8_region_nominal, tree.FatJet_MC_nominal)
               tree_new.Fill()
          outfile.cd()
          tree_new.Write()
          infile.cd()


          for event in xrange(0, treejesup.GetEntries()):
               treejesup.GetEntry(event)
               if event%10000==1:
                    sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejesup.GetEntries()))
               wBDTSF[0], wBDTUp[0], wBDTDown[0]= getNewBDT_SF(sample.label, treejesup.top_region_nominal, treejesup.Top_flavour_nominal, treejesup.Top_MC_nominal)
               wParNetSF[0], wParNetUp[0], wParNetDown[0]= getNewPN_SF(sample.label, treejesup.AK8_region_nominal, treejesup.FatJet_MC_nominal)
               treejesup_new.Fill()
          outfile.cd()
          treejesup_new.Write()
          infile.cd()


          for event in xrange(0, treejesdown.GetEntries()):
               treejesdown.GetEntry(event)
               if event%10000==1:
                    sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejesdown.GetEntries()))
               wBDTSF[0], wBDTUp[0], wBDTDown[0]= getNewBDT_SF(sample.label, treejesdown.top_region_nominal, treejesdown.Top_flavour_nominal, treejesdown.Top_MC_nominal)
               wParNetSF[0], wParNetUp[0], wParNetDown[0]= getNewPN_SF(sample.label, treejesdown.AK8_region_nominal, treejesdown.FatJet_MC_nominal)
               treejesdown_new.Fill()
          outfile.cd()
          treejesdown_new.Write()
          infile.cd()


          for event in xrange(0, treejerup.GetEntries()):
               treejerup.GetEntry(event)
               if event%10000==1:
                    sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejerup.GetEntries()))
               wBDTSF[0], wBDTUp[0], wBDTDown[0]= getNewBDT_SF(sample.label, treejerup.top_region_nominal, treejerup.Top_flavour_nominal, treejerup.Top_MC_nominal)
               wParNetSF[0], wParNetUp[0], wParNetDown[0]= getNewPN_SF(sample.label, treejerup.AK8_region_nominal, treejerup.FatJet_MC_nominal)
               treejerup_new.Fill()
          outfile.cd()
          treejerup_new.Write()
          infile.cd()


          for event in xrange(0, treejerdown.GetEntries()):
               treejerdown.GetEntry(event)
               if event%10000==1:
                    sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/treejerdown.GetEntries()))
               wBDTSF[0], wBDTUp[0], wBDTDown[0]= getNewBDT_SF(sample.label, treejerdown.top_region_nominal, treejerdown.Top_flavour_nominal, treejerdown.Top_MC_nominal)
               wParNetSF[0], wParNetUp[0], wParNetDown[0]= getNewPN_SF(sample.label, treejerdown.AK8_region_nominal, treejerdown.FatJet_MC_nominal)
               treejerdown_new.Fill()
          outfile.cd()
          treejerdown_new.Write()
          infile.Close()
          outfile.Close()
          print('\n')
          



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
          '2018': [ST_2018,QCD_2018,WJets_2018,TT_Mtt_2018,DataHT_2018,DataMu_2018,DataEle_2018,Tprime_tHq_1800LH_2018],#[ST_2018,WJets_2018, QCD_2018,TT_Mtt_2018,DataHT_2018,DataMu_2018,DataEle_2018,Tprime_tHq_1800LH_2018,Tprime_tHq_600LH_2018,Tprime_tHq_1200LH_2018],#TTVJets_2018,TTGammaJets_2018,TTH_2018,TGJets_2018],#Tprime_tHq_600LH_2018,Tprime_tHq_700LH_2018,Tprime_tHq_800LH_2018,Tprime_tHq_900LH_2018,Tprime_tHq_1000LH_2018,Tprime_tHq_1100LH_2018,Tprime_tHq_1200LH_2018,Tprime_tHq_1300LH_2018,Tprime_tHq_1400LH_2018,Tprime_tHq_1600LH_2018,Tprime_tHq_1700LH_2018,Tprime_tHq_1800LH_2018,DataMu_2018,Tprime_tHq_1500LH_2018, DataEle_2018, DataHT_2018, TT_Mtt_2018],
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
               weight_writer(sample)
