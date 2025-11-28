"""
#!/usr/bin/env python3
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopcandidate_v2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopevaluate import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoprepro_v2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.GenPart_MomFirstCp import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.preselection import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
import sys

fnames = [sys.argv[1]]
label = sys.argv[4]

if 'QCD' in fnames[0]:
    p=PostProcessor(".",fnames,modules=[MCweight_writer(), preselection(), nanoTopcand(), nanoTopevaluate()],  provenance=True, histFileName="histOut"+label+".root", histDirName="plots", maxEntries=10)
else:
    p=PostProcessor(".",fnames,modules=[MCweight_writer(), preselection(), GenPart_MomFirstCp(flavour="-5,-4,-3,-2,-1,1,2,3,4,5,6,-6,24,-24"),nanoprepro(),nanoTopcand(), nanoTopevaluate()], provenance=True, histFileName="histOut"+label+".root", histDirName="plots", maxEntries=10)
p.run()
"""
#new modules and postprocessor for 2024 samples
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object 
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopcandidate_v2 import nanoTopcand 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoprepro_v2 import nanoprepro 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.GenPart_MomFirstCp import GenPart_MomFirstCp 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.nanoTopEvaluate_MultiScore_v2 import nanoTopevaluate_MultiScore from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.MCweight_writer import MCweight_writer 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.Selection import * 
from PhysicsTools.NanoAODTools.postprocessing.modules.common.preselection import *

#Postprocessor for the Data with option isMC = 0
#p = PostProcessor("", files, cut="",   modules=[Selection(), preselection(),  nanoTopcand(isMC=0),nanoTopevaluate_MultiScore(year = 2022, isMC=0)], noOut=False, haddFileName="", histFileName="", histDirName="./")
#p.run()
#Postprocessor for the MonteCarlo samples
p = PostProcessor("", files, cut="", modules=[Selection(), preselection(),  GenPart_MomFirstCp(), nanoprepro(),nanoTopcand(),nanoTopevaluate_MultiScore(year = 2022) ], noOut=False, haddFileName="", histFileName="", histDirName="./")
p.run()

