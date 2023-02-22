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

#signal

Tprime_tHq_600LH_2016preVFP = sample(ROOT.kBlue,1,1001,"T' 600 LH","Tprime_tHq_600LH_2016preVFP")
Tprime_tHq_600LH_2016preVFP.sigma = 203.40/1000. #to be changed
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
Tprime_tHq_1200LH_2016preVFP.sigma = 5.342/1000. #to be changed
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
Tprime_tHq_1800LH_2016preVFP.sigma = 0.4588/1000. #to be changed
Tprime_tHq_1800LH_2016preVFP.year = 2016
Tprime_tHq_1800LH_2016preVFP.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016preVFP+"-v1/NANOAODSIM"

Tprime_LH_2016preVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2016preVFP")
Tprime_LH_2016preVFP.year = 2016
Tprime_LH_2016preVFP.components = [Tprime_tHq_600LH_2016preVFP,Tprime_tHq_700LH_2016preVFP,Tprime_tHq_800LH_2016preVFP,Tprime_tHq_900LH_2016preVFP,Tprime_tHq_1000LH_2016preVFP,Tprime_tHq_1100LH_2016preVFP,Tprime_tHq_1200LH_2016preVFP,Tprime_tHq_1300LH_2016preVFP,Tprime_tHq_1400LH_2016preVFP,Tprime_tHq_1500LH_2016preVFP,Tprime_tHq_1600LH_2016preVFP,Tprime_tHq_1700LH_2016preVFP,Tprime_tHq_1800LH_2016preVFP]


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
Tprime_tHq_600LH_2016postVFP.sigma = 203.40/1000. #to be changed
Tprime_tHq_600LH_2016postVFP.year = 2016
Tprime_tHq_600LH_2016postVFP.dataset="/TprimeBToTH_M-600_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_tHq_700LH_2016postVFP = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2016postVFP")
Tprime_tHq_700LH_2016postVFP.sigma = 88.107/1000. #to be changed
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
Tprime_tHq_1200LH_2016postVFP.sigma = 5.342/1000. #to be changed
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
Tprime_tHq_1800LH_2016postVFP.sigma = 0.4588/1000. #to be changed
Tprime_tHq_1800LH_2016postVFP.year = 2016
Tprime_tHq_1800LH_2016postVFP.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_13TeV-madgraph_pythia8/"+tag_2016postVFP+"-v1/NANOAODSIM"

Tprime_LH_2016postVFP = sample(ROOT.kBlue, 1, 1001, "T' LH", "Tprime_LH_2016postVFP")
Tprime_LH_2016postVFP.year = 2016
Tprime_LH_2016postVFP.components = [Tprime_tHq_600LH_2016postVFP,Tprime_tHq_700LH_2016postVFP,Tprime_tHq_800LH_2016postVFP,Tprime_tHq_900LH_2016postVFP,Tprime_tHq_1000LH_2016postVFP,Tprime_tHq_1100LH_2016postVFP,Tprime_tHq_1200LH_2016postVFP,Tprime_tHq_1300LH_2016postVFP,Tprime_tHq_1400LH_2016postVFP,Tprime_tHq_1500LH_2016postVFP,Tprime_tHq_1600LH_2016postVFP,Tprime_tHq_1700LH_2016postVFP,Tprime_tHq_1800LH_2016postVFP]



#Data
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
DataMu_2016preVFP.components = [DataMuB_2016preVFP, DataMuC_2016preVFP, DataMuD_2016preVFP, DataMuE_2016preVFP, DataMuF_2016preVFP]


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
DataEle_2016preVFP.components = [DataEleB_2016preVFP, DataEleC_2016preVFP, DataEleD_2016preVFP, DataEleE_2016preVFP, DataEleF_2016preVFP]


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
DataPh_2016preVFP.components = [DataPhB_2016preVFP, DataPhC_2016preVFP, DataPhD_2016preVFP, DataPhE_2016preVFP, DataPhF_2016preVFP]


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
DataHT_2016preVFP.components = [DataHTB_2016preVFP, DataHTC_2016preVFP, DataHTD_2016preVFP, DataHTE_2016preVFP, DataHTF_2016preVFP]


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
Tprime_tHq_600LH_2017.sigma = 203.40/1000. #to be changed
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
Tprime_tHq_1200LH_2017.sigma = 5.342/1000. #to be changed
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
Tprime_tHq_1800LH_2017.sigma = 0.4588/1000. #to be changed
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

