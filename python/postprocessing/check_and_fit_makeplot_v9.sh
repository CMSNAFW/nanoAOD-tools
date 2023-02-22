#Initialization
python makeplot.py  -f UL_v9 -y "2018" --mertree --merpart --lumi

# Fit AK8 Mass

#python makeplot.py  -f UL_v9 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p   
python makeplot.py  -f UL_v9 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p --fit
python makeplot.py  -f UL_v9 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_M_nominal>=110 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p --fit

#python makeplot.py  -f UL_v9 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal<50 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p
python makeplot.py  -f UL_v9 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=50 && FatJet_M_nominal<110 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p --fit
python makeplot.py  -f UL_v9 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_M_nominal>=110 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1)" -s -y "2018" -p --fit



#Final Fit
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==0" -s -y "2018" -p 
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==0" -s -y "2018" -p
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1" -s -y "2018" -p
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1" -s -y "2018" -p
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==1 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140" -s -y "2018" -p
#python makeplot.py  -f UL_v10 -S "all"  -C " Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==0 && Fwd4_region_nominal==1 && FatJet_M_nominal>=100 && FatJet_M_nominal<=140" -s -y "2018" -p



#Fit Met BDT SF

python makeplot.py  -f UL_v9 -S "all"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0" -s -y "2018" -p --fit
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s --fit
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==0" -p -s --fit 
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==0" -p -s --fit 
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==0" -p -s --fit 

python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s --fit 
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500 && top_region_nominal==1" -p -s --fit 
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500 && top_region_nominal==1" -p -s --fit 
python makeplot.py  -f UL_v9 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500 && top_region_nominal==1" -p -s --fit 
