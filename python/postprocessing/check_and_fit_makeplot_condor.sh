#!/bin/bash                                                                                                                                                                                                
cd /afs/cern.ch/user/f/fcarneva/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing/
eval `scramv1 runtime -sh`
#python makeplot.py  -f UL_v12 --mertree --lumi -y "2017" # --merpart 
#python makeplot.py  -f UL_v14 --mertree --lumi -y "2018"  

#python makeplot.py  -f UL_v13 --mertree --lumi -y "2016preVFP" &
#python makeplot.py  -f UL_v13 --mertree --lumi -y "2016postVFP"
#python makeplot.py  -f UL_v13 --mer2016 -y "2016"

#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p  -y "2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2017"  #"2018" 
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p  -y "2017" #"2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2016"  #"2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p -y "2016" #"2018"


#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -s -p -y "2016" 
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -s -p  -y "2016" 
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -s -p -y "2017"  #"2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -s -p  -y "2017" #"2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -s -p -y "2018"  #"2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -s -p -y "2018" #"2018"


#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2018"


#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2017"

#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"
#python makeplot.py  -f UL_v17 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0 && Fwd4_region_nominal==0 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140 && FatJet_pt_nominal[0]>=500"  -p -y "2016"




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


#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0" -p -s -y "2016" #--fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal==0" -p -s -y "2016" #--fit
###Cambia variabile in Top_M_nominal!!!
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal>=80" -p -s -y "2016" #--fit


### New fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016" 
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s  -p --fit -y "2016" 
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016" 
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016"  


#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2017"
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s  -p --fit -y "2017"
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2017"
#python makeplot.py  -f UL_v11 -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2017"

#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500"  -y "2016" -d "ST_2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" -d "ST_2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016" -d "ST_2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"   --fit -L "muon" -y "2016" -d "ST_2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"   --fit -L "electron" -y "2016" -d "ST_2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" -d "ST_2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016" -d "ST_2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" -d "ST_2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016" -d "ST_2016"


#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "muon" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500"  -y "2016" --fit -L "electron"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"   --fit -L "muon" -y "2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"   --fit -L "electron" -y "2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016"

#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"  --fit -L "muon" -y "2016" &
#python makeplot.py  -f UL_v11  "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500"  --fit -L "electron" -y "2016"


##fit AK8 pt>500

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit
###Cambia variabile in Top_M_nominal!!!
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal>=80 && FatJet_pt_nominal[0]>=500" -p -s -y "2016" #--fit


#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit
###Cambia variabile in Top_M_nominal!!!
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal>=80 && FatJet_pt_nominal[0]>=500" -p -s -y "2017" #--fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal==0 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit
###Cambia variabile in Top_M_nominal!!!
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal>=80 && FatJet_pt_nominal[0]>=500" -p -s -y "2018" #--fit





####Fit ParNett, cambia in UL_v12!!!!!!!!!!!!!!!!!####

##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016" #"2018"
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s  -p --fit -y "2016"  #"2018"

##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016"  #"2018"
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2016"  #"2018"


##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit  -y "2018"
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s  -p --fit -y "2018"

##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2018" 
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2018" 

##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit  -y "2017"
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s  -p --fit -y "2017"

##python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2017"
#python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && FatJet_pt_nominal[0]>=500" -s -p --fit -y "2017"
