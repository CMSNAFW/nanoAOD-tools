
void draw_mass(){
  TFile *f =TFile::Open("/eos/user/f/fcarneva/Tprime/nosynch/UL2018_final1/QCD_2018/QCD_2018.root");
  TTree *tree = (TTree *) f->Get("events_nominal");

  Float_t top_mass[1];tree->SetBranchAddress("Top_M1_wp99_nominal",&top_mass);
  Float_t top_pt[1];tree->SetBranchAddress("Top_pt1_wp99_nominal",&top_pt);
  Float_t top_eta[1];tree->SetBranchAddress("Top_eta1_wp99_nominal",&top_eta);
  Float_t top_phi[1];tree->SetBranchAddress("Top_phi1_wp99_nominal",&top_phi);

  Int_t top_reg[1]; tree->SetBranchAddress("top_region_nominal",&top_reg);
  Int_t ak8_reg[1]; tree->SetBranchAddress("AK8_region_nominal",&ak8_reg);
  Float_t w[1]; tree->SetBranchAddress("w_nominal",&w);


  Float_t fj_mass[1];tree->SetBranchAddress("FatJet_M1_nominal",&fj_mass);
  Float_t fj_pt[1];tree->SetBranchAddress("FatJet_pt1_nominal",&fj_pt);
  Float_t fj_eta[1];tree->SetBranchAddress("FatJet_eta1_nominal",&fj_eta);
  Float_t fj_phi[1];tree->SetBranchAddress("FatJet_phi1_nominal",&fj_phi);

  TH1F *h =new TH1F("h","h",100,1,-1);
  for (int i=0; i<tree->GetEntries();i++){


    tree->GetEntry(i);
    if(top_reg[0]==1 && ak8_reg[0]==2){
      TLorentzVector t,fj;
      t.SetPtEtaPhiM(top_pt[0],top_eta[0],top_phi[0],top_mass[0]);
      fj.SetPtEtaPhiM(fj_pt[0],fj_eta[0],fj_phi[0],fj_mass[0]);
      TLorentzVector T= t+fj;
      h->Fill(T.M(),w[0]);
      //std::cout<<top_pt[0]<<top_eta[0]<<top_phi[0]<<top_mass[0]<<std::endl;
    }
  }

  h->Draw();
}
