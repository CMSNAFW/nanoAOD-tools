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

#da controllare i tag aggiungere la QCD

tag_2016 = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

################################ WJets ################################
altXSUp=0
kFactorsQCD={
    "WJetsHT100to200" : 1.21,
    "WJetsHT200to400" : 1.21,
    "WJetsHT400to600" : 1.21,
    "WJetsHT600to800" : 1.21,
    "WJetsHT800to1200" : 1.21,
    "WJetsHT1200to2500" : 1.21,
    "WJetsHT2500toInf" : 1.21
}

###############################################################################################################################
##########################################                                           ##########################################
##########################################                    2022                   ##########################################
##########################################                                           ##########################################
###############################################################################################################################

######################## adrnico #################
TT_hadr_2022                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2022")
TT_hadr_2022.sigma          = 422.3
TT_hadr_2022.year           = 2022
TT_hadr_2022.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_hadr_2022.process        = 'TT_2022'
TT_hadr_2022.unix_code      = 31101
TT_hadr_2022.EE             = 0


################################ TTbar ################################
TT_semilep_2022             = sample(ROOT.kBlue, 1, 1001, "t#bar{t}", "TT_semilep_2022")
TT_semilep_2022.sigma       = 404.0 #pb
TT_semilep_2022.year        = 2022
TT_semilep_2022.dataset     = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
TT_semilep_2022.process     = 'TT_2022'
TT_semilep_2022.unix_code   = 31100
TT_semilep_2022.EE          = 0



################################ ZJets ################################


ZJetsToNuNu_HT100to200_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2022")
ZJetsToNuNu_HT100to200_2022.sigma       = 273 #pb
ZJetsToNuNu_HT100to200_2022.year        = 2022
ZJetsToNuNu_HT100to200_2022.dataset     = "/Zto2Nu-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT100to200_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT100to200_2022.unix_code   = 31200
ZJetsToNuNu_HT100to200_2022.EE          = 0

ZJetsToNuNu_HT200to400_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2022")
ZJetsToNuNu_HT200to400_2022.sigma       = 76.1 #pb
ZJetsToNuNu_HT200to400_2022.year        = 2022
ZJetsToNuNu_HT200to400_2022.dataset     = "/Zto2Nu-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT200to400_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT200to400_2022.unix_code   = 31201
ZJetsToNuNu_HT200to400_2022.EE          = 0

ZJetsToNuNu_HT400to800_2022             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2022")
ZJetsToNuNu_HT400to800_2022.sigma       = 13.2 #pb
ZJetsToNuNu_HT400to800_2022.year        = 2022
ZJetsToNuNu_HT400to800_2022.dataset     = "/Zto2Nu-4Jets_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2022.process     = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT400to800_2022.unix_code   = 31202
ZJetsToNuNu_HT400to800_2022.EE          = 0

ZJetsToNuNu_HT800to1500_2022            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2022")
ZJetsToNuNu_HT800to1500_2022.sigma      = 1.37 #pb
ZJetsToNuNu_HT800to1500_2022.year       = 2022
ZJetsToNuNu_HT800to1500_2022.dataset    = "/Zto2Nu-4Jets_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2022.process    = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT800to1500_2022.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2022.EE         = 0

ZJetsToNuNu_HT1500to2500_2022           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2022")
ZJetsToNuNu_HT1500to2500_2022.sigma     = 0.0985 #pb
ZJetsToNuNu_HT1500to2500_2022.year      = 2022
ZJetsToNuNu_HT1500to2500_2022.dataset   = "/Zto2Nu-4Jets_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2022.process   = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT1500to2500_2022.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2022.EE        = 0

ZJetsToNuNu_HT2500_2022                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2022")
ZJetsToNuNu_HT2500_2022.sigma           = 0.00669 #pb
ZJetsToNuNu_HT2500_2022.year            = 2022
ZJetsToNuNu_HT2500_2022.dataset         = "/Zto2Nu-4Jets_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2022.process         = 'ZJetsToNuNu_2022'
ZJetsToNuNu_HT2500_2022.unix_code       = 31205
ZJetsToNuNu_HT2500_2022.EE              = 0

