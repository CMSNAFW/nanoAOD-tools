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



void Tprime_top1(string filename, int merg, int lept, int pt){
    
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

  Float_t top_pt[size_max]; tree->SetBranchAddress("Top_pt",&top_pt);
  Int_t top_el_index[size_max]; tree->SetBranchAddress("Top_el_index",&top_el_index);
  Int_t top_isMerg[size_max]; tree->SetBranchAddress("Top_Is_dR_merg",&top_isMerg);
  Int_t top_truth[size_max]; tree->SetBranchAddress("Top_High_Truth",&top_truth);
  Float_t top_score[size_max]; tree->SetBranchAddress("Top_Score",&top_score);
  UInt_t nTop = tree->SetBranchAddress("nTop",&nTop);


  float Event_Number=0.;
  float  Event_run=0.;

  float eps_s[100]={}, eps_b[100]={}, NTrue_selected[100]={},NFalse_selected[100]={};
  float NFalse=0., NTrue=0.;

  float range[2]={0,500};
  if(pt==1) {
    range[0]=500;
    range[1]=100000;
  }
  std::cout<<range[0]<<std::endl;

  for(int i=0; i<nentries;i++){
    tree->GetEntry(i);

    for(int k=0;k<100;k++){
      float cut=k*0.01;

      for(int t=0; t<nTop;t++){

        if(top_isMerg[t]==merg){
          if(top_pt[t]>=range[0] && top_pt[t]<range[1]){

            if(lept==0 && top_el_index[t]>=0){
              if(top_truth[t]==0){
                NTrue++;
                if(top_score[t]>=cut)NTrue_selected[k]++; 
              }
              else {
                NFalse++;
                if(top_score[t]>=cut)NFalse_selected[k]++; 
                } 

            }//electron
            else if(lept==1 && top_el_index[t]==-1){
              if(top_truth[t]==0){
                NTrue++;
                if(top_score[t]>=cut)NTrue_selected[k]++; 
              }
              else {
                NFalse++;
                if(top_score[t]>=cut)NFalse_selected[k]++; 
                } 


            }//muon
          }// pt
        }//topology
      } //top loop
    }//cut loop
  }//entries loop

  if(lept==1) std::cout<<"Electron ";
  else std::cout<<"Muon ";

  if (merg==1) std::cout<<"Merged ";
  else std::cout<<"Resolved "; 

  if (pt==1) std::cout<<"High Pt"<<std::endl;
  else std::cout<<"Low Pt"<<std::endl;  

  for (int k =0; k<100;k++){
    eps_b[k]= NFalse_selected[k]/NFalse_selected[0];
    eps_s[k]= NTrue_selected[k]/NTrue_selected[0];
    if(eps_b[k]>=0.09 && eps_b[k]<=0.11)std::cout<<"s: "<<eps_s[k]<<", b: "<<eps_b[k]<<", cut: "<<k*0.01<<std::endl;
    if(eps_b[k]>=0.009 && eps_b[k]<=0.011)std::cout<<"s: "<<eps_s[k]<<", b: "<<eps_b[k]<<", cut: "<<k*0.01<<std::endl;  
  }

  
}// end of main 

void Top_tagger(){
  /*
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",1,1,1); //1,0,1 merged, electron, high pt
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",1,1,0);
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",1,0,1);
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",1,0,0);
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",0,1,1); 
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",0,1,0);
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",0,0,1);
  Tprime_top1("Tprime_tHq_1600LH_2018_part1.root",0,0,0);
  */
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",1,1,1); //1,0,1 merged, electron, high pt          
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",1,1,0);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",1,0,1);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",1,0,0);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",0,1,1);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",0,1,0);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",0,0,1);                                            
  Tprime_top1("TT_Mtt1000toInf_2018_part0.root",0,0,0);

}


