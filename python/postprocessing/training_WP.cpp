float training_WP_cut(bool pt, int lep, int dir, float cut){
  TFile *f = TFile::Open("score.root");
  TTree *tree = (TTree *) f->Get("events_nominal");

  Float_t pt1[1]; tree->SetBranchAddress("Top_pt1_wp90_nominal",&pt1);
  Float_t pt2[1]; tree->SetBranchAddress("Top_pt2_wp90_nominal",&pt2);
  Float_t pt3[1]; tree->SetBranchAddress("Top_pt3_wp90_nominal",&pt3);
  Float_t pt4[1]; tree->SetBranchAddress("Top_pt4_wp90_nominal",&pt4);

  Int_t flavour1[1]; tree->SetBranchAddress("Top_flavour1_wp90_nominal",&flavour1);
  Int_t flavour2[1]; tree->SetBranchAddress("Top_flavour2_wp90_nominal",&flavour2);
  Int_t flavour3[1]; tree->SetBranchAddress("Top_flavour3_wp90_nominal",&flavour3);
  Int_t flavour4[1]; tree->SetBranchAddress("Top_flavour4_wp90_nominal",&flavour4);

  Int_t MC1[1]; tree->SetBranchAddress("Top_MC1_wp90_nominal",&MC1);
  Int_t MC2[1]; tree->SetBranchAddress("Top_MC2_wp90_nominal",&MC2);
  Int_t MC3[1]; tree->SetBranchAddress("Top_MC3_wp90_nominal",&MC3);
  Int_t MC4[1]; tree->SetBranchAddress("Top_MC4_wp90_nominal",&MC4);

  Float_t isMerg1[1]; tree->SetBranchAddress("Top_isMerg1_wp90_nominal",&isMerg1);
  Float_t isMerg2[1]; tree->SetBranchAddress("Top_isMerg2_wp90_nominal",&isMerg2);
  Float_t isMerg3[1]; tree->SetBranchAddress("Top_isMerg3_wp90_nominal",&isMerg3);
  Float_t isMerg4[1]; tree->SetBranchAddress("Top_isMerg4_wp90_nominal",&isMerg4);

  Float_t Score1[1]; tree->SetBranchAddress("Top_Score1_wp90_nominal",&Score1);
  Float_t Score2[1]; tree->SetBranchAddress("Top_Score2_wp90_nominal",&Score2);
  Float_t Score3[1]; tree->SetBranchAddress("Top_Score3_wp90_nominal",&Score3);
  Float_t Score4[1]; tree->SetBranchAddress("Top_Score4_wp90_nominal",&Score4);

  int N_flase=0,N_false_select=0;

  for(int i=0; i< tree->GetEntries();i++){
    tree->GetEntry(i);
    //std::cout<<flavour1[0]<<" "<<isMerg1[0]<<" "<<MC1[0]<<std::endl; 
    if(abs(flavour1[0])==lep && isMerg1[0]==dir && MC1[0]==0){
      if(pt == false){
        if(pt1[0]>=0 && pt1[0]<500 ){
          N_flase++;
          if(Score1[0]>=cut)N_false_select++;
        }
      }
      else{
        if(pt1[0]>=500){
          N_flase++;
          if(Score1[0]>=cut)N_false_select++;
        } 
      }
    }

    if(abs(flavour2[0])==lep && isMerg2[0]==dir && MC2[0]==0){
      if(pt == false){
        if(pt2[0]>=0 && pt2[0]<500 ){
          N_flase++;
          if(Score2[0]>=cut)N_false_select++;
        }
      }
      else{
	if(pt2[0]>=500){
          N_flase++;
          if(Score2[0]>=cut)N_false_select++;
        }
      }
    }

    if(abs(flavour3[0])==lep && isMerg3[0]==dir && MC3[0]==0){
      if(pt == false){
        if(pt3[0]>=0 && pt3[0]<500 ){
          N_flase++;
          if(Score3[0]>=cut)N_false_select++;
        }
      }
      else{
	if(pt3[0]>=500){
          N_flase++;
          if(Score3[0]>=cut)N_false_select++;
        }
      }
    }

    if(abs(flavour4[0])==lep && isMerg4[0]==dir && MC4[0]==0){
      if(pt == false){
        if(pt4[0]>=0 && pt4[0]<500 ){
          N_flase++;
          if(Score4[0]>=cut)N_false_select++;
        }
      }
      else{
        if(pt4[0]>=500){
          N_flase++;
          if(Score4[0]>=cut)N_false_select++;
        }
      }
    }

  }
  std::cout<<N_flase<<" "<<N_false_select<<std::endl;
  return float(N_false_select)/float(N_flase);
 }

void training_WP(){
  //std::cout<<training_WP_cut(false, 13, 0, 0.6)<<std::endl;
  std::cout<<training_WP_cut(false, 11, 0, 0.6)<<std::endl;
  std::cout<<training_WP_cut(false, 13, 1, 0.6)<<std::endl;
  std::cout<<training_WP_cut(false, 13, 1, 0.6)<<std::endl;
}
