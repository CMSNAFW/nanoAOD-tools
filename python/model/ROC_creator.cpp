#include <TFile.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TGraph.h>
#include <TMultiGraph.h>
#include <TLegend.h>
#include <TAxis.h>
#include <TStyle.h>

void ROC_creator_filesTvsQCD(string filename, string title ,string name, float cut){

  TFile* file = new TFile((filename).c_str(),"READ");
TTree* tree = (TTree*) file->Get("scores");

Long64_t true_label;
float score0;
tree->SetBranchAddress("Truth",&true_label);
tree->SetBranchAddress("Score0",&score0);

TH1F* sig_scores = new TH1F("sig_scores","Signal Scores",100,0,1);
TH1F* bkg_scores = new TH1F("bkg_scores","Background Scores",100,0,1);

tree->Draw("Score2/(1-Score1)>>sig_scores","Truth==2");
tree->Draw("Score2/(1-Score1)>>bkg_scores","Truth==0");

 TLine *l = new TLine(1,0,1,1);
TGraph* roc_curve = new TGraph();
float eff_sig[sig_scores->GetNbinsX()+2];
float eff_bkg[sig_scores->GetNbinsX()+2];
for (int i=0;i<sig_scores->GetNbinsX()+2;i++) {
  eff_sig[i] = sig_scores->Integral(i,sig_scores->GetNbinsX()+1)/sig_scores->Integral(1,sig_scores->GetNbinsX()+1);
  eff_bkg[i] = bkg_scores->Integral(i,bkg_scores->GetNbinsX()+1)/bkg_scores->Integral(1,bkg_scores->GetNbinsX()+1);
  roc_curve->SetPoint(i,eff_bkg[i],eff_sig[i]);
  if(i==(cut*100)){
    l->SetX1(eff_bkg[i]);
    l->SetX2(eff_bkg[i]);
  }
 }

TCanvas* c1 = new TCanvas();
TMultiGraph* mg = new TMultiGraph();
 roc_curve->SetLineWidth(2);
 mg->SetTitle(("ROC Curve TvsQCD "+title).c_str());
mg->Add(roc_curve,"l");
mg->Draw("a");
mg->GetXaxis()->SetTitle("Background (TopQCD) Efficiency");
mg->GetYaxis()->SetTitle("Signal Efficiency");
 mg->GetXaxis()->SetRangeUser(0,1);
 mg->GetYaxis()->SetRangeUser(0,1.02);

 l->SetLineColor(kRed);
 l->SetLineWidth(2);
 l->Draw("same");

//c1->BuildLegend();
 c1->SaveAs((name+"_ROC_TvsQCD.pdf").c_str());
 c1->SaveAs((name+"_ROC_TvsQCD.png").c_str());
 c1->SaveAs((name+"_ROC_TvsQCD.C").c_str());


  }


void ROC_creator_filesTvsOth(string filename, string title ,string name, float cutL,float cutT, float cutQCD){

  TFile* file = new TFile((filename).c_str(),"READ");
  TTree* tree = (TTree*) file->Get("scores");

  Long64_t true_label;
  float score0;
  tree->SetBranchAddress("Truth",&true_label);
  tree->SetBranchAddress("Score0",&score0);

  TH1F* sig_scores = new TH1F("sig_scores","Signal Scores",100,0,1);
  TH1F* bkg_scores = new TH1F("bkg_scores","Background Scores",100,0,1);

  tree->Draw("Score2/(1-Score0)>>sig_scores",("Truth==2 && Score2/(1-Score1)>"+std::to_string(cutQCD)).c_str());
  tree->Draw("Score2/(1-Score0)>>bkg_scores",("Truth==1 && Score2/(1-Score1)>"+std::to_string(cutQCD)).c_str());

  TLine *lL = new TLine(1,0,1,1);
  TLine *lT = new TLine(1,0,1,1);
  TGraph* roc_curve = new TGraph();
  float eff_sig[sig_scores->GetNbinsX()+2];
  float eff_bkg[sig_scores->GetNbinsX()+2];
  for (int i=0;i<sig_scores->GetNbinsX()+2;i++) {
    eff_sig[i] = sig_scores->Integral(i,sig_scores->GetNbinsX()+1)/sig_scores->Integral(1,sig_scores->GetNbinsX()+1);
    eff_bkg[i] = bkg_scores->Integral(i,bkg_scores->GetNbinsX()+1)/bkg_scores->Integral(1,bkg_scores->GetNbinsX()+1);
    roc_curve->SetPoint(i,eff_bkg[i],eff_sig[i]);
    //std::cout<<i<<std::endl;
    if(i==((int)(cutL*100))){
      //std::cout<<i<<std::endl;
      lL->SetX1(eff_bkg[i]);
      lL->SetX2(eff_bkg[i]);
    }
    if(i==(cutT*100)){
      lT->SetX1(eff_bkg[i]);
      lT->SetX2(eff_bkg[i]);
    }


  }
  //std::cout<< cutL*100<<std::endl;

  TCanvas* c1 = new TCanvas();
  TMultiGraph* mg = new TMultiGraph();
  roc_curve->SetLineWidth(2);
  mg->SetTitle(("ROC Curve TvsOth "+title).c_str());
  mg->Add(roc_curve,"l");
  mg->Draw("a");
  mg->GetXaxis()->SetTitle("Background (TopOth) Efficiency");
  mg->GetYaxis()->SetTitle("Signal Efficiency");
  mg->GetXaxis()->SetRangeUser(0,1);
  mg->GetYaxis()->SetRangeUser(0,1.02);

  lL->SetLineWidth(2);
  lT->SetLineWidth(2);

  lL->SetLineColor(kBlue);
  lL->Draw("same");

  lT->SetLineColor(kOrange);
  lT->Draw("same");

  //c1->SetLogx();

  //c1->BuildLegend();
  c1->SaveAs((name+"_ROC_TvsOth.pdf").c_str());
  c1->SaveAs((name+"_ROC_TvsOth.png").c_str());
  c1->SaveAs((name+"_ROC_TvsOth.C").c_str());


}



