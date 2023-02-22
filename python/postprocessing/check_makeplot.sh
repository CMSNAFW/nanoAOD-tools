#python makeplot.py  -f UL_v3 -S "noSyst"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal>=500" -p  -s     
#python makeplot.py  -f UL_v3 -S "noSyst"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal>=500" -p  -s     
#python makeplot.py  -f UL_v3 -S "noSyst"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==0 && Top_pt_nominal<500" -p  -s
#python makeplot.py  -f UL_v3 -S "noSyst"  -C "Top_TvsQCD_nominal>0.6 && (N_muLoose_nominal+N_elLoose_nominal)==0 &&  AK8_region_nominal==0 && Top_isMerg_nominal==1 && Top_pt_nominal<500" -p  -s
python makeplot.py  -f UL_v4 -y "2018" --mertree --merpart --lumi -d "WJets_2018"
python makeplot.py  -f UL_v4 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && (TightMu_pt_nominal!=0 || TightEl_pt_nominal!=0) " -s -y "2018" -p
python makeplot.py  -f UL_v4 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 " -s -y "2018" -p
python makeplot.py  -f UL_v4 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && top_region_nominal==-1 && AK8_region_nominal==0" -s -y "2018" -p
#python makeplot.py  -f UL_v4 -S "noSyst"  -C " (N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0"  -s -y "2018" -p
