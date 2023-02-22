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



void Tprime_top1(string filename){
    
     gStyle->SetOptStat("e");
  gStyle->SetStatX(0.899514);
  gStyle->SetStatY(0.901);
  gStyle->SetStatW(0.3); 
  gStyle->SetStatH(0.25);




  TFile *f1 =  TFile::Open((filename).c_str());
  TTree *tree = new TTree;
    tree = (TTree*) f1->Get("Events");
  int nentries = tree->GetEntries(); 
 

int size_max=20;
int size_max2=300;


    
Float_t FatJet_eta[size_max]; tree->SetBranchAddress("FatJet_eta",&FatJet_eta);    
Float_t FatJet_phi[size_max]; tree->SetBranchAddress("FatJet_phi",&FatJet_phi);  

Float_t LHEPart_eta[size_max2]; tree->SetBranchAddress("LHEPart_eta",&LHEPart_eta);    
Float_t LHEPart_phi[size_max2]; tree->SetBranchAddress("LHEPart_phi",&LHEPart_phi);  

    
Int_t Gen_Id[size_max2]; tree->SetBranchAddress("LHEPart_pdgId",&Gen_Id);    
Int_t GenFatJet_Id[size_max2]; tree->SetBranchAddress("FatJet_genJetAK8Idx",&GenFatJet_Id);    

Float_t FatJet_msoftdrop[size_max]; tree->SetBranchAddress("FatJet_msoftdrop",&FatJet_msoftdrop);
Float_t FatJet_particleNetMD_Xbb[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_Xbb",&FatJet_particleNetMD_Xbb);
Float_t FatJet_btagDDBvL[size_max]; tree->SetBranchAddress("FatJet_btagDDBvL",&FatJet_btagDDBvL);


UInt_t nFatJet = tree->SetBranchAddress("nFatJet",&nFatJet);
UInt_t nLHEPart = tree->SetBranchAddress("nLHEPart",&nLHEPart);

TH1F *true_DB = new TH1F("true_DB","true_DB",50,100,150);
TH1F *false_DB = new TH1F("false_DB","false_DB",50,100,150);
TH1F *true_PN = new TH1F("true_PN","true_PN",50,100,150);
TH1F *false_PN = new TH1F("false_PN","false_PN",50,100,150);

 float nH_true=0;
 float nH_false=0;
 float nH_true_PN=0;
 float nH_false_PN=0;
 float nH_true_DB=0;
 float nH_false_DB=0;
 bool isH= false;

  for(int i=0; i<nentries;i++){
    tree->GetEntry(i);
    if(i%1000==0) std::cout<<i<<std::endl;
    for(int k=0; k<nFatJet;k++){
      isH=false;
      for(int t =0; t<nLHEPart;t++){
        if(Gen_Id[t]==25){
          float dPhi =(FatJet_phi[k]-LHEPart_phi[t]);
          if (dPhi>3.14) dPhi = dPhi-6.28;
          float dR = sqrt(pow((FatJet_eta[k] -LHEPart_eta[t]),2)+pow(dPhi,2));
          if(dR<0.1) isH=true;
        }
      }
      if(isH){
        nH_true=nH_true+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140 && FatJet_particleNetMD_Xbb[k]>0.94){ 
          nH_true_PN=nH_true_PN+1;
          true_PN->Fill(FatJet_msoftdrop[k]);
          }
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140 && FatJet_btagDDBvL[k]>0.91){
          nH_true_DB=nH_true_DB+1;
          true_DB->Fill(FatJet_msoftdrop[k]);
        }
      }
      else{
        nH_false=nH_false+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140 && FatJet_btagDDBvL[k]>0.91){
         nH_false_DB=nH_false_DB+1; 
         false_DB->Fill(FatJet_msoftdrop[k]);       
        }
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140 && FatJet_particleNetMD_Xbb[k]>0.94){
         nH_false_PN=nH_false_PN+1;
         false_PN->Fill(FatJet_msoftdrop[k]);
        }
      }

    }
  



}//end of loop entries
std::cout<<"False rate DB: "<< nH_false_DB/nH_false<<std::endl;
std::cout<<"True rate DB: "<< nH_true_DB/nH_true<<std::endl;
std::cout<<"False rate PN: "<< nH_false_PN/nH_false<<std::endl;
std::cout<<"True rate PN: "<< nH_true_PN/nH_true<<std::endl;
std::cout<<"True rate: "<< nH_true/nentries<<std::endl;  

TCanvas *c1 = new TCanvas();


true_PN->SetLineColor(kRed);
true_PN->SetFillColor(kRed);
true_PN->SetFillStyle(3001);

true_DB->SetLineColor(kBlack);
true_DB->SetFillColor(kBlack);
true_DB->SetFillStyle(3001);

false_DB->SetLineColor(kBlue);
false_DB->SetFillColor(kBlue);
false_DB->SetFillStyle(3001);

false_PN->SetLineColor(kGreen);
false_PN->SetFillColor(kGreen);
false_PN->SetFillStyle(3001);

true_PN->Draw();
true_DB->Draw("same");
false_DB->Draw("same");
false_PN->Draw("same");

TLegend *c = new TLegend();
c->AddEntry("true_PN","H True PN");
c->AddEntry("false_PN","H False PN");
c->AddEntry("true_DB","H True DB");
c->AddEntry("false_DB","H False DB");
c->Draw();



}// end of main 

void H_tagger_LHE(){

  Tprime_top1("/../../eos/user/f/fcarneva/public/signal_noskimmed/1200/tree_hadd_1.root");
}


