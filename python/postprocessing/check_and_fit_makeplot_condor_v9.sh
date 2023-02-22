#!/bin/bash                                                                                                                                                                                                
cd /afs/cern.ch/user/f/fcarneva/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing/
eval `scramv1 runtime -sh`
#python makeplot.py  -f UL_v5 -y "2018" --mertree --merpart --lumi
#check
#python makeplot.py  -f UL_v5 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && (TightMu_pt_nominal!=0 || TightEl_pt_nominal!=0) " -s -y "2018" -p
#python makeplot.py  -f UL_v5 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 " -s -y "2018" -p
#python makeplot.py  -f UL_v5 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0" -s -y "2018" -p

#fit
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==2 && top_region_nominal==-1 " -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==1 && top_region_nominal==-1" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1" -p --fit -s

#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==2 && top_region_nominal==-1 && FatJet_M_nominal<50 " -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==1 && top_region_nominal==-1 && FatJet_M_nominal<50" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && FatJet_M_nominal<50" -p --fit -s

#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==2 && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==1 && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -p --fit -s

#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==2 && top_region_nominal==-1  && FatJet_M_nominal>=110" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==1 && top_region_nominal==-1 && FatJet_M_nominal>=110" -p --fit -s
#python makeplot.py  -f UL_v5 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  top_region_nominal==-1 && FatJet_M_nominal>=110" -p --fit -s


python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1" -p --fit -s
python makeplot.py  -f UL_v5 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1" -p --fit -s