ZJetsToNuNu_2022                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2022")
ZJetsToNuNu_2022.year                   = 2022
ZJetsToNuNu_2022.components             = [
                                            ZJetsToNuNu_HT100to200_2022,
                                            ZJetsToNuNu_HT200to400_2022,
                                            ZJetsToNuNu_HT400to800_2022,
                                            ZJetsToNuNu_HT800to1500_2022,
                                            ZJetsToNuNu_HT1500to2500_2022,
                                            ZJetsToNuNu_HT2500_2022 
                                            ]


DataJetMETC_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETC_2022")
DataJetMETC_2022.runP       = 'C'
DataJetMETC_2022.year       = 2022
DataJetMETC_2022.dataset    = '/JetMET/Run2022C-22Sep2023-v1/NANOAOD' #/JetMET/Run2022C-JMENano12p5-v1/NANOAOD da capire quale vogliono che usiamo
DataJetMETC_2022.unix_code  = 30000
DataJetMETC_2022.EE         = 0
DataJetMETD_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETD_2022")
DataJetMETD_2022.runP       = 'D'
DataJetMETD_2022.year       = 2022
DataJetMETD_2022.dataset    = 'D'
DataJetMETD_2022.unix_code  = 30001
DataJetMETD_2022.EE         = 0
DataJetMETE_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETE_2022")
DataJetMETE_2022.runP       = 'E'
DataJetMETE_2022.year       = 2022
DataJetMETE_2022.dataset    = '/JetMET/Run2022E-22Sep2023-v1/NANOAOD'
DataJetMETE_2022.unix_code  = 30002
DataJetMETE_2022.EE         = 1
DataJetMETF_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETF_2022")
DataJetMETF_2022.runP       = 'F'
DataJetMETF_2022.year       = 2022
DataJetMETF_2022.dataset    = '/JetMET/Run2022F-22Sep2023-v2/NANOAOD'
DataJetMETF_2022.unix_code  = 30003
DataJetMETF_2022.EE         = 1
DataJetMETG_2022            = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMETG_2022")
DataJetMETG_2022.runP       = 'G'
DataJetMETG_2022.year       = 2022
DataJetMETG_2022.dataset    = '/JetMET/Run2022G-22Sep2023-v2/NANOAOD'
DataJetMETG_2022.unix_code  = 30004
DataJetMETG_2022.EE         = 1
DataJetMET_2022             = sample(ROOT.kBlack, 1, 1001, "Data", "DataJetMET_2022")
DataJetMET_2022.year        = 2022
DataJetMET_2022.components  = [DataJetMETC_2022, DataJetMETD_2022, DataJetMETE_2022, DataJetMETF_2022, DataJetMETG_2022]
2018
tDM_mPhi1000_mChi1_2025 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi1000_mChi1_2025")
tDM_mPhi1000_mChi1_2025.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
tDM_mPhi1000_mChi1_2025.year = 2025
tDM_mPhi1000_mChi1_2025.dataset = '/tDM_Mchi1MPhi1000_total/oiorio-tDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi1000_mChi1_2025.unix_code = 22100

tDM_mPhi500_mChi1_2025 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "tDM_mPhi500_mChi1_2025")
tDM_mPhi500_mChi1_2025.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
tDM_mPhi500_mChi1_2025.year = 2025
tDM_mPhi500_mChi1_2025.dataset = '/tDM_Mchi1MPhi500_total/oiorio-tDM_Mchi1MPhi500Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi500_mChi1_2025.unix_code = 22101

tDM_mPhi200_mChi1_2025= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=200)", "tDM_mPhi200_mChi1_2025")
tDM_mPhi200_mChi1_2025.year = 2018
tDM_mPhi200_mChi1_2025.sigma = 0.7  #pb
tDM_mPhi200_mChi1_2025.dataset = '/tDM_Mchi1MPhi200_total/oiorio-tDM_Mchi1MPhi200Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi200_mChi1_2025.unix_code = 22102

tDM_mPhi50_mChi1_2025= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "tDM_mPhi50_mChi1_2025")
tDM_mPhi50_mChi1_2025.year = 2025
tDM_mPhi50_mChi1_2025.sigma = 0.7  #pb
tDM_mPhi50_mChi1_2025.dataset = '/tDM_Mchi1MPhi50_total/oiorio-tDM_Mchi1MPhi50Run3_NANOAOD_F-00000000000000000000000000000000/USER'
tDM_mPhi50_mChi1_2025.unix_code = 22102

