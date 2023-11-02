#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MET_HLT_Filter import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.unpacking_vers2 import *
from PhysicsTools.NanoAODTools.postprocessing.examples.preselection_Tprime  import *
from PhysicsTools.NanoAODTools.postprocessing.examples.HLT_Filter  import *
from PhysicsTools.NanoAODTools.postprocessing.examples.GenPart_MomFirstCp import *
from PhysicsTools.NanoAODTools.postprocessing.examples.scoring import *

metCorrector_tot = createJMECorrector(isMC=True, dataYear=2018, jesUncert='Total', redojec=True)
fatJetCorrector_tot = createJMECorrector(isMC=True, dataYear=2018, jesUncert='Total',redojec=True)
metCorrector = createJMECorrector(isMC=True, dataYear=2018, jesUncert='All',redojec=True)
fatJetCorrector = createJMECorrector(isMC=True, dataYear=2018, jesUncert='All',redojec=True)

p = PostProcessor('/eos/home-f/fcarneva/public/', [#'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/68514DBB-6D58-9D40-B27A-1396FA185B1E.root'
                        #'/eos/home-f/fcarneva/public/52C9021B-19EA-B447-A010-77B033538D9F.root',
                        #'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/F42DD439-A135-E642-AAB1-E39F306458AC.root',
                        #'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18NanoAODv9/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2500000/2F9B15BD-907C-5F48-961D-5B0605F4927E.root'
                        "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL16NanoAODAPVv9/TprimeBToTH_TLep_Hbb_LH_MT600_MH25_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/2810000/3238B9FC-2C63-9E45-A737-F2E659EE13A5.root" 
                    ],'', modules=[
                        #metCorrector(),metCorrector_tot(),fatJetCorrector(), fatJetCorrector_tot()
                        MCweight_writer(),MET_HLT_Filter(2016), preselection_Tprime(), GenPart_MomFirstCp(flavour="11,12,13,14,15,16,5,6,24,23,25"), unpacking_MC(),#scoring(),  
                        metCorrector(), fatJetCorrector(), metCorrector_tot(), fatJetCorrector_tot(),puAutoWeight_2016(),PrefCorr_2016(),TightlepSF_2016preVFP(),IsoLooselepSF_2016preVFP(),LooselepSF_2016preVFP()], outputbranchsel=os.path.abspath('../scripts/keep_and_drop.txt'), histFileName="histOut.root", histDirName="plots", maxEntries=30, provenance=True, fwkJobReport=True)
p.run()
print 'DONE'
#, PrefCorr(), metCorrector(), fatJetCorrector()
