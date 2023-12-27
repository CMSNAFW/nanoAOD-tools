import ROOT
import os
#import json_reader as jr                                                                                                                                                                                                                                                                                         

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label

tag_data = '106X_dataRun2_v37'
tag_2016preVFP = 'RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11'
tag_2016postVFP = 'RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17'
tag_2017 = 'RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9'
tag_2018 = 'RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1'

tag_2016="NoTag"
###################################################################################################################################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
############################################################                    2016preVFP             ############################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
###################################################################################################################################################################                                                                                                                                               

################################ TTbar ################################                                                                                                                                                                                                                                        
kFactorsQCD={
    "WJetsHT100to200" : 1.26,
    "WJetsHT200to400" : 1.48,
    "WJetsHT400to600" : 1.26,
    "WJetsHT600to800" : 1.03,
    "WJetsHT800to1200" : 1.05,
    "WJetsHT1200to2500" : 0.77,
    "WJetsHT2500toInf" : 0.77
}
      


TT_Mtt700to1000_2016preVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2016preVFP")
TT_Mtt700to1000_2016preVFP.sigma = 80.5 #pb                                                                                                                                                                     
TT_Mtt700to1000_2016preVFP.year = 2016
TT_Mtt700to1000_2016preVFP.dataset ="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"                                              

TT_Mtt1000toInf_2016preVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2016preVFP")
TT_Mtt1000toInf_2016preVFP.sigma = 21.3 #pb                          
TT_Mtt1000toInf_2016preVFP.year = 2016
TT_Mtt1000toInf_2016preVFP.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

TT_semilep_2016preVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2016preVFP")
TT_semilep_2016preVFP.sigma = 831.76*0.438 #pb
TT_semilep_2016preVFP.year = 2016
TT_semilep_2016preVFP.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

TT_dilep_2016preVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2016preVFP")
TT_dilep_2016preVFP.sigma =  831.76 * 0.10 #pb                                                                                                                                                                    
TT_dilep_2016preVFP.year = 2016
TT_dilep_2016preVFP.dataset ="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

TT_Mtt_2016preVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2016preVFP")
TT_Mtt_2016preVFP.year = 2016
TT_Mtt_2016preVFP.components = [TT_dilep_2016preVFP,TT_semilep_2016preVFP,TT_Mtt700to1000_2016preVFP, TT_Mtt1000toInf_2016preVFP]

TT_Mtt = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt")

#WJets


WJetsHT70to100_2016preVFP = sample(ROOT.kGreen, 1, 1001, "W + Jets", "WJetsHT70to100_2016preVFP")
WJetsHT70to100_2016preVFP.sigma = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2016preVFP.year = 2016
WJetsHT70to100_2016preVFP.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

WJetsHT100to200_2016preVFP = sample(ROOT.kGreen+1, 1, 1001, "W + Jets", "WJetsHT100to200_2016preVFP")
WJetsHT100to200_2016preVFP.sigma = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2016preVFP.year = 2016
WJetsHT100to200_2016preVFP.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

WJetsHT200to400_2016preVFP = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2016preVFP")
WJetsHT200to400_2016preVFP.sigma = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2016preVFP.year = 2016
WJetsHT200to400_2016preVFP.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"
#WJetsHT200to400_2016preVFP.files = jr.json_reader(path+"/WJets_HT200To400_2016preVFP.json")

WJetsHT400to600_2016preVFP = sample(ROOT.kGreen+3, 1, 1001, "W + Jets", "WJetsHT400to600_2016preVFP")
WJetsHT400to600_2016preVFP.sigma = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2016preVFP.year = 2016
WJetsHT400to600_2016preVFP.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"
#WJetsHT400to600_2016preVFP.files = jr.json_reader(path+"/WJets_HT400To600_2016preVFP.json")

WJetsHT600to800_2016preVFP = sample(ROOT.kGreen+4, 1, 1001, "W + Jets", "WJetsHT600to800_2016preVFP")
WJetsHT600to800_2016preVFP.sigma = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2016preVFP.year = 2016
WJetsHT600to800_2016preVFP.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"
#WJetsHT600to800_2016preVFP.files = jr.json_reader(path+"/WJets_HT600To800_2016preVFP.json")

WJetsHT800to1200_2016preVFP = sample(ROOT.kGreen+5, 1, 1001, "W + Jets", "WJetsHT800to1200_2016preVFP")
WJetsHT800to1200_2016preVFP.sigma = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2016preVFP.year = 2016
WJetsHT800to1200_2016preVFP.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"
#WJetsHT800to1200_2016preVFP.files = jr.json_reader(path+"/WJets_HT800To1200_2016preVFP.json")

WJetsHT1200to2500_2016preVFP = sample(ROOT.kGreen+6, 1, 1001, "W + Jets", "WJetsHT1200to2500_2016preVFP")
WJetsHT1200to2500_2016preVFP.sigma = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2016preVFP.year = 2016
WJetsHT1200to2500_2016preVFP.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"


WJetsHT2500toInf_2016preVFP = sample(ROOT.kGreen+7, 1, 1001, "W + Jets", "WJetsHT2500toInf_2016preVFP")
WJetsHT2500toInf_2016preVFP.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2016preVFP.year = 2016
WJetsHT2500toInf_2016preVFP.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v2/NANOAODSIM"



WJets_2016preVFP = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2016preVFP")
WJets_2016preVFP.year = 2016
WJets_2016preVFP.components = [WJetsHT70to100_2016preVFP, WJetsHT100to200_2016preVFP, WJetsHT200to400_2016preVFP, WJetsHT400to600_2016preVFP, WJetsHT600to800_2016preVFP, WJetsHT800to1200_2016preVFP, WJetsHT1200to2500_2016preVFP, WJetsHT2500toInf_2016preVFP]

WJets = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets")

#QCD

QCDHT_50to100_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_50to100_2016preVFP")
QCDHT_50to100_2016preVFP.sigma = 0 #347700 #pb
QCDHT_50to100_2016preVFP.year = 2016
QCDHT_50to100_2016preVFP.dataset = "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_100to200_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2016preVFP")
QCDHT_100to200_2016preVFP.sigma = 27990000#0 #347700 #pb
QCDHT_100to200_2016preVFP.year = 2016
QCDHT_100to200_2016preVFP.dataset = "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_200to300_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2016preVFP")
QCDHT_200to300_2016preVFP.sigma = 1712000 #347700 #pb
QCDHT_200to300_2016preVFP.year = 2016
QCDHT_200to300_2016preVFP.dataset = "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v2/NANOAODSIM"

QCDHT_300to500_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2016preVFP")
QCDHT_300to500_2016preVFP.sigma = 347700 #pb
QCDHT_300to500_2016preVFP.year = 2016
QCDHT_300to500_2016preVFP.dataset = "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v2/NANOAODSIM"

QCDHT_500to700_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2016preVFP")
QCDHT_500to700_2016preVFP.sigma = 32100 #pb
QCDHT_500to700_2016preVFP.year = 2016
QCDHT_500to700_2016preVFP.dataset = "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_700to1000_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2016preVFP")
QCDHT_700to1000_2016preVFP.sigma = 6831 #pb
QCDHT_700to1000_2016preVFP.year = 2016
QCDHT_700to1000_2016preVFP.dataset = "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_1000to1500_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2016preVFP")
QCDHT_1000to1500_2016preVFP.sigma = 1207 #pb
QCDHT_1000to1500_2016preVFP.year = 2016
QCDHT_1000to1500_2016preVFP.dataset = "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_1500to2000_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2016preVFP")
QCDHT_1500to2000_2016preVFP.sigma = 119.9 #pb
QCDHT_1500to2000_2016preVFP.year = 2016
QCDHT_1500to2000_2016preVFP.dataset = "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCDHT_2000toInf_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2016preVFP")
QCDHT_2000toInf_2016preVFP.sigma = 25.24 #pb
QCDHT_2000toInf_2016preVFP.year = 2016
QCDHT_2000toInf_2016preVFP.dataset = "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

QCD_2016preVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2016preVFP")
QCD_2016preVFP.year = 2016
QCD_2016preVFP.components = [QCDHT_100to200_2016preVFP,QCDHT_200to300_2016preVFP,QCDHT_300to500_2016preVFP, QCDHT_500to700_2016preVFP, QCDHT_700to1000_2016preVFP, QCDHT_1000to1500_2016preVFP, QCDHT_1500to2000_2016preVFP, QCDHT_2000toInf_2016preVFP]

QCD = sample(ROOT.kGray, 1, 1001, "QCD", "QCD")

#ST
ST_tch_t_2016preVFP = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_t_2016preVFP")
ST_tch_t_2016preVFP.sigma =  136.02 #pb
ST_tch_t_2016preVFP.year = 2016
ST_tch_t_2016preVFP.dataset = "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

ST_tch_tbar_2016preVFP = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_tbar_2016preVFP")
ST_tch_tbar_2016preVFP.sigma =  80.95 #pb
ST_tch_tbar_2016preVFP.year = 2016
ST_tch_tbar_2016preVFP.dataset = "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

ST_tW_t_2016preVFP = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_t_2016preVFP")
ST_tW_t_2016preVFP.sigma =  71.7/2 #pb
ST_tW_t_2016preVFP.year = 2016
ST_tW_t_2016preVFP.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

ST_tW_tbar_2016preVFP = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_tbar_2016preVFP")
ST_tW_tbar_2016preVFP.sigma = 71.7/2 #pb
ST_tW_tbar_2016preVFP.year = 2016
ST_tW_tbar_2016preVFP.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

ST_sch_2016preVFP = sample(ROOT.kYellow, 1, 1001, "ST s-ch", "ST_sch_2016preVFP")
ST_sch_2016preVFP.sigma = 10.32*0.324 #pb
ST_sch_2016preVFP.year = 2016
ST_sch_2016preVFP.dataset = "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

ST_2016preVFP = sample(ROOT.kYellow, 1, 1001, "Single top", "ST_2016preVFP")
ST_2016preVFP.year = 2016
ST_2016preVFP.components = [ST_tch_t_2016preVFP, ST_tch_tbar_2016preVFP, ST_tW_t_2016preVFP, ST_tW_tbar_2016preVFP, ST_sch_2016preVFP]

ST = sample(ROOT.kYellow, 1, 1001, "Single top", "ST")

#signal

Tprime_tHq_600LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2016preVFP")
Tprime_tHq_600LH_2016preVFP.sigma = 0.07453
Tprime_tHq_600LH_2016preVFP.year = 2016
Tprime_tHq_600LH_2016preVFP.dataset="/TprimeBToTH_M-600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_700LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2016preVFP")
Tprime_tHq_700LH_2016preVFP.sigma = 88.107/1000. #to be changed
Tprime_tHq_700LH_2016preVFP.year = 2016
Tprime_tHq_700LH_2016preVFP.dataset="/TprimeBToTH_M-700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_800LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2016preVFP")
Tprime_tHq_800LH_2016preVFP.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2016preVFP.year = 2016
Tprime_tHq_800LH_2016preVFP.dataset="/TprimeBToTH_M-800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_900LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2016preVFP")
Tprime_tHq_900LH_2016preVFP.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2016preVFP.year = 2016
Tprime_tHq_900LH_2016preVFP.dataset="/TprimeBToTH_M-900_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1000LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2016preVFP")
Tprime_tHq_1000LH_2016preVFP.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2016preVFP.year = 2016
Tprime_tHq_1000LH_2016preVFP.dataset="/TprimeBToTH_M-1000_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1100LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2016preVFP")
Tprime_tHq_1100LH_2016preVFP.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2016preVFP.year = 2016
Tprime_tHq_1100LH_2016preVFP.dataset="/TprimeBToTH_M-1100_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1200LH_2016preVFP = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2016preVFP")
Tprime_tHq_1200LH_2016preVFP.sigma = 0.01973
Tprime_tHq_1200LH_2016preVFP.year = 2016
Tprime_tHq_1200LH_2016preVFP.dataset="/TprimeBToTH_M-1200_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1300LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2016preVFP")
Tprime_tHq_1300LH_2016preVFP.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2016preVFP.year = 2016
Tprime_tHq_1300LH_2016preVFP.dataset="/TprimeBToTH_M-1300_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1400LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2016preVFP")
Tprime_tHq_1400LH_2016preVFP.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2016preVFP.year = 2016
Tprime_tHq_1400LH_2016preVFP.dataset="/TprimeBToTH_M-1400_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1500LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2016preVFP")
Tprime_tHq_1500LH_2016preVFP.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2016preVFP.year = 2016
Tprime_tHq_1500LH_2016preVFP.dataset="/TprimeBToTH_M-1500_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1600LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2016preVFP")
Tprime_tHq_1600LH_2016preVFP.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2016preVFP.year = 2016
Tprime_tHq_1600LH_2016preVFP.dataset="/TprimeBToTH_M-1600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1700LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2016preVFP")
Tprime_tHq_1700LH_2016preVFP.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2016preVFP.year = 2016
Tprime_tHq_1700LH_2016preVFP.dataset="/TprimeBToTH_M-1700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tHq_1800LH_2016preVFP = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2016preVFP")
Tprime_tHq_1800LH_2016preVFP.sigma = 0.005829
Tprime_tHq_1800LH_2016preVFP.year = 2016
Tprime_tHq_1800LH_2016preVFP.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2016preVFP")
Tprime_LH_2016preVFP.year = 2016
Tprime_LH_2016preVFP.components = [Tprime_tHq_600LH_2016preVFP,Tprime_tHq_700LH_2016preVFP,Tprime_tHq_800LH_2016preVFP,Tprime_tHq_900LH_2016preVFP,Tprime_tHq_1000LH_2016preVFP,Tprime_tHq_1100LH_2016preVFP,Tprime_tHq_1200LH_2016preVFP,Tprime_tHq_1300LH_2016preVFP,Tprime_tHq_1400LH_2016preVFP,Tprime_tHq_1500LH_2016preVFP,Tprime_tHq_1600LH_2016preVFP,Tprime_tHq_1700LH_2016preVFP,Tprime_tHq_1800LH_2016preVFP]


Tprime_tHq_1800LH = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH")

###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2016postVFP             ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################

################################ TTbar ################################



TT_Mtt700to1000_2016postVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2016postVFP")
TT_Mtt700to1000_2016postVFP.sigma = 80.5 #pb
TT_Mtt700to1000_2016postVFP.year = 2016
TT_Mtt700to1000_2016postVFP.dataset ="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

TT_Mtt1000toInf_2016postVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2016postVFP")
TT_Mtt1000toInf_2016postVFP.sigma = 21.3 #pb
TT_Mtt1000toInf_2016postVFP.year = 2016
TT_Mtt1000toInf_2016postVFP.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

TT_semilep_2016postVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2016postVFP")
TT_semilep_2016postVFP.sigma = 831.76*0.438 #pb
TT_semilep_2016postVFP.year = 2016
TT_semilep_2016postVFP.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

TT_dilep_2016postVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2016postVFP")
TT_dilep_2016postVFP.sigma =  831.76 * 0.10 #pb
TT_dilep_2016postVFP.year = 2016
TT_dilep_2016postVFP.dataset ="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

TT_Mtt_2016postVFP = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2016postVFP")
TT_Mtt_2016postVFP.year = 2016
TT_Mtt_2016postVFP.components = [TT_dilep_2016postVFP,TT_semilep_2016postVFP,TT_Mtt700to1000_2016postVFP, TT_Mtt1000toInf_2016postVFP]


#WJets


WJetsHT70to100_2016postVFP = sample(ROOT.kGreen, 1, 1001, "W + Jets", "WJetsHT70to100_2016postVFP")
WJetsHT70to100_2016postVFP.sigma = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2016postVFP.year = 2016
WJetsHT70to100_2016postVFP.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

WJetsHT100to200_2016postVFP = sample(ROOT.kGreen+1, 1, 1001, "W + Jets", "WJetsHT100to200_2016postVFP")
WJetsHT100to200_2016postVFP.sigma = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2016postVFP.year = 2016
WJetsHT100to200_2016postVFP.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

WJetsHT200to400_2016postVFP = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2016postVFP")
WJetsHT200to400_2016postVFP.sigma = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2016postVFP.year = 2016
WJetsHT200to400_2016postVFP.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"
#WJetsHT200to400_2016postVFP.files = jr.json_reader(path+"/WJets_HT200To400_2016postVFP.json")

WJetsHT400to600_2016postVFP = sample(ROOT.kGreen+3, 1, 1001, "W + Jets", "WJetsHT400to600_2016postVFP")
WJetsHT400to600_2016postVFP.sigma = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2016postVFP.year = 2016
WJetsHT400to600_2016postVFP.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"
#WJetsHT400to600_2016postVFP.files = jr.json_reader(path+"/WJets_HT400To600_2016postVFP.json")

WJetsHT600to800_2016postVFP = sample(ROOT.kGreen+4, 1, 1001, "W + Jets", "WJetsHT600to800_2016postVFP")
WJetsHT600to800_2016postVFP.sigma = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2016postVFP.year = 2016
WJetsHT600to800_2016postVFP.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"
#WJetsHT600to800_2016postVFP.files = jr.json_reader(path+"/WJets_HT600To800_2016postVFP.json")

WJetsHT800to1200_2016postVFP = sample(ROOT.kGreen+5, 1, 1001, "W + Jets", "WJetsHT800to1200_2016postVFP")
WJetsHT800to1200_2016postVFP.sigma = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2016postVFP.year = 2016
WJetsHT800to1200_2016postVFP.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"
#WJetsHT800to1200_2016postVFP.files = jr.json_reader(path+"/WJets_HT800To1200_2016postVFP.json")

WJetsHT1200to2500_2016postVFP = sample(ROOT.kGreen+6, 1, 1001, "W + Jets", "WJetsHT1200to2500_2016postVFP")
WJetsHT1200to2500_2016postVFP.sigma = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2016postVFP.year = 2016
WJetsHT1200to2500_2016postVFP.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"


WJetsHT2500toInf_2016postVFP = sample(ROOT.kGreen+7, 1, 1001, "W + Jets", "WJetsHT2500toInf_2016postVFP")
WJetsHT2500toInf_2016postVFP.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2016postVFP.year = 2016
WJetsHT2500toInf_2016postVFP.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v2/NANOAODSIM"



WJets_2016postVFP = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2016postVFP")
WJets_2016postVFP.year = 2016
WJets_2016postVFP.components = [WJetsHT70to100_2016postVFP, WJetsHT100to200_2016postVFP, WJetsHT200to400_2016postVFP, WJetsHT400to600_2016postVFP, WJetsHT600to800_2016postVFP, WJetsHT800to1200_2016postVFP, WJetsHT1200to2500_2016postVFP, WJetsHT2500toInf_2016postVFP]

#QCD

QCDHT_50to100_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_50to100_2016postVFP")
QCDHT_50to100_2016postVFP.sigma = 0 #347700 #pb
QCDHT_50to100_2016postVFP.year = 2016
QCDHT_50to100_2016postVFP.dataset = "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_100to200_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2016postVFP")
QCDHT_100to200_2016postVFP.sigma = 27990000#0 #347700 #pb
QCDHT_100to200_2016postVFP.year = 2016
QCDHT_100to200_2016postVFP.dataset = "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_200to300_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2016postVFP")
QCDHT_200to300_2016postVFP.sigma = 1712000 #347700 #pb
QCDHT_200to300_2016postVFP.year = 2016
QCDHT_200to300_2016postVFP.dataset = "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_300to500_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2016postVFP")
QCDHT_300to500_2016postVFP.sigma = 347700 #pb
QCDHT_300to500_2016postVFP.year = 2016
QCDHT_300to500_2016postVFP.dataset = "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_500to700_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2016postVFP")
QCDHT_500to700_2016postVFP.sigma = 32100 #pb
QCDHT_500to700_2016postVFP.year = 2016
QCDHT_500to700_2016postVFP.dataset = "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_700to1000_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2016postVFP")
QCDHT_700to1000_2016postVFP.sigma = 6831 #pb
QCDHT_700to1000_2016postVFP.year = 2016
QCDHT_700to1000_2016postVFP.dataset = "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_1000to1500_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2016postVFP")
QCDHT_1000to1500_2016postVFP.sigma = 1207 #pb
QCDHT_1000to1500_2016postVFP.year = 2016
QCDHT_1000to1500_2016postVFP.dataset = "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_1500to2000_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2016postVFP")
QCDHT_1500to2000_2016postVFP.sigma = 119.9 #pb
QCDHT_1500to2000_2016postVFP.year = 2016
QCDHT_1500to2000_2016postVFP.dataset = "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCDHT_2000toInf_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2016postVFP")
QCDHT_2000toInf_2016postVFP.sigma = 25.24 #pb
QCDHT_2000toInf_2016postVFP.year = 2016
QCDHT_2000toInf_2016postVFP.dataset = "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

QCD_2016postVFP = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2016postVFP")
QCD_2016postVFP.year = 2016
QCD_2016postVFP.components = [QCDHT_100to200_2016postVFP,QCDHT_200to300_2016postVFP,QCDHT_300to500_2016postVFP, QCDHT_500to700_2016postVFP, QCDHT_700to1000_2016postVFP, QCDHT_1000to1500_2016postVFP, QCDHT_1500to2000_2016postVFP, QCDHT_2000toInf_2016postVFP]

#ST
ST_tch_t_2016postVFP = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_t_2016postVFP")
ST_tch_t_2016postVFP.sigma =  136.02 #pb
ST_tch_t_2016postVFP.year = 2016
ST_tch_t_2016postVFP.dataset = "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

ST_tch_tbar_2016postVFP = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_tbar_2016postVFP")
ST_tch_tbar_2016postVFP.sigma =  80.95 #pb
ST_tch_tbar_2016postVFP.year = 2016
ST_tch_tbar_2016postVFP.dataset = "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

ST_tW_t_2016postVFP = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_t_2016postVFP")
ST_tW_t_2016postVFP.sigma =  71.7/2 #pb
ST_tW_t_2016postVFP.year = 2016
ST_tW_t_2016postVFP.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v2/NANOAODSIM"

ST_tW_tbar_2016postVFP = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_tbar_2016postVFP")
ST_tW_tbar_2016postVFP.sigma = 71.7/2 #pb
ST_tW_tbar_2016postVFP.year = 2016
ST_tW_tbar_2016postVFP.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2016postVFP+"-v2/NANOAODSIM"

ST_sch_2016postVFP = sample(ROOT.kYellow, 1, 1001, "ST s-ch", "ST_sch_2016postVFP")
ST_sch_2016postVFP.sigma = 10.32*0.324 #pb
ST_sch_2016postVFP.year = 2016
ST_sch_2016postVFP.dataset = "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

ST_2016postVFP = sample(ROOT.kYellow, 1, 1001, "Single top", "ST_2016postVFP")
ST_2016postVFP.year = 2016
ST_2016postVFP.components = [ST_tch_t_2016postVFP, ST_tch_tbar_2016postVFP, ST_tW_t_2016postVFP, ST_tW_tbar_2016postVFP, ST_sch_2016postVFP]

#signal

Tprime_tHq_600LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2016postVFP")
Tprime_tHq_600LH_2016postVFP.sigma = 0.07453
Tprime_tHq_600LH_2016postVFP.year = 2016
Tprime_tHq_600LH_2016postVFP.dataset="/TprimeBToTH_M-600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_700LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2016postVFP")
Tprime_tHq_700LH_2016postVFP.sigma = 45.920/1000. #to be changed
Tprime_tHq_700LH_2016postVFP.year = 2016
Tprime_tHq_700LH_2016postVFP.dataset="/TprimeBToTH_M-700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_800LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2016postVFP")
Tprime_tHq_800LH_2016postVFP.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2016postVFP.year = 2016
Tprime_tHq_800LH_2016postVFP.dataset="/TprimeBToTH_M-800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_900LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2016postVFP")
Tprime_tHq_900LH_2016postVFP.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2016postVFP.year = 2016
Tprime_tHq_900LH_2016postVFP.dataset="/TprimeBToTH_M-900_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1000LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2016postVFP")
Tprime_tHq_1000LH_2016postVFP.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2016postVFP.year = 2016
Tprime_tHq_1000LH_2016postVFP.dataset="/TprimeBToTH_M-1000_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1100LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2016postVFP")
Tprime_tHq_1100LH_2016postVFP.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2016postVFP.year = 2016
Tprime_tHq_1100LH_2016postVFP.dataset="/TprimeBToTH_M-1100_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1200LH_2016postVFP = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2016postVFP")
Tprime_tHq_1200LH_2016postVFP.sigma = 0.01973
Tprime_tHq_1200LH_2016postVFP.year = 2016
Tprime_tHq_1200LH_2016postVFP.dataset="/TprimeBToTH_M-1200_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1300LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2016postVFP")
Tprime_tHq_1300LH_2016postVFP.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2016postVFP.year = 2016
Tprime_tHq_1300LH_2016postVFP.dataset="/TprimeBToTH_M-1300_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1400LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2016postVFP")
Tprime_tHq_1400LH_2016postVFP.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2016postVFP.year = 2016
Tprime_tHq_1400LH_2016postVFP.dataset="/TprimeBToTH_M-1400_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1500LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2016postVFP")
Tprime_tHq_1500LH_2016postVFP.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2016postVFP.year = 2016
Tprime_tHq_1500LH_2016postVFP.dataset="/TprimeBToTH_M-1500_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1600LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2016postVFP")
Tprime_tHq_1600LH_2016postVFP.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2016postVFP.year = 2016
Tprime_tHq_1600LH_2016postVFP.dataset="/TprimeBToTH_M-1600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1700LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2016postVFP")
Tprime_tHq_1700LH_2016postVFP.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2016postVFP.year = 2016
Tprime_tHq_1700LH_2016postVFP.dataset="/TprimeBToTH_M-1700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_1800LH_2016postVFP = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2016postVFP")
Tprime_tHq_1800LH_2016postVFP.sigma = 0.005829
Tprime_tHq_1800LH_2016postVFP.year = 2016
Tprime_tHq_1800LH_2016postVFP.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2016postVFP")
Tprime_LH_2016postVFP.year = 2016
Tprime_LH_2016postVFP.components = [Tprime_tHq_600LH_2016postVFP,Tprime_tHq_700LH_2016postVFP,Tprime_tHq_800LH_2016postVFP,Tprime_tHq_900LH_2016postVFP,Tprime_tHq_1000LH_2016postVFP,Tprime_tHq_1100LH_2016postVFP,Tprime_tHq_1200LH_2016postVFP,Tprime_tHq_1300LH_2016postVFP,Tprime_tHq_1400LH_2016postVFP,Tprime_tHq_1500LH_2016postVFP,Tprime_tHq_1600LH_2016postVFP,Tprime_tHq_1700LH_2016postVFP,Tprime_tHq_1800LH_2016postVFP]



#Data
DataMuB0_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB0_2016preVFP")
DataMuB0_2016preVFP.runP = 'B'
DataMuB0_2016preVFP.year = 2016
DataMuB0_2016preVFP.dataset = '/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataMuB_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2016preVFP")
DataMuB_2016preVFP.runP = 'B'
DataMuB_2016preVFP.year = 2016
DataMuB_2016preVFP.dataset = '/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMuC_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2016preVFP")
DataMuC_2016preVFP.runP = 'C'
DataMuC_2016preVFP.year = 2016
DataMuC_2016preVFP.dataset = '/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMuD_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2016preVFP")
DataMuD_2016preVFP.runP = 'D'
DataMuD_2016preVFP.year = 2016
DataMuD_2016preVFP.dataset = '/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataMuE_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2016preVFP")
DataMuE_2016preVFP.runP = 'E'
DataMuE_2016preVFP.year = 2016
DataMuE_2016preVFP.dataset = '/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataMuF_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2016preVFP")
DataMuF_2016preVFP.runP = 'F'
DataMuF_2016preVFP.year = 2016
DataMuF_2016preVFP.dataset = '/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataMu_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2016preVFP")
DataMu_2016preVFP.year = 2016
DataMu_2016preVFP.components = [DataMuB_2016preVFP, DataMuC_2016preVFP, DataMuD_2016preVFP, DataMuE_2016preVFP, DataMuF_2016preVFP] #DataMuB0_2016preVFP,


DataMuF_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2016postVFP")
DataMuF_2016postVFP.runP = 'F'
DataMuF_2016postVFP.year = 2016
DataMuF_2016postVFP.dataset = '/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuG_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuG_2016postVFP")
DataMuG_2016postVFP.runP = 'G'
DataMuG_2016postVFP.year = 2016
DataMuG_2016postVFP.dataset = '/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuH_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuH_2016postVFP")
DataMuH_2016postVFP.runP = 'H'
DataMuH_2016postVFP.year = 2016
DataMuH_2016postVFP.dataset = '/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMu_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2016postVFP")
DataMu_2016postVFP.year = 2016
DataMu_2016postVFP.components = [DataMuF_2016postVFP, DataMuG_2016postVFP, DataMuH_2016postVFP]


DataEleB0_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB0_2016preVFP")
DataEleB0_2016preVFP.runP = 'B'
DataEleB0_2016preVFP.year = 2016
DataEleB0_2016preVFP.dataset = '/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataEleB_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2016preVFP")
DataEleB_2016preVFP.runP = 'B'
DataEleB_2016preVFP.year = 2016
DataEleB_2016preVFP.dataset = '/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataEleC_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2016preVFP")
DataEleC_2016preVFP.runP = 'C'
DataEleC_2016preVFP.year = 2016
DataEleC_2016preVFP.dataset = '/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataEleD_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2016preVFP")
DataEleD_2016preVFP.runP = 'D'
DataEleD_2016preVFP.year = 2016
DataEleD_2016preVFP.dataset = '/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataEleE_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2016preVFP")
DataEleE_2016preVFP.runP = 'E'
DataEleE_2016preVFP.year = 2016
DataEleE_2016preVFP.dataset = '/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataEleF_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2016preVFP")
DataEleF_2016preVFP.runP = 'F'
DataEleF_2016preVFP.year = 2016
DataEleF_2016preVFP.dataset = '/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataEle_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2016preVFP")
DataEle_2016preVFP.year = 2016
DataEle_2016preVFP.components = [DataEleB_2016preVFP, DataEleC_2016preVFP, DataEleD_2016preVFP, DataEleE_2016preVFP, DataEleF_2016preVFP] # DataEleB0_2016preVFP,


DataEleF_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2016postVFP")
DataEleF_2016postVFP.runP = 'F'
DataEleF_2016postVFP.year = 2016
DataEleF_2016postVFP.dataset = '/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleG_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleG_2016postVFP")
DataEleG_2016postVFP.runP = 'G'
DataEleG_2016postVFP.year = 2016
DataEleG_2016postVFP.dataset = '/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleH_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleH_2016postVFP")
DataEleH_2016postVFP.runP = 'H'
DataEleH_2016postVFP.year = 2016
DataEleH_2016postVFP.dataset = '/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEle_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2016postVFP")
DataEle_2016postVFP.year = 2016
DataEle_2016postVFP.components = [DataEleF_2016postVFP, DataEleG_2016postVFP, DataEleH_2016postVFP]


DataPhB0_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhB0_2016preVFP")
DataPhB0_2016preVFP.runP = 'B'
DataPhB0_2016preVFP.year = 2016
DataPhB0_2016preVFP.dataset = '/SinglePhoton/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataPhB_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhB_2016preVFP")
DataPhB_2016preVFP.runP = 'B'
DataPhB_2016preVFP.year = 2016
DataPhB_2016preVFP.dataset = '/SinglePhoton/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataPhC_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhC_2016preVFP")
DataPhC_2016preVFP.runP = 'C'
DataPhC_2016preVFP.year = 2016
DataPhC_2016preVFP.dataset = '/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v4/NANOAOD'
DataPhD_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhD_2016preVFP")
DataPhD_2016preVFP.runP = 'D'
DataPhD_2016preVFP.year = 2016
DataPhD_2016preVFP.dataset = '/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataPhE_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhE_2016preVFP")
DataPhE_2016preVFP.runP = 'E'
DataPhE_2016preVFP.year = 2016
DataPhE_2016preVFP.dataset = '/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataPhF_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhF_2016preVFP")
DataPhF_2016preVFP.runP = 'F'
DataPhF_2016preVFP.year = 2016
DataPhF_2016preVFP.dataset = '/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataPh_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPh_2016preVFP")
DataPh_2016preVFP.year = 2016
DataPh_2016preVFP.components = [DataPhB_2016preVFP, DataPhC_2016preVFP, DataPhD_2016preVFP, DataPhE_2016preVFP, DataPhF_2016preVFP] #DataPhB0_2016preVFP,


DataPhF_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhF_2016postVFP")
DataPhF_2016postVFP.runP = 'F'
DataPhF_2016postVFP.year = 2016
DataPhF_2016postVFP.dataset = '/SinglePhoton/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPhG_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhG_2016postVFP")
DataPhG_2016postVFP.runP = 'G'
DataPhG_2016postVFP.year = 2016
DataPhG_2016postVFP.dataset = '/SinglePhoton/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataPhH_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhH_2016postVFP")
DataPhH_2016postVFP.runP = 'H'
DataPhH_2016postVFP.year = 2016
DataPhH_2016postVFP.dataset = '/SinglePhoton/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPh_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataPh_2016postVFP")
DataPh_2016postVFP.year = 2016
DataPh_2016postVFP.components = [DataPhF_2016postVFP, DataPhG_2016postVFP, DataPhH_2016postVFP]


DataHTB0_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB0_2016preVFP")
DataHTB0_2016preVFP.runP = 'B'
DataHTB0_2016preVFP.year = 2016
DataHTB0_2016preVFP.dataset = '/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataHTB_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2016preVFP")
DataHTB_2016preVFP.runP = 'B'
DataHTB_2016preVFP.year = 2016
DataHTB_2016preVFP.dataset = '/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataHTC_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2016preVFP")
DataHTC_2016preVFP.runP = 'C'
DataHTC_2016preVFP.year = 2016
DataHTC_2016preVFP.dataset = '/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataHTD_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2016preVFP")
DataHTD_2016preVFP.runP = 'D'
DataHTD_2016preVFP.year = 2016
DataHTD_2016preVFP.dataset = '/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataHTE_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2016preVFP")
DataHTE_2016preVFP.runP = 'E'
DataHTE_2016preVFP.year = 2016
DataHTE_2016preVFP.dataset = '/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataHTF_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2016preVFP")
DataHTF_2016preVFP.runP = 'F'
DataHTF_2016preVFP.year = 2016
DataHTF_2016preVFP.dataset = '/JetHT/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataHT_2016preVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2016preVFP")
DataHT_2016preVFP.year = 2016
DataHT_2016preVFP.components = [DataHTB_2016preVFP, DataHTC_2016preVFP, DataHTD_2016preVFP, DataHTE_2016preVFP, DataHTF_2016preVFP] #DataHTB0_2016preVFP,


DataHTF_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2016postVFP")
DataHTF_2016postVFP.runP = 'F'
DataHTF_2016postVFP.year = 2016
DataHTF_2016postVFP.dataset = '/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataHTG_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTG_2016postVFP")
DataHTG_2016postVFP.runP = 'G'
DataHTG_2016postVFP.year = 2016
DataHTG_2016postVFP.dataset = '/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataHTH_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTH_2016postVFP")
DataHTH_2016postVFP.runP = 'H'
DataHTH_2016postVFP.year = 2016
DataHTH_2016postVFP.dataset = '/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataHT_2016postVFP = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2016postVFP")
DataHT_2016postVFP.year = 2016
DataHT_2016postVFP.components = [DataHTF_2016postVFP, DataHTG_2016postVFP, DataHTH_2016postVFP]


###################################################################################################################################################################
############################################################                                           ############################################################
############################################################                    2016                   ############################################################
############################################################                                           ############################################################
###################################################################################################################################################################

################################ TTbar ################################

TT_Mtt700to1000_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2016")
TT_Mtt700to1000_2016.sigma = 80.5 #pb
TT_Mtt700to1000_2016.year = 2016
TT_Mtt700to1000_2016.dataset =""

TT_Mtt1000toInf_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2016")
TT_Mtt1000toInf_2016.sigma = 21.3 #pb
TT_Mtt1000toInf_2016.year = 2016
TT_Mtt1000toInf_2016.dataset = ""

TT_semilep_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2016")
TT_semilep_2016.sigma = 831.76*0.438 #pb
TT_semilep_2016.year = 2016
TT_semilep_2016.dataset = ""

TT_dilep_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2016")
TT_dilep_2016.sigma =  831.76 * 0.10 #pb
TT_dilep_2016.year = 2016
TT_dilep_2016.dataset =""

TT_Mtt_2016 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2016")
TT_Mtt_2016.year = 2016
TT_Mtt_2016.components = [TT_dilep_2016,TT_semilep_2016,TT_Mtt700to1000_2016, TT_Mtt1000toInf_2016]


#WJets


WJetsHT70to100_2016 = sample(ROOT.kGreen, 1, 1001, "W + Jets", "WJetsHT70to100_2016")
WJetsHT70to100_2016.sigma = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2016.year = 2016
WJetsHT70to100_2016.dataset = ""

WJetsHT100to200_2016 = sample(ROOT.kGreen+1, 1, 1001, "W + Jets", "WJetsHT100to200_2016")
WJetsHT100to200_2016.sigma = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2016.year = 2016
WJetsHT100to200_2016.dataset = ""

WJetsHT200to400_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2016")
WJetsHT200to400_2016.sigma = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2016.year = 2016
WJetsHT200to400_2016.dataset = ""


WJetsHT400to600_2016 = sample(ROOT.kGreen+3, 1, 1001, "W + Jets", "WJetsHT400to600_2016")
WJetsHT400to600_2016.sigma = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2016.year = 2016
WJetsHT400to600_2016.dataset = ""


WJetsHT600to800_2016 = sample(ROOT.kGreen+4, 1, 1001, "W + Jets", "WJetsHT600to800_2016")
WJetsHT600to800_2016.sigma = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2016.year = 2016
WJetsHT600to800_2016.dataset = ""


WJetsHT800to1200_2016 = sample(ROOT.kGreen+5, 1, 1001, "W + Jets", "WJetsHT800to1200_2016")
WJetsHT800to1200_2016.sigma = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2016.year = 2016
WJetsHT800to1200_2016.dataset = ""


WJetsHT1200to2500_2016 = sample(ROOT.kGreen+6, 1, 1001, "W + Jets", "WJetsHT1200to2500_2016")
WJetsHT1200to2500_2016.sigma = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2016.year = 2016
WJetsHT1200to2500_2016.dataset = ""


WJetsHT2500toInf_2016 = sample(ROOT.kGreen+7, 1, 1001, "W + Jets", "WJetsHT2500toInf_2016")
WJetsHT2500toInf_2016.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2016.year = 2016
WJetsHT2500toInf_2016.dataset = ""



WJets_2016 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2016")
WJets_2016.year = 2016
WJets_2016.components = [WJetsHT70to100_2016, WJetsHT100to200_2016, WJetsHT200to400_2016, WJetsHT400to600_2016, WJetsHT600to800_2016, WJetsHT800to1200_2016, WJetsHT1200to2500_2016, WJetsHT2500toInf_2016]


#QCD

QCDHT_50to100_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_50to100_2016")
QCDHT_50to100_2016.sigma = 0 #347700 #pb
QCDHT_50to100_2016.year = 2016
QCDHT_50to100_2016.dataset = ""

QCDHT_100to200_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2016")
QCDHT_100to200_2016.sigma = 27990000#0 #347700 #pb
QCDHT_100to200_2016.year = 2016
QCDHT_100to200_2016.dataset = ""

QCDHT_200to300_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2016")
QCDHT_200to300_2016.sigma = 1712000 #347700 #pb
QCDHT_200to300_2016.year = 2016
QCDHT_200to300_2016.dataset = ""

QCDHT_300to500_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2016")
QCDHT_300to500_2016.sigma = 347700 #pb
QCDHT_300to500_2016.year = 2016
QCDHT_300to500_2016.dataset = ""

QCDHT_500to700_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2016")
QCDHT_500to700_2016.sigma = 32100 #pb
QCDHT_500to700_2016.year = 2016
QCDHT_500to700_2016.dataset = ""

QCDHT_700to1000_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2016")
QCDHT_700to1000_2016.sigma = 6831 #pb
QCDHT_700to1000_2016.year = 2016
QCDHT_700to1000_2016.dataset = ""

QCDHT_1000to1500_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2016")
QCDHT_1000to1500_2016.sigma = 1207 #pb
QCDHT_1000to1500_2016.year = 2016
QCDHT_1000to1500_2016.dataset = ""

QCDHT_1500to2000_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2016")
QCDHT_1500to2000_2016.sigma = 119.9 #pb
QCDHT_1500to2000_2016.year = 2016
QCDHT_1500to2000_2016.dataset = ""

QCDHT_2000toInf_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2016")
QCDHT_2000toInf_2016.sigma = 25.24 #pb
QCDHT_2000toInf_2016.year = 2016
QCDHT_2000toInf_2016.dataset = ""

QCD_2016 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2016")
QCD_2016.year = 2016
QCD_2016.components = [QCDHT_100to200_2016,QCDHT_200to300_2016,QCDHT_300to500_2016, QCDHT_500to700_2016, QCDHT_700to1000_2016, QCDHT_1000to1500_2016, QCDHT_1500to2000_2016, QCDHT_2000toInf_2016]

#ST
ST_tch_t_2016 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_t_2016")
ST_tch_t_2016.sigma =  136.02 #pb
ST_tch_t_2016.year = 2016
ST_tch_t_2016.dataset = ""

ST_tch_tbar_2016 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_tbar_2016")
ST_tch_tbar_2016.sigma =  80.95 #pb
ST_tch_tbar_2016.year = 2016
ST_tch_tbar_2016.dataset = ""

ST_tW_t_2016 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_t_2016")
ST_tW_t_2016.sigma =  71.7/2 #pb
ST_tW_t_2016.year = 2016
ST_tW_t_2016.dataset = ""

ST_tW_tbar_2016 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_tbar_2016")
ST_tW_tbar_2016.sigma = 71.7/2 #pb
ST_tW_tbar_2016.year = 2016
ST_tW_tbar_2016.dataset = ""

ST_sch_2016 = sample(ROOT.kYellow, 1, 1001, "ST s-ch", "ST_sch_2016")
ST_sch_2016.sigma = 10.32*0.324 #pb
ST_sch_2016.year = 2016
ST_sch_2016.dataset = ""

ST_2016 = sample(ROOT.kYellow, 1, 1001, "Single top", "ST_2016")
ST_2016.year = 2016
ST_2016.components = [ST_tch_t_2016, ST_tch_tbar_2016, ST_tW_t_2016, ST_tW_tbar_2016, ST_sch_2016]

#signal

Tprime_tHq_600LH_2016 = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2016")
Tprime_tHq_600LH_2016.sigma = 0.07453
Tprime_tHq_600LH_2016.year = 2016
Tprime_tHq_600LH_2016.dataset=""

Tprime_tHq_700LH_2016 = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2016")
Tprime_tHq_700LH_2016.sigma = 88.107/1000. #to be changed
Tprime_tHq_700LH_2016.year = 2016
Tprime_tHq_700LH_2016.dataset=""

Tprime_tHq_800LH_2016 = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2016")
Tprime_tHq_800LH_2016.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2016.year = 2016
Tprime_tHq_800LH_2016.dataset=""

Tprime_tHq_900LH_2016 = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2016")
Tprime_tHq_900LH_2016.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2016.year = 2016
Tprime_tHq_900LH_2016.dataset=""

Tprime_tHq_1000LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2016")
Tprime_tHq_1000LH_2016.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2016.year = 2016
Tprime_tHq_1000LH_2016.dataset=""

Tprime_tHq_1100LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2016")
Tprime_tHq_1100LH_2016.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2016.year = 2016
Tprime_tHq_1100LH_2016.dataset=""

Tprime_tHq_1200LH_2016 = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2016")
Tprime_tHq_1200LH_2016.sigma = 0.01973
Tprime_tHq_1200LH_2016.year = 2016
Tprime_tHq_1200LH_2016.dataset=""

Tprime_tHq_1300LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2016")
Tprime_tHq_1300LH_2016.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2016.year = 2016
Tprime_tHq_1300LH_2016.dataset=""

Tprime_tHq_1400LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2016")
Tprime_tHq_1400LH_2016.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2016.year = 2016
Tprime_tHq_1400LH_2016.dataset=""

Tprime_tHq_1500LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2016")
Tprime_tHq_1500LH_2016.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2016.year = 2016
Tprime_tHq_1500LH_2016.dataset=""

Tprime_tHq_1600LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2016")
Tprime_tHq_1600LH_2016.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2016.year = 2016
Tprime_tHq_1600LH_2016.dataset=""

Tprime_tHq_1700LH_2016 = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2016")
Tprime_tHq_1700LH_2016.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2016.year = 2016
Tprime_tHq_1700LH_2016.dataset=""

Tprime_tHq_1800LH_2016 = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2016")
Tprime_tHq_1800LH_2016.sigma = 0.005829
Tprime_tHq_1800LH_2016.year = 2016
Tprime_tHq_1800LH_2016.dataset=""

Tprime_LH_2016 = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2016")
Tprime_LH_2016.year = 2016
Tprime_LH_2016.components = [Tprime_tHq_600LH_2016,Tprime_tHq_700LH_2016,Tprime_tHq_800LH_2016,Tprime_tHq_900LH_2016,Tprime_tHq_1000LH_2016,Tprime_tHq_1100LH_2016,Tprime_tHq_1200LH_2016,Tprime_tHq_1300LH_2016,Tprime_tHq_1400LH_2016,Tprime_tHq_1500LH_2016,Tprime_tHq_1600LH_2016,Tprime_tHq_1700LH_2016,Tprime_tHq_1800LH_2016]


#Data
DataMuB0_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB0_2016")
DataMuB0_2016.runP = 'B'
DataMuB0_2016.year = 2016
DataMuB0_2016.dataset = ''

DataMuB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2016")
DataMuB_2016.runP = 'B'
DataMuB_2016.year = 2016
DataMuB_2016.dataset = ''
DataMuC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2016")
DataMuC_2016.runP = 'C'
DataMuC_2016.year = 2016
DataMuC_2016.dataset = ''
DataMuD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2016")
DataMuD_2016.runP = 'D'
DataMuD_2016.year = 2016
DataMuD_2016.dataset = ''
DataMuE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2016")
DataMuE_2016.runP = 'E'
DataMuE_2016.year = 2016
DataMuE_2016.dataset = ''

DataMuF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2016")
DataMuF_2016.runP = 'F'
DataMuF_2016.year = 2016
DataMuF_2016.dataset = ''

DataMuG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuG_2016")
DataMuG_2016.runP = 'G'
DataMuG_2016.year = 2016
DataMuG_2016.dataset = ''
DataMuH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuH_2016")
DataMuH_2016.runP = 'H'
DataMuH_2016.year = 2016
DataMuH_2016.dataset = ''

DataMu_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2016")
DataMu_2016.year = 2016
DataMu_2016.components = [DataMuB0_2016,DataMuB_2016, DataMuC_2016, DataMuD_2016, DataMuE_2016, DataMuF_2016, DataMuG_2016, DataMuH_2016]

DataEleB0_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB0_2016")
DataEleB0_2016.runP = 'B'
DataEleB0_2016.year = 2016
DataEleB0_2016.dataset = ''

DataEleB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2016")
DataEleB_2016.runP = 'B'
DataEleB_2016.year = 2016
DataEleB_2016.dataset = ''
DataEleC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2016")
DataEleC_2016.runP = 'C'
DataEleC_2016.year = 2016
DataEleC_2016.dataset = ''
DataEleD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2016")
DataEleD_2016.runP = 'D'
DataEleD_2016.year = 2016
DataEleD_2016.dataset = ''
DataEleE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2016")
DataEleE_2016.runP = 'E'
DataEleE_2016.year = 2016
DataEleE_2016.dataset = ''

DataEleF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2016")
DataEleF_2016.runP = 'F'
DataEleF_2016.year = 2016
DataEleF_2016.dataset = ''
DataEleG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleG_2016")
DataEleG_2016.runP = 'G'
DataEleG_2016.year = 2016
DataEleG_2016.dataset = ''
DataEleH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleH_2016")
DataEleH_2016.runP = 'H'
DataEleH_2016.year = 2016
DataEleH_2016.dataset = ''

DataEle_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2016")
DataEle_2016.year = 2016
DataEle_2016.components = [DataEleB0_2016,DataEleB_2016, DataEleC_2016, DataEleD_2016, DataEleE_2016, DataEleF_2016, DataEleG_2016, DataEleH_2016]

DataPhB0_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhB0_2016")
DataPhB0_2016.runP = 'B'
DataPhB0_2016.year = 2016
DataPhB0_2016.dataset = ''

DataPhB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhB_2016")
DataPhB_2016.runP = 'B'
DataPhB_2016.year = 2016
DataPhB_2016.dataset = ''
DataPhC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhC_2016")
DataPhC_2016.runP = 'C'
DataPhC_2016.year = 2016
DataPhC_2016.dataset = ''
DataPhD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhD_2016")
DataPhD_2016.runP = 'D'
DataPhD_2016.year = 2016
DataPhD_2016.dataset = ''
DataPhE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhE_2016")
DataPhE_2016.runP = 'E'
DataPhE_2016.year = 2016
DataPhE_2016.dataset = ''

DataPhF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhF_2016")
DataPhF_2016.runP = 'F'
DataPhF_2016.year = 2016
DataPhF_2016.dataset = ''

DataPhG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhG_2016")
DataPhG_2016.runP = 'G'
DataPhG_2016.year = 2016
DataPhG_2016.dataset = ''
DataPhH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhH_2016")
DataPhH_2016.runP = 'H'
DataPhH_2016.year = 2016
DataPhH_2016.dataset = ''
DataPh_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPh_2016")
DataPh_2016.year = 2016
DataPh_2016.components = [DataPhB0_2016,DataPhB_2016, DataPhC_2016, DataPhD_2016, DataPhE_2016,DataPhF_2016, DataPhG_2016, DataPhH_2016]

DataHTB0_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB0_2016")
DataHTB0_2016.runP = 'B'
DataHTB0_2016.year = 2016
DataHTB0_2016.dataset = ''

DataHTB_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2016")
DataHTB_2016.runP = 'B'
DataHTB_2016.year = 2016
DataHTB_2016.dataset = ''
DataHTC_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2016")
DataHTC_2016.runP = 'C'
DataHTC_2016.year = 2016
DataHTC_2016.dataset = ''
DataHTD_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2016")
DataHTD_2016.runP = 'D'
DataHTD_2016.year = 2016
DataHTD_2016.dataset = ''
DataHTE_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2016")
DataHTE_2016.runP = 'E'
DataHTE_2016.year = 2016
DataHTE_2016.dataset = ''

DataHTF_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2016")
DataHTF_2016.runP = 'F'
DataHTF_2016.year = 2016
DataHTF_2016.dataset = ''

DataHTG_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTG_2016")
DataHTG_2016.runP = 'G'
DataHTG_2016.year = 2016
DataHTG_2016.dataset = ''
DataHTH_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTH_2016")
DataHTH_2016.runP = 'H'
DataHTH_2016.year = 2016
DataHTH_2016.dataset = ''
DataHT_2016 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2016")
DataHT_2016.year = 2016
DataHT_2016.components = [DataHTB0_2016, DataHTB_2016, DataHTC_2016, DataHTD_2016, DataHTE_2016, DataHTF_2016, DataHTG_2016, DataHTH_2016]

###################################################################################################################################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
############################################################                    2017                   ############################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
###################################################################################################################################################################                                                                                                                                               

################################ TTbar ################################                                                                                                                                                                                                                                           


TT_Mtt700to1000_2017 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2017")
TT_Mtt700to1000_2017.sigma = 80.5 #pb                                                                        
TT_Mtt700to1000_2017.year = 2017
TT_Mtt700to1000_2017.dataset ="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v2/NANOAODSIM"                                              

TT_Mtt1000toInf_2017 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2017")
TT_Mtt1000toInf_2017.sigma = 21.3 #pb                          
TT_Mtt1000toInf_2017.year = 2017
TT_Mtt1000toInf_2017.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v2/NANOAODSIM"

TT_semilep_2017 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2017")
TT_semilep_2017.sigma = 831.76*0.438 #pb
TT_semilep_2017.year = 2017
TT_semilep_2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

TT_dilep_2017 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2017")
TT_dilep_2017.sigma =  831.76 * 0.10 #pb
TT_dilep_2017.year = 2017
TT_dilep_2017.dataset ="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v1/NANOAODSIM"

TT_Mtt_2017 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2017")
TT_Mtt_2017.year = 2017
TT_Mtt_2017.components = [TT_dilep_2017,TT_semilep_2017,TT_Mtt700to1000_2017, TT_Mtt1000toInf_2017]


#WJets


WJetsHT70to100_2017 = sample(ROOT.kGreen, 1, 1001, "W + Jets", "WJetsHT70to100_2017")
WJetsHT70to100_2017.sigma = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2017.year = 2017
WJetsHT70to100_2017.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT100to200_2017 = sample(ROOT.kGreen+1, 1, 1001, "W + Jets", "WJetsHT100to200_2017")
WJetsHT100to200_2017.sigma = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2017.year = 2017
WJetsHT100to200_2017.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

WJetsHT200to400_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2017")
WJetsHT200to400_2017.sigma = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2017.year = 2017
WJetsHT200to400_2017.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT200to400_2017.files = jr.json_reader(path+"/WJets_HT200To400_2017.json")

WJetsHT400to600_2017 = sample(ROOT.kGreen+3, 1, 1001, "W + Jets", "WJetsHT400to600_2017")
WJetsHT400to600_2017.sigma = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2017.year = 2017
WJetsHT400to600_2017.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT400to600_2017.files = jr.json_reader(path+"/WJets_HT400To600_2017.json")

WJetsHT600to800_2017 = sample(ROOT.kGreen+4, 1, 1001, "W + Jets", "WJetsHT600to800_2017")
WJetsHT600to800_2017.sigma = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2017.year = 2017
WJetsHT600to800_2017.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"
#WJetsHT600to800_2017.files = jr.json_reader(path+"/WJets_HT600To800_2017.json")

WJetsHT800to1200_2017 = sample(ROOT.kGreen+5, 1, 1001, "W + Jets", "WJetsHT800to1200_2017")
WJetsHT800to1200_2017.sigma = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2017.year = 2017
WJetsHT800to1200_2017.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v3/NANOAODSIM"
#WJetsHT800to1200_2017.files = jr.json_reader(path+"/WJets_HT800To1200_2017.json")

WJetsHT1200to2500_2017 = sample(ROOT.kGreen+6, 1, 1001, "W + Jets", "WJetsHT1200to2500_2017")
WJetsHT1200to2500_2017.sigma = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2017.year = 2017
WJetsHT1200to2500_2017.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"


WJetsHT2500toInf_2017 = sample(ROOT.kGreen+7, 1, 1001, "W + Jets", "WJetsHT2500toInf_2017")
WJetsHT2500toInf_2017.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2017.year = 2017
WJetsHT2500toInf_2017.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v2/NANOAODSIM"



WJets_2017 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2017")
WJets_2017.year = 2017
WJets_2017.components = [WJetsHT70to100_2017, WJetsHT100to200_2017, WJetsHT200to400_2017, WJetsHT400to600_2017, WJetsHT600to800_2017, WJetsHT800to1200_2017, WJetsHT1200to2500_2017, WJetsHT2500toInf_2017]

#QCD

QCDHT_50to100_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_50to100_2017")
QCDHT_50to100_2017.sigma = 0 #347700 #pb
QCDHT_50to100_2017.year = 2017
QCDHT_50to100_2017.dataset = "/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_100to200_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2017")
QCDHT_100to200_2017.sigma = 27990000#0 #347700 #pb
QCDHT_100to200_2017.year = 2017
QCDHT_100to200_2017.dataset = "/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_200to300_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2017")
QCDHT_200to300_2017.sigma = 1712000 #347700 #pb
QCDHT_200to300_2017.year = 2017
QCDHT_200to300_2017.dataset = "/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_300to500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2017")
QCDHT_300to500_2017.sigma = 347700 #pb
QCDHT_300to500_2017.year = 2017
QCDHT_300to500_2017.dataset = "/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_500to700_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2017")
QCDHT_500to700_2017.sigma = 32100 #pb
QCDHT_500to700_2017.year = 2017
QCDHT_500to700_2017.dataset = "/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_700to1000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2017")
QCDHT_700to1000_2017.sigma = 6831 #pb
QCDHT_700to1000_2017.year = 2017
QCDHT_700to1000_2017.dataset = "/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_1000to1500_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2017")
QCDHT_1000to1500_2017.sigma = 1207 #pb
QCDHT_1000to1500_2017.year = 2017
QCDHT_1000to1500_2017.dataset = "/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_1500to2000_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2017")
QCDHT_1500to2000_2017.sigma = 119.9 #pb
QCDHT_1500to2000_2017.year = 2017
QCDHT_1500to2000_2017.dataset = "/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCDHT_2000toInf_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2017")
QCDHT_2000toInf_2017.sigma = 25.24 #pb
QCDHT_2000toInf_2017.year = 2017
QCDHT_2000toInf_2017.dataset = "/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2017+"-v1/NANOAODSIM"

QCD_2017 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2017")
QCD_2017.year = 2017
QCD_2017.components = [QCDHT_100to200_2017,QCDHT_200to300_2017,QCDHT_300to500_2017, QCDHT_500to700_2017, QCDHT_700to1000_2017, QCDHT_1000to1500_2017, QCDHT_1500to2000_2017, QCDHT_2000toInf_2017]

#ST
ST_tch_t_2017 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_t_2017")
ST_tch_t_2017.sigma =  136.02 #pb
ST_tch_t_2017.year = 2017
ST_tch_t_2017.dataset = "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2017+"-v1/NANOAODSIM"

ST_tch_tbar_2017 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_tbar_2017")
ST_tch_tbar_2017.sigma =  80.95 #pb
ST_tch_tbar_2017.year = 2017
ST_tch_tbar_2017.dataset = "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2017+"-v1/NANOAODSIM"

ST_tW_t_2017 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_t_2017")
ST_tW_t_2017.sigma =  71.7/2 #pb
ST_tW_t_2017.year = 2017
ST_tW_t_2017.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v2/NANOAODSIM"

ST_tW_tbar_2017 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_tbar_2017")
ST_tW_tbar_2017.sigma = 71.7/2 #pb
ST_tW_tbar_2017.year = 2017
ST_tW_tbar_2017.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2017+"-v2/NANOAODSIM"

ST_sch_2017 = sample(ROOT.kYellow, 1, 1001, "ST s-ch", "ST_sch_2017")
ST_sch_2017.sigma = 10.32*0.324 #pb
ST_sch_2017.year = 2017
ST_sch_2017.dataset = "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2017+"-v1/NANOAODSIM"

ST_2017 = sample(ROOT.kYellow, 1, 1001, "Single top", "ST_2017")
ST_2017.year = 2017
ST_2017.components = [ST_tch_t_2017, ST_tch_tbar_2017, ST_tW_t_2017, ST_tW_tbar_2017, ST_sch_2017]

#signal

Tprime_tHq_600LH_2017 = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2017")
Tprime_tHq_600LH_2017.sigma = 0.07453
Tprime_tHq_600LH_2017.year = 2017
Tprime_tHq_600LH_2017.dataset="/TprimeBToTH_M-600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_700LH_2017 = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2017")
Tprime_tHq_700LH_2017.sigma = 88.107/1000. #to be changed
Tprime_tHq_700LH_2017.year = 2017
Tprime_tHq_700LH_2017.dataset="/TprimeBToTH_M-700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_800LH_2017 = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2017")
Tprime_tHq_800LH_2017.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2017.year = 2017
Tprime_tHq_800LH_2017.dataset="/TprimeBToTH_M-800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_900LH_2017 = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2017")
Tprime_tHq_900LH_2017.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2017.year = 2017
Tprime_tHq_900LH_2017.dataset="/TprimeBToTH_M-900_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1000LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2017")
Tprime_tHq_1000LH_2017.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2017.year = 2017
Tprime_tHq_1000LH_2017.dataset="/TprimeBToTH_M-1000_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1100LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2017")
Tprime_tHq_1100LH_2017.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2017.year = 2017
Tprime_tHq_1100LH_2017.dataset="/TprimeBToTH_M-1100_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1200LH_2017 = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2017")
Tprime_tHq_1200LH_2017.sigma = 0.01973
Tprime_tHq_1200LH_2017.year = 2017
Tprime_tHq_1200LH_2017.dataset="/TprimeBToTH_M-1200_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1300LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2017")
Tprime_tHq_1300LH_2017.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2017.year = 2017
Tprime_tHq_1300LH_2017.dataset="/TprimeBToTH_M-1300_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1400LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2017")
Tprime_tHq_1400LH_2017.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2017.year = 2017
Tprime_tHq_1400LH_2017.dataset="/TprimeBToTH_M-1400_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1500LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2017")
Tprime_tHq_1500LH_2017.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2017.year = 2017
Tprime_tHq_1500LH_2017.dataset="/TprimeBToTH_M-1500_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1600LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2017")
Tprime_tHq_1600LH_2017.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2017.year = 2017
Tprime_tHq_1600LH_2017.dataset="/TprimeBToTH_M-1600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1700LH_2017 = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2017")
Tprime_tHq_1700LH_2017.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2017.year = 2017
Tprime_tHq_1700LH_2017.dataset="/TprimeBToTH_M-1700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tHq_1800LH_2017 = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2017")
Tprime_tHq_1800LH_2017.sigma = 0.005829
Tprime_tHq_1800LH_2017.year = 2017
Tprime_tHq_1800LH_2017.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2017")
Tprime_LH_2017.year = 2017
Tprime_LH_2017.components = [Tprime_tHq_600LH_2017,Tprime_tHq_700LH_2017,Tprime_tHq_800LH_2017,Tprime_tHq_900LH_2017,Tprime_tHq_1000LH_2017,Tprime_tHq_1100LH_2017,Tprime_tHq_1200LH_2017,Tprime_tHq_1300LH_2017,Tprime_tHq_1400LH_2017,Tprime_tHq_1500LH_2017,Tprime_tHq_1600LH_2017,Tprime_tHq_1700LH_2017,Tprime_tHq_1800LH_2017]

#Data
DataMuB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2017")
DataMuB_2017.runP = 'B'
DataMuB_2017.year = 2017
DataMuB_2017.dataset = '/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2017")
DataMuC_2017.runP = 'C'
DataMuC_2017.year = 2017
DataMuC_2017.dataset = '/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2017")
DataMuD_2017.runP = 'D'
DataMuD_2017.year = 2017
DataMuD_2017.dataset = '/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuE_2017")
DataMuE_2017.runP = 'E'
DataMuE_2017.year = 2017
DataMuE_2017.dataset = '/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMuF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuF_2017")
DataMuF_2017.runP = 'F'
DataMuF_2017.year = 2017
DataMuF_2017.dataset = '/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataMu_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2017")
DataMu_2017.year = 2017
DataMu_2017.components = [DataMuB_2017, DataMuC_2017, DataMuD_2017, DataMuE_2017, DataMuF_2017]

DataEleB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2017")
DataEleB_2017.runP = 'B'
DataEleB_2017.year = 2017
DataEleB_2017.dataset = '/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2017")
DataEleC_2017.runP = 'C'
DataEleC_2017.year = 2017
DataEleC_2017.dataset = '/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2017")
DataEleD_2017.runP = 'D'
DataEleD_2017.year = 2017
DataEleD_2017.dataset = '/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleE_2017")
DataEleE_2017.runP = 'E'
DataEleE_2017.year = 2017
DataEleE_2017.dataset = '/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleF_2017")
DataEleF_2017.runP = 'F'
DataEleF_2017.year = 2017
DataEleF_2017.dataset = '/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEle_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2017")
DataEle_2017.year = 2017
DataEle_2017.components = [DataEleB_2017, DataEleC_2017, DataEleD_2017, DataEleE_2017, DataEleF_2017]


DataPhB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhB_2017")
DataPhB_2017.runP = 'B'
DataPhB_2017.year = 2017
DataPhB_2017.dataset = '/SinglePhoton/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPhC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhC_2017")
DataPhC_2017.runP = 'C'
DataPhC_2017.year = 2017
DataPhC_2017.dataset = '/SinglePhoton/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPhD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhD_2017")
DataPhD_2017.runP = 'D'
DataPhD_2017.year = 2017
DataPhD_2017.dataset = '/SinglePhoton/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPhE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhE_2017")
DataPhE_2017.runP = 'E'
DataPhE_2017.year = 2017
DataPhE_2017.dataset = '/SinglePhoton/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPhF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPhF_2017")
DataPhF_2017.runP = 'F'
DataPhF_2017.year = 2017
DataPhF_2017.dataset = '/SinglePhoton/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataPh_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataPh_2017")
DataPh_2017.year = 2017
DataPh_2017.components = [DataPhB_2017, DataPhC_2017, DataPhD_2017, DataPhE_2017, DataPhF_2017]


DataHTB_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2017")
DataHTB_2017.runP = 'B'
DataHTB_2017.year = 2017
DataHTB_2017.dataset = '/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataHTC_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2017")
DataHTC_2017.runP = 'C'
DataHTC_2017.year = 2017
DataHTC_2017.dataset = '/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataHTD_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2017")
DataHTD_2017.runP = 'D'
DataHTD_2017.year = 2017
DataHTD_2017.dataset = '/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataHTE_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTE_2017")
DataHTE_2017.runP = 'E'
DataHTE_2017.year = 2017
DataHTE_2017.dataset = '/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataHTF_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTF_2017")
DataHTF_2017.runP = 'F'
DataHTF_2017.year = 2017
DataHTF_2017.dataset = '/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataHT_2017 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2017")
DataHT_2017.year = 2017
DataHT_2017.components = [ DataHTB_2017, DataHTC_2017, DataHTD_2017, DataHTE_2017, DataHTF_2017]


###################################################################################################################################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
############################################################                    2018                   ############################################################                                                                                                                                               
############################################################                                           ############################################################                                                                                                                                               
###################################################################################################################################################################                                                                                                                                               

################################ TTbar ################################                                                                                                                                                                                                                                           


TT_Mtt700to1000_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt700to1000_2018")
TT_Mtt700to1000_2018.sigma = 80.5 #pb                                                                                                                                                                     
TT_Mtt700to1000_2018.year = 2018
TT_Mtt700to1000_2018.dataset ="/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"                                              

TT_Mtt1000toInf_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt1000toInf_2018")
TT_Mtt1000toInf_2018.sigma = 21.3 #pb                          
TT_Mtt1000toInf_2018.year = 2018
TT_Mtt1000toInf_2018.dataset = "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TT_semilep_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_semilep_2018")
TT_semilep_2018.sigma = 831.76*0.438 #pb
TT_semilep_2018.year = 2018
TT_semilep_2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TT_dilep_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_dilep_2018")
TT_dilep_2018.sigma =  831.76 * 0.10 #pb                                                                                                                                                                    
TT_dilep_2018.year = 2018
TT_dilep_2018.dataset ="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/NANOAODSIM"

"""
TT_Had_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Had_2018")
TT_Had_2018.sigma =  831.76 * (1-0.10-0.438) #pb
TT_Had_2018.year = 2018
TT_Had_2018.dataset ="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v1/TT"
"""

TT_Mtt_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2018")
TT_Mtt_2018.year = 2018
TT_Mtt_2018.components = [TT_dilep_2018,TT_semilep_2018,TT_Mtt700to1000_2018, TT_Mtt1000toInf_2018]

TTJetsHT600to800_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t} Jets", "TTJetsHT600to800_2018")
TTJetsHT600to800_2018.sigma =  1.402 #pb
TTJetsHT600to800_2018.year = 2018
TTJetsHT600to800_2018.dataset ="/TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTJetsHT800to1200_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t} Jets", "TTJetsHT800to1200_2018")
TTJetsHT800to1200_2018.sigma =  0.5581 #pb
TTJetsHT800to1200_2018.year = 2018
TTJetsHT800to1200_2018.dataset ="/TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTJetsHT1200to2500_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t} Jets", "TTJetsHT1200to2500_2018")
TTJetsHT1200to2500_2018.sigma =  0.09876 #pb
TTJetsHT1200to2500_2018.year = 2018
TTJetsHT1200to2500_2018.dataset ="/TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTJetsHT2500toInf_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t} Jets", "TTJetsHT2500toInf_2018")
TTJetsHT2500toInf_2018.sigma =  9.277e-06 #pb
TTJetsHT2500toInf_2018.year = 2018
TTJetsHT2500toInf_2018.dataset ="/TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTJets_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t} Jets", "TTJets_2018")
TTJets_2018.year = 2018
TTJets_2018.components = [TTJetsHT600to800_2018,TTJetsHT800to1200_2018,TTJetsHT1200to2500_2018,TTJetsHT2500toInf_2018]

TTHtobb_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} H", "TTHtobb_2018")
TTHtobb_2018.sigma =  0.5269 #pb
TTHtobb_2018.year = 2018
TTHtobb_2018.dataset ="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v2/NANOAODSIM"

TTHtoNonbb_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} H", "TTHtoNonbb_2018")
TTHtoNonbb_2018.sigma =  0.5638 #pb
TTHtoNonbb_2018.year = 2018
TTHtoNonbb_2018.dataset ="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v2/NANOAODSIM"

TTH_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} H", "TTH_2018")
TTH_2018.year = 2018
TTH_2018.components = [TTHtoNonbb_2018,TTHtobb_2018]

TTWJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} W Jets", "TTWJets_2018")
TTWJets_2018.sigma =  0.4611 #pb
TTWJets_2018.year = 2018
TTWJets_2018.dataset ="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/"+tag_2018+"-v2/NANOAODSIM"

TTZJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} Z Jets", "TTZJets_2018")
TTZJets_2018.sigma =  0.5407 #pb
TTZJets_2018.year = 2018
TTZJets_2018.dataset ="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/"+tag_2018+"-v2/NANOAODSIM"

TTVJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} V", "TTVJets_2018")
TTVJets_2018.year = 2018
TTVJets_2018.components = [TTWJets_2018,TTZJets_2018]

TTGJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} G Jets", "TTGJets_2018")
TTGJets_2018.sigma =  3.774 #pb
TTGJets_2018.year = 2018
TTGJets_2018.dataset ="/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TTGHadJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} G Jets", "TTGHadJets_2018")
TTGHadJets_2018.sigma =  4.178 #pb
TTGHadJets_2018.year = 2018
TTGHadJets_2018.dataset ="/TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"


TTGammaJets_2018 = sample(ROOT.kBlue, 1, 1001, "t#bar{t} G Jets", "TTGammaJets_2018")
TTGammaJets_2018.sigma =  5.098 #pb
TTGammaJets_2018.year = 2018
TTGammaJets_2018.dataset ="/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

TGJets_2018 = sample(ROOT.kBlue, 1, 1001, "t G Jets", "TGJets_2018")
TGJets_2018.sigma =  2.997 #pb
TGJets_2018.year = 2018
TGJets_2018.dataset ="/TGJets_TuneCP5_13TeV-amcatnlo-madspin-pythia8/"+tag_2018+"-v2/NANOAODSIM"

#WJets


WJetsHT70to100_2018 = sample(ROOT.kGreen, 1, 1001, "W + Jets", "WJetsHT70to100_2018")
WJetsHT70to100_2018.sigma = 1353.0 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT70to100_2018.year = 2018
WJetsHT70to100_2018.dataset = "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT100to200_2018 = sample(ROOT.kGreen+1, 1, 1001, "W + Jets", "WJetsHT100to200_2018")
WJetsHT100to200_2018.sigma = 1345 * kFactorsQCD["WJetsHT100to200"] #pb
WJetsHT100to200_2018.year = 2018
WJetsHT100to200_2018.dataset = "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

WJetsHT200to400_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJetsHT200to400_2018")
WJetsHT200to400_2018.sigma = 359.7 * kFactorsQCD["WJetsHT200to400"] #pb
WJetsHT200to400_2018.year = 2018
WJetsHT200to400_2018.dataset = "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT200to400_2018.files = jr.json_reader(path+"/WJets_HT200To400_2018.json")

WJetsHT400to600_2018 = sample(ROOT.kGreen+3, 1, 1001, "W + Jets", "WJetsHT400to600_2018")
WJetsHT400to600_2018.sigma = 48.91 * kFactorsQCD["WJetsHT400to600"] #pb
WJetsHT400to600_2018.year = 2018
WJetsHT400to600_2018.dataset = "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT400to600_2018.files = jr.json_reader(path+"/WJets_HT400To600_2018.json")

WJetsHT600to800_2018 = sample(ROOT.kGreen+4, 1, 1001, "W + Jets", "WJetsHT600to800_2018")
WJetsHT600to800_2018.sigma = 12.05 * kFactorsQCD["WJetsHT600to800"] #pb
WJetsHT600to800_2018.year = 2018
WJetsHT600to800_2018.dataset = "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT600to800_2018.files = jr.json_reader(path+"/WJets_HT600To800_2018.json")

WJetsHT800to1200_2018 = sample(ROOT.kGreen+5, 1, 1001, "W + Jets", "WJetsHT800to1200_2018")
WJetsHT800to1200_2018.sigma = 5.501 * kFactorsQCD["WJetsHT800to1200"] #pb
WJetsHT800to1200_2018.year = 2018
WJetsHT800to1200_2018.dataset = "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"
#WJetsHT800to1200_2018.files = jr.json_reader(path+"/WJets_HT800To1200_2018.json")

WJetsHT1200to2500_2018 = sample(ROOT.kGreen+6, 1, 1001, "W + Jets", "WJetsHT1200to2500_2018")
WJetsHT1200to2500_2018.sigma = 1.329 * kFactorsQCD["WJetsHT1200to2500"] #pb
WJetsHT1200to2500_2018.year = 2018
WJetsHT1200to2500_2018.dataset = "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"


WJetsHT2500toInf_2018 = sample(ROOT.kGreen+7, 1, 1001, "W + Jets", "WJetsHT2500toInf_2018")
WJetsHT2500toInf_2018.sigma = 0.03216 * 1.2 #pb
WJetsHT2500toInf_2018.year = 2018
WJetsHT2500toInf_2018.dataset = "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v2/NANOAODSIM"



WJets_2018 = sample(ROOT.kGreen+2, 1, 1001, "W + Jets", "WJets_2018")
WJets_2018.year = 2018
WJets_2018.components = [WJetsHT70to100_2018, WJetsHT100to200_2018, WJetsHT200to400_2018, WJetsHT400to600_2018, WJetsHT600to800_2018, WJetsHT800to1200_2018, WJetsHT1200to2500_2018, WJetsHT2500toInf_2018]

#QCD

QCDHT_50to100_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_50to100_2018")
QCDHT_50to100_2018.sigma = 0 #347700 #pb
QCDHT_50to100_2018.year = 2018
QCDHT_50to100_2018.dataset = "/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_100to200_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_100to200_2018")
QCDHT_100to200_2018.sigma = 27990000#0 #347700 #pb
QCDHT_100to200_2018.year = 2018
QCDHT_100to200_2018.dataset = "/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_200to300_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_200to300_2018")
QCDHT_200to300_2018.sigma = 1712000 #347700 #pb
QCDHT_200to300_2018.year = 2018
QCDHT_200to300_2018.dataset = "/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_300to500_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_300to500_2018")
QCDHT_300to500_2018.sigma = 347700 #pb
QCDHT_300to500_2018.year = 2018
QCDHT_300to500_2018.dataset = "/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_500to700_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_500to700_2018")
QCDHT_500to700_2018.sigma = 32100 #pb
QCDHT_500to700_2018.year = 2018
QCDHT_500to700_2018.dataset = "/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_700to1000_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_700to1000_2018")
QCDHT_700to1000_2018.sigma = 6831 #pb
QCDHT_700to1000_2018.year = 2018
QCDHT_700to1000_2018.dataset = "/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_1000to1500_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1000to1500_2018")
QCDHT_1000to1500_2018.sigma = 1207 #pb
QCDHT_1000to1500_2018.year = 2018
QCDHT_1000to1500_2018.dataset = "/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_1500to2000_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_1500to2000_2018")
QCDHT_1500to2000_2018.sigma = 119.9 #pb
QCDHT_1500to2000_2018.year = 2018
QCDHT_1500to2000_2018.dataset = "/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCDHT_2000toInf_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCDHT_2000toInf_2018")
QCDHT_2000toInf_2018.sigma = 25.24 #pb
QCDHT_2000toInf_2018.year = 2018
QCDHT_2000toInf_2018.dataset = "/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/"+tag_2018+"-v1/NANOAODSIM"

QCD_2018 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2018")
QCD_2018.year = 2018
QCD_2018.components = [QCDHT_100to200_2018,QCDHT_200to300_2018,QCDHT_300to500_2018, QCDHT_500to700_2018, QCDHT_700to1000_2018, QCDHT_1000to1500_2018, QCDHT_1500to2000_2018, QCDHT_2000toInf_2018]

#ST
ST_tch_t_2018 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_t_2018")
ST_tch_t_2018.sigma =  136.02 #pb
ST_tch_t_2018.year = 2018
ST_tch_t_2018.dataset = "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2018+"-v1/NANOAODSIM"

ST_tch_tbar_2018 = sample(ROOT.kYellow, 1, 1001, "ST t-ch", "ST_tch_tbar_2018")
ST_tch_tbar_2018.sigma =  80.95 #pb
ST_tch_tbar_2018.year = 2018
ST_tch_tbar_2018.dataset = "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/"+tag_2018+"-v1/NANOAODSIM"

ST_tW_t_2018 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_t_2018")
ST_tW_t_2018.sigma =  71.7/2 #pb
ST_tW_t_2018.year = 2018
ST_tW_t_2018.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v2/NANOAODSIM"

ST_tW_tbar_2018 = sample(ROOT.kYellow, 1, 1001, "ST tW", "ST_tW_tbar_2018")
ST_tW_tbar_2018.sigma = 71.7/2 #pb
ST_tW_tbar_2018.year = 2018
ST_tW_tbar_2018.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/"+tag_2018+"-v2/NANOAODSIM"

ST_sch_2018 = sample(ROOT.kYellow, 1, 1001, "ST s-ch", "ST_sch_2018")
ST_sch_2018.sigma = 10.32*0.324 #pb
ST_sch_2018.year = 2018
ST_sch_2018.dataset = "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/"+tag_2018+"-v1/NANOAODSIM"

ST_2018 = sample(ROOT.kYellow, 1, 1001, "Single top", "ST_2018")
ST_2018.year = 2018
ST_2018.components = [ST_tch_t_2018, ST_tch_tbar_2018, ST_tW_t_2018, ST_tW_tbar_2018, ST_sch_2018]

#signal

Tprime_tHq_600LH_2018 = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2018")
Tprime_tHq_600LH_2018.sigma = 0.07453 
Tprime_tHq_600LH_2018.year = 2018
Tprime_tHq_600LH_2018.dataset="/TprimeBToTH_M-600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_700LH_2018 = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2018")
Tprime_tHq_700LH_2018.sigma = 88.107/1000. #to be changed
Tprime_tHq_700LH_2018.year = 2018
Tprime_tHq_700LH_2018.dataset="/TprimeBToTH_M-700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_800LH_2018 = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2018")
Tprime_tHq_800LH_2018.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2018.year = 2018
Tprime_tHq_800LH_2018.dataset="/TprimeBToTH_M-800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_900LH_2018 = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2018")
Tprime_tHq_900LH_2018.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2018.year = 2018
Tprime_tHq_900LH_2018.dataset="/TprimeBToTH_M-900_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1000LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2018")
Tprime_tHq_1000LH_2018.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2018.year = 2018
Tprime_tHq_1000LH_2018.dataset="/TprimeBToTH_M-1000_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1100LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2018")
Tprime_tHq_1100LH_2018.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2018.year = 2018
Tprime_tHq_1100LH_2018.dataset="/TprimeBToTH_M-1100_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1200LH_2018 = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2018")
Tprime_tHq_1200LH_2018.sigma = 0.01973
Tprime_tHq_1200LH_2018.year = 2018
Tprime_tHq_1200LH_2018.dataset="/TprimeBToTH_M-1200_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1300LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2018")
Tprime_tHq_1300LH_2018.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2018.year = 2018
Tprime_tHq_1300LH_2018.dataset="/TprimeBToTH_M-1300_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1400LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2018")
Tprime_tHq_1400LH_2018.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2018.year = 2018
Tprime_tHq_1400LH_2018.dataset="/TprimeBToTH_M-1400_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1500LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2018")
Tprime_tHq_1500LH_2018.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2018.year = 2018
Tprime_tHq_1500LH_2018.dataset="/TprimeBToTH_M-1500_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1600LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2018")
Tprime_tHq_1600LH_2018.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2018.year = 2018
Tprime_tHq_1600LH_2018.dataset="/TprimeBToTH_M-1600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1700LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2018")
Tprime_tHq_1700LH_2018.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2018.year = 2018
Tprime_tHq_1700LH_2018.dataset="/TprimeBToTH_M-1700_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tHq_1800LH_2018 = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2018")
Tprime_tHq_1800LH_2018.sigma = 0.005829
Tprime_tHq_1800LH_2018.year = 2018
Tprime_tHq_1800LH_2018.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2018")
Tprime_LH_2018.year = 2018
Tprime_LH_2018.components = [Tprime_tHq_600LH_2018,Tprime_tHq_700LH_2018,Tprime_tHq_800LH_2018,Tprime_tHq_900LH_2018,Tprime_tHq_1000LH_2018,Tprime_tHq_1100LH_2018,Tprime_tHq_1200LH_2018,Tprime_tHq_1300LH_2018,Tprime_tHq_1400LH_2018,Tprime_tHq_1500LH_2018,Tprime_tHq_1600LH_2018,Tprime_tHq_1700LH_2018,Tprime_tHq_1800LH_2018]

#Data
DataMuA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuA_2018")
DataMuA_2018.runP = 'A'
DataMuA_2018.year = 2018
DataMuA_2018.dataset = '/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD' #'/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'#'/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD'

DataMuB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuB_2018")
DataMuB_2018.runP = 'B'
DataMuB_2018.year = 2018
DataMuB_2018.dataset = '/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataMuC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuC_2018")
DataMuC_2018.runP = 'C'
DataMuC_2018.year = 2018
DataMuC_2018.dataset = '/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'

DataMuD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMuD_2018")
DataMuD_2018.runP = 'D'
DataMuD_2018.year = 2018
DataMuD_2018.dataset = '/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'

DataMu_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataMu_2018")
DataMu_2018.year = 2018
DataMu_2018.components = [DataMuA_2018,DataMuB_2018,DataMuC_2018,DataMuD_2018]#DataMuA_2018,

DataEleA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleA_2018")
DataEleA_2018.runP = 'A'
DataEleA_2018.year = 2018
DataEleA_2018.dataset = '/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleB_2018")
DataEleB_2018.runP = 'B'
DataEleB_2018.year = 2018
DataEleB_2018.dataset = '/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleC_2018")
DataEleC_2018.runP = 'C'
DataEleC_2018.year = 2018
DataEleC_2018.dataset = '/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataEleD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEleD_2018")
DataEleD_2018.runP = 'D'
DataEleD_2018.year = 2018
DataEleD_2018.dataset = '/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD'
DataEle_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataEle_2018")
DataEle_2018.year = 2018
DataEle_2018.components = [DataEleA_2018, DataEleB_2018, DataEleC_2018, DataEleD_2018]

DataHTA_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTA_2018")
DataHTA_2018.runP = 'A'
DataHTA_2018.year = 2018
DataHTA_2018.dataset = '/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataHTB_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTB_2018")
DataHTB_2018.runP = 'B'
DataHTB_2018.year = 2018
DataHTB_2018.dataset = '/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataHTC_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTC_2018")
DataHTC_2018.runP = 'C'
DataHTC_2018.year = 2018
DataHTC_2018.dataset = '/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD'
DataHTD_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHTD_2018")
DataHTD_2018.runP = 'D'
DataHTD_2018.year = 2018
DataHTD_2018.dataset = '/JetHT/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD'
DataHT_2018 = sample(ROOT.kBlack, 1, 1001, "Data", "DataHT_2018")
DataHT_2018.year = 2018
DataHT_2018.components = [DataHTA_2018, DataHTB_2018, DataHTC_2018, DataHTD_2018]


### T tAq signal samples ####

### 2016pre ####

# MT=600
Tprime_tAq_600_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH25_LH_2016preVFP")
Tprime_tAq_600_MH25_LH_2016preVFP.sigma  = 0.0002903
Tprime_tAq_600_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH50_LH_2016preVFP")
Tprime_tAq_600_MH50_LH_2016preVFP.sigma  = 0.0006855
Tprime_tAq_600_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH75_LH_2016preVFP")
Tprime_tAq_600_MH75_LH_2016preVFP.sigma  = 0.001038
Tprime_tAq_600_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH100_LH_2016preVFP")
Tprime_tAq_600_MH100_LH_2016preVFP.sigma  = 0.001359
Tprime_tAq_600_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH125_LH_2016preVFP")
Tprime_tAq_600_MH125_LH_2016preVFP.sigma  = 0.001647
Tprime_tAq_600_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH150_LH_2016preVFP")
Tprime_tAq_600_MH150_LH_2016preVFP.sigma  = 0.00189
Tprime_tAq_600_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH175_LH_2016preVFP")
Tprime_tAq_600_MH175_LH_2016preVFP.sigma  = 0.002103
Tprime_tAq_600_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH200_LH_2016preVFP")
Tprime_tAq_600_MH200_LH_2016preVFP.sigma  = 0.002245
Tprime_tAq_600_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH250_LH_2016preVFP")
Tprime_tAq_600_MH250_LH_2016preVFP.sigma  = 0.002365
Tprime_tAq_600_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH350_LH_2016preVFP")
Tprime_tAq_600_MH350_LH_2016preVFP.sigma  = 0.00181
Tprime_tAq_600_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH450_LH_2016preVFP")
Tprime_tAq_600_MH450_LH_2016preVFP.sigma  = 1.525e-05
Tprime_tAq_600_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH500_LH_2016preVFP")
Tprime_tAq_600_MH500_LH_2016preVFP.sigma  = 8.808e-08
Tprime_tAq_600_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_600_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=700
Tprime_tAq_700_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH25_LH_2016preVFP")
Tprime_tAq_700_MH25_LH_2016preVFP.sigma  = 0.0002274
Tprime_tAq_700_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH50_LH_2016preVFP")
Tprime_tAq_700_MH50_LH_2016preVFP.sigma  = 0.0005375
Tprime_tAq_700_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH75_LH_2016preVFP")
Tprime_tAq_700_MH75_LH_2016preVFP.sigma  = 0.0008201
Tprime_tAq_700_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH100_LH_2016preVFP")
Tprime_tAq_700_MH100_LH_2016preVFP.sigma  = 0.001083
Tprime_tAq_700_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH125_LH_2016preVFP")
Tprime_tAq_700_MH125_LH_2016preVFP.sigma  = 0.001327
Tprime_tAq_700_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH150_LH_2016preVFP")
Tprime_tAq_700_MH150_LH_2016preVFP.sigma  = 0.001547
Tprime_tAq_700_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH175_LH_2016preVFP")
Tprime_tAq_700_MH175_LH_2016preVFP.sigma  = 0.00174
Tprime_tAq_700_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH200_LH_2016preVFP")
Tprime_tAq_700_MH200_LH_2016preVFP.sigma  = 0.001907
Tprime_tAq_700_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH250_LH_2016preVFP")
Tprime_tAq_700_MH250_LH_2016preVFP.sigma  = 0.002135
Tprime_tAq_700_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH350_LH_2016preVFP")
Tprime_tAq_700_MH350_LH_2016preVFP.sigma  = 0.002099
Tprime_tAq_700_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH450_LH_2016preVFP")
Tprime_tAq_700_MH450_LH_2016preVFP.sigma  = 0.001408
Tprime_tAq_700_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH500_LH_2016preVFP")
Tprime_tAq_700_MH500_LH_2016preVFP.sigma  = 0.0007664
Tprime_tAq_700_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_700_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=800
Tprime_tAq_800_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH25_LH_2016preVFP")
Tprime_tAq_800_MH25_LH_2016preVFP.sigma  = 0.0001764
Tprime_tAq_800_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH50_LH_2016preVFP")
Tprime_tAq_800_MH50_LH_2016preVFP.sigma  = 0.0004184
Tprime_tAq_800_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH75_LH_2016preVFP")
Tprime_tAq_800_MH75_LH_2016preVFP.sigma  = 0.0006423
Tprime_tAq_800_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH100_LH_2016preVFP")
Tprime_tAq_800_MH100_LH_2016preVFP.sigma  = 0.0008548
Tprime_tAq_800_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH125_LH_2016preVFP")
Tprime_tAq_800_MH125_LH_2016preVFP.sigma  = 0.001053
Tprime_tAq_800_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH150_LH_2016preVFP")
Tprime_tAq_800_MH150_LH_2016preVFP.sigma  = 0.001241
Tprime_tAq_800_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH175_LH_2016preVFP")
Tprime_tAq_800_MH175_LH_2016preVFP.sigma  = 0.001409
Tprime_tAq_800_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH200_LH_2016preVFP")
Tprime_tAq_800_MH200_LH_2016preVFP.sigma  = 0.001558
Tprime_tAq_800_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH250_LH_2016preVFP")
Tprime_tAq_800_MH250_LH_2016preVFP.sigma  = 0.001809
Tprime_tAq_800_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH350_LH_2016preVFP")
Tprime_tAq_800_MH350_LH_2016preVFP.sigma  = 0.00199
Tprime_tAq_800_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH450_LH_2016preVFP")
Tprime_tAq_800_MH450_LH_2016preVFP.sigma  = 0.001746
Tprime_tAq_800_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH500_LH_2016preVFP")
Tprime_tAq_800_MH500_LH_2016preVFP.sigma  = 0.00146
Tprime_tAq_800_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_800_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=900
Tprime_tAq_900_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH25_LH_2016preVFP")
Tprime_tAq_900_MH25_LH_2016preVFP.sigma  = 0.0001424
Tprime_tAq_900_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH50_LH_2016preVFP")
Tprime_tAq_900_MH50_LH_2016preVFP.sigma  = 0.0003344
Tprime_tAq_900_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH75_LH_2016preVFP")
Tprime_tAq_900_MH75_LH_2016preVFP.sigma  = 0.0005126
Tprime_tAq_900_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH100_LH_2016preVFP")
Tprime_tAq_900_MH100_LH_2016preVFP.sigma  = 0.0006827
Tprime_tAq_900_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH125_LH_2016preVFP")
Tprime_tAq_900_MH125_LH_2016preVFP.sigma  = 0.0008462
Tprime_tAq_900_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH150_LH_2016preVFP")
Tprime_tAq_900_MH150_LH_2016preVFP.sigma  = 0.0009996
Tprime_tAq_900_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH175_LH_2016preVFP")
Tprime_tAq_900_MH175_LH_2016preVFP.sigma  = 0.001149
Tprime_tAq_900_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH200_LH_2016preVFP")
Tprime_tAq_900_MH200_LH_2016preVFP.sigma  = 0.001273
Tprime_tAq_900_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH250_LH_2016preVFP")
Tprime_tAq_900_MH250_LH_2016preVFP.sigma  = 0.001497
Tprime_tAq_900_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH350_LH_2016preVFP")
Tprime_tAq_900_MH350_LH_2016preVFP.sigma  = 0.001763
Tprime_tAq_900_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH450_LH_2016preVFP")
Tprime_tAq_900_MH450_LH_2016preVFP.sigma  = 0.001734
Tprime_tAq_900_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH500_LH_2016preVFP")
Tprime_tAq_900_MH500_LH_2016preVFP.sigma  = 0.001604
Tprime_tAq_900_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_900_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1000
Tprime_tAq_1000_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH25_LH_2016preVFP")
Tprime_tAq_1000_MH25_LH_2016preVFP.sigma  = 0.0001116
Tprime_tAq_1000_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH50_LH_2016preVFP")
Tprime_tAq_1000_MH50_LH_2016preVFP.sigma  = 0.0002655
Tprime_tAq_1000_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH75_LH_2016preVFP")
Tprime_tAq_1000_MH75_LH_2016preVFP.sigma  = 0.0004078
Tprime_tAq_1000_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH100_LH_2016preVFP")
Tprime_tAq_1000_MH100_LH_2016preVFP.sigma  = 0.0005434
Tprime_tAq_1000_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH125_LH_2016preVFP")
Tprime_tAq_1000_MH125_LH_2016preVFP.sigma  = 0.0006745
Tprime_tAq_1000_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH150_LH_2016preVFP")
Tprime_tAq_1000_MH150_LH_2016preVFP.sigma  = 0.0007994
Tprime_tAq_1000_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH175_LH_2016preVFP")
Tprime_tAq_1000_MH175_LH_2016preVFP.sigma  = 0.0009197
Tprime_tAq_1000_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH200_LH_2016preVFP")
Tprime_tAq_1000_MH200_LH_2016preVFP.sigma  = 0.001031
Tprime_tAq_1000_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH250_LH_2016preVFP")
Tprime_tAq_1000_MH250_LH_2016preVFP.sigma  = 0.001227
Tprime_tAq_1000_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH350_LH_2016preVFP")
Tprime_tAq_1000_MH350_LH_2016preVFP.sigma  = 0.001513
Tprime_tAq_1000_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH450_LH_2016preVFP")
Tprime_tAq_1000_MH450_LH_2016preVFP.sigma  = 0.001575
Tprime_tAq_1000_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH500_LH_2016preVFP")
Tprime_tAq_1000_MH500_LH_2016preVFP.sigma  = 0.001544
Tprime_tAq_1000_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1000_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1100
Tprime_tAq_1100_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH25_LH_2016preVFP")
Tprime_tAq_1100_MH25_LH_2016preVFP.sigma  = 8.915e-05
Tprime_tAq_1100_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH50_LH_2016preVFP")
Tprime_tAq_1100_MH50_LH_2016preVFP.sigma  = 0.0002115
Tprime_tAq_1100_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH75_LH_2016preVFP")
Tprime_tAq_1100_MH75_LH_2016preVFP.sigma  = 0.0003253
Tprime_tAq_1100_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH100_LH_2016preVFP")
Tprime_tAq_1100_MH100_LH_2016preVFP.sigma  = 0.0004356
Tprime_tAq_1100_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH125_LH_2016preVFP")
Tprime_tAq_1100_MH125_LH_2016preVFP.sigma  = 0.0005412
Tprime_tAq_1100_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH150_LH_2016preVFP")
Tprime_tAq_1100_MH150_LH_2016preVFP.sigma  = 0.0006435
Tprime_tAq_1100_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH175_LH_2016preVFP")
Tprime_tAq_1100_MH175_LH_2016preVFP.sigma  = 0.0007414
Tprime_tAq_1100_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH200_LH_2016preVFP")
Tprime_tAq_1100_MH200_LH_2016preVFP.sigma  = 0.0008344
Tprime_tAq_1100_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH250_LH_2016preVFP")
Tprime_tAq_1100_MH250_LH_2016preVFP.sigma  = 0.001003
Tprime_tAq_1100_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH350_LH_2016preVFP")
Tprime_tAq_1100_MH350_LH_2016preVFP.sigma  = 0.001263
Tprime_tAq_1100_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH450_LH_2016preVFP")
Tprime_tAq_1100_MH450_LH_2016preVFP.sigma  = 0.001382
Tprime_tAq_1100_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH500_LH_2016preVFP")
Tprime_tAq_1100_MH500_LH_2016preVFP.sigma  = 0.001396
Tprime_tAq_1100_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1100_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1200
Tprime_tAq_1200_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH25_LH_2016preVFP")
Tprime_tAq_1200_MH25_LH_2016preVFP.sigma  = 7.205e-05
Tprime_tAq_1200_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH50_LH_2016preVFP")
Tprime_tAq_1200_MH50_LH_2016preVFP.sigma  = 0.0001711
Tprime_tAq_1200_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH75_LH_2016preVFP")
Tprime_tAq_1200_MH75_LH_2016preVFP.sigma  = 0.0002633
Tprime_tAq_1200_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH100_LH_2016preVFP")
Tprime_tAq_1200_MH100_LH_2016preVFP.sigma  = 0.0003525
Tprime_tAq_1200_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH125_LH_2016preVFP")
Tprime_tAq_1200_MH125_LH_2016preVFP.sigma  = 0.0004401
Tprime_tAq_1200_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH150_LH_2016preVFP")
Tprime_tAq_1200_MH150_LH_2016preVFP.sigma  = 0.0005238
Tprime_tAq_1200_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH175_LH_2016preVFP")
Tprime_tAq_1200_MH175_LH_2016preVFP.sigma  = 0.0006072
Tprime_tAq_1200_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH200_LH_2016preVFP")
Tprime_tAq_1200_MH200_LH_2016preVFP.sigma  = 0.0006849
Tprime_tAq_1200_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH250_LH_2016preVFP")
Tprime_tAq_1200_MH250_LH_2016preVFP.sigma  = 0.0008286
Tprime_tAq_1200_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH350_LH_2016preVFP")
Tprime_tAq_1200_MH350_LH_2016preVFP.sigma  = 0.001061
Tprime_tAq_1200_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH450_LH_2016preVFP")
Tprime_tAq_1200_MH450_LH_2016preVFP.sigma  = 0.001187
Tprime_tAq_1200_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH500_LH_2016preVFP")
Tprime_tAq_1200_MH500_LH_2016preVFP.sigma  = 0.001218
Tprime_tAq_1200_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1200_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1300
Tprime_tAq_1300_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH25_LH_2016preVFP")
Tprime_tAq_1300_MH25_LH_2016preVFP.sigma  = 5.836e-05
Tprime_tAq_1300_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH50_LH_2016preVFP")
Tprime_tAq_1300_MH50_LH_2016preVFP.sigma  = 0.0001387
Tprime_tAq_1300_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH75_LH_2016preVFP")
Tprime_tAq_1300_MH75_LH_2016preVFP.sigma  = 0.0002136
Tprime_tAq_1300_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH100_LH_2016preVFP")
Tprime_tAq_1300_MH100_LH_2016preVFP.sigma  = 0.0002862
Tprime_tAq_1300_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH125_LH_2016preVFP")
Tprime_tAq_1300_MH125_LH_2016preVFP.sigma  = 0.0003573
Tprime_tAq_1300_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH150_LH_2016preVFP")
Tprime_tAq_1300_MH150_LH_2016preVFP.sigma  = 0.0004262
Tprime_tAq_1300_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH175_LH_2016preVFP")
Tprime_tAq_1300_MH175_LH_2016preVFP.sigma  = 0.0004933
Tprime_tAq_1300_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH200_LH_2016preVFP")
Tprime_tAq_1300_MH200_LH_2016preVFP.sigma  = 0.0005579
Tprime_tAq_1300_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH250_LH_2016preVFP")
Tprime_tAq_1300_MH250_LH_2016preVFP.sigma  = 0.000678
Tprime_tAq_1300_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH350_LH_2016preVFP")
Tprime_tAq_1300_MH350_LH_2016preVFP.sigma  = 0.0008797
Tprime_tAq_1300_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH450_LH_2016preVFP")
Tprime_tAq_1300_MH450_LH_2016preVFP.sigma  = 0.001014
Tprime_tAq_1300_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH500_LH_2016preVFP")
Tprime_tAq_1300_MH500_LH_2016preVFP.sigma  = 0.001051
Tprime_tAq_1300_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1300_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1400
Tprime_tAq_1400_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH25_LH_2016preVFP")
Tprime_tAq_1400_MH25_LH_2016preVFP.sigma  = 4.705e-05
Tprime_tAq_1400_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH50_LH_2016preVFP")
Tprime_tAq_1400_MH50_LH_2016preVFP.sigma  = 0.0001119
Tprime_tAq_1400_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH75_LH_2016preVFP")
Tprime_tAq_1400_MH75_LH_2016preVFP.sigma  = 0.0001724
Tprime_tAq_1400_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH100_LH_2016preVFP")
Tprime_tAq_1400_MH100_LH_2016preVFP.sigma  = 0.0002309
Tprime_tAq_1400_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH125_LH_2016preVFP")
Tprime_tAq_1400_MH125_LH_2016preVFP.sigma  = 0.0002881
Tprime_tAq_1400_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH150_LH_2016preVFP")
Tprime_tAq_1400_MH150_LH_2016preVFP.sigma  = 0.0003442
Tprime_tAq_1400_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH175_LH_2016preVFP")
Tprime_tAq_1400_MH175_LH_2016preVFP.sigma  = 0.0004004
Tprime_tAq_1400_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH200_LH_2016preVFP")
Tprime_tAq_1400_MH200_LH_2016preVFP.sigma  = 0.0004536
Tprime_tAq_1400_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH250_LH_2016preVFP")
Tprime_tAq_1400_MH250_LH_2016preVFP.sigma  = 0.0005538
Tprime_tAq_1400_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH350_LH_2016preVFP")
Tprime_tAq_1400_MH350_LH_2016preVFP.sigma  = 0.0007273
Tprime_tAq_1400_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH450_LH_2016preVFP")
Tprime_tAq_1400_MH450_LH_2016preVFP.sigma  = 0.0008543
Tprime_tAq_1400_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH500_LH_2016preVFP")
Tprime_tAq_1400_MH500_LH_2016preVFP.sigma  = 0.0008969
Tprime_tAq_1400_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1400_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1500
Tprime_tAq_1500_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH25_LH_2016preVFP")
Tprime_tAq_1500_MH25_LH_2016preVFP.sigma  = 3.827e-05
Tprime_tAq_1500_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH50_LH_2016preVFP")
Tprime_tAq_1500_MH50_LH_2016preVFP.sigma  = 9.102e-05
Tprime_tAq_1500_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH75_LH_2016preVFP")
Tprime_tAq_1500_MH75_LH_2016preVFP.sigma  = 0.0001403
Tprime_tAq_1500_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH100_LH_2016preVFP")
Tprime_tAq_1500_MH100_LH_2016preVFP.sigma  = 0.0001883
Tprime_tAq_1500_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH125_LH_2016preVFP")
Tprime_tAq_1500_MH125_LH_2016preVFP.sigma  = 0.0002353
Tprime_tAq_1500_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH150_LH_2016preVFP")
Tprime_tAq_1500_MH150_LH_2016preVFP.sigma  = 0.0002808
Tprime_tAq_1500_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH175_LH_2016preVFP")
Tprime_tAq_1500_MH175_LH_2016preVFP.sigma  = 0.0003257
Tprime_tAq_1500_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH200_LH_2016preVFP")
Tprime_tAq_1500_MH200_LH_2016preVFP.sigma  = 0.0003694
Tprime_tAq_1500_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH250_LH_2016preVFP")
Tprime_tAq_1500_MH250_LH_2016preVFP.sigma  = 0.0004541
Tprime_tAq_1500_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH350_LH_2016preVFP")
Tprime_tAq_1500_MH350_LH_2016preVFP.sigma  = 0.0006032
Tprime_tAq_1500_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH450_LH_2016preVFP")
Tprime_tAq_1500_MH450_LH_2016preVFP.sigma  = 0.0007173
Tprime_tAq_1500_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH500_LH_2016preVFP")
Tprime_tAq_1500_MH500_LH_2016preVFP.sigma  = 0.0007597
Tprime_tAq_1500_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1500_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1600
Tprime_tAq_1600_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH25_LH_2016preVFP")
Tprime_tAq_1600_MH25_LH_2016preVFP.sigma  = 3.119e-05
Tprime_tAq_1600_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH50_LH_2016preVFP")
Tprime_tAq_1600_MH50_LH_2016preVFP.sigma  = 7.417e-05
Tprime_tAq_1600_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH75_LH_2016preVFP")
Tprime_tAq_1600_MH75_LH_2016preVFP.sigma  = 0.0001144
Tprime_tAq_1600_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH100_LH_2016preVFP")
Tprime_tAq_1600_MH100_LH_2016preVFP.sigma  = 0.0001536
Tprime_tAq_1600_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH125_LH_2016preVFP")
Tprime_tAq_1600_MH125_LH_2016preVFP.sigma  = 0.0001921
Tprime_tAq_1600_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH150_LH_2016preVFP")
Tprime_tAq_1600_MH150_LH_2016preVFP.sigma  = 0.0002298
Tprime_tAq_1600_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH175_LH_2016preVFP")
Tprime_tAq_1600_MH175_LH_2016preVFP.sigma  = 0.0002668
Tprime_tAq_1600_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH200_LH_2016preVFP")
Tprime_tAq_1600_MH200_LH_2016preVFP.sigma  = 0.0003029
Tprime_tAq_1600_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH250_LH_2016preVFP")
Tprime_tAq_1600_MH250_LH_2016preVFP.sigma  = 0.0003721
Tprime_tAq_1600_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH350_LH_2016preVFP")
Tprime_tAq_1600_MH350_LH_2016preVFP.sigma  = 0.0004956
Tprime_tAq_1600_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH450_LH_2016preVFP")
Tprime_tAq_1600_MH450_LH_2016preVFP.sigma  = 0.0005936
Tprime_tAq_1600_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH500_LH_2016preVFP")
Tprime_tAq_1600_MH500_LH_2016preVFP.sigma  = 0.0006336
Tprime_tAq_1600_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1600_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1700
Tprime_tAq_1700_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH25_LH_2016preVFP")
Tprime_tAq_1700_MH25_LH_2016preVFP.sigma  = 2.541e-05
Tprime_tAq_1700_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH50_LH_2016preVFP")
Tprime_tAq_1700_MH50_LH_2016preVFP.sigma  = 6.043e-05
Tprime_tAq_1700_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH75_LH_2016preVFP")
Tprime_tAq_1700_MH75_LH_2016preVFP.sigma  = 9.323e-05
Tprime_tAq_1700_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH100_LH_2016preVFP")
Tprime_tAq_1700_MH100_LH_2016preVFP.sigma  = 0.0001252
Tprime_tAq_1700_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH125_LH_2016preVFP")
Tprime_tAq_1700_MH125_LH_2016preVFP.sigma  = 0.0001567
Tprime_tAq_1700_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH150_LH_2016preVFP")
Tprime_tAq_1700_MH150_LH_2016preVFP.sigma  = 0.0001876
Tprime_tAq_1700_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH175_LH_2016preVFP")
Tprime_tAq_1700_MH175_LH_2016preVFP.sigma  = 0.0002178
Tprime_tAq_1700_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH200_LH_2016preVFP")
Tprime_tAq_1700_MH200_LH_2016preVFP.sigma  = 0.0002476
Tprime_tAq_1700_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH250_LH_2016preVFP")
Tprime_tAq_1700_MH250_LH_2016preVFP.sigma  = 0.0003049
Tprime_tAq_1700_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH350_LH_2016preVFP")
Tprime_tAq_1700_MH350_LH_2016preVFP.sigma  = 0.0004092
Tprime_tAq_1700_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH450_LH_2016preVFP")
Tprime_tAq_1700_MH450_LH_2016preVFP.sigma  = 0.0004959
Tprime_tAq_1700_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH500_LH_2016preVFP")
Tprime_tAq_1700_MH500_LH_2016preVFP.sigma  = 0.0005317
Tprime_tAq_1700_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1700_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1800
Tprime_tAq_1800_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH25_LH_2016preVFP")
Tprime_tAq_1800_MH25_LH_2016preVFP.sigma  = 2.076e-05
Tprime_tAq_1800_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH50_LH_2016preVFP")
Tprime_tAq_1800_MH50_LH_2016preVFP.sigma  = 4.931e-05
Tprime_tAq_1800_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH75_LH_2016preVFP")
Tprime_tAq_1800_MH75_LH_2016preVFP.sigma  = 7.608e-05
Tprime_tAq_1800_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH100_LH_2016preVFP")
Tprime_tAq_1800_MH100_LH_2016preVFP.sigma  = 0.0001022
Tprime_tAq_1800_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH125_LH_2016preVFP")
Tprime_tAq_1800_MH125_LH_2016preVFP.sigma  = 0.000128
Tprime_tAq_1800_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH150_LH_2016preVFP")
Tprime_tAq_1800_MH150_LH_2016preVFP.sigma  = 0.0001533
Tprime_tAq_1800_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH175_LH_2016preVFP")
Tprime_tAq_1800_MH175_LH_2016preVFP.sigma  = 0.0001782
Tprime_tAq_1800_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH200_LH_2016preVFP")
Tprime_tAq_1800_MH200_LH_2016preVFP.sigma  = 0.0002026
Tprime_tAq_1800_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH250_LH_2016preVFP")
Tprime_tAq_1800_MH250_LH_2016preVFP.sigma  = 0.00025
Tprime_tAq_1800_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH350_LH_2016preVFP")
Tprime_tAq_1800_MH350_LH_2016preVFP.sigma  = 0.0003371
Tprime_tAq_1800_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH450_LH_2016preVFP")
Tprime_tAq_1800_MH450_LH_2016preVFP.sigma  = 0.0004113
Tprime_tAq_1800_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH500_LH_2016preVFP")
Tprime_tAq_1800_MH500_LH_2016preVFP.sigma  = 0.0004428
Tprime_tAq_1800_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1800_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=1900
Tprime_tAq_1900_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH25_LH_2016preVFP")
Tprime_tAq_1900_MH25_LH_2016preVFP.sigma  = 1.696e-05
Tprime_tAq_1900_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH50_LH_2016preVFP")
Tprime_tAq_1900_MH50_LH_2016preVFP.sigma  = 4.037e-05
Tprime_tAq_1900_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH75_LH_2016preVFP")
Tprime_tAq_1900_MH75_LH_2016preVFP.sigma  = 6.23e-05
Tprime_tAq_1900_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH100_LH_2016preVFP")
Tprime_tAq_1900_MH100_LH_2016preVFP.sigma  = 8.373e-05
Tprime_tAq_1900_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH125_LH_2016preVFP")
Tprime_tAq_1900_MH125_LH_2016preVFP.sigma  = 0.0001048
Tprime_tAq_1900_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH150_LH_2016preVFP")
Tprime_tAq_1900_MH150_LH_2016preVFP.sigma  = 0.0001257
Tprime_tAq_1900_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH175_LH_2016preVFP")
Tprime_tAq_1900_MH175_LH_2016preVFP.sigma  = 0.0001461
Tprime_tAq_1900_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH200_LH_2016preVFP")
Tprime_tAq_1900_MH200_LH_2016preVFP.sigma  = 0.0001662
Tprime_tAq_1900_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH250_LH_2016preVFP")
Tprime_tAq_1900_MH250_LH_2016preVFP.sigma  = 0.0002061
Tprime_tAq_1900_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH350_LH_2016preVFP")
Tprime_tAq_1900_MH350_LH_2016preVFP.sigma  = 0.0002791
Tprime_tAq_1900_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH450_LH_2016preVFP")
Tprime_tAq_1900_MH450_LH_2016preVFP.sigma  = 0.000341
Tprime_tAq_1900_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH500_LH_2016preVFP")
Tprime_tAq_1900_MH500_LH_2016preVFP.sigma  = 0.0003716
Tprime_tAq_1900_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_1900_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2000
Tprime_tAq_2000_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH25_LH_2016preVFP")
Tprime_tAq_2000_MH25_LH_2016preVFP.sigma  = 1.39e-05
Tprime_tAq_2000_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH50_LH_2016preVFP")
Tprime_tAq_2000_MH50_LH_2016preVFP.sigma  = 3.308e-05
Tprime_tAq_2000_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH75_LH_2016preVFP")
Tprime_tAq_2000_MH75_LH_2016preVFP.sigma  = 5.107e-05
Tprime_tAq_2000_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH100_LH_2016preVFP")
Tprime_tAq_2000_MH100_LH_2016preVFP.sigma  = 6.868e-05
Tprime_tAq_2000_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH125_LH_2016preVFP")
Tprime_tAq_2000_MH125_LH_2016preVFP.sigma  = 8.602e-05
Tprime_tAq_2000_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH150_LH_2016preVFP")
Tprime_tAq_2000_MH150_LH_2016preVFP.sigma  = 0.0001031
Tprime_tAq_2000_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH175_LH_2016preVFP")
Tprime_tAq_2000_MH175_LH_2016preVFP.sigma  = 0.00012
Tprime_tAq_2000_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH200_LH_2016preVFP")
Tprime_tAq_2000_MH200_LH_2016preVFP.sigma  = 0.0001367
Tprime_tAq_2000_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH250_LH_2016preVFP")
Tprime_tAq_2000_MH250_LH_2016preVFP.sigma  = 0.000169
Tprime_tAq_2000_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH350_LH_2016preVFP")
Tprime_tAq_2000_MH350_LH_2016preVFP.sigma  = 0.0002297
Tprime_tAq_2000_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH450_LH_2016preVFP")
Tprime_tAq_2000_MH450_LH_2016preVFP.sigma  = 0.0002834
Tprime_tAq_2000_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH500_LH_2016preVFP")
Tprime_tAq_2000_MH500_LH_2016preVFP.sigma  = 0.0003069
Tprime_tAq_2000_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2000_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2100
Tprime_tAq_2100_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH25_LH_2016preVFP")
Tprime_tAq_2100_MH25_LH_2016preVFP.sigma  = 1.143e-05
Tprime_tAq_2100_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH50_LH_2016preVFP")
Tprime_tAq_2100_MH50_LH_2016preVFP.sigma  = 2.715e-05
Tprime_tAq_2100_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH75_LH_2016preVFP")
Tprime_tAq_2100_MH75_LH_2016preVFP.sigma  = 4.193e-05
Tprime_tAq_2100_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH100_LH_2016preVFP")
Tprime_tAq_2100_MH100_LH_2016preVFP.sigma  = 5.637e-05
Tprime_tAq_2100_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH125_LH_2016preVFP")
Tprime_tAq_2100_MH125_LH_2016preVFP.sigma  = 7.061e-05
Tprime_tAq_2100_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH150_LH_2016preVFP")
Tprime_tAq_2100_MH150_LH_2016preVFP.sigma  = 8.467e-05
Tprime_tAq_2100_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH175_LH_2016preVFP")
Tprime_tAq_2100_MH175_LH_2016preVFP.sigma  = 9.855e-05
Tprime_tAq_2100_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH200_LH_2016preVFP")
Tprime_tAq_2100_MH200_LH_2016preVFP.sigma  = 0.0001123
Tprime_tAq_2100_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH250_LH_2016preVFP")
Tprime_tAq_2100_MH250_LH_2016preVFP.sigma  = 0.0001395
Tprime_tAq_2100_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH350_LH_2016preVFP")
Tprime_tAq_2100_MH350_LH_2016preVFP.sigma  = 0.0001904
Tprime_tAq_2100_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH450_LH_2016preVFP")
Tprime_tAq_2100_MH450_LH_2016preVFP.sigma  = 0.0002359
Tprime_tAq_2100_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH500_LH_2016preVFP")
Tprime_tAq_2100_MH500_LH_2016preVFP.sigma  = 0.0002563
Tprime_tAq_2100_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2100_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2200
Tprime_tAq_2200_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH25_LH_2016preVFP")
Tprime_tAq_2200_MH25_LH_2016preVFP.sigma  = 9.434e-06
Tprime_tAq_2200_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH50_LH_2016preVFP")
Tprime_tAq_2200_MH50_LH_2016preVFP.sigma  = 2.246e-05
Tprime_tAq_2200_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH75_LH_2016preVFP")
Tprime_tAq_2200_MH75_LH_2016preVFP.sigma  = 3.467e-05
Tprime_tAq_2200_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH100_LH_2016preVFP")
Tprime_tAq_2200_MH100_LH_2016preVFP.sigma  = 4.672e-05
Tprime_tAq_2200_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH125_LH_2016preVFP")
Tprime_tAq_2200_MH125_LH_2016preVFP.sigma  = 5.855e-05
Tprime_tAq_2200_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH150_LH_2016preVFP")
Tprime_tAq_2200_MH150_LH_2016preVFP.sigma  = 7.027e-05
Tprime_tAq_2200_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH175_LH_2016preVFP")
Tprime_tAq_2200_MH175_LH_2016preVFP.sigma  = 8.19e-05
Tprime_tAq_2200_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH200_LH_2016preVFP")
Tprime_tAq_2200_MH200_LH_2016preVFP.sigma  = 9.334e-05
Tprime_tAq_2200_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH250_LH_2016preVFP")
Tprime_tAq_2200_MH250_LH_2016preVFP.sigma  = 0.0001157
Tprime_tAq_2200_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH350_LH_2016preVFP")
Tprime_tAq_2200_MH350_LH_2016preVFP.sigma  = 0.0001579
Tprime_tAq_2200_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH450_LH_2016preVFP")
Tprime_tAq_2200_MH450_LH_2016preVFP.sigma  = 0.0001955
Tprime_tAq_2200_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH500_LH_2016preVFP")
Tprime_tAq_2200_MH500_LH_2016preVFP.sigma  = 0.0002133
Tprime_tAq_2200_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2200_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2300
Tprime_tAq_2300_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH25_LH_2016preVFP")
Tprime_tAq_2300_MH25_LH_2016preVFP.sigma  = 7.755e-06
Tprime_tAq_2300_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH50_LH_2016preVFP")
Tprime_tAq_2300_MH50_LH_2016preVFP.sigma  = 1.848e-05
Tprime_tAq_2300_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH75_LH_2016preVFP")
Tprime_tAq_2300_MH75_LH_2016preVFP.sigma  = 2.853e-05
Tprime_tAq_2300_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH100_LH_2016preVFP")
Tprime_tAq_2300_MH100_LH_2016preVFP.sigma  = 3.837e-05
Tprime_tAq_2300_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH125_LH_2016preVFP")
Tprime_tAq_2300_MH125_LH_2016preVFP.sigma  = 4.81e-05
Tprime_tAq_2300_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH150_LH_2016preVFP")
Tprime_tAq_2300_MH150_LH_2016preVFP.sigma  = 5.757e-05
Tprime_tAq_2300_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH175_LH_2016preVFP")
Tprime_tAq_2300_MH175_LH_2016preVFP.sigma  = 6.703e-05
Tprime_tAq_2300_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH200_LH_2016preVFP")
Tprime_tAq_2300_MH200_LH_2016preVFP.sigma  = 7.641e-05
Tprime_tAq_2300_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH250_LH_2016preVFP")
Tprime_tAq_2300_MH250_LH_2016preVFP.sigma  = 9.486e-05
Tprime_tAq_2300_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH350_LH_2016preVFP")
Tprime_tAq_2300_MH350_LH_2016preVFP.sigma  = 0.0001299
Tprime_tAq_2300_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH450_LH_2016preVFP")
Tprime_tAq_2300_MH450_LH_2016preVFP.sigma  = 0.0001618
Tprime_tAq_2300_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH500_LH_2016preVFP")
Tprime_tAq_2300_MH500_LH_2016preVFP.sigma  = 0.0001764
Tprime_tAq_2300_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2300_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2400
Tprime_tAq_2400_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH25_LH_2016preVFP")
Tprime_tAq_2400_MH25_LH_2016preVFP.sigma  = 6.361e-06
Tprime_tAq_2400_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH50_LH_2016preVFP")
Tprime_tAq_2400_MH50_LH_2016preVFP.sigma  = 1.515e-05
Tprime_tAq_2400_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH75_LH_2016preVFP")
Tprime_tAq_2400_MH75_LH_2016preVFP.sigma  = 2.34e-05
Tprime_tAq_2400_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH100_LH_2016preVFP")
Tprime_tAq_2400_MH100_LH_2016preVFP.sigma  = 3.148e-05
Tprime_tAq_2400_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH125_LH_2016preVFP")
Tprime_tAq_2400_MH125_LH_2016preVFP.sigma  = 3.946e-05
Tprime_tAq_2400_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH150_LH_2016preVFP")
Tprime_tAq_2400_MH150_LH_2016preVFP.sigma  = 4.736e-05
Tprime_tAq_2400_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH175_LH_2016preVFP")
Tprime_tAq_2400_MH175_LH_2016preVFP.sigma  = 5.519e-05
Tprime_tAq_2400_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH200_LH_2016preVFP")
Tprime_tAq_2400_MH200_LH_2016preVFP.sigma  = 6.293e-05
Tprime_tAq_2400_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH250_LH_2016preVFP")
Tprime_tAq_2400_MH250_LH_2016preVFP.sigma  = 7.813e-05
Tprime_tAq_2400_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH350_LH_2016preVFP")
Tprime_tAq_2400_MH350_LH_2016preVFP.sigma  = 0.0001075
Tprime_tAq_2400_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH450_LH_2016preVFP")
Tprime_tAq_2400_MH450_LH_2016preVFP.sigma  = 0.0001343
Tprime_tAq_2400_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH500_LH_2016preVFP")
Tprime_tAq_2400_MH500_LH_2016preVFP.sigma  = 0.0001467
Tprime_tAq_2400_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2400_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2500
Tprime_tAq_2500_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH25_LH_2016preVFP")
Tprime_tAq_2500_MH25_LH_2016preVFP.sigma  = 5.237e-06
Tprime_tAq_2500_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH50_LH_2016preVFP")
Tprime_tAq_2500_MH50_LH_2016preVFP.sigma  = 1.247e-05
Tprime_tAq_2500_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH75_LH_2016preVFP")
Tprime_tAq_2500_MH75_LH_2016preVFP.sigma  = 1.926e-05
Tprime_tAq_2500_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH100_LH_2016preVFP")
Tprime_tAq_2500_MH100_LH_2016preVFP.sigma  = 2.59e-05
Tprime_tAq_2500_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH125_LH_2016preVFP")
Tprime_tAq_2500_MH125_LH_2016preVFP.sigma  = 3.251e-05
Tprime_tAq_2500_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH150_LH_2016preVFP")
Tprime_tAq_2500_MH150_LH_2016preVFP.sigma  = 3.901e-05
Tprime_tAq_2500_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH175_LH_2016preVFP")
Tprime_tAq_2500_MH175_LH_2016preVFP.sigma  = 4.547e-05
Tprime_tAq_2500_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH200_LH_2016preVFP")
Tprime_tAq_2500_MH200_LH_2016preVFP.sigma  = 5.186e-05
Tprime_tAq_2500_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH250_LH_2016preVFP")
Tprime_tAq_2500_MH250_LH_2016preVFP.sigma  = 6.452e-05
Tprime_tAq_2500_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH350_LH_2016preVFP")
Tprime_tAq_2500_MH350_LH_2016preVFP.sigma  = 8.859e-05
Tprime_tAq_2500_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH450_LH_2016preVFP")
Tprime_tAq_2500_MH450_LH_2016preVFP.sigma  = 0.0001111
Tprime_tAq_2500_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH500_LH_2016preVFP")
Tprime_tAq_2500_MH500_LH_2016preVFP.sigma  = 0.0001215
Tprime_tAq_2500_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2500_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2600
Tprime_tAq_2600_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH25_LH_2016preVFP")
Tprime_tAq_2600_MH25_LH_2016preVFP.sigma  = 4.255e-06
Tprime_tAq_2600_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH50_LH_2016preVFP")
Tprime_tAq_2600_MH50_LH_2016preVFP.sigma  = 1.015e-05
Tprime_tAq_2600_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH75_LH_2016preVFP")
Tprime_tAq_2600_MH75_LH_2016preVFP.sigma  = 1.568e-05
Tprime_tAq_2600_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH100_LH_2016preVFP")
Tprime_tAq_2600_MH100_LH_2016preVFP.sigma  = 2.11e-05
Tprime_tAq_2600_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH125_LH_2016preVFP")
Tprime_tAq_2600_MH125_LH_2016preVFP.sigma  = 2.646e-05
Tprime_tAq_2600_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH150_LH_2016preVFP")
Tprime_tAq_2600_MH150_LH_2016preVFP.sigma  = 3.171e-05
Tprime_tAq_2600_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH175_LH_2016preVFP")
Tprime_tAq_2600_MH175_LH_2016preVFP.sigma  = 3.697e-05
Tprime_tAq_2600_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH200_LH_2016preVFP")
Tprime_tAq_2600_MH200_LH_2016preVFP.sigma  = 4.218e-05
Tprime_tAq_2600_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH250_LH_2016preVFP")
Tprime_tAq_2600_MH250_LH_2016preVFP.sigma  = 5.243e-05
Tprime_tAq_2600_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH350_LH_2016preVFP")
Tprime_tAq_2600_MH350_LH_2016preVFP.sigma  = 7.213e-05
Tprime_tAq_2600_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH450_LH_2016preVFP")
Tprime_tAq_2600_MH450_LH_2016preVFP.sigma  = 9.067e-05
Tprime_tAq_2600_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH500_LH_2016preVFP")
Tprime_tAq_2600_MH500_LH_2016preVFP.sigma  = 9.929e-05
Tprime_tAq_2600_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2600_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2700
Tprime_tAq_2700_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH25_LH_2016preVFP")
Tprime_tAq_2700_MH25_LH_2016preVFP.sigma  = 3.545e-06
Tprime_tAq_2700_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH50_LH_2016preVFP")
Tprime_tAq_2700_MH50_LH_2016preVFP.sigma  = 8.424e-06
Tprime_tAq_2700_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH75_LH_2016preVFP")
Tprime_tAq_2700_MH75_LH_2016preVFP.sigma  = 1.301e-05
Tprime_tAq_2700_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH100_LH_2016preVFP")
Tprime_tAq_2700_MH100_LH_2016preVFP.sigma  = 1.751e-05
Tprime_tAq_2700_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH125_LH_2016preVFP")
Tprime_tAq_2700_MH125_LH_2016preVFP.sigma  = 2.196e-05
Tprime_tAq_2700_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH150_LH_2016preVFP")
Tprime_tAq_2700_MH150_LH_2016preVFP.sigma  = 2.643e-05
Tprime_tAq_2700_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH175_LH_2016preVFP")
Tprime_tAq_2700_MH175_LH_2016preVFP.sigma  = 3.084e-05
Tprime_tAq_2700_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH200_LH_2016preVFP")
Tprime_tAq_2700_MH200_LH_2016preVFP.sigma  = 3.519e-05
Tprime_tAq_2700_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH250_LH_2016preVFP")
Tprime_tAq_2700_MH250_LH_2016preVFP.sigma  = 4.376e-05
Tprime_tAq_2700_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH350_LH_2016preVFP")
Tprime_tAq_2700_MH350_LH_2016preVFP.sigma  = 6.03e-05
Tprime_tAq_2700_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH450_LH_2016preVFP")
Tprime_tAq_2700_MH450_LH_2016preVFP.sigma  = 7.577e-05
Tprime_tAq_2700_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH500_LH_2016preVFP")
Tprime_tAq_2700_MH500_LH_2016preVFP.sigma  = 8.31e-05
Tprime_tAq_2700_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2700_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2800
Tprime_tAq_2800_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH25_LH_2016preVFP")
Tprime_tAq_2800_MH25_LH_2016preVFP.sigma  = 2.937e-06
Tprime_tAq_2800_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH50_LH_2016preVFP")
Tprime_tAq_2800_MH50_LH_2016preVFP.sigma  = 6.968e-06
Tprime_tAq_2800_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH75_LH_2016preVFP")
Tprime_tAq_2800_MH75_LH_2016preVFP.sigma  = 1.076e-05
Tprime_tAq_2800_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH100_LH_2016preVFP")
Tprime_tAq_2800_MH100_LH_2016preVFP.sigma  = 1.448e-05
Tprime_tAq_2800_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH125_LH_2016preVFP")
Tprime_tAq_2800_MH125_LH_2016preVFP.sigma  = 1.817e-05
Tprime_tAq_2800_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH150_LH_2016preVFP")
Tprime_tAq_2800_MH150_LH_2016preVFP.sigma  = 2.177e-05
Tprime_tAq_2800_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH175_LH_2016preVFP")
Tprime_tAq_2800_MH175_LH_2016preVFP.sigma  = 2.538e-05
Tprime_tAq_2800_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH200_LH_2016preVFP")
Tprime_tAq_2800_MH200_LH_2016preVFP.sigma  = 2.896e-05
Tprime_tAq_2800_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH250_LH_2016preVFP")
Tprime_tAq_2800_MH250_LH_2016preVFP.sigma  = 3.6e-05
Tprime_tAq_2800_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH350_LH_2016preVFP")
Tprime_tAq_2800_MH350_LH_2016preVFP.sigma  = 4.967e-05
Tprime_tAq_2800_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH450_LH_2016preVFP")
Tprime_tAq_2800_MH450_LH_2016preVFP.sigma  = 6.256e-05
Tprime_tAq_2800_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH500_LH_2016preVFP")
Tprime_tAq_2800_MH500_LH_2016preVFP.sigma  = 6.865e-05
Tprime_tAq_2800_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2800_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=2900
Tprime_tAq_2900_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH25_LH_2016preVFP")
Tprime_tAq_2900_MH25_LH_2016preVFP.sigma  = 2.403e-06
Tprime_tAq_2900_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH50_LH_2016preVFP")
Tprime_tAq_2900_MH50_LH_2016preVFP.sigma  = 5.726e-06
Tprime_tAq_2900_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH75_LH_2016preVFP")
Tprime_tAq_2900_MH75_LH_2016preVFP.sigma  = 8.842e-06
Tprime_tAq_2900_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH100_LH_2016preVFP")
Tprime_tAq_2900_MH100_LH_2016preVFP.sigma  = 1.19e-05
Tprime_tAq_2900_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH125_LH_2016preVFP")
Tprime_tAq_2900_MH125_LH_2016preVFP.sigma  = 1.493e-05
Tprime_tAq_2900_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH150_LH_2016preVFP")
Tprime_tAq_2900_MH150_LH_2016preVFP.sigma  = 1.793e-05
Tprime_tAq_2900_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH175_LH_2016preVFP")
Tprime_tAq_2900_MH175_LH_2016preVFP.sigma  = 2.091e-05
Tprime_tAq_2900_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH200_LH_2016preVFP")
Tprime_tAq_2900_MH200_LH_2016preVFP.sigma  = 2.387e-05
Tprime_tAq_2900_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH250_LH_2016preVFP")
Tprime_tAq_2900_MH250_LH_2016preVFP.sigma  = 2.971e-05
Tprime_tAq_2900_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH350_LH_2016preVFP")
Tprime_tAq_2900_MH350_LH_2016preVFP.sigma  = 4.106e-05
Tprime_tAq_2900_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH450_LH_2016preVFP")
Tprime_tAq_2900_MH450_LH_2016preVFP.sigma  = 5.175e-05
Tprime_tAq_2900_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH500_LH_2016preVFP")
Tprime_tAq_2900_MH500_LH_2016preVFP.sigma  = 5.69e-05
Tprime_tAq_2900_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_2900_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# MT=3000
Tprime_tAq_3000_MH25_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH25_LH_2016preVFP")
Tprime_tAq_3000_MH25_LH_2016preVFP.sigma  = 1.972e-06
Tprime_tAq_3000_MH25_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH25_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH50_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH50_LH_2016preVFP")
Tprime_tAq_3000_MH50_LH_2016preVFP.sigma  = 4.696e-06
Tprime_tAq_3000_MH50_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH50_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH75_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH75_LH_2016preVFP")
Tprime_tAq_3000_MH75_LH_2016preVFP.sigma  = 7.255e-06
Tprime_tAq_3000_MH75_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH75_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH100_LH_2016preVFP")
Tprime_tAq_3000_MH100_LH_2016preVFP.sigma  = 9.765e-06
Tprime_tAq_3000_MH100_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH100_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH125_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH125_LH_2016preVFP")
Tprime_tAq_3000_MH125_LH_2016preVFP.sigma  = 1.225e-05
Tprime_tAq_3000_MH125_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH125_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH150_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH150_LH_2016preVFP")
Tprime_tAq_3000_MH150_LH_2016preVFP.sigma  = 1.471e-05
Tprime_tAq_3000_MH150_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH150_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH175_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH175_LH_2016preVFP")
Tprime_tAq_3000_MH175_LH_2016preVFP.sigma  = 1.72e-05
Tprime_tAq_3000_MH175_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH175_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH200_LH_2016preVFP")
Tprime_tAq_3000_MH200_LH_2016preVFP.sigma  = 1.964e-05
Tprime_tAq_3000_MH200_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH200_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH250_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH250_LH_2016preVFP")
Tprime_tAq_3000_MH250_LH_2016preVFP.sigma  = 2.446e-05
Tprime_tAq_3000_MH250_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH250_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH350_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH350_LH_2016preVFP")
Tprime_tAq_3000_MH350_LH_2016preVFP.sigma  = 3.381e-05
Tprime_tAq_3000_MH350_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH350_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH450_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH450_LH_2016preVFP")
Tprime_tAq_3000_MH450_LH_2016preVFP.sigma  = 4.27e-05
Tprime_tAq_3000_MH450_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH450_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH500_LH_2016preVFP")
Tprime_tAq_3000_MH500_LH_2016preVFP.sigma  = 4.694e-05
Tprime_tAq_3000_MH500_LH_2016preVFP.year = 2016
Tprime_tAq_3000_MH500_LH_2016preVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

# 2016pre bunches of tAq samples by MT mass

Tprime_tAq_600_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_LH_2016preVFP")
Tprime_tAq_600_LH_2016preVFP.year = 2016
Tprime_tAq_600_LH_2016preVFP.components = [Tprime_tAq_600_MH25_LH_2016preVFP, Tprime_tAq_600_MH50_LH_2016preVFP, Tprime_tAq_600_MH75_LH_2016preVFP, Tprime_tAq_600_MH100_LH_2016preVFP, Tprime_tAq_600_MH125_LH_2016preVFP, Tprime_tAq_600_MH150_LH_2016preVFP, Tprime_tAq_600_MH175_LH_2016preVFP, Tprime_tAq_600_MH200_LH_2016preVFP, Tprime_tAq_600_MH250_LH_2016preVFP, Tprime_tAq_600_MH350_LH_2016preVFP, Tprime_tAq_600_MH450_LH_2016preVFP, Tprime_tAq_600_MH500_LH_2016preVFP]

Tprime_tAq_700_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_LH_2016preVFP")
Tprime_tAq_700_LH_2016preVFP.year = 2016
Tprime_tAq_700_LH_2016preVFP.components = [Tprime_tAq_700_MH25_LH_2016preVFP, Tprime_tAq_700_MH50_LH_2016preVFP, Tprime_tAq_700_MH75_LH_2016preVFP, Tprime_tAq_700_MH100_LH_2016preVFP, Tprime_tAq_700_MH125_LH_2016preVFP, Tprime_tAq_700_MH150_LH_2016preVFP, Tprime_tAq_700_MH175_LH_2016preVFP, Tprime_tAq_700_MH200_LH_2016preVFP, Tprime_tAq_700_MH250_LH_2016preVFP, Tprime_tAq_700_MH350_LH_2016preVFP, Tprime_tAq_700_MH450_LH_2016preVFP, Tprime_tAq_700_MH500_LH_2016preVFP]

Tprime_tAq_800_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_LH_2016preVFP")
Tprime_tAq_800_LH_2016preVFP.year = 2016
Tprime_tAq_800_LH_2016preVFP.components = [Tprime_tAq_800_MH25_LH_2016preVFP, Tprime_tAq_800_MH50_LH_2016preVFP, Tprime_tAq_800_MH75_LH_2016preVFP, Tprime_tAq_800_MH100_LH_2016preVFP, Tprime_tAq_800_MH125_LH_2016preVFP, Tprime_tAq_800_MH150_LH_2016preVFP, Tprime_tAq_800_MH175_LH_2016preVFP, Tprime_tAq_800_MH200_LH_2016preVFP, Tprime_tAq_800_MH250_LH_2016preVFP, Tprime_tAq_800_MH350_LH_2016preVFP, Tprime_tAq_800_MH450_LH_2016preVFP, Tprime_tAq_800_MH500_LH_2016preVFP]

Tprime_tAq_900_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_LH_2016preVFP")
Tprime_tAq_900_LH_2016preVFP.year = 2016
Tprime_tAq_900_LH_2016preVFP.components = [Tprime_tAq_900_MH25_LH_2016preVFP, Tprime_tAq_900_MH50_LH_2016preVFP, Tprime_tAq_900_MH75_LH_2016preVFP, Tprime_tAq_900_MH100_LH_2016preVFP, Tprime_tAq_900_MH125_LH_2016preVFP, Tprime_tAq_900_MH150_LH_2016preVFP, Tprime_tAq_900_MH175_LH_2016preVFP, Tprime_tAq_900_MH200_LH_2016preVFP, Tprime_tAq_900_MH250_LH_2016preVFP, Tprime_tAq_900_MH350_LH_2016preVFP, Tprime_tAq_900_MH450_LH_2016preVFP, Tprime_tAq_900_MH500_LH_2016preVFP]

Tprime_tAq_1000_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_LH_2016preVFP")
Tprime_tAq_1000_LH_2016preVFP.year = 2016
Tprime_tAq_1000_LH_2016preVFP.components = [Tprime_tAq_1000_MH25_LH_2016preVFP, Tprime_tAq_1000_MH50_LH_2016preVFP, Tprime_tAq_1000_MH75_LH_2016preVFP, Tprime_tAq_1000_MH100_LH_2016preVFP, Tprime_tAq_1000_MH125_LH_2016preVFP, Tprime_tAq_1000_MH150_LH_2016preVFP, Tprime_tAq_1000_MH175_LH_2016preVFP, Tprime_tAq_1000_MH200_LH_2016preVFP, Tprime_tAq_1000_MH250_LH_2016preVFP, Tprime_tAq_1000_MH350_LH_2016preVFP, Tprime_tAq_1000_MH450_LH_2016preVFP, Tprime_tAq_1000_MH500_LH_2016preVFP]

Tprime_tAq_1100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_LH_2016preVFP")
Tprime_tAq_1100_LH_2016preVFP.year = 2016
Tprime_tAq_1100_LH_2016preVFP.components = [Tprime_tAq_1100_MH25_LH_2016preVFP, Tprime_tAq_1100_MH50_LH_2016preVFP, Tprime_tAq_1100_MH75_LH_2016preVFP, Tprime_tAq_1100_MH100_LH_2016preVFP, Tprime_tAq_1100_MH125_LH_2016preVFP, Tprime_tAq_1100_MH150_LH_2016preVFP, Tprime_tAq_1100_MH175_LH_2016preVFP, Tprime_tAq_1100_MH200_LH_2016preVFP, Tprime_tAq_1100_MH250_LH_2016preVFP, Tprime_tAq_1100_MH350_LH_2016preVFP, Tprime_tAq_1100_MH450_LH_2016preVFP, Tprime_tAq_1100_MH500_LH_2016preVFP]

Tprime_tAq_1200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_LH_2016preVFP")
Tprime_tAq_1200_LH_2016preVFP.year = 2016
Tprime_tAq_1200_LH_2016preVFP.components = [Tprime_tAq_1200_MH25_LH_2016preVFP, Tprime_tAq_1200_MH50_LH_2016preVFP, Tprime_tAq_1200_MH75_LH_2016preVFP, Tprime_tAq_1200_MH100_LH_2016preVFP, Tprime_tAq_1200_MH125_LH_2016preVFP, Tprime_tAq_1200_MH150_LH_2016preVFP, Tprime_tAq_1200_MH175_LH_2016preVFP, Tprime_tAq_1200_MH200_LH_2016preVFP, Tprime_tAq_1200_MH250_LH_2016preVFP, Tprime_tAq_1200_MH350_LH_2016preVFP, Tprime_tAq_1200_MH450_LH_2016preVFP, Tprime_tAq_1200_MH500_LH_2016preVFP]

Tprime_tAq_1300_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_LH_2016preVFP")
Tprime_tAq_1300_LH_2016preVFP.year = 2016
Tprime_tAq_1300_LH_2016preVFP.components = [Tprime_tAq_1300_MH25_LH_2016preVFP, Tprime_tAq_1300_MH50_LH_2016preVFP, Tprime_tAq_1300_MH75_LH_2016preVFP, Tprime_tAq_1300_MH100_LH_2016preVFP, Tprime_tAq_1300_MH125_LH_2016preVFP, Tprime_tAq_1300_MH150_LH_2016preVFP, Tprime_tAq_1300_MH175_LH_2016preVFP, Tprime_tAq_1300_MH200_LH_2016preVFP, Tprime_tAq_1300_MH250_LH_2016preVFP, Tprime_tAq_1300_MH350_LH_2016preVFP, Tprime_tAq_1300_MH450_LH_2016preVFP, Tprime_tAq_1300_MH500_LH_2016preVFP]

Tprime_tAq_1400_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_LH_2016preVFP")
Tprime_tAq_1400_LH_2016preVFP.year = 2016
Tprime_tAq_1400_LH_2016preVFP.components = [Tprime_tAq_1400_MH25_LH_2016preVFP, Tprime_tAq_1400_MH50_LH_2016preVFP, Tprime_tAq_1400_MH75_LH_2016preVFP, Tprime_tAq_1400_MH100_LH_2016preVFP, Tprime_tAq_1400_MH125_LH_2016preVFP, Tprime_tAq_1400_MH150_LH_2016preVFP, Tprime_tAq_1400_MH175_LH_2016preVFP, Tprime_tAq_1400_MH200_LH_2016preVFP, Tprime_tAq_1400_MH250_LH_2016preVFP, Tprime_tAq_1400_MH350_LH_2016preVFP, Tprime_tAq_1400_MH450_LH_2016preVFP, Tprime_tAq_1400_MH500_LH_2016preVFP]

Tprime_tAq_1500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_LH_2016preVFP")
Tprime_tAq_1500_LH_2016preVFP.year = 2016
Tprime_tAq_1500_LH_2016preVFP.components = [Tprime_tAq_1500_MH25_LH_2016preVFP, Tprime_tAq_1500_MH50_LH_2016preVFP, Tprime_tAq_1500_MH75_LH_2016preVFP, Tprime_tAq_1500_MH100_LH_2016preVFP, Tprime_tAq_1500_MH125_LH_2016preVFP, Tprime_tAq_1500_MH150_LH_2016preVFP, Tprime_tAq_1500_MH175_LH_2016preVFP, Tprime_tAq_1500_MH200_LH_2016preVFP, Tprime_tAq_1500_MH250_LH_2016preVFP, Tprime_tAq_1500_MH350_LH_2016preVFP, Tprime_tAq_1500_MH450_LH_2016preVFP, Tprime_tAq_1500_MH500_LH_2016preVFP]

Tprime_tAq_1600_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_LH_2016preVFP")
Tprime_tAq_1600_LH_2016preVFP.year = 2016
Tprime_tAq_1600_LH_2016preVFP.components = [Tprime_tAq_1600_MH25_LH_2016preVFP, Tprime_tAq_1600_MH50_LH_2016preVFP, Tprime_tAq_1600_MH75_LH_2016preVFP, Tprime_tAq_1600_MH100_LH_2016preVFP, Tprime_tAq_1600_MH125_LH_2016preVFP, Tprime_tAq_1600_MH150_LH_2016preVFP, Tprime_tAq_1600_MH175_LH_2016preVFP, Tprime_tAq_1600_MH200_LH_2016preVFP, Tprime_tAq_1600_MH250_LH_2016preVFP, Tprime_tAq_1600_MH350_LH_2016preVFP, Tprime_tAq_1600_MH450_LH_2016preVFP, Tprime_tAq_1600_MH500_LH_2016preVFP]

Tprime_tAq_1700_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_LH_2016preVFP")
Tprime_tAq_1700_LH_2016preVFP.year = 2016
Tprime_tAq_1700_LH_2016preVFP.components = [Tprime_tAq_1700_MH25_LH_2016preVFP, Tprime_tAq_1700_MH50_LH_2016preVFP, Tprime_tAq_1700_MH75_LH_2016preVFP, Tprime_tAq_1700_MH100_LH_2016preVFP, Tprime_tAq_1700_MH125_LH_2016preVFP, Tprime_tAq_1700_MH150_LH_2016preVFP, Tprime_tAq_1700_MH175_LH_2016preVFP, Tprime_tAq_1700_MH200_LH_2016preVFP, Tprime_tAq_1700_MH250_LH_2016preVFP, Tprime_tAq_1700_MH350_LH_2016preVFP, Tprime_tAq_1700_MH450_LH_2016preVFP, Tprime_tAq_1700_MH500_LH_2016preVFP]

Tprime_tAq_1800_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_LH_2016preVFP")
Tprime_tAq_1800_LH_2016preVFP.year = 2016
Tprime_tAq_1800_LH_2016preVFP.components = [Tprime_tAq_1800_MH25_LH_2016preVFP, Tprime_tAq_1800_MH50_LH_2016preVFP, Tprime_tAq_1800_MH75_LH_2016preVFP, Tprime_tAq_1800_MH100_LH_2016preVFP, Tprime_tAq_1800_MH125_LH_2016preVFP, Tprime_tAq_1800_MH150_LH_2016preVFP, Tprime_tAq_1800_MH175_LH_2016preVFP, Tprime_tAq_1800_MH200_LH_2016preVFP, Tprime_tAq_1800_MH250_LH_2016preVFP, Tprime_tAq_1800_MH350_LH_2016preVFP, Tprime_tAq_1800_MH450_LH_2016preVFP, Tprime_tAq_1800_MH500_LH_2016preVFP]

Tprime_tAq_1900_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_LH_2016preVFP")
Tprime_tAq_1900_LH_2016preVFP.year = 2016
Tprime_tAq_1900_LH_2016preVFP.components = [Tprime_tAq_1900_MH25_LH_2016preVFP, Tprime_tAq_1900_MH50_LH_2016preVFP, Tprime_tAq_1900_MH75_LH_2016preVFP, Tprime_tAq_1900_MH100_LH_2016preVFP, Tprime_tAq_1900_MH125_LH_2016preVFP, Tprime_tAq_1900_MH150_LH_2016preVFP, Tprime_tAq_1900_MH175_LH_2016preVFP, Tprime_tAq_1900_MH200_LH_2016preVFP, Tprime_tAq_1900_MH250_LH_2016preVFP, Tprime_tAq_1900_MH350_LH_2016preVFP, Tprime_tAq_1900_MH450_LH_2016preVFP, Tprime_tAq_1900_MH500_LH_2016preVFP]

Tprime_tAq_2000_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_LH_2016preVFP")
Tprime_tAq_2000_LH_2016preVFP.year = 2016
Tprime_tAq_2000_LH_2016preVFP.components = [Tprime_tAq_2000_MH25_LH_2016preVFP, Tprime_tAq_2000_MH50_LH_2016preVFP, Tprime_tAq_2000_MH75_LH_2016preVFP, Tprime_tAq_2000_MH100_LH_2016preVFP, Tprime_tAq_2000_MH125_LH_2016preVFP, Tprime_tAq_2000_MH150_LH_2016preVFP, Tprime_tAq_2000_MH175_LH_2016preVFP, Tprime_tAq_2000_MH200_LH_2016preVFP, Tprime_tAq_2000_MH250_LH_2016preVFP, Tprime_tAq_2000_MH350_LH_2016preVFP, Tprime_tAq_2000_MH450_LH_2016preVFP, Tprime_tAq_2000_MH500_LH_2016preVFP]

Tprime_tAq_2100_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_LH_2016preVFP")
Tprime_tAq_2100_LH_2016preVFP.year = 2016
Tprime_tAq_2100_LH_2016preVFP.components = [Tprime_tAq_2100_MH25_LH_2016preVFP, Tprime_tAq_2100_MH50_LH_2016preVFP, Tprime_tAq_2100_MH75_LH_2016preVFP, Tprime_tAq_2100_MH100_LH_2016preVFP, Tprime_tAq_2100_MH125_LH_2016preVFP, Tprime_tAq_2100_MH150_LH_2016preVFP, Tprime_tAq_2100_MH175_LH_2016preVFP, Tprime_tAq_2100_MH200_LH_2016preVFP, Tprime_tAq_2100_MH250_LH_2016preVFP, Tprime_tAq_2100_MH350_LH_2016preVFP, Tprime_tAq_2100_MH450_LH_2016preVFP, Tprime_tAq_2100_MH500_LH_2016preVFP]

Tprime_tAq_2200_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_LH_2016preVFP")
Tprime_tAq_2200_LH_2016preVFP.year = 2016
Tprime_tAq_2200_LH_2016preVFP.components = [Tprime_tAq_2200_MH25_LH_2016preVFP, Tprime_tAq_2200_MH50_LH_2016preVFP, Tprime_tAq_2200_MH75_LH_2016preVFP, Tprime_tAq_2200_MH100_LH_2016preVFP, Tprime_tAq_2200_MH125_LH_2016preVFP, Tprime_tAq_2200_MH150_LH_2016preVFP, Tprime_tAq_2200_MH175_LH_2016preVFP, Tprime_tAq_2200_MH200_LH_2016preVFP, Tprime_tAq_2200_MH250_LH_2016preVFP, Tprime_tAq_2200_MH350_LH_2016preVFP, Tprime_tAq_2200_MH450_LH_2016preVFP, Tprime_tAq_2200_MH500_LH_2016preVFP]

Tprime_tAq_2300_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_LH_2016preVFP")
Tprime_tAq_2300_LH_2016preVFP.year = 2016
Tprime_tAq_2300_LH_2016preVFP.components = [Tprime_tAq_2300_MH25_LH_2016preVFP, Tprime_tAq_2300_MH50_LH_2016preVFP, Tprime_tAq_2300_MH75_LH_2016preVFP, Tprime_tAq_2300_MH100_LH_2016preVFP, Tprime_tAq_2300_MH125_LH_2016preVFP, Tprime_tAq_2300_MH150_LH_2016preVFP, Tprime_tAq_2300_MH175_LH_2016preVFP, Tprime_tAq_2300_MH200_LH_2016preVFP, Tprime_tAq_2300_MH250_LH_2016preVFP, Tprime_tAq_2300_MH350_LH_2016preVFP, Tprime_tAq_2300_MH450_LH_2016preVFP, Tprime_tAq_2300_MH500_LH_2016preVFP]

Tprime_tAq_2400_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_LH_2016preVFP")
Tprime_tAq_2400_LH_2016preVFP.year = 2016
Tprime_tAq_2400_LH_2016preVFP.components = [Tprime_tAq_2400_MH25_LH_2016preVFP, Tprime_tAq_2400_MH50_LH_2016preVFP, Tprime_tAq_2400_MH75_LH_2016preVFP, Tprime_tAq_2400_MH100_LH_2016preVFP, Tprime_tAq_2400_MH125_LH_2016preVFP, Tprime_tAq_2400_MH150_LH_2016preVFP, Tprime_tAq_2400_MH175_LH_2016preVFP, Tprime_tAq_2400_MH200_LH_2016preVFP, Tprime_tAq_2400_MH250_LH_2016preVFP, Tprime_tAq_2400_MH350_LH_2016preVFP, Tprime_tAq_2400_MH450_LH_2016preVFP, Tprime_tAq_2400_MH500_LH_2016preVFP]

Tprime_tAq_2500_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_LH_2016preVFP")
Tprime_tAq_2500_LH_2016preVFP.year = 2016
Tprime_tAq_2500_LH_2016preVFP.components = [Tprime_tAq_2500_MH25_LH_2016preVFP, Tprime_tAq_2500_MH50_LH_2016preVFP, Tprime_tAq_2500_MH75_LH_2016preVFP, Tprime_tAq_2500_MH100_LH_2016preVFP, Tprime_tAq_2500_MH125_LH_2016preVFP, Tprime_tAq_2500_MH150_LH_2016preVFP, Tprime_tAq_2500_MH175_LH_2016preVFP, Tprime_tAq_2500_MH200_LH_2016preVFP, Tprime_tAq_2500_MH250_LH_2016preVFP, Tprime_tAq_2500_MH350_LH_2016preVFP, Tprime_tAq_2500_MH450_LH_2016preVFP, Tprime_tAq_2500_MH500_LH_2016preVFP]

Tprime_tAq_2600_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_LH_2016preVFP")
Tprime_tAq_2600_LH_2016preVFP.year = 2016
Tprime_tAq_2600_LH_2016preVFP.components = [Tprime_tAq_2600_MH25_LH_2016preVFP, Tprime_tAq_2600_MH50_LH_2016preVFP, Tprime_tAq_2600_MH75_LH_2016preVFP, Tprime_tAq_2600_MH100_LH_2016preVFP, Tprime_tAq_2600_MH125_LH_2016preVFP, Tprime_tAq_2600_MH150_LH_2016preVFP, Tprime_tAq_2600_MH175_LH_2016preVFP, Tprime_tAq_2600_MH200_LH_2016preVFP, Tprime_tAq_2600_MH250_LH_2016preVFP, Tprime_tAq_2600_MH350_LH_2016preVFP, Tprime_tAq_2600_MH450_LH_2016preVFP, Tprime_tAq_2600_MH500_LH_2016preVFP]

Tprime_tAq_2700_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_LH_2016preVFP")
Tprime_tAq_2700_LH_2016preVFP.year = 2016
Tprime_tAq_2700_LH_2016preVFP.components = [Tprime_tAq_2700_MH25_LH_2016preVFP, Tprime_tAq_2700_MH50_LH_2016preVFP, Tprime_tAq_2700_MH75_LH_2016preVFP, Tprime_tAq_2700_MH100_LH_2016preVFP, Tprime_tAq_2700_MH125_LH_2016preVFP, Tprime_tAq_2700_MH150_LH_2016preVFP, Tprime_tAq_2700_MH175_LH_2016preVFP, Tprime_tAq_2700_MH200_LH_2016preVFP, Tprime_tAq_2700_MH250_LH_2016preVFP, Tprime_tAq_2700_MH350_LH_2016preVFP, Tprime_tAq_2700_MH450_LH_2016preVFP, Tprime_tAq_2700_MH500_LH_2016preVFP]

Tprime_tAq_2800_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_LH_2016preVFP")
Tprime_tAq_2800_LH_2016preVFP.year = 2016
Tprime_tAq_2800_LH_2016preVFP.components = [Tprime_tAq_2800_MH25_LH_2016preVFP, Tprime_tAq_2800_MH50_LH_2016preVFP, Tprime_tAq_2800_MH75_LH_2016preVFP, Tprime_tAq_2800_MH100_LH_2016preVFP, Tprime_tAq_2800_MH125_LH_2016preVFP, Tprime_tAq_2800_MH150_LH_2016preVFP, Tprime_tAq_2800_MH175_LH_2016preVFP, Tprime_tAq_2800_MH200_LH_2016preVFP, Tprime_tAq_2800_MH250_LH_2016preVFP, Tprime_tAq_2800_MH350_LH_2016preVFP, Tprime_tAq_2800_MH450_LH_2016preVFP, Tprime_tAq_2800_MH500_LH_2016preVFP]

Tprime_tAq_2900_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_LH_2016preVFP")
Tprime_tAq_2900_LH_2016preVFP.year = 2016
Tprime_tAq_2900_LH_2016preVFP.components = [Tprime_tAq_2900_MH25_LH_2016preVFP, Tprime_tAq_2900_MH50_LH_2016preVFP, Tprime_tAq_2900_MH75_LH_2016preVFP, Tprime_tAq_2900_MH100_LH_2016preVFP, Tprime_tAq_2900_MH125_LH_2016preVFP, Tprime_tAq_2900_MH150_LH_2016preVFP, Tprime_tAq_2900_MH175_LH_2016preVFP, Tprime_tAq_2900_MH200_LH_2016preVFP, Tprime_tAq_2900_MH250_LH_2016preVFP, Tprime_tAq_2900_MH350_LH_2016preVFP, Tprime_tAq_2900_MH450_LH_2016preVFP, Tprime_tAq_2900_MH500_LH_2016preVFP]

Tprime_tAq_3000_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_LH_2016preVFP")
Tprime_tAq_3000_LH_2016preVFP.year = 2016
Tprime_tAq_3000_LH_2016preVFP.components = [Tprime_tAq_3000_MH25_LH_2016preVFP, Tprime_tAq_3000_MH50_LH_2016preVFP, Tprime_tAq_3000_MH75_LH_2016preVFP, Tprime_tAq_3000_MH100_LH_2016preVFP, Tprime_tAq_3000_MH125_LH_2016preVFP, Tprime_tAq_3000_MH150_LH_2016preVFP, Tprime_tAq_3000_MH175_LH_2016preVFP, Tprime_tAq_3000_MH200_LH_2016preVFP, Tprime_tAq_3000_MH250_LH_2016preVFP, Tprime_tAq_3000_MH350_LH_2016preVFP, Tprime_tAq_3000_MH450_LH_2016preVFP, Tprime_tAq_3000_MH500_LH_2016preVFP]


#Tprime_tAq_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_tAq_LH_2016preVFP")
#Tprime_tAq_LH_2016preVFP.year = 2016

### 2016post ####

# MT=600
Tprime_tAq_600_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH25_LH_2016postVFP")
Tprime_tAq_600_MH25_LH_2016postVFP.sigma  = 0.0002903
Tprime_tAq_600_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH50_LH_2016postVFP")
Tprime_tAq_600_MH50_LH_2016postVFP.sigma  = 0.0006855
Tprime_tAq_600_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH75_LH_2016postVFP")
Tprime_tAq_600_MH75_LH_2016postVFP.sigma  = 0.001038
Tprime_tAq_600_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH100_LH_2016postVFP")
Tprime_tAq_600_MH100_LH_2016postVFP.sigma  = 0.001359
Tprime_tAq_600_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH125_LH_2016postVFP")
Tprime_tAq_600_MH125_LH_2016postVFP.sigma  = 0.001647
Tprime_tAq_600_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH150_LH_2016postVFP")
Tprime_tAq_600_MH150_LH_2016postVFP.sigma  = 0.00189
Tprime_tAq_600_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH175_LH_2016postVFP")
Tprime_tAq_600_MH175_LH_2016postVFP.sigma  = 0.002103
Tprime_tAq_600_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH200_LH_2016postVFP")
Tprime_tAq_600_MH200_LH_2016postVFP.sigma  = 0.002245
Tprime_tAq_600_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH250_LH_2016postVFP")
Tprime_tAq_600_MH250_LH_2016postVFP.sigma  = 0.002365
Tprime_tAq_600_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH350_LH_2016postVFP")
Tprime_tAq_600_MH350_LH_2016postVFP.sigma  = 0.00181
Tprime_tAq_600_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH450_LH_2016postVFP")
Tprime_tAq_600_MH450_LH_2016postVFP.sigma  = 1.525e-05
Tprime_tAq_600_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_600_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH500_LH_2016postVFP")
Tprime_tAq_600_MH500_LH_2016postVFP.sigma  = 8.808e-08
Tprime_tAq_600_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_600_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH25_LH_2016postVFP")
Tprime_tAq_700_MH25_LH_2016postVFP.sigma  = 0.0002274
Tprime_tAq_700_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH50_LH_2016postVFP")
Tprime_tAq_700_MH50_LH_2016postVFP.sigma  = 0.0005375
Tprime_tAq_700_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH75_LH_2016postVFP")
Tprime_tAq_700_MH75_LH_2016postVFP.sigma  = 0.0008201
Tprime_tAq_700_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH100_LH_2016postVFP")
Tprime_tAq_700_MH100_LH_2016postVFP.sigma  = 0.001083
Tprime_tAq_700_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH125_LH_2016postVFP")
Tprime_tAq_700_MH125_LH_2016postVFP.sigma  = 0.001327
Tprime_tAq_700_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH150_LH_2016postVFP")
Tprime_tAq_700_MH150_LH_2016postVFP.sigma  = 0.001547
Tprime_tAq_700_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH175_LH_2016postVFP")
Tprime_tAq_700_MH175_LH_2016postVFP.sigma  = 0.00174
Tprime_tAq_700_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH200_LH_2016postVFP")
Tprime_tAq_700_MH200_LH_2016postVFP.sigma  = 0.001907
Tprime_tAq_700_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH250_LH_2016postVFP")
Tprime_tAq_700_MH250_LH_2016postVFP.sigma  = 0.002135
Tprime_tAq_700_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH350_LH_2016postVFP")
Tprime_tAq_700_MH350_LH_2016postVFP.sigma  = 0.002099
Tprime_tAq_700_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH450_LH_2016postVFP")
Tprime_tAq_700_MH450_LH_2016postVFP.sigma  = 0.001408
Tprime_tAq_700_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_700_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH500_LH_2016postVFP")
Tprime_tAq_700_MH500_LH_2016postVFP.sigma  = 0.0007664
Tprime_tAq_700_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_700_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH25_LH_2016postVFP")
Tprime_tAq_800_MH25_LH_2016postVFP.sigma  = 0.0001764
Tprime_tAq_800_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH50_LH_2016postVFP")
Tprime_tAq_800_MH50_LH_2016postVFP.sigma  = 0.0004184
Tprime_tAq_800_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH75_LH_2016postVFP")
Tprime_tAq_800_MH75_LH_2016postVFP.sigma  = 0.0006423
Tprime_tAq_800_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH100_LH_2016postVFP")
Tprime_tAq_800_MH100_LH_2016postVFP.sigma  = 0.0008548
Tprime_tAq_800_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH125_LH_2016postVFP")
Tprime_tAq_800_MH125_LH_2016postVFP.sigma  = 0.001053
Tprime_tAq_800_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH150_LH_2016postVFP")
Tprime_tAq_800_MH150_LH_2016postVFP.sigma  = 0.001241
Tprime_tAq_800_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH175_LH_2016postVFP")
Tprime_tAq_800_MH175_LH_2016postVFP.sigma  = 0.001409
Tprime_tAq_800_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH200_LH_2016postVFP")
Tprime_tAq_800_MH200_LH_2016postVFP.sigma  = 0.001558
Tprime_tAq_800_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH250_LH_2016postVFP")
Tprime_tAq_800_MH250_LH_2016postVFP.sigma  = 0.001809
Tprime_tAq_800_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH350_LH_2016postVFP")
Tprime_tAq_800_MH350_LH_2016postVFP.sigma  = 0.00199
Tprime_tAq_800_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH450_LH_2016postVFP")
Tprime_tAq_800_MH450_LH_2016postVFP.sigma  = 0.001746
Tprime_tAq_800_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_800_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH500_LH_2016postVFP")
Tprime_tAq_800_MH500_LH_2016postVFP.sigma  = 0.00146
Tprime_tAq_800_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_800_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH25_LH_2016postVFP")
Tprime_tAq_900_MH25_LH_2016postVFP.sigma  = 0.0001424
Tprime_tAq_900_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH50_LH_2016postVFP")
Tprime_tAq_900_MH50_LH_2016postVFP.sigma  = 0.0003344
Tprime_tAq_900_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH75_LH_2016postVFP")
Tprime_tAq_900_MH75_LH_2016postVFP.sigma  = 0.0005126
Tprime_tAq_900_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH100_LH_2016postVFP")
Tprime_tAq_900_MH100_LH_2016postVFP.sigma  = 0.0006827
Tprime_tAq_900_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH125_LH_2016postVFP")
Tprime_tAq_900_MH125_LH_2016postVFP.sigma  = 0.0008462
Tprime_tAq_900_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH150_LH_2016postVFP")
Tprime_tAq_900_MH150_LH_2016postVFP.sigma  = 0.0009996
Tprime_tAq_900_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH175_LH_2016postVFP")
Tprime_tAq_900_MH175_LH_2016postVFP.sigma  = 0.001149
Tprime_tAq_900_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH200_LH_2016postVFP")
Tprime_tAq_900_MH200_LH_2016postVFP.sigma  = 0.001273
Tprime_tAq_900_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH250_LH_2016postVFP")
Tprime_tAq_900_MH250_LH_2016postVFP.sigma  = 0.001497
Tprime_tAq_900_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH350_LH_2016postVFP")
Tprime_tAq_900_MH350_LH_2016postVFP.sigma  = 0.001763
Tprime_tAq_900_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH450_LH_2016postVFP")
Tprime_tAq_900_MH450_LH_2016postVFP.sigma  = 0.001734
Tprime_tAq_900_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_900_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH500_LH_2016postVFP")
Tprime_tAq_900_MH500_LH_2016postVFP.sigma  = 0.001604
Tprime_tAq_900_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_900_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH25_LH_2016postVFP")
Tprime_tAq_1000_MH25_LH_2016postVFP.sigma  = 0.0001116
Tprime_tAq_1000_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH50_LH_2016postVFP")
Tprime_tAq_1000_MH50_LH_2016postVFP.sigma  = 0.0002655
Tprime_tAq_1000_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH75_LH_2016postVFP")
Tprime_tAq_1000_MH75_LH_2016postVFP.sigma  = 0.0004078
Tprime_tAq_1000_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH100_LH_2016postVFP")
Tprime_tAq_1000_MH100_LH_2016postVFP.sigma  = 0.0005434
Tprime_tAq_1000_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH125_LH_2016postVFP")
Tprime_tAq_1000_MH125_LH_2016postVFP.sigma  = 0.0006745
Tprime_tAq_1000_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH150_LH_2016postVFP")
Tprime_tAq_1000_MH150_LH_2016postVFP.sigma  = 0.0007994
Tprime_tAq_1000_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH175_LH_2016postVFP")
Tprime_tAq_1000_MH175_LH_2016postVFP.sigma  = 0.0009197
Tprime_tAq_1000_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH200_LH_2016postVFP")
Tprime_tAq_1000_MH200_LH_2016postVFP.sigma  = 0.001031
Tprime_tAq_1000_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH250_LH_2016postVFP")
Tprime_tAq_1000_MH250_LH_2016postVFP.sigma  = 0.001227
Tprime_tAq_1000_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH350_LH_2016postVFP")
Tprime_tAq_1000_MH350_LH_2016postVFP.sigma  = 0.001513
Tprime_tAq_1000_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH450_LH_2016postVFP")
Tprime_tAq_1000_MH450_LH_2016postVFP.sigma  = 0.001575
Tprime_tAq_1000_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH500_LH_2016postVFP")
Tprime_tAq_1000_MH500_LH_2016postVFP.sigma  = 0.001544
Tprime_tAq_1000_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1000_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH25_LH_2016postVFP")
Tprime_tAq_1100_MH25_LH_2016postVFP.sigma  = 8.915e-05
Tprime_tAq_1100_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH50_LH_2016postVFP")
Tprime_tAq_1100_MH50_LH_2016postVFP.sigma  = 0.0002115
Tprime_tAq_1100_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH75_LH_2016postVFP")
Tprime_tAq_1100_MH75_LH_2016postVFP.sigma  = 0.0003253
Tprime_tAq_1100_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH100_LH_2016postVFP")
Tprime_tAq_1100_MH100_LH_2016postVFP.sigma  = 0.0004356
Tprime_tAq_1100_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH125_LH_2016postVFP")
Tprime_tAq_1100_MH125_LH_2016postVFP.sigma  = 0.0005412
Tprime_tAq_1100_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH150_LH_2016postVFP")
Tprime_tAq_1100_MH150_LH_2016postVFP.sigma  = 0.0006435
Tprime_tAq_1100_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH175_LH_2016postVFP")
Tprime_tAq_1100_MH175_LH_2016postVFP.sigma  = 0.0007414
Tprime_tAq_1100_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH200_LH_2016postVFP")
Tprime_tAq_1100_MH200_LH_2016postVFP.sigma  = 0.0008344
Tprime_tAq_1100_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH250_LH_2016postVFP")
Tprime_tAq_1100_MH250_LH_2016postVFP.sigma  = 0.001003
Tprime_tAq_1100_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH350_LH_2016postVFP")
Tprime_tAq_1100_MH350_LH_2016postVFP.sigma  = 0.001263
Tprime_tAq_1100_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH450_LH_2016postVFP")
Tprime_tAq_1100_MH450_LH_2016postVFP.sigma  = 0.001382
Tprime_tAq_1100_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH500_LH_2016postVFP")
Tprime_tAq_1100_MH500_LH_2016postVFP.sigma  = 0.001396
Tprime_tAq_1100_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1100_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH25_LH_2016postVFP")
Tprime_tAq_1200_MH25_LH_2016postVFP.sigma  = 7.205e-05
Tprime_tAq_1200_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH50_LH_2016postVFP")
Tprime_tAq_1200_MH50_LH_2016postVFP.sigma  = 0.0001711
Tprime_tAq_1200_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH75_LH_2016postVFP")
Tprime_tAq_1200_MH75_LH_2016postVFP.sigma  = 0.0002633
Tprime_tAq_1200_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH100_LH_2016postVFP")
Tprime_tAq_1200_MH100_LH_2016postVFP.sigma  = 0.0003525
Tprime_tAq_1200_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH125_LH_2016postVFP")
Tprime_tAq_1200_MH125_LH_2016postVFP.sigma  = 0.0004401
Tprime_tAq_1200_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH150_LH_2016postVFP")
Tprime_tAq_1200_MH150_LH_2016postVFP.sigma  = 0.0005238
Tprime_tAq_1200_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH175_LH_2016postVFP")
Tprime_tAq_1200_MH175_LH_2016postVFP.sigma  = 0.0006072
Tprime_tAq_1200_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH200_LH_2016postVFP")
Tprime_tAq_1200_MH200_LH_2016postVFP.sigma  = 0.0006849
Tprime_tAq_1200_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH250_LH_2016postVFP")
Tprime_tAq_1200_MH250_LH_2016postVFP.sigma  = 0.0008286
Tprime_tAq_1200_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH350_LH_2016postVFP")
Tprime_tAq_1200_MH350_LH_2016postVFP.sigma  = 0.001061
Tprime_tAq_1200_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH450_LH_2016postVFP")
Tprime_tAq_1200_MH450_LH_2016postVFP.sigma  = 0.001187
Tprime_tAq_1200_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH500_LH_2016postVFP")
Tprime_tAq_1200_MH500_LH_2016postVFP.sigma  = 0.001218
Tprime_tAq_1200_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1200_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH25_LH_2016postVFP")
Tprime_tAq_1300_MH25_LH_2016postVFP.sigma  = 5.836e-05
Tprime_tAq_1300_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH50_LH_2016postVFP")
Tprime_tAq_1300_MH50_LH_2016postVFP.sigma  = 0.0001387
Tprime_tAq_1300_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH75_LH_2016postVFP")
Tprime_tAq_1300_MH75_LH_2016postVFP.sigma  = 0.0002136
Tprime_tAq_1300_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH100_LH_2016postVFP")
Tprime_tAq_1300_MH100_LH_2016postVFP.sigma  = 0.0002862
Tprime_tAq_1300_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH125_LH_2016postVFP")
Tprime_tAq_1300_MH125_LH_2016postVFP.sigma  = 0.0003573
Tprime_tAq_1300_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH150_LH_2016postVFP")
Tprime_tAq_1300_MH150_LH_2016postVFP.sigma  = 0.0004262
Tprime_tAq_1300_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH175_LH_2016postVFP")
Tprime_tAq_1300_MH175_LH_2016postVFP.sigma  = 0.0004933
Tprime_tAq_1300_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH200_LH_2016postVFP")
Tprime_tAq_1300_MH200_LH_2016postVFP.sigma  = 0.0005579
Tprime_tAq_1300_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH250_LH_2016postVFP")
Tprime_tAq_1300_MH250_LH_2016postVFP.sigma  = 0.000678
Tprime_tAq_1300_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH350_LH_2016postVFP")
Tprime_tAq_1300_MH350_LH_2016postVFP.sigma  = 0.0008797
Tprime_tAq_1300_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH450_LH_2016postVFP")
Tprime_tAq_1300_MH450_LH_2016postVFP.sigma  = 0.001014
Tprime_tAq_1300_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH500_LH_2016postVFP")
Tprime_tAq_1300_MH500_LH_2016postVFP.sigma  = 0.001051
Tprime_tAq_1300_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1300_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH25_LH_2016postVFP")
Tprime_tAq_1400_MH25_LH_2016postVFP.sigma  = 4.705e-05
Tprime_tAq_1400_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH50_LH_2016postVFP")
Tprime_tAq_1400_MH50_LH_2016postVFP.sigma  = 0.0001119
Tprime_tAq_1400_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH75_LH_2016postVFP")
Tprime_tAq_1400_MH75_LH_2016postVFP.sigma  = 0.0001724
Tprime_tAq_1400_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH100_LH_2016postVFP")
Tprime_tAq_1400_MH100_LH_2016postVFP.sigma  = 0.0002309
Tprime_tAq_1400_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH125_LH_2016postVFP")
Tprime_tAq_1400_MH125_LH_2016postVFP.sigma  = 0.0002881
Tprime_tAq_1400_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH150_LH_2016postVFP")
Tprime_tAq_1400_MH150_LH_2016postVFP.sigma  = 0.0003442
Tprime_tAq_1400_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH175_LH_2016postVFP")
Tprime_tAq_1400_MH175_LH_2016postVFP.sigma  = 0.0004004
Tprime_tAq_1400_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH200_LH_2016postVFP")
Tprime_tAq_1400_MH200_LH_2016postVFP.sigma  = 0.0004536
Tprime_tAq_1400_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH250_LH_2016postVFP")
Tprime_tAq_1400_MH250_LH_2016postVFP.sigma  = 0.0005538
Tprime_tAq_1400_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH350_LH_2016postVFP")
Tprime_tAq_1400_MH350_LH_2016postVFP.sigma  = 0.0007273
Tprime_tAq_1400_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH450_LH_2016postVFP")
Tprime_tAq_1400_MH450_LH_2016postVFP.sigma  = 0.0008543
Tprime_tAq_1400_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH500_LH_2016postVFP")
Tprime_tAq_1400_MH500_LH_2016postVFP.sigma  = 0.0008969
Tprime_tAq_1400_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1400_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH25_LH_2016postVFP")
Tprime_tAq_1500_MH25_LH_2016postVFP.sigma  = 3.827e-05
Tprime_tAq_1500_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH50_LH_2016postVFP")
Tprime_tAq_1500_MH50_LH_2016postVFP.sigma  = 9.102e-05
Tprime_tAq_1500_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH75_LH_2016postVFP")
Tprime_tAq_1500_MH75_LH_2016postVFP.sigma  = 0.0001403
Tprime_tAq_1500_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH100_LH_2016postVFP")
Tprime_tAq_1500_MH100_LH_2016postVFP.sigma  = 0.0001883
Tprime_tAq_1500_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH125_LH_2016postVFP")
Tprime_tAq_1500_MH125_LH_2016postVFP.sigma  = 0.0002353
Tprime_tAq_1500_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH150_LH_2016postVFP")
Tprime_tAq_1500_MH150_LH_2016postVFP.sigma  = 0.0002808
Tprime_tAq_1500_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH175_LH_2016postVFP")
Tprime_tAq_1500_MH175_LH_2016postVFP.sigma  = 0.0003257
Tprime_tAq_1500_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH200_LH_2016postVFP")
Tprime_tAq_1500_MH200_LH_2016postVFP.sigma  = 0.0003694
Tprime_tAq_1500_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH250_LH_2016postVFP")
Tprime_tAq_1500_MH250_LH_2016postVFP.sigma  = 0.0004541
Tprime_tAq_1500_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH350_LH_2016postVFP")
Tprime_tAq_1500_MH350_LH_2016postVFP.sigma  = 0.0006032
Tprime_tAq_1500_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH450_LH_2016postVFP")
Tprime_tAq_1500_MH450_LH_2016postVFP.sigma  = 0.0007173
Tprime_tAq_1500_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH500_LH_2016postVFP")
Tprime_tAq_1500_MH500_LH_2016postVFP.sigma  = 0.0007597
Tprime_tAq_1500_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1500_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH25_LH_2016postVFP")
Tprime_tAq_1600_MH25_LH_2016postVFP.sigma  = 3.119e-05
Tprime_tAq_1600_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH50_LH_2016postVFP")
Tprime_tAq_1600_MH50_LH_2016postVFP.sigma  = 7.417e-05
Tprime_tAq_1600_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH75_LH_2016postVFP")
Tprime_tAq_1600_MH75_LH_2016postVFP.sigma  = 0.0001144
Tprime_tAq_1600_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH100_LH_2016postVFP")
Tprime_tAq_1600_MH100_LH_2016postVFP.sigma  = 0.0001536
Tprime_tAq_1600_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH125_LH_2016postVFP")
Tprime_tAq_1600_MH125_LH_2016postVFP.sigma  = 0.0001921
Tprime_tAq_1600_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH150_LH_2016postVFP")
Tprime_tAq_1600_MH150_LH_2016postVFP.sigma  = 0.0002298
Tprime_tAq_1600_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH175_LH_2016postVFP")
Tprime_tAq_1600_MH175_LH_2016postVFP.sigma  = 0.0002668
Tprime_tAq_1600_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH200_LH_2016postVFP")
Tprime_tAq_1600_MH200_LH_2016postVFP.sigma  = 0.0003029
Tprime_tAq_1600_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH250_LH_2016postVFP")
Tprime_tAq_1600_MH250_LH_2016postVFP.sigma  = 0.0003721
Tprime_tAq_1600_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH350_LH_2016postVFP")
Tprime_tAq_1600_MH350_LH_2016postVFP.sigma  = 0.0004956
Tprime_tAq_1600_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH450_LH_2016postVFP")
Tprime_tAq_1600_MH450_LH_2016postVFP.sigma  = 0.0005936
Tprime_tAq_1600_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH500_LH_2016postVFP")
Tprime_tAq_1600_MH500_LH_2016postVFP.sigma  = 0.0006336
Tprime_tAq_1600_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1600_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH25_LH_2016postVFP")
Tprime_tAq_1700_MH25_LH_2016postVFP.sigma  = 2.541e-05
Tprime_tAq_1700_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH50_LH_2016postVFP")
Tprime_tAq_1700_MH50_LH_2016postVFP.sigma  = 6.043e-05
Tprime_tAq_1700_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH75_LH_2016postVFP")
Tprime_tAq_1700_MH75_LH_2016postVFP.sigma  = 9.323e-05
Tprime_tAq_1700_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH100_LH_2016postVFP")
Tprime_tAq_1700_MH100_LH_2016postVFP.sigma  = 0.0001252
Tprime_tAq_1700_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH125_LH_2016postVFP")
Tprime_tAq_1700_MH125_LH_2016postVFP.sigma  = 0.0001567
Tprime_tAq_1700_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH150_LH_2016postVFP")
Tprime_tAq_1700_MH150_LH_2016postVFP.sigma  = 0.0001876
Tprime_tAq_1700_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH175_LH_2016postVFP")
Tprime_tAq_1700_MH175_LH_2016postVFP.sigma  = 0.0002178
Tprime_tAq_1700_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH200_LH_2016postVFP")
Tprime_tAq_1700_MH200_LH_2016postVFP.sigma  = 0.0002476
Tprime_tAq_1700_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH250_LH_2016postVFP")
Tprime_tAq_1700_MH250_LH_2016postVFP.sigma  = 0.0003049
Tprime_tAq_1700_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH350_LH_2016postVFP")
Tprime_tAq_1700_MH350_LH_2016postVFP.sigma  = 0.0004092
Tprime_tAq_1700_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH450_LH_2016postVFP")
Tprime_tAq_1700_MH450_LH_2016postVFP.sigma  = 0.0004959
Tprime_tAq_1700_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH500_LH_2016postVFP")
Tprime_tAq_1700_MH500_LH_2016postVFP.sigma  = 0.0005317
Tprime_tAq_1700_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1700_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH25_LH_2016postVFP")
Tprime_tAq_1800_MH25_LH_2016postVFP.sigma  = 2.076e-05
Tprime_tAq_1800_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH50_LH_2016postVFP")
Tprime_tAq_1800_MH50_LH_2016postVFP.sigma  = 4.931e-05
Tprime_tAq_1800_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH75_LH_2016postVFP")
Tprime_tAq_1800_MH75_LH_2016postVFP.sigma  = 7.608e-05
Tprime_tAq_1800_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH100_LH_2016postVFP")
Tprime_tAq_1800_MH100_LH_2016postVFP.sigma  = 0.0001022
Tprime_tAq_1800_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH125_LH_2016postVFP")
Tprime_tAq_1800_MH125_LH_2016postVFP.sigma  = 0.000128
Tprime_tAq_1800_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH150_LH_2016postVFP")
Tprime_tAq_1800_MH150_LH_2016postVFP.sigma  = 0.0001533
Tprime_tAq_1800_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH175_LH_2016postVFP")
Tprime_tAq_1800_MH175_LH_2016postVFP.sigma  = 0.0001782
Tprime_tAq_1800_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH200_LH_2016postVFP")
Tprime_tAq_1800_MH200_LH_2016postVFP.sigma  = 0.0002026
Tprime_tAq_1800_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH250_LH_2016postVFP")
Tprime_tAq_1800_MH250_LH_2016postVFP.sigma  = 0.00025
Tprime_tAq_1800_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH350_LH_2016postVFP")
Tprime_tAq_1800_MH350_LH_2016postVFP.sigma  = 0.0003371
Tprime_tAq_1800_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH450_LH_2016postVFP")
Tprime_tAq_1800_MH450_LH_2016postVFP.sigma  = 0.0004113
Tprime_tAq_1800_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH500_LH_2016postVFP")
Tprime_tAq_1800_MH500_LH_2016postVFP.sigma  = 0.0004428
Tprime_tAq_1800_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1800_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH25_LH_2016postVFP")
Tprime_tAq_1900_MH25_LH_2016postVFP.sigma  = 1.696e-05
Tprime_tAq_1900_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH50_LH_2016postVFP")
Tprime_tAq_1900_MH50_LH_2016postVFP.sigma  = 4.037e-05
Tprime_tAq_1900_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH75_LH_2016postVFP")
Tprime_tAq_1900_MH75_LH_2016postVFP.sigma  = 6.23e-05
Tprime_tAq_1900_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH100_LH_2016postVFP")
Tprime_tAq_1900_MH100_LH_2016postVFP.sigma  = 8.373e-05
Tprime_tAq_1900_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH125_LH_2016postVFP")
Tprime_tAq_1900_MH125_LH_2016postVFP.sigma  = 0.0001048
Tprime_tAq_1900_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH150_LH_2016postVFP")
Tprime_tAq_1900_MH150_LH_2016postVFP.sigma  = 0.0001257
Tprime_tAq_1900_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH175_LH_2016postVFP")
Tprime_tAq_1900_MH175_LH_2016postVFP.sigma  = 0.0001461
Tprime_tAq_1900_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH200_LH_2016postVFP")
Tprime_tAq_1900_MH200_LH_2016postVFP.sigma  = 0.0001662
Tprime_tAq_1900_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH250_LH_2016postVFP")
Tprime_tAq_1900_MH250_LH_2016postVFP.sigma  = 0.0002061
Tprime_tAq_1900_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH350_LH_2016postVFP")
Tprime_tAq_1900_MH350_LH_2016postVFP.sigma  = 0.0002791
Tprime_tAq_1900_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH450_LH_2016postVFP")
Tprime_tAq_1900_MH450_LH_2016postVFP.sigma  = 0.000341
Tprime_tAq_1900_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH500_LH_2016postVFP")
Tprime_tAq_1900_MH500_LH_2016postVFP.sigma  = 0.0003716
Tprime_tAq_1900_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_1900_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH25_LH_2016postVFP")
Tprime_tAq_2000_MH25_LH_2016postVFP.sigma  = 1.39e-05
Tprime_tAq_2000_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH50_LH_2016postVFP")
Tprime_tAq_2000_MH50_LH_2016postVFP.sigma  = 3.308e-05
Tprime_tAq_2000_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH75_LH_2016postVFP")
Tprime_tAq_2000_MH75_LH_2016postVFP.sigma  = 5.107e-05
Tprime_tAq_2000_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH100_LH_2016postVFP")
Tprime_tAq_2000_MH100_LH_2016postVFP.sigma  = 6.868e-05
Tprime_tAq_2000_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH125_LH_2016postVFP")
Tprime_tAq_2000_MH125_LH_2016postVFP.sigma  = 8.602e-05
Tprime_tAq_2000_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH150_LH_2016postVFP")
Tprime_tAq_2000_MH150_LH_2016postVFP.sigma  = 0.0001031
Tprime_tAq_2000_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH175_LH_2016postVFP")
Tprime_tAq_2000_MH175_LH_2016postVFP.sigma  = 0.00012
Tprime_tAq_2000_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH200_LH_2016postVFP")
Tprime_tAq_2000_MH200_LH_2016postVFP.sigma  = 0.0001367
Tprime_tAq_2000_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH250_LH_2016postVFP")
Tprime_tAq_2000_MH250_LH_2016postVFP.sigma  = 0.000169
Tprime_tAq_2000_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH350_LH_2016postVFP")
Tprime_tAq_2000_MH350_LH_2016postVFP.sigma  = 0.0002297
Tprime_tAq_2000_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH450_LH_2016postVFP")
Tprime_tAq_2000_MH450_LH_2016postVFP.sigma  = 0.0002834
Tprime_tAq_2000_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH500_LH_2016postVFP")
Tprime_tAq_2000_MH500_LH_2016postVFP.sigma  = 0.0003069
Tprime_tAq_2000_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2000_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH25_LH_2016postVFP")
Tprime_tAq_2100_MH25_LH_2016postVFP.sigma  = 1.143e-05
Tprime_tAq_2100_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH50_LH_2016postVFP")
Tprime_tAq_2100_MH50_LH_2016postVFP.sigma  = 2.715e-05
Tprime_tAq_2100_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH75_LH_2016postVFP")
Tprime_tAq_2100_MH75_LH_2016postVFP.sigma  = 4.193e-05
Tprime_tAq_2100_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH100_LH_2016postVFP")
Tprime_tAq_2100_MH100_LH_2016postVFP.sigma  = 5.637e-05
Tprime_tAq_2100_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH125_LH_2016postVFP")
Tprime_tAq_2100_MH125_LH_2016postVFP.sigma  = 7.061e-05
Tprime_tAq_2100_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH150_LH_2016postVFP")
Tprime_tAq_2100_MH150_LH_2016postVFP.sigma  = 8.467e-05
Tprime_tAq_2100_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH175_LH_2016postVFP")
Tprime_tAq_2100_MH175_LH_2016postVFP.sigma  = 9.855e-05
Tprime_tAq_2100_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH200_LH_2016postVFP")
Tprime_tAq_2100_MH200_LH_2016postVFP.sigma  = 0.0001123
Tprime_tAq_2100_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH250_LH_2016postVFP")
Tprime_tAq_2100_MH250_LH_2016postVFP.sigma  = 0.0001395
Tprime_tAq_2100_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH350_LH_2016postVFP")
Tprime_tAq_2100_MH350_LH_2016postVFP.sigma  = 0.0001904
Tprime_tAq_2100_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH450_LH_2016postVFP")
Tprime_tAq_2100_MH450_LH_2016postVFP.sigma  = 0.0002359
Tprime_tAq_2100_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH500_LH_2016postVFP")
Tprime_tAq_2100_MH500_LH_2016postVFP.sigma  = 0.0002563
Tprime_tAq_2100_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2100_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH25_LH_2016postVFP")
Tprime_tAq_2200_MH25_LH_2016postVFP.sigma  = 9.434e-06
Tprime_tAq_2200_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH50_LH_2016postVFP")
Tprime_tAq_2200_MH50_LH_2016postVFP.sigma  = 2.246e-05
Tprime_tAq_2200_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH75_LH_2016postVFP")
Tprime_tAq_2200_MH75_LH_2016postVFP.sigma  = 3.467e-05
Tprime_tAq_2200_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH100_LH_2016postVFP")
Tprime_tAq_2200_MH100_LH_2016postVFP.sigma  = 4.672e-05
Tprime_tAq_2200_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH125_LH_2016postVFP")
Tprime_tAq_2200_MH125_LH_2016postVFP.sigma  = 5.855e-05
Tprime_tAq_2200_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH150_LH_2016postVFP")
Tprime_tAq_2200_MH150_LH_2016postVFP.sigma  = 7.027e-05
Tprime_tAq_2200_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH175_LH_2016postVFP")
Tprime_tAq_2200_MH175_LH_2016postVFP.sigma  = 8.19e-05
Tprime_tAq_2200_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH200_LH_2016postVFP")
Tprime_tAq_2200_MH200_LH_2016postVFP.sigma  = 9.334e-05
Tprime_tAq_2200_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH250_LH_2016postVFP")
Tprime_tAq_2200_MH250_LH_2016postVFP.sigma  = 0.0001157
Tprime_tAq_2200_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH350_LH_2016postVFP")
Tprime_tAq_2200_MH350_LH_2016postVFP.sigma  = 0.0001579
Tprime_tAq_2200_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH450_LH_2016postVFP")
Tprime_tAq_2200_MH450_LH_2016postVFP.sigma  = 0.0001955
Tprime_tAq_2200_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH500_LH_2016postVFP")
Tprime_tAq_2200_MH500_LH_2016postVFP.sigma  = 0.0002133
Tprime_tAq_2200_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2200_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH25_LH_2016postVFP")
Tprime_tAq_2300_MH25_LH_2016postVFP.sigma  = 7.755e-06
Tprime_tAq_2300_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH50_LH_2016postVFP")
Tprime_tAq_2300_MH50_LH_2016postVFP.sigma  = 1.848e-05
Tprime_tAq_2300_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH75_LH_2016postVFP")
Tprime_tAq_2300_MH75_LH_2016postVFP.sigma  = 2.853e-05
Tprime_tAq_2300_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH100_LH_2016postVFP")
Tprime_tAq_2300_MH100_LH_2016postVFP.sigma  = 3.837e-05
Tprime_tAq_2300_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH125_LH_2016postVFP")
Tprime_tAq_2300_MH125_LH_2016postVFP.sigma  = 4.81e-05
Tprime_tAq_2300_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH150_LH_2016postVFP")
Tprime_tAq_2300_MH150_LH_2016postVFP.sigma  = 5.757e-05
Tprime_tAq_2300_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH175_LH_2016postVFP")
Tprime_tAq_2300_MH175_LH_2016postVFP.sigma  = 6.703e-05
Tprime_tAq_2300_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH200_LH_2016postVFP")
Tprime_tAq_2300_MH200_LH_2016postVFP.sigma  = 7.641e-05
Tprime_tAq_2300_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH250_LH_2016postVFP")
Tprime_tAq_2300_MH250_LH_2016postVFP.sigma  = 9.486e-05
Tprime_tAq_2300_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH350_LH_2016postVFP")
Tprime_tAq_2300_MH350_LH_2016postVFP.sigma  = 0.0001299
Tprime_tAq_2300_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH450_LH_2016postVFP")
Tprime_tAq_2300_MH450_LH_2016postVFP.sigma  = 0.0001618
Tprime_tAq_2300_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH500_LH_2016postVFP")
Tprime_tAq_2300_MH500_LH_2016postVFP.sigma  = 0.0001764
Tprime_tAq_2300_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2300_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH25_LH_2016postVFP")
Tprime_tAq_2400_MH25_LH_2016postVFP.sigma  = 6.361e-06
Tprime_tAq_2400_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH50_LH_2016postVFP")
Tprime_tAq_2400_MH50_LH_2016postVFP.sigma  = 1.515e-05
Tprime_tAq_2400_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH75_LH_2016postVFP")
Tprime_tAq_2400_MH75_LH_2016postVFP.sigma  = 2.34e-05
Tprime_tAq_2400_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH100_LH_2016postVFP")
Tprime_tAq_2400_MH100_LH_2016postVFP.sigma  = 3.148e-05
Tprime_tAq_2400_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH125_LH_2016postVFP")
Tprime_tAq_2400_MH125_LH_2016postVFP.sigma  = 3.946e-05
Tprime_tAq_2400_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH150_LH_2016postVFP")
Tprime_tAq_2400_MH150_LH_2016postVFP.sigma  = 4.736e-05
Tprime_tAq_2400_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH175_LH_2016postVFP")
Tprime_tAq_2400_MH175_LH_2016postVFP.sigma  = 5.519e-05
Tprime_tAq_2400_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH200_LH_2016postVFP")
Tprime_tAq_2400_MH200_LH_2016postVFP.sigma  = 6.293e-05
Tprime_tAq_2400_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH250_LH_2016postVFP")
Tprime_tAq_2400_MH250_LH_2016postVFP.sigma  = 7.813e-05
Tprime_tAq_2400_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH350_LH_2016postVFP")
Tprime_tAq_2400_MH350_LH_2016postVFP.sigma  = 0.0001075
Tprime_tAq_2400_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH450_LH_2016postVFP")
Tprime_tAq_2400_MH450_LH_2016postVFP.sigma  = 0.0001343
Tprime_tAq_2400_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH500_LH_2016postVFP")
Tprime_tAq_2400_MH500_LH_2016postVFP.sigma  = 0.0001467
Tprime_tAq_2400_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2400_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH25_LH_2016postVFP")
Tprime_tAq_2500_MH25_LH_2016postVFP.sigma  = 5.237e-06
Tprime_tAq_2500_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH50_LH_2016postVFP")
Tprime_tAq_2500_MH50_LH_2016postVFP.sigma  = 1.247e-05
Tprime_tAq_2500_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH75_LH_2016postVFP")
Tprime_tAq_2500_MH75_LH_2016postVFP.sigma  = 1.926e-05
Tprime_tAq_2500_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH100_LH_2016postVFP")
Tprime_tAq_2500_MH100_LH_2016postVFP.sigma  = 2.59e-05
Tprime_tAq_2500_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH125_LH_2016postVFP")
Tprime_tAq_2500_MH125_LH_2016postVFP.sigma  = 3.251e-05
Tprime_tAq_2500_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH150_LH_2016postVFP")
Tprime_tAq_2500_MH150_LH_2016postVFP.sigma  = 3.901e-05
Tprime_tAq_2500_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH175_LH_2016postVFP")
Tprime_tAq_2500_MH175_LH_2016postVFP.sigma  = 4.547e-05
Tprime_tAq_2500_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH200_LH_2016postVFP")
Tprime_tAq_2500_MH200_LH_2016postVFP.sigma  = 5.186e-05
Tprime_tAq_2500_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH250_LH_2016postVFP")
Tprime_tAq_2500_MH250_LH_2016postVFP.sigma  = 6.452e-05
Tprime_tAq_2500_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH350_LH_2016postVFP")
Tprime_tAq_2500_MH350_LH_2016postVFP.sigma  = 8.859e-05
Tprime_tAq_2500_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH450_LH_2016postVFP")
Tprime_tAq_2500_MH450_LH_2016postVFP.sigma  = 0.0001111
Tprime_tAq_2500_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH500_LH_2016postVFP")
Tprime_tAq_2500_MH500_LH_2016postVFP.sigma  = 0.0001215
Tprime_tAq_2500_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2500_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH25_LH_2016postVFP")
Tprime_tAq_2600_MH25_LH_2016postVFP.sigma  = 4.255e-06
Tprime_tAq_2600_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH50_LH_2016postVFP")
Tprime_tAq_2600_MH50_LH_2016postVFP.sigma  = 1.015e-05
Tprime_tAq_2600_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH75_LH_2016postVFP")
Tprime_tAq_2600_MH75_LH_2016postVFP.sigma  = 1.568e-05
Tprime_tAq_2600_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH100_LH_2016postVFP")
Tprime_tAq_2600_MH100_LH_2016postVFP.sigma  = 2.11e-05
Tprime_tAq_2600_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH125_LH_2016postVFP")
Tprime_tAq_2600_MH125_LH_2016postVFP.sigma  = 2.646e-05
Tprime_tAq_2600_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH150_LH_2016postVFP")
Tprime_tAq_2600_MH150_LH_2016postVFP.sigma  = 3.171e-05
Tprime_tAq_2600_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH175_LH_2016postVFP")
Tprime_tAq_2600_MH175_LH_2016postVFP.sigma  = 3.697e-05
Tprime_tAq_2600_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH200_LH_2016postVFP")
Tprime_tAq_2600_MH200_LH_2016postVFP.sigma  = 4.218e-05
Tprime_tAq_2600_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH250_LH_2016postVFP")
Tprime_tAq_2600_MH250_LH_2016postVFP.sigma  = 5.243e-05
Tprime_tAq_2600_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH350_LH_2016postVFP")
Tprime_tAq_2600_MH350_LH_2016postVFP.sigma  = 7.213e-05
Tprime_tAq_2600_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH450_LH_2016postVFP")
Tprime_tAq_2600_MH450_LH_2016postVFP.sigma  = 9.067e-05
Tprime_tAq_2600_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH500_LH_2016postVFP")
Tprime_tAq_2600_MH500_LH_2016postVFP.sigma  = 9.929e-05
Tprime_tAq_2600_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2600_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH25_LH_2016postVFP")
Tprime_tAq_2700_MH25_LH_2016postVFP.sigma  = 3.545e-06
Tprime_tAq_2700_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH50_LH_2016postVFP")
Tprime_tAq_2700_MH50_LH_2016postVFP.sigma  = 8.424e-06
Tprime_tAq_2700_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH75_LH_2016postVFP")
Tprime_tAq_2700_MH75_LH_2016postVFP.sigma  = 1.301e-05
Tprime_tAq_2700_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH100_LH_2016postVFP")
Tprime_tAq_2700_MH100_LH_2016postVFP.sigma  = 1.751e-05
Tprime_tAq_2700_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH125_LH_2016postVFP")
Tprime_tAq_2700_MH125_LH_2016postVFP.sigma  = 2.196e-05
Tprime_tAq_2700_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH150_LH_2016postVFP")
Tprime_tAq_2700_MH150_LH_2016postVFP.sigma  = 2.643e-05
Tprime_tAq_2700_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH175_LH_2016postVFP")
Tprime_tAq_2700_MH175_LH_2016postVFP.sigma  = 3.084e-05
Tprime_tAq_2700_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH200_LH_2016postVFP")
Tprime_tAq_2700_MH200_LH_2016postVFP.sigma  = 3.519e-05
Tprime_tAq_2700_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH250_LH_2016postVFP")
Tprime_tAq_2700_MH250_LH_2016postVFP.sigma  = 4.376e-05
Tprime_tAq_2700_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH350_LH_2016postVFP")
Tprime_tAq_2700_MH350_LH_2016postVFP.sigma  = 6.03e-05
Tprime_tAq_2700_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH450_LH_2016postVFP")
Tprime_tAq_2700_MH450_LH_2016postVFP.sigma  = 7.577e-05
Tprime_tAq_2700_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH500_LH_2016postVFP")
Tprime_tAq_2700_MH500_LH_2016postVFP.sigma  = 8.31e-05
Tprime_tAq_2700_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2700_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH25_LH_2016postVFP")
Tprime_tAq_2800_MH25_LH_2016postVFP.sigma  = 2.937e-06
Tprime_tAq_2800_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH50_LH_2016postVFP")
Tprime_tAq_2800_MH50_LH_2016postVFP.sigma  = 6.968e-06
Tprime_tAq_2800_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH75_LH_2016postVFP")
Tprime_tAq_2800_MH75_LH_2016postVFP.sigma  = 1.076e-05
Tprime_tAq_2800_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH100_LH_2016postVFP")
Tprime_tAq_2800_MH100_LH_2016postVFP.sigma  = 1.448e-05
Tprime_tAq_2800_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH125_LH_2016postVFP")
Tprime_tAq_2800_MH125_LH_2016postVFP.sigma  = 1.817e-05
Tprime_tAq_2800_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH150_LH_2016postVFP")
Tprime_tAq_2800_MH150_LH_2016postVFP.sigma  = 2.177e-05
Tprime_tAq_2800_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH175_LH_2016postVFP")
Tprime_tAq_2800_MH175_LH_2016postVFP.sigma  = 2.538e-05
Tprime_tAq_2800_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH200_LH_2016postVFP")
Tprime_tAq_2800_MH200_LH_2016postVFP.sigma  = 2.896e-05
Tprime_tAq_2800_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH250_LH_2016postVFP")
Tprime_tAq_2800_MH250_LH_2016postVFP.sigma  = 3.6e-05
Tprime_tAq_2800_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH350_LH_2016postVFP")
Tprime_tAq_2800_MH350_LH_2016postVFP.sigma  = 4.967e-05
Tprime_tAq_2800_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH450_LH_2016postVFP")
Tprime_tAq_2800_MH450_LH_2016postVFP.sigma  = 6.256e-05
Tprime_tAq_2800_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH500_LH_2016postVFP")
Tprime_tAq_2800_MH500_LH_2016postVFP.sigma  = 6.865e-05
Tprime_tAq_2800_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2800_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH25_LH_2016postVFP")
Tprime_tAq_2900_MH25_LH_2016postVFP.sigma  = 2.403e-06
Tprime_tAq_2900_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH50_LH_2016postVFP")
Tprime_tAq_2900_MH50_LH_2016postVFP.sigma  = 5.726e-06
Tprime_tAq_2900_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH75_LH_2016postVFP")
Tprime_tAq_2900_MH75_LH_2016postVFP.sigma  = 8.842e-06
Tprime_tAq_2900_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH100_LH_2016postVFP")
Tprime_tAq_2900_MH100_LH_2016postVFP.sigma  = 1.19e-05
Tprime_tAq_2900_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH125_LH_2016postVFP")
Tprime_tAq_2900_MH125_LH_2016postVFP.sigma  = 1.493e-05
Tprime_tAq_2900_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH150_LH_2016postVFP")
Tprime_tAq_2900_MH150_LH_2016postVFP.sigma  = 1.793e-05
Tprime_tAq_2900_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH175_LH_2016postVFP")
Tprime_tAq_2900_MH175_LH_2016postVFP.sigma  = 2.091e-05
Tprime_tAq_2900_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH200_LH_2016postVFP")
Tprime_tAq_2900_MH200_LH_2016postVFP.sigma  = 2.387e-05
Tprime_tAq_2900_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH250_LH_2016postVFP")
Tprime_tAq_2900_MH250_LH_2016postVFP.sigma  = 2.971e-05
Tprime_tAq_2900_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH350_LH_2016postVFP")
Tprime_tAq_2900_MH350_LH_2016postVFP.sigma  = 4.106e-05
Tprime_tAq_2900_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH450_LH_2016postVFP")
Tprime_tAq_2900_MH450_LH_2016postVFP.sigma  = 5.175e-05
Tprime_tAq_2900_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH500_LH_2016postVFP")
Tprime_tAq_2900_MH500_LH_2016postVFP.sigma  = 5.69e-05
Tprime_tAq_2900_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_2900_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH25_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH25_LH_2016postVFP")
Tprime_tAq_3000_MH25_LH_2016postVFP.sigma  = 1.972e-06
Tprime_tAq_3000_MH25_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH25_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH50_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH50_LH_2016postVFP")
Tprime_tAq_3000_MH50_LH_2016postVFP.sigma  = 4.696e-06
Tprime_tAq_3000_MH50_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH50_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH75_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH75_LH_2016postVFP")
Tprime_tAq_3000_MH75_LH_2016postVFP.sigma  = 7.255e-06
Tprime_tAq_3000_MH75_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH75_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH100_LH_2016postVFP")
Tprime_tAq_3000_MH100_LH_2016postVFP.sigma  = 9.765e-06
Tprime_tAq_3000_MH100_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH100_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH125_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH125_LH_2016postVFP")
Tprime_tAq_3000_MH125_LH_2016postVFP.sigma  = 1.225e-05
Tprime_tAq_3000_MH125_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH125_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH150_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH150_LH_2016postVFP")
Tprime_tAq_3000_MH150_LH_2016postVFP.sigma  = 1.471e-05
Tprime_tAq_3000_MH150_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH150_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH175_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH175_LH_2016postVFP")
Tprime_tAq_3000_MH175_LH_2016postVFP.sigma  = 1.72e-05
Tprime_tAq_3000_MH175_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH175_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH200_LH_2016postVFP")
Tprime_tAq_3000_MH200_LH_2016postVFP.sigma  = 1.964e-05
Tprime_tAq_3000_MH200_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH200_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH250_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH250_LH_2016postVFP")
Tprime_tAq_3000_MH250_LH_2016postVFP.sigma  = 2.446e-05
Tprime_tAq_3000_MH250_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH250_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH350_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH350_LH_2016postVFP")
Tprime_tAq_3000_MH350_LH_2016postVFP.sigma  = 3.381e-05
Tprime_tAq_3000_MH350_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH350_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH450_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH450_LH_2016postVFP")
Tprime_tAq_3000_MH450_LH_2016postVFP.sigma  = 4.27e-05
Tprime_tAq_3000_MH450_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH450_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH500_LH_2016postVFP")
Tprime_tAq_3000_MH500_LH_2016postVFP.sigma  = 4.694e-05
Tprime_tAq_3000_MH500_LH_2016postVFP.year = 2016
Tprime_tAq_3000_MH500_LH_2016postVFP.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

# 2016postVFP bunches of tAq samples by MT mass

Tprime_tAq_600_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_LH_2016postVFP")
Tprime_tAq_600_LH_2016postVFP.year = 2016
Tprime_tAq_600_LH_2016postVFP.components = [Tprime_tAq_600_MH25_LH_2016postVFP, Tprime_tAq_600_MH50_LH_2016postVFP, Tprime_tAq_600_MH75_LH_2016postVFP, Tprime_tAq_600_MH100_LH_2016postVFP, Tprime_tAq_600_MH125_LH_2016postVFP, Tprime_tAq_600_MH150_LH_2016postVFP, Tprime_tAq_600_MH175_LH_2016postVFP, Tprime_tAq_600_MH200_LH_2016postVFP, Tprime_tAq_600_MH250_LH_2016postVFP, Tprime_tAq_600_MH350_LH_2016postVFP, Tprime_tAq_600_MH450_LH_2016postVFP, Tprime_tAq_600_MH500_LH_2016postVFP]

Tprime_tAq_700_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_LH_2016postVFP")
Tprime_tAq_700_LH_2016postVFP.year = 2016
Tprime_tAq_700_LH_2016postVFP.components = [Tprime_tAq_700_MH25_LH_2016postVFP, Tprime_tAq_700_MH50_LH_2016postVFP, Tprime_tAq_700_MH75_LH_2016postVFP, Tprime_tAq_700_MH100_LH_2016postVFP, Tprime_tAq_700_MH125_LH_2016postVFP, Tprime_tAq_700_MH150_LH_2016postVFP, Tprime_tAq_700_MH175_LH_2016postVFP, Tprime_tAq_700_MH200_LH_2016postVFP, Tprime_tAq_700_MH250_LH_2016postVFP, Tprime_tAq_700_MH350_LH_2016postVFP, Tprime_tAq_700_MH450_LH_2016postVFP, Tprime_tAq_700_MH500_LH_2016postVFP]

Tprime_tAq_800_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_LH_2016postVFP")
Tprime_tAq_800_LH_2016postVFP.year = 2016
Tprime_tAq_800_LH_2016postVFP.components = [Tprime_tAq_800_MH25_LH_2016postVFP, Tprime_tAq_800_MH50_LH_2016postVFP, Tprime_tAq_800_MH75_LH_2016postVFP, Tprime_tAq_800_MH100_LH_2016postVFP, Tprime_tAq_800_MH125_LH_2016postVFP, Tprime_tAq_800_MH150_LH_2016postVFP, Tprime_tAq_800_MH175_LH_2016postVFP, Tprime_tAq_800_MH200_LH_2016postVFP, Tprime_tAq_800_MH250_LH_2016postVFP, Tprime_tAq_800_MH350_LH_2016postVFP, Tprime_tAq_800_MH450_LH_2016postVFP, Tprime_tAq_800_MH500_LH_2016postVFP]

Tprime_tAq_900_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_LH_2016postVFP")
Tprime_tAq_900_LH_2016postVFP.year = 2016
Tprime_tAq_900_LH_2016postVFP.components = [Tprime_tAq_900_MH25_LH_2016postVFP, Tprime_tAq_900_MH50_LH_2016postVFP, Tprime_tAq_900_MH75_LH_2016postVFP, Tprime_tAq_900_MH100_LH_2016postVFP, Tprime_tAq_900_MH125_LH_2016postVFP, Tprime_tAq_900_MH150_LH_2016postVFP, Tprime_tAq_900_MH175_LH_2016postVFP, Tprime_tAq_900_MH200_LH_2016postVFP, Tprime_tAq_900_MH250_LH_2016postVFP, Tprime_tAq_900_MH350_LH_2016postVFP, Tprime_tAq_900_MH450_LH_2016postVFP, Tprime_tAq_900_MH500_LH_2016postVFP]

Tprime_tAq_1000_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_LH_2016postVFP")
Tprime_tAq_1000_LH_2016postVFP.year = 2016
Tprime_tAq_1000_LH_2016postVFP.components = [Tprime_tAq_1000_MH25_LH_2016postVFP, Tprime_tAq_1000_MH50_LH_2016postVFP, Tprime_tAq_1000_MH75_LH_2016postVFP, Tprime_tAq_1000_MH100_LH_2016postVFP, Tprime_tAq_1000_MH125_LH_2016postVFP, Tprime_tAq_1000_MH150_LH_2016postVFP, Tprime_tAq_1000_MH175_LH_2016postVFP, Tprime_tAq_1000_MH200_LH_2016postVFP, Tprime_tAq_1000_MH250_LH_2016postVFP, Tprime_tAq_1000_MH350_LH_2016postVFP, Tprime_tAq_1000_MH450_LH_2016postVFP, Tprime_tAq_1000_MH500_LH_2016postVFP]

Tprime_tAq_1100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_LH_2016postVFP")
Tprime_tAq_1100_LH_2016postVFP.year = 2016
Tprime_tAq_1100_LH_2016postVFP.components = [Tprime_tAq_1100_MH25_LH_2016postVFP, Tprime_tAq_1100_MH50_LH_2016postVFP, Tprime_tAq_1100_MH75_LH_2016postVFP, Tprime_tAq_1100_MH100_LH_2016postVFP, Tprime_tAq_1100_MH125_LH_2016postVFP, Tprime_tAq_1100_MH150_LH_2016postVFP, Tprime_tAq_1100_MH175_LH_2016postVFP, Tprime_tAq_1100_MH200_LH_2016postVFP, Tprime_tAq_1100_MH250_LH_2016postVFP, Tprime_tAq_1100_MH350_LH_2016postVFP, Tprime_tAq_1100_MH450_LH_2016postVFP, Tprime_tAq_1100_MH500_LH_2016postVFP]

Tprime_tAq_1200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_LH_2016postVFP")
Tprime_tAq_1200_LH_2016postVFP.year = 2016
Tprime_tAq_1200_LH_2016postVFP.components = [Tprime_tAq_1200_MH25_LH_2016postVFP, Tprime_tAq_1200_MH50_LH_2016postVFP, Tprime_tAq_1200_MH75_LH_2016postVFP, Tprime_tAq_1200_MH100_LH_2016postVFP, Tprime_tAq_1200_MH125_LH_2016postVFP, Tprime_tAq_1200_MH150_LH_2016postVFP, Tprime_tAq_1200_MH175_LH_2016postVFP, Tprime_tAq_1200_MH200_LH_2016postVFP, Tprime_tAq_1200_MH250_LH_2016postVFP, Tprime_tAq_1200_MH350_LH_2016postVFP, Tprime_tAq_1200_MH450_LH_2016postVFP, Tprime_tAq_1200_MH500_LH_2016postVFP]

Tprime_tAq_1300_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_LH_2016postVFP")
Tprime_tAq_1300_LH_2016postVFP.year = 2016
Tprime_tAq_1300_LH_2016postVFP.components = [Tprime_tAq_1300_MH25_LH_2016postVFP, Tprime_tAq_1300_MH50_LH_2016postVFP, Tprime_tAq_1300_MH75_LH_2016postVFP, Tprime_tAq_1300_MH100_LH_2016postVFP, Tprime_tAq_1300_MH125_LH_2016postVFP, Tprime_tAq_1300_MH150_LH_2016postVFP, Tprime_tAq_1300_MH175_LH_2016postVFP, Tprime_tAq_1300_MH200_LH_2016postVFP, Tprime_tAq_1300_MH250_LH_2016postVFP, Tprime_tAq_1300_MH350_LH_2016postVFP, Tprime_tAq_1300_MH450_LH_2016postVFP, Tprime_tAq_1300_MH500_LH_2016postVFP]

Tprime_tAq_1400_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_LH_2016postVFP")
Tprime_tAq_1400_LH_2016postVFP.year = 2016
Tprime_tAq_1400_LH_2016postVFP.components = [Tprime_tAq_1400_MH25_LH_2016postVFP, Tprime_tAq_1400_MH50_LH_2016postVFP, Tprime_tAq_1400_MH75_LH_2016postVFP, Tprime_tAq_1400_MH100_LH_2016postVFP, Tprime_tAq_1400_MH125_LH_2016postVFP, Tprime_tAq_1400_MH150_LH_2016postVFP, Tprime_tAq_1400_MH175_LH_2016postVFP, Tprime_tAq_1400_MH200_LH_2016postVFP, Tprime_tAq_1400_MH250_LH_2016postVFP, Tprime_tAq_1400_MH350_LH_2016postVFP, Tprime_tAq_1400_MH450_LH_2016postVFP, Tprime_tAq_1400_MH500_LH_2016postVFP]

Tprime_tAq_1500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_LH_2016postVFP")
Tprime_tAq_1500_LH_2016postVFP.year = 2016
Tprime_tAq_1500_LH_2016postVFP.components = [Tprime_tAq_1500_MH25_LH_2016postVFP, Tprime_tAq_1500_MH50_LH_2016postVFP, Tprime_tAq_1500_MH75_LH_2016postVFP, Tprime_tAq_1500_MH100_LH_2016postVFP, Tprime_tAq_1500_MH125_LH_2016postVFP, Tprime_tAq_1500_MH150_LH_2016postVFP, Tprime_tAq_1500_MH175_LH_2016postVFP, Tprime_tAq_1500_MH200_LH_2016postVFP, Tprime_tAq_1500_MH250_LH_2016postVFP, Tprime_tAq_1500_MH350_LH_2016postVFP, Tprime_tAq_1500_MH450_LH_2016postVFP, Tprime_tAq_1500_MH500_LH_2016postVFP]

Tprime_tAq_1600_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_LH_2016postVFP")
Tprime_tAq_1600_LH_2016postVFP.year = 2016
Tprime_tAq_1600_LH_2016postVFP.components = [Tprime_tAq_1600_MH25_LH_2016postVFP, Tprime_tAq_1600_MH50_LH_2016postVFP, Tprime_tAq_1600_MH75_LH_2016postVFP, Tprime_tAq_1600_MH100_LH_2016postVFP, Tprime_tAq_1600_MH125_LH_2016postVFP, Tprime_tAq_1600_MH150_LH_2016postVFP, Tprime_tAq_1600_MH175_LH_2016postVFP, Tprime_tAq_1600_MH200_LH_2016postVFP, Tprime_tAq_1600_MH250_LH_2016postVFP, Tprime_tAq_1600_MH350_LH_2016postVFP, Tprime_tAq_1600_MH450_LH_2016postVFP, Tprime_tAq_1600_MH500_LH_2016postVFP]

Tprime_tAq_1700_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_LH_2016postVFP")
Tprime_tAq_1700_LH_2016postVFP.year = 2016
Tprime_tAq_1700_LH_2016postVFP.components = [Tprime_tAq_1700_MH25_LH_2016postVFP, Tprime_tAq_1700_MH50_LH_2016postVFP, Tprime_tAq_1700_MH75_LH_2016postVFP, Tprime_tAq_1700_MH100_LH_2016postVFP, Tprime_tAq_1700_MH125_LH_2016postVFP, Tprime_tAq_1700_MH150_LH_2016postVFP, Tprime_tAq_1700_MH175_LH_2016postVFP, Tprime_tAq_1700_MH200_LH_2016postVFP, Tprime_tAq_1700_MH250_LH_2016postVFP, Tprime_tAq_1700_MH350_LH_2016postVFP, Tprime_tAq_1700_MH450_LH_2016postVFP, Tprime_tAq_1700_MH500_LH_2016postVFP]

Tprime_tAq_1800_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_LH_2016postVFP")
Tprime_tAq_1800_LH_2016postVFP.year = 2016
Tprime_tAq_1800_LH_2016postVFP.components = [Tprime_tAq_1800_MH25_LH_2016postVFP, Tprime_tAq_1800_MH50_LH_2016postVFP, Tprime_tAq_1800_MH75_LH_2016postVFP, Tprime_tAq_1800_MH100_LH_2016postVFP, Tprime_tAq_1800_MH125_LH_2016postVFP, Tprime_tAq_1800_MH150_LH_2016postVFP, Tprime_tAq_1800_MH175_LH_2016postVFP, Tprime_tAq_1800_MH200_LH_2016postVFP, Tprime_tAq_1800_MH250_LH_2016postVFP, Tprime_tAq_1800_MH350_LH_2016postVFP, Tprime_tAq_1800_MH450_LH_2016postVFP, Tprime_tAq_1800_MH500_LH_2016postVFP]

Tprime_tAq_1900_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_LH_2016postVFP")
Tprime_tAq_1900_LH_2016postVFP.year = 2016
Tprime_tAq_1900_LH_2016postVFP.components = [Tprime_tAq_1900_MH25_LH_2016postVFP, Tprime_tAq_1900_MH50_LH_2016postVFP, Tprime_tAq_1900_MH75_LH_2016postVFP, Tprime_tAq_1900_MH100_LH_2016postVFP, Tprime_tAq_1900_MH125_LH_2016postVFP, Tprime_tAq_1900_MH150_LH_2016postVFP, Tprime_tAq_1900_MH175_LH_2016postVFP, Tprime_tAq_1900_MH200_LH_2016postVFP, Tprime_tAq_1900_MH250_LH_2016postVFP, Tprime_tAq_1900_MH350_LH_2016postVFP, Tprime_tAq_1900_MH450_LH_2016postVFP, Tprime_tAq_1900_MH500_LH_2016postVFP]

Tprime_tAq_2000_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_LH_2016postVFP")
Tprime_tAq_2000_LH_2016postVFP.year = 2016
Tprime_tAq_2000_LH_2016postVFP.components = [Tprime_tAq_2000_MH25_LH_2016postVFP, Tprime_tAq_2000_MH50_LH_2016postVFP, Tprime_tAq_2000_MH75_LH_2016postVFP, Tprime_tAq_2000_MH100_LH_2016postVFP, Tprime_tAq_2000_MH125_LH_2016postVFP, Tprime_tAq_2000_MH150_LH_2016postVFP, Tprime_tAq_2000_MH175_LH_2016postVFP, Tprime_tAq_2000_MH200_LH_2016postVFP, Tprime_tAq_2000_MH250_LH_2016postVFP, Tprime_tAq_2000_MH350_LH_2016postVFP, Tprime_tAq_2000_MH450_LH_2016postVFP, Tprime_tAq_2000_MH500_LH_2016postVFP]

Tprime_tAq_2100_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_LH_2016postVFP")
Tprime_tAq_2100_LH_2016postVFP.year = 2016
Tprime_tAq_2100_LH_2016postVFP.components = [Tprime_tAq_2100_MH25_LH_2016postVFP, Tprime_tAq_2100_MH50_LH_2016postVFP, Tprime_tAq_2100_MH75_LH_2016postVFP, Tprime_tAq_2100_MH100_LH_2016postVFP, Tprime_tAq_2100_MH125_LH_2016postVFP, Tprime_tAq_2100_MH150_LH_2016postVFP, Tprime_tAq_2100_MH175_LH_2016postVFP, Tprime_tAq_2100_MH200_LH_2016postVFP, Tprime_tAq_2100_MH250_LH_2016postVFP, Tprime_tAq_2100_MH350_LH_2016postVFP, Tprime_tAq_2100_MH450_LH_2016postVFP, Tprime_tAq_2100_MH500_LH_2016postVFP]

Tprime_tAq_2200_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_LH_2016postVFP")
Tprime_tAq_2200_LH_2016postVFP.year = 2016
Tprime_tAq_2200_LH_2016postVFP.components = [Tprime_tAq_2200_MH25_LH_2016postVFP, Tprime_tAq_2200_MH50_LH_2016postVFP, Tprime_tAq_2200_MH75_LH_2016postVFP, Tprime_tAq_2200_MH100_LH_2016postVFP, Tprime_tAq_2200_MH125_LH_2016postVFP, Tprime_tAq_2200_MH150_LH_2016postVFP, Tprime_tAq_2200_MH175_LH_2016postVFP, Tprime_tAq_2200_MH200_LH_2016postVFP, Tprime_tAq_2200_MH250_LH_2016postVFP, Tprime_tAq_2200_MH350_LH_2016postVFP, Tprime_tAq_2200_MH450_LH_2016postVFP, Tprime_tAq_2200_MH500_LH_2016postVFP]

Tprime_tAq_2300_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_LH_2016postVFP")
Tprime_tAq_2300_LH_2016postVFP.year = 2016
Tprime_tAq_2300_LH_2016postVFP.components = [Tprime_tAq_2300_MH25_LH_2016postVFP, Tprime_tAq_2300_MH50_LH_2016postVFP, Tprime_tAq_2300_MH75_LH_2016postVFP, Tprime_tAq_2300_MH100_LH_2016postVFP, Tprime_tAq_2300_MH125_LH_2016postVFP, Tprime_tAq_2300_MH150_LH_2016postVFP, Tprime_tAq_2300_MH175_LH_2016postVFP, Tprime_tAq_2300_MH200_LH_2016postVFP, Tprime_tAq_2300_MH250_LH_2016postVFP, Tprime_tAq_2300_MH350_LH_2016postVFP, Tprime_tAq_2300_MH450_LH_2016postVFP, Tprime_tAq_2300_MH500_LH_2016postVFP]

Tprime_tAq_2400_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_LH_2016postVFP")
Tprime_tAq_2400_LH_2016postVFP.year = 2016
Tprime_tAq_2400_LH_2016postVFP.components = [Tprime_tAq_2400_MH25_LH_2016postVFP, Tprime_tAq_2400_MH50_LH_2016postVFP, Tprime_tAq_2400_MH75_LH_2016postVFP, Tprime_tAq_2400_MH100_LH_2016postVFP, Tprime_tAq_2400_MH125_LH_2016postVFP, Tprime_tAq_2400_MH150_LH_2016postVFP, Tprime_tAq_2400_MH175_LH_2016postVFP, Tprime_tAq_2400_MH200_LH_2016postVFP, Tprime_tAq_2400_MH250_LH_2016postVFP, Tprime_tAq_2400_MH350_LH_2016postVFP, Tprime_tAq_2400_MH450_LH_2016postVFP, Tprime_tAq_2400_MH500_LH_2016postVFP]

Tprime_tAq_2500_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_LH_2016postVFP")
Tprime_tAq_2500_LH_2016postVFP.year = 2016
Tprime_tAq_2500_LH_2016postVFP.components = [Tprime_tAq_2500_MH25_LH_2016postVFP, Tprime_tAq_2500_MH50_LH_2016postVFP, Tprime_tAq_2500_MH75_LH_2016postVFP, Tprime_tAq_2500_MH100_LH_2016postVFP, Tprime_tAq_2500_MH125_LH_2016postVFP, Tprime_tAq_2500_MH150_LH_2016postVFP, Tprime_tAq_2500_MH175_LH_2016postVFP, Tprime_tAq_2500_MH200_LH_2016postVFP, Tprime_tAq_2500_MH250_LH_2016postVFP, Tprime_tAq_2500_MH350_LH_2016postVFP, Tprime_tAq_2500_MH450_LH_2016postVFP, Tprime_tAq_2500_MH500_LH_2016postVFP]

Tprime_tAq_2600_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_LH_2016postVFP")
Tprime_tAq_2600_LH_2016postVFP.year = 2016
Tprime_tAq_2600_LH_2016postVFP.components = [Tprime_tAq_2600_MH25_LH_2016postVFP, Tprime_tAq_2600_MH50_LH_2016postVFP, Tprime_tAq_2600_MH75_LH_2016postVFP, Tprime_tAq_2600_MH100_LH_2016postVFP, Tprime_tAq_2600_MH125_LH_2016postVFP, Tprime_tAq_2600_MH150_LH_2016postVFP, Tprime_tAq_2600_MH175_LH_2016postVFP, Tprime_tAq_2600_MH200_LH_2016postVFP, Tprime_tAq_2600_MH250_LH_2016postVFP, Tprime_tAq_2600_MH350_LH_2016postVFP, Tprime_tAq_2600_MH450_LH_2016postVFP, Tprime_tAq_2600_MH500_LH_2016postVFP]

Tprime_tAq_2700_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_LH_2016postVFP")
Tprime_tAq_2700_LH_2016postVFP.year = 2016
Tprime_tAq_2700_LH_2016postVFP.components = [Tprime_tAq_2700_MH25_LH_2016postVFP, Tprime_tAq_2700_MH50_LH_2016postVFP, Tprime_tAq_2700_MH75_LH_2016postVFP, Tprime_tAq_2700_MH100_LH_2016postVFP, Tprime_tAq_2700_MH125_LH_2016postVFP, Tprime_tAq_2700_MH150_LH_2016postVFP, Tprime_tAq_2700_MH175_LH_2016postVFP, Tprime_tAq_2700_MH200_LH_2016postVFP, Tprime_tAq_2700_MH250_LH_2016postVFP, Tprime_tAq_2700_MH350_LH_2016postVFP, Tprime_tAq_2700_MH450_LH_2016postVFP, Tprime_tAq_2700_MH500_LH_2016postVFP]

Tprime_tAq_2800_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_LH_2016postVFP")
Tprime_tAq_2800_LH_2016postVFP.year = 2016
Tprime_tAq_2800_LH_2016postVFP.components = [Tprime_tAq_2800_MH25_LH_2016postVFP, Tprime_tAq_2800_MH50_LH_2016postVFP, Tprime_tAq_2800_MH75_LH_2016postVFP, Tprime_tAq_2800_MH100_LH_2016postVFP, Tprime_tAq_2800_MH125_LH_2016postVFP, Tprime_tAq_2800_MH150_LH_2016postVFP, Tprime_tAq_2800_MH175_LH_2016postVFP, Tprime_tAq_2800_MH200_LH_2016postVFP, Tprime_tAq_2800_MH250_LH_2016postVFP, Tprime_tAq_2800_MH350_LH_2016postVFP, Tprime_tAq_2800_MH450_LH_2016postVFP, Tprime_tAq_2800_MH500_LH_2016postVFP]

Tprime_tAq_2900_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_LH_2016postVFP")
Tprime_tAq_2900_LH_2016postVFP.year = 2016
Tprime_tAq_2900_LH_2016postVFP.components = [Tprime_tAq_2900_MH25_LH_2016postVFP, Tprime_tAq_2900_MH50_LH_2016postVFP, Tprime_tAq_2900_MH75_LH_2016postVFP, Tprime_tAq_2900_MH100_LH_2016postVFP, Tprime_tAq_2900_MH125_LH_2016postVFP, Tprime_tAq_2900_MH150_LH_2016postVFP, Tprime_tAq_2900_MH175_LH_2016postVFP, Tprime_tAq_2900_MH200_LH_2016postVFP, Tprime_tAq_2900_MH250_LH_2016postVFP, Tprime_tAq_2900_MH350_LH_2016postVFP, Tprime_tAq_2900_MH450_LH_2016postVFP, Tprime_tAq_2900_MH500_LH_2016postVFP]

Tprime_tAq_3000_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_LH_2016postVFP")
Tprime_tAq_3000_LH_2016postVFP.year = 2016
Tprime_tAq_3000_LH_2016postVFP.components = [Tprime_tAq_3000_MH25_LH_2016postVFP, Tprime_tAq_3000_MH50_LH_2016postVFP, Tprime_tAq_3000_MH75_LH_2016postVFP, Tprime_tAq_3000_MH100_LH_2016postVFP, Tprime_tAq_3000_MH125_LH_2016postVFP, Tprime_tAq_3000_MH150_LH_2016postVFP, Tprime_tAq_3000_MH175_LH_2016postVFP, Tprime_tAq_3000_MH200_LH_2016postVFP, Tprime_tAq_3000_MH250_LH_2016postVFP, Tprime_tAq_3000_MH350_LH_2016postVFP, Tprime_tAq_3000_MH450_LH_2016postVFP, Tprime_tAq_3000_MH500_LH_2016postVFP]


#Tprime_tAq_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_tAq_LH_2016postVFP")
#Tprime_tAq_LH_2016postVFP.year = 2016


### 2017 ####

# MT=600
Tprime_tAq_600_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH25_LH_2017")
Tprime_tAq_600_MH25_LH_2017.sigma  = 0.0002725
Tprime_tAq_600_MH25_LH_2017.year = 2017
Tprime_tAq_600_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH50_LH_2017")
Tprime_tAq_600_MH50_LH_2017.sigma  = 0.0006501
Tprime_tAq_600_MH50_LH_2017.year = 2017
Tprime_tAq_600_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH75_LH_2017")
Tprime_tAq_600_MH75_LH_2017.sigma  = 0.0009798
Tprime_tAq_600_MH75_LH_2017.year = 2017
Tprime_tAq_600_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH100_LH_2017")
Tprime_tAq_600_MH100_LH_2017.sigma  = 0.001275
Tprime_tAq_600_MH100_LH_2017.year = 2017
Tprime_tAq_600_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH125_LH_2017")
Tprime_tAq_600_MH125_LH_2017.sigma  = 0.001559
Tprime_tAq_600_MH125_LH_2017.year = 2017
Tprime_tAq_600_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH150_LH_2017")
Tprime_tAq_600_MH150_LH_2017.sigma  = 0.001796
Tprime_tAq_600_MH150_LH_2017.year = 2017
Tprime_tAq_600_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH175_LH_2017")
Tprime_tAq_600_MH175_LH_2017.sigma  = 0.001981
Tprime_tAq_600_MH175_LH_2017.year = 2017
Tprime_tAq_600_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH200_LH_2017")
Tprime_tAq_600_MH200_LH_2017.sigma  = 0.002091
Tprime_tAq_600_MH200_LH_2017.year = 2017
Tprime_tAq_600_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH250_LH_2017")
Tprime_tAq_600_MH250_LH_2017.sigma  = 0.002244
Tprime_tAq_600_MH250_LH_2017.year = 2017
Tprime_tAq_600_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH350_LH_2017")
Tprime_tAq_600_MH350_LH_2017.sigma  = 0.001713
Tprime_tAq_600_MH350_LH_2017.year = 2017
Tprime_tAq_600_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH450_LH_2017")
Tprime_tAq_600_MH450_LH_2017.sigma  = 1.434e-05
Tprime_tAq_600_MH450_LH_2017.year = 2017
Tprime_tAq_600_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_600_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH500_LH_2017")
Tprime_tAq_600_MH500_LH_2017.sigma  = 8.239e-08
Tprime_tAq_600_MH500_LH_2017.year = 2017
Tprime_tAq_600_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH25_LH_2017")
Tprime_tAq_700_MH25_LH_2017.sigma  = 0.000217
Tprime_tAq_700_MH25_LH_2017.year = 2017
Tprime_tAq_700_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH50_LH_2017")
Tprime_tAq_700_MH50_LH_2017.sigma  = 0.000511
Tprime_tAq_700_MH50_LH_2017.year = 2017
Tprime_tAq_700_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH75_LH_2017")
Tprime_tAq_700_MH75_LH_2017.sigma  = 0.0007798
Tprime_tAq_700_MH75_LH_2017.year = 2017
Tprime_tAq_700_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH100_LH_2017")
Tprime_tAq_700_MH100_LH_2017.sigma  = 0.00103
Tprime_tAq_700_MH100_LH_2017.year = 2017
Tprime_tAq_700_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH125_LH_2017")
Tprime_tAq_700_MH125_LH_2017.sigma  = 0.001251
Tprime_tAq_700_MH125_LH_2017.year = 2017
Tprime_tAq_700_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH150_LH_2017")
Tprime_tAq_700_MH150_LH_2017.sigma  = 0.001467
Tprime_tAq_700_MH150_LH_2017.year = 2017
Tprime_tAq_700_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH175_LH_2017")
Tprime_tAq_700_MH175_LH_2017.sigma  = 0.001651
Tprime_tAq_700_MH175_LH_2017.year = 2017
Tprime_tAq_700_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH200_LH_2017")
Tprime_tAq_700_MH200_LH_2017.sigma  = 0.001806
Tprime_tAq_700_MH200_LH_2017.year = 2017
Tprime_tAq_700_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH250_LH_2017")
Tprime_tAq_700_MH250_LH_2017.sigma  = 0.002018
Tprime_tAq_700_MH250_LH_2017.year = 2017
Tprime_tAq_700_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH350_LH_2017")
Tprime_tAq_700_MH350_LH_2017.sigma  = 0.001986
Tprime_tAq_700_MH350_LH_2017.year = 2017
Tprime_tAq_700_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH450_LH_2017")
Tprime_tAq_700_MH450_LH_2017.sigma  = 0.001326
Tprime_tAq_700_MH450_LH_2017.year = 2017
Tprime_tAq_700_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_700_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH500_LH_2017")
Tprime_tAq_700_MH500_LH_2017.sigma  = 0.0007135
Tprime_tAq_700_MH500_LH_2017.year = 2017
Tprime_tAq_700_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH25_LH_2017")
Tprime_tAq_800_MH25_LH_2017.sigma  = 0.000168
Tprime_tAq_800_MH25_LH_2017.year = 2017
Tprime_tAq_800_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH50_LH_2017")
Tprime_tAq_800_MH50_LH_2017.sigma  = 0.0003993
Tprime_tAq_800_MH50_LH_2017.year = 2017
Tprime_tAq_800_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH75_LH_2017")
Tprime_tAq_800_MH75_LH_2017.sigma  = 0.0006061
Tprime_tAq_800_MH75_LH_2017.year = 2017
Tprime_tAq_800_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH100_LH_2017")
Tprime_tAq_800_MH100_LH_2017.sigma  = 0.0008047
Tprime_tAq_800_MH100_LH_2017.year = 2017
Tprime_tAq_800_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH125_LH_2017")
Tprime_tAq_800_MH125_LH_2017.sigma  = 0.0009924
Tprime_tAq_800_MH125_LH_2017.year = 2017
Tprime_tAq_800_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH150_LH_2017")
Tprime_tAq_800_MH150_LH_2017.sigma  = 0.001166
Tprime_tAq_800_MH150_LH_2017.year = 2017
Tprime_tAq_800_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH175_LH_2017")
Tprime_tAq_800_MH175_LH_2017.sigma  = 0.001324
Tprime_tAq_800_MH175_LH_2017.year = 2017
Tprime_tAq_800_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH200_LH_2017")
Tprime_tAq_800_MH200_LH_2017.sigma  = 0.001468
Tprime_tAq_800_MH200_LH_2017.year = 2017
Tprime_tAq_800_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH250_LH_2017")
Tprime_tAq_800_MH250_LH_2017.sigma  = 0.001708
Tprime_tAq_800_MH250_LH_2017.year = 2017
Tprime_tAq_800_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH350_LH_2017")
Tprime_tAq_800_MH350_LH_2017.sigma  = 0.001872
Tprime_tAq_800_MH350_LH_2017.year = 2017
Tprime_tAq_800_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH450_LH_2017")
Tprime_tAq_800_MH450_LH_2017.sigma  = 0.00164
Tprime_tAq_800_MH450_LH_2017.year = 2017
Tprime_tAq_800_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_800_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH500_LH_2017")
Tprime_tAq_800_MH500_LH_2017.sigma  = 0.001371
Tprime_tAq_800_MH500_LH_2017.year = 2017
Tprime_tAq_800_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH25_LH_2017")
Tprime_tAq_900_MH25_LH_2017.sigma  = 0.0001338
Tprime_tAq_900_MH25_LH_2017.year = 2017
Tprime_tAq_900_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH50_LH_2017")
Tprime_tAq_900_MH50_LH_2017.sigma  = 0.0003153
Tprime_tAq_900_MH50_LH_2017.year = 2017
Tprime_tAq_900_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH75_LH_2017")
Tprime_tAq_900_MH75_LH_2017.sigma  = 0.0004835
Tprime_tAq_900_MH75_LH_2017.year = 2017
Tprime_tAq_900_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH100_LH_2017")
Tprime_tAq_900_MH100_LH_2017.sigma  = 0.0006426
Tprime_tAq_900_MH100_LH_2017.year = 2017
Tprime_tAq_900_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH125_LH_2017")
Tprime_tAq_900_MH125_LH_2017.sigma  = 0.0007962
Tprime_tAq_900_MH125_LH_2017.year = 2017
Tprime_tAq_900_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH150_LH_2017")
Tprime_tAq_900_MH150_LH_2017.sigma  = 0.0009446
Tprime_tAq_900_MH150_LH_2017.year = 2017
Tprime_tAq_900_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH175_LH_2017")
Tprime_tAq_900_MH175_LH_2017.sigma  = 0.001081
Tprime_tAq_900_MH175_LH_2017.year = 2017
Tprime_tAq_900_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH200_LH_2017")
Tprime_tAq_900_MH200_LH_2017.sigma  = 0.001203
Tprime_tAq_900_MH200_LH_2017.year = 2017
Tprime_tAq_900_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH250_LH_2017")
Tprime_tAq_900_MH250_LH_2017.sigma  = 0.001414
Tprime_tAq_900_MH250_LH_2017.year = 2017
Tprime_tAq_900_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH350_LH_2017")
Tprime_tAq_900_MH350_LH_2017.sigma  = 0.001681
Tprime_tAq_900_MH350_LH_2017.year = 2017
Tprime_tAq_900_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH450_LH_2017")
Tprime_tAq_900_MH450_LH_2017.sigma  = 0.001634
Tprime_tAq_900_MH450_LH_2017.year = 2017
Tprime_tAq_900_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_900_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH500_LH_2017")
Tprime_tAq_900_MH500_LH_2017.sigma  = 0.001522
Tprime_tAq_900_MH500_LH_2017.year = 2017
Tprime_tAq_900_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH25_LH_2017")
Tprime_tAq_1000_MH25_LH_2017.sigma  = 0.0001052
Tprime_tAq_1000_MH25_LH_2017.year = 2017
Tprime_tAq_1000_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH50_LH_2017")
Tprime_tAq_1000_MH50_LH_2017.sigma  = 0.0002505
Tprime_tAq_1000_MH50_LH_2017.year = 2017
Tprime_tAq_1000_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH75_LH_2017")
Tprime_tAq_1000_MH75_LH_2017.sigma  = 0.0003843
Tprime_tAq_1000_MH75_LH_2017.year = 2017
Tprime_tAq_1000_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH100_LH_2017")
Tprime_tAq_1000_MH100_LH_2017.sigma  = 0.0005132
Tprime_tAq_1000_MH100_LH_2017.year = 2017
Tprime_tAq_1000_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH125_LH_2017")
Tprime_tAq_1000_MH125_LH_2017.sigma  = 0.0006371
Tprime_tAq_1000_MH125_LH_2017.year = 2017
Tprime_tAq_1000_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH150_LH_2017")
Tprime_tAq_1000_MH150_LH_2017.sigma  = 0.0007554
Tprime_tAq_1000_MH150_LH_2017.year = 2017
Tprime_tAq_1000_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH175_LH_2017")
Tprime_tAq_1000_MH175_LH_2017.sigma  = 0.0008683
Tprime_tAq_1000_MH175_LH_2017.year = 2017
Tprime_tAq_1000_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH200_LH_2017")
Tprime_tAq_1000_MH200_LH_2017.sigma  = 0.000973
Tprime_tAq_1000_MH200_LH_2017.year = 2017
Tprime_tAq_1000_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH250_LH_2017")
Tprime_tAq_1000_MH250_LH_2017.sigma  = 0.00116
Tprime_tAq_1000_MH250_LH_2017.year = 2017
Tprime_tAq_1000_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH350_LH_2017")
Tprime_tAq_1000_MH350_LH_2017.sigma  = 0.001412
Tprime_tAq_1000_MH350_LH_2017.year = 2017
Tprime_tAq_1000_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH450_LH_2017")
Tprime_tAq_1000_MH450_LH_2017.sigma  = 0.001484
Tprime_tAq_1000_MH450_LH_2017.year = 2017
Tprime_tAq_1000_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH500_LH_2017")
Tprime_tAq_1000_MH500_LH_2017.sigma  = 0.001448
Tprime_tAq_1000_MH500_LH_2017.year = 2017
Tprime_tAq_1000_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH25_LH_2017")
Tprime_tAq_1100_MH25_LH_2017.sigma  = 8.434e-05
Tprime_tAq_1100_MH25_LH_2017.year = 2017
Tprime_tAq_1100_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH50_LH_2017")
Tprime_tAq_1100_MH50_LH_2017.sigma  = 0.0002003
Tprime_tAq_1100_MH50_LH_2017.year = 2017
Tprime_tAq_1100_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH75_LH_2017")
Tprime_tAq_1100_MH75_LH_2017.sigma  = 0.000308
Tprime_tAq_1100_MH75_LH_2017.year = 2017
Tprime_tAq_1100_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH100_LH_2017")
Tprime_tAq_1100_MH100_LH_2017.sigma  = 0.0004107
Tprime_tAq_1100_MH100_LH_2017.year = 2017
Tprime_tAq_1100_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH125_LH_2017")
Tprime_tAq_1100_MH125_LH_2017.sigma  = 0.0005111
Tprime_tAq_1100_MH125_LH_2017.year = 2017
Tprime_tAq_1100_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH150_LH_2017")
Tprime_tAq_1100_MH150_LH_2017.sigma  = 0.0006076
Tprime_tAq_1100_MH150_LH_2017.year = 2017
Tprime_tAq_1100_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH175_LH_2017")
Tprime_tAq_1100_MH175_LH_2017.sigma  = 0.0007005
Tprime_tAq_1100_MH175_LH_2017.year = 2017
Tprime_tAq_1100_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH200_LH_2017")
Tprime_tAq_1100_MH200_LH_2017.sigma  = 0.0007884
Tprime_tAq_1100_MH200_LH_2017.year = 2017
Tprime_tAq_1100_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH250_LH_2017")
Tprime_tAq_1100_MH250_LH_2017.sigma  = 0.0009486
Tprime_tAq_1100_MH250_LH_2017.year = 2017
Tprime_tAq_1100_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH350_LH_2017")
Tprime_tAq_1100_MH350_LH_2017.sigma  = 0.001186
Tprime_tAq_1100_MH350_LH_2017.year = 2017
Tprime_tAq_1100_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH450_LH_2017")
Tprime_tAq_1100_MH450_LH_2017.sigma  = 0.001302
Tprime_tAq_1100_MH450_LH_2017.year = 2017
Tprime_tAq_1100_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH500_LH_2017")
Tprime_tAq_1100_MH500_LH_2017.sigma  = 0.001306
Tprime_tAq_1100_MH500_LH_2017.year = 2017
Tprime_tAq_1100_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH25_LH_2017")
Tprime_tAq_1200_MH25_LH_2017.sigma  = 6.834e-05
Tprime_tAq_1200_MH25_LH_2017.year = 2017
Tprime_tAq_1200_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH50_LH_2017")
Tprime_tAq_1200_MH50_LH_2017.sigma  = 0.0001621
Tprime_tAq_1200_MH50_LH_2017.year = 2017
Tprime_tAq_1200_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH75_LH_2017")
Tprime_tAq_1200_MH75_LH_2017.sigma  = 0.0002496
Tprime_tAq_1200_MH75_LH_2017.year = 2017
Tprime_tAq_1200_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH100_LH_2017")
Tprime_tAq_1200_MH100_LH_2017.sigma  = 0.0003333
Tprime_tAq_1200_MH100_LH_2017.year = 2017
Tprime_tAq_1200_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH125_LH_2017")
Tprime_tAq_1200_MH125_LH_2017.sigma  = 0.0004151
Tprime_tAq_1200_MH125_LH_2017.year = 2017
Tprime_tAq_1200_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH150_LH_2017")
Tprime_tAq_1200_MH150_LH_2017.sigma  = 0.0004946
Tprime_tAq_1200_MH150_LH_2017.year = 2017
Tprime_tAq_1200_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH175_LH_2017")
Tprime_tAq_1200_MH175_LH_2017.sigma  = 0.0005709
Tprime_tAq_1200_MH175_LH_2017.year = 2017
Tprime_tAq_1200_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH200_LH_2017")
Tprime_tAq_1200_MH200_LH_2017.sigma  = 0.0006444
Tprime_tAq_1200_MH200_LH_2017.year = 2017
Tprime_tAq_1200_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH250_LH_2017")
Tprime_tAq_1200_MH250_LH_2017.sigma  = 0.0007796
Tprime_tAq_1200_MH250_LH_2017.year = 2017
Tprime_tAq_1200_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH350_LH_2017")
Tprime_tAq_1200_MH350_LH_2017.sigma  = 0.0009997
Tprime_tAq_1200_MH350_LH_2017.year = 2017
Tprime_tAq_1200_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH450_LH_2017")
Tprime_tAq_1200_MH450_LH_2017.sigma  = 0.001124
Tprime_tAq_1200_MH450_LH_2017.year = 2017
Tprime_tAq_1200_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH500_LH_2017")
Tprime_tAq_1200_MH500_LH_2017.sigma  = 0.001151
Tprime_tAq_1200_MH500_LH_2017.year = 2017
Tprime_tAq_1200_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH25_LH_2017")
Tprime_tAq_1300_MH25_LH_2017.sigma  = 5.51e-05
Tprime_tAq_1300_MH25_LH_2017.year = 2017
Tprime_tAq_1300_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH50_LH_2017")
Tprime_tAq_1300_MH50_LH_2017.sigma  = 0.000131
Tprime_tAq_1300_MH50_LH_2017.year = 2017
Tprime_tAq_1300_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH75_LH_2017")
Tprime_tAq_1300_MH75_LH_2017.sigma  = 0.0002016
Tprime_tAq_1300_MH75_LH_2017.year = 2017
Tprime_tAq_1300_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH100_LH_2017")
Tprime_tAq_1300_MH100_LH_2017.sigma  = 0.0002701
Tprime_tAq_1300_MH100_LH_2017.year = 2017
Tprime_tAq_1300_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH125_LH_2017")
Tprime_tAq_1300_MH125_LH_2017.sigma  = 0.0003369
Tprime_tAq_1300_MH125_LH_2017.year = 2017
Tprime_tAq_1300_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH150_LH_2017")
Tprime_tAq_1300_MH150_LH_2017.sigma  = 0.000402
Tprime_tAq_1300_MH150_LH_2017.year = 2017
Tprime_tAq_1300_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH175_LH_2017")
Tprime_tAq_1300_MH175_LH_2017.sigma  = 0.000465
Tprime_tAq_1300_MH175_LH_2017.year = 2017
Tprime_tAq_1300_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH200_LH_2017")
Tprime_tAq_1300_MH200_LH_2017.sigma  = 0.0005258
Tprime_tAq_1300_MH200_LH_2017.year = 2017
Tprime_tAq_1300_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH250_LH_2017")
Tprime_tAq_1300_MH250_LH_2017.sigma  = 0.0006392
Tprime_tAq_1300_MH250_LH_2017.year = 2017
Tprime_tAq_1300_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH350_LH_2017")
Tprime_tAq_1300_MH350_LH_2017.sigma  = 0.0008297
Tprime_tAq_1300_MH350_LH_2017.year = 2017
Tprime_tAq_1300_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH450_LH_2017")
Tprime_tAq_1300_MH450_LH_2017.sigma  = 0.000958
Tprime_tAq_1300_MH450_LH_2017.year = 2017
Tprime_tAq_1300_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH500_LH_2017")
Tprime_tAq_1300_MH500_LH_2017.sigma  = 0.0009965
Tprime_tAq_1300_MH500_LH_2017.year = 2017
Tprime_tAq_1300_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH25_LH_2017")
Tprime_tAq_1400_MH25_LH_2017.sigma  = 4.468e-05
Tprime_tAq_1400_MH25_LH_2017.year = 2017
Tprime_tAq_1400_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH50_LH_2017")
Tprime_tAq_1400_MH50_LH_2017.sigma  = 0.0001062
Tprime_tAq_1400_MH50_LH_2017.year = 2017
Tprime_tAq_1400_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH75_LH_2017")
Tprime_tAq_1400_MH75_LH_2017.sigma  = 0.0001637
Tprime_tAq_1400_MH75_LH_2017.year = 2017
Tprime_tAq_1400_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH100_LH_2017")
Tprime_tAq_1400_MH100_LH_2017.sigma  = 0.0002192
Tprime_tAq_1400_MH100_LH_2017.year = 2017
Tprime_tAq_1400_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH125_LH_2017")
Tprime_tAq_1400_MH125_LH_2017.sigma  = 0.0002736
Tprime_tAq_1400_MH125_LH_2017.year = 2017
Tprime_tAq_1400_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH150_LH_2017")
Tprime_tAq_1400_MH150_LH_2017.sigma  = 0.0003269
Tprime_tAq_1400_MH150_LH_2017.year = 2017
Tprime_tAq_1400_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH175_LH_2017")
Tprime_tAq_1400_MH175_LH_2017.sigma  = 0.0003787
Tprime_tAq_1400_MH175_LH_2017.year = 2017
Tprime_tAq_1400_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH200_LH_2017")
Tprime_tAq_1400_MH200_LH_2017.sigma  = 0.0004289
Tprime_tAq_1400_MH200_LH_2017.year = 2017
Tprime_tAq_1400_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH250_LH_2017")
Tprime_tAq_1400_MH250_LH_2017.sigma  = 0.0005231
Tprime_tAq_1400_MH250_LH_2017.year = 2017
Tprime_tAq_1400_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH350_LH_2017")
Tprime_tAq_1400_MH350_LH_2017.sigma  = 0.0006847
Tprime_tAq_1400_MH350_LH_2017.year = 2017
Tprime_tAq_1400_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH450_LH_2017")
Tprime_tAq_1400_MH450_LH_2017.sigma  = 0.0008049
Tprime_tAq_1400_MH450_LH_2017.year = 2017
Tprime_tAq_1400_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH500_LH_2017")
Tprime_tAq_1400_MH500_LH_2017.sigma  = 0.0008453
Tprime_tAq_1400_MH500_LH_2017.year = 2017
Tprime_tAq_1400_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH25_LH_2017")
Tprime_tAq_1500_MH25_LH_2017.sigma  = 3.581e-05
Tprime_tAq_1500_MH25_LH_2017.year = 2017
Tprime_tAq_1500_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH50_LH_2017")
Tprime_tAq_1500_MH50_LH_2017.sigma  = 8.514e-05
Tprime_tAq_1500_MH50_LH_2017.year = 2017
Tprime_tAq_1500_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH75_LH_2017")
Tprime_tAq_1500_MH75_LH_2017.sigma  = 0.0001313
Tprime_tAq_1500_MH75_LH_2017.year = 2017
Tprime_tAq_1500_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH100_LH_2017")
Tprime_tAq_1500_MH100_LH_2017.sigma  = 0.0001762
Tprime_tAq_1500_MH100_LH_2017.year = 2017
Tprime_tAq_1500_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH125_LH_2017")
Tprime_tAq_1500_MH125_LH_2017.sigma  = 0.0002202
Tprime_tAq_1500_MH125_LH_2017.year = 2017
Tprime_tAq_1500_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH150_LH_2017")
Tprime_tAq_1500_MH150_LH_2017.sigma  = 0.0002633
Tprime_tAq_1500_MH150_LH_2017.year = 2017
Tprime_tAq_1500_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH175_LH_2017")
Tprime_tAq_1500_MH175_LH_2017.sigma  = 0.0003051
Tprime_tAq_1500_MH175_LH_2017.year = 2017
Tprime_tAq_1500_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH200_LH_2017")
Tprime_tAq_1500_MH200_LH_2017.sigma  = 0.0003467
Tprime_tAq_1500_MH200_LH_2017.year = 2017
Tprime_tAq_1500_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH250_LH_2017")
Tprime_tAq_1500_MH250_LH_2017.sigma  = 0.0004246
Tprime_tAq_1500_MH250_LH_2017.year = 2017
Tprime_tAq_1500_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH350_LH_2017")
Tprime_tAq_1500_MH350_LH_2017.sigma  = 0.0005626
Tprime_tAq_1500_MH350_LH_2017.year = 2017
Tprime_tAq_1500_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH450_LH_2017")
Tprime_tAq_1500_MH450_LH_2017.sigma  = 0.0006697
Tprime_tAq_1500_MH450_LH_2017.year = 2017
Tprime_tAq_1500_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH500_LH_2017")
Tprime_tAq_1500_MH500_LH_2017.sigma  = 0.0007093
Tprime_tAq_1500_MH500_LH_2017.year = 2017
Tprime_tAq_1500_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH25_LH_2017")
Tprime_tAq_1600_MH25_LH_2017.sigma  = 2.945e-05
Tprime_tAq_1600_MH25_LH_2017.year = 2017
Tprime_tAq_1600_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH50_LH_2017")
Tprime_tAq_1600_MH50_LH_2017.sigma  = 7.004e-05
Tprime_tAq_1600_MH50_LH_2017.year = 2017
Tprime_tAq_1600_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH75_LH_2017")
Tprime_tAq_1600_MH75_LH_2017.sigma  = 0.0001079
Tprime_tAq_1600_MH75_LH_2017.year = 2017
Tprime_tAq_1600_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH100_LH_2017")
Tprime_tAq_1600_MH100_LH_2017.sigma  = 0.0001449
Tprime_tAq_1600_MH100_LH_2017.year = 2017
Tprime_tAq_1600_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH125_LH_2017")
Tprime_tAq_1600_MH125_LH_2017.sigma  = 0.0001812
Tprime_tAq_1600_MH125_LH_2017.year = 2017
Tprime_tAq_1600_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH150_LH_2017")
Tprime_tAq_1600_MH150_LH_2017.sigma  = 0.0002168
Tprime_tAq_1600_MH150_LH_2017.year = 2017
Tprime_tAq_1600_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH175_LH_2017")
Tprime_tAq_1600_MH175_LH_2017.sigma  = 0.0002517
Tprime_tAq_1600_MH175_LH_2017.year = 2017
Tprime_tAq_1600_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH200_LH_2017")
Tprime_tAq_1600_MH200_LH_2017.sigma  = 0.0002858
Tprime_tAq_1600_MH200_LH_2017.year = 2017
Tprime_tAq_1600_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH250_LH_2017")
Tprime_tAq_1600_MH250_LH_2017.sigma  = 0.0003522
Tprime_tAq_1600_MH250_LH_2017.year = 2017
Tprime_tAq_1600_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH350_LH_2017")
Tprime_tAq_1600_MH350_LH_2017.sigma  = 0.0004698
Tprime_tAq_1600_MH350_LH_2017.year = 2017
Tprime_tAq_1600_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH450_LH_2017")
Tprime_tAq_1600_MH450_LH_2017.sigma  = 0.0005646
Tprime_tAq_1600_MH450_LH_2017.year = 2017
Tprime_tAq_1600_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH500_LH_2017")
Tprime_tAq_1600_MH500_LH_2017.sigma  = 0.0006016
Tprime_tAq_1600_MH500_LH_2017.year = 2017
Tprime_tAq_1600_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH25_LH_2017")
Tprime_tAq_1700_MH25_LH_2017.sigma  = 2.409e-05
Tprime_tAq_1700_MH25_LH_2017.year = 2017
Tprime_tAq_1700_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH50_LH_2017")
Tprime_tAq_1700_MH50_LH_2017.sigma  = 5.729e-05
Tprime_tAq_1700_MH50_LH_2017.year = 2017
Tprime_tAq_1700_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH75_LH_2017")
Tprime_tAq_1700_MH75_LH_2017.sigma  = 8.839e-05
Tprime_tAq_1700_MH75_LH_2017.year = 2017
Tprime_tAq_1700_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH100_LH_2017")
Tprime_tAq_1700_MH100_LH_2017.sigma  = 0.0001189
Tprime_tAq_1700_MH100_LH_2017.year = 2017
Tprime_tAq_1700_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH125_LH_2017")
Tprime_tAq_1700_MH125_LH_2017.sigma  = 0.0001488
Tprime_tAq_1700_MH125_LH_2017.year = 2017
Tprime_tAq_1700_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH150_LH_2017")
Tprime_tAq_1700_MH150_LH_2017.sigma  = 0.0001781
Tprime_tAq_1700_MH150_LH_2017.year = 2017
Tprime_tAq_1700_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH175_LH_2017")
Tprime_tAq_1700_MH175_LH_2017.sigma  = 0.0002068
Tprime_tAq_1700_MH175_LH_2017.year = 2017
Tprime_tAq_1700_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH200_LH_2017")
Tprime_tAq_1700_MH200_LH_2017.sigma  = 0.0002351
Tprime_tAq_1700_MH200_LH_2017.year = 2017
Tprime_tAq_1700_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH250_LH_2017")
Tprime_tAq_1700_MH250_LH_2017.sigma  = 0.0002892
Tprime_tAq_1700_MH250_LH_2017.year = 2017
Tprime_tAq_1700_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH350_LH_2017")
Tprime_tAq_1700_MH350_LH_2017.sigma  = 0.0003879
Tprime_tAq_1700_MH350_LH_2017.year = 2017
Tprime_tAq_1700_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH450_LH_2017")
Tprime_tAq_1700_MH450_LH_2017.sigma  = 0.0004715
Tprime_tAq_1700_MH450_LH_2017.year = 2017
Tprime_tAq_1700_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH500_LH_2017")
Tprime_tAq_1700_MH500_LH_2017.sigma  = 0.000506
Tprime_tAq_1700_MH500_LH_2017.year = 2017
Tprime_tAq_1700_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH25_LH_2017")
Tprime_tAq_1800_MH25_LH_2017.sigma  = 1.955e-05
Tprime_tAq_1800_MH25_LH_2017.year = 2017
Tprime_tAq_1800_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH50_LH_2017")
Tprime_tAq_1800_MH50_LH_2017.sigma  = 4.652e-05
Tprime_tAq_1800_MH50_LH_2017.year = 2017
Tprime_tAq_1800_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH75_LH_2017")
Tprime_tAq_1800_MH75_LH_2017.sigma  = 7.183e-05
Tprime_tAq_1800_MH75_LH_2017.year = 2017
Tprime_tAq_1800_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH100_LH_2017")
Tprime_tAq_1800_MH100_LH_2017.sigma  = 9.639e-05
Tprime_tAq_1800_MH100_LH_2017.year = 2017
Tprime_tAq_1800_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH125_LH_2017")
Tprime_tAq_1800_MH125_LH_2017.sigma  = 0.0001207
Tprime_tAq_1800_MH125_LH_2017.year = 2017
Tprime_tAq_1800_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH150_LH_2017")
Tprime_tAq_1800_MH150_LH_2017.sigma  = 0.0001446
Tprime_tAq_1800_MH150_LH_2017.year = 2017
Tprime_tAq_1800_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH175_LH_2017")
Tprime_tAq_1800_MH175_LH_2017.sigma  = 0.000168
Tprime_tAq_1800_MH175_LH_2017.year = 2017
Tprime_tAq_1800_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH200_LH_2017")
Tprime_tAq_1800_MH200_LH_2017.sigma  = 0.000191
Tprime_tAq_1800_MH200_LH_2017.year = 2017
Tprime_tAq_1800_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH250_LH_2017")
Tprime_tAq_1800_MH250_LH_2017.sigma  = 0.0002358
Tprime_tAq_1800_MH250_LH_2017.year = 2017
Tprime_tAq_1800_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH350_LH_2017")
Tprime_tAq_1800_MH350_LH_2017.sigma  = 0.0003182
Tprime_tAq_1800_MH350_LH_2017.year = 2017
Tprime_tAq_1800_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH450_LH_2017")
Tprime_tAq_1800_MH450_LH_2017.sigma  = 0.0003873
Tprime_tAq_1800_MH450_LH_2017.year = 2017
Tprime_tAq_1800_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH500_LH_2017")
Tprime_tAq_1800_MH500_LH_2017.sigma  = 0.0004171
Tprime_tAq_1800_MH500_LH_2017.year = 2017
Tprime_tAq_1800_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH25_LH_2017")
Tprime_tAq_1900_MH25_LH_2017.sigma  = 1.601e-05
Tprime_tAq_1900_MH25_LH_2017.year = 2017
Tprime_tAq_1900_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH50_LH_2017")
Tprime_tAq_1900_MH50_LH_2017.sigma  = 3.811e-05
Tprime_tAq_1900_MH50_LH_2017.year = 2017
Tprime_tAq_1900_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH75_LH_2017")
Tprime_tAq_1900_MH75_LH_2017.sigma  = 5.881e-05
Tprime_tAq_1900_MH75_LH_2017.year = 2017
Tprime_tAq_1900_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH100_LH_2017")
Tprime_tAq_1900_MH100_LH_2017.sigma  = 7.904e-05
Tprime_tAq_1900_MH100_LH_2017.year = 2017
Tprime_tAq_1900_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH125_LH_2017")
Tprime_tAq_1900_MH125_LH_2017.sigma  = 9.897e-05
Tprime_tAq_1900_MH125_LH_2017.year = 2017
Tprime_tAq_1900_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH150_LH_2017")
Tprime_tAq_1900_MH150_LH_2017.sigma  = 0.0001185
Tprime_tAq_1900_MH150_LH_2017.year = 2017
Tprime_tAq_1900_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH175_LH_2017")
Tprime_tAq_1900_MH175_LH_2017.sigma  = 0.0001379
Tprime_tAq_1900_MH175_LH_2017.year = 2017
Tprime_tAq_1900_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH200_LH_2017")
Tprime_tAq_1900_MH200_LH_2017.sigma  = 0.000157
Tprime_tAq_1900_MH200_LH_2017.year = 2017
Tprime_tAq_1900_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH250_LH_2017")
Tprime_tAq_1900_MH250_LH_2017.sigma  = 0.000194
Tprime_tAq_1900_MH250_LH_2017.year = 2017
Tprime_tAq_1900_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH350_LH_2017")
Tprime_tAq_1900_MH350_LH_2017.sigma  = 0.0002628
Tprime_tAq_1900_MH350_LH_2017.year = 2017
Tprime_tAq_1900_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH450_LH_2017")
Tprime_tAq_1900_MH450_LH_2017.sigma  = 0.0003233
Tprime_tAq_1900_MH450_LH_2017.year = 2017
Tprime_tAq_1900_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH500_LH_2017")
Tprime_tAq_1900_MH500_LH_2017.sigma  = 0.0003491
Tprime_tAq_1900_MH500_LH_2017.year = 2017
Tprime_tAq_1900_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH25_LH_2017")
Tprime_tAq_2000_MH25_LH_2017.sigma  = 1.331e-05
Tprime_tAq_2000_MH25_LH_2017.year = 2017
Tprime_tAq_2000_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH50_LH_2017")
Tprime_tAq_2000_MH50_LH_2017.sigma  = 3.168e-05
Tprime_tAq_2000_MH50_LH_2017.year = 2017
Tprime_tAq_2000_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH75_LH_2017")
Tprime_tAq_2000_MH75_LH_2017.sigma  = 4.889e-05
Tprime_tAq_2000_MH75_LH_2017.year = 2017
Tprime_tAq_2000_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH100_LH_2017")
Tprime_tAq_2000_MH100_LH_2017.sigma  = 6.573e-05
Tprime_tAq_2000_MH100_LH_2017.year = 2017
Tprime_tAq_2000_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH125_LH_2017")
Tprime_tAq_2000_MH125_LH_2017.sigma  = 8.233e-05
Tprime_tAq_2000_MH125_LH_2017.year = 2017
Tprime_tAq_2000_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH150_LH_2017")
Tprime_tAq_2000_MH150_LH_2017.sigma  = 9.871e-05
Tprime_tAq_2000_MH150_LH_2017.year = 2017
Tprime_tAq_2000_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH175_LH_2017")
Tprime_tAq_2000_MH175_LH_2017.sigma  = 0.0001149
Tprime_tAq_2000_MH175_LH_2017.year = 2017
Tprime_tAq_2000_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH200_LH_2017")
Tprime_tAq_2000_MH200_LH_2017.sigma  = 0.0001308
Tprime_tAq_2000_MH200_LH_2017.year = 2017
Tprime_tAq_2000_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH250_LH_2017")
Tprime_tAq_2000_MH250_LH_2017.sigma  = 0.0001618
Tprime_tAq_2000_MH250_LH_2017.year = 2017
Tprime_tAq_2000_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH350_LH_2017")
Tprime_tAq_2000_MH350_LH_2017.sigma  = 0.0002198
Tprime_tAq_2000_MH350_LH_2017.year = 2017
Tprime_tAq_2000_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH450_LH_2017")
Tprime_tAq_2000_MH450_LH_2017.sigma  = 0.0002711
Tprime_tAq_2000_MH450_LH_2017.year = 2017
Tprime_tAq_2000_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH500_LH_2017")
Tprime_tAq_2000_MH500_LH_2017.sigma  = 0.0002938
Tprime_tAq_2000_MH500_LH_2017.year = 2017
Tprime_tAq_2000_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH25_LH_2017")
Tprime_tAq_2100_MH25_LH_2017.sigma  = 1.078e-05
Tprime_tAq_2100_MH25_LH_2017.year = 2017
Tprime_tAq_2100_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH50_LH_2017")
Tprime_tAq_2100_MH50_LH_2017.sigma  = 2.565e-05
Tprime_tAq_2100_MH50_LH_2017.year = 2017
Tprime_tAq_2100_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH75_LH_2017")
Tprime_tAq_2100_MH75_LH_2017.sigma  = 3.96e-05
Tprime_tAq_2100_MH75_LH_2017.year = 2017
Tprime_tAq_2100_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH100_LH_2017")
Tprime_tAq_2100_MH100_LH_2017.sigma  = 5.324e-05
Tprime_tAq_2100_MH100_LH_2017.year = 2017
Tprime_tAq_2100_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH125_LH_2017")
Tprime_tAq_2100_MH125_LH_2017.sigma  = 6.671e-05
Tprime_tAq_2100_MH125_LH_2017.year = 2017
Tprime_tAq_2100_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH150_LH_2017")
Tprime_tAq_2100_MH150_LH_2017.sigma  = 8.002e-05
Tprime_tAq_2100_MH150_LH_2017.year = 2017
Tprime_tAq_2100_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH175_LH_2017")
Tprime_tAq_2100_MH175_LH_2017.sigma  = 9.315e-05
Tprime_tAq_2100_MH175_LH_2017.year = 2017
Tprime_tAq_2100_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH200_LH_2017")
Tprime_tAq_2100_MH200_LH_2017.sigma  = 0.0001061
Tprime_tAq_2100_MH200_LH_2017.year = 2017
Tprime_tAq_2100_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH250_LH_2017")
Tprime_tAq_2100_MH250_LH_2017.sigma  = 0.0001314
Tprime_tAq_2100_MH250_LH_2017.year = 2017
Tprime_tAq_2100_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH350_LH_2017")
Tprime_tAq_2100_MH350_LH_2017.sigma  = 0.0001791
Tprime_tAq_2100_MH350_LH_2017.year = 2017
Tprime_tAq_2100_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH450_LH_2017")
Tprime_tAq_2100_MH450_LH_2017.sigma  = 0.0002216
Tprime_tAq_2100_MH450_LH_2017.year = 2017
Tprime_tAq_2100_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH500_LH_2017")
Tprime_tAq_2100_MH500_LH_2017.sigma  = 0.0002407
Tprime_tAq_2100_MH500_LH_2017.year = 2017
Tprime_tAq_2100_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH25_LH_2017")
Tprime_tAq_2200_MH25_LH_2017.sigma  = 8.958e-06
Tprime_tAq_2200_MH25_LH_2017.year = 2017
Tprime_tAq_2200_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH50_LH_2017")
Tprime_tAq_2200_MH50_LH_2017.sigma  = 2.132e-05
Tprime_tAq_2200_MH50_LH_2017.year = 2017
Tprime_tAq_2200_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH75_LH_2017")
Tprime_tAq_2200_MH75_LH_2017.sigma  = 3.292e-05
Tprime_tAq_2200_MH75_LH_2017.year = 2017
Tprime_tAq_2200_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH100_LH_2017")
Tprime_tAq_2200_MH100_LH_2017.sigma  = 4.427e-05
Tprime_tAq_2200_MH100_LH_2017.year = 2017
Tprime_tAq_2200_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH125_LH_2017")
Tprime_tAq_2200_MH125_LH_2017.sigma  = 5.548e-05
Tprime_tAq_2200_MH125_LH_2017.year = 2017
Tprime_tAq_2200_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH150_LH_2017")
Tprime_tAq_2200_MH150_LH_2017.sigma  = 6.656e-05
Tprime_tAq_2200_MH150_LH_2017.year = 2017
Tprime_tAq_2200_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH175_LH_2017")
Tprime_tAq_2200_MH175_LH_2017.sigma  = 7.751e-05
Tprime_tAq_2200_MH175_LH_2017.year = 2017
Tprime_tAq_2200_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH200_LH_2017")
Tprime_tAq_2200_MH200_LH_2017.sigma  = 8.831e-05
Tprime_tAq_2200_MH200_LH_2017.year = 2017
Tprime_tAq_2200_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH250_LH_2017")
Tprime_tAq_2200_MH250_LH_2017.sigma  = 0.0001095
Tprime_tAq_2200_MH250_LH_2017.year = 2017
Tprime_tAq_2200_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH350_LH_2017")
Tprime_tAq_2200_MH350_LH_2017.sigma  = 0.0001496
Tprime_tAq_2200_MH350_LH_2017.year = 2017
Tprime_tAq_2200_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH450_LH_2017")
Tprime_tAq_2200_MH450_LH_2017.sigma  = 0.0001858
Tprime_tAq_2200_MH450_LH_2017.year = 2017
Tprime_tAq_2200_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH500_LH_2017")
Tprime_tAq_2200_MH500_LH_2017.sigma  = 0.0002023
Tprime_tAq_2200_MH500_LH_2017.year = 2017
Tprime_tAq_2200_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH25_LH_2017")
Tprime_tAq_2300_MH25_LH_2017.sigma  = 7.415e-06
Tprime_tAq_2300_MH25_LH_2017.year = 2017
Tprime_tAq_2300_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH50_LH_2017")
Tprime_tAq_2300_MH50_LH_2017.sigma  = 1.765e-05
Tprime_tAq_2300_MH50_LH_2017.year = 2017
Tprime_tAq_2300_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH75_LH_2017")
Tprime_tAq_2300_MH75_LH_2017.sigma  = 2.726e-05
Tprime_tAq_2300_MH75_LH_2017.year = 2017
Tprime_tAq_2300_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH100_LH_2017")
Tprime_tAq_2300_MH100_LH_2017.sigma  = 3.666e-05
Tprime_tAq_2300_MH100_LH_2017.year = 2017
Tprime_tAq_2300_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH125_LH_2017")
Tprime_tAq_2300_MH125_LH_2017.sigma  = 4.595e-05
Tprime_tAq_2300_MH125_LH_2017.year = 2017
Tprime_tAq_2300_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH150_LH_2017")
Tprime_tAq_2300_MH150_LH_2017.sigma  = 5.514e-05
Tprime_tAq_2300_MH150_LH_2017.year = 2017
Tprime_tAq_2300_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH175_LH_2017")
Tprime_tAq_2300_MH175_LH_2017.sigma  = 6.424e-05
Tprime_tAq_2300_MH175_LH_2017.year = 2017
Tprime_tAq_2300_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH200_LH_2017")
Tprime_tAq_2300_MH200_LH_2017.sigma  = 7.323e-05
Tprime_tAq_2300_MH200_LH_2017.year = 2017
Tprime_tAq_2300_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH250_LH_2017")
Tprime_tAq_2300_MH250_LH_2017.sigma  = 9.084e-05
Tprime_tAq_2300_MH250_LH_2017.year = 2017
Tprime_tAq_2300_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH350_LH_2017")
Tprime_tAq_2300_MH350_LH_2017.sigma  = 0.0001244
Tprime_tAq_2300_MH350_LH_2017.year = 2017
Tprime_tAq_2300_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH450_LH_2017")
Tprime_tAq_2300_MH450_LH_2017.sigma  = 0.0001551
Tprime_tAq_2300_MH450_LH_2017.year = 2017
Tprime_tAq_2300_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH500_LH_2017")
Tprime_tAq_2300_MH500_LH_2017.sigma  = 0.0001691
Tprime_tAq_2300_MH500_LH_2017.year = 2017
Tprime_tAq_2300_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH25_LH_2017")
Tprime_tAq_2400_MH25_LH_2017.sigma  = 6.132e-06
Tprime_tAq_2400_MH25_LH_2017.year = 2017
Tprime_tAq_2400_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH50_LH_2017")
Tprime_tAq_2400_MH50_LH_2017.sigma  = 1.461e-05
Tprime_tAq_2400_MH50_LH_2017.year = 2017
Tprime_tAq_2400_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH75_LH_2017")
Tprime_tAq_2400_MH75_LH_2017.sigma  = 2.256e-05
Tprime_tAq_2400_MH75_LH_2017.year = 2017
Tprime_tAq_2400_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH100_LH_2017")
Tprime_tAq_2400_MH100_LH_2017.sigma  = 3.035e-05
Tprime_tAq_2400_MH100_LH_2017.year = 2017
Tprime_tAq_2400_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH125_LH_2017")
Tprime_tAq_2400_MH125_LH_2017.sigma  = 3.804e-05
Tprime_tAq_2400_MH125_LH_2017.year = 2017
Tprime_tAq_2400_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH150_LH_2017")
Tprime_tAq_2400_MH150_LH_2017.sigma  = 4.566e-05
Tprime_tAq_2400_MH150_LH_2017.year = 2017
Tprime_tAq_2400_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH175_LH_2017")
Tprime_tAq_2400_MH175_LH_2017.sigma  = 5.321e-05
Tprime_tAq_2400_MH175_LH_2017.year = 2017
Tprime_tAq_2400_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH200_LH_2017")
Tprime_tAq_2400_MH200_LH_2017.sigma  = 6.069e-05
Tprime_tAq_2400_MH200_LH_2017.year = 2017
Tprime_tAq_2400_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH250_LH_2017")
Tprime_tAq_2400_MH250_LH_2017.sigma  = 7.535e-05
Tprime_tAq_2400_MH250_LH_2017.year = 2017
Tprime_tAq_2400_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH350_LH_2017")
Tprime_tAq_2400_MH350_LH_2017.sigma  = 0.0001034
Tprime_tAq_2400_MH350_LH_2017.year = 2017
Tprime_tAq_2400_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH450_LH_2017")
Tprime_tAq_2400_MH450_LH_2017.sigma  = 0.0001291
Tprime_tAq_2400_MH450_LH_2017.year = 2017
Tprime_tAq_2400_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH500_LH_2017")
Tprime_tAq_2400_MH500_LH_2017.sigma  = 0.0001411
Tprime_tAq_2400_MH500_LH_2017.year = 2017
Tprime_tAq_2400_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH25_LH_2017")
Tprime_tAq_2500_MH25_LH_2017.sigma  = 5.095e-06
Tprime_tAq_2500_MH25_LH_2017.year = 2017
Tprime_tAq_2500_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH50_LH_2017")
Tprime_tAq_2500_MH50_LH_2017.sigma  = 1.213e-05
Tprime_tAq_2500_MH50_LH_2017.year = 2017
Tprime_tAq_2500_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH75_LH_2017")
Tprime_tAq_2500_MH75_LH_2017.sigma  = 1.873e-05
Tprime_tAq_2500_MH75_LH_2017.year = 2017
Tprime_tAq_2500_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH100_LH_2017")
Tprime_tAq_2500_MH100_LH_2017.sigma  = 2.52e-05
Tprime_tAq_2500_MH100_LH_2017.year = 2017
Tprime_tAq_2500_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH125_LH_2017")
Tprime_tAq_2500_MH125_LH_2017.sigma  = 3.16e-05
Tprime_tAq_2500_MH125_LH_2017.year = 2017
Tprime_tAq_2500_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH150_LH_2017")
Tprime_tAq_2500_MH150_LH_2017.sigma  = 3.787e-05
Tprime_tAq_2500_MH150_LH_2017.year = 2017
Tprime_tAq_2500_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH175_LH_2017")
Tprime_tAq_2500_MH175_LH_2017.sigma  = 4.414e-05
Tprime_tAq_2500_MH175_LH_2017.year = 2017
Tprime_tAq_2500_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH200_LH_2017")
Tprime_tAq_2500_MH200_LH_2017.sigma  = 5.034e-05
Tprime_tAq_2500_MH200_LH_2017.year = 2017
Tprime_tAq_2500_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH250_LH_2017")
Tprime_tAq_2500_MH250_LH_2017.sigma  = 6.248e-05
Tprime_tAq_2500_MH250_LH_2017.year = 2017
Tprime_tAq_2500_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH350_LH_2017")
Tprime_tAq_2500_MH350_LH_2017.sigma  = 8.587e-05
Tprime_tAq_2500_MH350_LH_2017.year = 2017
Tprime_tAq_2500_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH450_LH_2017")
Tprime_tAq_2500_MH450_LH_2017.sigma  = 0.000108
Tprime_tAq_2500_MH450_LH_2017.year = 2017
Tprime_tAq_2500_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH500_LH_2017")
Tprime_tAq_2500_MH500_LH_2017.sigma  = 0.000118
Tprime_tAq_2500_MH500_LH_2017.year = 2017
Tprime_tAq_2500_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH25_LH_2017")
Tprime_tAq_2600_MH25_LH_2017.sigma  = 4.123e-06
Tprime_tAq_2600_MH25_LH_2017.year = 2017
Tprime_tAq_2600_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH50_LH_2017")
Tprime_tAq_2600_MH50_LH_2017.sigma  = 9.817e-06
Tprime_tAq_2600_MH50_LH_2017.year = 2017
Tprime_tAq_2600_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH75_LH_2017")
Tprime_tAq_2600_MH75_LH_2017.sigma  = 1.517e-05
Tprime_tAq_2600_MH75_LH_2017.year = 2017
Tprime_tAq_2600_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH100_LH_2017")
Tprime_tAq_2600_MH100_LH_2017.sigma  = 2.041e-05
Tprime_tAq_2600_MH100_LH_2017.year = 2017
Tprime_tAq_2600_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH125_LH_2017")
Tprime_tAq_2600_MH125_LH_2017.sigma  = 2.559e-05
Tprime_tAq_2600_MH125_LH_2017.year = 2017
Tprime_tAq_2600_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH150_LH_2017")
Tprime_tAq_2600_MH150_LH_2017.sigma  = 3.073e-05
Tprime_tAq_2600_MH150_LH_2017.year = 2017
Tprime_tAq_2600_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH175_LH_2017")
Tprime_tAq_2600_MH175_LH_2017.sigma  = 3.582e-05
Tprime_tAq_2600_MH175_LH_2017.year = 2017
Tprime_tAq_2600_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH200_LH_2017")
Tprime_tAq_2600_MH200_LH_2017.sigma  = 4.086e-05
Tprime_tAq_2600_MH200_LH_2017.year = 2017
Tprime_tAq_2600_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH250_LH_2017")
Tprime_tAq_2600_MH250_LH_2017.sigma  = 5.08e-05
Tprime_tAq_2600_MH250_LH_2017.year = 2017
Tprime_tAq_2600_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH350_LH_2017")
Tprime_tAq_2600_MH350_LH_2017.sigma  = 6.99e-05
Tprime_tAq_2600_MH350_LH_2017.year = 2017
Tprime_tAq_2600_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH450_LH_2017")
Tprime_tAq_2600_MH450_LH_2017.sigma  = 8.775e-05
Tprime_tAq_2600_MH450_LH_2017.year = 2017
Tprime_tAq_2600_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH500_LH_2017")
Tprime_tAq_2600_MH500_LH_2017.sigma  = 9.599e-05
Tprime_tAq_2600_MH500_LH_2017.year = 2017
Tprime_tAq_2600_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH25_LH_2017")
Tprime_tAq_2700_MH25_LH_2017.sigma  = 3.433e-06
Tprime_tAq_2700_MH25_LH_2017.year = 2017
Tprime_tAq_2700_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH50_LH_2017")
Tprime_tAq_2700_MH50_LH_2017.sigma  = 8.187e-06
Tprime_tAq_2700_MH50_LH_2017.year = 2017
Tprime_tAq_2700_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH75_LH_2017")
Tprime_tAq_2700_MH75_LH_2017.sigma  = 1.265e-05
Tprime_tAq_2700_MH75_LH_2017.year = 2017
Tprime_tAq_2700_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH100_LH_2017")
Tprime_tAq_2700_MH100_LH_2017.sigma  = 1.702e-05
Tprime_tAq_2700_MH100_LH_2017.year = 2017
Tprime_tAq_2700_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH125_LH_2017")
Tprime_tAq_2700_MH125_LH_2017.sigma  = 2.133e-05
Tprime_tAq_2700_MH125_LH_2017.year = 2017
Tprime_tAq_2700_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH150_LH_2017")
Tprime_tAq_2700_MH150_LH_2017.sigma  = 2.558e-05
Tprime_tAq_2700_MH150_LH_2017.year = 2017
Tprime_tAq_2700_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH175_LH_2017")
Tprime_tAq_2700_MH175_LH_2017.sigma  = 2.982e-05
Tprime_tAq_2700_MH175_LH_2017.year = 2017
Tprime_tAq_2700_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH200_LH_2017")
Tprime_tAq_2700_MH200_LH_2017.sigma  = 3.403e-05
Tprime_tAq_2700_MH200_LH_2017.year = 2017
Tprime_tAq_2700_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH250_LH_2017")
Tprime_tAq_2700_MH250_LH_2017.sigma  = 4.232e-05
Tprime_tAq_2700_MH250_LH_2017.year = 2017
Tprime_tAq_2700_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH350_LH_2017")
Tprime_tAq_2700_MH350_LH_2017.sigma  = 5.833e-05
Tprime_tAq_2700_MH350_LH_2017.year = 2017
Tprime_tAq_2700_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH450_LH_2017")
Tprime_tAq_2700_MH450_LH_2017.sigma  = 7.334e-05
Tprime_tAq_2700_MH450_LH_2017.year = 2017
Tprime_tAq_2700_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH500_LH_2017")
Tprime_tAq_2700_MH500_LH_2017.sigma  = 8.036e-05
Tprime_tAq_2700_MH500_LH_2017.year = 2017
Tprime_tAq_2700_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH25_LH_2017")
Tprime_tAq_2800_MH25_LH_2017.sigma  = 2.848e-06
Tprime_tAq_2800_MH25_LH_2017.year = 2017
Tprime_tAq_2800_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH50_LH_2017")
Tprime_tAq_2800_MH50_LH_2017.sigma  = 6.834e-06
Tprime_tAq_2800_MH50_LH_2017.year = 2017
Tprime_tAq_2800_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH75_LH_2017")
Tprime_tAq_2800_MH75_LH_2017.sigma  = 1.057e-05
Tprime_tAq_2800_MH75_LH_2017.year = 2017
Tprime_tAq_2800_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH100_LH_2017")
Tprime_tAq_2800_MH100_LH_2017.sigma  = 1.411e-05
Tprime_tAq_2800_MH100_LH_2017.year = 2017
Tprime_tAq_2800_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH125_LH_2017")
Tprime_tAq_2800_MH125_LH_2017.sigma  = 1.769e-05
Tprime_tAq_2800_MH125_LH_2017.year = 2017
Tprime_tAq_2800_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH150_LH_2017")
Tprime_tAq_2800_MH150_LH_2017.sigma  = 2.125e-05
Tprime_tAq_2800_MH150_LH_2017.year = 2017
Tprime_tAq_2800_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH175_LH_2017")
Tprime_tAq_2800_MH175_LH_2017.sigma  = 2.477e-05
Tprime_tAq_2800_MH175_LH_2017.year = 2017
Tprime_tAq_2800_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH200_LH_2017")
Tprime_tAq_2800_MH200_LH_2017.sigma  = 2.827e-05
Tprime_tAq_2800_MH200_LH_2017.year = 2017
Tprime_tAq_2800_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH250_LH_2017")
Tprime_tAq_2800_MH250_LH_2017.sigma  = 3.518e-05
Tprime_tAq_2800_MH250_LH_2017.year = 2017
Tprime_tAq_2800_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH350_LH_2017")
Tprime_tAq_2800_MH350_LH_2017.sigma  = 4.855e-05
Tprime_tAq_2800_MH350_LH_2017.year = 2017
Tprime_tAq_2800_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH450_LH_2017")
Tprime_tAq_2800_MH450_LH_2017.sigma  = 6.108e-05
Tprime_tAq_2800_MH450_LH_2017.year = 2017
Tprime_tAq_2800_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH500_LH_2017")
Tprime_tAq_2800_MH500_LH_2017.sigma  = 6.7e-05
Tprime_tAq_2800_MH500_LH_2017.year = 2017
Tprime_tAq_2800_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH25_LH_2017")
Tprime_tAq_2900_MH25_LH_2017.sigma  = 2.356e-06
Tprime_tAq_2900_MH25_LH_2017.year = 2017
Tprime_tAq_2900_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH50_LH_2017")
Tprime_tAq_2900_MH50_LH_2017.sigma  = 5.609e-06
Tprime_tAq_2900_MH50_LH_2017.year = 2017
Tprime_tAq_2900_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH75_LH_2017")
Tprime_tAq_2900_MH75_LH_2017.sigma  = 8.666e-06
Tprime_tAq_2900_MH75_LH_2017.year = 2017
Tprime_tAq_2900_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH100_LH_2017")
Tprime_tAq_2900_MH100_LH_2017.sigma  = 1.166e-05
Tprime_tAq_2900_MH100_LH_2017.year = 2017
Tprime_tAq_2900_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH125_LH_2017")
Tprime_tAq_2900_MH125_LH_2017.sigma  = 1.463e-05
Tprime_tAq_2900_MH125_LH_2017.year = 2017
Tprime_tAq_2900_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH150_LH_2017")
Tprime_tAq_2900_MH150_LH_2017.sigma  = 1.757e-05
Tprime_tAq_2900_MH150_LH_2017.year = 2017
Tprime_tAq_2900_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH175_LH_2017")
Tprime_tAq_2900_MH175_LH_2017.sigma  = 2.052e-05
Tprime_tAq_2900_MH175_LH_2017.year = 2017
Tprime_tAq_2900_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH200_LH_2017")
Tprime_tAq_2900_MH200_LH_2017.sigma  = 2.342e-05
Tprime_tAq_2900_MH200_LH_2017.year = 2017
Tprime_tAq_2900_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH250_LH_2017")
Tprime_tAq_2900_MH250_LH_2017.sigma  = 2.916e-05
Tprime_tAq_2900_MH250_LH_2017.year = 2017
Tprime_tAq_2900_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH350_LH_2017")
Tprime_tAq_2900_MH350_LH_2017.sigma  = 4.025e-05
Tprime_tAq_2900_MH350_LH_2017.year = 2017
Tprime_tAq_2900_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH450_LH_2017")
Tprime_tAq_2900_MH450_LH_2017.sigma  = 5.079e-05
Tprime_tAq_2900_MH450_LH_2017.year = 2017
Tprime_tAq_2900_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH500_LH_2017")
Tprime_tAq_2900_MH500_LH_2017.sigma  = 5.577e-05
Tprime_tAq_2900_MH500_LH_2017.year = 2017
Tprime_tAq_2900_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH25_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH25_LH_2017")
Tprime_tAq_3000_MH25_LH_2017.sigma  = 1.953e-06
Tprime_tAq_3000_MH25_LH_2017.year = 2017
Tprime_tAq_3000_MH25_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH50_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH50_LH_2017")
Tprime_tAq_3000_MH50_LH_2017.sigma  = 4.645e-06
Tprime_tAq_3000_MH50_LH_2017.year = 2017
Tprime_tAq_3000_MH50_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH75_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH75_LH_2017")
Tprime_tAq_3000_MH75_LH_2017.sigma  = 7.177e-06
Tprime_tAq_3000_MH75_LH_2017.year = 2017
Tprime_tAq_3000_MH75_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH100_LH_2017")
Tprime_tAq_3000_MH100_LH_2017.sigma  = 9.661e-06
Tprime_tAq_3000_MH100_LH_2017.year = 2017
Tprime_tAq_3000_MH100_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH125_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH125_LH_2017")
Tprime_tAq_3000_MH125_LH_2017.sigma  = 1.212e-05
Tprime_tAq_3000_MH125_LH_2017.year = 2017
Tprime_tAq_3000_MH125_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH150_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH150_LH_2017")
Tprime_tAq_3000_MH150_LH_2017.sigma  = 1.455e-05
Tprime_tAq_3000_MH150_LH_2017.year = 2017
Tprime_tAq_3000_MH150_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH175_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH175_LH_2017")
Tprime_tAq_3000_MH175_LH_2017.sigma  = 1.697e-05
Tprime_tAq_3000_MH175_LH_2017.year = 2017
Tprime_tAq_3000_MH175_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH200_LH_2017")
Tprime_tAq_3000_MH200_LH_2017.sigma  = 1.938e-05
Tprime_tAq_3000_MH200_LH_2017.year = 2017
Tprime_tAq_3000_MH200_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH250_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH250_LH_2017")
Tprime_tAq_3000_MH250_LH_2017.sigma  = 2.413e-05
Tprime_tAq_3000_MH250_LH_2017.year = 2017
Tprime_tAq_3000_MH250_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH350_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH350_LH_2017")
Tprime_tAq_3000_MH350_LH_2017.sigma  = 3.343e-05
Tprime_tAq_3000_MH350_LH_2017.year = 2017
Tprime_tAq_3000_MH350_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH450_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH450_LH_2017")
Tprime_tAq_3000_MH450_LH_2017.sigma  = 4.234e-05
Tprime_tAq_3000_MH450_LH_2017.year = 2017
Tprime_tAq_3000_MH450_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH500_LH_2017")
Tprime_tAq_3000_MH500_LH_2017.sigma  = 4.652e-05
Tprime_tAq_3000_MH500_LH_2017.year = 2017
Tprime_tAq_3000_MH500_LH_2017.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2017+"-v1/NANOAODSIM"

# 2017 bunches of tAq samples by MT mass

Tprime_tAq_600_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_LH_2017")
Tprime_tAq_600_LH_2017.year = 2017
Tprime_tAq_600_LH_2017.components = [Tprime_tAq_600_MH25_LH_2017, Tprime_tAq_600_MH50_LH_2017, Tprime_tAq_600_MH75_LH_2017, Tprime_tAq_600_MH100_LH_2017, Tprime_tAq_600_MH125_LH_2017, Tprime_tAq_600_MH150_LH_2017, Tprime_tAq_600_MH175_LH_2017, Tprime_tAq_600_MH200_LH_2017, Tprime_tAq_600_MH250_LH_2017, Tprime_tAq_600_MH350_LH_2017, Tprime_tAq_600_MH450_LH_2017, Tprime_tAq_600_MH500_LH_2017]

Tprime_tAq_700_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_LH_2017")
Tprime_tAq_700_LH_2017.year = 2017
Tprime_tAq_700_LH_2017.components = [Tprime_tAq_700_MH25_LH_2017, Tprime_tAq_700_MH50_LH_2017, Tprime_tAq_700_MH75_LH_2017, Tprime_tAq_700_MH100_LH_2017, Tprime_tAq_700_MH125_LH_2017, Tprime_tAq_700_MH150_LH_2017, Tprime_tAq_700_MH175_LH_2017, Tprime_tAq_700_MH200_LH_2017, Tprime_tAq_700_MH250_LH_2017, Tprime_tAq_700_MH350_LH_2017, Tprime_tAq_700_MH450_LH_2017, Tprime_tAq_700_MH500_LH_2017]

Tprime_tAq_800_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_LH_2017")
Tprime_tAq_800_LH_2017.year = 2017
Tprime_tAq_800_LH_2017.components = [Tprime_tAq_800_MH25_LH_2017, Tprime_tAq_800_MH50_LH_2017, Tprime_tAq_800_MH75_LH_2017, Tprime_tAq_800_MH100_LH_2017, Tprime_tAq_800_MH125_LH_2017, Tprime_tAq_800_MH150_LH_2017, Tprime_tAq_800_MH175_LH_2017, Tprime_tAq_800_MH200_LH_2017, Tprime_tAq_800_MH250_LH_2017, Tprime_tAq_800_MH350_LH_2017, Tprime_tAq_800_MH450_LH_2017, Tprime_tAq_800_MH500_LH_2017]

Tprime_tAq_900_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_LH_2017")
Tprime_tAq_900_LH_2017.year = 2017
Tprime_tAq_900_LH_2017.components = [Tprime_tAq_900_MH25_LH_2017, Tprime_tAq_900_MH50_LH_2017, Tprime_tAq_900_MH75_LH_2017, Tprime_tAq_900_MH100_LH_2017, Tprime_tAq_900_MH125_LH_2017, Tprime_tAq_900_MH150_LH_2017, Tprime_tAq_900_MH175_LH_2017, Tprime_tAq_900_MH200_LH_2017, Tprime_tAq_900_MH250_LH_2017, Tprime_tAq_900_MH350_LH_2017, Tprime_tAq_900_MH450_LH_2017, Tprime_tAq_900_MH500_LH_2017]

Tprime_tAq_1000_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_LH_2017")
Tprime_tAq_1000_LH_2017.year = 2017
Tprime_tAq_1000_LH_2017.components = [Tprime_tAq_1000_MH25_LH_2017, Tprime_tAq_1000_MH50_LH_2017, Tprime_tAq_1000_MH75_LH_2017, Tprime_tAq_1000_MH100_LH_2017, Tprime_tAq_1000_MH125_LH_2017, Tprime_tAq_1000_MH150_LH_2017, Tprime_tAq_1000_MH175_LH_2017, Tprime_tAq_1000_MH200_LH_2017, Tprime_tAq_1000_MH250_LH_2017, Tprime_tAq_1000_MH350_LH_2017, Tprime_tAq_1000_MH450_LH_2017, Tprime_tAq_1000_MH500_LH_2017]

Tprime_tAq_1100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_LH_2017")
Tprime_tAq_1100_LH_2017.year = 2017
Tprime_tAq_1100_LH_2017.components = [Tprime_tAq_1100_MH25_LH_2017, Tprime_tAq_1100_MH50_LH_2017, Tprime_tAq_1100_MH75_LH_2017, Tprime_tAq_1100_MH100_LH_2017, Tprime_tAq_1100_MH125_LH_2017, Tprime_tAq_1100_MH150_LH_2017, Tprime_tAq_1100_MH175_LH_2017, Tprime_tAq_1100_MH200_LH_2017, Tprime_tAq_1100_MH250_LH_2017, Tprime_tAq_1100_MH350_LH_2017, Tprime_tAq_1100_MH450_LH_2017, Tprime_tAq_1100_MH500_LH_2017]

Tprime_tAq_1200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_LH_2017")
Tprime_tAq_1200_LH_2017.year = 2017
Tprime_tAq_1200_LH_2017.components = [Tprime_tAq_1200_MH25_LH_2017, Tprime_tAq_1200_MH50_LH_2017, Tprime_tAq_1200_MH75_LH_2017, Tprime_tAq_1200_MH100_LH_2017, Tprime_tAq_1200_MH125_LH_2017, Tprime_tAq_1200_MH150_LH_2017, Tprime_tAq_1200_MH175_LH_2017, Tprime_tAq_1200_MH200_LH_2017, Tprime_tAq_1200_MH250_LH_2017, Tprime_tAq_1200_MH350_LH_2017, Tprime_tAq_1200_MH450_LH_2017, Tprime_tAq_1200_MH500_LH_2017]

Tprime_tAq_1300_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_LH_2017")
Tprime_tAq_1300_LH_2017.year = 2017
Tprime_tAq_1300_LH_2017.components = [Tprime_tAq_1300_MH25_LH_2017, Tprime_tAq_1300_MH50_LH_2017, Tprime_tAq_1300_MH75_LH_2017, Tprime_tAq_1300_MH100_LH_2017, Tprime_tAq_1300_MH125_LH_2017, Tprime_tAq_1300_MH150_LH_2017, Tprime_tAq_1300_MH175_LH_2017, Tprime_tAq_1300_MH200_LH_2017, Tprime_tAq_1300_MH250_LH_2017, Tprime_tAq_1300_MH350_LH_2017, Tprime_tAq_1300_MH450_LH_2017, Tprime_tAq_1300_MH500_LH_2017]

Tprime_tAq_1400_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_LH_2017")
Tprime_tAq_1400_LH_2017.year = 2017
Tprime_tAq_1400_LH_2017.components = [Tprime_tAq_1400_MH25_LH_2017, Tprime_tAq_1400_MH50_LH_2017, Tprime_tAq_1400_MH75_LH_2017, Tprime_tAq_1400_MH100_LH_2017, Tprime_tAq_1400_MH125_LH_2017, Tprime_tAq_1400_MH150_LH_2017, Tprime_tAq_1400_MH175_LH_2017, Tprime_tAq_1400_MH200_LH_2017, Tprime_tAq_1400_MH250_LH_2017, Tprime_tAq_1400_MH350_LH_2017, Tprime_tAq_1400_MH450_LH_2017, Tprime_tAq_1400_MH500_LH_2017]

Tprime_tAq_1500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_LH_2017")
Tprime_tAq_1500_LH_2017.year = 2017
Tprime_tAq_1500_LH_2017.components = [Tprime_tAq_1500_MH25_LH_2017, Tprime_tAq_1500_MH50_LH_2017, Tprime_tAq_1500_MH75_LH_2017, Tprime_tAq_1500_MH100_LH_2017, Tprime_tAq_1500_MH125_LH_2017, Tprime_tAq_1500_MH150_LH_2017, Tprime_tAq_1500_MH175_LH_2017, Tprime_tAq_1500_MH200_LH_2017, Tprime_tAq_1500_MH250_LH_2017, Tprime_tAq_1500_MH350_LH_2017, Tprime_tAq_1500_MH450_LH_2017, Tprime_tAq_1500_MH500_LH_2017]

Tprime_tAq_1600_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_LH_2017")
Tprime_tAq_1600_LH_2017.year = 2017
Tprime_tAq_1600_LH_2017.components = [Tprime_tAq_1600_MH25_LH_2017, Tprime_tAq_1600_MH50_LH_2017, Tprime_tAq_1600_MH75_LH_2017, Tprime_tAq_1600_MH100_LH_2017, Tprime_tAq_1600_MH125_LH_2017, Tprime_tAq_1600_MH150_LH_2017, Tprime_tAq_1600_MH175_LH_2017, Tprime_tAq_1600_MH200_LH_2017, Tprime_tAq_1600_MH250_LH_2017, Tprime_tAq_1600_MH350_LH_2017, Tprime_tAq_1600_MH450_LH_2017, Tprime_tAq_1600_MH500_LH_2017]

Tprime_tAq_1700_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_LH_2017")
Tprime_tAq_1700_LH_2017.year = 2017
Tprime_tAq_1700_LH_2017.components = [Tprime_tAq_1700_MH25_LH_2017, Tprime_tAq_1700_MH50_LH_2017, Tprime_tAq_1700_MH75_LH_2017, Tprime_tAq_1700_MH100_LH_2017, Tprime_tAq_1700_MH125_LH_2017, Tprime_tAq_1700_MH150_LH_2017, Tprime_tAq_1700_MH175_LH_2017, Tprime_tAq_1700_MH200_LH_2017, Tprime_tAq_1700_MH250_LH_2017, Tprime_tAq_1700_MH350_LH_2017, Tprime_tAq_1700_MH450_LH_2017, Tprime_tAq_1700_MH500_LH_2017]

Tprime_tAq_1800_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_LH_2017")
Tprime_tAq_1800_LH_2017.year = 2017
Tprime_tAq_1800_LH_2017.components = [Tprime_tAq_1800_MH25_LH_2017, Tprime_tAq_1800_MH50_LH_2017, Tprime_tAq_1800_MH75_LH_2017, Tprime_tAq_1800_MH100_LH_2017, Tprime_tAq_1800_MH125_LH_2017, Tprime_tAq_1800_MH150_LH_2017, Tprime_tAq_1800_MH175_LH_2017, Tprime_tAq_1800_MH200_LH_2017, Tprime_tAq_1800_MH250_LH_2017, Tprime_tAq_1800_MH350_LH_2017, Tprime_tAq_1800_MH450_LH_2017, Tprime_tAq_1800_MH500_LH_2017]

Tprime_tAq_1900_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_LH_2017")
Tprime_tAq_1900_LH_2017.year = 2017
Tprime_tAq_1900_LH_2017.components = [Tprime_tAq_1900_MH25_LH_2017, Tprime_tAq_1900_MH50_LH_2017, Tprime_tAq_1900_MH75_LH_2017, Tprime_tAq_1900_MH100_LH_2017, Tprime_tAq_1900_MH125_LH_2017, Tprime_tAq_1900_MH150_LH_2017, Tprime_tAq_1900_MH175_LH_2017, Tprime_tAq_1900_MH200_LH_2017, Tprime_tAq_1900_MH250_LH_2017, Tprime_tAq_1900_MH350_LH_2017, Tprime_tAq_1900_MH450_LH_2017, Tprime_tAq_1900_MH500_LH_2017]

Tprime_tAq_2000_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_LH_2017")
Tprime_tAq_2000_LH_2017.year = 2017
Tprime_tAq_2000_LH_2017.components = [Tprime_tAq_2000_MH25_LH_2017, Tprime_tAq_2000_MH50_LH_2017, Tprime_tAq_2000_MH75_LH_2017, Tprime_tAq_2000_MH100_LH_2017, Tprime_tAq_2000_MH125_LH_2017, Tprime_tAq_2000_MH150_LH_2017, Tprime_tAq_2000_MH175_LH_2017, Tprime_tAq_2000_MH200_LH_2017, Tprime_tAq_2000_MH250_LH_2017, Tprime_tAq_2000_MH350_LH_2017, Tprime_tAq_2000_MH450_LH_2017, Tprime_tAq_2000_MH500_LH_2017]

Tprime_tAq_2100_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_LH_2017")
Tprime_tAq_2100_LH_2017.year = 2017
Tprime_tAq_2100_LH_2017.components = [Tprime_tAq_2100_MH25_LH_2017, Tprime_tAq_2100_MH50_LH_2017, Tprime_tAq_2100_MH75_LH_2017, Tprime_tAq_2100_MH100_LH_2017, Tprime_tAq_2100_MH125_LH_2017, Tprime_tAq_2100_MH150_LH_2017, Tprime_tAq_2100_MH175_LH_2017, Tprime_tAq_2100_MH200_LH_2017, Tprime_tAq_2100_MH250_LH_2017, Tprime_tAq_2100_MH350_LH_2017, Tprime_tAq_2100_MH450_LH_2017, Tprime_tAq_2100_MH500_LH_2017]

Tprime_tAq_2200_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_LH_2017")
Tprime_tAq_2200_LH_2017.year = 2017
Tprime_tAq_2200_LH_2017.components = [Tprime_tAq_2200_MH25_LH_2017, Tprime_tAq_2200_MH50_LH_2017, Tprime_tAq_2200_MH75_LH_2017, Tprime_tAq_2200_MH100_LH_2017, Tprime_tAq_2200_MH125_LH_2017, Tprime_tAq_2200_MH150_LH_2017, Tprime_tAq_2200_MH175_LH_2017, Tprime_tAq_2200_MH200_LH_2017, Tprime_tAq_2200_MH250_LH_2017, Tprime_tAq_2200_MH350_LH_2017, Tprime_tAq_2200_MH450_LH_2017, Tprime_tAq_2200_MH500_LH_2017]

Tprime_tAq_2300_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_LH_2017")
Tprime_tAq_2300_LH_2017.year = 2017
Tprime_tAq_2300_LH_2017.components = [Tprime_tAq_2300_MH25_LH_2017, Tprime_tAq_2300_MH50_LH_2017, Tprime_tAq_2300_MH75_LH_2017, Tprime_tAq_2300_MH100_LH_2017, Tprime_tAq_2300_MH125_LH_2017, Tprime_tAq_2300_MH150_LH_2017, Tprime_tAq_2300_MH175_LH_2017, Tprime_tAq_2300_MH200_LH_2017, Tprime_tAq_2300_MH250_LH_2017, Tprime_tAq_2300_MH350_LH_2017, Tprime_tAq_2300_MH450_LH_2017, Tprime_tAq_2300_MH500_LH_2017]

Tprime_tAq_2400_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_LH_2017")
Tprime_tAq_2400_LH_2017.year = 2017
Tprime_tAq_2400_LH_2017.components = [Tprime_tAq_2400_MH25_LH_2017, Tprime_tAq_2400_MH50_LH_2017, Tprime_tAq_2400_MH75_LH_2017, Tprime_tAq_2400_MH100_LH_2017, Tprime_tAq_2400_MH125_LH_2017, Tprime_tAq_2400_MH150_LH_2017, Tprime_tAq_2400_MH175_LH_2017, Tprime_tAq_2400_MH200_LH_2017, Tprime_tAq_2400_MH250_LH_2017, Tprime_tAq_2400_MH350_LH_2017, Tprime_tAq_2400_MH450_LH_2017, Tprime_tAq_2400_MH500_LH_2017]

Tprime_tAq_2500_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_LH_2017")
Tprime_tAq_2500_LH_2017.year = 2017
Tprime_tAq_2500_LH_2017.components = [Tprime_tAq_2500_MH25_LH_2017, Tprime_tAq_2500_MH50_LH_2017, Tprime_tAq_2500_MH75_LH_2017, Tprime_tAq_2500_MH100_LH_2017, Tprime_tAq_2500_MH125_LH_2017, Tprime_tAq_2500_MH150_LH_2017, Tprime_tAq_2500_MH175_LH_2017, Tprime_tAq_2500_MH200_LH_2017, Tprime_tAq_2500_MH250_LH_2017, Tprime_tAq_2500_MH350_LH_2017, Tprime_tAq_2500_MH450_LH_2017, Tprime_tAq_2500_MH500_LH_2017]

Tprime_tAq_2600_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_LH_2017")
Tprime_tAq_2600_LH_2017.year = 2017
Tprime_tAq_2600_LH_2017.components = [Tprime_tAq_2600_MH25_LH_2017, Tprime_tAq_2600_MH50_LH_2017, Tprime_tAq_2600_MH75_LH_2017, Tprime_tAq_2600_MH100_LH_2017, Tprime_tAq_2600_MH125_LH_2017, Tprime_tAq_2600_MH150_LH_2017, Tprime_tAq_2600_MH175_LH_2017, Tprime_tAq_2600_MH200_LH_2017, Tprime_tAq_2600_MH250_LH_2017, Tprime_tAq_2600_MH350_LH_2017, Tprime_tAq_2600_MH450_LH_2017, Tprime_tAq_2600_MH500_LH_2017]

Tprime_tAq_2700_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_LH_2017")
Tprime_tAq_2700_LH_2017.year = 2017
Tprime_tAq_2700_LH_2017.components = [Tprime_tAq_2700_MH25_LH_2017, Tprime_tAq_2700_MH50_LH_2017, Tprime_tAq_2700_MH75_LH_2017, Tprime_tAq_2700_MH100_LH_2017, Tprime_tAq_2700_MH125_LH_2017, Tprime_tAq_2700_MH150_LH_2017, Tprime_tAq_2700_MH175_LH_2017, Tprime_tAq_2700_MH200_LH_2017, Tprime_tAq_2700_MH250_LH_2017, Tprime_tAq_2700_MH350_LH_2017, Tprime_tAq_2700_MH450_LH_2017, Tprime_tAq_2700_MH500_LH_2017]

Tprime_tAq_2800_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_LH_2017")
Tprime_tAq_2800_LH_2017.year = 2017
Tprime_tAq_2800_LH_2017.components = [Tprime_tAq_2800_MH25_LH_2017, Tprime_tAq_2800_MH50_LH_2017, Tprime_tAq_2800_MH75_LH_2017, Tprime_tAq_2800_MH100_LH_2017, Tprime_tAq_2800_MH125_LH_2017, Tprime_tAq_2800_MH150_LH_2017, Tprime_tAq_2800_MH175_LH_2017, Tprime_tAq_2800_MH200_LH_2017, Tprime_tAq_2800_MH250_LH_2017, Tprime_tAq_2800_MH350_LH_2017, Tprime_tAq_2800_MH450_LH_2017, Tprime_tAq_2800_MH500_LH_2017]

Tprime_tAq_2900_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_LH_2017")
Tprime_tAq_2900_LH_2017.year = 2017
Tprime_tAq_2900_LH_2017.components = [Tprime_tAq_2900_MH25_LH_2017, Tprime_tAq_2900_MH50_LH_2017, Tprime_tAq_2900_MH75_LH_2017, Tprime_tAq_2900_MH100_LH_2017, Tprime_tAq_2900_MH125_LH_2017, Tprime_tAq_2900_MH150_LH_2017, Tprime_tAq_2900_MH175_LH_2017, Tprime_tAq_2900_MH200_LH_2017, Tprime_tAq_2900_MH250_LH_2017, Tprime_tAq_2900_MH350_LH_2017, Tprime_tAq_2900_MH450_LH_2017, Tprime_tAq_2900_MH500_LH_2017]

Tprime_tAq_3000_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_LH_2017")
Tprime_tAq_3000_LH_2017.year = 2017
Tprime_tAq_3000_LH_2017.components = [Tprime_tAq_3000_MH25_LH_2017, Tprime_tAq_3000_MH50_LH_2017, Tprime_tAq_3000_MH75_LH_2017, Tprime_tAq_3000_MH100_LH_2017, Tprime_tAq_3000_MH125_LH_2017, Tprime_tAq_3000_MH150_LH_2017, Tprime_tAq_3000_MH175_LH_2017, Tprime_tAq_3000_MH200_LH_2017, Tprime_tAq_3000_MH250_LH_2017, Tprime_tAq_3000_MH350_LH_2017, Tprime_tAq_3000_MH450_LH_2017, Tprime_tAq_3000_MH500_LH_2017]

#Tprime_tAq_LH_2017 = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_tAq_LH_2017")
#Tprime_tAq_LH_2017.year = 2017

### 2018 ####

# MT=600                                                                                                                                                                 
Tprime_tAq_600_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH25_LH_2018")
Tprime_tAq_600_MH25_LH_2018.sigma  = 0.0002725
Tprime_tAq_600_MH25_LH_2018.year = 2018
Tprime_tAq_600_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH50_LH_2018")
Tprime_tAq_600_MH50_LH_2018.sigma  = 0.0006501
Tprime_tAq_600_MH50_LH_2018.year = 2018
Tprime_tAq_600_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH75_LH_2018")
Tprime_tAq_600_MH75_LH_2018.sigma  = 0.0009798
Tprime_tAq_600_MH75_LH_2018.year = 2018
Tprime_tAq_600_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH100_LH_2018")
Tprime_tAq_600_MH100_LH_2018.sigma  = 0.001275
Tprime_tAq_600_MH100_LH_2018.year = 2018
Tprime_tAq_600_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH125_LH_2018")
Tprime_tAq_600_MH125_LH_2018.sigma  = 0.001559
Tprime_tAq_600_MH125_LH_2018.year = 2018
Tprime_tAq_600_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH150_LH_2018")
Tprime_tAq_600_MH150_LH_2018.sigma  = 0.001796
Tprime_tAq_600_MH150_LH_2018.year = 2018
Tprime_tAq_600_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH175_LH_2018")
Tprime_tAq_600_MH175_LH_2018.sigma  = 0.001981
Tprime_tAq_600_MH175_LH_2018.year = 2018
Tprime_tAq_600_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH200_LH_2018")
Tprime_tAq_600_MH200_LH_2018.sigma  = 0.002091
Tprime_tAq_600_MH200_LH_2018.year = 2018
Tprime_tAq_600_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH250_LH_2018")
Tprime_tAq_600_MH250_LH_2018.sigma  = 0.002244
Tprime_tAq_600_MH250_LH_2018.year = 2018
Tprime_tAq_600_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH350_LH_2018")
Tprime_tAq_600_MH350_LH_2018.sigma  = 0.001713
Tprime_tAq_600_MH350_LH_2018.year = 2018
Tprime_tAq_600_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH450_LH_2018")
Tprime_tAq_600_MH450_LH_2018.sigma  = 1.434e-05
Tprime_tAq_600_MH450_LH_2018.year = 2018
Tprime_tAq_600_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_600_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_MH500_LH_2018")
Tprime_tAq_600_MH500_LH_2018.sigma  = 8.239e-08
Tprime_tAq_600_MH500_LH_2018.year = 2018
Tprime_tAq_600_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH25_LH_2018")
Tprime_tAq_700_MH25_LH_2018.sigma  = 0.000217
Tprime_tAq_700_MH25_LH_2018.year = 2018
Tprime_tAq_700_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH50_LH_2018")
Tprime_tAq_700_MH50_LH_2018.sigma  = 0.000511
Tprime_tAq_700_MH50_LH_2018.year = 2018
Tprime_tAq_700_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH75_LH_2018")
Tprime_tAq_700_MH75_LH_2018.sigma  = 0.0007798
Tprime_tAq_700_MH75_LH_2018.year = 2018
Tprime_tAq_700_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH100_LH_2018")
Tprime_tAq_700_MH100_LH_2018.sigma  = 0.00103
Tprime_tAq_700_MH100_LH_2018.year = 2018
Tprime_tAq_700_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH125_LH_2018")
Tprime_tAq_700_MH125_LH_2018.sigma  = 0.001251
Tprime_tAq_700_MH125_LH_2018.year = 2018
Tprime_tAq_700_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH150_LH_2018")
Tprime_tAq_700_MH150_LH_2018.sigma  = 0.001467
Tprime_tAq_700_MH150_LH_2018.year = 2018
Tprime_tAq_700_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH175_LH_2018")
Tprime_tAq_700_MH175_LH_2018.sigma  = 0.001651
Tprime_tAq_700_MH175_LH_2018.year = 2018
Tprime_tAq_700_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH200_LH_2018")
Tprime_tAq_700_MH200_LH_2018.sigma  = 0.001806
Tprime_tAq_700_MH200_LH_2018.year = 2018
Tprime_tAq_700_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH250_LH_2018")
Tprime_tAq_700_MH250_LH_2018.sigma  = 0.002018
Tprime_tAq_700_MH250_LH_2018.year = 2018
Tprime_tAq_700_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH350_LH_2018")
Tprime_tAq_700_MH350_LH_2018.sigma  = 0.001986
Tprime_tAq_700_MH350_LH_2018.year = 2018
Tprime_tAq_700_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH450_LH_2018")
Tprime_tAq_700_MH450_LH_2018.sigma  = 0.001326
Tprime_tAq_700_MH450_LH_2018.year = 2018
Tprime_tAq_700_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_700_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_MH500_LH_2018")
Tprime_tAq_700_MH500_LH_2018.sigma  = 0.0007135
Tprime_tAq_700_MH500_LH_2018.year = 2018
Tprime_tAq_700_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH25_LH_2018")
Tprime_tAq_800_MH25_LH_2018.sigma  = 0.000168
Tprime_tAq_800_MH25_LH_2018.year = 2018
Tprime_tAq_800_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH50_LH_2018")
Tprime_tAq_800_MH50_LH_2018.sigma  = 0.0003993
Tprime_tAq_800_MH50_LH_2018.year = 2018
Tprime_tAq_800_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH75_LH_2018")
Tprime_tAq_800_MH75_LH_2018.sigma  = 0.0006061
Tprime_tAq_800_MH75_LH_2018.year = 2018
Tprime_tAq_800_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH100_LH_2018")
Tprime_tAq_800_MH100_LH_2018.sigma  = 0.0008047
Tprime_tAq_800_MH100_LH_2018.year = 2018
Tprime_tAq_800_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH125_LH_2018")
Tprime_tAq_800_MH125_LH_2018.sigma  = 0.0009924
Tprime_tAq_800_MH125_LH_2018.year = 2018
Tprime_tAq_800_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH150_LH_2018")
Tprime_tAq_800_MH150_LH_2018.sigma  = 0.001166
Tprime_tAq_800_MH150_LH_2018.year = 2018
Tprime_tAq_800_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH175_LH_2018")
Tprime_tAq_800_MH175_LH_2018.sigma  = 0.001324
Tprime_tAq_800_MH175_LH_2018.year = 2018
Tprime_tAq_800_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH200_LH_2018")
Tprime_tAq_800_MH200_LH_2018.sigma  = 0.001468
Tprime_tAq_800_MH200_LH_2018.year = 2018
Tprime_tAq_800_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH250_LH_2018")
Tprime_tAq_800_MH250_LH_2018.sigma  = 0.001708
Tprime_tAq_800_MH250_LH_2018.year = 2018
Tprime_tAq_800_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH350_LH_2018")
Tprime_tAq_800_MH350_LH_2018.sigma  = 0.001872
Tprime_tAq_800_MH350_LH_2018.year = 2018
Tprime_tAq_800_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH450_LH_2018")
Tprime_tAq_800_MH450_LH_2018.sigma  = 0.00164
Tprime_tAq_800_MH450_LH_2018.year = 2018
Tprime_tAq_800_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_800_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_MH500_LH_2018")
Tprime_tAq_800_MH500_LH_2018.sigma  = 0.001371
Tprime_tAq_800_MH500_LH_2018.year = 2018
Tprime_tAq_800_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH25_LH_2018")
Tprime_tAq_900_MH25_LH_2018.sigma  = 0.0001338
Tprime_tAq_900_MH25_LH_2018.year = 2018
Tprime_tAq_900_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH50_LH_2018")
Tprime_tAq_900_MH50_LH_2018.sigma  = 0.0003153
Tprime_tAq_900_MH50_LH_2018.year = 2018
Tprime_tAq_900_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH75_LH_2018")
Tprime_tAq_900_MH75_LH_2018.sigma  = 0.0004835
Tprime_tAq_900_MH75_LH_2018.year = 2018
Tprime_tAq_900_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH100_LH_2018")
Tprime_tAq_900_MH100_LH_2018.sigma  = 0.0006426
Tprime_tAq_900_MH100_LH_2018.year = 2018
Tprime_tAq_900_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH125_LH_2018")
Tprime_tAq_900_MH125_LH_2018.sigma  = 0.0007962
Tprime_tAq_900_MH125_LH_2018.year = 2018
Tprime_tAq_900_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH150_LH_2018")
Tprime_tAq_900_MH150_LH_2018.sigma  = 0.0009446
Tprime_tAq_900_MH150_LH_2018.year = 2018
Tprime_tAq_900_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH175_LH_2018")
Tprime_tAq_900_MH175_LH_2018.sigma  = 0.001081
Tprime_tAq_900_MH175_LH_2018.year = 2018
Tprime_tAq_900_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH200_LH_2018")
Tprime_tAq_900_MH200_LH_2018.sigma  = 0.001203
Tprime_tAq_900_MH200_LH_2018.year = 2018
Tprime_tAq_900_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH250_LH_2018")
Tprime_tAq_900_MH250_LH_2018.sigma  = 0.001414
Tprime_tAq_900_MH250_LH_2018.year = 2018
Tprime_tAq_900_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH350_LH_2018")
Tprime_tAq_900_MH350_LH_2018.sigma  = 0.001681
Tprime_tAq_900_MH350_LH_2018.year = 2018
Tprime_tAq_900_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH450_LH_2018")
Tprime_tAq_900_MH450_LH_2018.sigma  = 0.001634
Tprime_tAq_900_MH450_LH_2018.year = 2018
Tprime_tAq_900_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_900_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_MH500_LH_2018")
Tprime_tAq_900_MH500_LH_2018.sigma  = 0.001522
Tprime_tAq_900_MH500_LH_2018.year = 2018
Tprime_tAq_900_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH25_LH_2018")
Tprime_tAq_1000_MH25_LH_2018.sigma  = 0.0001052
Tprime_tAq_1000_MH25_LH_2018.year = 2018
Tprime_tAq_1000_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH50_LH_2018")
Tprime_tAq_1000_MH50_LH_2018.sigma  = 0.0002505
Tprime_tAq_1000_MH50_LH_2018.year = 2018
Tprime_tAq_1000_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH75_LH_2018")
Tprime_tAq_1000_MH75_LH_2018.sigma  = 0.0003843
Tprime_tAq_1000_MH75_LH_2018.year = 2018
Tprime_tAq_1000_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH100_LH_2018")
Tprime_tAq_1000_MH100_LH_2018.sigma  = 0.0005132
Tprime_tAq_1000_MH100_LH_2018.year = 2018
Tprime_tAq_1000_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH125_LH_2018")
Tprime_tAq_1000_MH125_LH_2018.sigma  = 0.0006371
Tprime_tAq_1000_MH125_LH_2018.year = 2018
Tprime_tAq_1000_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH150_LH_2018")
Tprime_tAq_1000_MH150_LH_2018.sigma  = 0.0007554
Tprime_tAq_1000_MH150_LH_2018.year = 2018
Tprime_tAq_1000_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH175_LH_2018")
Tprime_tAq_1000_MH175_LH_2018.sigma  = 0.0008683
Tprime_tAq_1000_MH175_LH_2018.year = 2018
Tprime_tAq_1000_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH200_LH_2018")
Tprime_tAq_1000_MH200_LH_2018.sigma  = 0.000973
Tprime_tAq_1000_MH200_LH_2018.year = 2018
Tprime_tAq_1000_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH250_LH_2018")
Tprime_tAq_1000_MH250_LH_2018.sigma  = 0.00116
Tprime_tAq_1000_MH250_LH_2018.year = 2018
Tprime_tAq_1000_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH350_LH_2018")
Tprime_tAq_1000_MH350_LH_2018.sigma  = 0.001412
Tprime_tAq_1000_MH350_LH_2018.year = 2018
Tprime_tAq_1000_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH450_LH_2018")
Tprime_tAq_1000_MH450_LH_2018.sigma  = 0.001484
Tprime_tAq_1000_MH450_LH_2018.year = 2018
Tprime_tAq_1000_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1000_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_MH500_LH_2018")
Tprime_tAq_1000_MH500_LH_2018.sigma  = 0.001448
Tprime_tAq_1000_MH500_LH_2018.year = 2018
Tprime_tAq_1000_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH25_LH_2018")
Tprime_tAq_1100_MH25_LH_2018.sigma  = 8.434e-05
Tprime_tAq_1100_MH25_LH_2018.year = 2018
Tprime_tAq_1100_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH50_LH_2018")
Tprime_tAq_1100_MH50_LH_2018.sigma  = 0.0002003
Tprime_tAq_1100_MH50_LH_2018.year = 2018
Tprime_tAq_1100_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH75_LH_2018")
Tprime_tAq_1100_MH75_LH_2018.sigma  = 0.000308
Tprime_tAq_1100_MH75_LH_2018.year = 2018
Tprime_tAq_1100_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH100_LH_2018")
Tprime_tAq_1100_MH100_LH_2018.sigma  = 0.0004107
Tprime_tAq_1100_MH100_LH_2018.year = 2018
Tprime_tAq_1100_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH125_LH_2018")
Tprime_tAq_1100_MH125_LH_2018.sigma  = 0.0005111
Tprime_tAq_1100_MH125_LH_2018.year = 2018
Tprime_tAq_1100_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH150_LH_2018")
Tprime_tAq_1100_MH150_LH_2018.sigma  = 0.0006076
Tprime_tAq_1100_MH150_LH_2018.year = 2018
Tprime_tAq_1100_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH175_LH_2018")
Tprime_tAq_1100_MH175_LH_2018.sigma  = 0.0007005
Tprime_tAq_1100_MH175_LH_2018.year = 2018
Tprime_tAq_1100_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH200_LH_2018")
Tprime_tAq_1100_MH200_LH_2018.sigma  = 0.0007884
Tprime_tAq_1100_MH200_LH_2018.year = 2018
Tprime_tAq_1100_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH250_LH_2018")
Tprime_tAq_1100_MH250_LH_2018.sigma  = 0.0009486
Tprime_tAq_1100_MH250_LH_2018.year = 2018
Tprime_tAq_1100_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH350_LH_2018")
Tprime_tAq_1100_MH350_LH_2018.sigma  = 0.001186
Tprime_tAq_1100_MH350_LH_2018.year = 2018
Tprime_tAq_1100_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH450_LH_2018")
Tprime_tAq_1100_MH450_LH_2018.sigma  = 0.001302
Tprime_tAq_1100_MH450_LH_2018.year = 2018
Tprime_tAq_1100_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1100_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_MH500_LH_2018")
Tprime_tAq_1100_MH500_LH_2018.sigma  = 0.001306
Tprime_tAq_1100_MH500_LH_2018.year = 2018
Tprime_tAq_1100_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH25_LH_2018")
Tprime_tAq_1200_MH25_LH_2018.sigma  = 6.834e-05
Tprime_tAq_1200_MH25_LH_2018.year = 2018
Tprime_tAq_1200_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH50_LH_2018")
Tprime_tAq_1200_MH50_LH_2018.sigma  = 0.0001621
Tprime_tAq_1200_MH50_LH_2018.year = 2018
Tprime_tAq_1200_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH75_LH_2018")
Tprime_tAq_1200_MH75_LH_2018.sigma  = 0.0002496
Tprime_tAq_1200_MH75_LH_2018.year = 2018
Tprime_tAq_1200_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH100_LH_2018")
Tprime_tAq_1200_MH100_LH_2018.sigma  = 0.0003333
Tprime_tAq_1200_MH100_LH_2018.year = 2018
Tprime_tAq_1200_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH125_LH_2018")
Tprime_tAq_1200_MH125_LH_2018.sigma  = 0.0004151
Tprime_tAq_1200_MH125_LH_2018.year = 2018
Tprime_tAq_1200_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH150_LH_2018")
Tprime_tAq_1200_MH150_LH_2018.sigma  = 0.0004946
Tprime_tAq_1200_MH150_LH_2018.year = 2018
Tprime_tAq_1200_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH175_LH_2018")
Tprime_tAq_1200_MH175_LH_2018.sigma  = 0.0005709
Tprime_tAq_1200_MH175_LH_2018.year = 2018
Tprime_tAq_1200_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH200_LH_2018")
Tprime_tAq_1200_MH200_LH_2018.sigma  = 0.0006444
Tprime_tAq_1200_MH200_LH_2018.year = 2018
Tprime_tAq_1200_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH250_LH_2018")
Tprime_tAq_1200_MH250_LH_2018.sigma  = 0.0007796
Tprime_tAq_1200_MH250_LH_2018.year = 2018
Tprime_tAq_1200_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH350_LH_2018")
Tprime_tAq_1200_MH350_LH_2018.sigma  = 0.0009997
Tprime_tAq_1200_MH350_LH_2018.year = 2018
Tprime_tAq_1200_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH450_LH_2018")
Tprime_tAq_1200_MH450_LH_2018.sigma  = 0.001124
Tprime_tAq_1200_MH450_LH_2018.year = 2018
Tprime_tAq_1200_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1200_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_MH500_LH_2018")
Tprime_tAq_1200_MH500_LH_2018.sigma  = 0.001151
Tprime_tAq_1200_MH500_LH_2018.year = 2018
Tprime_tAq_1200_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH25_LH_2018")
Tprime_tAq_1300_MH25_LH_2018.sigma  = 5.51e-05
Tprime_tAq_1300_MH25_LH_2018.year = 2018
Tprime_tAq_1300_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH50_LH_2018")
Tprime_tAq_1300_MH50_LH_2018.sigma  = 0.000131
Tprime_tAq_1300_MH50_LH_2018.year = 2018
Tprime_tAq_1300_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH75_LH_2018")
Tprime_tAq_1300_MH75_LH_2018.sigma  = 0.0002016
Tprime_tAq_1300_MH75_LH_2018.year = 2018
Tprime_tAq_1300_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH100_LH_2018")
Tprime_tAq_1300_MH100_LH_2018.sigma  = 0.0002701
Tprime_tAq_1300_MH100_LH_2018.year = 2018
Tprime_tAq_1300_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH125_LH_2018")
Tprime_tAq_1300_MH125_LH_2018.sigma  = 0.0003369
Tprime_tAq_1300_MH125_LH_2018.year = 2018
Tprime_tAq_1300_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH150_LH_2018")
Tprime_tAq_1300_MH150_LH_2018.sigma  = 0.000402
Tprime_tAq_1300_MH150_LH_2018.year = 2018
Tprime_tAq_1300_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH175_LH_2018")
Tprime_tAq_1300_MH175_LH_2018.sigma  = 0.000465
Tprime_tAq_1300_MH175_LH_2018.year = 2018
Tprime_tAq_1300_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH200_LH_2018")
Tprime_tAq_1300_MH200_LH_2018.sigma  = 0.0005258
Tprime_tAq_1300_MH200_LH_2018.year = 2018
Tprime_tAq_1300_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH250_LH_2018")
Tprime_tAq_1300_MH250_LH_2018.sigma  = 0.0006392
Tprime_tAq_1300_MH250_LH_2018.year = 2018
Tprime_tAq_1300_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH350_LH_2018")
Tprime_tAq_1300_MH350_LH_2018.sigma  = 0.0008297
Tprime_tAq_1300_MH350_LH_2018.year = 2018
Tprime_tAq_1300_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH450_LH_2018")
Tprime_tAq_1300_MH450_LH_2018.sigma  = 0.000958
Tprime_tAq_1300_MH450_LH_2018.year = 2018
Tprime_tAq_1300_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1300_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_MH500_LH_2018")
Tprime_tAq_1300_MH500_LH_2018.sigma  = 0.0009965
Tprime_tAq_1300_MH500_LH_2018.year = 2018
Tprime_tAq_1300_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH25_LH_2018")
Tprime_tAq_1400_MH25_LH_2018.sigma  = 4.468e-05
Tprime_tAq_1400_MH25_LH_2018.year = 2018
Tprime_tAq_1400_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH50_LH_2018")
Tprime_tAq_1400_MH50_LH_2018.sigma  = 0.0001062
Tprime_tAq_1400_MH50_LH_2018.year = 2018
Tprime_tAq_1400_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH75_LH_2018")
Tprime_tAq_1400_MH75_LH_2018.sigma  = 0.0001637
Tprime_tAq_1400_MH75_LH_2018.year = 2018
Tprime_tAq_1400_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH100_LH_2018")
Tprime_tAq_1400_MH100_LH_2018.sigma  = 0.0002192
Tprime_tAq_1400_MH100_LH_2018.year = 2018
Tprime_tAq_1400_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH125_LH_2018")
Tprime_tAq_1400_MH125_LH_2018.sigma  = 0.0002736
Tprime_tAq_1400_MH125_LH_2018.year = 2018
Tprime_tAq_1400_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH150_LH_2018")
Tprime_tAq_1400_MH150_LH_2018.sigma  = 0.0003269
Tprime_tAq_1400_MH150_LH_2018.year = 2018
Tprime_tAq_1400_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH175_LH_2018")
Tprime_tAq_1400_MH175_LH_2018.sigma  = 0.0003787
Tprime_tAq_1400_MH175_LH_2018.year = 2018
Tprime_tAq_1400_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH200_LH_2018")
Tprime_tAq_1400_MH200_LH_2018.sigma  = 0.0004289
Tprime_tAq_1400_MH200_LH_2018.year = 2018
Tprime_tAq_1400_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH250_LH_2018")
Tprime_tAq_1400_MH250_LH_2018.sigma  = 0.0005231
Tprime_tAq_1400_MH250_LH_2018.year = 2018
Tprime_tAq_1400_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH350_LH_2018")
Tprime_tAq_1400_MH350_LH_2018.sigma  = 0.0006847
Tprime_tAq_1400_MH350_LH_2018.year = 2018
Tprime_tAq_1400_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH450_LH_2018")
Tprime_tAq_1400_MH450_LH_2018.sigma  = 0.0008049
Tprime_tAq_1400_MH450_LH_2018.year = 2018
Tprime_tAq_1400_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1400_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_MH500_LH_2018")
Tprime_tAq_1400_MH500_LH_2018.sigma  = 0.0008453
Tprime_tAq_1400_MH500_LH_2018.year = 2018
Tprime_tAq_1400_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH25_LH_2018")
Tprime_tAq_1500_MH25_LH_2018.sigma  = 3.581e-05
Tprime_tAq_1500_MH25_LH_2018.year = 2018
Tprime_tAq_1500_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH50_LH_2018")
Tprime_tAq_1500_MH50_LH_2018.sigma  = 8.514e-05
Tprime_tAq_1500_MH50_LH_2018.year = 2018
Tprime_tAq_1500_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH75_LH_2018")
Tprime_tAq_1500_MH75_LH_2018.sigma  = 0.0001313
Tprime_tAq_1500_MH75_LH_2018.year = 2018
Tprime_tAq_1500_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH100_LH_2018")
Tprime_tAq_1500_MH100_LH_2018.sigma  = 0.0001762
Tprime_tAq_1500_MH100_LH_2018.year = 2018
Tprime_tAq_1500_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH125_LH_2018")
Tprime_tAq_1500_MH125_LH_2018.sigma  = 0.0002202
Tprime_tAq_1500_MH125_LH_2018.year = 2018
Tprime_tAq_1500_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH150_LH_2018")
Tprime_tAq_1500_MH150_LH_2018.sigma  = 0.0002633
Tprime_tAq_1500_MH150_LH_2018.year = 2018
Tprime_tAq_1500_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH175_LH_2018")
Tprime_tAq_1500_MH175_LH_2018.sigma  = 0.0003051
Tprime_tAq_1500_MH175_LH_2018.year = 2018
Tprime_tAq_1500_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH200_LH_2018")
Tprime_tAq_1500_MH200_LH_2018.sigma  = 0.0003467
Tprime_tAq_1500_MH200_LH_2018.year = 2018
Tprime_tAq_1500_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH250_LH_2018")
Tprime_tAq_1500_MH250_LH_2018.sigma  = 0.0004246
Tprime_tAq_1500_MH250_LH_2018.year = 2018
Tprime_tAq_1500_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH350_LH_2018")
Tprime_tAq_1500_MH350_LH_2018.sigma  = 0.0005626
Tprime_tAq_1500_MH350_LH_2018.year = 2018
Tprime_tAq_1500_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH450_LH_2018")
Tprime_tAq_1500_MH450_LH_2018.sigma  = 0.0006697
Tprime_tAq_1500_MH450_LH_2018.year = 2018
Tprime_tAq_1500_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1500_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_MH500_LH_2018")
Tprime_tAq_1500_MH500_LH_2018.sigma  = 0.0007093
Tprime_tAq_1500_MH500_LH_2018.year = 2018
Tprime_tAq_1500_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH25_LH_2018")
Tprime_tAq_1600_MH25_LH_2018.sigma  = 2.945e-05
Tprime_tAq_1600_MH25_LH_2018.year = 2018
Tprime_tAq_1600_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH50_LH_2018")
Tprime_tAq_1600_MH50_LH_2018.sigma  = 7.004e-05
Tprime_tAq_1600_MH50_LH_2018.year = 2018
Tprime_tAq_1600_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH75_LH_2018")
Tprime_tAq_1600_MH75_LH_2018.sigma  = 0.0001079
Tprime_tAq_1600_MH75_LH_2018.year = 2018
Tprime_tAq_1600_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH100_LH_2018")
Tprime_tAq_1600_MH100_LH_2018.sigma  = 0.0001449
Tprime_tAq_1600_MH100_LH_2018.year = 2018
Tprime_tAq_1600_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH125_LH_2018")
Tprime_tAq_1600_MH125_LH_2018.sigma  = 0.0001812
Tprime_tAq_1600_MH125_LH_2018.year = 2018
Tprime_tAq_1600_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH150_LH_2018")
Tprime_tAq_1600_MH150_LH_2018.sigma  = 0.0002168
Tprime_tAq_1600_MH150_LH_2018.year = 2018
Tprime_tAq_1600_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH175_LH_2018")
Tprime_tAq_1600_MH175_LH_2018.sigma  = 0.0002517
Tprime_tAq_1600_MH175_LH_2018.year = 2018
Tprime_tAq_1600_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH200_LH_2018")
Tprime_tAq_1600_MH200_LH_2018.sigma  = 0.0002858
Tprime_tAq_1600_MH200_LH_2018.year = 2018
Tprime_tAq_1600_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH250_LH_2018")
Tprime_tAq_1600_MH250_LH_2018.sigma  = 0.0003522
Tprime_tAq_1600_MH250_LH_2018.year = 2018
Tprime_tAq_1600_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH350_LH_2018")
Tprime_tAq_1600_MH350_LH_2018.sigma  = 0.0004698
Tprime_tAq_1600_MH350_LH_2018.year = 2018
Tprime_tAq_1600_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH450_LH_2018")
Tprime_tAq_1600_MH450_LH_2018.sigma  = 0.0005646
Tprime_tAq_1600_MH450_LH_2018.year = 2018
Tprime_tAq_1600_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1600_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_MH500_LH_2018")
Tprime_tAq_1600_MH500_LH_2018.sigma  = 0.0006016
Tprime_tAq_1600_MH500_LH_2018.year = 2018
Tprime_tAq_1600_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH25_LH_2018")
Tprime_tAq_1700_MH25_LH_2018.sigma  = 2.409e-05
Tprime_tAq_1700_MH25_LH_2018.year = 2018
Tprime_tAq_1700_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH50_LH_2018")
Tprime_tAq_1700_MH50_LH_2018.sigma  = 5.729e-05
Tprime_tAq_1700_MH50_LH_2018.year = 2018
Tprime_tAq_1700_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH75_LH_2018")
Tprime_tAq_1700_MH75_LH_2018.sigma  = 8.839e-05
Tprime_tAq_1700_MH75_LH_2018.year = 2018
Tprime_tAq_1700_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH100_LH_2018")
Tprime_tAq_1700_MH100_LH_2018.sigma  = 0.0001189
Tprime_tAq_1700_MH100_LH_2018.year = 2018
Tprime_tAq_1700_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH125_LH_2018")
Tprime_tAq_1700_MH125_LH_2018.sigma  = 0.0001488
Tprime_tAq_1700_MH125_LH_2018.year = 2018
Tprime_tAq_1700_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH150_LH_2018")
Tprime_tAq_1700_MH150_LH_2018.sigma  = 0.0001781
Tprime_tAq_1700_MH150_LH_2018.year = 2018
Tprime_tAq_1700_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH175_LH_2018")
Tprime_tAq_1700_MH175_LH_2018.sigma  = 0.0002068
Tprime_tAq_1700_MH175_LH_2018.year = 2018
Tprime_tAq_1700_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH200_LH_2018")
Tprime_tAq_1700_MH200_LH_2018.sigma  = 0.0002351
Tprime_tAq_1700_MH200_LH_2018.year = 2018
Tprime_tAq_1700_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH250_LH_2018")
Tprime_tAq_1700_MH250_LH_2018.sigma  = 0.0002892
Tprime_tAq_1700_MH250_LH_2018.year = 2018
Tprime_tAq_1700_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH350_LH_2018")
Tprime_tAq_1700_MH350_LH_2018.sigma  = 0.0003879
Tprime_tAq_1700_MH350_LH_2018.year = 2018
Tprime_tAq_1700_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH450_LH_2018")
Tprime_tAq_1700_MH450_LH_2018.sigma  = 0.0004715
Tprime_tAq_1700_MH450_LH_2018.year = 2018
Tprime_tAq_1700_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1700_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_MH500_LH_2018")
Tprime_tAq_1700_MH500_LH_2018.sigma  = 0.000506
Tprime_tAq_1700_MH500_LH_2018.year = 2018
Tprime_tAq_1700_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH25_LH_2018")
Tprime_tAq_1800_MH25_LH_2018.sigma  = 1.955e-05
Tprime_tAq_1800_MH25_LH_2018.year = 2018
Tprime_tAq_1800_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH50_LH_2018")
Tprime_tAq_1800_MH50_LH_2018.sigma  = 4.652e-05
Tprime_tAq_1800_MH50_LH_2018.year = 2018
Tprime_tAq_1800_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH75_LH_2018")
Tprime_tAq_1800_MH75_LH_2018.sigma  = 7.183e-05
Tprime_tAq_1800_MH75_LH_2018.year = 2018
Tprime_tAq_1800_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH100_LH_2018")
Tprime_tAq_1800_MH100_LH_2018.sigma  = 9.639e-05
Tprime_tAq_1800_MH100_LH_2018.year = 2018
Tprime_tAq_1800_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH125_LH_2018")
Tprime_tAq_1800_MH125_LH_2018.sigma  = 0.0001207
Tprime_tAq_1800_MH125_LH_2018.year = 2018
Tprime_tAq_1800_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH150_LH_2018")
Tprime_tAq_1800_MH150_LH_2018.sigma  = 0.0001446
Tprime_tAq_1800_MH150_LH_2018.year = 2018
Tprime_tAq_1800_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH175_LH_2018")
Tprime_tAq_1800_MH175_LH_2018.sigma  = 0.000168
Tprime_tAq_1800_MH175_LH_2018.year = 2018
Tprime_tAq_1800_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH200_LH_2018")
Tprime_tAq_1800_MH200_LH_2018.sigma  = 0.000191
Tprime_tAq_1800_MH200_LH_2018.year = 2018
Tprime_tAq_1800_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH250_LH_2018")
Tprime_tAq_1800_MH250_LH_2018.sigma  = 0.0002358
Tprime_tAq_1800_MH250_LH_2018.year = 2018
Tprime_tAq_1800_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH350_LH_2018")
Tprime_tAq_1800_MH350_LH_2018.sigma  = 0.0003182
Tprime_tAq_1800_MH350_LH_2018.year = 2018
Tprime_tAq_1800_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH450_LH_2018")
Tprime_tAq_1800_MH450_LH_2018.sigma  = 0.0003873
Tprime_tAq_1800_MH450_LH_2018.year = 2018
Tprime_tAq_1800_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1800_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_MH500_LH_2018")
Tprime_tAq_1800_MH500_LH_2018.sigma  = 0.0004171
Tprime_tAq_1800_MH500_LH_2018.year = 2018
Tprime_tAq_1800_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH25_LH_2018")
Tprime_tAq_1900_MH25_LH_2018.sigma  = 1.601e-05
Tprime_tAq_1900_MH25_LH_2018.year = 2018
Tprime_tAq_1900_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH50_LH_2018")
Tprime_tAq_1900_MH50_LH_2018.sigma  = 3.811e-05
Tprime_tAq_1900_MH50_LH_2018.year = 2018
Tprime_tAq_1900_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH75_LH_2018")
Tprime_tAq_1900_MH75_LH_2018.sigma  = 5.881e-05
Tprime_tAq_1900_MH75_LH_2018.year = 2018
Tprime_tAq_1900_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH100_LH_2018")
Tprime_tAq_1900_MH100_LH_2018.sigma  = 7.904e-05
Tprime_tAq_1900_MH100_LH_2018.year = 2018
Tprime_tAq_1900_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH125_LH_2018")
Tprime_tAq_1900_MH125_LH_2018.sigma  = 9.897e-05
Tprime_tAq_1900_MH125_LH_2018.year = 2018
Tprime_tAq_1900_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH150_LH_2018")
Tprime_tAq_1900_MH150_LH_2018.sigma  = 0.0001185
Tprime_tAq_1900_MH150_LH_2018.year = 2018
Tprime_tAq_1900_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH175_LH_2018")
Tprime_tAq_1900_MH175_LH_2018.sigma  = 0.0001379
Tprime_tAq_1900_MH175_LH_2018.year = 2018
Tprime_tAq_1900_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH200_LH_2018")
Tprime_tAq_1900_MH200_LH_2018.sigma  = 0.000157
Tprime_tAq_1900_MH200_LH_2018.year = 2018
Tprime_tAq_1900_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH250_LH_2018")
Tprime_tAq_1900_MH250_LH_2018.sigma  = 0.000194
Tprime_tAq_1900_MH250_LH_2018.year = 2018
Tprime_tAq_1900_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH350_LH_2018")
Tprime_tAq_1900_MH350_LH_2018.sigma  = 0.0002628
Tprime_tAq_1900_MH350_LH_2018.year = 2018
Tprime_tAq_1900_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH450_LH_2018")
Tprime_tAq_1900_MH450_LH_2018.sigma  = 0.0003233
Tprime_tAq_1900_MH450_LH_2018.year = 2018
Tprime_tAq_1900_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_1900_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_MH500_LH_2018")
Tprime_tAq_1900_MH500_LH_2018.sigma  = 0.0003491
Tprime_tAq_1900_MH500_LH_2018.year = 2018
Tprime_tAq_1900_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT1900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH25_LH_2018")
Tprime_tAq_2000_MH25_LH_2018.sigma  = 1.331e-05
Tprime_tAq_2000_MH25_LH_2018.year = 2018
Tprime_tAq_2000_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH50_LH_2018")
Tprime_tAq_2000_MH50_LH_2018.sigma  = 3.168e-05
Tprime_tAq_2000_MH50_LH_2018.year = 2018
Tprime_tAq_2000_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH75_LH_2018")
Tprime_tAq_2000_MH75_LH_2018.sigma  = 4.889e-05
Tprime_tAq_2000_MH75_LH_2018.year = 2018
Tprime_tAq_2000_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH100_LH_2018")
Tprime_tAq_2000_MH100_LH_2018.sigma  = 6.573e-05
Tprime_tAq_2000_MH100_LH_2018.year = 2018
Tprime_tAq_2000_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH125_LH_2018")
Tprime_tAq_2000_MH125_LH_2018.sigma  = 8.233e-05
Tprime_tAq_2000_MH125_LH_2018.year = 2018
Tprime_tAq_2000_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH150_LH_2018")
Tprime_tAq_2000_MH150_LH_2018.sigma  = 9.871e-05
Tprime_tAq_2000_MH150_LH_2018.year = 2018
Tprime_tAq_2000_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH175_LH_2018")
Tprime_tAq_2000_MH175_LH_2018.sigma  = 0.0001149
Tprime_tAq_2000_MH175_LH_2018.year = 2018
Tprime_tAq_2000_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH200_LH_2018")
Tprime_tAq_2000_MH200_LH_2018.sigma  = 0.0001308
Tprime_tAq_2000_MH200_LH_2018.year = 2018
Tprime_tAq_2000_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH250_LH_2018")
Tprime_tAq_2000_MH250_LH_2018.sigma  = 0.0001618
Tprime_tAq_2000_MH250_LH_2018.year = 2018
Tprime_tAq_2000_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH350_LH_2018")
Tprime_tAq_2000_MH350_LH_2018.sigma  = 0.0002198
Tprime_tAq_2000_MH350_LH_2018.year = 2018
Tprime_tAq_2000_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH450_LH_2018")
Tprime_tAq_2000_MH450_LH_2018.sigma  = 0.0002711
Tprime_tAq_2000_MH450_LH_2018.year = 2018
Tprime_tAq_2000_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2000_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_MH500_LH_2018")
Tprime_tAq_2000_MH500_LH_2018.sigma  = 0.0002938
Tprime_tAq_2000_MH500_LH_2018.year = 2018
Tprime_tAq_2000_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH25_LH_2018")
Tprime_tAq_2100_MH25_LH_2018.sigma  = 1.078e-05
Tprime_tAq_2100_MH25_LH_2018.year = 2018
Tprime_tAq_2100_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH50_LH_2018")
Tprime_tAq_2100_MH50_LH_2018.sigma  = 2.565e-05
Tprime_tAq_2100_MH50_LH_2018.year = 2018
Tprime_tAq_2100_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH75_LH_2018")
Tprime_tAq_2100_MH75_LH_2018.sigma  = 3.96e-05
Tprime_tAq_2100_MH75_LH_2018.year = 2018
Tprime_tAq_2100_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH100_LH_2018")
Tprime_tAq_2100_MH100_LH_2018.sigma  = 5.324e-05
Tprime_tAq_2100_MH100_LH_2018.year = 2018
Tprime_tAq_2100_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH125_LH_2018")
Tprime_tAq_2100_MH125_LH_2018.sigma  = 6.671e-05
Tprime_tAq_2100_MH125_LH_2018.year = 2018
Tprime_tAq_2100_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH150_LH_2018")
Tprime_tAq_2100_MH150_LH_2018.sigma  = 8.002e-05
Tprime_tAq_2100_MH150_LH_2018.year = 2018
Tprime_tAq_2100_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH175_LH_2018")
Tprime_tAq_2100_MH175_LH_2018.sigma  = 9.315e-05
Tprime_tAq_2100_MH175_LH_2018.year = 2018
Tprime_tAq_2100_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH200_LH_2018")
Tprime_tAq_2100_MH200_LH_2018.sigma  = 0.0001061
Tprime_tAq_2100_MH200_LH_2018.year = 2018
Tprime_tAq_2100_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH250_LH_2018")
Tprime_tAq_2100_MH250_LH_2018.sigma  = 0.0001314
Tprime_tAq_2100_MH250_LH_2018.year = 2018
Tprime_tAq_2100_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH350_LH_2018")
Tprime_tAq_2100_MH350_LH_2018.sigma  = 0.0001791
Tprime_tAq_2100_MH350_LH_2018.year = 2018
Tprime_tAq_2100_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH450_LH_2018")
Tprime_tAq_2100_MH450_LH_2018.sigma  = 0.0002216
Tprime_tAq_2100_MH450_LH_2018.year = 2018
Tprime_tAq_2100_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2100_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_MH500_LH_2018")
Tprime_tAq_2100_MH500_LH_2018.sigma  = 0.0002407
Tprime_tAq_2100_MH500_LH_2018.year = 2018
Tprime_tAq_2100_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2100_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH25_LH_2018")
Tprime_tAq_2200_MH25_LH_2018.sigma  = 8.958e-06
Tprime_tAq_2200_MH25_LH_2018.year = 2018
Tprime_tAq_2200_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH50_LH_2018")
Tprime_tAq_2200_MH50_LH_2018.sigma  = 2.132e-05
Tprime_tAq_2200_MH50_LH_2018.year = 2018
Tprime_tAq_2200_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH75_LH_2018")
Tprime_tAq_2200_MH75_LH_2018.sigma  = 3.292e-05
Tprime_tAq_2200_MH75_LH_2018.year = 2018
Tprime_tAq_2200_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH100_LH_2018")
Tprime_tAq_2200_MH100_LH_2018.sigma  = 4.427e-05
Tprime_tAq_2200_MH100_LH_2018.year = 2018
Tprime_tAq_2200_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH125_LH_2018")
Tprime_tAq_2200_MH125_LH_2018.sigma  = 5.548e-05
Tprime_tAq_2200_MH125_LH_2018.year = 2018
Tprime_tAq_2200_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH150_LH_2018")
Tprime_tAq_2200_MH150_LH_2018.sigma  = 6.656e-05
Tprime_tAq_2200_MH150_LH_2018.year = 2018
Tprime_tAq_2200_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH175_LH_2018")
Tprime_tAq_2200_MH175_LH_2018.sigma  = 7.751e-05
Tprime_tAq_2200_MH175_LH_2018.year = 2018
Tprime_tAq_2200_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH200_LH_2018")
Tprime_tAq_2200_MH200_LH_2018.sigma  = 8.831e-05
Tprime_tAq_2200_MH200_LH_2018.year = 2018
Tprime_tAq_2200_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH250_LH_2018")
Tprime_tAq_2200_MH250_LH_2018.sigma  = 0.0001095
Tprime_tAq_2200_MH250_LH_2018.year = 2018
Tprime_tAq_2200_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH350_LH_2018")
Tprime_tAq_2200_MH350_LH_2018.sigma  = 0.0001496
Tprime_tAq_2200_MH350_LH_2018.year = 2018
Tprime_tAq_2200_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH450_LH_2018")
Tprime_tAq_2200_MH450_LH_2018.sigma  = 0.0001858
Tprime_tAq_2200_MH450_LH_2018.year = 2018
Tprime_tAq_2200_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2200_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_MH500_LH_2018")
Tprime_tAq_2200_MH500_LH_2018.sigma  = 0.0002023
Tprime_tAq_2200_MH500_LH_2018.year = 2018
Tprime_tAq_2200_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2200_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH25_LH_2018")
Tprime_tAq_2300_MH25_LH_2018.sigma  = 7.415e-06
Tprime_tAq_2300_MH25_LH_2018.year = 2018
Tprime_tAq_2300_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH50_LH_2018")
Tprime_tAq_2300_MH50_LH_2018.sigma  = 1.765e-05
Tprime_tAq_2300_MH50_LH_2018.year = 2018
Tprime_tAq_2300_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH75_LH_2018")
Tprime_tAq_2300_MH75_LH_2018.sigma  = 2.726e-05
Tprime_tAq_2300_MH75_LH_2018.year = 2018
Tprime_tAq_2300_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH100_LH_2018")
Tprime_tAq_2300_MH100_LH_2018.sigma  = 3.666e-05
Tprime_tAq_2300_MH100_LH_2018.year = 2018
Tprime_tAq_2300_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH125_LH_2018")
Tprime_tAq_2300_MH125_LH_2018.sigma  = 4.595e-05
Tprime_tAq_2300_MH125_LH_2018.year = 2018
Tprime_tAq_2300_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH150_LH_2018")
Tprime_tAq_2300_MH150_LH_2018.sigma  = 5.514e-05
Tprime_tAq_2300_MH150_LH_2018.year = 2018
Tprime_tAq_2300_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH175_LH_2018")
Tprime_tAq_2300_MH175_LH_2018.sigma  = 6.424e-05
Tprime_tAq_2300_MH175_LH_2018.year = 2018
Tprime_tAq_2300_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH200_LH_2018")
Tprime_tAq_2300_MH200_LH_2018.sigma  = 7.323e-05
Tprime_tAq_2300_MH200_LH_2018.year = 2018
Tprime_tAq_2300_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH250_LH_2018")
Tprime_tAq_2300_MH250_LH_2018.sigma  = 9.084e-05
Tprime_tAq_2300_MH250_LH_2018.year = 2018
Tprime_tAq_2300_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH350_LH_2018")
Tprime_tAq_2300_MH350_LH_2018.sigma  = 0.0001244
Tprime_tAq_2300_MH350_LH_2018.year = 2018
Tprime_tAq_2300_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH450_LH_2018")
Tprime_tAq_2300_MH450_LH_2018.sigma  = 0.0001551
Tprime_tAq_2300_MH450_LH_2018.year = 2018
Tprime_tAq_2300_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2300_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_MH500_LH_2018")
Tprime_tAq_2300_MH500_LH_2018.sigma  = 0.0001691
Tprime_tAq_2300_MH500_LH_2018.year = 2018
Tprime_tAq_2300_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2300_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH25_LH_2018")
Tprime_tAq_2400_MH25_LH_2018.sigma  = 6.132e-06
Tprime_tAq_2400_MH25_LH_2018.year = 2018
Tprime_tAq_2400_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH50_LH_2018")
Tprime_tAq_2400_MH50_LH_2018.sigma  = 1.461e-05
Tprime_tAq_2400_MH50_LH_2018.year = 2018
Tprime_tAq_2400_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH75_LH_2018")
Tprime_tAq_2400_MH75_LH_2018.sigma  = 2.256e-05
Tprime_tAq_2400_MH75_LH_2018.year = 2018
Tprime_tAq_2400_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH100_LH_2018")
Tprime_tAq_2400_MH100_LH_2018.sigma  = 3.035e-05
Tprime_tAq_2400_MH100_LH_2018.year = 2018
Tprime_tAq_2400_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH125_LH_2018")
Tprime_tAq_2400_MH125_LH_2018.sigma  = 3.804e-05
Tprime_tAq_2400_MH125_LH_2018.year = 2018
Tprime_tAq_2400_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH150_LH_2018")
Tprime_tAq_2400_MH150_LH_2018.sigma  = 4.566e-05
Tprime_tAq_2400_MH150_LH_2018.year = 2018
Tprime_tAq_2400_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH175_LH_2018")
Tprime_tAq_2400_MH175_LH_2018.sigma  = 5.321e-05
Tprime_tAq_2400_MH175_LH_2018.year = 2018
Tprime_tAq_2400_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH200_LH_2018")
Tprime_tAq_2400_MH200_LH_2018.sigma  = 6.069e-05
Tprime_tAq_2400_MH200_LH_2018.year = 2018
Tprime_tAq_2400_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH250_LH_2018")
Tprime_tAq_2400_MH250_LH_2018.sigma  = 7.535e-05
Tprime_tAq_2400_MH250_LH_2018.year = 2018
Tprime_tAq_2400_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH350_LH_2018")
Tprime_tAq_2400_MH350_LH_2018.sigma  = 0.0001034
Tprime_tAq_2400_MH350_LH_2018.year = 2018
Tprime_tAq_2400_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH450_LH_2018")
Tprime_tAq_2400_MH450_LH_2018.sigma  = 0.0001291
Tprime_tAq_2400_MH450_LH_2018.year = 2018
Tprime_tAq_2400_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2400_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_MH500_LH_2018")
Tprime_tAq_2400_MH500_LH_2018.sigma  = 0.0001411
Tprime_tAq_2400_MH500_LH_2018.year = 2018
Tprime_tAq_2400_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2400_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH25_LH_2018")
Tprime_tAq_2500_MH25_LH_2018.sigma  = 5.095e-06
Tprime_tAq_2500_MH25_LH_2018.year = 2018
Tprime_tAq_2500_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH50_LH_2018")
Tprime_tAq_2500_MH50_LH_2018.sigma  = 1.213e-05
Tprime_tAq_2500_MH50_LH_2018.year = 2018
Tprime_tAq_2500_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH75_LH_2018")
Tprime_tAq_2500_MH75_LH_2018.sigma  = 1.873e-05
Tprime_tAq_2500_MH75_LH_2018.year = 2018
Tprime_tAq_2500_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH100_LH_2018")
Tprime_tAq_2500_MH100_LH_2018.sigma  = 2.52e-05
Tprime_tAq_2500_MH100_LH_2018.year = 2018
Tprime_tAq_2500_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH125_LH_2018")
Tprime_tAq_2500_MH125_LH_2018.sigma  = 3.16e-05
Tprime_tAq_2500_MH125_LH_2018.year = 2018
Tprime_tAq_2500_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH150_LH_2018")
Tprime_tAq_2500_MH150_LH_2018.sigma  = 3.787e-05
Tprime_tAq_2500_MH150_LH_2018.year = 2018
Tprime_tAq_2500_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH175_LH_2018")
Tprime_tAq_2500_MH175_LH_2018.sigma  = 4.414e-05
Tprime_tAq_2500_MH175_LH_2018.year = 2018
Tprime_tAq_2500_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH200_LH_2018")
Tprime_tAq_2500_MH200_LH_2018.sigma  = 5.034e-05
Tprime_tAq_2500_MH200_LH_2018.year = 2018
Tprime_tAq_2500_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH250_LH_2018")
Tprime_tAq_2500_MH250_LH_2018.sigma  = 6.248e-05
Tprime_tAq_2500_MH250_LH_2018.year = 2018
Tprime_tAq_2500_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH350_LH_2018")
Tprime_tAq_2500_MH350_LH_2018.sigma  = 8.587e-05
Tprime_tAq_2500_MH350_LH_2018.year = 2018
Tprime_tAq_2500_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH450_LH_2018")
Tprime_tAq_2500_MH450_LH_2018.sigma  = 0.000108
Tprime_tAq_2500_MH450_LH_2018.year = 2018
Tprime_tAq_2500_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2500_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_MH500_LH_2018")
Tprime_tAq_2500_MH500_LH_2018.sigma  = 0.000118
Tprime_tAq_2500_MH500_LH_2018.year = 2018
Tprime_tAq_2500_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2500_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH25_LH_2018")
Tprime_tAq_2600_MH25_LH_2018.sigma  = 4.123e-06
Tprime_tAq_2600_MH25_LH_2018.year = 2018
Tprime_tAq_2600_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH50_LH_2018")
Tprime_tAq_2600_MH50_LH_2018.sigma  = 9.817e-06
Tprime_tAq_2600_MH50_LH_2018.year = 2018
Tprime_tAq_2600_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH75_LH_2018")
Tprime_tAq_2600_MH75_LH_2018.sigma  = 1.517e-05
Tprime_tAq_2600_MH75_LH_2018.year = 2018
Tprime_tAq_2600_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH100_LH_2018")
Tprime_tAq_2600_MH100_LH_2018.sigma  = 2.041e-05
Tprime_tAq_2600_MH100_LH_2018.year = 2018
Tprime_tAq_2600_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH125_LH_2018")
Tprime_tAq_2600_MH125_LH_2018.sigma  = 2.559e-05
Tprime_tAq_2600_MH125_LH_2018.year = 2018
Tprime_tAq_2600_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH150_LH_2018")
Tprime_tAq_2600_MH150_LH_2018.sigma  = 3.073e-05
Tprime_tAq_2600_MH150_LH_2018.year = 2018
Tprime_tAq_2600_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH175_LH_2018")
Tprime_tAq_2600_MH175_LH_2018.sigma  = 3.582e-05
Tprime_tAq_2600_MH175_LH_2018.year = 2018
Tprime_tAq_2600_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH200_LH_2018")
Tprime_tAq_2600_MH200_LH_2018.sigma  = 4.086e-05
Tprime_tAq_2600_MH200_LH_2018.year = 2018
Tprime_tAq_2600_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH250_LH_2018")
Tprime_tAq_2600_MH250_LH_2018.sigma  = 5.08e-05
Tprime_tAq_2600_MH250_LH_2018.year = 2018
Tprime_tAq_2600_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH350_LH_2018")
Tprime_tAq_2600_MH350_LH_2018.sigma  = 6.99e-05
Tprime_tAq_2600_MH350_LH_2018.year = 2018
Tprime_tAq_2600_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH450_LH_2018")
Tprime_tAq_2600_MH450_LH_2018.sigma  = 8.775e-05
Tprime_tAq_2600_MH450_LH_2018.year = 2018
Tprime_tAq_2600_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2600_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_MH500_LH_2018")
Tprime_tAq_2600_MH500_LH_2018.sigma  = 9.599e-05
Tprime_tAq_2600_MH500_LH_2018.year = 2018
Tprime_tAq_2600_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2600_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH25_LH_2018")
Tprime_tAq_2700_MH25_LH_2018.sigma  = 3.433e-06
Tprime_tAq_2700_MH25_LH_2018.year = 2018
Tprime_tAq_2700_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH50_LH_2018")
Tprime_tAq_2700_MH50_LH_2018.sigma  = 8.187e-06
Tprime_tAq_2700_MH50_LH_2018.year = 2018
Tprime_tAq_2700_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH75_LH_2018")
Tprime_tAq_2700_MH75_LH_2018.sigma  = 1.265e-05
Tprime_tAq_2700_MH75_LH_2018.year = 2018
Tprime_tAq_2700_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH100_LH_2018")
Tprime_tAq_2700_MH100_LH_2018.sigma  = 1.702e-05
Tprime_tAq_2700_MH100_LH_2018.year = 2018
Tprime_tAq_2700_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH125_LH_2018")
Tprime_tAq_2700_MH125_LH_2018.sigma  = 2.133e-05
Tprime_tAq_2700_MH125_LH_2018.year = 2018
Tprime_tAq_2700_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH150_LH_2018")
Tprime_tAq_2700_MH150_LH_2018.sigma  = 2.558e-05
Tprime_tAq_2700_MH150_LH_2018.year = 2018
Tprime_tAq_2700_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH175_LH_2018")
Tprime_tAq_2700_MH175_LH_2018.sigma  = 2.982e-05
Tprime_tAq_2700_MH175_LH_2018.year = 2018
Tprime_tAq_2700_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH200_LH_2018")
Tprime_tAq_2700_MH200_LH_2018.sigma  = 3.403e-05
Tprime_tAq_2700_MH200_LH_2018.year = 2018
Tprime_tAq_2700_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH250_LH_2018")
Tprime_tAq_2700_MH250_LH_2018.sigma  = 4.232e-05
Tprime_tAq_2700_MH250_LH_2018.year = 2018
Tprime_tAq_2700_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH350_LH_2018")
Tprime_tAq_2700_MH350_LH_2018.sigma  = 5.833e-05
Tprime_tAq_2700_MH350_LH_2018.year = 2018
Tprime_tAq_2700_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH450_LH_2018")
Tprime_tAq_2700_MH450_LH_2018.sigma  = 7.334e-05
Tprime_tAq_2700_MH450_LH_2018.year = 2018
Tprime_tAq_2700_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2700_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_MH500_LH_2018")
Tprime_tAq_2700_MH500_LH_2018.sigma  = 8.036e-05
Tprime_tAq_2700_MH500_LH_2018.year = 2018
Tprime_tAq_2700_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2700_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH25_LH_2018")
Tprime_tAq_2800_MH25_LH_2018.sigma  = 2.848e-06
Tprime_tAq_2800_MH25_LH_2018.year = 2018
Tprime_tAq_2800_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH50_LH_2018")
Tprime_tAq_2800_MH50_LH_2018.sigma  = 6.834e-06
Tprime_tAq_2800_MH50_LH_2018.year = 2018
Tprime_tAq_2800_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH75_LH_2018")
Tprime_tAq_2800_MH75_LH_2018.sigma  = 1.057e-05
Tprime_tAq_2800_MH75_LH_2018.year = 2018
Tprime_tAq_2800_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH100_LH_2018")
Tprime_tAq_2800_MH100_LH_2018.sigma  = 1.411e-05
Tprime_tAq_2800_MH100_LH_2018.year = 2018
Tprime_tAq_2800_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH125_LH_2018")
Tprime_tAq_2800_MH125_LH_2018.sigma  = 1.769e-05
Tprime_tAq_2800_MH125_LH_2018.year = 2018
Tprime_tAq_2800_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH150_LH_2018")
Tprime_tAq_2800_MH150_LH_2018.sigma  = 2.125e-05
Tprime_tAq_2800_MH150_LH_2018.year = 2018
Tprime_tAq_2800_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH175_LH_2018")
Tprime_tAq_2800_MH175_LH_2018.sigma  = 2.477e-05
Tprime_tAq_2800_MH175_LH_2018.year = 2018
Tprime_tAq_2800_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH200_LH_2018")
Tprime_tAq_2800_MH200_LH_2018.sigma  = 2.827e-05
Tprime_tAq_2800_MH200_LH_2018.year = 2018
Tprime_tAq_2800_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH250_LH_2018")
Tprime_tAq_2800_MH250_LH_2018.sigma  = 3.518e-05
Tprime_tAq_2800_MH250_LH_2018.year = 2018
Tprime_tAq_2800_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH350_LH_2018")
Tprime_tAq_2800_MH350_LH_2018.sigma  = 4.855e-05
Tprime_tAq_2800_MH350_LH_2018.year = 2018
Tprime_tAq_2800_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH450_LH_2018")
Tprime_tAq_2800_MH450_LH_2018.sigma  = 6.108e-05
Tprime_tAq_2800_MH450_LH_2018.year = 2018
Tprime_tAq_2800_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2800_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_MH500_LH_2018")
Tprime_tAq_2800_MH500_LH_2018.sigma  = 6.7e-05
Tprime_tAq_2800_MH500_LH_2018.year = 2018
Tprime_tAq_2800_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2800_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH25_LH_2018")
Tprime_tAq_2900_MH25_LH_2018.sigma  = 2.356e-06
Tprime_tAq_2900_MH25_LH_2018.year = 2018
Tprime_tAq_2900_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH50_LH_2018")
Tprime_tAq_2900_MH50_LH_2018.sigma  = 5.609e-06
Tprime_tAq_2900_MH50_LH_2018.year = 2018
Tprime_tAq_2900_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH75_LH_2018")
Tprime_tAq_2900_MH75_LH_2018.sigma  = 8.666e-06
Tprime_tAq_2900_MH75_LH_2018.year = 2018
Tprime_tAq_2900_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH100_LH_2018")
Tprime_tAq_2900_MH100_LH_2018.sigma  = 1.166e-05
Tprime_tAq_2900_MH100_LH_2018.year = 2018
Tprime_tAq_2900_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH125_LH_2018")
Tprime_tAq_2900_MH125_LH_2018.sigma  = 1.463e-05
Tprime_tAq_2900_MH125_LH_2018.year = 2018
Tprime_tAq_2900_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH150_LH_2018")
Tprime_tAq_2900_MH150_LH_2018.sigma  = 1.757e-05
Tprime_tAq_2900_MH150_LH_2018.year = 2018
Tprime_tAq_2900_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH175_LH_2018")
Tprime_tAq_2900_MH175_LH_2018.sigma  = 2.052e-05
Tprime_tAq_2900_MH175_LH_2018.year = 2018
Tprime_tAq_2900_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH200_LH_2018")
Tprime_tAq_2900_MH200_LH_2018.sigma  = 2.342e-05
Tprime_tAq_2900_MH200_LH_2018.year = 2018
Tprime_tAq_2900_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH250_LH_2018")
Tprime_tAq_2900_MH250_LH_2018.sigma  = 2.916e-05
Tprime_tAq_2900_MH250_LH_2018.year = 2018
Tprime_tAq_2900_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH350_LH_2018")
Tprime_tAq_2900_MH350_LH_2018.sigma  = 4.025e-05
Tprime_tAq_2900_MH350_LH_2018.year = 2018
Tprime_tAq_2900_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH450_LH_2018")
Tprime_tAq_2900_MH450_LH_2018.sigma  = 5.079e-05
Tprime_tAq_2900_MH450_LH_2018.year = 2018
Tprime_tAq_2900_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_2900_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_MH500_LH_2018")
Tprime_tAq_2900_MH500_LH_2018.sigma  = 5.577e-05
Tprime_tAq_2900_MH500_LH_2018.year = 2018
Tprime_tAq_2900_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT2900_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH25_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH25_LH_2018")
Tprime_tAq_3000_MH25_LH_2018.sigma  = 1.953e-06
Tprime_tAq_3000_MH25_LH_2018.year = 2018
Tprime_tAq_3000_MH25_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH25_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH50_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH50_LH_2018")
Tprime_tAq_3000_MH50_LH_2018.sigma  = 4.645e-06
Tprime_tAq_3000_MH50_LH_2018.year = 2018
Tprime_tAq_3000_MH50_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH50_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH75_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH75_LH_2018")
Tprime_tAq_3000_MH75_LH_2018.sigma  = 7.177e-06
Tprime_tAq_3000_MH75_LH_2018.year = 2018
Tprime_tAq_3000_MH75_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH75_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH100_LH_2018")
Tprime_tAq_3000_MH100_LH_2018.sigma  = 9.661e-06
Tprime_tAq_3000_MH100_LH_2018.year = 2018
Tprime_tAq_3000_MH100_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH100_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH125_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH125_LH_2018")
Tprime_tAq_3000_MH125_LH_2018.sigma  = 1.212e-05
Tprime_tAq_3000_MH125_LH_2018.year = 2018
Tprime_tAq_3000_MH125_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH125_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH150_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH150_LH_2018")
Tprime_tAq_3000_MH150_LH_2018.sigma  = 1.455e-05
Tprime_tAq_3000_MH150_LH_2018.year = 2018
Tprime_tAq_3000_MH150_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH150_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH175_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH175_LH_2018")
Tprime_tAq_3000_MH175_LH_2018.sigma  = 1.697e-05
Tprime_tAq_3000_MH175_LH_2018.year = 2018
Tprime_tAq_3000_MH175_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH175_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH200_LH_2018")
Tprime_tAq_3000_MH200_LH_2018.sigma  = 1.938e-05
Tprime_tAq_3000_MH200_LH_2018.year = 2018
Tprime_tAq_3000_MH200_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH200_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH250_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH250_LH_2018")
Tprime_tAq_3000_MH250_LH_2018.sigma  = 2.413e-05
Tprime_tAq_3000_MH250_LH_2018.year = 2018
Tprime_tAq_3000_MH250_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH250_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH350_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH350_LH_2018")
Tprime_tAq_3000_MH350_LH_2018.sigma  = 3.343e-05
Tprime_tAq_3000_MH350_LH_2018.year = 2018
Tprime_tAq_3000_MH350_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH350_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH450_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH450_LH_2018")
Tprime_tAq_3000_MH450_LH_2018.sigma  = 4.234e-05
Tprime_tAq_3000_MH450_LH_2018.year = 2018
Tprime_tAq_3000_MH450_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH450_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

Tprime_tAq_3000_MH500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_MH500_LH_2018")
Tprime_tAq_3000_MH500_LH_2018.sigma  = 4.652e-05
Tprime_tAq_3000_MH500_LH_2018.year = 2018
Tprime_tAq_3000_MH500_LH_2018.dataset = "/TprimeBToTH_TLep_Hbb_LH_MT3000_MH500_TuneCP5_13TeV-madgraph-pythia8/"+tag_2018+"-v1/NANOAODSIM"

# 2018 bunches of tAq samples by MT mass

Tprime_tAq_600_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.6TeV(0%) LH", "Tprime_tAq_600_LH_2018")
Tprime_tAq_600_LH_2018.year = 2018
Tprime_tAq_600_LH_2018.components = [Tprime_tAq_600_MH25_LH_2018, Tprime_tAq_600_MH50_LH_2018, Tprime_tAq_600_MH75_LH_2018, Tprime_tAq_600_MH100_LH_2018, Tprime_tAq_600_MH125_LH_2018, Tprime_tAq_600_MH150_LH_2018, Tprime_tAq_600_MH175_LH_2018, Tprime_tAq_600_MH200_LH_2018, Tprime_tAq_600_MH250_LH_2018, Tprime_tAq_600_MH350_LH_2018, Tprime_tAq_600_MH450_LH_2018, Tprime_tAq_600_MH500_LH_2018]

Tprime_tAq_700_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.7TeV(0%) LH", "Tprime_tAq_700_LH_2018")
Tprime_tAq_700_LH_2018.year = 2018
Tprime_tAq_700_LH_2018.components = [Tprime_tAq_700_MH25_LH_2018, Tprime_tAq_700_MH50_LH_2018, Tprime_tAq_700_MH75_LH_2018, Tprime_tAq_700_MH100_LH_2018, Tprime_tAq_700_MH125_LH_2018, Tprime_tAq_700_MH150_LH_2018, Tprime_tAq_700_MH175_LH_2018, Tprime_tAq_700_MH200_LH_2018, Tprime_tAq_700_MH250_LH_2018, Tprime_tAq_700_MH350_LH_2018, Tprime_tAq_700_MH450_LH_2018, Tprime_tAq_700_MH500_LH_2018]

Tprime_tAq_800_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.8TeV(0%) LH", "Tprime_tAq_800_LH_2018")
Tprime_tAq_800_LH_2018.year = 2018
Tprime_tAq_800_LH_2018.components = [Tprime_tAq_800_MH25_LH_2018, Tprime_tAq_800_MH50_LH_2018, Tprime_tAq_800_MH75_LH_2018, Tprime_tAq_800_MH100_LH_2018, Tprime_tAq_800_MH125_LH_2018, Tprime_tAq_800_MH150_LH_2018, Tprime_tAq_800_MH175_LH_2018, Tprime_tAq_800_MH200_LH_2018, Tprime_tAq_800_MH250_LH_2018, Tprime_tAq_800_MH350_LH_2018, Tprime_tAq_800_MH450_LH_2018, Tprime_tAq_800_MH500_LH_2018]

Tprime_tAq_900_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 0.9TeV(0%) LH", "Tprime_tAq_900_LH_2018")
Tprime_tAq_900_LH_2018.year = 2018
Tprime_tAq_900_LH_2018.components = [Tprime_tAq_900_MH25_LH_2018, Tprime_tAq_900_MH50_LH_2018, Tprime_tAq_900_MH75_LH_2018, Tprime_tAq_900_MH100_LH_2018, Tprime_tAq_900_MH125_LH_2018, Tprime_tAq_900_MH150_LH_2018, Tprime_tAq_900_MH175_LH_2018, Tprime_tAq_900_MH200_LH_2018, Tprime_tAq_900_MH250_LH_2018, Tprime_tAq_900_MH350_LH_2018, Tprime_tAq_900_MH450_LH_2018, Tprime_tAq_900_MH500_LH_2018]

Tprime_tAq_1000_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.0TeV(0%) LH", "Tprime_tAq_1000_LH_2018")
Tprime_tAq_1000_LH_2018.year = 2018
Tprime_tAq_1000_LH_2018.components = [Tprime_tAq_1000_MH25_LH_2018, Tprime_tAq_1000_MH50_LH_2018, Tprime_tAq_1000_MH75_LH_2018, Tprime_tAq_1000_MH100_LH_2018, Tprime_tAq_1000_MH125_LH_2018, Tprime_tAq_1000_MH150_LH_2018, Tprime_tAq_1000_MH175_LH_2018, Tprime_tAq_1000_MH200_LH_2018, Tprime_tAq_1000_MH250_LH_2018, Tprime_tAq_1000_MH350_LH_2018, Tprime_tAq_1000_MH450_LH_2018, Tprime_tAq_1000_MH500_LH_2018]

Tprime_tAq_1100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.1TeV(0%) LH", "Tprime_tAq_1100_LH_2018")
Tprime_tAq_1100_LH_2018.year = 2018
Tprime_tAq_1100_LH_2018.components = [Tprime_tAq_1100_MH25_LH_2018, Tprime_tAq_1100_MH50_LH_2018, Tprime_tAq_1100_MH75_LH_2018, Tprime_tAq_1100_MH100_LH_2018, Tprime_tAq_1100_MH125_LH_2018, Tprime_tAq_1100_MH150_LH_2018, Tprime_tAq_1100_MH175_LH_2018, Tprime_tAq_1100_MH200_LH_2018, Tprime_tAq_1100_MH250_LH_2018, Tprime_tAq_1100_MH350_LH_2018, Tprime_tAq_1100_MH450_LH_2018, Tprime_tAq_1100_MH500_LH_2018]

Tprime_tAq_1200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.2TeV(0%) LH", "Tprime_tAq_1200_LH_2018")
Tprime_tAq_1200_LH_2018.year = 2018
Tprime_tAq_1200_LH_2018.components = [Tprime_tAq_1200_MH25_LH_2018, Tprime_tAq_1200_MH50_LH_2018, Tprime_tAq_1200_MH75_LH_2018, Tprime_tAq_1200_MH100_LH_2018, Tprime_tAq_1200_MH125_LH_2018, Tprime_tAq_1200_MH150_LH_2018, Tprime_tAq_1200_MH175_LH_2018, Tprime_tAq_1200_MH200_LH_2018, Tprime_tAq_1200_MH250_LH_2018, Tprime_tAq_1200_MH350_LH_2018, Tprime_tAq_1200_MH450_LH_2018, Tprime_tAq_1200_MH500_LH_2018]

Tprime_tAq_1300_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.3TeV(0%) LH", "Tprime_tAq_1300_LH_2018")
Tprime_tAq_1300_LH_2018.year = 2018
Tprime_tAq_1300_LH_2018.components = [Tprime_tAq_1300_MH25_LH_2018, Tprime_tAq_1300_MH50_LH_2018, Tprime_tAq_1300_MH75_LH_2018, Tprime_tAq_1300_MH100_LH_2018, Tprime_tAq_1300_MH125_LH_2018, Tprime_tAq_1300_MH150_LH_2018, Tprime_tAq_1300_MH175_LH_2018, Tprime_tAq_1300_MH200_LH_2018, Tprime_tAq_1300_MH250_LH_2018, Tprime_tAq_1300_MH350_LH_2018, Tprime_tAq_1300_MH450_LH_2018, Tprime_tAq_1300_MH500_LH_2018]

Tprime_tAq_1400_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.4TeV(0%) LH", "Tprime_tAq_1400_LH_2018")
Tprime_tAq_1400_LH_2018.year = 2018
Tprime_tAq_1400_LH_2018.components = [Tprime_tAq_1400_MH25_LH_2018, Tprime_tAq_1400_MH50_LH_2018, Tprime_tAq_1400_MH75_LH_2018, Tprime_tAq_1400_MH100_LH_2018, Tprime_tAq_1400_MH125_LH_2018, Tprime_tAq_1400_MH150_LH_2018, Tprime_tAq_1400_MH175_LH_2018, Tprime_tAq_1400_MH200_LH_2018, Tprime_tAq_1400_MH250_LH_2018, Tprime_tAq_1400_MH350_LH_2018, Tprime_tAq_1400_MH450_LH_2018, Tprime_tAq_1400_MH500_LH_2018]

Tprime_tAq_1500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.5TeV(0%) LH", "Tprime_tAq_1500_LH_2018")
Tprime_tAq_1500_LH_2018.year = 2018
Tprime_tAq_1500_LH_2018.components = [Tprime_tAq_1500_MH25_LH_2018, Tprime_tAq_1500_MH50_LH_2018, Tprime_tAq_1500_MH75_LH_2018, Tprime_tAq_1500_MH100_LH_2018, Tprime_tAq_1500_MH125_LH_2018, Tprime_tAq_1500_MH150_LH_2018, Tprime_tAq_1500_MH175_LH_2018, Tprime_tAq_1500_MH200_LH_2018, Tprime_tAq_1500_MH250_LH_2018, Tprime_tAq_1500_MH350_LH_2018, Tprime_tAq_1500_MH450_LH_2018, Tprime_tAq_1500_MH500_LH_2018]

Tprime_tAq_1600_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.6TeV(0%) LH", "Tprime_tAq_1600_LH_2018")
Tprime_tAq_1600_LH_2018.year = 2018
Tprime_tAq_1600_LH_2018.components = [Tprime_tAq_1600_MH25_LH_2018, Tprime_tAq_1600_MH50_LH_2018, Tprime_tAq_1600_MH75_LH_2018, Tprime_tAq_1600_MH100_LH_2018, Tprime_tAq_1600_MH125_LH_2018, Tprime_tAq_1600_MH150_LH_2018, Tprime_tAq_1600_MH175_LH_2018, Tprime_tAq_1600_MH200_LH_2018, Tprime_tAq_1600_MH250_LH_2018, Tprime_tAq_1600_MH350_LH_2018, Tprime_tAq_1600_MH450_LH_2018, Tprime_tAq_1600_MH500_LH_2018]

Tprime_tAq_1700_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.7TeV(0%) LH", "Tprime_tAq_1700_LH_2018")
Tprime_tAq_1700_LH_2018.year = 2018
Tprime_tAq_1700_LH_2018.components = [Tprime_tAq_1700_MH25_LH_2018, Tprime_tAq_1700_MH50_LH_2018, Tprime_tAq_1700_MH75_LH_2018, Tprime_tAq_1700_MH100_LH_2018, Tprime_tAq_1700_MH125_LH_2018, Tprime_tAq_1700_MH150_LH_2018, Tprime_tAq_1700_MH175_LH_2018, Tprime_tAq_1700_MH200_LH_2018, Tprime_tAq_1700_MH250_LH_2018, Tprime_tAq_1700_MH350_LH_2018, Tprime_tAq_1700_MH450_LH_2018, Tprime_tAq_1700_MH500_LH_2018]

Tprime_tAq_1800_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.8TeV(0%) LH", "Tprime_tAq_1800_LH_2018")
Tprime_tAq_1800_LH_2018.year = 2018
Tprime_tAq_1800_LH_2018.components = [Tprime_tAq_1800_MH25_LH_2018, Tprime_tAq_1800_MH50_LH_2018, Tprime_tAq_1800_MH75_LH_2018, Tprime_tAq_1800_MH100_LH_2018, Tprime_tAq_1800_MH125_LH_2018, Tprime_tAq_1800_MH150_LH_2018, Tprime_tAq_1800_MH175_LH_2018, Tprime_tAq_1800_MH200_LH_2018, Tprime_tAq_1800_MH250_LH_2018, Tprime_tAq_1800_MH350_LH_2018, Tprime_tAq_1800_MH450_LH_2018, Tprime_tAq_1800_MH500_LH_2018]

Tprime_tAq_1900_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 1.9TeV(0%) LH", "Tprime_tAq_1900_LH_2018")
Tprime_tAq_1900_LH_2018.year = 2018
Tprime_tAq_1900_LH_2018.components = [Tprime_tAq_1900_MH25_LH_2018, Tprime_tAq_1900_MH50_LH_2018, Tprime_tAq_1900_MH75_LH_2018, Tprime_tAq_1900_MH100_LH_2018, Tprime_tAq_1900_MH125_LH_2018, Tprime_tAq_1900_MH150_LH_2018, Tprime_tAq_1900_MH175_LH_2018, Tprime_tAq_1900_MH200_LH_2018, Tprime_tAq_1900_MH250_LH_2018, Tprime_tAq_1900_MH350_LH_2018, Tprime_tAq_1900_MH450_LH_2018, Tprime_tAq_1900_MH500_LH_2018]

Tprime_tAq_2000_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.0TeV(0%) LH", "Tprime_tAq_2000_LH_2018")
Tprime_tAq_2000_LH_2018.year = 2018
Tprime_tAq_2000_LH_2018.components = [Tprime_tAq_2000_MH25_LH_2018, Tprime_tAq_2000_MH50_LH_2018, Tprime_tAq_2000_MH75_LH_2018, Tprime_tAq_2000_MH100_LH_2018, Tprime_tAq_2000_MH125_LH_2018, Tprime_tAq_2000_MH150_LH_2018, Tprime_tAq_2000_MH175_LH_2018, Tprime_tAq_2000_MH200_LH_2018, Tprime_tAq_2000_MH250_LH_2018, Tprime_tAq_2000_MH350_LH_2018, Tprime_tAq_2000_MH450_LH_2018, Tprime_tAq_2000_MH500_LH_2018]

Tprime_tAq_2100_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.1TeV(0%) LH", "Tprime_tAq_2100_LH_2018")
Tprime_tAq_2100_LH_2018.year = 2018
Tprime_tAq_2100_LH_2018.components = [Tprime_tAq_2100_MH25_LH_2018, Tprime_tAq_2100_MH50_LH_2018, Tprime_tAq_2100_MH75_LH_2018, Tprime_tAq_2100_MH100_LH_2018, Tprime_tAq_2100_MH125_LH_2018, Tprime_tAq_2100_MH150_LH_2018, Tprime_tAq_2100_MH175_LH_2018, Tprime_tAq_2100_MH200_LH_2018, Tprime_tAq_2100_MH250_LH_2018, Tprime_tAq_2100_MH350_LH_2018, Tprime_tAq_2100_MH450_LH_2018, Tprime_tAq_2100_MH500_LH_2018]

Tprime_tAq_2200_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.2TeV(0%) LH", "Tprime_tAq_2200_LH_2018")
Tprime_tAq_2200_LH_2018.year = 2018
Tprime_tAq_2200_LH_2018.components = [Tprime_tAq_2200_MH25_LH_2018, Tprime_tAq_2200_MH50_LH_2018, Tprime_tAq_2200_MH75_LH_2018, Tprime_tAq_2200_MH100_LH_2018, Tprime_tAq_2200_MH125_LH_2018, Tprime_tAq_2200_MH150_LH_2018, Tprime_tAq_2200_MH175_LH_2018, Tprime_tAq_2200_MH200_LH_2018, Tprime_tAq_2200_MH250_LH_2018, Tprime_tAq_2200_MH350_LH_2018, Tprime_tAq_2200_MH450_LH_2018, Tprime_tAq_2200_MH500_LH_2018]

Tprime_tAq_2300_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.3TeV(0%) LH", "Tprime_tAq_2300_LH_2018")
Tprime_tAq_2300_LH_2018.year = 2018
Tprime_tAq_2300_LH_2018.components = [Tprime_tAq_2300_MH25_LH_2018, Tprime_tAq_2300_MH50_LH_2018, Tprime_tAq_2300_MH75_LH_2018, Tprime_tAq_2300_MH100_LH_2018, Tprime_tAq_2300_MH125_LH_2018, Tprime_tAq_2300_MH150_LH_2018, Tprime_tAq_2300_MH175_LH_2018, Tprime_tAq_2300_MH200_LH_2018, Tprime_tAq_2300_MH250_LH_2018, Tprime_tAq_2300_MH350_LH_2018, Tprime_tAq_2300_MH450_LH_2018, Tprime_tAq_2300_MH500_LH_2018]

Tprime_tAq_2400_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.4TeV(0%) LH", "Tprime_tAq_2400_LH_2018")
Tprime_tAq_2400_LH_2018.year = 2018
Tprime_tAq_2400_LH_2018.components = [Tprime_tAq_2400_MH25_LH_2018, Tprime_tAq_2400_MH50_LH_2018, Tprime_tAq_2400_MH75_LH_2018, Tprime_tAq_2400_MH100_LH_2018, Tprime_tAq_2400_MH125_LH_2018, Tprime_tAq_2400_MH150_LH_2018, Tprime_tAq_2400_MH175_LH_2018, Tprime_tAq_2400_MH200_LH_2018, Tprime_tAq_2400_MH250_LH_2018, Tprime_tAq_2400_MH350_LH_2018, Tprime_tAq_2400_MH450_LH_2018, Tprime_tAq_2400_MH500_LH_2018]

Tprime_tAq_2500_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.5TeV(0%) LH", "Tprime_tAq_2500_LH_2018")
Tprime_tAq_2500_LH_2018.year = 2018
Tprime_tAq_2500_LH_2018.components = [Tprime_tAq_2500_MH25_LH_2018, Tprime_tAq_2500_MH50_LH_2018, Tprime_tAq_2500_MH75_LH_2018, Tprime_tAq_2500_MH100_LH_2018, Tprime_tAq_2500_MH125_LH_2018, Tprime_tAq_2500_MH150_LH_2018, Tprime_tAq_2500_MH175_LH_2018, Tprime_tAq_2500_MH200_LH_2018, Tprime_tAq_2500_MH250_LH_2018, Tprime_tAq_2500_MH350_LH_2018, Tprime_tAq_2500_MH450_LH_2018, Tprime_tAq_2500_MH500_LH_2018]

Tprime_tAq_2600_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.6TeV(0%) LH", "Tprime_tAq_2600_LH_2018")
Tprime_tAq_2600_LH_2018.year = 2018
Tprime_tAq_2600_LH_2018.components = [Tprime_tAq_2600_MH25_LH_2018, Tprime_tAq_2600_MH50_LH_2018, Tprime_tAq_2600_MH75_LH_2018, Tprime_tAq_2600_MH100_LH_2018, Tprime_tAq_2600_MH125_LH_2018, Tprime_tAq_2600_MH150_LH_2018, Tprime_tAq_2600_MH175_LH_2018, Tprime_tAq_2600_MH200_LH_2018, Tprime_tAq_2600_MH250_LH_2018, Tprime_tAq_2600_MH350_LH_2018, Tprime_tAq_2600_MH450_LH_2018, Tprime_tAq_2600_MH500_LH_2018]

Tprime_tAq_2700_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.7TeV(0%) LH", "Tprime_tAq_2700_LH_2018")
Tprime_tAq_2700_LH_2018.year = 2018
Tprime_tAq_2700_LH_2018.components = [Tprime_tAq_2700_MH25_LH_2018, Tprime_tAq_2700_MH50_LH_2018, Tprime_tAq_2700_MH75_LH_2018, Tprime_tAq_2700_MH100_LH_2018, Tprime_tAq_2700_MH125_LH_2018, Tprime_tAq_2700_MH150_LH_2018, Tprime_tAq_2700_MH175_LH_2018, Tprime_tAq_2700_MH200_LH_2018, Tprime_tAq_2700_MH250_LH_2018, Tprime_tAq_2700_MH350_LH_2018, Tprime_tAq_2700_MH450_LH_2018, Tprime_tAq_2700_MH500_LH_2018]

Tprime_tAq_2800_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.8TeV(0%) LH", "Tprime_tAq_2800_LH_2018")
Tprime_tAq_2800_LH_2018.year = 2018
Tprime_tAq_2800_LH_2018.components = [Tprime_tAq_2800_MH25_LH_2018, Tprime_tAq_2800_MH50_LH_2018, Tprime_tAq_2800_MH75_LH_2018, Tprime_tAq_2800_MH100_LH_2018, Tprime_tAq_2800_MH125_LH_2018, Tprime_tAq_2800_MH150_LH_2018, Tprime_tAq_2800_MH175_LH_2018, Tprime_tAq_2800_MH200_LH_2018, Tprime_tAq_2800_MH250_LH_2018, Tprime_tAq_2800_MH350_LH_2018, Tprime_tAq_2800_MH450_LH_2018, Tprime_tAq_2800_MH500_LH_2018]

Tprime_tAq_2900_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 2.9TeV(0%) LH", "Tprime_tAq_2900_LH_2018")
Tprime_tAq_2900_LH_2018.year = 2018
Tprime_tAq_2900_LH_2018.components = [Tprime_tAq_2900_MH25_LH_2018, Tprime_tAq_2900_MH50_LH_2018, Tprime_tAq_2900_MH75_LH_2018, Tprime_tAq_2900_MH100_LH_2018, Tprime_tAq_2900_MH125_LH_2018, Tprime_tAq_2900_MH150_LH_2018, Tprime_tAq_2900_MH175_LH_2018, Tprime_tAq_2900_MH200_LH_2018, Tprime_tAq_2900_MH250_LH_2018, Tprime_tAq_2900_MH350_LH_2018, Tprime_tAq_2900_MH450_LH_2018, Tprime_tAq_2900_MH500_LH_2018]

Tprime_tAq_3000_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' 3.0TeV(0%) LH", "Tprime_tAq_3000_LH_2018")
Tprime_tAq_3000_LH_2018.year = 2018
Tprime_tAq_3000_LH_2018.components = [Tprime_tAq_3000_MH25_LH_2018, Tprime_tAq_3000_MH50_LH_2018, Tprime_tAq_3000_MH75_LH_2018, Tprime_tAq_3000_MH100_LH_2018, Tprime_tAq_3000_MH125_LH_2018, Tprime_tAq_3000_MH150_LH_2018, Tprime_tAq_3000_MH175_LH_2018, Tprime_tAq_3000_MH200_LH_2018, Tprime_tAq_3000_MH250_LH_2018, Tprime_tAq_3000_MH350_LH_2018, Tprime_tAq_3000_MH450_LH_2018, Tprime_tAq_3000_MH500_LH_2018]


#Tprime_tAq_LH_2018 = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_tAq_LH_2018")
#Tprime_tAq_LH_2018.year = 2018






sample_dict = {
"QCD":QCD, "TT_Mtt":TT_Mtt, "WJets":WJets,"ST":ST,"Tprime_tHq_1800LH":Tprime_tHq_1800LH,
"Tprime_tHq_600LH_2016":Tprime_tHq_600LH_2016,"Tprime_tHq_700LH_2016":Tprime_tHq_700LH_2016,"Tprime_tHq_800LH_2016":Tprime_tHq_800LH_2016,"Tprime_tHq_900LH_2016":Tprime_tHq_900LH_2016,
"Tprime_tHq_1000LH_2016":Tprime_tHq_1000LH_2016,"Tprime_tHq_1100LH_2016":Tprime_tHq_1100LH_2016,"Tprime_tHq_1200LH_2016":Tprime_tHq_1200LH_2016,"Tprime_tHq_1300LH_2016":Tprime_tHq_1300LH_2016,
"Tprime_tHq_1400LH_2016":Tprime_tHq_1400LH_2016,"Tprime_tHq_1500LH_2016":Tprime_tHq_1500LH_2016,"Tprime_tHq_1600LH_2016":Tprime_tHq_1600LH_2016,"Tprime_tHq_1700LH_2016":Tprime_tHq_1700LH_2016,
"Tprime_tHq_1800LH_2016":Tprime_tHq_1800LH_2016,"Tprime_LH_2016":Tprime_LH_2016,
'TT_Mtt700to1000_2016':TT_Mtt700to1000_2016, 'TT_Mtt1000toInf_2016':TT_Mtt1000toInf_2016,"TT_semilep_2016":TT_semilep_2016,"TT_dilep_2016":TT_dilep_2016, "TT_Mtt_2016":TT_Mtt_2016,
'WJets_2016':WJets_2016, 'WJetsHT70to100_2016':WJetsHT70to100_2016, 'WJetsHT100to200_2016':WJetsHT100to200_2016, 'WJetsHT200to400_2016':WJetsHT200to400_2016,'WJetsHT400to600_2016':WJetsHT400to600_2016, 'WJetsHT600to800_2016':WJetsHT600to800_2016, 'WJetsHT800to1200_2016':WJetsHT800to1200_2016, 'WJetsHT1200to2500_2016':WJetsHT1200to2500_2016,'WJetsHT2500toInf_2016':WJetsHT2500toInf_2016,
'QCD_2016':QCD_2016, 'QCDHT_50to100_2016':QCDHT_50to100_2016,'QCDHT_100to200_2016':QCDHT_100to200_2016,'QCDHT_200to300_2016':QCDHT_200to300_2016,'QCDHT_300to500_2016':QCDHT_300to500_2016, 'QCDHT_500to700_2016':QCDHT_500to700_2016, 'QCDHT_700to1000_2016':QCDHT_700to1000_2016,'QCDHT_1000to1500_2016':QCDHT_1000to1500_2016, 'QCDHT_1500to2000_2016':QCDHT_1500to2000_2016, 'QCDHT_2000toInf_2016':QCDHT_2000toInf_2016,
'ST_2016':ST_2016, 'ST_tch_t_2016':ST_tch_t_2016, 'ST_tch_tbar_2016':ST_tch_tbar_2016, 'ST_tW_t_2016':ST_tW_t_2016, 'ST_tW_tbar_2016':ST_tW_tbar_2016, 'ST_sch_2016':ST_sch_2016,

"Tprime_tHq_600LH_2016preVFP":Tprime_tHq_600LH_2016preVFP,"Tprime_tHq_700LH_2016preVFP":Tprime_tHq_700LH_2016preVFP,"Tprime_tHq_800LH_2016preVFP":Tprime_tHq_800LH_2016preVFP,"Tprime_tHq_900LH_2016preVFP":Tprime_tHq_900LH_2016preVFP,
"Tprime_tHq_1000LH_2016preVFP":Tprime_tHq_1000LH_2016preVFP,"Tprime_tHq_1100LH_2016preVFP":Tprime_tHq_1100LH_2016preVFP,"Tprime_tHq_1200LH_2016preVFP":Tprime_tHq_1200LH_2016preVFP,"Tprime_tHq_1300LH_2016preVFP":Tprime_tHq_1300LH_2016preVFP,
"Tprime_tHq_1400LH_2016preVFP":Tprime_tHq_1400LH_2016preVFP,"Tprime_tHq_1500LH_2016preVFP":Tprime_tHq_1500LH_2016preVFP,"Tprime_tHq_1600LH_2016preVFP":Tprime_tHq_1600LH_2016preVFP,"Tprime_tHq_1700LH_2016preVFP":Tprime_tHq_1700LH_2016preVFP,
"Tprime_tHq_1800LH_2016preVFP":Tprime_tHq_1800LH_2016preVFP,"Tprime_LH_2016preVFP":Tprime_LH_2016preVFP,
'TT_Mtt700to1000_2016preVFP':TT_Mtt700to1000_2016preVFP, 'TT_Mtt1000toInf_2016preVFP':TT_Mtt1000toInf_2016preVFP,"TT_semilep_2016preVFP":TT_semilep_2016preVFP,"TT_dilep_2016preVFP":TT_dilep_2016preVFP, "TT_Mtt_2016preVFP":TT_Mtt_2016preVFP,  
'WJets_2016preVFP':WJets_2016preVFP, 'WJetsHT70to100_2016preVFP':WJetsHT70to100_2016preVFP, 'WJetsHT100to200_2016preVFP':WJetsHT100to200_2016preVFP, 'WJetsHT200to400_2016preVFP':WJetsHT200to400_2016preVFP,'WJetsHT400to600_2016preVFP':WJetsHT400to600_2016preVFP, 'WJetsHT600to800_2016preVFP':WJetsHT600to800_2016preVFP, 'WJetsHT800to1200_2016preVFP':WJetsHT800to1200_2016preVFP, 'WJetsHT1200to2500_2016preVFP':WJetsHT1200to2500_2016preVFP,'WJetsHT2500toInf_2016preVFP':WJetsHT2500toInf_2016preVFP,
'QCD_2016preVFP':QCD_2016preVFP, 'QCDHT_50to100_2016preVFP':QCDHT_50to100_2016preVFP,'QCDHT_100to200_2016preVFP':QCDHT_100to200_2016preVFP,'QCDHT_200to300_2016preVFP':QCDHT_200to300_2016preVFP,'QCDHT_300to500_2016preVFP':QCDHT_300to500_2016preVFP, 'QCDHT_500to700_2016preVFP':QCDHT_500to700_2016preVFP, 'QCDHT_700to1000_2016preVFP':QCDHT_700to1000_2016preVFP,'QCDHT_1000to1500_2016preVFP':QCDHT_1000to1500_2016preVFP, 'QCDHT_1500to2000_2016preVFP':QCDHT_1500to2000_2016preVFP, 'QCDHT_2000toInf_2016preVFP':QCDHT_2000toInf_2016preVFP,
'ST_2016preVFP':ST_2016preVFP, 'ST_tch_t_2016preVFP':ST_tch_t_2016preVFP, 'ST_tch_tbar_2016preVFP':ST_tch_tbar_2016preVFP, 'ST_tW_t_2016preVFP':ST_tW_t_2016preVFP, 'ST_tW_tbar_2016preVFP':ST_tW_tbar_2016preVFP, 'ST_sch_2016preVFP':ST_sch_2016preVFP,

"Tprime_tHq_600LH_2016postVFP":Tprime_tHq_600LH_2016postVFP,"Tprime_tHq_700LH_2016postVFP":Tprime_tHq_700LH_2016postVFP,"Tprime_tHq_800LH_2016postVFP":Tprime_tHq_800LH_2016postVFP,"Tprime_tHq_900LH_2016postVFP":Tprime_tHq_900LH_2016postVFP,
"Tprime_tHq_1000LH_2016postVFP":Tprime_tHq_1000LH_2016postVFP,"Tprime_tHq_1100LH_2016postVFP":Tprime_tHq_1100LH_2016postVFP,"Tprime_tHq_1200LH_2016postVFP":Tprime_tHq_1200LH_2016postVFP,"Tprime_tHq_1300LH_2016postVFP":Tprime_tHq_1300LH_2016postVFP,
"Tprime_tHq_1400LH_2016postVFP":Tprime_tHq_1400LH_2016postVFP,"Tprime_tHq_1500LH_2016postVFP":Tprime_tHq_1500LH_2016postVFP,"Tprime_tHq_1600LH_2016postVFP":Tprime_tHq_1600LH_2016postVFP,"Tprime_tHq_1700LH_2016postVFP":Tprime_tHq_1700LH_2016postVFP,
"Tprime_tHq_1800LH_2016postVFP":Tprime_tHq_1800LH_2016postVFP,"Tprime_LH_2016postVFP":Tprime_LH_2016postVFP,
'TT_Mtt700to1000_2016postVFP':TT_Mtt700to1000_2016postVFP, 'TT_Mtt1000toInf_2016postVFP':TT_Mtt1000toInf_2016postVFP,"TT_semilep_2016postVFP":TT_semilep_2016postVFP,"TT_dilep_2016postVFP":TT_dilep_2016postVFP, "TT_Mtt_2016postVFP":TT_Mtt_2016postVFP,
'WJets_2016postVFP':WJets_2016postVFP, 'WJetsHT70to100_2016postVFP':WJetsHT70to100_2016postVFP, 'WJetsHT100to200_2016postVFP':WJetsHT100to200_2016postVFP, 'WJetsHT200to400_2016postVFP':WJetsHT200to400_2016postVFP,'WJetsHT400to600_2016postVFP':WJetsHT400to600_2016postVFP, 'WJetsHT600to800_2016postVFP':WJetsHT600to800_2016postVFP, 'WJetsHT800to1200_2016postVFP':WJetsHT800to1200_2016postVFP, 'WJetsHT1200to2500_2016postVFP':WJetsHT1200to2500_2016postVFP,'WJetsHT2500toInf_2016postVFP':WJetsHT2500toInf_2016postVFP,
'QCD_2016postVFP':QCD_2016postVFP, 'QCDHT_50to100_2016postVFP':QCDHT_50to100_2016postVFP,'QCDHT_100to200_2016postVFP':QCDHT_100to200_2016postVFP,'QCDHT_200to300_2016postVFP':QCDHT_200to300_2016postVFP,'QCDHT_300to500_2016postVFP':QCDHT_300to500_2016postVFP, 'QCDHT_500to700_2016postVFP':QCDHT_500to700_2016postVFP, 'QCDHT_700to1000_2016postVFP':QCDHT_700to1000_2016postVFP,'QCDHT_1000to1500_2016postVFP':QCDHT_1000to1500_2016postVFP, 'QCDHT_1500to2000_2016postVFP':QCDHT_1500to2000_2016postVFP, 'QCDHT_2000toInf_2016postVFP':QCDHT_2000toInf_2016postVFP,
'ST_2016postVFP':ST_2016postVFP, 'ST_tch_t_2016postVFP':ST_tch_t_2016postVFP, 'ST_tch_tbar_2016postVFP':ST_tch_tbar_2016postVFP, 'ST_tW_t_2016postVFP':ST_tW_t_2016postVFP, 'ST_tW_tbar_2016postVFP':ST_tW_tbar_2016postVFP, 'ST_sch_2016postVFP':ST_sch_2016postVFP,



"DataMu_2016preVFP":DataMu_2016preVFP,"DataMuB0_2016preVFP":DataMuB0_2016preVFP,"DataMuB_2016preVFP":DataMuB_2016preVFP,"DataMuC_2016preVFP":DataMuC_2016preVFP,"DataMuD_2016preVFP":DataMuD_2016preVFP,"DataMuE_2016preVFP":DataMuE_2016preVFP,"DataMuF_2016preVFP":DataMuF_2016preVFP,
"DataMu_2016postVFP":DataMu_2016postVFP,"DataMuF_2016postVFP":DataMuF_2016postVFP,"DataMuG_2016postVFP":DataMuG_2016postVFP,"DataMuH_2016postVFP":DataMuH_2016postVFP,
"DataMu_2016":DataMu_2016,
"DataEle_2016preVFP":DataEle_2016preVFP,"DataEleB0_2016preVFP":DataEleB0_2016preVFP,"DataEleB_2016preVFP":DataEleB_2016preVFP,"DataEleC_2016preVFP":DataEleC_2016preVFP,"DataEleD_2016preVFP":DataEleD_2016preVFP,"DataEleE_2016preVFP":DataEleE_2016preVFP,"DataEleF_2016preVFP":DataEleF_2016preVFP,
"DataEle_2016postVFP":DataEle_2016postVFP,"DataEleF_2016postVFP":DataEleF_2016postVFP,"DataEleG_2016postVFP":DataEleG_2016postVFP,"DataEleH_2016postVFP":DataEleH_2016postVFP,
"DataEle_2016":DataEle_2016,
"DataPh_2016preVFP":DataPh_2016preVFP,"DataPhB0_2016preVFP":DataPhB0_2016preVFP,"DataPhB_2016preVFP":DataPhB_2016preVFP,"DataPhC_2016preVFP":DataPhC_2016preVFP,"DataPhD_2016preVFP":DataPhD_2016preVFP,"DataPhE_2016preVFP":DataPhE_2016preVFP,"DataPhF_2016preVFP":DataPhF_2016preVFP,
"DataPh_2016postVFP":DataPh_2016postVFP,"DataPhF_2016postVFP":DataPhF_2016postVFP,"DataPhG_2016postVFP":DataPhG_2016postVFP,"DataPhH_2016postVFP":DataPhH_2016postVFP,
"DataPh_2016":DataPh_2016,
"DataHT_2016preVFP":DataHT_2016preVFP,"DataHTB0_2016preVFP":DataHTB0_2016preVFP,"DataHTB_2016preVFP":DataHTB_2016preVFP,"DataHTC_2016preVFP":DataHTC_2016preVFP,"DataHTD_2016preVFP":DataHTD_2016preVFP,"DataHTE_2016preVFP":DataHTE_2016preVFP,"DataHTF_2016preVFP":DataHTF_2016preVFP,
"DataHT_2016postVFP":DataHT_2016postVFP,"DataHTF_2016postVFP":DataHTF_2016postVFP,"DataHTG_2016postVFP":DataHTG_2016postVFP,"DataHTH_2016postVFP":DataHTH_2016postVFP,
"DataHT_2016":DataHT_2016,
"Tprime_tHq_600LH_2017":Tprime_tHq_600LH_2017,"Tprime_tHq_700LH_2017":Tprime_tHq_700LH_2017,"Tprime_tHq_800LH_2017":Tprime_tHq_800LH_2017,"Tprime_tHq_900LH_2017":Tprime_tHq_900LH_2017,
"Tprime_tHq_1000LH_2017":Tprime_tHq_1000LH_2017,"Tprime_tHq_1100LH_2017":Tprime_tHq_1100LH_2017,"Tprime_tHq_1200LH_2017":Tprime_tHq_1200LH_2017,"Tprime_tHq_1300LH_2017":Tprime_tHq_1300LH_2017,
"Tprime_tHq_1400LH_2017":Tprime_tHq_1400LH_2017,"Tprime_tHq_1500LH_2017":Tprime_tHq_1500LH_2017,"Tprime_tHq_1600LH_2017":Tprime_tHq_1600LH_2017,"Tprime_tHq_1700LH_2017":Tprime_tHq_1700LH_2017,
"Tprime_tHq_1800LH_2017":Tprime_tHq_1800LH_2017,"Tprime_LH_2017":Tprime_LH_2017,
'TT_Mtt700to1000_2017':TT_Mtt700to1000_2017, 'TT_Mtt1000toInf_2017':TT_Mtt1000toInf_2017,"TT_semilep_2017":TT_semilep_2017,"TT_dilep_2017":TT_dilep_2017, "TT_Mtt_2017":TT_Mtt_2017,  
'WJets_2017':WJets_2017, 'WJetsHT70to100_2017':WJetsHT70to100_2017, 'WJetsHT100to200_2017':WJetsHT100to200_2017, 'WJetsHT200to400_2017':WJetsHT200to400_2017,'WJetsHT400to600_2017':WJetsHT400to600_2017, 'WJetsHT600to800_2017':WJetsHT600to800_2017, 'WJetsHT800to1200_2017':WJetsHT800to1200_2017, 'WJetsHT1200to2500_2017':WJetsHT1200to2500_2017,
'WJetsHT2500toInf_2017':WJetsHT2500toInf_2017,
'QCD_2017':QCD_2017, 'QCDHT_50to100_2017':QCDHT_50to100_2017,'QCDHT_100to200_2017':QCDHT_100to200_2017,'QCDHT_200to300_2017':QCDHT_200to300_2017,'QCDHT_300to500_2017':QCDHT_300to500_2017, 'QCDHT_500to700_2017':QCDHT_500to700_2017, 'QCDHT_700to1000_2017':QCDHT_700to1000_2017,
'QCDHT_1000to1500_2017':QCDHT_1000to1500_2017, 'QCDHT_1500to2000_2017':QCDHT_1500to2000_2017, 'QCDHT_2000toInf_2017':QCDHT_2000toInf_2017,
'ST_2017':ST_2017, 'ST_tch_t_2017':ST_tch_t_2017, 'ST_tch_tbar_2017':ST_tch_tbar_2017, 'ST_tW_t_2017':ST_tW_t_2017, 'ST_tW_tbar_2017':ST_tW_tbar_2017, 'ST_sch_2017':ST_sch_2017,"DataMuE_2017":DataMuE_2017,"DataMu_2017":DataMu_2017,"DataMuB_2017":DataMuB_2017,"DataMuC_2017":DataMuC_2017,"DataMuD_2017":DataMuD_2017,"DataMuF_2017":DataMuF_2017,
"DataEleE_2017":DataEleE_2017,"DataEle_2017":DataEle_2017,"DataEleB_2017":DataEleB_2017,"DataEleC_2017":DataEleC_2017,"DataEleD_2017":DataEleD_2017,"DataEleF_2017":DataEleF_2017,
"DataPhE_2017":DataPhE_2017,"DataPh_2017":DataPh_2017,"DataPhB_2017":DataPhB_2017,"DataPhC_2017":DataPhC_2017,"DataPhD_2017":DataPhD_2017,"DataPhF_2017":DataPhF_2017,
"DataHTE_2017":DataHTE_2017,"DataHT_2017":DataHT_2017,"DataHTB_2017":DataHTB_2017,"DataHTC_2017":DataHTC_2017,"DataHTD_2017":DataHTD_2017,"DataHTF_2017":DataHTF_2017,

"Tprime_tHq_600LH_2018":Tprime_tHq_600LH_2018,"Tprime_tHq_700LH_2018":Tprime_tHq_700LH_2018,"Tprime_tHq_800LH_2018":Tprime_tHq_800LH_2018,"Tprime_tHq_900LH_2018":Tprime_tHq_900LH_2018,
"Tprime_tHq_1000LH_2018":Tprime_tHq_1000LH_2018,"Tprime_tHq_1100LH_2018":Tprime_tHq_1100LH_2018,"Tprime_tHq_1200LH_2018":Tprime_tHq_1200LH_2018,"Tprime_tHq_1300LH_2018":Tprime_tHq_1300LH_2018,
"Tprime_tHq_1400LH_2018":Tprime_tHq_1400LH_2018,"Tprime_tHq_1500LH_2018":Tprime_tHq_1500LH_2018,"Tprime_tHq_1600LH_2018":Tprime_tHq_1600LH_2018,"Tprime_tHq_1700LH_2018":Tprime_tHq_1700LH_2018,
"Tprime_tHq_1800LH_2018":Tprime_tHq_1800LH_2018,"Tprime_LH_2018":Tprime_LH_2018,
'TT_Mtt700to1000_2018':TT_Mtt700to1000_2018, 'TT_Mtt1000toInf_2018':TT_Mtt1000toInf_2018,"TT_semilep_2018":TT_semilep_2018,"TT_dilep_2018":TT_dilep_2018,"TTJetsHT600to800_2018":TTJetsHT600to800_2018,"TTJetsHT800to1200_2018":TTJetsHT800to1200_2018, "TTJetsHT1200to2500_2018":TTJetsHT1200to2500_2018, "TTJetsHT2500toInf_2018":TTJetsHT2500toInf_2018, "TTJets_2018":TTJets_2018 ,"TT_Mtt_2018":TT_Mtt_2018, "TTH_2018":TTH_2018,"TTHtoNonbb_2018":TTHtoNonbb_2018,"TTHtobb_2018":TTHtobb_2018, "TTVJets_2018": TTVJets_2018,"TTZJets_2018":TTZJets_2018, "TTWJets_2018":TTWJets_2018, "TTGJets_2018":TTGJets_2018, "TGJets_2018":TGJets_2018, "TTGammaJets_2018":TTGammaJets_2018, "TTGHadJets_2018":TTGHadJets_2018,
'WJets_2018':WJets_2018, 'WJetsHT70to100_2018':WJetsHT70to100_2018, 'WJetsHT100to200_2018':WJetsHT100to200_2018, 'WJetsHT200to400_2018':WJetsHT200to400_2018,'WJetsHT400to600_2018':WJetsHT400to600_2018, 'WJetsHT600to800_2018':WJetsHT600to800_2018, 'WJetsHT800to1200_2018':WJetsHT800to1200_2018, 'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018,
'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
'QCD_2018':QCD_2018, 'QCDHT_50to100_2018':QCDHT_50to100_2018,'QCDHT_100to200_2018':QCDHT_100to200_2018,'QCDHT_200to300_2018':QCDHT_200to300_2018,'QCDHT_300to500_2018':QCDHT_300to500_2018, 'QCDHT_500to700_2018':QCDHT_500to700_2018, 'QCDHT_700to1000_2018':QCDHT_700to1000_2018,
'QCDHT_1000to1500_2018':QCDHT_1000to1500_2018, 'QCDHT_1500to2000_2018':QCDHT_1500to2000_2018, 'QCDHT_2000toInf_2018':QCDHT_2000toInf_2018,
'ST_2018':ST_2018, 'ST_tch_t_2018':ST_tch_t_2018, 'ST_tch_tbar_2018':ST_tch_tbar_2018, 'ST_tW_t_2018':ST_tW_t_2018, 'ST_tW_tbar_2018':ST_tW_tbar_2018, 'ST_sch_2018':ST_sch_2018,
"DataMuA_2018":DataMuA_2018,"DataMu_2018":DataMu_2018,"DataMuB_2018":DataMuB_2018,"DataMuC_2018":DataMuC_2018,"DataMuD_2018":DataMuD_2018,
"DataEleA_2018":DataEleA_2018,"DataEle_2018":DataEle_2018,"DataEleB_2018":DataEleB_2018,"DataEleC_2018":DataEleC_2018,"DataEleD_2018":DataEleD_2018,
"DataHTA_2018":DataHTA_2018,"DataHT_2018":DataHT_2018,"DataHTB_2018":DataHTB_2018,"DataHTC_2018":DataHTC_2018,"DataHTD_2018":DataHTD_2018,
'Tprime_tAq_600_MH25_LH_2016preVFP':Tprime_tAq_600_MH25_LH_2016preVFP, 'Tprime_tAq_600_MH50_LH_2016preVFP':Tprime_tAq_600_MH50_LH_2016preVFP, 'Tprime_tAq_600_MH75_LH_2016preVFP':Tprime_tAq_600_MH75_LH_2016preVFP, 'Tprime_tAq_600_MH100_LH_2016preVFP':Tprime_tAq_600_MH100_LH_2016preVFP, 'Tprime_tAq_600_MH125_LH_2016preVFP':Tprime_tAq_600_MH125_LH_2016preVFP, 'Tprime_tAq_600_MH150_LH_2016preVFP':Tprime_tAq_600_MH150_LH_2016preVFP, 'Tprime_tAq_600_MH175_LH_2016preVFP':Tprime_tAq_600_MH175_LH_2016preVFP, 'Tprime_tAq_600_MH200_LH_2016preVFP':Tprime_tAq_600_MH200_LH_2016preVFP, 'Tprime_tAq_600_MH250_LH_2016preVFP':Tprime_tAq_600_MH250_LH_2016preVFP, 'Tprime_tAq_600_MH350_LH_2016preVFP':Tprime_tAq_600_MH350_LH_2016preVFP, 'Tprime_tAq_600_MH450_LH_2016preVFP':Tprime_tAq_600_MH450_LH_2016preVFP, 'Tprime_tAq_600_MH500_LH_2016preVFP':Tprime_tAq_600_MH500_LH_2016preVFP, 'Tprime_tAq_700_MH25_LH_2016preVFP':Tprime_tAq_700_MH25_LH_2016preVFP, 'Tprime_tAq_700_MH50_LH_2016preVFP':Tprime_tAq_700_MH50_LH_2016preVFP, 'Tprime_tAq_700_MH75_LH_2016preVFP':Tprime_tAq_700_MH75_LH_2016preVFP, 'Tprime_tAq_700_MH100_LH_2016preVFP':Tprime_tAq_700_MH100_LH_2016preVFP, 'Tprime_tAq_700_MH125_LH_2016preVFP':Tprime_tAq_700_MH125_LH_2016preVFP, 'Tprime_tAq_700_MH150_LH_2016preVFP':Tprime_tAq_700_MH150_LH_2016preVFP, 'Tprime_tAq_700_MH175_LH_2016preVFP':Tprime_tAq_700_MH175_LH_2016preVFP, 'Tprime_tAq_700_MH200_LH_2016preVFP':Tprime_tAq_700_MH200_LH_2016preVFP, 'Tprime_tAq_700_MH250_LH_2016preVFP':Tprime_tAq_700_MH250_LH_2016preVFP, 'Tprime_tAq_700_MH350_LH_2016preVFP':Tprime_tAq_700_MH350_LH_2016preVFP, 'Tprime_tAq_700_MH450_LH_2016preVFP':Tprime_tAq_700_MH450_LH_2016preVFP, 'Tprime_tAq_700_MH500_LH_2016preVFP':Tprime_tAq_700_MH500_LH_2016preVFP, 'Tprime_tAq_800_MH25_LH_2016preVFP':Tprime_tAq_800_MH25_LH_2016preVFP, 'Tprime_tAq_800_MH50_LH_2016preVFP':Tprime_tAq_800_MH50_LH_2016preVFP, 'Tprime_tAq_800_MH75_LH_2016preVFP':Tprime_tAq_800_MH75_LH_2016preVFP, 'Tprime_tAq_800_MH100_LH_2016preVFP':Tprime_tAq_800_MH100_LH_2016preVFP, 'Tprime_tAq_800_MH125_LH_2016preVFP':Tprime_tAq_800_MH125_LH_2016preVFP, 'Tprime_tAq_800_MH150_LH_2016preVFP':Tprime_tAq_800_MH150_LH_2016preVFP, 'Tprime_tAq_800_MH175_LH_2016preVFP':Tprime_tAq_800_MH175_LH_2016preVFP, 'Tprime_tAq_800_MH200_LH_2016preVFP':Tprime_tAq_800_MH200_LH_2016preVFP, 'Tprime_tAq_800_MH250_LH_2016preVFP':Tprime_tAq_800_MH250_LH_2016preVFP, 'Tprime_tAq_800_MH350_LH_2016preVFP':Tprime_tAq_800_MH350_LH_2016preVFP, 'Tprime_tAq_800_MH450_LH_2016preVFP':Tprime_tAq_800_MH450_LH_2016preVFP, 'Tprime_tAq_800_MH500_LH_2016preVFP':Tprime_tAq_800_MH500_LH_2016preVFP, 'Tprime_tAq_900_MH25_LH_2016preVFP':Tprime_tAq_900_MH25_LH_2016preVFP, 'Tprime_tAq_900_MH50_LH_2016preVFP':Tprime_tAq_900_MH50_LH_2016preVFP, 'Tprime_tAq_900_MH75_LH_2016preVFP':Tprime_tAq_900_MH75_LH_2016preVFP, 'Tprime_tAq_900_MH100_LH_2016preVFP':Tprime_tAq_900_MH100_LH_2016preVFP, 'Tprime_tAq_900_MH125_LH_2016preVFP':Tprime_tAq_900_MH125_LH_2016preVFP, 'Tprime_tAq_900_MH150_LH_2016preVFP':Tprime_tAq_900_MH150_LH_2016preVFP, 'Tprime_tAq_900_MH175_LH_2016preVFP':Tprime_tAq_900_MH175_LH_2016preVFP, 'Tprime_tAq_900_MH200_LH_2016preVFP':Tprime_tAq_900_MH200_LH_2016preVFP, 'Tprime_tAq_900_MH250_LH_2016preVFP':Tprime_tAq_900_MH250_LH_2016preVFP, 'Tprime_tAq_900_MH350_LH_2016preVFP':Tprime_tAq_900_MH350_LH_2016preVFP, 'Tprime_tAq_900_MH450_LH_2016preVFP':Tprime_tAq_900_MH450_LH_2016preVFP, 'Tprime_tAq_900_MH500_LH_2016preVFP':Tprime_tAq_900_MH500_LH_2016preVFP, 'Tprime_tAq_1000_MH25_LH_2016preVFP':Tprime_tAq_1000_MH25_LH_2016preVFP, 'Tprime_tAq_1000_MH50_LH_2016preVFP':Tprime_tAq_1000_MH50_LH_2016preVFP, 'Tprime_tAq_1000_MH75_LH_2016preVFP':Tprime_tAq_1000_MH75_LH_2016preVFP, 'Tprime_tAq_1000_MH100_LH_2016preVFP':Tprime_tAq_1000_MH100_LH_2016preVFP, 'Tprime_tAq_1000_MH125_LH_2016preVFP':Tprime_tAq_1000_MH125_LH_2016preVFP, 'Tprime_tAq_1000_MH150_LH_2016preVFP':Tprime_tAq_1000_MH150_LH_2016preVFP, 'Tprime_tAq_1000_MH175_LH_2016preVFP':Tprime_tAq_1000_MH175_LH_2016preVFP, 'Tprime_tAq_1000_MH200_LH_2016preVFP':Tprime_tAq_1000_MH200_LH_2016preVFP, 'Tprime_tAq_1000_MH250_LH_2016preVFP':Tprime_tAq_1000_MH250_LH_2016preVFP, 'Tprime_tAq_1000_MH350_LH_2016preVFP':Tprime_tAq_1000_MH350_LH_2016preVFP, 'Tprime_tAq_1000_MH450_LH_2016preVFP':Tprime_tAq_1000_MH450_LH_2016preVFP, 'Tprime_tAq_1000_MH500_LH_2016preVFP':Tprime_tAq_1000_MH500_LH_2016preVFP, 'Tprime_tAq_1100_MH25_LH_2016preVFP':Tprime_tAq_1100_MH25_LH_2016preVFP, 'Tprime_tAq_1100_MH50_LH_2016preVFP':Tprime_tAq_1100_MH50_LH_2016preVFP, 'Tprime_tAq_1100_MH75_LH_2016preVFP':Tprime_tAq_1100_MH75_LH_2016preVFP, 'Tprime_tAq_1100_MH100_LH_2016preVFP':Tprime_tAq_1100_MH100_LH_2016preVFP, 'Tprime_tAq_1100_MH125_LH_2016preVFP':Tprime_tAq_1100_MH125_LH_2016preVFP, 'Tprime_tAq_1100_MH150_LH_2016preVFP':Tprime_tAq_1100_MH150_LH_2016preVFP, 'Tprime_tAq_1100_MH175_LH_2016preVFP':Tprime_tAq_1100_MH175_LH_2016preVFP, 'Tprime_tAq_1100_MH200_LH_2016preVFP':Tprime_tAq_1100_MH200_LH_2016preVFP, 'Tprime_tAq_1100_MH250_LH_2016preVFP':Tprime_tAq_1100_MH250_LH_2016preVFP, 'Tprime_tAq_1100_MH350_LH_2016preVFP':Tprime_tAq_1100_MH350_LH_2016preVFP, 'Tprime_tAq_1100_MH450_LH_2016preVFP':Tprime_tAq_1100_MH450_LH_2016preVFP, 'Tprime_tAq_1100_MH500_LH_2016preVFP':Tprime_tAq_1100_MH500_LH_2016preVFP, 'Tprime_tAq_1200_MH25_LH_2016preVFP':Tprime_tAq_1200_MH25_LH_2016preVFP, 'Tprime_tAq_1200_MH50_LH_2016preVFP':Tprime_tAq_1200_MH50_LH_2016preVFP, 'Tprime_tAq_1200_MH75_LH_2016preVFP':Tprime_tAq_1200_MH75_LH_2016preVFP, 'Tprime_tAq_1200_MH100_LH_2016preVFP':Tprime_tAq_1200_MH100_LH_2016preVFP, 'Tprime_tAq_1200_MH125_LH_2016preVFP':Tprime_tAq_1200_MH125_LH_2016preVFP, 'Tprime_tAq_1200_MH150_LH_2016preVFP':Tprime_tAq_1200_MH150_LH_2016preVFP, 'Tprime_tAq_1200_MH175_LH_2016preVFP':Tprime_tAq_1200_MH175_LH_2016preVFP, 'Tprime_tAq_1200_MH200_LH_2016preVFP':Tprime_tAq_1200_MH200_LH_2016preVFP, 'Tprime_tAq_1200_MH250_LH_2016preVFP':Tprime_tAq_1200_MH250_LH_2016preVFP, 'Tprime_tAq_1200_MH350_LH_2016preVFP':Tprime_tAq_1200_MH350_LH_2016preVFP, 'Tprime_tAq_1200_MH450_LH_2016preVFP':Tprime_tAq_1200_MH450_LH_2016preVFP, 'Tprime_tAq_1200_MH500_LH_2016preVFP':Tprime_tAq_1200_MH500_LH_2016preVFP, 'Tprime_tAq_1300_MH25_LH_2016preVFP':Tprime_tAq_1300_MH25_LH_2016preVFP, 'Tprime_tAq_1300_MH50_LH_2016preVFP':Tprime_tAq_1300_MH50_LH_2016preVFP, 'Tprime_tAq_1300_MH75_LH_2016preVFP':Tprime_tAq_1300_MH75_LH_2016preVFP, 'Tprime_tAq_1300_MH100_LH_2016preVFP':Tprime_tAq_1300_MH100_LH_2016preVFP, 'Tprime_tAq_1300_MH125_LH_2016preVFP':Tprime_tAq_1300_MH125_LH_2016preVFP, 'Tprime_tAq_1300_MH150_LH_2016preVFP':Tprime_tAq_1300_MH150_LH_2016preVFP, 'Tprime_tAq_1300_MH175_LH_2016preVFP':Tprime_tAq_1300_MH175_LH_2016preVFP, 'Tprime_tAq_1300_MH200_LH_2016preVFP':Tprime_tAq_1300_MH200_LH_2016preVFP, 'Tprime_tAq_1300_MH250_LH_2016preVFP':Tprime_tAq_1300_MH250_LH_2016preVFP, 'Tprime_tAq_1300_MH350_LH_2016preVFP':Tprime_tAq_1300_MH350_LH_2016preVFP, 'Tprime_tAq_1300_MH450_LH_2016preVFP':Tprime_tAq_1300_MH450_LH_2016preVFP, 'Tprime_tAq_1300_MH500_LH_2016preVFP':Tprime_tAq_1300_MH500_LH_2016preVFP, 'Tprime_tAq_1400_MH25_LH_2016preVFP':Tprime_tAq_1400_MH25_LH_2016preVFP, 'Tprime_tAq_1400_MH50_LH_2016preVFP':Tprime_tAq_1400_MH50_LH_2016preVFP, 'Tprime_tAq_1400_MH75_LH_2016preVFP':Tprime_tAq_1400_MH75_LH_2016preVFP, 'Tprime_tAq_1400_MH100_LH_2016preVFP':Tprime_tAq_1400_MH100_LH_2016preVFP, 'Tprime_tAq_1400_MH125_LH_2016preVFP':Tprime_tAq_1400_MH125_LH_2016preVFP, 'Tprime_tAq_1400_MH150_LH_2016preVFP':Tprime_tAq_1400_MH150_LH_2016preVFP, 'Tprime_tAq_1400_MH175_LH_2016preVFP':Tprime_tAq_1400_MH175_LH_2016preVFP, 'Tprime_tAq_1400_MH200_LH_2016preVFP':Tprime_tAq_1400_MH200_LH_2016preVFP, 'Tprime_tAq_1400_MH250_LH_2016preVFP':Tprime_tAq_1400_MH250_LH_2016preVFP, 'Tprime_tAq_1400_MH350_LH_2016preVFP':Tprime_tAq_1400_MH350_LH_2016preVFP, 'Tprime_tAq_1400_MH450_LH_2016preVFP':Tprime_tAq_1400_MH450_LH_2016preVFP, 'Tprime_tAq_1400_MH500_LH_2016preVFP':Tprime_tAq_1400_MH500_LH_2016preVFP, 'Tprime_tAq_1500_MH25_LH_2016preVFP':Tprime_tAq_1500_MH25_LH_2016preVFP, 'Tprime_tAq_1500_MH50_LH_2016preVFP':Tprime_tAq_1500_MH50_LH_2016preVFP, 'Tprime_tAq_1500_MH75_LH_2016preVFP':Tprime_tAq_1500_MH75_LH_2016preVFP, 'Tprime_tAq_1500_MH100_LH_2016preVFP':Tprime_tAq_1500_MH100_LH_2016preVFP, 'Tprime_tAq_1500_MH125_LH_2016preVFP':Tprime_tAq_1500_MH125_LH_2016preVFP, 'Tprime_tAq_1500_MH150_LH_2016preVFP':Tprime_tAq_1500_MH150_LH_2016preVFP, 'Tprime_tAq_1500_MH175_LH_2016preVFP':Tprime_tAq_1500_MH175_LH_2016preVFP, 'Tprime_tAq_1500_MH200_LH_2016preVFP':Tprime_tAq_1500_MH200_LH_2016preVFP, 'Tprime_tAq_1500_MH250_LH_2016preVFP':Tprime_tAq_1500_MH250_LH_2016preVFP, 'Tprime_tAq_1500_MH350_LH_2016preVFP':Tprime_tAq_1500_MH350_LH_2016preVFP, 'Tprime_tAq_1500_MH450_LH_2016preVFP':Tprime_tAq_1500_MH450_LH_2016preVFP, 'Tprime_tAq_1500_MH500_LH_2016preVFP':Tprime_tAq_1500_MH500_LH_2016preVFP, 'Tprime_tAq_1600_MH25_LH_2016preVFP':Tprime_tAq_1600_MH25_LH_2016preVFP, 'Tprime_tAq_1600_MH50_LH_2016preVFP':Tprime_tAq_1600_MH50_LH_2016preVFP, 'Tprime_tAq_1600_MH75_LH_2016preVFP':Tprime_tAq_1600_MH75_LH_2016preVFP, 'Tprime_tAq_1600_MH100_LH_2016preVFP':Tprime_tAq_1600_MH100_LH_2016preVFP, 'Tprime_tAq_1600_MH125_LH_2016preVFP':Tprime_tAq_1600_MH125_LH_2016preVFP, 'Tprime_tAq_1600_MH150_LH_2016preVFP':Tprime_tAq_1600_MH150_LH_2016preVFP, 'Tprime_tAq_1600_MH175_LH_2016preVFP':Tprime_tAq_1600_MH175_LH_2016preVFP, 'Tprime_tAq_1600_MH200_LH_2016preVFP':Tprime_tAq_1600_MH200_LH_2016preVFP, 'Tprime_tAq_1600_MH250_LH_2016preVFP':Tprime_tAq_1600_MH250_LH_2016preVFP, 'Tprime_tAq_1600_MH350_LH_2016preVFP':Tprime_tAq_1600_MH350_LH_2016preVFP, 'Tprime_tAq_1600_MH450_LH_2016preVFP':Tprime_tAq_1600_MH450_LH_2016preVFP, 'Tprime_tAq_1600_MH500_LH_2016preVFP':Tprime_tAq_1600_MH500_LH_2016preVFP, 'Tprime_tAq_1700_MH25_LH_2016preVFP':Tprime_tAq_1700_MH25_LH_2016preVFP, 'Tprime_tAq_1700_MH50_LH_2016preVFP':Tprime_tAq_1700_MH50_LH_2016preVFP, 'Tprime_tAq_1700_MH75_LH_2016preVFP':Tprime_tAq_1700_MH75_LH_2016preVFP, 'Tprime_tAq_1700_MH100_LH_2016preVFP':Tprime_tAq_1700_MH100_LH_2016preVFP, 'Tprime_tAq_1700_MH125_LH_2016preVFP':Tprime_tAq_1700_MH125_LH_2016preVFP, 'Tprime_tAq_1700_MH150_LH_2016preVFP':Tprime_tAq_1700_MH150_LH_2016preVFP, 'Tprime_tAq_1700_MH175_LH_2016preVFP':Tprime_tAq_1700_MH175_LH_2016preVFP, 'Tprime_tAq_1700_MH200_LH_2016preVFP':Tprime_tAq_1700_MH200_LH_2016preVFP, 'Tprime_tAq_1700_MH250_LH_2016preVFP':Tprime_tAq_1700_MH250_LH_2016preVFP, 'Tprime_tAq_1700_MH350_LH_2016preVFP':Tprime_tAq_1700_MH350_LH_2016preVFP, 'Tprime_tAq_1700_MH450_LH_2016preVFP':Tprime_tAq_1700_MH450_LH_2016preVFP, 'Tprime_tAq_1700_MH500_LH_2016preVFP':Tprime_tAq_1700_MH500_LH_2016preVFP, 'Tprime_tAq_1800_MH25_LH_2016preVFP':Tprime_tAq_1800_MH25_LH_2016preVFP, 'Tprime_tAq_1800_MH50_LH_2016preVFP':Tprime_tAq_1800_MH50_LH_2016preVFP, 'Tprime_tAq_1800_MH75_LH_2016preVFP':Tprime_tAq_1800_MH75_LH_2016preVFP, 'Tprime_tAq_1800_MH100_LH_2016preVFP':Tprime_tAq_1800_MH100_LH_2016preVFP, 'Tprime_tAq_1800_MH125_LH_2016preVFP':Tprime_tAq_1800_MH125_LH_2016preVFP, 'Tprime_tAq_1800_MH150_LH_2016preVFP':Tprime_tAq_1800_MH150_LH_2016preVFP, 'Tprime_tAq_1800_MH175_LH_2016preVFP':Tprime_tAq_1800_MH175_LH_2016preVFP, 'Tprime_tAq_1800_MH200_LH_2016preVFP':Tprime_tAq_1800_MH200_LH_2016preVFP, 'Tprime_tAq_1800_MH250_LH_2016preVFP':Tprime_tAq_1800_MH250_LH_2016preVFP, 'Tprime_tAq_1800_MH350_LH_2016preVFP':Tprime_tAq_1800_MH350_LH_2016preVFP, 'Tprime_tAq_1800_MH450_LH_2016preVFP':Tprime_tAq_1800_MH450_LH_2016preVFP, 'Tprime_tAq_1800_MH500_LH_2016preVFP':Tprime_tAq_1800_MH500_LH_2016preVFP, 'Tprime_tAq_1900_MH25_LH_2016preVFP':Tprime_tAq_1900_MH25_LH_2016preVFP, 'Tprime_tAq_1900_MH50_LH_2016preVFP':Tprime_tAq_1900_MH50_LH_2016preVFP, 'Tprime_tAq_1900_MH75_LH_2016preVFP':Tprime_tAq_1900_MH75_LH_2016preVFP, 'Tprime_tAq_1900_MH100_LH_2016preVFP':Tprime_tAq_1900_MH100_LH_2016preVFP, 'Tprime_tAq_1900_MH125_LH_2016preVFP':Tprime_tAq_1900_MH125_LH_2016preVFP, 'Tprime_tAq_1900_MH150_LH_2016preVFP':Tprime_tAq_1900_MH150_LH_2016preVFP, 'Tprime_tAq_1900_MH175_LH_2016preVFP':Tprime_tAq_1900_MH175_LH_2016preVFP, 'Tprime_tAq_1900_MH200_LH_2016preVFP':Tprime_tAq_1900_MH200_LH_2016preVFP, 'Tprime_tAq_1900_MH250_LH_2016preVFP':Tprime_tAq_1900_MH250_LH_2016preVFP, 'Tprime_tAq_1900_MH350_LH_2016preVFP':Tprime_tAq_1900_MH350_LH_2016preVFP, 'Tprime_tAq_1900_MH450_LH_2016preVFP':Tprime_tAq_1900_MH450_LH_2016preVFP, 'Tprime_tAq_1900_MH500_LH_2016preVFP':Tprime_tAq_1900_MH500_LH_2016preVFP, 'Tprime_tAq_2000_MH25_LH_2016preVFP':Tprime_tAq_2000_MH25_LH_2016preVFP, 'Tprime_tAq_2000_MH50_LH_2016preVFP':Tprime_tAq_2000_MH50_LH_2016preVFP, 'Tprime_tAq_2000_MH75_LH_2016preVFP':Tprime_tAq_2000_MH75_LH_2016preVFP, 'Tprime_tAq_2000_MH100_LH_2016preVFP':Tprime_tAq_2000_MH100_LH_2016preVFP, 'Tprime_tAq_2000_MH125_LH_2016preVFP':Tprime_tAq_2000_MH125_LH_2016preVFP, 'Tprime_tAq_2000_MH150_LH_2016preVFP':Tprime_tAq_2000_MH150_LH_2016preVFP, 'Tprime_tAq_2000_MH175_LH_2016preVFP':Tprime_tAq_2000_MH175_LH_2016preVFP, 'Tprime_tAq_2000_MH200_LH_2016preVFP':Tprime_tAq_2000_MH200_LH_2016preVFP, 'Tprime_tAq_2000_MH250_LH_2016preVFP':Tprime_tAq_2000_MH250_LH_2016preVFP, 'Tprime_tAq_2000_MH350_LH_2016preVFP':Tprime_tAq_2000_MH350_LH_2016preVFP, 'Tprime_tAq_2000_MH450_LH_2016preVFP':Tprime_tAq_2000_MH450_LH_2016preVFP, 'Tprime_tAq_2000_MH500_LH_2016preVFP':Tprime_tAq_2000_MH500_LH_2016preVFP, 'Tprime_tAq_2100_MH25_LH_2016preVFP':Tprime_tAq_2100_MH25_LH_2016preVFP, 'Tprime_tAq_2100_MH50_LH_2016preVFP':Tprime_tAq_2100_MH50_LH_2016preVFP, 'Tprime_tAq_2100_MH75_LH_2016preVFP':Tprime_tAq_2100_MH75_LH_2016preVFP, 'Tprime_tAq_2100_MH100_LH_2016preVFP':Tprime_tAq_2100_MH100_LH_2016preVFP, 'Tprime_tAq_2100_MH125_LH_2016preVFP':Tprime_tAq_2100_MH125_LH_2016preVFP, 'Tprime_tAq_2100_MH150_LH_2016preVFP':Tprime_tAq_2100_MH150_LH_2016preVFP, 'Tprime_tAq_2100_MH175_LH_2016preVFP':Tprime_tAq_2100_MH175_LH_2016preVFP, 'Tprime_tAq_2100_MH200_LH_2016preVFP':Tprime_tAq_2100_MH200_LH_2016preVFP, 'Tprime_tAq_2100_MH250_LH_2016preVFP':Tprime_tAq_2100_MH250_LH_2016preVFP, 'Tprime_tAq_2100_MH350_LH_2016preVFP':Tprime_tAq_2100_MH350_LH_2016preVFP, 'Tprime_tAq_2100_MH450_LH_2016preVFP':Tprime_tAq_2100_MH450_LH_2016preVFP, 'Tprime_tAq_2100_MH500_LH_2016preVFP':Tprime_tAq_2100_MH500_LH_2016preVFP, 'Tprime_tAq_2200_MH25_LH_2016preVFP':Tprime_tAq_2200_MH25_LH_2016preVFP, 'Tprime_tAq_2200_MH50_LH_2016preVFP':Tprime_tAq_2200_MH50_LH_2016preVFP, 'Tprime_tAq_2200_MH75_LH_2016preVFP':Tprime_tAq_2200_MH75_LH_2016preVFP, 'Tprime_tAq_2200_MH100_LH_2016preVFP':Tprime_tAq_2200_MH100_LH_2016preVFP, 'Tprime_tAq_2200_MH125_LH_2016preVFP':Tprime_tAq_2200_MH125_LH_2016preVFP, 'Tprime_tAq_2200_MH150_LH_2016preVFP':Tprime_tAq_2200_MH150_LH_2016preVFP, 'Tprime_tAq_2200_MH175_LH_2016preVFP':Tprime_tAq_2200_MH175_LH_2016preVFP, 'Tprime_tAq_2200_MH200_LH_2016preVFP':Tprime_tAq_2200_MH200_LH_2016preVFP, 'Tprime_tAq_2200_MH250_LH_2016preVFP':Tprime_tAq_2200_MH250_LH_2016preVFP, 'Tprime_tAq_2200_MH350_LH_2016preVFP':Tprime_tAq_2200_MH350_LH_2016preVFP, 'Tprime_tAq_2200_MH450_LH_2016preVFP':Tprime_tAq_2200_MH450_LH_2016preVFP, 'Tprime_tAq_2200_MH500_LH_2016preVFP':Tprime_tAq_2200_MH500_LH_2016preVFP, 'Tprime_tAq_2300_MH25_LH_2016preVFP':Tprime_tAq_2300_MH25_LH_2016preVFP, 'Tprime_tAq_2300_MH50_LH_2016preVFP':Tprime_tAq_2300_MH50_LH_2016preVFP, 'Tprime_tAq_2300_MH75_LH_2016preVFP':Tprime_tAq_2300_MH75_LH_2016preVFP, 'Tprime_tAq_2300_MH100_LH_2016preVFP':Tprime_tAq_2300_MH100_LH_2016preVFP, 'Tprime_tAq_2300_MH125_LH_2016preVFP':Tprime_tAq_2300_MH125_LH_2016preVFP, 'Tprime_tAq_2300_MH150_LH_2016preVFP':Tprime_tAq_2300_MH150_LH_2016preVFP, 'Tprime_tAq_2300_MH175_LH_2016preVFP':Tprime_tAq_2300_MH175_LH_2016preVFP, 'Tprime_tAq_2300_MH200_LH_2016preVFP':Tprime_tAq_2300_MH200_LH_2016preVFP, 'Tprime_tAq_2300_MH250_LH_2016preVFP':Tprime_tAq_2300_MH250_LH_2016preVFP, 'Tprime_tAq_2300_MH350_LH_2016preVFP':Tprime_tAq_2300_MH350_LH_2016preVFP, 'Tprime_tAq_2300_MH450_LH_2016preVFP':Tprime_tAq_2300_MH450_LH_2016preVFP, 'Tprime_tAq_2300_MH500_LH_2016preVFP':Tprime_tAq_2300_MH500_LH_2016preVFP, 'Tprime_tAq_2400_MH25_LH_2016preVFP':Tprime_tAq_2400_MH25_LH_2016preVFP, 'Tprime_tAq_2400_MH50_LH_2016preVFP':Tprime_tAq_2400_MH50_LH_2016preVFP, 'Tprime_tAq_2400_MH75_LH_2016preVFP':Tprime_tAq_2400_MH75_LH_2016preVFP, 'Tprime_tAq_2400_MH100_LH_2016preVFP':Tprime_tAq_2400_MH100_LH_2016preVFP, 'Tprime_tAq_2400_MH125_LH_2016preVFP':Tprime_tAq_2400_MH125_LH_2016preVFP, 'Tprime_tAq_2400_MH150_LH_2016preVFP':Tprime_tAq_2400_MH150_LH_2016preVFP, 'Tprime_tAq_2400_MH175_LH_2016preVFP':Tprime_tAq_2400_MH175_LH_2016preVFP, 'Tprime_tAq_2400_MH200_LH_2016preVFP':Tprime_tAq_2400_MH200_LH_2016preVFP, 'Tprime_tAq_2400_MH250_LH_2016preVFP':Tprime_tAq_2400_MH250_LH_2016preVFP, 'Tprime_tAq_2400_MH350_LH_2016preVFP':Tprime_tAq_2400_MH350_LH_2016preVFP, 'Tprime_tAq_2400_MH450_LH_2016preVFP':Tprime_tAq_2400_MH450_LH_2016preVFP, 'Tprime_tAq_2400_MH500_LH_2016preVFP':Tprime_tAq_2400_MH500_LH_2016preVFP, 'Tprime_tAq_2500_MH25_LH_2016preVFP':Tprime_tAq_2500_MH25_LH_2016preVFP, 'Tprime_tAq_2500_MH50_LH_2016preVFP':Tprime_tAq_2500_MH50_LH_2016preVFP, 'Tprime_tAq_2500_MH75_LH_2016preVFP':Tprime_tAq_2500_MH75_LH_2016preVFP, 'Tprime_tAq_2500_MH100_LH_2016preVFP':Tprime_tAq_2500_MH100_LH_2016preVFP, 'Tprime_tAq_2500_MH125_LH_2016preVFP':Tprime_tAq_2500_MH125_LH_2016preVFP, 'Tprime_tAq_2500_MH150_LH_2016preVFP':Tprime_tAq_2500_MH150_LH_2016preVFP, 'Tprime_tAq_2500_MH175_LH_2016preVFP':Tprime_tAq_2500_MH175_LH_2016preVFP, 'Tprime_tAq_2500_MH200_LH_2016preVFP':Tprime_tAq_2500_MH200_LH_2016preVFP, 'Tprime_tAq_2500_MH250_LH_2016preVFP':Tprime_tAq_2500_MH250_LH_2016preVFP, 'Tprime_tAq_2500_MH350_LH_2016preVFP':Tprime_tAq_2500_MH350_LH_2016preVFP, 'Tprime_tAq_2500_MH450_LH_2016preVFP':Tprime_tAq_2500_MH450_LH_2016preVFP, 'Tprime_tAq_2500_MH500_LH_2016preVFP':Tprime_tAq_2500_MH500_LH_2016preVFP, 'Tprime_tAq_2600_MH25_LH_2016preVFP':Tprime_tAq_2600_MH25_LH_2016preVFP, 'Tprime_tAq_2600_MH50_LH_2016preVFP':Tprime_tAq_2600_MH50_LH_2016preVFP, 'Tprime_tAq_2600_MH75_LH_2016preVFP':Tprime_tAq_2600_MH75_LH_2016preVFP, 'Tprime_tAq_2600_MH100_LH_2016preVFP':Tprime_tAq_2600_MH100_LH_2016preVFP, 'Tprime_tAq_2600_MH125_LH_2016preVFP':Tprime_tAq_2600_MH125_LH_2016preVFP, 'Tprime_tAq_2600_MH150_LH_2016preVFP':Tprime_tAq_2600_MH150_LH_2016preVFP, 'Tprime_tAq_2600_MH175_LH_2016preVFP':Tprime_tAq_2600_MH175_LH_2016preVFP, 'Tprime_tAq_2600_MH200_LH_2016preVFP':Tprime_tAq_2600_MH200_LH_2016preVFP, 'Tprime_tAq_2600_MH250_LH_2016preVFP':Tprime_tAq_2600_MH250_LH_2016preVFP, 'Tprime_tAq_2600_MH350_LH_2016preVFP':Tprime_tAq_2600_MH350_LH_2016preVFP, 'Tprime_tAq_2600_MH450_LH_2016preVFP':Tprime_tAq_2600_MH450_LH_2016preVFP, 'Tprime_tAq_2600_MH500_LH_2016preVFP':Tprime_tAq_2600_MH500_LH_2016preVFP, 'Tprime_tAq_2700_MH25_LH_2016preVFP':Tprime_tAq_2700_MH25_LH_2016preVFP, 'Tprime_tAq_2700_MH50_LH_2016preVFP':Tprime_tAq_2700_MH50_LH_2016preVFP, 'Tprime_tAq_2700_MH75_LH_2016preVFP':Tprime_tAq_2700_MH75_LH_2016preVFP, 'Tprime_tAq_2700_MH100_LH_2016preVFP':Tprime_tAq_2700_MH100_LH_2016preVFP, 'Tprime_tAq_2700_MH125_LH_2016preVFP':Tprime_tAq_2700_MH125_LH_2016preVFP, 'Tprime_tAq_2700_MH150_LH_2016preVFP':Tprime_tAq_2700_MH150_LH_2016preVFP, 'Tprime_tAq_2700_MH175_LH_2016preVFP':Tprime_tAq_2700_MH175_LH_2016preVFP, 'Tprime_tAq_2700_MH200_LH_2016preVFP':Tprime_tAq_2700_MH200_LH_2016preVFP, 'Tprime_tAq_2700_MH250_LH_2016preVFP':Tprime_tAq_2700_MH250_LH_2016preVFP, 'Tprime_tAq_2700_MH350_LH_2016preVFP':Tprime_tAq_2700_MH350_LH_2016preVFP, 'Tprime_tAq_2700_MH450_LH_2016preVFP':Tprime_tAq_2700_MH450_LH_2016preVFP, 'Tprime_tAq_2700_MH500_LH_2016preVFP':Tprime_tAq_2700_MH500_LH_2016preVFP, 'Tprime_tAq_2800_MH25_LH_2016preVFP':Tprime_tAq_2800_MH25_LH_2016preVFP, 'Tprime_tAq_2800_MH50_LH_2016preVFP':Tprime_tAq_2800_MH50_LH_2016preVFP, 'Tprime_tAq_2800_MH75_LH_2016preVFP':Tprime_tAq_2800_MH75_LH_2016preVFP, 'Tprime_tAq_2800_MH100_LH_2016preVFP':Tprime_tAq_2800_MH100_LH_2016preVFP, 'Tprime_tAq_2800_MH125_LH_2016preVFP':Tprime_tAq_2800_MH125_LH_2016preVFP, 'Tprime_tAq_2800_MH150_LH_2016preVFP':Tprime_tAq_2800_MH150_LH_2016preVFP, 'Tprime_tAq_2800_MH175_LH_2016preVFP':Tprime_tAq_2800_MH175_LH_2016preVFP, 'Tprime_tAq_2800_MH200_LH_2016preVFP':Tprime_tAq_2800_MH200_LH_2016preVFP, 'Tprime_tAq_2800_MH250_LH_2016preVFP':Tprime_tAq_2800_MH250_LH_2016preVFP, 'Tprime_tAq_2800_MH350_LH_2016preVFP':Tprime_tAq_2800_MH350_LH_2016preVFP, 'Tprime_tAq_2800_MH450_LH_2016preVFP':Tprime_tAq_2800_MH450_LH_2016preVFP, 'Tprime_tAq_2800_MH500_LH_2016preVFP':Tprime_tAq_2800_MH500_LH_2016preVFP, 'Tprime_tAq_2900_MH25_LH_2016preVFP':Tprime_tAq_2900_MH25_LH_2016preVFP, 'Tprime_tAq_2900_MH50_LH_2016preVFP':Tprime_tAq_2900_MH50_LH_2016preVFP, 'Tprime_tAq_2900_MH75_LH_2016preVFP':Tprime_tAq_2900_MH75_LH_2016preVFP, 'Tprime_tAq_2900_MH100_LH_2016preVFP':Tprime_tAq_2900_MH100_LH_2016preVFP, 'Tprime_tAq_2900_MH125_LH_2016preVFP':Tprime_tAq_2900_MH125_LH_2016preVFP, 'Tprime_tAq_2900_MH150_LH_2016preVFP':Tprime_tAq_2900_MH150_LH_2016preVFP, 'Tprime_tAq_2900_MH175_LH_2016preVFP':Tprime_tAq_2900_MH175_LH_2016preVFP, 'Tprime_tAq_2900_MH200_LH_2016preVFP':Tprime_tAq_2900_MH200_LH_2016preVFP, 'Tprime_tAq_2900_MH250_LH_2016preVFP':Tprime_tAq_2900_MH250_LH_2016preVFP, 'Tprime_tAq_2900_MH350_LH_2016preVFP':Tprime_tAq_2900_MH350_LH_2016preVFP, 'Tprime_tAq_2900_MH450_LH_2016preVFP':Tprime_tAq_2900_MH450_LH_2016preVFP, 'Tprime_tAq_2900_MH500_LH_2016preVFP':Tprime_tAq_2900_MH500_LH_2016preVFP, 'Tprime_tAq_3000_MH25_LH_2016preVFP':Tprime_tAq_3000_MH25_LH_2016preVFP, 'Tprime_tAq_3000_MH50_LH_2016preVFP':Tprime_tAq_3000_MH50_LH_2016preVFP, 'Tprime_tAq_3000_MH75_LH_2016preVFP':Tprime_tAq_3000_MH75_LH_2016preVFP, 'Tprime_tAq_3000_MH100_LH_2016preVFP':Tprime_tAq_3000_MH100_LH_2016preVFP, 'Tprime_tAq_3000_MH125_LH_2016preVFP':Tprime_tAq_3000_MH125_LH_2016preVFP, 'Tprime_tAq_3000_MH150_LH_2016preVFP':Tprime_tAq_3000_MH150_LH_2016preVFP, 'Tprime_tAq_3000_MH175_LH_2016preVFP':Tprime_tAq_3000_MH175_LH_2016preVFP, 'Tprime_tAq_3000_MH200_LH_2016preVFP':Tprime_tAq_3000_MH200_LH_2016preVFP, 'Tprime_tAq_3000_MH250_LH_2016preVFP':Tprime_tAq_3000_MH250_LH_2016preVFP, 'Tprime_tAq_3000_MH350_LH_2016preVFP':Tprime_tAq_3000_MH350_LH_2016preVFP, 'Tprime_tAq_3000_MH450_LH_2016preVFP':Tprime_tAq_3000_MH450_LH_2016preVFP, 'Tprime_tAq_3000_MH500_LH_2016preVFP':Tprime_tAq_3000_MH500_LH_2016preVFP,
'Tprime_tAq_600_MH25_LH_2016postVFP':Tprime_tAq_600_MH25_LH_2016postVFP, 'Tprime_tAq_600_MH50_LH_2016postVFP':Tprime_tAq_600_MH50_LH_2016postVFP, 'Tprime_tAq_600_MH75_LH_2016postVFP':Tprime_tAq_600_MH75_LH_2016postVFP, 'Tprime_tAq_600_MH100_LH_2016postVFP':Tprime_tAq_600_MH100_LH_2016postVFP, 'Tprime_tAq_600_MH125_LH_2016postVFP':Tprime_tAq_600_MH125_LH_2016postVFP, 'Tprime_tAq_600_MH150_LH_2016postVFP':Tprime_tAq_600_MH150_LH_2016postVFP, 'Tprime_tAq_600_MH175_LH_2016postVFP':Tprime_tAq_600_MH175_LH_2016postVFP, 'Tprime_tAq_600_MH200_LH_2016postVFP':Tprime_tAq_600_MH200_LH_2016postVFP, 'Tprime_tAq_600_MH250_LH_2016postVFP':Tprime_tAq_600_MH250_LH_2016postVFP, 'Tprime_tAq_600_MH350_LH_2016postVFP':Tprime_tAq_600_MH350_LH_2016postVFP, 'Tprime_tAq_600_MH450_LH_2016postVFP':Tprime_tAq_600_MH450_LH_2016postVFP, 'Tprime_tAq_600_MH500_LH_2016postVFP':Tprime_tAq_600_MH500_LH_2016postVFP, 'Tprime_tAq_700_MH25_LH_2016postVFP':Tprime_tAq_700_MH25_LH_2016postVFP, 'Tprime_tAq_700_MH50_LH_2016postVFP':Tprime_tAq_700_MH50_LH_2016postVFP, 'Tprime_tAq_700_MH75_LH_2016postVFP':Tprime_tAq_700_MH75_LH_2016postVFP, 'Tprime_tAq_700_MH100_LH_2016postVFP':Tprime_tAq_700_MH100_LH_2016postVFP, 'Tprime_tAq_700_MH125_LH_2016postVFP':Tprime_tAq_700_MH125_LH_2016postVFP, 'Tprime_tAq_700_MH150_LH_2016postVFP':Tprime_tAq_700_MH150_LH_2016postVFP, 'Tprime_tAq_700_MH175_LH_2016postVFP':Tprime_tAq_700_MH175_LH_2016postVFP, 'Tprime_tAq_700_MH200_LH_2016postVFP':Tprime_tAq_700_MH200_LH_2016postVFP, 'Tprime_tAq_700_MH250_LH_2016postVFP':Tprime_tAq_700_MH250_LH_2016postVFP, 'Tprime_tAq_700_MH350_LH_2016postVFP':Tprime_tAq_700_MH350_LH_2016postVFP, 'Tprime_tAq_700_MH450_LH_2016postVFP':Tprime_tAq_700_MH450_LH_2016postVFP, 'Tprime_tAq_700_MH500_LH_2016postVFP':Tprime_tAq_700_MH500_LH_2016postVFP, 'Tprime_tAq_800_MH25_LH_2016postVFP':Tprime_tAq_800_MH25_LH_2016postVFP, 'Tprime_tAq_800_MH50_LH_2016postVFP':Tprime_tAq_800_MH50_LH_2016postVFP, 'Tprime_tAq_800_MH75_LH_2016postVFP':Tprime_tAq_800_MH75_LH_2016postVFP, 'Tprime_tAq_800_MH100_LH_2016postVFP':Tprime_tAq_800_MH100_LH_2016postVFP, 'Tprime_tAq_800_MH125_LH_2016postVFP':Tprime_tAq_800_MH125_LH_2016postVFP, 'Tprime_tAq_800_MH150_LH_2016postVFP':Tprime_tAq_800_MH150_LH_2016postVFP, 'Tprime_tAq_800_MH175_LH_2016postVFP':Tprime_tAq_800_MH175_LH_2016postVFP, 'Tprime_tAq_800_MH200_LH_2016postVFP':Tprime_tAq_800_MH200_LH_2016postVFP, 'Tprime_tAq_800_MH250_LH_2016postVFP':Tprime_tAq_800_MH250_LH_2016postVFP, 'Tprime_tAq_800_MH350_LH_2016postVFP':Tprime_tAq_800_MH350_LH_2016postVFP, 'Tprime_tAq_800_MH450_LH_2016postVFP':Tprime_tAq_800_MH450_LH_2016postVFP, 'Tprime_tAq_800_MH500_LH_2016postVFP':Tprime_tAq_800_MH500_LH_2016postVFP, 'Tprime_tAq_900_MH25_LH_2016postVFP':Tprime_tAq_900_MH25_LH_2016postVFP, 'Tprime_tAq_900_MH50_LH_2016postVFP':Tprime_tAq_900_MH50_LH_2016postVFP, 'Tprime_tAq_900_MH75_LH_2016postVFP':Tprime_tAq_900_MH75_LH_2016postVFP, 'Tprime_tAq_900_MH100_LH_2016postVFP':Tprime_tAq_900_MH100_LH_2016postVFP, 'Tprime_tAq_900_MH125_LH_2016postVFP':Tprime_tAq_900_MH125_LH_2016postVFP, 'Tprime_tAq_900_MH150_LH_2016postVFP':Tprime_tAq_900_MH150_LH_2016postVFP, 'Tprime_tAq_900_MH175_LH_2016postVFP':Tprime_tAq_900_MH175_LH_2016postVFP, 'Tprime_tAq_900_MH200_LH_2016postVFP':Tprime_tAq_900_MH200_LH_2016postVFP, 'Tprime_tAq_900_MH250_LH_2016postVFP':Tprime_tAq_900_MH250_LH_2016postVFP, 'Tprime_tAq_900_MH350_LH_2016postVFP':Tprime_tAq_900_MH350_LH_2016postVFP, 'Tprime_tAq_900_MH450_LH_2016postVFP':Tprime_tAq_900_MH450_LH_2016postVFP, 'Tprime_tAq_900_MH500_LH_2016postVFP':Tprime_tAq_900_MH500_LH_2016postVFP, 'Tprime_tAq_1000_MH25_LH_2016postVFP':Tprime_tAq_1000_MH25_LH_2016postVFP, 'Tprime_tAq_1000_MH50_LH_2016postVFP':Tprime_tAq_1000_MH50_LH_2016postVFP, 'Tprime_tAq_1000_MH75_LH_2016postVFP':Tprime_tAq_1000_MH75_LH_2016postVFP, 'Tprime_tAq_1000_MH100_LH_2016postVFP':Tprime_tAq_1000_MH100_LH_2016postVFP, 'Tprime_tAq_1000_MH125_LH_2016postVFP':Tprime_tAq_1000_MH125_LH_2016postVFP, 'Tprime_tAq_1000_MH150_LH_2016postVFP':Tprime_tAq_1000_MH150_LH_2016postVFP, 'Tprime_tAq_1000_MH175_LH_2016postVFP':Tprime_tAq_1000_MH175_LH_2016postVFP, 'Tprime_tAq_1000_MH200_LH_2016postVFP':Tprime_tAq_1000_MH200_LH_2016postVFP, 'Tprime_tAq_1000_MH250_LH_2016postVFP':Tprime_tAq_1000_MH250_LH_2016postVFP, 'Tprime_tAq_1000_MH350_LH_2016postVFP':Tprime_tAq_1000_MH350_LH_2016postVFP, 'Tprime_tAq_1000_MH450_LH_2016postVFP':Tprime_tAq_1000_MH450_LH_2016postVFP, 'Tprime_tAq_1000_MH500_LH_2016postVFP':Tprime_tAq_1000_MH500_LH_2016postVFP, 'Tprime_tAq_1100_MH25_LH_2016postVFP':Tprime_tAq_1100_MH25_LH_2016postVFP, 'Tprime_tAq_1100_MH50_LH_2016postVFP':Tprime_tAq_1100_MH50_LH_2016postVFP, 'Tprime_tAq_1100_MH75_LH_2016postVFP':Tprime_tAq_1100_MH75_LH_2016postVFP, 'Tprime_tAq_1100_MH100_LH_2016postVFP':Tprime_tAq_1100_MH100_LH_2016postVFP, 'Tprime_tAq_1100_MH125_LH_2016postVFP':Tprime_tAq_1100_MH125_LH_2016postVFP, 'Tprime_tAq_1100_MH150_LH_2016postVFP':Tprime_tAq_1100_MH150_LH_2016postVFP, 'Tprime_tAq_1100_MH175_LH_2016postVFP':Tprime_tAq_1100_MH175_LH_2016postVFP, 'Tprime_tAq_1100_MH200_LH_2016postVFP':Tprime_tAq_1100_MH200_LH_2016postVFP, 'Tprime_tAq_1100_MH250_LH_2016postVFP':Tprime_tAq_1100_MH250_LH_2016postVFP, 'Tprime_tAq_1100_MH350_LH_2016postVFP':Tprime_tAq_1100_MH350_LH_2016postVFP, 'Tprime_tAq_1100_MH450_LH_2016postVFP':Tprime_tAq_1100_MH450_LH_2016postVFP, 'Tprime_tAq_1100_MH500_LH_2016postVFP':Tprime_tAq_1100_MH500_LH_2016postVFP, 'Tprime_tAq_1200_MH25_LH_2016postVFP':Tprime_tAq_1200_MH25_LH_2016postVFP, 'Tprime_tAq_1200_MH50_LH_2016postVFP':Tprime_tAq_1200_MH50_LH_2016postVFP, 'Tprime_tAq_1200_MH75_LH_2016postVFP':Tprime_tAq_1200_MH75_LH_2016postVFP, 'Tprime_tAq_1200_MH100_LH_2016postVFP':Tprime_tAq_1200_MH100_LH_2016postVFP, 'Tprime_tAq_1200_MH125_LH_2016postVFP':Tprime_tAq_1200_MH125_LH_2016postVFP, 'Tprime_tAq_1200_MH150_LH_2016postVFP':Tprime_tAq_1200_MH150_LH_2016postVFP, 'Tprime_tAq_1200_MH175_LH_2016postVFP':Tprime_tAq_1200_MH175_LH_2016postVFP, 'Tprime_tAq_1200_MH200_LH_2016postVFP':Tprime_tAq_1200_MH200_LH_2016postVFP, 'Tprime_tAq_1200_MH250_LH_2016postVFP':Tprime_tAq_1200_MH250_LH_2016postVFP, 'Tprime_tAq_1200_MH350_LH_2016postVFP':Tprime_tAq_1200_MH350_LH_2016postVFP, 'Tprime_tAq_1200_MH450_LH_2016postVFP':Tprime_tAq_1200_MH450_LH_2016postVFP, 'Tprime_tAq_1200_MH500_LH_2016postVFP':Tprime_tAq_1200_MH500_LH_2016postVFP, 'Tprime_tAq_1300_MH25_LH_2016postVFP':Tprime_tAq_1300_MH25_LH_2016postVFP, 'Tprime_tAq_1300_MH50_LH_2016postVFP':Tprime_tAq_1300_MH50_LH_2016postVFP, 'Tprime_tAq_1300_MH75_LH_2016postVFP':Tprime_tAq_1300_MH75_LH_2016postVFP, 'Tprime_tAq_1300_MH100_LH_2016postVFP':Tprime_tAq_1300_MH100_LH_2016postVFP, 'Tprime_tAq_1300_MH125_LH_2016postVFP':Tprime_tAq_1300_MH125_LH_2016postVFP, 'Tprime_tAq_1300_MH150_LH_2016postVFP':Tprime_tAq_1300_MH150_LH_2016postVFP, 'Tprime_tAq_1300_MH175_LH_2016postVFP':Tprime_tAq_1300_MH175_LH_2016postVFP, 'Tprime_tAq_1300_MH200_LH_2016postVFP':Tprime_tAq_1300_MH200_LH_2016postVFP, 'Tprime_tAq_1300_MH250_LH_2016postVFP':Tprime_tAq_1300_MH250_LH_2016postVFP, 'Tprime_tAq_1300_MH350_LH_2016postVFP':Tprime_tAq_1300_MH350_LH_2016postVFP, 'Tprime_tAq_1300_MH450_LH_2016postVFP':Tprime_tAq_1300_MH450_LH_2016postVFP, 'Tprime_tAq_1300_MH500_LH_2016postVFP':Tprime_tAq_1300_MH500_LH_2016postVFP, 'Tprime_tAq_1400_MH25_LH_2016postVFP':Tprime_tAq_1400_MH25_LH_2016postVFP, 'Tprime_tAq_1400_MH50_LH_2016postVFP':Tprime_tAq_1400_MH50_LH_2016postVFP, 'Tprime_tAq_1400_MH75_LH_2016postVFP':Tprime_tAq_1400_MH75_LH_2016postVFP, 'Tprime_tAq_1400_MH100_LH_2016postVFP':Tprime_tAq_1400_MH100_LH_2016postVFP, 'Tprime_tAq_1400_MH125_LH_2016postVFP':Tprime_tAq_1400_MH125_LH_2016postVFP, 'Tprime_tAq_1400_MH150_LH_2016postVFP':Tprime_tAq_1400_MH150_LH_2016postVFP, 'Tprime_tAq_1400_MH175_LH_2016postVFP':Tprime_tAq_1400_MH175_LH_2016postVFP, 'Tprime_tAq_1400_MH200_LH_2016postVFP':Tprime_tAq_1400_MH200_LH_2016postVFP, 'Tprime_tAq_1400_MH250_LH_2016postVFP':Tprime_tAq_1400_MH250_LH_2016postVFP, 'Tprime_tAq_1400_MH350_LH_2016postVFP':Tprime_tAq_1400_MH350_LH_2016postVFP, 'Tprime_tAq_1400_MH450_LH_2016postVFP':Tprime_tAq_1400_MH450_LH_2016postVFP, 'Tprime_tAq_1400_MH500_LH_2016postVFP':Tprime_tAq_1400_MH500_LH_2016postVFP, 'Tprime_tAq_1500_MH25_LH_2016postVFP':Tprime_tAq_1500_MH25_LH_2016postVFP, 'Tprime_tAq_1500_MH50_LH_2016postVFP':Tprime_tAq_1500_MH50_LH_2016postVFP, 'Tprime_tAq_1500_MH75_LH_2016postVFP':Tprime_tAq_1500_MH75_LH_2016postVFP, 'Tprime_tAq_1500_MH100_LH_2016postVFP':Tprime_tAq_1500_MH100_LH_2016postVFP, 'Tprime_tAq_1500_MH125_LH_2016postVFP':Tprime_tAq_1500_MH125_LH_2016postVFP, 'Tprime_tAq_1500_MH150_LH_2016postVFP':Tprime_tAq_1500_MH150_LH_2016postVFP, 'Tprime_tAq_1500_MH175_LH_2016postVFP':Tprime_tAq_1500_MH175_LH_2016postVFP, 'Tprime_tAq_1500_MH200_LH_2016postVFP':Tprime_tAq_1500_MH200_LH_2016postVFP, 'Tprime_tAq_1500_MH250_LH_2016postVFP':Tprime_tAq_1500_MH250_LH_2016postVFP, 'Tprime_tAq_1500_MH350_LH_2016postVFP':Tprime_tAq_1500_MH350_LH_2016postVFP, 'Tprime_tAq_1500_MH450_LH_2016postVFP':Tprime_tAq_1500_MH450_LH_2016postVFP, 'Tprime_tAq_1500_MH500_LH_2016postVFP':Tprime_tAq_1500_MH500_LH_2016postVFP, 'Tprime_tAq_1600_MH25_LH_2016postVFP':Tprime_tAq_1600_MH25_LH_2016postVFP, 'Tprime_tAq_1600_MH50_LH_2016postVFP':Tprime_tAq_1600_MH50_LH_2016postVFP, 'Tprime_tAq_1600_MH75_LH_2016postVFP':Tprime_tAq_1600_MH75_LH_2016postVFP, 'Tprime_tAq_1600_MH100_LH_2016postVFP':Tprime_tAq_1600_MH100_LH_2016postVFP, 'Tprime_tAq_1600_MH125_LH_2016postVFP':Tprime_tAq_1600_MH125_LH_2016postVFP, 'Tprime_tAq_1600_MH150_LH_2016postVFP':Tprime_tAq_1600_MH150_LH_2016postVFP, 'Tprime_tAq_1600_MH175_LH_2016postVFP':Tprime_tAq_1600_MH175_LH_2016postVFP, 'Tprime_tAq_1600_MH200_LH_2016postVFP':Tprime_tAq_1600_MH200_LH_2016postVFP, 'Tprime_tAq_1600_MH250_LH_2016postVFP':Tprime_tAq_1600_MH250_LH_2016postVFP, 'Tprime_tAq_1600_MH350_LH_2016postVFP':Tprime_tAq_1600_MH350_LH_2016postVFP, 'Tprime_tAq_1600_MH450_LH_2016postVFP':Tprime_tAq_1600_MH450_LH_2016postVFP, 'Tprime_tAq_1600_MH500_LH_2016postVFP':Tprime_tAq_1600_MH500_LH_2016postVFP, 'Tprime_tAq_1700_MH25_LH_2016postVFP':Tprime_tAq_1700_MH25_LH_2016postVFP, 'Tprime_tAq_1700_MH50_LH_2016postVFP':Tprime_tAq_1700_MH50_LH_2016postVFP, 'Tprime_tAq_1700_MH75_LH_2016postVFP':Tprime_tAq_1700_MH75_LH_2016postVFP, 'Tprime_tAq_1700_MH100_LH_2016postVFP':Tprime_tAq_1700_MH100_LH_2016postVFP, 'Tprime_tAq_1700_MH125_LH_2016postVFP':Tprime_tAq_1700_MH125_LH_2016postVFP, 'Tprime_tAq_1700_MH150_LH_2016postVFP':Tprime_tAq_1700_MH150_LH_2016postVFP, 'Tprime_tAq_1700_MH175_LH_2016postVFP':Tprime_tAq_1700_MH175_LH_2016postVFP, 'Tprime_tAq_1700_MH200_LH_2016postVFP':Tprime_tAq_1700_MH200_LH_2016postVFP, 'Tprime_tAq_1700_MH250_LH_2016postVFP':Tprime_tAq_1700_MH250_LH_2016postVFP, 'Tprime_tAq_1700_MH350_LH_2016postVFP':Tprime_tAq_1700_MH350_LH_2016postVFP, 'Tprime_tAq_1700_MH450_LH_2016postVFP':Tprime_tAq_1700_MH450_LH_2016postVFP, 'Tprime_tAq_1700_MH500_LH_2016postVFP':Tprime_tAq_1700_MH500_LH_2016postVFP, 'Tprime_tAq_1800_MH25_LH_2016postVFP':Tprime_tAq_1800_MH25_LH_2016postVFP, 'Tprime_tAq_1800_MH50_LH_2016postVFP':Tprime_tAq_1800_MH50_LH_2016postVFP, 'Tprime_tAq_1800_MH75_LH_2016postVFP':Tprime_tAq_1800_MH75_LH_2016postVFP, 'Tprime_tAq_1800_MH100_LH_2016postVFP':Tprime_tAq_1800_MH100_LH_2016postVFP, 'Tprime_tAq_1800_MH125_LH_2016postVFP':Tprime_tAq_1800_MH125_LH_2016postVFP, 'Tprime_tAq_1800_MH150_LH_2016postVFP':Tprime_tAq_1800_MH150_LH_2016postVFP, 'Tprime_tAq_1800_MH175_LH_2016postVFP':Tprime_tAq_1800_MH175_LH_2016postVFP, 'Tprime_tAq_1800_MH200_LH_2016postVFP':Tprime_tAq_1800_MH200_LH_2016postVFP, 'Tprime_tAq_1800_MH250_LH_2016postVFP':Tprime_tAq_1800_MH250_LH_2016postVFP, 'Tprime_tAq_1800_MH350_LH_2016postVFP':Tprime_tAq_1800_MH350_LH_2016postVFP, 'Tprime_tAq_1800_MH450_LH_2016postVFP':Tprime_tAq_1800_MH450_LH_2016postVFP, 'Tprime_tAq_1800_MH500_LH_2016postVFP':Tprime_tAq_1800_MH500_LH_2016postVFP, 'Tprime_tAq_1900_MH25_LH_2016postVFP':Tprime_tAq_1900_MH25_LH_2016postVFP, 'Tprime_tAq_1900_MH50_LH_2016postVFP':Tprime_tAq_1900_MH50_LH_2016postVFP, 'Tprime_tAq_1900_MH75_LH_2016postVFP':Tprime_tAq_1900_MH75_LH_2016postVFP, 'Tprime_tAq_1900_MH100_LH_2016postVFP':Tprime_tAq_1900_MH100_LH_2016postVFP, 'Tprime_tAq_1900_MH125_LH_2016postVFP':Tprime_tAq_1900_MH125_LH_2016postVFP, 'Tprime_tAq_1900_MH150_LH_2016postVFP':Tprime_tAq_1900_MH150_LH_2016postVFP, 'Tprime_tAq_1900_MH175_LH_2016postVFP':Tprime_tAq_1900_MH175_LH_2016postVFP, 'Tprime_tAq_1900_MH200_LH_2016postVFP':Tprime_tAq_1900_MH200_LH_2016postVFP, 'Tprime_tAq_1900_MH250_LH_2016postVFP':Tprime_tAq_1900_MH250_LH_2016postVFP, 'Tprime_tAq_1900_MH350_LH_2016postVFP':Tprime_tAq_1900_MH350_LH_2016postVFP, 'Tprime_tAq_1900_MH450_LH_2016postVFP':Tprime_tAq_1900_MH450_LH_2016postVFP, 'Tprime_tAq_1900_MH500_LH_2016postVFP':Tprime_tAq_1900_MH500_LH_2016postVFP, 'Tprime_tAq_2000_MH25_LH_2016postVFP':Tprime_tAq_2000_MH25_LH_2016postVFP, 'Tprime_tAq_2000_MH50_LH_2016postVFP':Tprime_tAq_2000_MH50_LH_2016postVFP, 'Tprime_tAq_2000_MH75_LH_2016postVFP':Tprime_tAq_2000_MH75_LH_2016postVFP, 'Tprime_tAq_2000_MH100_LH_2016postVFP':Tprime_tAq_2000_MH100_LH_2016postVFP, 'Tprime_tAq_2000_MH125_LH_2016postVFP':Tprime_tAq_2000_MH125_LH_2016postVFP, 'Tprime_tAq_2000_MH150_LH_2016postVFP':Tprime_tAq_2000_MH150_LH_2016postVFP, 'Tprime_tAq_2000_MH175_LH_2016postVFP':Tprime_tAq_2000_MH175_LH_2016postVFP, 'Tprime_tAq_2000_MH200_LH_2016postVFP':Tprime_tAq_2000_MH200_LH_2016postVFP, 'Tprime_tAq_2000_MH250_LH_2016postVFP':Tprime_tAq_2000_MH250_LH_2016postVFP, 'Tprime_tAq_2000_MH350_LH_2016postVFP':Tprime_tAq_2000_MH350_LH_2016postVFP, 'Tprime_tAq_2000_MH450_LH_2016postVFP':Tprime_tAq_2000_MH450_LH_2016postVFP, 'Tprime_tAq_2000_MH500_LH_2016postVFP':Tprime_tAq_2000_MH500_LH_2016postVFP, 'Tprime_tAq_2100_MH25_LH_2016postVFP':Tprime_tAq_2100_MH25_LH_2016postVFP, 'Tprime_tAq_2100_MH50_LH_2016postVFP':Tprime_tAq_2100_MH50_LH_2016postVFP, 'Tprime_tAq_2100_MH75_LH_2016postVFP':Tprime_tAq_2100_MH75_LH_2016postVFP, 'Tprime_tAq_2100_MH100_LH_2016postVFP':Tprime_tAq_2100_MH100_LH_2016postVFP, 'Tprime_tAq_2100_MH125_LH_2016postVFP':Tprime_tAq_2100_MH125_LH_2016postVFP, 'Tprime_tAq_2100_MH150_LH_2016postVFP':Tprime_tAq_2100_MH150_LH_2016postVFP, 'Tprime_tAq_2100_MH175_LH_2016postVFP':Tprime_tAq_2100_MH175_LH_2016postVFP, 'Tprime_tAq_2100_MH200_LH_2016postVFP':Tprime_tAq_2100_MH200_LH_2016postVFP, 'Tprime_tAq_2100_MH250_LH_2016postVFP':Tprime_tAq_2100_MH250_LH_2016postVFP, 'Tprime_tAq_2100_MH350_LH_2016postVFP':Tprime_tAq_2100_MH350_LH_2016postVFP, 'Tprime_tAq_2100_MH450_LH_2016postVFP':Tprime_tAq_2100_MH450_LH_2016postVFP, 'Tprime_tAq_2100_MH500_LH_2016postVFP':Tprime_tAq_2100_MH500_LH_2016postVFP, 'Tprime_tAq_2200_MH25_LH_2016postVFP':Tprime_tAq_2200_MH25_LH_2016postVFP, 'Tprime_tAq_2200_MH50_LH_2016postVFP':Tprime_tAq_2200_MH50_LH_2016postVFP, 'Tprime_tAq_2200_MH75_LH_2016postVFP':Tprime_tAq_2200_MH75_LH_2016postVFP, 'Tprime_tAq_2200_MH100_LH_2016postVFP':Tprime_tAq_2200_MH100_LH_2016postVFP, 'Tprime_tAq_2200_MH125_LH_2016postVFP':Tprime_tAq_2200_MH125_LH_2016postVFP, 'Tprime_tAq_2200_MH150_LH_2016postVFP':Tprime_tAq_2200_MH150_LH_2016postVFP, 'Tprime_tAq_2200_MH175_LH_2016postVFP':Tprime_tAq_2200_MH175_LH_2016postVFP, 'Tprime_tAq_2200_MH200_LH_2016postVFP':Tprime_tAq_2200_MH200_LH_2016postVFP, 'Tprime_tAq_2200_MH250_LH_2016postVFP':Tprime_tAq_2200_MH250_LH_2016postVFP, 'Tprime_tAq_2200_MH350_LH_2016postVFP':Tprime_tAq_2200_MH350_LH_2016postVFP, 'Tprime_tAq_2200_MH450_LH_2016postVFP':Tprime_tAq_2200_MH450_LH_2016postVFP, 'Tprime_tAq_2200_MH500_LH_2016postVFP':Tprime_tAq_2200_MH500_LH_2016postVFP, 'Tprime_tAq_2300_MH25_LH_2016postVFP':Tprime_tAq_2300_MH25_LH_2016postVFP, 'Tprime_tAq_2300_MH50_LH_2016postVFP':Tprime_tAq_2300_MH50_LH_2016postVFP, 'Tprime_tAq_2300_MH75_LH_2016postVFP':Tprime_tAq_2300_MH75_LH_2016postVFP, 'Tprime_tAq_2300_MH100_LH_2016postVFP':Tprime_tAq_2300_MH100_LH_2016postVFP, 'Tprime_tAq_2300_MH125_LH_2016postVFP':Tprime_tAq_2300_MH125_LH_2016postVFP, 'Tprime_tAq_2300_MH150_LH_2016postVFP':Tprime_tAq_2300_MH150_LH_2016postVFP, 'Tprime_tAq_2300_MH175_LH_2016postVFP':Tprime_tAq_2300_MH175_LH_2016postVFP, 'Tprime_tAq_2300_MH200_LH_2016postVFP':Tprime_tAq_2300_MH200_LH_2016postVFP, 'Tprime_tAq_2300_MH250_LH_2016postVFP':Tprime_tAq_2300_MH250_LH_2016postVFP, 'Tprime_tAq_2300_MH350_LH_2016postVFP':Tprime_tAq_2300_MH350_LH_2016postVFP, 'Tprime_tAq_2300_MH450_LH_2016postVFP':Tprime_tAq_2300_MH450_LH_2016postVFP, 'Tprime_tAq_2300_MH500_LH_2016postVFP':Tprime_tAq_2300_MH500_LH_2016postVFP, 'Tprime_tAq_2400_MH25_LH_2016postVFP':Tprime_tAq_2400_MH25_LH_2016postVFP, 'Tprime_tAq_2400_MH50_LH_2016postVFP':Tprime_tAq_2400_MH50_LH_2016postVFP, 'Tprime_tAq_2400_MH75_LH_2016postVFP':Tprime_tAq_2400_MH75_LH_2016postVFP, 'Tprime_tAq_2400_MH100_LH_2016postVFP':Tprime_tAq_2400_MH100_LH_2016postVFP, 'Tprime_tAq_2400_MH125_LH_2016postVFP':Tprime_tAq_2400_MH125_LH_2016postVFP, 'Tprime_tAq_2400_MH150_LH_2016postVFP':Tprime_tAq_2400_MH150_LH_2016postVFP, 'Tprime_tAq_2400_MH175_LH_2016postVFP':Tprime_tAq_2400_MH175_LH_2016postVFP, 'Tprime_tAq_2400_MH200_LH_2016postVFP':Tprime_tAq_2400_MH200_LH_2016postVFP, 'Tprime_tAq_2400_MH250_LH_2016postVFP':Tprime_tAq_2400_MH250_LH_2016postVFP, 'Tprime_tAq_2400_MH350_LH_2016postVFP':Tprime_tAq_2400_MH350_LH_2016postVFP, 'Tprime_tAq_2400_MH450_LH_2016postVFP':Tprime_tAq_2400_MH450_LH_2016postVFP, 'Tprime_tAq_2400_MH500_LH_2016postVFP':Tprime_tAq_2400_MH500_LH_2016postVFP, 'Tprime_tAq_2500_MH25_LH_2016postVFP':Tprime_tAq_2500_MH25_LH_2016postVFP, 'Tprime_tAq_2500_MH50_LH_2016postVFP':Tprime_tAq_2500_MH50_LH_2016postVFP, 'Tprime_tAq_2500_MH75_LH_2016postVFP':Tprime_tAq_2500_MH75_LH_2016postVFP, 'Tprime_tAq_2500_MH100_LH_2016postVFP':Tprime_tAq_2500_MH100_LH_2016postVFP, 'Tprime_tAq_2500_MH125_LH_2016postVFP':Tprime_tAq_2500_MH125_LH_2016postVFP, 'Tprime_tAq_2500_MH150_LH_2016postVFP':Tprime_tAq_2500_MH150_LH_2016postVFP, 'Tprime_tAq_2500_MH175_LH_2016postVFP':Tprime_tAq_2500_MH175_LH_2016postVFP, 'Tprime_tAq_2500_MH200_LH_2016postVFP':Tprime_tAq_2500_MH200_LH_2016postVFP, 'Tprime_tAq_2500_MH250_LH_2016postVFP':Tprime_tAq_2500_MH250_LH_2016postVFP, 'Tprime_tAq_2500_MH350_LH_2016postVFP':Tprime_tAq_2500_MH350_LH_2016postVFP, 'Tprime_tAq_2500_MH450_LH_2016postVFP':Tprime_tAq_2500_MH450_LH_2016postVFP, 'Tprime_tAq_2500_MH500_LH_2016postVFP':Tprime_tAq_2500_MH500_LH_2016postVFP, 'Tprime_tAq_2600_MH25_LH_2016postVFP':Tprime_tAq_2600_MH25_LH_2016postVFP, 'Tprime_tAq_2600_MH50_LH_2016postVFP':Tprime_tAq_2600_MH50_LH_2016postVFP, 'Tprime_tAq_2600_MH75_LH_2016postVFP':Tprime_tAq_2600_MH75_LH_2016postVFP, 'Tprime_tAq_2600_MH100_LH_2016postVFP':Tprime_tAq_2600_MH100_LH_2016postVFP, 'Tprime_tAq_2600_MH125_LH_2016postVFP':Tprime_tAq_2600_MH125_LH_2016postVFP, 'Tprime_tAq_2600_MH150_LH_2016postVFP':Tprime_tAq_2600_MH150_LH_2016postVFP, 'Tprime_tAq_2600_MH175_LH_2016postVFP':Tprime_tAq_2600_MH175_LH_2016postVFP, 'Tprime_tAq_2600_MH200_LH_2016postVFP':Tprime_tAq_2600_MH200_LH_2016postVFP, 'Tprime_tAq_2600_MH250_LH_2016postVFP':Tprime_tAq_2600_MH250_LH_2016postVFP, 'Tprime_tAq_2600_MH350_LH_2016postVFP':Tprime_tAq_2600_MH350_LH_2016postVFP, 'Tprime_tAq_2600_MH450_LH_2016postVFP':Tprime_tAq_2600_MH450_LH_2016postVFP, 'Tprime_tAq_2600_MH500_LH_2016postVFP':Tprime_tAq_2600_MH500_LH_2016postVFP, 'Tprime_tAq_2700_MH25_LH_2016postVFP':Tprime_tAq_2700_MH25_LH_2016postVFP, 'Tprime_tAq_2700_MH50_LH_2016postVFP':Tprime_tAq_2700_MH50_LH_2016postVFP, 'Tprime_tAq_2700_MH75_LH_2016postVFP':Tprime_tAq_2700_MH75_LH_2016postVFP, 'Tprime_tAq_2700_MH100_LH_2016postVFP':Tprime_tAq_2700_MH100_LH_2016postVFP, 'Tprime_tAq_2700_MH125_LH_2016postVFP':Tprime_tAq_2700_MH125_LH_2016postVFP, 'Tprime_tAq_2700_MH150_LH_2016postVFP':Tprime_tAq_2700_MH150_LH_2016postVFP, 'Tprime_tAq_2700_MH175_LH_2016postVFP':Tprime_tAq_2700_MH175_LH_2016postVFP, 'Tprime_tAq_2700_MH200_LH_2016postVFP':Tprime_tAq_2700_MH200_LH_2016postVFP, 'Tprime_tAq_2700_MH250_LH_2016postVFP':Tprime_tAq_2700_MH250_LH_2016postVFP, 'Tprime_tAq_2700_MH350_LH_2016postVFP':Tprime_tAq_2700_MH350_LH_2016postVFP, 'Tprime_tAq_2700_MH450_LH_2016postVFP':Tprime_tAq_2700_MH450_LH_2016postVFP, 'Tprime_tAq_2700_MH500_LH_2016postVFP':Tprime_tAq_2700_MH500_LH_2016postVFP, 'Tprime_tAq_2800_MH25_LH_2016postVFP':Tprime_tAq_2800_MH25_LH_2016postVFP, 'Tprime_tAq_2800_MH50_LH_2016postVFP':Tprime_tAq_2800_MH50_LH_2016postVFP, 'Tprime_tAq_2800_MH75_LH_2016postVFP':Tprime_tAq_2800_MH75_LH_2016postVFP, 'Tprime_tAq_2800_MH100_LH_2016postVFP':Tprime_tAq_2800_MH100_LH_2016postVFP, 'Tprime_tAq_2800_MH125_LH_2016postVFP':Tprime_tAq_2800_MH125_LH_2016postVFP, 'Tprime_tAq_2800_MH150_LH_2016postVFP':Tprime_tAq_2800_MH150_LH_2016postVFP, 'Tprime_tAq_2800_MH175_LH_2016postVFP':Tprime_tAq_2800_MH175_LH_2016postVFP, 'Tprime_tAq_2800_MH200_LH_2016postVFP':Tprime_tAq_2800_MH200_LH_2016postVFP, 'Tprime_tAq_2800_MH250_LH_2016postVFP':Tprime_tAq_2800_MH250_LH_2016postVFP, 'Tprime_tAq_2800_MH350_LH_2016postVFP':Tprime_tAq_2800_MH350_LH_2016postVFP, 'Tprime_tAq_2800_MH450_LH_2016postVFP':Tprime_tAq_2800_MH450_LH_2016postVFP, 'Tprime_tAq_2800_MH500_LH_2016postVFP':Tprime_tAq_2800_MH500_LH_2016postVFP, 'Tprime_tAq_2900_MH25_LH_2016postVFP':Tprime_tAq_2900_MH25_LH_2016postVFP, 'Tprime_tAq_2900_MH50_LH_2016postVFP':Tprime_tAq_2900_MH50_LH_2016postVFP, 'Tprime_tAq_2900_MH75_LH_2016postVFP':Tprime_tAq_2900_MH75_LH_2016postVFP, 'Tprime_tAq_2900_MH100_LH_2016postVFP':Tprime_tAq_2900_MH100_LH_2016postVFP, 'Tprime_tAq_2900_MH125_LH_2016postVFP':Tprime_tAq_2900_MH125_LH_2016postVFP, 'Tprime_tAq_2900_MH150_LH_2016postVFP':Tprime_tAq_2900_MH150_LH_2016postVFP, 'Tprime_tAq_2900_MH175_LH_2016postVFP':Tprime_tAq_2900_MH175_LH_2016postVFP, 'Tprime_tAq_2900_MH200_LH_2016postVFP':Tprime_tAq_2900_MH200_LH_2016postVFP, 'Tprime_tAq_2900_MH250_LH_2016postVFP':Tprime_tAq_2900_MH250_LH_2016postVFP, 'Tprime_tAq_2900_MH350_LH_2016postVFP':Tprime_tAq_2900_MH350_LH_2016postVFP, 'Tprime_tAq_2900_MH450_LH_2016postVFP':Tprime_tAq_2900_MH450_LH_2016postVFP, 'Tprime_tAq_2900_MH500_LH_2016postVFP':Tprime_tAq_2900_MH500_LH_2016postVFP, 'Tprime_tAq_3000_MH25_LH_2016postVFP':Tprime_tAq_3000_MH25_LH_2016postVFP, 'Tprime_tAq_3000_MH50_LH_2016postVFP':Tprime_tAq_3000_MH50_LH_2016postVFP, 'Tprime_tAq_3000_MH75_LH_2016postVFP':Tprime_tAq_3000_MH75_LH_2016postVFP, 'Tprime_tAq_3000_MH100_LH_2016postVFP':Tprime_tAq_3000_MH100_LH_2016postVFP, 'Tprime_tAq_3000_MH125_LH_2016postVFP':Tprime_tAq_3000_MH125_LH_2016postVFP, 'Tprime_tAq_3000_MH150_LH_2016postVFP':Tprime_tAq_3000_MH150_LH_2016postVFP, 'Tprime_tAq_3000_MH175_LH_2016postVFP':Tprime_tAq_3000_MH175_LH_2016postVFP, 'Tprime_tAq_3000_MH200_LH_2016postVFP':Tprime_tAq_3000_MH200_LH_2016postVFP, 'Tprime_tAq_3000_MH250_LH_2016postVFP':Tprime_tAq_3000_MH250_LH_2016postVFP, 'Tprime_tAq_3000_MH350_LH_2016postVFP':Tprime_tAq_3000_MH350_LH_2016postVFP, 'Tprime_tAq_3000_MH450_LH_2016postVFP':Tprime_tAq_3000_MH450_LH_2016postVFP, 'Tprime_tAq_3000_MH500_LH_2016postVFP':Tprime_tAq_3000_MH500_LH_2016postVFP, 'Tprime_tAq_600_MH25_LH_2017':Tprime_tAq_600_MH25_LH_2017, 'Tprime_tAq_600_MH50_LH_2017':Tprime_tAq_600_MH50_LH_2017, 'Tprime_tAq_600_MH75_LH_2017':Tprime_tAq_600_MH75_LH_2017, 'Tprime_tAq_600_MH100_LH_2017':Tprime_tAq_600_MH100_LH_2017, 'Tprime_tAq_600_MH125_LH_2017':Tprime_tAq_600_MH125_LH_2017, 'Tprime_tAq_600_MH150_LH_2017':Tprime_tAq_600_MH150_LH_2017, 'Tprime_tAq_600_MH175_LH_2017':Tprime_tAq_600_MH175_LH_2017, 'Tprime_tAq_600_MH200_LH_2017':Tprime_tAq_600_MH200_LH_2017, 'Tprime_tAq_600_MH250_LH_2017':Tprime_tAq_600_MH250_LH_2017, 'Tprime_tAq_600_MH350_LH_2017':Tprime_tAq_600_MH350_LH_2017, 'Tprime_tAq_600_MH450_LH_2017':Tprime_tAq_600_MH450_LH_2017, 'Tprime_tAq_600_MH500_LH_2017':Tprime_tAq_600_MH500_LH_2017, 'Tprime_tAq_700_MH25_LH_2017':Tprime_tAq_700_MH25_LH_2017, 'Tprime_tAq_700_MH50_LH_2017':Tprime_tAq_700_MH50_LH_2017, 'Tprime_tAq_700_MH75_LH_2017':Tprime_tAq_700_MH75_LH_2017, 'Tprime_tAq_700_MH100_LH_2017':Tprime_tAq_700_MH100_LH_2017, 'Tprime_tAq_700_MH125_LH_2017':Tprime_tAq_700_MH125_LH_2017, 'Tprime_tAq_700_MH150_LH_2017':Tprime_tAq_700_MH150_LH_2017, 'Tprime_tAq_700_MH175_LH_2017':Tprime_tAq_700_MH175_LH_2017, 'Tprime_tAq_700_MH200_LH_2017':Tprime_tAq_700_MH200_LH_2017, 'Tprime_tAq_700_MH250_LH_2017':Tprime_tAq_700_MH250_LH_2017, 'Tprime_tAq_700_MH350_LH_2017':Tprime_tAq_700_MH350_LH_2017, 'Tprime_tAq_700_MH450_LH_2017':Tprime_tAq_700_MH450_LH_2017, 'Tprime_tAq_700_MH500_LH_2017':Tprime_tAq_700_MH500_LH_2017, 'Tprime_tAq_800_MH25_LH_2017':Tprime_tAq_800_MH25_LH_2017, 'Tprime_tAq_800_MH50_LH_2017':Tprime_tAq_800_MH50_LH_2017, 'Tprime_tAq_800_MH75_LH_2017':Tprime_tAq_800_MH75_LH_2017, 'Tprime_tAq_800_MH100_LH_2017':Tprime_tAq_800_MH100_LH_2017, 'Tprime_tAq_800_MH125_LH_2017':Tprime_tAq_800_MH125_LH_2017, 'Tprime_tAq_800_MH150_LH_2017':Tprime_tAq_800_MH150_LH_2017, 'Tprime_tAq_800_MH175_LH_2017':Tprime_tAq_800_MH175_LH_2017, 'Tprime_tAq_800_MH200_LH_2017':Tprime_tAq_800_MH200_LH_2017, 'Tprime_tAq_800_MH250_LH_2017':Tprime_tAq_800_MH250_LH_2017, 'Tprime_tAq_800_MH350_LH_2017':Tprime_tAq_800_MH350_LH_2017, 'Tprime_tAq_800_MH450_LH_2017':Tprime_tAq_800_MH450_LH_2017, 'Tprime_tAq_800_MH500_LH_2017':Tprime_tAq_800_MH500_LH_2017, 'Tprime_tAq_900_MH25_LH_2017':Tprime_tAq_900_MH25_LH_2017, 'Tprime_tAq_900_MH50_LH_2017':Tprime_tAq_900_MH50_LH_2017, 'Tprime_tAq_900_MH75_LH_2017':Tprime_tAq_900_MH75_LH_2017, 'Tprime_tAq_900_MH100_LH_2017':Tprime_tAq_900_MH100_LH_2017, 'Tprime_tAq_900_MH125_LH_2017':Tprime_tAq_900_MH125_LH_2017, 'Tprime_tAq_900_MH150_LH_2017':Tprime_tAq_900_MH150_LH_2017, 'Tprime_tAq_900_MH175_LH_2017':Tprime_tAq_900_MH175_LH_2017, 'Tprime_tAq_900_MH200_LH_2017':Tprime_tAq_900_MH200_LH_2017, 'Tprime_tAq_900_MH250_LH_2017':Tprime_tAq_900_MH250_LH_2017, 'Tprime_tAq_900_MH350_LH_2017':Tprime_tAq_900_MH350_LH_2017, 'Tprime_tAq_900_MH450_LH_2017':Tprime_tAq_900_MH450_LH_2017, 'Tprime_tAq_900_MH500_LH_2017':Tprime_tAq_900_MH500_LH_2017, 'Tprime_tAq_1000_MH25_LH_2017':Tprime_tAq_1000_MH25_LH_2017, 'Tprime_tAq_1000_MH50_LH_2017':Tprime_tAq_1000_MH50_LH_2017, 'Tprime_tAq_1000_MH75_LH_2017':Tprime_tAq_1000_MH75_LH_2017, 'Tprime_tAq_1000_MH100_LH_2017':Tprime_tAq_1000_MH100_LH_2017, 'Tprime_tAq_1000_MH125_LH_2017':Tprime_tAq_1000_MH125_LH_2017, 'Tprime_tAq_1000_MH150_LH_2017':Tprime_tAq_1000_MH150_LH_2017, 'Tprime_tAq_1000_MH175_LH_2017':Tprime_tAq_1000_MH175_LH_2017, 'Tprime_tAq_1000_MH200_LH_2017':Tprime_tAq_1000_MH200_LH_2017, 'Tprime_tAq_1000_MH250_LH_2017':Tprime_tAq_1000_MH250_LH_2017, 'Tprime_tAq_1000_MH350_LH_2017':Tprime_tAq_1000_MH350_LH_2017, 'Tprime_tAq_1000_MH450_LH_2017':Tprime_tAq_1000_MH450_LH_2017, 'Tprime_tAq_1000_MH500_LH_2017':Tprime_tAq_1000_MH500_LH_2017, 'Tprime_tAq_1100_MH25_LH_2017':Tprime_tAq_1100_MH25_LH_2017, 'Tprime_tAq_1100_MH50_LH_2017':Tprime_tAq_1100_MH50_LH_2017, 'Tprime_tAq_1100_MH75_LH_2017':Tprime_tAq_1100_MH75_LH_2017, 'Tprime_tAq_1100_MH100_LH_2017':Tprime_tAq_1100_MH100_LH_2017, 'Tprime_tAq_1100_MH125_LH_2017':Tprime_tAq_1100_MH125_LH_2017, 'Tprime_tAq_1100_MH150_LH_2017':Tprime_tAq_1100_MH150_LH_2017, 'Tprime_tAq_1100_MH175_LH_2017':Tprime_tAq_1100_MH175_LH_2017, 'Tprime_tAq_1100_MH200_LH_2017':Tprime_tAq_1100_MH200_LH_2017, 'Tprime_tAq_1100_MH250_LH_2017':Tprime_tAq_1100_MH250_LH_2017, 'Tprime_tAq_1100_MH350_LH_2017':Tprime_tAq_1100_MH350_LH_2017, 'Tprime_tAq_1100_MH450_LH_2017':Tprime_tAq_1100_MH450_LH_2017, 'Tprime_tAq_1100_MH500_LH_2017':Tprime_tAq_1100_MH500_LH_2017, 'Tprime_tAq_1200_MH25_LH_2017':Tprime_tAq_1200_MH25_LH_2017, 'Tprime_tAq_1200_MH50_LH_2017':Tprime_tAq_1200_MH50_LH_2017, 'Tprime_tAq_1200_MH75_LH_2017':Tprime_tAq_1200_MH75_LH_2017, 'Tprime_tAq_1200_MH100_LH_2017':Tprime_tAq_1200_MH100_LH_2017, 'Tprime_tAq_1200_MH125_LH_2017':Tprime_tAq_1200_MH125_LH_2017, 'Tprime_tAq_1200_MH150_LH_2017':Tprime_tAq_1200_MH150_LH_2017, 'Tprime_tAq_1200_MH175_LH_2017':Tprime_tAq_1200_MH175_LH_2017, 'Tprime_tAq_1200_MH200_LH_2017':Tprime_tAq_1200_MH200_LH_2017, 'Tprime_tAq_1200_MH250_LH_2017':Tprime_tAq_1200_MH250_LH_2017, 'Tprime_tAq_1200_MH350_LH_2017':Tprime_tAq_1200_MH350_LH_2017, 'Tprime_tAq_1200_MH450_LH_2017':Tprime_tAq_1200_MH450_LH_2017, 'Tprime_tAq_1200_MH500_LH_2017':Tprime_tAq_1200_MH500_LH_2017, 'Tprime_tAq_1300_MH25_LH_2017':Tprime_tAq_1300_MH25_LH_2017, 'Tprime_tAq_1300_MH50_LH_2017':Tprime_tAq_1300_MH50_LH_2017, 'Tprime_tAq_1300_MH75_LH_2017':Tprime_tAq_1300_MH75_LH_2017, 'Tprime_tAq_1300_MH100_LH_2017':Tprime_tAq_1300_MH100_LH_2017, 'Tprime_tAq_1300_MH125_LH_2017':Tprime_tAq_1300_MH125_LH_2017, 'Tprime_tAq_1300_MH150_LH_2017':Tprime_tAq_1300_MH150_LH_2017, 'Tprime_tAq_1300_MH175_LH_2017':Tprime_tAq_1300_MH175_LH_2017, 'Tprime_tAq_1300_MH200_LH_2017':Tprime_tAq_1300_MH200_LH_2017, 'Tprime_tAq_1300_MH250_LH_2017':Tprime_tAq_1300_MH250_LH_2017, 'Tprime_tAq_1300_MH350_LH_2017':Tprime_tAq_1300_MH350_LH_2017, 'Tprime_tAq_1300_MH450_LH_2017':Tprime_tAq_1300_MH450_LH_2017, 'Tprime_tAq_1300_MH500_LH_2017':Tprime_tAq_1300_MH500_LH_2017, 'Tprime_tAq_1400_MH25_LH_2017':Tprime_tAq_1400_MH25_LH_2017, 'Tprime_tAq_1400_MH50_LH_2017':Tprime_tAq_1400_MH50_LH_2017, 'Tprime_tAq_1400_MH75_LH_2017':Tprime_tAq_1400_MH75_LH_2017, 'Tprime_tAq_1400_MH100_LH_2017':Tprime_tAq_1400_MH100_LH_2017, 'Tprime_tAq_1400_MH125_LH_2017':Tprime_tAq_1400_MH125_LH_2017, 'Tprime_tAq_1400_MH150_LH_2017':Tprime_tAq_1400_MH150_LH_2017, 'Tprime_tAq_1400_MH175_LH_2017':Tprime_tAq_1400_MH175_LH_2017, 'Tprime_tAq_1400_MH200_LH_2017':Tprime_tAq_1400_MH200_LH_2017, 'Tprime_tAq_1400_MH250_LH_2017':Tprime_tAq_1400_MH250_LH_2017, 'Tprime_tAq_1400_MH350_LH_2017':Tprime_tAq_1400_MH350_LH_2017, 'Tprime_tAq_1400_MH450_LH_2017':Tprime_tAq_1400_MH450_LH_2017, 'Tprime_tAq_1400_MH500_LH_2017':Tprime_tAq_1400_MH500_LH_2017, 'Tprime_tAq_1500_MH25_LH_2017':Tprime_tAq_1500_MH25_LH_2017, 'Tprime_tAq_1500_MH50_LH_2017':Tprime_tAq_1500_MH50_LH_2017, 'Tprime_tAq_1500_MH75_LH_2017':Tprime_tAq_1500_MH75_LH_2017, 'Tprime_tAq_1500_MH100_LH_2017':Tprime_tAq_1500_MH100_LH_2017, 'Tprime_tAq_1500_MH125_LH_2017':Tprime_tAq_1500_MH125_LH_2017, 'Tprime_tAq_1500_MH150_LH_2017':Tprime_tAq_1500_MH150_LH_2017, 'Tprime_tAq_1500_MH175_LH_2017':Tprime_tAq_1500_MH175_LH_2017, 'Tprime_tAq_1500_MH200_LH_2017':Tprime_tAq_1500_MH200_LH_2017, 'Tprime_tAq_1500_MH250_LH_2017':Tprime_tAq_1500_MH250_LH_2017, 'Tprime_tAq_1500_MH350_LH_2017':Tprime_tAq_1500_MH350_LH_2017, 'Tprime_tAq_1500_MH450_LH_2017':Tprime_tAq_1500_MH450_LH_2017, 'Tprime_tAq_1500_MH500_LH_2017':Tprime_tAq_1500_MH500_LH_2017, 'Tprime_tAq_1600_MH25_LH_2017':Tprime_tAq_1600_MH25_LH_2017, 'Tprime_tAq_1600_MH50_LH_2017':Tprime_tAq_1600_MH50_LH_2017, 'Tprime_tAq_1600_MH75_LH_2017':Tprime_tAq_1600_MH75_LH_2017, 'Tprime_tAq_1600_MH100_LH_2017':Tprime_tAq_1600_MH100_LH_2017, 'Tprime_tAq_1600_MH125_LH_2017':Tprime_tAq_1600_MH125_LH_2017, 'Tprime_tAq_1600_MH150_LH_2017':Tprime_tAq_1600_MH150_LH_2017, 'Tprime_tAq_1600_MH175_LH_2017':Tprime_tAq_1600_MH175_LH_2017, 'Tprime_tAq_1600_MH200_LH_2017':Tprime_tAq_1600_MH200_LH_2017, 'Tprime_tAq_1600_MH250_LH_2017':Tprime_tAq_1600_MH250_LH_2017, 'Tprime_tAq_1600_MH350_LH_2017':Tprime_tAq_1600_MH350_LH_2017, 'Tprime_tAq_1600_MH450_LH_2017':Tprime_tAq_1600_MH450_LH_2017, 'Tprime_tAq_1600_MH500_LH_2017':Tprime_tAq_1600_MH500_LH_2017, 'Tprime_tAq_1700_MH25_LH_2017':Tprime_tAq_1700_MH25_LH_2017, 'Tprime_tAq_1700_MH50_LH_2017':Tprime_tAq_1700_MH50_LH_2017, 'Tprime_tAq_1700_MH75_LH_2017':Tprime_tAq_1700_MH75_LH_2017, 'Tprime_tAq_1700_MH100_LH_2017':Tprime_tAq_1700_MH100_LH_2017, 'Tprime_tAq_1700_MH125_LH_2017':Tprime_tAq_1700_MH125_LH_2017, 'Tprime_tAq_1700_MH150_LH_2017':Tprime_tAq_1700_MH150_LH_2017, 'Tprime_tAq_1700_MH175_LH_2017':Tprime_tAq_1700_MH175_LH_2017, 'Tprime_tAq_1700_MH200_LH_2017':Tprime_tAq_1700_MH200_LH_2017, 'Tprime_tAq_1700_MH250_LH_2017':Tprime_tAq_1700_MH250_LH_2017, 'Tprime_tAq_1700_MH350_LH_2017':Tprime_tAq_1700_MH350_LH_2017, 'Tprime_tAq_1700_MH450_LH_2017':Tprime_tAq_1700_MH450_LH_2017, 'Tprime_tAq_1700_MH500_LH_2017':Tprime_tAq_1700_MH500_LH_2017, 'Tprime_tAq_1800_MH25_LH_2017':Tprime_tAq_1800_MH25_LH_2017, 'Tprime_tAq_1800_MH50_LH_2017':Tprime_tAq_1800_MH50_LH_2017, 'Tprime_tAq_1800_MH75_LH_2017':Tprime_tAq_1800_MH75_LH_2017, 'Tprime_tAq_1800_MH100_LH_2017':Tprime_tAq_1800_MH100_LH_2017, 'Tprime_tAq_1800_MH125_LH_2017':Tprime_tAq_1800_MH125_LH_2017, 'Tprime_tAq_1800_MH150_LH_2017':Tprime_tAq_1800_MH150_LH_2017, 'Tprime_tAq_1800_MH175_LH_2017':Tprime_tAq_1800_MH175_LH_2017, 'Tprime_tAq_1800_MH200_LH_2017':Tprime_tAq_1800_MH200_LH_2017, 'Tprime_tAq_1800_MH250_LH_2017':Tprime_tAq_1800_MH250_LH_2017, 'Tprime_tAq_1800_MH350_LH_2017':Tprime_tAq_1800_MH350_LH_2017, 'Tprime_tAq_1800_MH450_LH_2017':Tprime_tAq_1800_MH450_LH_2017, 'Tprime_tAq_1800_MH500_LH_2017':Tprime_tAq_1800_MH500_LH_2017, 'Tprime_tAq_1900_MH25_LH_2017':Tprime_tAq_1900_MH25_LH_2017, 'Tprime_tAq_1900_MH50_LH_2017':Tprime_tAq_1900_MH50_LH_2017, 'Tprime_tAq_1900_MH75_LH_2017':Tprime_tAq_1900_MH75_LH_2017, 'Tprime_tAq_1900_MH100_LH_2017':Tprime_tAq_1900_MH100_LH_2017, 'Tprime_tAq_1900_MH125_LH_2017':Tprime_tAq_1900_MH125_LH_2017, 'Tprime_tAq_1900_MH150_LH_2017':Tprime_tAq_1900_MH150_LH_2017, 'Tprime_tAq_1900_MH175_LH_2017':Tprime_tAq_1900_MH175_LH_2017, 'Tprime_tAq_1900_MH200_LH_2017':Tprime_tAq_1900_MH200_LH_2017, 'Tprime_tAq_1900_MH250_LH_2017':Tprime_tAq_1900_MH250_LH_2017, 'Tprime_tAq_1900_MH350_LH_2017':Tprime_tAq_1900_MH350_LH_2017, 'Tprime_tAq_1900_MH450_LH_2017':Tprime_tAq_1900_MH450_LH_2017, 'Tprime_tAq_1900_MH500_LH_2017':Tprime_tAq_1900_MH500_LH_2017, 'Tprime_tAq_2000_MH25_LH_2017':Tprime_tAq_2000_MH25_LH_2017, 'Tprime_tAq_2000_MH50_LH_2017':Tprime_tAq_2000_MH50_LH_2017, 'Tprime_tAq_2000_MH75_LH_2017':Tprime_tAq_2000_MH75_LH_2017, 'Tprime_tAq_2000_MH100_LH_2017':Tprime_tAq_2000_MH100_LH_2017, 'Tprime_tAq_2000_MH125_LH_2017':Tprime_tAq_2000_MH125_LH_2017, 'Tprime_tAq_2000_MH150_LH_2017':Tprime_tAq_2000_MH150_LH_2017, 'Tprime_tAq_2000_MH175_LH_2017':Tprime_tAq_2000_MH175_LH_2017, 'Tprime_tAq_2000_MH200_LH_2017':Tprime_tAq_2000_MH200_LH_2017, 'Tprime_tAq_2000_MH250_LH_2017':Tprime_tAq_2000_MH250_LH_2017, 'Tprime_tAq_2000_MH350_LH_2017':Tprime_tAq_2000_MH350_LH_2017, 'Tprime_tAq_2000_MH450_LH_2017':Tprime_tAq_2000_MH450_LH_2017, 'Tprime_tAq_2000_MH500_LH_2017':Tprime_tAq_2000_MH500_LH_2017, 'Tprime_tAq_2100_MH25_LH_2017':Tprime_tAq_2100_MH25_LH_2017, 'Tprime_tAq_2100_MH50_LH_2017':Tprime_tAq_2100_MH50_LH_2017, 'Tprime_tAq_2100_MH75_LH_2017':Tprime_tAq_2100_MH75_LH_2017, 'Tprime_tAq_2100_MH100_LH_2017':Tprime_tAq_2100_MH100_LH_2017, 'Tprime_tAq_2100_MH125_LH_2017':Tprime_tAq_2100_MH125_LH_2017, 'Tprime_tAq_2100_MH150_LH_2017':Tprime_tAq_2100_MH150_LH_2017, 'Tprime_tAq_2100_MH175_LH_2017':Tprime_tAq_2100_MH175_LH_2017, 'Tprime_tAq_2100_MH200_LH_2017':Tprime_tAq_2100_MH200_LH_2017, 'Tprime_tAq_2100_MH250_LH_2017':Tprime_tAq_2100_MH250_LH_2017, 'Tprime_tAq_2100_MH350_LH_2017':Tprime_tAq_2100_MH350_LH_2017, 'Tprime_tAq_2100_MH450_LH_2017':Tprime_tAq_2100_MH450_LH_2017, 'Tprime_tAq_2100_MH500_LH_2017':Tprime_tAq_2100_MH500_LH_2017, 'Tprime_tAq_2200_MH25_LH_2017':Tprime_tAq_2200_MH25_LH_2017, 'Tprime_tAq_2200_MH50_LH_2017':Tprime_tAq_2200_MH50_LH_2017, 'Tprime_tAq_2200_MH75_LH_2017':Tprime_tAq_2200_MH75_LH_2017, 'Tprime_tAq_2200_MH100_LH_2017':Tprime_tAq_2200_MH100_LH_2017, 'Tprime_tAq_2200_MH125_LH_2017':Tprime_tAq_2200_MH125_LH_2017, 'Tprime_tAq_2200_MH150_LH_2017':Tprime_tAq_2200_MH150_LH_2017, 'Tprime_tAq_2200_MH175_LH_2017':Tprime_tAq_2200_MH175_LH_2017, 'Tprime_tAq_2200_MH200_LH_2017':Tprime_tAq_2200_MH200_LH_2017, 'Tprime_tAq_2200_MH250_LH_2017':Tprime_tAq_2200_MH250_LH_2017, 'Tprime_tAq_2200_MH350_LH_2017':Tprime_tAq_2200_MH350_LH_2017, 'Tprime_tAq_2200_MH450_LH_2017':Tprime_tAq_2200_MH450_LH_2017, 'Tprime_tAq_2200_MH500_LH_2017':Tprime_tAq_2200_MH500_LH_2017, 'Tprime_tAq_2300_MH25_LH_2017':Tprime_tAq_2300_MH25_LH_2017, 'Tprime_tAq_2300_MH50_LH_2017':Tprime_tAq_2300_MH50_LH_2017, 'Tprime_tAq_2300_MH75_LH_2017':Tprime_tAq_2300_MH75_LH_2017, 'Tprime_tAq_2300_MH100_LH_2017':Tprime_tAq_2300_MH100_LH_2017, 'Tprime_tAq_2300_MH125_LH_2017':Tprime_tAq_2300_MH125_LH_2017, 'Tprime_tAq_2300_MH150_LH_2017':Tprime_tAq_2300_MH150_LH_2017, 'Tprime_tAq_2300_MH175_LH_2017':Tprime_tAq_2300_MH175_LH_2017, 'Tprime_tAq_2300_MH200_LH_2017':Tprime_tAq_2300_MH200_LH_2017, 'Tprime_tAq_2300_MH250_LH_2017':Tprime_tAq_2300_MH250_LH_2017, 'Tprime_tAq_2300_MH350_LH_2017':Tprime_tAq_2300_MH350_LH_2017, 'Tprime_tAq_2300_MH450_LH_2017':Tprime_tAq_2300_MH450_LH_2017, 'Tprime_tAq_2300_MH500_LH_2017':Tprime_tAq_2300_MH500_LH_2017, 'Tprime_tAq_2400_MH25_LH_2017':Tprime_tAq_2400_MH25_LH_2017, 'Tprime_tAq_2400_MH50_LH_2017':Tprime_tAq_2400_MH50_LH_2017, 'Tprime_tAq_2400_MH75_LH_2017':Tprime_tAq_2400_MH75_LH_2017, 'Tprime_tAq_2400_MH100_LH_2017':Tprime_tAq_2400_MH100_LH_2017, 'Tprime_tAq_2400_MH125_LH_2017':Tprime_tAq_2400_MH125_LH_2017, 'Tprime_tAq_2400_MH150_LH_2017':Tprime_tAq_2400_MH150_LH_2017, 'Tprime_tAq_2400_MH175_LH_2017':Tprime_tAq_2400_MH175_LH_2017, 'Tprime_tAq_2400_MH200_LH_2017':Tprime_tAq_2400_MH200_LH_2017, 'Tprime_tAq_2400_MH250_LH_2017':Tprime_tAq_2400_MH250_LH_2017, 'Tprime_tAq_2400_MH350_LH_2017':Tprime_tAq_2400_MH350_LH_2017, 'Tprime_tAq_2400_MH450_LH_2017':Tprime_tAq_2400_MH450_LH_2017, 'Tprime_tAq_2400_MH500_LH_2017':Tprime_tAq_2400_MH500_LH_2017, 'Tprime_tAq_2500_MH25_LH_2017':Tprime_tAq_2500_MH25_LH_2017, 'Tprime_tAq_2500_MH50_LH_2017':Tprime_tAq_2500_MH50_LH_2017, 'Tprime_tAq_2500_MH75_LH_2017':Tprime_tAq_2500_MH75_LH_2017, 'Tprime_tAq_2500_MH100_LH_2017':Tprime_tAq_2500_MH100_LH_2017, 'Tprime_tAq_2500_MH125_LH_2017':Tprime_tAq_2500_MH125_LH_2017, 'Tprime_tAq_2500_MH150_LH_2017':Tprime_tAq_2500_MH150_LH_2017, 'Tprime_tAq_2500_MH175_LH_2017':Tprime_tAq_2500_MH175_LH_2017, 'Tprime_tAq_2500_MH200_LH_2017':Tprime_tAq_2500_MH200_LH_2017, 'Tprime_tAq_2500_MH250_LH_2017':Tprime_tAq_2500_MH250_LH_2017, 'Tprime_tAq_2500_MH350_LH_2017':Tprime_tAq_2500_MH350_LH_2017, 'Tprime_tAq_2500_MH450_LH_2017':Tprime_tAq_2500_MH450_LH_2017, 'Tprime_tAq_2500_MH500_LH_2017':Tprime_tAq_2500_MH500_LH_2017, 'Tprime_tAq_2600_MH25_LH_2017':Tprime_tAq_2600_MH25_LH_2017, 'Tprime_tAq_2600_MH50_LH_2017':Tprime_tAq_2600_MH50_LH_2017, 'Tprime_tAq_2600_MH75_LH_2017':Tprime_tAq_2600_MH75_LH_2017, 'Tprime_tAq_2600_MH100_LH_2017':Tprime_tAq_2600_MH100_LH_2017, 'Tprime_tAq_2600_MH125_LH_2017':Tprime_tAq_2600_MH125_LH_2017, 'Tprime_tAq_2600_MH150_LH_2017':Tprime_tAq_2600_MH150_LH_2017, 'Tprime_tAq_2600_MH175_LH_2017':Tprime_tAq_2600_MH175_LH_2017, 'Tprime_tAq_2600_MH200_LH_2017':Tprime_tAq_2600_MH200_LH_2017, 'Tprime_tAq_2600_MH250_LH_2017':Tprime_tAq_2600_MH250_LH_2017, 'Tprime_tAq_2600_MH350_LH_2017':Tprime_tAq_2600_MH350_LH_2017, 'Tprime_tAq_2600_MH450_LH_2017':Tprime_tAq_2600_MH450_LH_2017, 'Tprime_tAq_2600_MH500_LH_2017':Tprime_tAq_2600_MH500_LH_2017, 'Tprime_tAq_2700_MH25_LH_2017':Tprime_tAq_2700_MH25_LH_2017, 'Tprime_tAq_2700_MH50_LH_2017':Tprime_tAq_2700_MH50_LH_2017, 'Tprime_tAq_2700_MH75_LH_2017':Tprime_tAq_2700_MH75_LH_2017, 'Tprime_tAq_2700_MH100_LH_2017':Tprime_tAq_2700_MH100_LH_2017, 'Tprime_tAq_2700_MH125_LH_2017':Tprime_tAq_2700_MH125_LH_2017, 'Tprime_tAq_2700_MH150_LH_2017':Tprime_tAq_2700_MH150_LH_2017, 'Tprime_tAq_2700_MH175_LH_2017':Tprime_tAq_2700_MH175_LH_2017, 'Tprime_tAq_2700_MH200_LH_2017':Tprime_tAq_2700_MH200_LH_2017, 'Tprime_tAq_2700_MH250_LH_2017':Tprime_tAq_2700_MH250_LH_2017, 'Tprime_tAq_2700_MH350_LH_2017':Tprime_tAq_2700_MH350_LH_2017, 'Tprime_tAq_2700_MH450_LH_2017':Tprime_tAq_2700_MH450_LH_2017, 'Tprime_tAq_2700_MH500_LH_2017':Tprime_tAq_2700_MH500_LH_2017, 'Tprime_tAq_2800_MH25_LH_2017':Tprime_tAq_2800_MH25_LH_2017, 'Tprime_tAq_2800_MH50_LH_2017':Tprime_tAq_2800_MH50_LH_2017, 'Tprime_tAq_2800_MH75_LH_2017':Tprime_tAq_2800_MH75_LH_2017, 'Tprime_tAq_2800_MH100_LH_2017':Tprime_tAq_2800_MH100_LH_2017, 'Tprime_tAq_2800_MH125_LH_2017':Tprime_tAq_2800_MH125_LH_2017, 'Tprime_tAq_2800_MH150_LH_2017':Tprime_tAq_2800_MH150_LH_2017, 'Tprime_tAq_2800_MH175_LH_2017':Tprime_tAq_2800_MH175_LH_2017, 'Tprime_tAq_2800_MH200_LH_2017':Tprime_tAq_2800_MH200_LH_2017, 'Tprime_tAq_2800_MH250_LH_2017':Tprime_tAq_2800_MH250_LH_2017, 'Tprime_tAq_2800_MH350_LH_2017':Tprime_tAq_2800_MH350_LH_2017, 'Tprime_tAq_2800_MH450_LH_2017':Tprime_tAq_2800_MH450_LH_2017, 'Tprime_tAq_2800_MH500_LH_2017':Tprime_tAq_2800_MH500_LH_2017, 'Tprime_tAq_2900_MH25_LH_2017':Tprime_tAq_2900_MH25_LH_2017, 'Tprime_tAq_2900_MH50_LH_2017':Tprime_tAq_2900_MH50_LH_2017, 'Tprime_tAq_2900_MH75_LH_2017':Tprime_tAq_2900_MH75_LH_2017, 'Tprime_tAq_2900_MH100_LH_2017':Tprime_tAq_2900_MH100_LH_2017, 'Tprime_tAq_2900_MH125_LH_2017':Tprime_tAq_2900_MH125_LH_2017, 'Tprime_tAq_2900_MH150_LH_2017':Tprime_tAq_2900_MH150_LH_2017, 'Tprime_tAq_2900_MH175_LH_2017':Tprime_tAq_2900_MH175_LH_2017, 'Tprime_tAq_2900_MH200_LH_2017':Tprime_tAq_2900_MH200_LH_2017, 'Tprime_tAq_2900_MH250_LH_2017':Tprime_tAq_2900_MH250_LH_2017, 'Tprime_tAq_2900_MH350_LH_2017':Tprime_tAq_2900_MH350_LH_2017, 'Tprime_tAq_2900_MH450_LH_2017':Tprime_tAq_2900_MH450_LH_2017, 'Tprime_tAq_2900_MH500_LH_2017':Tprime_tAq_2900_MH500_LH_2017, 'Tprime_tAq_3000_MH25_LH_2017':Tprime_tAq_3000_MH25_LH_2017, 'Tprime_tAq_3000_MH50_LH_2017':Tprime_tAq_3000_MH50_LH_2017, 'Tprime_tAq_3000_MH75_LH_2017':Tprime_tAq_3000_MH75_LH_2017, 'Tprime_tAq_3000_MH100_LH_2017':Tprime_tAq_3000_MH100_LH_2017, 'Tprime_tAq_3000_MH125_LH_2017':Tprime_tAq_3000_MH125_LH_2017, 'Tprime_tAq_3000_MH150_LH_2017':Tprime_tAq_3000_MH150_LH_2017, 'Tprime_tAq_3000_MH175_LH_2017':Tprime_tAq_3000_MH175_LH_2017, 'Tprime_tAq_3000_MH200_LH_2017':Tprime_tAq_3000_MH200_LH_2017, 'Tprime_tAq_3000_MH250_LH_2017':Tprime_tAq_3000_MH250_LH_2017, 'Tprime_tAq_3000_MH350_LH_2017':Tprime_tAq_3000_MH350_LH_2017, 'Tprime_tAq_3000_MH450_LH_2017':Tprime_tAq_3000_MH450_LH_2017, 'Tprime_tAq_3000_MH500_LH_2017':Tprime_tAq_3000_MH500_LH_2017,'Tprime_tAq_600_MH25_LH_2018':Tprime_tAq_600_MH25_LH_2018, 'Tprime_tAq_600_MH50_LH_2018':Tprime_tAq_600_MH50_LH_2018, 'Tprime_tAq_600_MH75_LH_2018':Tprime_tAq_600_MH75_LH_2018, 'Tprime_tAq_600_MH100_LH_2018':Tprime_tAq_600_MH100_LH_2018, 'Tprime_tAq_600_MH125_LH_2018':Tprime_tAq_600_MH125_LH_2018, 'Tprime_tAq_600_MH150_LH_2018':Tprime_tAq_600_MH150_LH_2018, 'Tprime_tAq_600_MH175_LH_2018':Tprime_tAq_600_MH175_LH_2018, 'Tprime_tAq_600_MH200_LH_2018':Tprime_tAq_600_MH200_LH_2018, 'Tprime_tAq_600_MH250_LH_2018':Tprime_tAq_600_MH250_LH_2018, 'Tprime_tAq_600_MH350_LH_2018':Tprime_tAq_600_MH350_LH_2018, 'Tprime_tAq_600_MH450_LH_2018':Tprime_tAq_600_MH450_LH_2018, 'Tprime_tAq_600_MH500_LH_2018':Tprime_tAq_600_MH500_LH_2018, 'Tprime_tAq_700_MH25_LH_2018':Tprime_tAq_700_MH25_LH_2018, 'Tprime_tAq_700_MH50_LH_2018':Tprime_tAq_700_MH50_LH_2018, 'Tprime_tAq_700_MH75_LH_2018':Tprime_tAq_700_MH75_LH_2018, 'Tprime_tAq_700_MH100_LH_2018':Tprime_tAq_700_MH100_LH_2018, 'Tprime_tAq_700_MH125_LH_2018':Tprime_tAq_700_MH125_LH_2018, 'Tprime_tAq_700_MH150_LH_2018':Tprime_tAq_700_MH150_LH_2018, 'Tprime_tAq_700_MH175_LH_2018':Tprime_tAq_700_MH175_LH_2018, 'Tprime_tAq_700_MH200_LH_2018':Tprime_tAq_700_MH200_LH_2018, 'Tprime_tAq_700_MH250_LH_2018':Tprime_tAq_700_MH250_LH_2018, 'Tprime_tAq_700_MH350_LH_2018':Tprime_tAq_700_MH350_LH_2018, 'Tprime_tAq_700_MH450_LH_2018':Tprime_tAq_700_MH450_LH_2018, 'Tprime_tAq_700_MH500_LH_2018':Tprime_tAq_700_MH500_LH_2018, 'Tprime_tAq_800_MH25_LH_2018':Tprime_tAq_800_MH25_LH_2018, 'Tprime_tAq_800_MH50_LH_2018':Tprime_tAq_800_MH50_LH_2018, 'Tprime_tAq_800_MH75_LH_2018':Tprime_tAq_800_MH75_LH_2018, 'Tprime_tAq_800_MH100_LH_2018':Tprime_tAq_800_MH100_LH_2018, 'Tprime_tAq_800_MH125_LH_2018':Tprime_tAq_800_MH125_LH_2018, 'Tprime_tAq_800_MH150_LH_2018':Tprime_tAq_800_MH150_LH_2018, 'Tprime_tAq_800_MH175_LH_2018':Tprime_tAq_800_MH175_LH_2018, 'Tprime_tAq_800_MH200_LH_2018':Tprime_tAq_800_MH200_LH_2018, 'Tprime_tAq_800_MH250_LH_2018':Tprime_tAq_800_MH250_LH_2018, 'Tprime_tAq_800_MH350_LH_2018':Tprime_tAq_800_MH350_LH_2018, 'Tprime_tAq_800_MH450_LH_2018':Tprime_tAq_800_MH450_LH_2018, 'Tprime_tAq_800_MH500_LH_2018':Tprime_tAq_800_MH500_LH_2018, 'Tprime_tAq_900_MH25_LH_2018':Tprime_tAq_900_MH25_LH_2018, 'Tprime_tAq_900_MH50_LH_2018':Tprime_tAq_900_MH50_LH_2018, 'Tprime_tAq_900_MH75_LH_2018':Tprime_tAq_900_MH75_LH_2018, 'Tprime_tAq_900_MH100_LH_2018':Tprime_tAq_900_MH100_LH_2018, 'Tprime_tAq_900_MH125_LH_2018':Tprime_tAq_900_MH125_LH_2018, 'Tprime_tAq_900_MH150_LH_2018':Tprime_tAq_900_MH150_LH_2018, 'Tprime_tAq_900_MH175_LH_2018':Tprime_tAq_900_MH175_LH_2018, 'Tprime_tAq_900_MH200_LH_2018':Tprime_tAq_900_MH200_LH_2018, 'Tprime_tAq_900_MH250_LH_2018':Tprime_tAq_900_MH250_LH_2018, 'Tprime_tAq_900_MH350_LH_2018':Tprime_tAq_900_MH350_LH_2018, 'Tprime_tAq_900_MH450_LH_2018':Tprime_tAq_900_MH450_LH_2018, 'Tprime_tAq_900_MH500_LH_2018':Tprime_tAq_900_MH500_LH_2018, 'Tprime_tAq_1000_MH25_LH_2018':Tprime_tAq_1000_MH25_LH_2018, 'Tprime_tAq_1000_MH50_LH_2018':Tprime_tAq_1000_MH50_LH_2018, 'Tprime_tAq_1000_MH75_LH_2018':Tprime_tAq_1000_MH75_LH_2018, 'Tprime_tAq_1000_MH100_LH_2018':Tprime_tAq_1000_MH100_LH_2018, 'Tprime_tAq_1000_MH125_LH_2018':Tprime_tAq_1000_MH125_LH_2018, 'Tprime_tAq_1000_MH150_LH_2018':Tprime_tAq_1000_MH150_LH_2018, 'Tprime_tAq_1000_MH175_LH_2018':Tprime_tAq_1000_MH175_LH_2018, 'Tprime_tAq_1000_MH200_LH_2018':Tprime_tAq_1000_MH200_LH_2018, 'Tprime_tAq_1000_MH250_LH_2018':Tprime_tAq_1000_MH250_LH_2018, 'Tprime_tAq_1000_MH350_LH_2018':Tprime_tAq_1000_MH350_LH_2018, 'Tprime_tAq_1000_MH450_LH_2018':Tprime_tAq_1000_MH450_LH_2018, 'Tprime_tAq_1000_MH500_LH_2018':Tprime_tAq_1000_MH500_LH_2018, 'Tprime_tAq_1100_MH25_LH_2018':Tprime_tAq_1100_MH25_LH_2018, 'Tprime_tAq_1100_MH50_LH_2018':Tprime_tAq_1100_MH50_LH_2018, 'Tprime_tAq_1100_MH75_LH_2018':Tprime_tAq_1100_MH75_LH_2018, 'Tprime_tAq_1100_MH100_LH_2018':Tprime_tAq_1100_MH100_LH_2018, 'Tprime_tAq_1100_MH125_LH_2018':Tprime_tAq_1100_MH125_LH_2018, 'Tprime_tAq_1100_MH150_LH_2018':Tprime_tAq_1100_MH150_LH_2018, 'Tprime_tAq_1100_MH175_LH_2018':Tprime_tAq_1100_MH175_LH_2018, 'Tprime_tAq_1100_MH200_LH_2018':Tprime_tAq_1100_MH200_LH_2018, 'Tprime_tAq_1100_MH250_LH_2018':Tprime_tAq_1100_MH250_LH_2018, 'Tprime_tAq_1100_MH350_LH_2018':Tprime_tAq_1100_MH350_LH_2018, 'Tprime_tAq_1100_MH450_LH_2018':Tprime_tAq_1100_MH450_LH_2018, 'Tprime_tAq_1100_MH500_LH_2018':Tprime_tAq_1100_MH500_LH_2018, 'Tprime_tAq_1200_MH25_LH_2018':Tprime_tAq_1200_MH25_LH_2018, 'Tprime_tAq_1200_MH50_LH_2018':Tprime_tAq_1200_MH50_LH_2018, 'Tprime_tAq_1200_MH75_LH_2018':Tprime_tAq_1200_MH75_LH_2018, 'Tprime_tAq_1200_MH100_LH_2018':Tprime_tAq_1200_MH100_LH_2018, 'Tprime_tAq_1200_MH125_LH_2018':Tprime_tAq_1200_MH125_LH_2018, 'Tprime_tAq_1200_MH150_LH_2018':Tprime_tAq_1200_MH150_LH_2018, 'Tprime_tAq_1200_MH175_LH_2018':Tprime_tAq_1200_MH175_LH_2018, 'Tprime_tAq_1200_MH200_LH_2018':Tprime_tAq_1200_MH200_LH_2018, 'Tprime_tAq_1200_MH250_LH_2018':Tprime_tAq_1200_MH250_LH_2018, 'Tprime_tAq_1200_MH350_LH_2018':Tprime_tAq_1200_MH350_LH_2018, 'Tprime_tAq_1200_MH450_LH_2018':Tprime_tAq_1200_MH450_LH_2018, 'Tprime_tAq_1200_MH500_LH_2018':Tprime_tAq_1200_MH500_LH_2018, 'Tprime_tAq_1300_MH25_LH_2018':Tprime_tAq_1300_MH25_LH_2018, 'Tprime_tAq_1300_MH50_LH_2018':Tprime_tAq_1300_MH50_LH_2018, 'Tprime_tAq_1300_MH75_LH_2018':Tprime_tAq_1300_MH75_LH_2018, 'Tprime_tAq_1300_MH100_LH_2018':Tprime_tAq_1300_MH100_LH_2018, 'Tprime_tAq_1300_MH125_LH_2018':Tprime_tAq_1300_MH125_LH_2018, 'Tprime_tAq_1300_MH150_LH_2018':Tprime_tAq_1300_MH150_LH_2018, 'Tprime_tAq_1300_MH175_LH_2018':Tprime_tAq_1300_MH175_LH_2018, 'Tprime_tAq_1300_MH200_LH_2018':Tprime_tAq_1300_MH200_LH_2018, 'Tprime_tAq_1300_MH250_LH_2018':Tprime_tAq_1300_MH250_LH_2018, 'Tprime_tAq_1300_MH350_LH_2018':Tprime_tAq_1300_MH350_LH_2018, 'Tprime_tAq_1300_MH450_LH_2018':Tprime_tAq_1300_MH450_LH_2018, 'Tprime_tAq_1300_MH500_LH_2018':Tprime_tAq_1300_MH500_LH_2018, 'Tprime_tAq_1400_MH25_LH_2018':Tprime_tAq_1400_MH25_LH_2018, 'Tprime_tAq_1400_MH50_LH_2018':Tprime_tAq_1400_MH50_LH_2018, 'Tprime_tAq_1400_MH75_LH_2018':Tprime_tAq_1400_MH75_LH_2018, 'Tprime_tAq_1400_MH100_LH_2018':Tprime_tAq_1400_MH100_LH_2018, 'Tprime_tAq_1400_MH125_LH_2018':Tprime_tAq_1400_MH125_LH_2018, 'Tprime_tAq_1400_MH150_LH_2018':Tprime_tAq_1400_MH150_LH_2018, 'Tprime_tAq_1400_MH175_LH_2018':Tprime_tAq_1400_MH175_LH_2018, 'Tprime_tAq_1400_MH200_LH_2018':Tprime_tAq_1400_MH200_LH_2018, 'Tprime_tAq_1400_MH250_LH_2018':Tprime_tAq_1400_MH250_LH_2018, 'Tprime_tAq_1400_MH350_LH_2018':Tprime_tAq_1400_MH350_LH_2018, 'Tprime_tAq_1400_MH450_LH_2018':Tprime_tAq_1400_MH450_LH_2018, 'Tprime_tAq_1400_MH500_LH_2018':Tprime_tAq_1400_MH500_LH_2018, 'Tprime_tAq_1500_MH25_LH_2018':Tprime_tAq_1500_MH25_LH_2018, 'Tprime_tAq_1500_MH50_LH_2018':Tprime_tAq_1500_MH50_LH_2018, 'Tprime_tAq_1500_MH75_LH_2018':Tprime_tAq_1500_MH75_LH_2018, 'Tprime_tAq_1500_MH100_LH_2018':Tprime_tAq_1500_MH100_LH_2018, 'Tprime_tAq_1500_MH125_LH_2018':Tprime_tAq_1500_MH125_LH_2018, 'Tprime_tAq_1500_MH150_LH_2018':Tprime_tAq_1500_MH150_LH_2018, 'Tprime_tAq_1500_MH175_LH_2018':Tprime_tAq_1500_MH175_LH_2018, 'Tprime_tAq_1500_MH200_LH_2018':Tprime_tAq_1500_MH200_LH_2018, 'Tprime_tAq_1500_MH250_LH_2018':Tprime_tAq_1500_MH250_LH_2018, 'Tprime_tAq_1500_MH350_LH_2018':Tprime_tAq_1500_MH350_LH_2018, 'Tprime_tAq_1500_MH450_LH_2018':Tprime_tAq_1500_MH450_LH_2018, 'Tprime_tAq_1500_MH500_LH_2018':Tprime_tAq_1500_MH500_LH_2018, 'Tprime_tAq_1600_MH25_LH_2018':Tprime_tAq_1600_MH25_LH_2018, 'Tprime_tAq_1600_MH50_LH_2018':Tprime_tAq_1600_MH50_LH_2018, 'Tprime_tAq_1600_MH75_LH_2018':Tprime_tAq_1600_MH75_LH_2018, 'Tprime_tAq_1600_MH100_LH_2018':Tprime_tAq_1600_MH100_LH_2018, 'Tprime_tAq_1600_MH125_LH_2018':Tprime_tAq_1600_MH125_LH_2018, 'Tprime_tAq_1600_MH150_LH_2018':Tprime_tAq_1600_MH150_LH_2018, 'Tprime_tAq_1600_MH175_LH_2018':Tprime_tAq_1600_MH175_LH_2018, 'Tprime_tAq_1600_MH200_LH_2018':Tprime_tAq_1600_MH200_LH_2018, 'Tprime_tAq_1600_MH250_LH_2018':Tprime_tAq_1600_MH250_LH_2018, 'Tprime_tAq_1600_MH350_LH_2018':Tprime_tAq_1600_MH350_LH_2018, 'Tprime_tAq_1600_MH450_LH_2018':Tprime_tAq_1600_MH450_LH_2018, 'Tprime_tAq_1600_MH500_LH_2018':Tprime_tAq_1600_MH500_LH_2018, 'Tprime_tAq_1700_MH25_LH_2018':Tprime_tAq_1700_MH25_LH_2018, 'Tprime_tAq_1700_MH50_LH_2018':Tprime_tAq_1700_MH50_LH_2018, 'Tprime_tAq_1700_MH75_LH_2018':Tprime_tAq_1700_MH75_LH_2018, 'Tprime_tAq_1700_MH100_LH_2018':Tprime_tAq_1700_MH100_LH_2018, 'Tprime_tAq_1700_MH125_LH_2018':Tprime_tAq_1700_MH125_LH_2018, 'Tprime_tAq_1700_MH150_LH_2018':Tprime_tAq_1700_MH150_LH_2018, 'Tprime_tAq_1700_MH175_LH_2018':Tprime_tAq_1700_MH175_LH_2018, 'Tprime_tAq_1700_MH200_LH_2018':Tprime_tAq_1700_MH200_LH_2018, 'Tprime_tAq_1700_MH250_LH_2018':Tprime_tAq_1700_MH250_LH_2018, 'Tprime_tAq_1700_MH350_LH_2018':Tprime_tAq_1700_MH350_LH_2018, 'Tprime_tAq_1700_MH450_LH_2018':Tprime_tAq_1700_MH450_LH_2018, 'Tprime_tAq_1700_MH500_LH_2018':Tprime_tAq_1700_MH500_LH_2018, 'Tprime_tAq_1800_MH25_LH_2018':Tprime_tAq_1800_MH25_LH_2018, 'Tprime_tAq_1800_MH50_LH_2018':Tprime_tAq_1800_MH50_LH_2018, 'Tprime_tAq_1800_MH75_LH_2018':Tprime_tAq_1800_MH75_LH_2018, 'Tprime_tAq_1800_MH100_LH_2018':Tprime_tAq_1800_MH100_LH_2018, 'Tprime_tAq_1800_MH125_LH_2018':Tprime_tAq_1800_MH125_LH_2018, 'Tprime_tAq_1800_MH150_LH_2018':Tprime_tAq_1800_MH150_LH_2018, 'Tprime_tAq_1800_MH175_LH_2018':Tprime_tAq_1800_MH175_LH_2018, 'Tprime_tAq_1800_MH200_LH_2018':Tprime_tAq_1800_MH200_LH_2018, 'Tprime_tAq_1800_MH250_LH_2018':Tprime_tAq_1800_MH250_LH_2018, 'Tprime_tAq_1800_MH350_LH_2018':Tprime_tAq_1800_MH350_LH_2018, 'Tprime_tAq_1800_MH450_LH_2018':Tprime_tAq_1800_MH450_LH_2018, 'Tprime_tAq_1800_MH500_LH_2018':Tprime_tAq_1800_MH500_LH_2018, 'Tprime_tAq_1900_MH25_LH_2018':Tprime_tAq_1900_MH25_LH_2018, 'Tprime_tAq_1900_MH50_LH_2018':Tprime_tAq_1900_MH50_LH_2018, 'Tprime_tAq_1900_MH75_LH_2018':Tprime_tAq_1900_MH75_LH_2018, 'Tprime_tAq_1900_MH100_LH_2018':Tprime_tAq_1900_MH100_LH_2018, 'Tprime_tAq_1900_MH125_LH_2018':Tprime_tAq_1900_MH125_LH_2018, 'Tprime_tAq_1900_MH150_LH_2018':Tprime_tAq_1900_MH150_LH_2018, 'Tprime_tAq_1900_MH175_LH_2018':Tprime_tAq_1900_MH175_LH_2018, 'Tprime_tAq_1900_MH200_LH_2018':Tprime_tAq_1900_MH200_LH_2018, 'Tprime_tAq_1900_MH250_LH_2018':Tprime_tAq_1900_MH250_LH_2018, 'Tprime_tAq_1900_MH350_LH_2018':Tprime_tAq_1900_MH350_LH_2018, 'Tprime_tAq_1900_MH450_LH_2018':Tprime_tAq_1900_MH450_LH_2018, 'Tprime_tAq_1900_MH500_LH_2018':Tprime_tAq_1900_MH500_LH_2018, 'Tprime_tAq_2000_MH25_LH_2018':Tprime_tAq_2000_MH25_LH_2018, 'Tprime_tAq_2000_MH50_LH_2018':Tprime_tAq_2000_MH50_LH_2018, 'Tprime_tAq_2000_MH75_LH_2018':Tprime_tAq_2000_MH75_LH_2018, 'Tprime_tAq_2000_MH100_LH_2018':Tprime_tAq_2000_MH100_LH_2018, 'Tprime_tAq_2000_MH125_LH_2018':Tprime_tAq_2000_MH125_LH_2018, 'Tprime_tAq_2000_MH150_LH_2018':Tprime_tAq_2000_MH150_LH_2018, 'Tprime_tAq_2000_MH175_LH_2018':Tprime_tAq_2000_MH175_LH_2018, 'Tprime_tAq_2000_MH200_LH_2018':Tprime_tAq_2000_MH200_LH_2018, 'Tprime_tAq_2000_MH250_LH_2018':Tprime_tAq_2000_MH250_LH_2018, 'Tprime_tAq_2000_MH350_LH_2018':Tprime_tAq_2000_MH350_LH_2018, 'Tprime_tAq_2000_MH450_LH_2018':Tprime_tAq_2000_MH450_LH_2018, 'Tprime_tAq_2000_MH500_LH_2018':Tprime_tAq_2000_MH500_LH_2018, 'Tprime_tAq_2100_MH25_LH_2018':Tprime_tAq_2100_MH25_LH_2018, 'Tprime_tAq_2100_MH50_LH_2018':Tprime_tAq_2100_MH50_LH_2018, 'Tprime_tAq_2100_MH75_LH_2018':Tprime_tAq_2100_MH75_LH_2018, 'Tprime_tAq_2100_MH100_LH_2018':Tprime_tAq_2100_MH100_LH_2018, 'Tprime_tAq_2100_MH125_LH_2018':Tprime_tAq_2100_MH125_LH_2018, 'Tprime_tAq_2100_MH150_LH_2018':Tprime_tAq_2100_MH150_LH_2018, 'Tprime_tAq_2100_MH175_LH_2018':Tprime_tAq_2100_MH175_LH_2018, 'Tprime_tAq_2100_MH200_LH_2018':Tprime_tAq_2100_MH200_LH_2018, 'Tprime_tAq_2100_MH250_LH_2018':Tprime_tAq_2100_MH250_LH_2018, 'Tprime_tAq_2100_MH350_LH_2018':Tprime_tAq_2100_MH350_LH_2018, 'Tprime_tAq_2100_MH450_LH_2018':Tprime_tAq_2100_MH450_LH_2018, 'Tprime_tAq_2100_MH500_LH_2018':Tprime_tAq_2100_MH500_LH_2018, 'Tprime_tAq_2200_MH25_LH_2018':Tprime_tAq_2200_MH25_LH_2018, 'Tprime_tAq_2200_MH50_LH_2018':Tprime_tAq_2200_MH50_LH_2018, 'Tprime_tAq_2200_MH75_LH_2018':Tprime_tAq_2200_MH75_LH_2018, 'Tprime_tAq_2200_MH100_LH_2018':Tprime_tAq_2200_MH100_LH_2018, 'Tprime_tAq_2200_MH125_LH_2018':Tprime_tAq_2200_MH125_LH_2018, 'Tprime_tAq_2200_MH150_LH_2018':Tprime_tAq_2200_MH150_LH_2018, 'Tprime_tAq_2200_MH175_LH_2018':Tprime_tAq_2200_MH175_LH_2018, 'Tprime_tAq_2200_MH200_LH_2018':Tprime_tAq_2200_MH200_LH_2018, 'Tprime_tAq_2200_MH250_LH_2018':Tprime_tAq_2200_MH250_LH_2018, 'Tprime_tAq_2200_MH350_LH_2018':Tprime_tAq_2200_MH350_LH_2018, 'Tprime_tAq_2200_MH450_LH_2018':Tprime_tAq_2200_MH450_LH_2018, 'Tprime_tAq_2200_MH500_LH_2018':Tprime_tAq_2200_MH500_LH_2018, 'Tprime_tAq_2300_MH25_LH_2018':Tprime_tAq_2300_MH25_LH_2018, 'Tprime_tAq_2300_MH50_LH_2018':Tprime_tAq_2300_MH50_LH_2018, 'Tprime_tAq_2300_MH75_LH_2018':Tprime_tAq_2300_MH75_LH_2018, 'Tprime_tAq_2300_MH100_LH_2018':Tprime_tAq_2300_MH100_LH_2018, 'Tprime_tAq_2300_MH125_LH_2018':Tprime_tAq_2300_MH125_LH_2018, 'Tprime_tAq_2300_MH150_LH_2018':Tprime_tAq_2300_MH150_LH_2018, 'Tprime_tAq_2300_MH175_LH_2018':Tprime_tAq_2300_MH175_LH_2018, 'Tprime_tAq_2300_MH200_LH_2018':Tprime_tAq_2300_MH200_LH_2018, 'Tprime_tAq_2300_MH250_LH_2018':Tprime_tAq_2300_MH250_LH_2018, 'Tprime_tAq_2300_MH350_LH_2018':Tprime_tAq_2300_MH350_LH_2018, 'Tprime_tAq_2300_MH450_LH_2018':Tprime_tAq_2300_MH450_LH_2018, 'Tprime_tAq_2300_MH500_LH_2018':Tprime_tAq_2300_MH500_LH_2018, 'Tprime_tAq_2400_MH25_LH_2018':Tprime_tAq_2400_MH25_LH_2018, 'Tprime_tAq_2400_MH50_LH_2018':Tprime_tAq_2400_MH50_LH_2018, 'Tprime_tAq_2400_MH75_LH_2018':Tprime_tAq_2400_MH75_LH_2018, 'Tprime_tAq_2400_MH100_LH_2018':Tprime_tAq_2400_MH100_LH_2018, 'Tprime_tAq_2400_MH125_LH_2018':Tprime_tAq_2400_MH125_LH_2018, 'Tprime_tAq_2400_MH150_LH_2018':Tprime_tAq_2400_MH150_LH_2018, 'Tprime_tAq_2400_MH175_LH_2018':Tprime_tAq_2400_MH175_LH_2018, 'Tprime_tAq_2400_MH200_LH_2018':Tprime_tAq_2400_MH200_LH_2018, 'Tprime_tAq_2400_MH250_LH_2018':Tprime_tAq_2400_MH250_LH_2018, 'Tprime_tAq_2400_MH350_LH_2018':Tprime_tAq_2400_MH350_LH_2018, 'Tprime_tAq_2400_MH450_LH_2018':Tprime_tAq_2400_MH450_LH_2018, 'Tprime_tAq_2400_MH500_LH_2018':Tprime_tAq_2400_MH500_LH_2018, 'Tprime_tAq_2500_MH25_LH_2018':Tprime_tAq_2500_MH25_LH_2018, 'Tprime_tAq_2500_MH50_LH_2018':Tprime_tAq_2500_MH50_LH_2018, 'Tprime_tAq_2500_MH75_LH_2018':Tprime_tAq_2500_MH75_LH_2018, 'Tprime_tAq_2500_MH100_LH_2018':Tprime_tAq_2500_MH100_LH_2018, 'Tprime_tAq_2500_MH125_LH_2018':Tprime_tAq_2500_MH125_LH_2018, 'Tprime_tAq_2500_MH150_LH_2018':Tprime_tAq_2500_MH150_LH_2018, 'Tprime_tAq_2500_MH175_LH_2018':Tprime_tAq_2500_MH175_LH_2018, 'Tprime_tAq_2500_MH200_LH_2018':Tprime_tAq_2500_MH200_LH_2018, 'Tprime_tAq_2500_MH250_LH_2018':Tprime_tAq_2500_MH250_LH_2018, 'Tprime_tAq_2500_MH350_LH_2018':Tprime_tAq_2500_MH350_LH_2018, 'Tprime_tAq_2500_MH450_LH_2018':Tprime_tAq_2500_MH450_LH_2018, 'Tprime_tAq_2500_MH500_LH_2018':Tprime_tAq_2500_MH500_LH_2018, 'Tprime_tAq_2600_MH25_LH_2018':Tprime_tAq_2600_MH25_LH_2018, 'Tprime_tAq_2600_MH50_LH_2018':Tprime_tAq_2600_MH50_LH_2018, 'Tprime_tAq_2600_MH75_LH_2018':Tprime_tAq_2600_MH75_LH_2018, 'Tprime_tAq_2600_MH100_LH_2018':Tprime_tAq_2600_MH100_LH_2018, 'Tprime_tAq_2600_MH125_LH_2018':Tprime_tAq_2600_MH125_LH_2018, 'Tprime_tAq_2600_MH150_LH_2018':Tprime_tAq_2600_MH150_LH_2018, 'Tprime_tAq_2600_MH175_LH_2018':Tprime_tAq_2600_MH175_LH_2018, 'Tprime_tAq_2600_MH200_LH_2018':Tprime_tAq_2600_MH200_LH_2018, 'Tprime_tAq_2600_MH250_LH_2018':Tprime_tAq_2600_MH250_LH_2018, 'Tprime_tAq_2600_MH350_LH_2018':Tprime_tAq_2600_MH350_LH_2018, 'Tprime_tAq_2600_MH450_LH_2018':Tprime_tAq_2600_MH450_LH_2018, 'Tprime_tAq_2600_MH500_LH_2018':Tprime_tAq_2600_MH500_LH_2018, 'Tprime_tAq_2700_MH25_LH_2018':Tprime_tAq_2700_MH25_LH_2018, 'Tprime_tAq_2700_MH50_LH_2018':Tprime_tAq_2700_MH50_LH_2018, 'Tprime_tAq_2700_MH75_LH_2018':Tprime_tAq_2700_MH75_LH_2018, 'Tprime_tAq_2700_MH100_LH_2018':Tprime_tAq_2700_MH100_LH_2018, 'Tprime_tAq_2700_MH125_LH_2018':Tprime_tAq_2700_MH125_LH_2018, 'Tprime_tAq_2700_MH150_LH_2018':Tprime_tAq_2700_MH150_LH_2018, 'Tprime_tAq_2700_MH175_LH_2018':Tprime_tAq_2700_MH175_LH_2018, 'Tprime_tAq_2700_MH200_LH_2018':Tprime_tAq_2700_MH200_LH_2018, 'Tprime_tAq_2700_MH250_LH_2018':Tprime_tAq_2700_MH250_LH_2018, 'Tprime_tAq_2700_MH350_LH_2018':Tprime_tAq_2700_MH350_LH_2018, 'Tprime_tAq_2700_MH450_LH_2018':Tprime_tAq_2700_MH450_LH_2018, 'Tprime_tAq_2700_MH500_LH_2018':Tprime_tAq_2700_MH500_LH_2018, 'Tprime_tAq_2800_MH25_LH_2018':Tprime_tAq_2800_MH25_LH_2018, 'Tprime_tAq_2800_MH50_LH_2018':Tprime_tAq_2800_MH50_LH_2018, 'Tprime_tAq_2800_MH75_LH_2018':Tprime_tAq_2800_MH75_LH_2018, 'Tprime_tAq_2800_MH100_LH_2018':Tprime_tAq_2800_MH100_LH_2018, 'Tprime_tAq_2800_MH125_LH_2018':Tprime_tAq_2800_MH125_LH_2018, 'Tprime_tAq_2800_MH150_LH_2018':Tprime_tAq_2800_MH150_LH_2018, 'Tprime_tAq_2800_MH175_LH_2018':Tprime_tAq_2800_MH175_LH_2018, 'Tprime_tAq_2800_MH200_LH_2018':Tprime_tAq_2800_MH200_LH_2018, 'Tprime_tAq_2800_MH250_LH_2018':Tprime_tAq_2800_MH250_LH_2018, 'Tprime_tAq_2800_MH350_LH_2018':Tprime_tAq_2800_MH350_LH_2018, 'Tprime_tAq_2800_MH450_LH_2018':Tprime_tAq_2800_MH450_LH_2018, 'Tprime_tAq_2800_MH500_LH_2018':Tprime_tAq_2800_MH500_LH_2018, 'Tprime_tAq_2900_MH25_LH_2018':Tprime_tAq_2900_MH25_LH_2018, 'Tprime_tAq_2900_MH50_LH_2018':Tprime_tAq_2900_MH50_LH_2018, 'Tprime_tAq_2900_MH75_LH_2018':Tprime_tAq_2900_MH75_LH_2018, 'Tprime_tAq_2900_MH100_LH_2018':Tprime_tAq_2900_MH100_LH_2018, 'Tprime_tAq_2900_MH125_LH_2018':Tprime_tAq_2900_MH125_LH_2018, 'Tprime_tAq_2900_MH150_LH_2018':Tprime_tAq_2900_MH150_LH_2018, 'Tprime_tAq_2900_MH175_LH_2018':Tprime_tAq_2900_MH175_LH_2018, 'Tprime_tAq_2900_MH200_LH_2018':Tprime_tAq_2900_MH200_LH_2018, 'Tprime_tAq_2900_MH250_LH_2018':Tprime_tAq_2900_MH250_LH_2018, 'Tprime_tAq_2900_MH350_LH_2018':Tprime_tAq_2900_MH350_LH_2018, 'Tprime_tAq_2900_MH450_LH_2018':Tprime_tAq_2900_MH450_LH_2018, 'Tprime_tAq_2900_MH500_LH_2018':Tprime_tAq_2900_MH500_LH_2018, 'Tprime_tAq_3000_MH25_LH_2018':Tprime_tAq_3000_MH25_LH_2018, 'Tprime_tAq_3000_MH50_LH_2018':Tprime_tAq_3000_MH50_LH_2018, 'Tprime_tAq_3000_MH75_LH_2018':Tprime_tAq_3000_MH75_LH_2018, 'Tprime_tAq_3000_MH100_LH_2018':Tprime_tAq_3000_MH100_LH_2018, 'Tprime_tAq_3000_MH125_LH_2018':Tprime_tAq_3000_MH125_LH_2018, 'Tprime_tAq_3000_MH150_LH_2018':Tprime_tAq_3000_MH150_LH_2018, 'Tprime_tAq_3000_MH175_LH_2018':Tprime_tAq_3000_MH175_LH_2018, 'Tprime_tAq_3000_MH200_LH_2018':Tprime_tAq_3000_MH200_LH_2018, 'Tprime_tAq_3000_MH250_LH_2018':Tprime_tAq_3000_MH250_LH_2018, 'Tprime_tAq_3000_MH350_LH_2018':Tprime_tAq_3000_MH350_LH_2018, 'Tprime_tAq_3000_MH450_LH_2018':Tprime_tAq_3000_MH450_LH_2018, 'Tprime_tAq_3000_MH500_LH_2018':Tprime_tAq_3000_MH500_LH_2018, 
'Tprime_tAq_600_LH_2016preVFP':Tprime_tAq_600_LH_2016preVFP, 
'Tprime_tAq_700_LH_2016preVFP':Tprime_tAq_700_LH_2016preVFP, 
'Tprime_tAq_800_LH_2016preVFP':Tprime_tAq_800_LH_2016preVFP, 
'Tprime_tAq_900_LH_2016preVFP':Tprime_tAq_900_LH_2016preVFP, 
'Tprime_tAq_1000_LH_2016preVFP':Tprime_tAq_1000_LH_2016preVFP,  
'Tprime_tAq_1100_LH_2016preVFP':Tprime_tAq_1100_LH_2016preVFP, 
'Tprime_tAq_1200_LH_2016preVFP':Tprime_tAq_1200_LH_2016preVFP, 
'Tprime_tAq_1300_LH_2016preVFP':Tprime_tAq_1300_LH_2016preVFP, 
'Tprime_tAq_1400_LH_2016preVFP':Tprime_tAq_1400_LH_2016preVFP, 
'Tprime_tAq_1500_LH_2016preVFP':Tprime_tAq_1500_LH_2016preVFP, 
'Tprime_tAq_1600_LH_2016preVFP':Tprime_tAq_1600_LH_2016preVFP, 
'Tprime_tAq_1700_LH_2016preVFP':Tprime_tAq_1700_LH_2016preVFP, 
'Tprime_tAq_1800_LH_2016preVFP':Tprime_tAq_1800_LH_2016preVFP, 
'Tprime_tAq_1900_LH_2016preVFP':Tprime_tAq_1900_LH_2016preVFP, 
'Tprime_tAq_2000_LH_2016preVFP':Tprime_tAq_2000_LH_2016preVFP, 
'Tprime_tAq_2100_LH_2016preVFP':Tprime_tAq_2100_LH_2016preVFP, 
'Tprime_tAq_2200_LH_2016preVFP':Tprime_tAq_2200_LH_2016preVFP, 
'Tprime_tAq_2300_LH_2016preVFP':Tprime_tAq_2300_LH_2016preVFP, 
'Tprime_tAq_2400_LH_2016preVFP':Tprime_tAq_2400_LH_2016preVFP, 
'Tprime_tAq_2500_LH_2016preVFP':Tprime_tAq_2500_LH_2016preVFP, 
'Tprime_tAq_2600_LH_2016preVFP':Tprime_tAq_2600_LH_2016preVFP, 
'Tprime_tAq_2700_LH_2016preVFP':Tprime_tAq_2700_LH_2016preVFP, 
'Tprime_tAq_2800_LH_2016preVFP':Tprime_tAq_2800_LH_2016preVFP, 
'Tprime_tAq_3000_LH_2016preVFP':Tprime_tAq_3000_LH_2016preVFP, 
'Tprime_tAq_600_LH_2016postVFP':Tprime_tAq_600_LH_2016postVFP, 
'Tprime_tAq_700_LH_2016postVFP':Tprime_tAq_700_LH_2016postVFP, 
'Tprime_tAq_800_LH_2016postVFP':Tprime_tAq_800_LH_2016postVFP, 
'Tprime_tAq_900_LH_2016postVFP':Tprime_tAq_900_LH_2016postVFP, 
'Tprime_tAq_1000_LH_2016postVFP':Tprime_tAq_1000_LH_2016postVFP,  
'Tprime_tAq_1100_LH_2016postVFP':Tprime_tAq_1100_LH_2016postVFP, 
'Tprime_tAq_1200_LH_2016postVFP':Tprime_tAq_1200_LH_2016postVFP, 
'Tprime_tAq_1300_LH_2016postVFP':Tprime_tAq_1300_LH_2016postVFP, 
'Tprime_tAq_1400_LH_2016postVFP':Tprime_tAq_1400_LH_2016postVFP, 
'Tprime_tAq_1500_LH_2016postVFP':Tprime_tAq_1500_LH_2016postVFP, 
'Tprime_tAq_1600_LH_2016postVFP':Tprime_tAq_1600_LH_2016postVFP, 
'Tprime_tAq_1700_LH_2016postVFP':Tprime_tAq_1700_LH_2016postVFP, 
'Tprime_tAq_1800_LH_2016postVFP':Tprime_tAq_1800_LH_2016postVFP, 
'Tprime_tAq_1900_LH_2016postVFP':Tprime_tAq_1900_LH_2016postVFP, 
'Tprime_tAq_2000_LH_2016postVFP':Tprime_tAq_2000_LH_2016postVFP, 
'Tprime_tAq_2100_LH_2016postVFP':Tprime_tAq_2100_LH_2016postVFP, 
'Tprime_tAq_2200_LH_2016postVFP':Tprime_tAq_2200_LH_2016postVFP, 
'Tprime_tAq_2300_LH_2016postVFP':Tprime_tAq_2300_LH_2016postVFP, 
'Tprime_tAq_2400_LH_2016postVFP':Tprime_tAq_2400_LH_2016postVFP, 
'Tprime_tAq_2500_LH_2016postVFP':Tprime_tAq_2500_LH_2016postVFP, 
'Tprime_tAq_2600_LH_2016postVFP':Tprime_tAq_2600_LH_2016postVFP, 
'Tprime_tAq_2700_LH_2016postVFP':Tprime_tAq_2700_LH_2016postVFP, 
'Tprime_tAq_2800_LH_2016postVFP':Tprime_tAq_2800_LH_2016postVFP, 
'Tprime_tAq_3000_LH_2016postVFP':Tprime_tAq_3000_LH_2016postVFP, 
'Tprime_tAq_600_LH_2017':Tprime_tAq_600_LH_2017, 
'Tprime_tAq_700_LH_2017':Tprime_tAq_700_LH_2017, 
'Tprime_tAq_800_LH_2017':Tprime_tAq_800_LH_2017, 
'Tprime_tAq_900_LH_2017':Tprime_tAq_900_LH_2017, 
'Tprime_tAq_1000_LH_2017':Tprime_tAq_1000_LH_2017,  
'Tprime_tAq_1100_LH_2017':Tprime_tAq_1100_LH_2017, 
'Tprime_tAq_1200_LH_2017':Tprime_tAq_1200_LH_2017, 
'Tprime_tAq_1300_LH_2017':Tprime_tAq_1300_LH_2017, 
'Tprime_tAq_1400_LH_2017':Tprime_tAq_1400_LH_2017, 
'Tprime_tAq_1500_LH_2017':Tprime_tAq_1500_LH_2017, 
'Tprime_tAq_1600_LH_2017':Tprime_tAq_1600_LH_2017, 
'Tprime_tAq_1700_LH_2017':Tprime_tAq_1700_LH_2017, 
'Tprime_tAq_1800_LH_2017':Tprime_tAq_1800_LH_2017, 
'Tprime_tAq_1900_LH_2017':Tprime_tAq_1900_LH_2017, 
'Tprime_tAq_2000_LH_2017':Tprime_tAq_2000_LH_2017, 
'Tprime_tAq_2100_LH_2017':Tprime_tAq_2100_LH_2017, 
'Tprime_tAq_2200_LH_2017':Tprime_tAq_2200_LH_2017, 
'Tprime_tAq_2300_LH_2017':Tprime_tAq_2300_LH_2017, 
'Tprime_tAq_2400_LH_2017':Tprime_tAq_2400_LH_2017, 
'Tprime_tAq_2500_LH_2017':Tprime_tAq_2500_LH_2017, 
'Tprime_tAq_2600_LH_2017':Tprime_tAq_2600_LH_2017, 
'Tprime_tAq_2700_LH_2017':Tprime_tAq_2700_LH_2017, 
'Tprime_tAq_2800_LH_2017':Tprime_tAq_2800_LH_2017, 
'Tprime_tAq_3000_LH_2017':Tprime_tAq_3000_LH_2017, 
'Tprime_tAq_600_LH_2018':Tprime_tAq_600_LH_2018, 
'Tprime_tAq_700_LH_2018':Tprime_tAq_700_LH_2018, 
'Tprime_tAq_800_LH_2018':Tprime_tAq_800_LH_2018, 
'Tprime_tAq_900_LH_2018':Tprime_tAq_900_LH_2018, 
'Tprime_tAq_1000_LH_2018':Tprime_tAq_1000_LH_2018,  
'Tprime_tAq_1100_LH_2018':Tprime_tAq_1100_LH_2018, 
'Tprime_tAq_1200_LH_2018':Tprime_tAq_1200_LH_2018, 
'Tprime_tAq_1300_LH_2018':Tprime_tAq_1300_LH_2018, 
'Tprime_tAq_1400_LH_2018':Tprime_tAq_1400_LH_2018, 
'Tprime_tAq_1500_LH_2018':Tprime_tAq_1500_LH_2018, 
'Tprime_tAq_1600_LH_2018':Tprime_tAq_1600_LH_2018, 
'Tprime_tAq_1700_LH_2018':Tprime_tAq_1700_LH_2018, 
'Tprime_tAq_1800_LH_2018':Tprime_tAq_1800_LH_2018, 
'Tprime_tAq_1900_LH_2018':Tprime_tAq_1900_LH_2018, 
'Tprime_tAq_2000_LH_2018':Tprime_tAq_2000_LH_2018, 
'Tprime_tAq_2100_LH_2018':Tprime_tAq_2100_LH_2018, 
'Tprime_tAq_2200_LH_2018':Tprime_tAq_2200_LH_2018, 
'Tprime_tAq_2300_LH_2018':Tprime_tAq_2300_LH_2018, 
'Tprime_tAq_2400_LH_2018':Tprime_tAq_2400_LH_2018, 
'Tprime_tAq_2500_LH_2018':Tprime_tAq_2500_LH_2018, 
'Tprime_tAq_2600_LH_2018':Tprime_tAq_2600_LH_2018, 
'Tprime_tAq_2700_LH_2018':Tprime_tAq_2700_LH_2018, 
'Tprime_tAq_2800_LH_2018':Tprime_tAq_2800_LH_2018, 
'Tprime_tAq_3000_LH_2018':Tprime_tAq_3000_LH_2018, 
#'Tprime_tAq_LH_2016preVFP':Tprime_tAq_LH_2016preVFP, 
#'Tprime_tAq_LH_2016postVFP':Tprime_tAq_LH_2016postVFP, 
#'Tprime_tAq_LH_2017':Tprime_tAq_LH_2017,
#'Tprime_tAq_LH_2018':Tprime_tAq_LH_2018
}