ttDM_mPhi1000_mChi1_2025 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=1000)", "ttDM_mPhi1000_mChi1_2025")
ttDM_mPhi1000_mChi1_2025.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
ttDM_mPhi1000_mChi1_2025.year = 2025
ttDM_mPhi1000_mChi1_2025.dataset = '/ttDM_Mchi1MPhi1000_total/oiorio-ttDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi1000_mChi1_2025.unix_code = 22103

ttDM_mPhi500_mChi1_2025 = sample(ROOT.kGreen+2, 1, 1001, "DM (m_{#Phi}=500)", "ttDM_mPhi500_mChi1_2025")
ttDM_mPhi500_mChi1_2025.sigma = 24.99 *0.00001 #*100    #pb  aggiunto*100 per i plot
ttDM_mPhi500_mChi1_2025.year = 2025
ttDM_mPhi500_mChi1_2025.dataset = '/ttDM_Mchi1MPhi1000_total/oiorio-ttDM_Mchi1MPhi1000Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi500_mChi1_2025.unix_code = 22104

ttDM_mPhi200_mChi1_2025= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=200)", "ttDM_mPhi200_mChi1_2025")
ttDM_mPhi200_mChi1_2025.year = 2025
ttDM_mPhi200_mChi1_2025.sigma = 0.7  #pb
ttDM_mPhi200_mChi1_2025.dataset = '/ttDM_Mchi1MPhi200_total/oiorio-ttDM_Mchi1MPhi200Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi200_mChi1_2025.unix_code = 22105


ttDM_mPhi50_mChi1_2025= sample(ROOT.kGreen, 1, 1001, "DM (m_{#Phi}=50)", "ttDM_mPhi50_mChi1_2025")
ttDM_mPhi50_mChi1_2025.year = 2025
ttDM_mPhi50_mChi1_2025.sigma = 0.7  #pb
ttDM_mPhi50_mChi1_2025.dataset = '/ttDM_Mchi1MPhi50_total/oiorio-ttDM_Mchi1MPhi50Run3_NANOAOD_F-00000000000000000000000000000000/USER'
ttDM_mPhi50_mChi1_2025.unix_code = 22106

QCD_HT40to70_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT40to70_2022")
QCD_HT40to70_2022.sigma           = 311400000 #pb
QCD_HT40to70_2022.year            = 2022
QCD_HT40to70_2022.dataset         = "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_HT40to70_2022.process         = "QCD_2022"
QCD_HT40to70_2022.unix_code       = 31000
QCD_HT40to70_2022.EE              = 0 
QCD_2022                          = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022")
QCD_2022.year                     = 2022


QCD_HT70to100_2022              = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT70to100_2022")
QCD_HT70to100_2022.sigma        = 58.6*(10**6) #pb
QCD_HT70to100_2022.year         = 2022
QCD_HT70to100_2022.dataset      = "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT70to100_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT70to100_2022.process      = "QCD_2022"
QCD_HT70to100_2022.unix_code    = 31001
QCD_HT70to100_2022.EE           = 0


QCD_HT100to200_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT100to200_2022")
QCD_HT100to200_2022.sigma       = 25.1*(10**6) #pb
QCD_HT100to200_2022.year        = 2022
QCD_HT100to200_2022.dataset     = "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT100to200_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT100to200_2022.process     = "QCD_2022"
QCD_HT100to200_2022.unix_code   = 31002
QCD_HT100to200_2022.EE          = 0

QCD_HT200to400_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT200to400_2022")
QCD_HT200to400_2022.sigma       = 1.96*(10**6) #pb
QCD_HT200to400_2022.year        = 2022
QCD_HT200to400_2022.dataset     = "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT200to400_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT200to400_2022.process     = "QCD_2022"
QCD_HT200to400_2022.unix_code   = 31003
QCD_HT200to400_2022.EE          = 0

