void compute_efficency_el(std::string trig, std::string file){
	TFile *f = TFile::Open((file).c_str());
	TTree *tree = (TTree *) f->Get("Events");
	double eff=0.,n=0, d=0 ; 
	n=tree->GetEntries(("Top_wp90==1 && Top_el_index>=-1 && Top_High_Truth==0 && "+trig).c_str());
	d=	tree->GetEntries("Top_wp90==1 && Top_el_index>=-1 && Top_High_Truth==0");
	eff = n/d;
	std::cout<< file << " " << trig << " " << eff << std::endl;

}

void search_trig(){
	std::vector<std::string> files = {"/eos/user/f/fcarneva/Tprime/nosynch/signal/Tprime_tHq_600LH_2018/Tprime_tHq_600LH_2018_part0.root",
			"/eos/user/f/fcarneva/Tprime/nosynch/signal/Tprime_tHq_1200LH_2018/Tprime_tHq_1200LH_2018_part0.root",
			"/eos/user/f/fcarneva/Tprime/nosynch/signal/Tprime_tHq_1800LH_2018/Tprime_tHq_1800LH_2018_part0.root"};
	std::vector<std::string> trig = {"HLT_Ele27_WPTight_Gsf",
					//"(HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon75 || HLT_Ele27_WPTight_Gsf || HLT_Mu37_TkMu27 || HLT_Mu37_Ele27_CaloIdL_MW || HLT_PFHT680)",
					//"(HLT_PFHT680 || HLT_Ele27_WPTight_Gsf || HLT_Mu37_TkMu27)",
					"( HLT_Mu50 || HLT_IsoMu24 || HLT_Ele27_WPTight_Gsf || HLT_Photon200 || HLT_AK8PFJet360_TrimMass30)"};//HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4  )"}; //|| HLT_AK8PFJet500 ) "};
	for(int i=0; i< files.size(); i++){
		for(int j=0; j < trig.size(); j++) compute_efficency_el(trig[j],files[i]);
	}
}