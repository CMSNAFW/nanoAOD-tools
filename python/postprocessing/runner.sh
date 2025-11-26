#!/usr/bin/bash 
cd /afs/cern.ch/user/f/fscrivan/new/new2/CMSSW_14_1_0_pre4/src/PhysicsTools/NanoAODTools/python/postprocessing/examples/nuova_reg/controllo/
export XRD_NETWORKSTACK=IPv4
python3 control_region_Z.py $1 $2 $3 $4
hadd $2 $3 histOut$4.root