QCD_HT400to600_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT400to600_2022")
QCD_HT400to600_2022.sigma       = 96.0*(10**3) #pb
QCD_HT400to600_2022.year        = 2022
QCD_HT400to600_2022.dataset     = "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT400to600_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT400to600_2022.process     = "QCD_2022"
QCD_HT400to600_2022.unix_code   = 31004
QCD_HT400to600_2022.EE          = 0

QCD_HT600to800_2022             = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT600to800_2022")
QCD_HT600to800_2022.sigma       = 13.5*(10**3) #pb
QCD_HT600to800_2022.year        = 2022
QCD_HT600to800_2022.dataset     = "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT600to800_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT600to800_2022.process     = "QCD_2022"
QCD_HT600to800_2022.unix_code   = 31005
QCD_HT600to800_2022.EE          = 0

QCD_HT800to1000_2022            = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT800to1000_2022")
QCD_HT800to1000_2022.sigma      = 3.03*(10**3) #pb
QCD_HT800to1000_2022.year       = 2022
QCD_HT800to1000_2022.dataset    = "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT800to1000_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT800to1000_2022.process    = "QCD_2022"
QCD_HT800to1000_2022.unix_code  = 31006
QCD_HT800to1000_2022.EE         = 0

QCD_HT1000to1200_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1000to1200_2022")
QCD_HT1000to1200_2022.sigma     = 881.4 #pb
QCD_HT1000to1200_2022.year      = 2022
QCD_HT1000to1200_2022.dataset   = "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT1000to1200_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT1000to1200_2022.process   = "QCD_2022"
QCD_HT1000to1200_2022.unix_code = 31007
QCD_HT1000to1200_2022.EE        = 0

QCD_HT1200to1500_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1200to1500_2022")
QCD_HT1200to1500_2022.sigma     = 384 #pb 
QCD_HT1200to1500_2022.year      = 2022
QCD_HT1200to1500_2022.dataset   = "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT1200to1500_2022_v2-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT1200to1500_2022.process   = "QCD_2022"
QCD_HT1200to1500_2022.unix_code = 31007
QCD_HT1200to1500_2022.EE        = 0

QCD_HT1500to2000_2022           = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT1500to2000_2022")
QCD_HT1500to2000_2022.sigma     = 125 #pb
QCD_HT1500to2000_2022.year      = 2022
QCD_HT1500to2000_2022.dataset   = "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT1500to2000_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT1500to2000_2022.process   = "QCD_2022"
QCD_HT1500to2000_2022.unix_code = 31008
QCD_HT1500to2000_2022.EE        = 0

QCD_HT2000_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_HT2000_2022")
QCD_HT2000_2022.sigma           = 26.5 #pb
QCD_HT2000_2022.year            = 2022
QCD_HT2000_2022.dataset         = "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-QCD_HT2000_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
QCD_HT2000_2022.process         = "QCD_2022"
QCD_HT2000_2022.unix_code       = 31009
QCD_HT2000_2022.EE              = 0
QCD_2022                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_2022")
QCD_2022.year                   = 2022
QCD_2022.components             = [  
                                    QCD_HT70to100_2022, QCD_HT100to200_2022, QCD_HT200to400_2022,
                                    QCD_HT400to600_2022, QCD_HT600to800_2022, QCD_HT800to1000_2022, 
                                    QCD_HT1000to1200_2022, QCD_HT1200to1500_2022,
                                    QCD_HT1500to2000_2022, QCD_HT2000_2022
                                ]





QCD_PT15to30_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT15to30_2022")
QCD_PT15to30_2022.sigma           = 1301000000 #pb
QCD_PT15to30_2022.year            = 2022
QCD_PT15to30_2022.dataset         = "/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
QCD_PT15to30_2022.process         = "QCD_2022"
QCD_PT15to30_2022.unix_code       = 40001
QCD_PT15to30_2022.EE              = 0
       

QCD_PT30to50_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT30to50_2022")
QCD_PT30to50_2022.sigma           = 1301000000 #pb
QCD_PT30to50_2022.year            = 2022
QCD_PT30to50_2022.dataset         = "/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
QCD_PT30to50_2022.process         = "QCD_2022"
QCD_PT30to50_2022.unix_code       = 40002
QCD_PT30to50_2022.EE              = 0   

