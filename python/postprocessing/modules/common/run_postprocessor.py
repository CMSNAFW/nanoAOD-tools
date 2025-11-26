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
from PhysicsTools.NanoAODTools.postprocessing.modules.common.genlevel_analysis import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
import sys

fnames = ["/eos/user/o/oiorio/tDM/13p6TeV/TT_Inclusive.root"]
label = "test"

p=PostProcessor(".",fnames,modules=[GenPart_MomFirstCp(flavour="-5,-4,-3,-2,-1,1,2,3,4,5,6,-6,24,-24"),genlevel_analysis()], provenance=True, histFileName="histOut"+label+".root", histDirName="plots", haddFileName='tree_hadd'+label+".root",maxEntries=3)
p.run()

