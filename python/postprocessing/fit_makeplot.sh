#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 " -p --fit
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0" -p --fit
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0" -p --fit
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && AK8_region_nominal==1" -p --fit
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && AK8_region_nominal==2" -p --fit

#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500" -p --fit -s

#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==0" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==0" -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==0 && Top_isMerg_nominal==1 " -p --fit -s
#python makeplot.py  -f UL_v3 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==1 && AK8_region_nominal==0 && Top_isMerg_nominal==1" -p --fit -s

#train per train but FatJet Veto
python makeplot.py  -f UL_v4 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500" -p --fit -s
python makeplot.py  -f UL_v4 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500" -p --fit -s
python makeplot.py  -f UL_v4 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500" -p --fit -s
python makeplot.py  -f UL_v4 -S "all"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500" -p --fit -s