QCD_PT50to80_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT50to80_2022")
QCD_PT50to80_2022.sigma           = 1301000000 #pb
QCD_PT50to80_2022.year            = 2022
QCD_PT50to80_2022.dataset         = "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT50to80_2022.process         = "QCD_2022"
QCD_PT50to80_2022.unix_code       = 40003
QCD_PT50to80_2022.EE              = 0   



QCD_PT80to120_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT80to120_2022")
QCD_PT80to120_2022.sigma           =  2534000.0 #pb
QCD_PT80to120_2022.year            = 2022
QCD_PT80to120_2022.dataset         = "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT80to120_2022.process         = "QCD_2022"
QCD_PT80to120_2022.unix_code       = 40004
QCD_PT80to120_2022.EE              = 0    


QCD_PT120to170_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT120to170_2022")
QCD_PT120to170_2022.sigma           = 445800.0 #pb
QCD_PT120to170_2022.year            = 2022
QCD_PT120to170_2022.dataset         = "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT120to170_2022.process         = "QCD_2022"
QCD_PT120to170_2022.unix_code       = 40005
QCD_PT120to170_2022.EE              = 0    

QCD_PT170to300_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT170to300_2022")
QCD_PT170to300_2022.sigma           = 113700.0 #pb
QCD_PT170to300_2022.year            = 2022
QCD_PT170to300_2022.dataset         = "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT170to300_2022.process         = "QCD_2022"
QCD_PT170to300_2022.unix_code       = 40006
QCD_PT170to300_2022.EE              = 0    




QCD_PT300to470_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT300to470_2022")
QCD_PT300to470_2022.sigma           = 7589.0 #pb
QCD_PT300to470_2022.year            = 2022
QCD_PT300to470_2022.dataset         = "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM"
QCD_PT300to470_2022.process         = "QCD_2022"
QCD_PT300to470_2022.unix_code       = 40007
QCD_PT300to470_2022.EE              = 0   

QCD_PT470to600_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT470to600_2022")
QCD_PT470to600_2022.sigma           = 626.4 #pb
QCD_PT470to600_2022.year            = 2022
QCD_PT470to600_2022.dataset         = "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT470to600_2022.process         = "QCD_2022"
QCD_PT470to600_2022.unix_code       = 40008
QCD_PT470to600_2022.EE              = 0   

QCD_PT600to800_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT600to800_2022")
QCD_PT600to800_2022.sigma           = 626.4 #pb
QCD_PT600to800_2022.year            = 2022
QCD_PT600to800_2022.dataset         = "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT600to800_2022.process         = "QCD_2022"
QCD_PT600to800_2022.unix_code       = 40009
QCD_PT600to800_2022.EE              = 0   


QCD_PT800to1000_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT800to1000_2022")
QCD_PT800to1000_2022.sigma           = 30.57 #pb
QCD_PT800to1000_2022.year            = 2022
QCD_PT800to1000_2022.dataset         = "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT800to1000_2022.process         = "QCD_2022"
QCD_PT800to1000_2022.unix_code       = 40009
QCD_PT800to1000_2022.EE              = 0   


QCD_PT1000to1400_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT1000to1400_2022")
QCD_PT1000to1400_2022.sigma           = 8.92 #pb
QCD_PT1000to1400_2022.year            = 2022
QCD_PT1000to1400_2022.dataset         = "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT1000to1400_2022.process         = "QCD_2022"
QCD_PT1000to1400_2022.unix_code       = 40010
QCD_PT1000to1400_2022.EE              = 0   




QCD_PT1400to1800_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT1400to1800_2022")
QCD_PT1400to1800_2022.sigma           = 0.8103 #pb
QCD_PT1400to1800_2022.year            = 2022
QCD_PT1400to1800_2022.dataset         = "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT1400to1800_2022.process         = "QCD_2022"
QCD_PT1400to1800_2022.unix_code       = 40010
QCD_PT1400to1800_2022.EE              = 0   


QCD_PT1800to2400_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT1800to2400_2022")
QCD_PT1800to2400_2022.sigma           = 0.1148 #pb
QCD_PT1800to2400_2022.year            = 2022
QCD_PT1800to2400_2022.dataset         = "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT1800to2400_2022.process         = "QCD_2022"
QCD_PT1800to2400_2022.unix_code       = 40010
QCD_PT1800to2400_2022.EE              = 0   