TT_Mtt_2018 = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_Mtt_2018")
TT_Mtt_2018.year = 2018
TT_Mtt_2018.components = [TT_dilep_2018,TT_semilep_2018,TT_Mtt700to1000_2018, TT_Mtt1000toInf_2018]


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
Tprime_tHq_600LH_2018.sigma = 203.40/1000. #to be changed
Tprime_tHq_600LH_2018.year = 2018
Tprime_tHq_600LH_2018.dataset="/TprimeBToTH_M-600_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_700LH_2018 = sample(ROOT.kBlue,1,1001,"T' 700 LH","Tprime_tHq_700LH_2018")
Tprime_tHq_700LH_2018.sigma = 88.107/1000. #to be changed
Tprime_tHq_700LH_2018.year = 2018
Tprime_tHq_700LH_2018.dataset="/TprimeBToTH_M-700_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_800LH_2018 = sample(ROOT.kBlue,1,1001,"T' 800 LH","Tprime_tHq_800LH_2018")
Tprime_tHq_800LH_2018.sigma = 45.920/1000. #to be changed
Tprime_tHq_800LH_2018.year = 2018
Tprime_tHq_800LH_2018.dataset="/TprimeBToTH_M-800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_900LH_2018 = sample(ROOT.kBlue,1,1001,"T' 900 LH","Tprime_tHq_900LH_2018")
Tprime_tHq_900LH_2018.sigma = 25.327/1000. #to be changed
Tprime_tHq_900LH_2018.year = 2018
Tprime_tHq_900LH_2018.dataset="/TprimeBToTH_M-900_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1000LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1000 LH","Tprime_tHq_1000LH_2018")
Tprime_tHq_1000LH_2018.sigma = 14.550/1000. #to be changed
Tprime_tHq_1000LH_2018.year = 2018
Tprime_tHq_1000LH_2018.dataset="/TprimeBToTH_M-1000_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1100LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1100 LH","Tprime_tHq_1100LH_2018")
Tprime_tHq_1100LH_2018.sigma = 8.640/1000. #to be changed
Tprime_tHq_1100LH_2018.year = 2018
Tprime_tHq_1100LH_2018.dataset="/TprimeBToTH_M-1100_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1200LH_2018 = sample(ROOT.kCyan,1,1001,"T' 1200 LH","Tprime_tHq_1200LH_2018")
Tprime_tHq_1200LH_2018.sigma = 5.342/1000. #to be changed
Tprime_tHq_1200LH_2018.year = 2018
Tprime_tHq_1200LH_2018.dataset="/TprimeBToTH_M-1200_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1300LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1300 LH","Tprime_tHq_1300LH_2018")
Tprime_tHq_1300LH_2018.sigma = 3.390/1000. #to be changed
Tprime_tHq_1300LH_2018.year = 2018
Tprime_tHq_1300LH_2018.dataset="/TprimeBToTH_M-1300_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1400LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1400 LH","Tprime_tHq_1400LH_2018")
Tprime_tHq_1400LH_2018.sigma = 2.197/1000. #to be changed
Tprime_tHq_1400LH_2018.year = 2018
Tprime_tHq_1400LH_2018.dataset="/TprimeBToTH_M-1400_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1500LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1500 LH","Tprime_tHq_1500LH_2018")
Tprime_tHq_1500LH_2018.sigma = 1.448/1000. #to be changed
Tprime_tHq_1500LH_2018.year = 2018
Tprime_tHq_1500LH_2018.dataset="/TprimeBToTH_M-1500_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1600LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1600 LH","Tprime_tHq_1600LH_2018")
Tprime_tHq_1600LH_2018.sigma = 0.9743/1000. #to be changed
Tprime_tHq_1600LH_2018.year = 2018
Tprime_tHq_1600LH_2018.dataset="/TprimeBToTH_M-1600_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1700LH_2018 = sample(ROOT.kBlue,1,1001,"T' 1700 LH","Tprime_tHq_1700LH_2018")
Tprime_tHq_1700LH_2018.sigma = 0.6638/1000. #to be changed
Tprime_tHq_1700LH_2018.year = 2018
Tprime_tHq_1700LH_2018.dataset="/TprimeBToTH_M-1700_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

Tprime_tHq_1800LH_2018 = sample(ROOT.kBlack,1,1001,"T' 1800 LH","Tprime_tHq_1800LH_2018")
Tprime_tHq_1800LH_2018.sigma = 0.4588/1000. #to be changed
Tprime_tHq_1800LH_2018.year = 2018
Tprime_tHq_1800LH_2018.dataset="/TprimeBToTH_M-1800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"

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
DataMu_2018.components = [DataMuA_2018,DataMuB_2018,DataMuC_2018,DataMuD_2018]

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

