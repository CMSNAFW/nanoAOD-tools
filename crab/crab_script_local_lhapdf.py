#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MET_HLT_Filter import *
from PhysicsTools.NanoAODTools.postprocessing.examples.preselection import *
from PhysicsTools.NanoAODTools.postprocessing.examples.highpt import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
#from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.LHAPDFWeightProducer import * 

metCorrector_tot = createJMECorrector(isMC=True, dataYear=2017, jesUncert='Total', redojec=True)
fatJetCorrector_tot = createJMECorrector(isMC=True, dataYear=2017, jesUncert='Total', redojec=True, jetType = 'AK8PFchs')
metCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', redojec=True)
fatJetCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', redojec=True, jetType = 'AK8PFchs')

#/store/mc/RunIIFall17NanoAODv6/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/270000/DAFDDE94-47A7-2246-A5DD-4832005E4371.root'
#/store/mc/RunIISummer16NanoAODv7/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1/70000/5C07EA76-5479-D042-BE17-2A55EE0F5846.root
#fnames=["/eos/home-o/oiorio/Wprime/toptag/nanoAODJMAR/nano102x_on_mini102x_2018_mc_NANO.root"]
fnames=["file:/tmp/oiorio/tree_hadd_1.root"]
p = PostProcessor('.', fnames, '', modules=[LHAPDFWeight_NNPDF(),LHAPDFWeight_PDF4LHC15(),MCweight_writer(LHAPDFs=['LHANNPDF','LHAPDF4LHC15'])], outputbranchsel=os.path.abspath('../scripts/keep_and_drop.txt'), histFileName="histOut.root", histDirName="plots", provenance=True, maxEntries=10000, fwkJobReport=True)
#p = PostProcessor('.', fnames, '', modules=[LHAPDFWeight_NNPDF(),MCweight_writer()], outputbranchsel=os.path.abspath('../scripts/keep_and_drop.txt'), histFileName="histOut.root", histDirName="plots", provenance=True, maxEntries=1000, fwkJobReport=True)

p.run()
print 'DONE'
#, PrefCorr(), metCorrector(), fatJetCorrector()