QCD_PT2400to3200_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT2400to3200_2022")
QCD_PT2400to3200_2022.sigma           = 0.007542 #pb
QCD_PT2400to3200_2022.year            = 2022
QCD_PT2400to3200_2022.dataset         = "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT2400to3200_2022.process         = "QCD_2022"
QCD_PT2400to3200_2022.unix_code       = 40010
QCD_PT2400to3200_2022.EE              = 0   


QCD_PT3200_2022                 = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT3200_2022")
QCD_PT3200_2022.sigma           = 0.0002331 #pb
QCD_PT3200_2022.year            = 2022
QCD_PT3200_2022.dataset         = "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM"
QCD_PT3200_2022.process         = "QCD_2022"
QCD_PT3200_2022.unix_code       = 40011
QCD_PT3200_2022.EE              = 0   



QCD_PT_2022                        = sample(ROOT.kGray, 1, 1001, "QCD", "QCD_PT_2022")
QCD_PT_2022.year                   = 2022
QCD_PT_2022.components             = [  
                                    QCD_PT15to30_2022, QCD_PT30to50_2022, QCD_PT50to80_2022,
                                    QCD_PT80to120_2022, QCD_PT120to170_2022, QCD_PT170to300_2022, 
                                    QCD_PT300to470_2022, QCD_PT470to600_2022,
                                    QCD_PT600to800_2022, QCD_PT800to1000_2022, QCD_PT1000to1400_2022,
                                    QCD_PT1400to1800_2022, QCD_PT1800to2400_2022, QCD_PT2400to3200_2022,
                                    QCD_PT3200_2022
                                ]

WtoLNu_4Jets_2022           = sample(ROOT.kYellow-3, 1, 1001, "W + LNu", "WtoLNu_4Jets_2022")
WtoLNu_4Jets_2022.dataset   = "/WtoLNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-WtoLNu_4Jets_2022_v1-0fa328e40e38f44cd311b92489b92b5b/USER"
WtoLNu_4Jets_2022.sigma     = 416.5
WtoLNu_4Jets_2022.year      = 2022
WtoLNu_4Jets_2022.process   = "WtoLNu_4Jets_2022"
WtoLNu_4Jets_2022.unix_code = 31308
WtoLNu_4Jets_2022.EE        = 0

WtoLNu_4Jets_4J_2022         = sample(ROOT.kYellow-3, 1, 1001, "W + LNu", "WtoLNu_4Jets_4J_2022")
WtoLNu_4Jets_4J_2022.dataset   = "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/apuglia-WtoLNu_4Jets_2022-0fa328e40e38f44cd311b92489b92b5b/USER"
WtoLNu_4Jets_4J_2022.sigma     = 416.5
WtoLNu_4Jets_4J_2022.year      = 2022
WtoLNu_4Jets_4J_2022.process   = "WtoLNu_4Jets_4J_2022"
WtoLNu_4Jets_4J_2022.unix_code = 31309
WtoLNu_4Jets_4J_2022.EE        = 0

################################ 2024 ################################

TT_Semilep_2024 = sample(ROOT.kOrange,1,1001,"t#bar{t}","TT_Semilep_2024")
TT_Semilep_2024.sigma = 404#pb
TT_Semilep_2024.year = 2024
TT_Semilep_2024.dataset = "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TT_Semilep_2024.process = "TTbar_semilep_2024"
TT_Semilep_2024.unix_code = 31100
TT_Semilep_2024.EE = 0

TT_Dileptonic_2024 = sample(ROOT.kOrange,1,1001,"t#bar{t}","TT_Dilep_2024")
TT_Dileptonic_2024.sigma = 96.6 #pb
TT_Dileptonic_2024.year = 2024
TT_Dileptonic_2024.dataset = "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
TT_Dileptonic_2024.process = "TT_Dileptonic_2024"
TT_Dileptonic_2024.unix_code = 31101
TT_Dileptonic_2024.EE = 0

