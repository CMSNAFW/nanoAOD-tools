python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_partM_nominal>=50 && FatJet_partM_nominal<110 && FatJet_pt_nominal[0]>=500"   -p --fit -L "muon" -y "2018" &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_partM_nominal>=50 && FatJet_partM_nominal<110 && FatJet_pt_nominal[0]>=500"   -p --fit -L "electron" -y "2018" 

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_partM_nominal>=110 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018" &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_partM_nominal>=110 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018" 

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_partM_nominal>=50 && FatJet_partM_nominal<110 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018" &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_partM_nominal>=50 && FatJet_partM_nominal<110 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018" 

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_partM_nominal>=110 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018"  &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==2  && top_region_nominal==-1 && FatJet_partM_nominal>=110 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018" 

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==0 && Top_TvsQCD_nominal>0.6 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018"  &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==0 && Top_TvsQCD_nominal>0.6 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018"

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==1 && Top_TvsQCD_nominal>0.6 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018"  &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==1 && Top_TvsQCD_nominal>0.6 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018"

python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500" -p --fit -L "muon" -y "2018"  &
python makeplot.py  -f UL_v12_pnm -S "all"  -C "(N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==0  && top_region_nominal==-1 && FatJet_pt_nominal[0]>=500" -p --fit -L "electron" -y "2018"
