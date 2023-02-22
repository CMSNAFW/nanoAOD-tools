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




Int_t Gen_MomId[size_max2]; tree->SetBranchAddress("GenPart_genPartIdxMother",&Gen_MomId);
    
Int_t Gen_Id[size_max2]; tree->SetBranchAddress("GenPart_pdgId",&Gen_Id);    

UInt_t nGenPart = tree->SetBranchAddress("nGenPart",&nGenPart);

TH1F *nChild= new TH1F("nChild","nChild",10,-0.5,9.5);
TH1F *ChildId =new  TH1F("ChildId","ChildId",100,-40.5,50.5);
int nch=0;

  for(int i=0; i<nentries;i++){
    tree->GetEntry(i);

    if(i%10000==0) std::cout<<i<<std::endl;
    nch=0;
      for(int t =0; t<nGenPart;t++){
        if((abs(Gen_Id[t])!=25 )  && Gen_MomId[t]>=0){
          
        if(Gen_Id[Gen_MomId[t]]==25 ){  
          nch++;
          ChildId->Fill(Gen_Id[t]);
        }
        }
     

    }
  
nChild->Fill(nch);


}//end of loop entries
TCanvas *c1 = new TCanvas();
nChild->Draw();
TCanvas *c2 = new TCanvas();
ChildId->Draw();



}// end of main 

void H_check(){

  Tprime_top1("/../../eos/home-f/fcarneva/public/signal_noskimmed_notop_TH/1600/798880A0-CA3F-924E-BE4C-0EB9EE43070A.root");
}


