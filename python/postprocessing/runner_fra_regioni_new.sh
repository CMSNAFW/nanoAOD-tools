#!/usr/bin/bash 
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /afs/cern.ch/user/f/fscrivan/new/new2/CMSSW_14_1_0_pre4/src/
eval `scramv1 runtime -sh`


cd /afs/cern.ch/user/f/fscrivan/new/new2/CMSSW_14_1_0_pre4/src/PhysicsTools/NanoAODTools/python/postprocessing/examples/Tprime/
    
python3 pres.py -d $1 -l $4 -n $5

#GIRARE LE Z GLOBALI SIA NUOVE CHE VECCHIE REGIONI


#questo divrebbe unire il file di output e quello degli istogrammi
#hadd $2 $3 histOut$4.root

# Se sei all'ultimo file del dataset (es. file numero 50), fai il merge