#!/bin/bash 
cd /afs/cern.ch/user/f/fcarneva/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing
eval `scramv1 runtime -sh` 
python tree_skimmer_Tprime_final_newselection.py Tprime_tHq_1800LH_2018 1 root://cms-xrd-global.cern.ch//store/user/fcarneva/Tprime/TprimeBToTH_M-1800_LH_TuneCP5_PSweights_13TeV-madgraph_pythia8/Tprime_tHq_1800LH_2018/220907_094555/0000/tree_hadd_2.root /eos/user/f/fcarneva/Tprime/nosynch/UL_v10/Tprime_tHq_1800LH_2018 BDT_Tprime
rm runner_Tprime_tHq_1800LH_2018_1.sh