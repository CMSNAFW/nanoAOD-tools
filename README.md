# nanoAOD-tools
Tools for working with NanoAOD (requiring only python + root, not CMSSW)

## Checkout instructions: standalone

Note that you can also find the github.io page with all instructions here:

    https://cmsnafw.github.io/nanoAOD-tools/

You need to setup python 2.7 and a recent ROOT version first.

    git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git NanoAODTools
    cd NanoAODTools
    bash standalone/env_standalone.sh build
    source standalone/env_standalone.sh

Repeat only the last command at the beginning of every session.

Please never commit neither the build directory, nor the empty init.py files created by the script.

## Checkout instructions: CMSSW_10_6_27

    cmsrel CMSSW_10_6_27
    cd CMSSW_10_6_27/src
    git clone -b Tprime https://github.com/CMSNAFW/nanoAOD-tools.git PhysicsTools/NanoAODTools
    cd PhysicsTools/NanoAODTools
    cmsenv
    scram b -j 10

## General instructions to run on CRAB

Crab modules for the PostProcessor are already setted.

To submit jobs on crab you need to run the "submit_crab.py" scrip:
    
    python submit_crab.py -d <dataset.label> -s

for example
    
     python submit_crab.py -d TT_dilep_2016postVFP -s
     
The dataset.label could be found here:

CMSSW_10_6_27/src/PhysicsTools/NanoAODTools/python/postprocessing/samples/samples.py

To more samples you can edit "submit_crab_all.sh" and run it directly:

    source submit_crab_all.sh

Other useful options:

--status, to check the status of yout jobs:
    
    python submit_crab.py -d <dataset.label> --status

-r, to resubmit your failed jobs:

    python submit_crab.py -d <dataset.label> -r
    
-g, to get the .txt file with the list of the output(s) location(s)

    python submit_crab.py -d <dataset.label> -g

The .txt can be found here:

CMSSW_10_6_27/src/PhysicsTools/NanoAODTools/crab/macros/files/<dataset.label>.txt
    