sample_dict = {
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



"DataMu_2016preVFP":DataMu_2016preVFP,"DataMuB_2016preVFP":DataMuB_2016preVFP,"DataMuC_2016preVFP":DataMuC_2016preVFP,"DataMuD_2016preVFP":DataMuD_2016preVFP,"DataMuE_2016preVFP":DataMuE_2016preVFP,"DataMuF_2016preVFP":DataMuF_2016preVFP,
"DataMu_2016postVFP":DataMu_2016postVFP,"DataMuF_2016postVFP":DataMuF_2016postVFP,"DataMuG_2016postVFP":DataMuG_2016postVFP,"DataMuH_2016postVFP":DataMuH_2016postVFP,

"DataEle_2016preVFP":DataEle_2016preVFP,"DataEleB_2016preVFP":DataEleB_2016preVFP,"DataEleC_2016preVFP":DataEleC_2016preVFP,"DataEleD_2016preVFP":DataEleD_2016preVFP,"DataEleE_2016preVFP":DataEleE_2016preVFP,"DataEleF_2016preVFP":DataEleF_2016preVFP,
"DataEle_2016postVFP":DataEle_2016postVFP,"DataEleF_2016postVFP":DataEleF_2016postVFP,"DataEleG_2016postVFP":DataEleG_2016postVFP,"DataEleH_2016postVFP":DataEleH_2016postVFP,

"DataPh_2016preVFP":DataPh_2016preVFP,"DataPhB_2016preVFP":DataPhB_2016preVFP,"DataPhC_2016preVFP":DataPhC_2016preVFP,"DataPhD_2016preVFP":DataPhD_2016preVFP,"DataPhE_2016preVFP":DataPhE_2016preVFP,"DataPhF_2016preVFP":DataPhF_2016preVFP,
"DataPh_2016postVFP":DataPh_2016postVFP,"DataPhF_2016postVFP":DataPhF_2016postVFP,"DataPhG_2016postVFP":DataPhG_2016postVFP,"DataPhH_2016postVFP":DataPhH_2016postVFP,

"DataHT_2016preVFP":DataHT_2016preVFP,"DataHTB_2016preVFP":DataHTB_2016preVFP,"DataHTC_2016preVFP":DataHTC_2016preVFP,"DataHTD_2016preVFP":DataHTD_2016preVFP,"DataHTE_2016preVFP":DataHTE_2016preVFP,"DataHTF_2016preVFP":DataHTF_2016preVFP,
"DataHT_2016postVFP":DataHT_2016postVFP,"DataHTF_2016postVFP":DataHTF_2016postVFP,"DataHTG_2016postVFP":DataHTG_2016postVFP,"DataHTH_2016postVFP":DataHTH_2016postVFP,

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
'TT_Mtt700to1000_2018':TT_Mtt700to1000_2018, 'TT_Mtt1000toInf_2018':TT_Mtt1000toInf_2018,"TT_semilep_2018":TT_semilep_2018,"TT_dilep_2018":TT_dilep_2018, "TT_Mtt_2018":TT_Mtt_2018,  
'WJets_2018':WJets_2018, 'WJetsHT70to100_2018':WJetsHT70to100_2018, 'WJetsHT100to200_2018':WJetsHT100to200_2018, 'WJetsHT200to400_2018':WJetsHT200to400_2018,'WJetsHT400to600_2018':WJetsHT400to600_2018, 'WJetsHT600to800_2018':WJetsHT600to800_2018, 'WJetsHT800to1200_2018':WJetsHT800to1200_2018, 'WJetsHT1200to2500_2018':WJetsHT1200to2500_2018,
'WJetsHT2500toInf_2018':WJetsHT2500toInf_2018,
'QCD_2018':QCD_2018, 'QCDHT_50to100_2018':QCDHT_50to100_2018,'QCDHT_100to200_2018':QCDHT_100to200_2018,'QCDHT_200to300_2018':QCDHT_200to300_2018,'QCDHT_300to500_2018':QCDHT_300to500_2018, 'QCDHT_500to700_2018':QCDHT_500to700_2018, 'QCDHT_700to1000_2018':QCDHT_700to1000_2018,
'QCDHT_1000to1500_2018':QCDHT_1000to1500_2018, 'QCDHT_1500to2000_2018':QCDHT_1500to2000_2018, 'QCDHT_2000toInf_2018':QCDHT_2000toInf_2018,
'ST_2018':ST_2018, 'ST_tch_t_2018':ST_tch_t_2018, 'ST_tch_tbar_2018':ST_tch_tbar_2018, 'ST_tW_t_2018':ST_tW_t_2018, 'ST_tW_tbar_2018':ST_tW_tbar_2018, 'ST_sch_2018':ST_sch_2018,
"DataMuA_2018":DataMuA_2018,"DataMu_2018":DataMu_2018,"DataMuB_2018":DataMuB_2018,"DataMuC_2018":DataMuC_2018,"DataMuD_2018":DataMuD_2018,
"DataEleA_2018":DataEleA_2018,"DataEle_2018":DataEle_2018,"DataEleB_2018":DataEleB_2018,"DataEleC_2018":DataEleC_2018,"DataEleD_2018":DataEleD_2018,
"DataHTA_2018":DataHTA_2018,"DataHT_2018":DataHT_2018,"DataHTB_2018":DataHTB_2018,"DataHTC_2018":DataHTC_2018,"DataHTD_2018":DataHTD_2018
}