TT_bar_2024 = sample (ROOT.kGreen-3,1,1001,"t#bar{t}","TT_bar_2024")
TT_bar_2024.year = 2024
TT_bar_2024.components = [TT_Semilep_2024,TT_Dileptonic_2024]


######################## adrnico #################
TT_hadr_2024                = sample(ROOT.kRed, 1, 1001, "t#bar{t}", "TT_hadr_2024")
TT_hadr_2024.sigma          = 422.3
TT_hadr_2024.year           = 2022
TT_hadr_2024.dataset        = "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
TT_hadr_2024.process        = 'TT_2022'
TT_hadr_2024.unix_code      = 31101
TT_hadr_2024.EE             = 0





################################ ZJets ################################


ZJetsToNuNu_HT100to200_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT100to200_2024")
ZJetsToNuNu_HT100to200_2024.sigma       = 273 #pb
ZJetsToNuNu_HT100to200_2024.year        = 2022
ZJetsToNuNu_HT100to200_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_HT100to200_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT100to200_2024.unix_code   = 31200
ZJetsToNuNu_HT100to200_2024.EE          = 0

ZJetsToNuNu_HT200to400_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT200to400_2024")
ZJetsToNuNu_HT200to400_2024.sigma       = 76.1 #pb
ZJetsToNuNu_HT200to400_2024.year        = 2022
ZJetsToNuNu_HT200to400_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"
ZJetsToNuNu_HT200to400_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT200to400_2024.unix_code   = 31201
ZJetsToNuNu_HT200to400_2024.EE          = 0

ZJetsToNuNu_HT400to800_2024             = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT400to800_2024")
ZJetsToNuNu_HT400to800_2024.sigma       = 13.2 #pb
ZJetsToNuNu_HT400to800_2024.year        = 2022
ZJetsToNuNu_HT400to800_2024.dataset     = "/Zto2Nu-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT400to800_2024.process     = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT400to800_2024.unix_code   = 31202
ZJetsToNuNu_HT400to800_2024.EE          = 0

ZJetsToNuNu_HT800to1500_2024            = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT800to1500_2024")
ZJetsToNuNu_HT800to1500_2024.sigma      = 1.37 #pb
ZJetsToNuNu_HT800to1500_2024.year       = 2022
ZJetsToNuNu_HT800to1500_2024.dataset    = "/Zto2Nu-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT800to1500_2024.process    = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT800to1500_2024.unix_code  = 31203
ZJetsToNuNu_HT800to1500_2024.EE         = 0

ZJetsToNuNu_HT1500to2500_2024           = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT1500to2500_2024")
ZJetsToNuNu_HT1500to2500_2024.sigma     = 0.0985 #pb
ZJetsToNuNu_HT1500to2500_2024.year      = 2022
ZJetsToNuNu_HT1500to2500_2024.dataset   = "/Zto2Nu-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT1500to2500_2024.process   = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT1500to2500_2024.unix_code = 31204
ZJetsToNuNu_HT1500to2500_2024.EE        = 0

ZJetsToNuNu_HT2500_2024                 = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_HT2500_2024")
ZJetsToNuNu_HT2500_2024.sigma           = 0.00669 #pb
ZJetsToNuNu_HT2500_2024.year            = 2022
ZJetsToNuNu_HT2500_2024.dataset         = "/Zto2Nu-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"
ZJetsToNuNu_HT2500_2024.process         = 'ZJetsToNuNu_2024'
ZJetsToNuNu_HT2500_2024.unix_code       = 31205
ZJetsToNuNu_HT2500_2024.EE              = 0

ZJetsToNuNu_2024                        = sample(ROOT.kAzure+6, 1, 1001, "ZJets #rightarrow #nu#nu", "ZJetsToNuNu_2024")
ZJetsToNuNu_2024.year                   = 2022
ZJetsToNuNu_2024.components             = [
                                            ZJetsToNuNu_HT100to200_2024,
                                            ZJetsToNuNu_HT200to400_2024,
                                            ZJetsToNuNu_HT400to800_2024,
                                            ZJetsToNuNu_HT800to1500_2024,
                                            ZJetsToNuNu_HT1500to2500_2024,
                                            ZJetsToNuNu_HT2500_2024 
                                            ]
