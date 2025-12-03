#!/usr/bin/env python3
import os
import sys
import ROOT
import math
import subprocess
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from Corrections_2024 import get_SF_modules
from PhysicsTools.NanoAODTools.postprocessing.modules.Pre_Selection import Pre_Selection

# Important variables for the analysis
fnames = [sys.argv[1]]
label = sys.argv[2]
folder_histo_events = sys.argv[3]
label_part = sys.argv[4]

# Import modules for post-processor
modules = get_SF_modules()
modules.append(Pre_Selection())

# Create output folder
output_analysis = label
output_path = '/eos/user/c/cdifraia/tWb_CKM/' + output_analysis
os.makedirs(output_path, exist_ok=True)

p = PostProcessor(
    '/eos/user/c/cdifraia/tWb_CKM/' + output_analysis,
    fnames,
    modules = modules,
    noOut = False,
    postfix = '_' + label_part,
    maxEntries=100,
    outputbranchsel=os.path.abspath('./keep_and_drop.txt')
)

p.run()
