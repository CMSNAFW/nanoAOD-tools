#!/bin/bash                                                                                                                                                                                                
cd /afs/cern.ch/user/f/fcarneva/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing/
eval `scramv1 runtime -sh`
#python makeplot.py  -f UL_v12 --mertree --merpart --lumi -y "2018" #"2018"


#python makeplot.py  -f UL_v12 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2018"
#python makeplot.py  -f UL_v12 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p  -y "2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2017" #"2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p  -y "2017" #"2018"



#python makeplot.py  -f UL_v13 -S "noSyst"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==1" -s -p -y "2017" #"2018"
#python makeplot.py  -f UL_v13 -S "noSyst"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==0" -s -p  -y "2017" #"2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140" -s -p -y "2017" #"2018"
#python makeplot.py  -f UL_v13 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140" -s -p -y "2017" #"2018"


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


#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0" -p -s -y "2017" --fit

#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1" -p -s -y "2017" --fit
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal==0" -p -s -y "2017" --fit
###Cambia variabile in Top_M_nominal!!!
#python makeplot.py  -f UL_v11 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0 && Top_M_nominal>=80" -p -s -y "2017" --fit


####Fit ParNett, cambia in UL_v12!!!!!!!!!!!!!!!!!####

#python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
##python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -s -p --fit -L "electron" -y "2017" #"2018"
##python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 " -s  -p --fit -L "electron" -y "2017" #"2018"

#python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
##python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -s -p --fit -L "electron" -y "2017" #"2018"
##python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110" -s -p --fit -L "electron" -y "2017" #"2018"


#python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -s -p --fit  -y "2018"
python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 " -s  -p --fit -L "electron" -y "2018"

#python makeplot.py  -f UL_v12 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110" -s -p --fit -y "2018"
python makeplot.py  -f UL_v12 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110" -s -p --fit -L "electron" -y "2018"
