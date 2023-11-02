#include "TMath.h"
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <time.h>
#include "TFile.h"
#include "TChain.h"
#include "TTree.h"
#include "TBranch.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "RooGlobalFunc.h"
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include <vector>
#include <assert.h>
#include <TMVA/Reader.h>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cassert>
#include <sstream>
#include <string>
#include "TFileCollection.h"
#include "THashList.h"
#include "TBenchmark.h"


TH1F *chi_rid = new TH1F("chi_rid","chi_rid",10,0,3);

void tagger(string filename, string tree_name, string tag, float QCDcut){

  gROOT->SetBatch(kTRUE);
 /*   
  gStyle->SetOptStat("e");
  gStyle->SetStatX(0.899514);
  gStyle->SetStatY(0.901);
  gStyle->SetStatW(0.3); 
  gStyle->SetStatH(0.25);
*/



  TFile *f1 =  TFile::Open((filename).c_str());
  TTree *tree = new TTree;
  tree = (TTree*) f1->Get((tree_name).c_str());
  int nentries = tree->GetEntries(); 
 

  int size_max=20;
  int size_max2=300;

  float Score0 = tree->SetBranchAddress("Score0",&Score0);
  float Score1 = tree->SetBranchAddress("Score1",&Score1);
  float Score2 = tree->SetBranchAddress("Score2",&Score2);

  TH1F *sc0_0 =new TH1F("sc0_0","sc0_0",20,0,1);
  TH1F *sc0_1 =new TH1F("sc0_1","sc0_1",20,0,1);
  TH1F *sc0_2 =new TH1F("sc0_2","sc0_2",20,0,1);
  TH1F *sc1_0 =new TH1F("sc1_0","sc1_0",20,0,1);
  TH1F *sc1_1 =new TH1F("sc1_1","sc1_1",20,0,1);
  TH1F *sc1_2 =new TH1F("sc1_2","sc1_2",20,0,1);
  TH1F *sc2_0 =new TH1F("sc2_0","sc2_0",20,0,1);
  TH1F *sc2_1 =new TH1F("sc2_1","sc2_1",20,0,1);
  TH1F *sc2_2 =new TH1F("sc2_2","sc2_2",20,0,1);



  TH1F *sc0_0_test =new TH1F("sc0_0_test","sc0_0_test",20,0,1);
  TH1F *sc0_1_test =new TH1F("sc0_1_test","sc0_1_test",20,0,1);
  TH1F *sc0_2_test =new TH1F("sc0_2_test","sc0_2_test",20,0,1);

  TH1F *sc0_0_train =new TH1F("sc0_0_train","sc0_0_train",20,0,1);
  TH1F *sc0_1_train =new TH1F("sc0_1_train","sc0_1_train",20,0,1);
  TH1F *sc0_2_train =new TH1F("sc0_2_train","sc0_2_train",20,0,1);

  TH1F *sc1_0_test =new TH1F("sc1_0_test","sc1_0_test",20,0,1);
  TH1F *sc1_1_test =new TH1F("sc1_1_test","sc1_1_test",20,0,1);
  TH1F *sc1_2_test =new TH1F("sc1_2_test","sc1_2_test",20,0,1);

  TH1F *sc1_0_train =new TH1F("sc1_0_train","sc1_0_train",20,0,1);
  TH1F *sc1_1_train =new TH1F("sc1_1_train","sc1_1_train",20,0,1);
  TH1F *sc1_2_train =new TH1F("sc1_2_train","sc1_2_train",20,0,1);

  TH1F *sc2_0_test =new TH1F("sc2_0_test","sc2_0_test",20,0,1);
  TH1F *sc2_1_test =new TH1F("sc2_1_test","sc2_1_test",20,0,1);
  TH1F *sc2_2_test =new TH1F("sc2_2_test","sc2_2_test",20,0,1);

  TH1F *sc2_0_train =new TH1F("sc2_0_train","sc2_0_train",20,0,1);
  TH1F *sc2_1_train =new TH1F("sc2_1_train","sc2_1_train",20,0,1);
  TH1F *sc2_2_train =new TH1F("sc2_2_train","sc2_2_train",20,0,1);

  TH1F *tagvsQCD_0 =new TH1F("tagvsQCD_0","tagvsQCD_0",20,0,1);
  TH1F *tagvsQCD_1 =new TH1F("tagvsQCD_1","tagvsQCD_1",20,0,1);
  TH1F *tagvsQCD_2 =new TH1F("tagvsQCD_2","tagvsQCD_2",20,0,1);
  TH1F *tagvsOth_0 =new TH1F("tagvsOth_0","tagvsOth_0",20,0,1);
  TH1F *tagvsOth_1 =new TH1F("tagvsOth_1","tagvsOth_1",20,0,1);
  TH1F *tagvsOth_2 =new TH1F("tagvsOth_2","tagvsOth_2",20,0,1);


  TH1F *tagvsQCD_0_test =new TH1F("tagvsQCD_0_test","tagvsQCD_0_test",20,0,1);
  TH1F *tagvsQCD_1_test =new TH1F("tagvsQCD_1_test","tagvsQCD_1_test",20,0,1);
  TH1F *tagvsQCD_2_test =new TH1F("tagvsQCD_2_test","tagvsQCD_2_test",20,0,1);

  TH1F *tagvsQCD_0_train =new TH1F("tagvsQCD_0_train","tagvsQCD_0_train",20,0,1);
  TH1F *tagvsQCD_1_train =new TH1F("tagvsQCD_1_train","tagvsQCD_1_train",20,0,1);
  TH1F *tagvsQCD_2_train =new TH1F("tagvsQCD_2_train","tagvsQCD_2_train",20,0,1);

  TH1F *tagvsOth_0_test =new TH1F("tagvsOth_0_test","tagvsOth_0_test",20,0,1);
  TH1F *tagvsOth_1_test =new TH1F("tagvsOth_1_test","tagvsOth_1_test",20,0,1);
  TH1F *tagvsOth_2_test =new TH1F("tagvsOth_2_test","tagvsOth_2_test",20,0,1);

  TH1F *tagvsOth_0_train =new TH1F("tagvsOth_0_train","tagvsOth_0_train",20,0,1);
  TH1F *tagvsOth_1_train =new TH1F("tagvsOth_1_train","tagvsOth_1_train",20,0,1);
  TH1F *tagvsOth_2_train =new TH1F("tagvsOth_2_train","tagvsOth_2_train",20,0,1);


// Score0

//tree->Draw("Score0>>sc0_0","Truth==0","HIST");
//tree->Draw("Score0>>sc0_1","Truth==1","HIST");
//tree->Draw("Score0>>sc0_2","Truth==2","HIST");


tree->Draw("Score0>>sc0_0_train","Truth==0 && Train==1");
tree->Draw("Score0>>sc0_1_train","Truth==1 && Train==1");
tree->Draw("Score0>>sc0_2_train","Truth==2 && Train==1");

tree->Draw("Score0>>sc0_0_test","Truth==0 && Train==0","HIST");
tree->Draw("Score0>>sc0_1_test","Truth==1 && Train==0","HIST");
tree->Draw("Score0>>sc0_2_test","Truth==2 && Train==0","HIST");

sc0_0_train->SetLineColor(kBlue);
sc0_0_train->SetLineWidth(2);
sc0_0_train->Scale(1./sc0_0_train->Integral());

sc0_0_test->SetMarkerColor(kBlue);
sc0_0_test->SetLineColor(kBlue);
sc0_0_test->SetMarkerStyle(8);
sc0_0_test->SetLineWidth(2);
sc0_0_test->Scale(1./sc0_0_test->Integral());

sc0_1_train->SetLineColor(kGreen);
sc0_1_train->SetLineWidth(2);
sc0_1_train->Scale(1./sc0_1_train->Integral());

sc0_1_test->SetMarkerColor(kGreen);
sc0_1_test->SetLineColor(kGreen);
sc0_1_test->SetMarkerStyle(8);
sc0_1_test->SetLineWidth(2);
sc0_1_test->Scale(1./sc0_1_test->Integral());

sc0_2_train->SetLineColor(kRed);
sc0_2_train->SetLineWidth(2);
sc0_2_train->Scale(1./sc0_2_train->Integral());

sc0_2_test->SetMarkerColor(kRed);
sc0_2_test->SetLineColor(kRed);
sc0_2_test->SetMarkerStyle(8);
sc0_2_test->SetLineWidth(2);
sc0_2_test->Scale(1./sc0_2_test->Integral());

TCanvas *scor0 = new TCanvas("scor0","scor0");
scor0->cd();
sc0_0_train->Draw("hist");
sc0_0_test->Draw("samee");
sc0_1_train->Draw("hist same");
sc0_1_test->Draw("samee");
sc0_2_train->Draw("hist same");
sc0_2_test->Draw("samee");
//scor0->SaveAs((tag+"_scor0.C").c_str());


// Score 1

tree->Draw("Score1>>sc1_0_train","Truth==0 && Train==1");
tree->Draw("Score1>>sc1_1_train","Truth==1 && Train==1");
tree->Draw("Score1>>sc1_2_train","Truth==2 && Train==1");

tree->Draw("Score1>>sc1_0_test","Truth==0 && Train==0","HIST");
tree->Draw("Score1>>sc1_1_test","Truth==1 && Train==0","HIST");
tree->Draw("Score1>>sc1_2_test","Truth==2 && Train==0","HIST");


sc1_0_train->SetLineColor(kBlue);
sc1_0_train->SetLineWidth(2);
sc1_0_train->Scale(1./sc1_0_train->Integral());

sc1_0_test->SetMarkerColor(kBlue);
sc1_0_test->SetMarkerStyle(8);
sc1_0_test->SetLineWidth(2);
sc1_0_test->Scale(1./sc1_0_test->Integral());

sc1_1_train->SetLineColor(kGreen);
sc1_1_train->SetLineWidth(2);
sc1_1_train->Scale(1./sc1_1_train->Integral());

sc1_1_test->SetMarkerColor(kGreen);
sc1_1_test->SetMarkerStyle(8);
sc1_1_test->SetLineWidth(2);
sc1_1_test->Scale(1./sc1_1_test->Integral());

sc1_2_train->SetLineColor(kRed);
sc1_2_train->SetLineWidth(2);
sc1_2_train->Scale(1./sc1_2_train->Integral());

sc1_2_test->SetMarkerColor(kRed);
sc1_2_test->SetMarkerStyle(8);
sc1_2_test->SetLineWidth(2);
sc1_2_test->Scale(1./sc1_2_test->Integral());

sc1_2_test->SetLineColor(kRed);
sc1_1_test->SetLineColor(kGreen);
sc1_0_test->SetLineColor(kBlue);

TCanvas *scor1 = new TCanvas("scor1","scor1");
scor1->cd();
sc1_0_train->Draw("hist");
sc1_0_test->Draw("samee");
sc1_1_train->Draw("hist same");
sc1_1_test->Draw("samee");
sc1_2_train->Draw("hist same");
sc1_2_test->Draw("samee");
//scor1->SaveAs((tag+"_scor1.C").c_str());



// Score2 

tree->Draw("Score2>>sc2_0_train","Truth==0 && Train==1");
tree->Draw("Score2>>sc2_1_train","Truth==1 && Train==1");
tree->Draw("Score2>>sc2_2_train","Truth==2 && Train==1");

tree->Draw("Score2>>sc2_0_test","Truth==0 && Train==0","HIST");
tree->Draw("Score2>>sc2_1_test","Truth==1 && Train==0","HIST");
tree->Draw("Score2>>sc2_2_test","Truth==2 && Train==0","HIST");


sc2_0_train->SetLineColor(kBlue);
sc2_0_train->SetLineWidth(2);
sc2_0_train->Scale(1./sc2_0_train->Integral());

sc2_0_test->SetMarkerColor(kBlue);
sc2_0_test->SetMarkerStyle(8);
sc2_0_test->SetLineWidth(2);
sc2_0_test->Scale(1./sc2_0_test->Integral());

sc2_1_train->SetLineColor(kGreen);
sc2_1_train->SetLineWidth(2);
sc2_1_train->Scale(1./sc2_1_train->Integral());

sc2_1_test->SetMarkerColor(kGreen);
sc2_1_test->SetMarkerStyle(8);
sc2_1_test->SetLineWidth(2);
sc2_1_test->Scale(1./sc2_1_test->Integral());

sc2_2_train->SetLineColor(kRed);
sc2_2_train->SetLineWidth(2);
sc2_2_train->Scale(1./sc2_2_train->Integral());

sc2_2_test->SetMarkerColor(kRed);
sc2_2_test->SetMarkerStyle(8);
sc2_2_test->SetLineWidth(2);
sc2_2_test->Scale(1./sc2_2_test->Integral());

sc2_2_test->SetLineColor(kRed);
sc2_1_test->SetLineColor(kGreen);
sc2_0_test->SetLineColor(kBlue);

TCanvas *scor2 = new TCanvas("scor2","scor2");
scor2->cd();
sc2_0_train->Draw("hist");
sc2_0_test->Draw("samee");
sc2_1_train->Draw("hist same");
sc2_1_test->Draw("samee");
sc2_2_train->Draw("hist same");
sc2_2_test->Draw("samee");
//scor2->SaveAs((tag+"_scor2.C").c_str());


// tag vs QCD

tree->Draw("Score2/(1-Score1)>>tagvsQCD_0_train","Truth==0 && Train==1");
tree->Draw("Score2/(1-Score1)>>tagvsQCD_1_train","Truth==1 && Train==1");
tree->Draw("Score2/(1-Score1)>>tagvsQCD_2_train","Truth==2 && Train==1");

tree->Draw("Score2/(1-Score1)>>tagvsQCD_0_test","Truth==0 && Train==0","HIST");
tree->Draw("Score2/(1-Score1)>>tagvsQCD_1_test","Truth==1 && Train==0","HIST");
tree->Draw("Score2/(1-Score1)>>tagvsQCD_2_test","Truth==2 && Train==0","HIST");

tagvsQCD_0_train->SetLineColor(kBlue);
tagvsQCD_0_train->SetLineWidth(2);
tagvsQCD_0_train->Scale(1./tagvsQCD_0_train->Integral());

tagvsQCD_0_test->SetMarkerColor(kBlue);
tagvsQCD_0_test->SetMarkerStyle(8);
tagvsQCD_0_test->SetLineWidth(2);
tagvsQCD_0_test->Scale(1./tagvsQCD_0_test->Integral());

tagvsQCD_1_train->SetLineColor(kGreen);
tagvsQCD_1_train->SetLineWidth(2);
tagvsQCD_1_train->Scale(1./tagvsQCD_1_train->Integral());

tagvsQCD_1_test->SetMarkerColor(kGreen);
tagvsQCD_1_test->SetMarkerStyle(8);
tagvsQCD_1_test->SetLineWidth(2);
tagvsQCD_1_test->Scale(1./tagvsQCD_1_test->Integral());

tagvsQCD_2_train->SetLineColor(kRed);
tagvsQCD_2_train->SetLineWidth(2);
tagvsQCD_2_train->Scale(1./tagvsQCD_2_train->Integral());

tagvsQCD_2_test->SetMarkerColor(kRed);
tagvsQCD_2_test->SetMarkerStyle(8);
tagvsQCD_2_test->SetLineWidth(2);
tagvsQCD_2_test->Scale(1./tagvsQCD_2_test->Integral());

tagvsQCD_2_test->SetLineColor(kRed);
tagvsQCD_1_test->SetLineColor(kGreen);
tagvsQCD_0_test->SetLineColor(kBlue);

TCanvas *tagvsQCD = new TCanvas("tagvsQCD","tagvsQCD");
tagvsQCD->cd();
tagvsQCD_0_train->Draw("hist");
tagvsQCD_0_test->Draw("samee");
tagvsQCD_1_train->Draw("hist same");
tagvsQCD_1_test->Draw("samee");
tagvsQCD_2_train->Draw("hist same");
tagvsQCD_2_test->Draw("samee");
//tagvsQCD->SaveAs((tag+"_tagvsQCD.C").c_str());



// tag vs Oth

tree->Draw("Score2/(1-Score0)>>tagvsOth_0_train","Truth==0 && Train==1");
tree->Draw("Score2/(1-Score0)>>tagvsOth_1_train","Truth==1 && Train==1");
tree->Draw("Score2/(1-Score0)>>tagvsOth_2_train","Truth==2 && Train==1");

tree->Draw("Score2/(1-Score0)>>tagvsOth_0_test","Truth==0 && Train==0","HIST");
tree->Draw("Score2/(1-Score0)>>tagvsOth_1_test","Truth==1 && Train==0","HIST");
tree->Draw("Score2/(1-Score0)>>tagvsOth_2_test","Truth==2 && Train==0","HIST");

tagvsOth_0_train->SetLineColor(kBlue);
tagvsOth_0_train->SetLineWidth(2);
tagvsOth_0_train->Scale(1./tagvsOth_0_train->Integral());

tagvsOth_0_test->SetMarkerColor(kBlue);
tagvsOth_0_test->SetMarkerStyle(8);
tagvsOth_0_test->SetLineWidth(2);
tagvsOth_0_test->Scale(1./tagvsOth_0_test->Integral());

tagvsOth_1_train->SetLineColor(kGreen);
tagvsOth_1_train->SetLineWidth(2);
tagvsOth_1_train->Scale(1./tagvsOth_1_train->Integral());

tagvsOth_1_test->SetMarkerColor(kGreen);
tagvsOth_1_test->SetMarkerStyle(8);
tagvsOth_1_test->SetLineWidth(2);
tagvsOth_1_test->Scale(1./tagvsOth_1_test->Integral());

tagvsOth_2_train->SetLineColor(kRed);
tagvsOth_2_train->SetLineWidth(2);
tagvsOth_2_train->Scale(1./tagvsOth_2_train->Integral());

tagvsOth_2_test->SetMarkerColor(kRed);
tagvsOth_2_test->SetMarkerStyle(8);
tagvsOth_2_test->SetLineWidth(2);
tagvsOth_2_test->Scale(1./tagvsOth_2_test->Integral());

tagvsOth_2_test->SetLineColor(kRed);
tagvsOth_1_test->SetLineColor(kGreen);
tagvsOth_0_test->SetLineColor(kBlue);


TCanvas *tagvsOth = new TCanvas("tagvsOth","tagvsOth");
tagvsOth->cd();
tagvsOth_0_train->Draw("hist");
tagvsOth_0_test->Draw("samee");
tagvsOth_1_train->Draw("hist same");
tagvsOth_1_test->Draw("samee");
tagvsOth_2_train->Draw("hist same");
tagvsOth_2_test->Draw("samee");
//tagvsOth->SaveAs((tag+"_tagvsOth.C").c_str());
 //std::cout<<tagvsOth_0_train->Integral()<<std::endl;

 //std::cout<<tagvsOth_1_train->GetIntegral()[10]<<" "<<tagvsOth_2_train->GetIntegral()[10]<<std::endl;

 double chi0_TvsOth=0.;
 double chi1_TvsOth=0.;
 double chi2_TvsOth=0.;


 double chi0_TvsQCD=0.;
 double chi1_TvsQCD=0.;
 double chi2_TvsQCD=0.;

 double chi0=0.;
 double chi1=0.;
 double chi2=0.;


 for(int i=1;i<21;i++){
   chi0_TvsOth+=(std::pow(tagvsOth_0_test->GetBinContent(i)-tagvsOth_0_train->GetBinContent(i),2))/(std::pow(tagvsOth_0_test->GetBinError(i),2)+std::pow(tagvsOth_0_train->GetBinError(i),2));
   chi1_TvsOth+=(std::pow(tagvsOth_1_test->GetBinContent(i)-tagvsOth_1_train->GetBinContent(i),2))/(std::pow(tagvsOth_1_test->GetBinError(i),2)+std::pow(tagvsOth_1_train->GetBinError(i),2));
   chi2_TvsOth+=(std::pow(tagvsOth_2_test->GetBinContent(i)-tagvsOth_2_train->GetBinContent(i),2))/(std::pow(tagvsOth_2_test->GetBinError(i),2)+std::pow(tagvsOth_2_train->GetBinError(i),2));

   chi0_TvsQCD+=(std::pow(tagvsQCD_0_test->GetBinContent(i)-tagvsQCD_0_train->GetBinContent(i),2))/(std::pow(tagvsQCD_0_test->GetBinError(i),2)+std::pow(tagvsQCD_0_train->GetBinError(i),2));
   chi1_TvsQCD+=(std::pow(tagvsQCD_1_test->GetBinContent(i)-tagvsQCD_1_train->GetBinContent(i),2))/(std::pow(tagvsQCD_1_test->GetBinError(i),2)+std::pow(tagvsQCD_1_train->GetBinError(i),2));
   chi2_TvsQCD+=(std::pow(tagvsQCD_2_test->GetBinContent(i)-tagvsQCD_2_train->GetBinContent(i),2))/(std::pow(tagvsQCD_2_test->GetBinError(i),2)+std::pow(tagvsQCD_2_train->GetBinError(i),2));

   /*
   chi0+=(std::pow(sc0_0_test->GetBinContent(i)-sc0_0_train->GetBinContent(i),2))/(std::pow(sc0_0_test->GetBinError(i),2)+std::pow(sc0_0_train->GetBinError(i),2));
   chi0+=(std::pow(sc1_0_test->GetBinContent(i)-sc1_0_train->GetBinContent(i),2))/(std::pow(sc1_0_test->GetBinError(i),2)+std::pow(sc1_0_train->GetBinError(i),2));
   chi0+=(std::pow(sc2_0_test->GetBinContent(i)-sc2_0_train->GetBinContent(i),2))/(std::pow(sc2_0_test->GetBinError(i),2)+std::pow(sc2_0_train->GetBinError(i),2));

   chi1+=(std::pow(sc0_1_test->GetBinContent(i)-sc0_1_train->GetBinContent(i),2))/(std::pow(sc0_1_test->GetBinError(i),2)+std::pow(sc0_1_train->GetBinError(i),2));
   chi1+=(std::pow(sc1_1_test->GetBinContent(i)-sc1_1_train->GetBinContent(i),2))/(std::pow(sc1_1_test->GetBinError(i),2)+std::pow(sc1_1_train->GetBinError(i),2));
   chi1+=(std::pow(sc2_1_test->GetBinContent(i)-sc2_1_train->GetBinContent(i),2))/(std::pow(sc2_1_test->GetBinError(i),2)+std::pow(sc2_1_train->GetBinError(i),2));

   chi1+=(std::pow(sc0_2_test->GetBinContent(i)-sc0_2_train->GetBinContent(i),2))/(std::pow(sc0_2_test->GetBinError(i),2)+std::pow(sc0_2_train->GetBinError(i),2));
   chi1+=(std::pow(sc1_2_test->GetBinContent(i)-sc1_2_train->GetBinContent(i),2))/(std::pow(sc1_2_test->GetBinError(i),2)+std::pow(sc1_2_train->GetBinError(i),2));
   chi1+=(std::pow(sc2_2_test->GetBinContent(i)-sc2_2_train->GetBinContent(i),2))/(std::pow(sc2_2_test->GetBinError(i),2)+std::pow(sc2_2_train->GetBinError(i),2));

   std::cout<<i<<" "<<chi1<<" "<<chi2<<" "<<chi0<<std::endl;
   */
}

 std::cout<<filename<<" "<<" TvsOth 0 "<<chi0_TvsOth/20.<<" "<<TMath::Prob(chi0_TvsOth,20)<<std::endl;
 std::cout<<filename<<" "<<" TvsOth 1 "<<chi1_TvsOth/20.<<" "<<TMath::Prob(chi1_TvsOth,20)<<std::endl;
 std::cout<<filename<<" "<<" TvsOth 2 "<<chi2_TvsOth/20.<<" "<<TMath::Prob(chi2_TvsOth,20)<<std::endl;

 std::cout<<filename<<" "<<" TvsQCD 0 "<<chi0_TvsQCD/20.<<" "<<TMath::Prob(chi0_TvsQCD,20)<<std::endl;
 std::cout<<filename<<" "<<" TvsQCD 1 "<<chi1_TvsQCD/20.<<" "<<TMath::Prob(chi1_TvsQCD,20)<<std::endl;
 std::cout<<filename<<" "<<" TvsQCD 2 "<<chi2_TvsQCD/20.<<" "<<TMath::Prob(chi2_TvsQCD,20)<<std::endl;

 chi_rid->Fill(chi0_TvsOth/20.);
 chi_rid->Fill(chi1_TvsOth/20.);
 chi_rid->Fill(chi2_TvsOth/20.);

 chi_rid->Fill(chi0_TvsQCD/20.);
 chi_rid->Fill(chi1_TvsQCD/20.);
 chi_rid->Fill(chi2_TvsQCD/20.);

 /*
 std::cout<<filename<<" "<<" Scores 0 "<<chi0/60.<<" "<<TMath::Prob(chi0,60)<<std::endl;
 std::cout<<filename<<" "<<" Scores 1 "<<chi1/60.<<" "<<TMath::Prob(chi1,60)<<std::endl;
 std::cout<<filename<<" "<<" Scores 2 "<<chi2/60.<<" "<<TMath::Prob(chi2,60)<<std::endl;



 
 std::cout<<filename<<" "<<" TvsOth 0 "<<tagvsOth_0_test->Chi2Test(tagvsOth_0_train,"NORMUUP")<<std::endl;
 std::cout<<filename<<" "<<" TvsOth 1 "<<tagvsOth_1_test->Chi2Test(tagvsOth_1_train,"NORMUUP")<<std::endl; 
 std::cout<<filename<<" "<<" TvsOth 2 "<<tagvsOth_2_test->Chi2Test(tagvsOth_2_train,"NORMUUP")<<std::endl;

 std::cout<<filename<<" "<<" TvsQCD 0 "<<tagvsQCD_0_test->Chi2Test(tagvsQCD_0_train,"NORMUUP")<<std::endl;
 std::cout<<filename<<" "<<" TvsQCD 1 "<<tagvsQCD_1_test->Chi2Test(tagvsQCD_1_train,"NORMUUP")<<std::endl;
 std::cout<<filename<<" "<<" TvsQCD 2 "<<tagvsQCD_2_test->Chi2Test(tagvsQCD_2_train,"NORMUUP")<<std::endl;
 */

 scor0->Delete();
 scor1->Delete();
 scor2->Delete();
 tagvsOth->Delete();
 tagvsQCD->Delete();

 int n_true = tree->GetEntries("Truth==2");
 int n_QCD = tree->GetEntries("Truth==0");

 std::ofstream f((tag+".txt").c_str());

 for(int j=0; j<20;j++){
   float n_true_passed= tree->GetEntries(("Truth==2 && Score2/(1-Score1)>"+std::to_string(0.01*j)).c_str());
   float n_QCD_passed= tree->GetEntries(("Truth==0 && Score2/(1-Score1)>"+std::to_string(0.01*j)).c_str());
   if(n_true_passed/n_true>0.98){
     f<<n_true_passed/n_true<<" "<<n_QCD_passed/n_QCD<<" "<<0.01*j<<"\n";
   }

 } 
 f<<"Other Cut \n";
 int n_true_cut = tree->GetEntries(("Truth==2 && Score2/(1-Score1)>"+std::to_string(QCDcut)).c_str());
 int n_Oth = tree->GetEntries(("Truth==1 && Score2/(1-Score1)>"+std::to_string(QCDcut)).c_str());


 for(int h=0;h<1000;h++){

   float n_true_cut_passed= tree->GetEntries(("Truth==2 && Score2/(1-Score1)>"+std::to_string(QCDcut)+" && Score2/(1-Score0)>"+std::to_string(0.001*h)).c_str());
   float n_Oth_passed= tree->GetEntries(("Truth==1 && Score2/(1-Score1)>"+std::to_string(QCDcut)+" && Score2/(1-Score0)>"+std::to_string(0.001*h)).c_str());
   if((n_Oth_passed/n_Oth>0.09 && n_Oth_passed/n_Oth<0.11) || (n_Oth_passed/n_Oth>0.008 && n_Oth_passed/n_Oth<0.012)){
     f<<n_true_cut_passed/n_true_cut<<" "<<n_Oth_passed/n_Oth<<" "<<0.001*h<<"\n";
   }




}


 f.close();}
// end of main 

void efficiency2(){
  //TH1F *chi_rid = new TH1F("chi_rid","chi_rid",10,0,3);
  //tagger("scores.root","scores"); //1,0,1 merged, electron, high pt
  tagger("scores_el_resolved_high_pt.root","scores","plots/el_res_hi",0.17);
  tagger("scores_mu_resolved_high_pt.root","scores","plots/mu_res_hi",0.17); 
  tagger("scores_el_merged_high_pt.root","scores","plots/el_mer_hi",0.09);
  tagger("scores_mu_merged_high_pt.root","scores","plots/mu_mer_hi",0.06);
  tagger("scores_el_resolved_low_pt.root","scores","plots/el_res_lo",0.09);
  tagger("scores_mu_resolved_low_pt.root","scores","plots/mu_res_lo",0.09);
  tagger("scores_el_merged_low_pt.root","scores","plots/el_mer_lo",0.035);
  tagger("scores_mu_merged_low_pt.root","scores","plots/mu_mer_lo",0.05);

  chi_rid->Draw();
}