void ROC_creator(){

  
  ROC_creator_filesTvsQCD("scores_el_resolved_high_pt.root","Resolved Top(e,jet), High p_{T}","ROCs/el_res_hi",0.17);
  ROC_creator_filesTvsQCD("scores_mu_resolved_high_pt.root","Resolved Top(#mu,jet), High p_{T}","ROCs/mu_res_hi",0.17);
  ROC_creator_filesTvsQCD("scores_el_merged_high_pt.root","Merged Top(e,jet), High p_{T}","ROCs/el_mer_hi",0.09);
  ROC_creator_filesTvsQCD("scores_mu_merged_high_pt.root","Merged Top(#mu,jet), High p_{T}","ROCs/mu_mer_hi",0.06);
  ROC_creator_filesTvsQCD("scores_el_resolved_low_pt.root","Resolved Top(e,jet), Low p_{T}","ROCs/el_res_lo",0.09);
  ROC_creator_filesTvsQCD("scores_mu_resolved_low_pt.root","Resolved Top(#mu,jet), Low p_{T}","ROCs/mu_res_lo",0.09);
  ROC_creator_filesTvsQCD("scores_el_merged_low_pt.root","Merged Top(e,jet), Low p_{T}","ROCs/el_mer_lo",0.04);//0.035
  ROC_creator_filesTvsQCD("scores_mu_merged_low_pt.root","Merged Top(#mu,jet), Low p_{T}","ROCs/mu_mer_lo",0.05);




  ROC_creator_filesTvsOth("scores_el_resolved_high_pt.root","Resolved Top(e,jet), High p_{T}","ROCs/el_res_hi",0.90,0.99,0.17);
  ROC_creator_filesTvsOth("scores_mu_resolved_high_pt.root","Resolved Top(#mu,jet), High p_{T}","ROCs/mu_res_hi",0.88,0.99,0.17);
  ROC_creator_filesTvsOth("scores_el_merged_high_pt.root","Merged Top(e,jet), High p_{T}","ROCs/el_mer_hi",0.87,0.99,0.09);
  ROC_creator_filesTvsOth("scores_mu_merged_high_pt.root","Merged Top(#mu,jet), High p_{T}","ROCs/mu_mer_hi",0.69,0.99,0.06);
  ROC_creator_filesTvsOth("scores_el_resolved_low_pt.root","Resolved Top(e,jet), Low p_{T}","ROCs/el_res_lo",0.65,0.96,0.09);
  ROC_creator_filesTvsOth("scores_mu_resolved_low_pt.root","Resolved Top(#mu,jet), Low p_{T}","ROCs/mu_res_lo",0.60,0.96,0.09);
  ROC_creator_filesTvsOth("scores_el_merged_low_pt.root","Merged Top(e,jet), Low p_{T}","ROCs/el_mer_lo",0.06,0.72,0.04);//0.035
  ROC_creator_filesTvsOth("scores_mu_merged_low_pt.root","Merged Top(#mu,jet), Low p_{T}","ROCs/mu_mer_lo",0.16,0.81,0.05);

}
