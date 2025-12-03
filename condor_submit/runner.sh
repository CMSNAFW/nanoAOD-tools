#!/usr/bin/bash
cd /afs/cern.ch/user/c/cdifraia/ 
source /cvmfs/cms.cern.ch/cmsset_default.sh 
cd CMSSW_15_0_17/src 
eval `scramv1 runtime -sh` 
cmsenv
cd PhysicsTools/NanoAODTools/condor_submit
export XRD_NETWORKSTACK=IPv4
python3 run_postproccesor.py $1 $2 $3 $4 
