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



void Tprime_top1(string filename,float cut_PN[101], float cut_DB[101]){
    
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
float ep_sPN[101],ep_bPN[101],ep_sDB[101],ep_bDB[101];
float  ep_sPNMcut[101],ep_sDBMcut[101],ep_bDBMcut[101],ep_bPNMcut[101];
float  ep_sPNMcut_norm[101],ep_sDBMcut_norm[101],ep_bDBMcut_norm[101],ep_bPNMcut_norm[101];
float ep_WPN[101],ep_WDB[101],ep_WDBMcut[101],ep_WPNMcut[101],ep_WDBMcut_norm[101],ep_WPNMcut_norm[101]; 
    
Float_t FatJet_eta[size_max]; tree->SetBranchAddress("FatJet_eta",&FatJet_eta);    
Float_t FatJet_phi[size_max]; tree->SetBranchAddress("FatJet_phi",&FatJet_phi);  

Float_t GenPart_eta[size_max2]; tree->SetBranchAddress("GenPart_eta",&GenPart_eta);    
Float_t GenPart_phi[size_max2]; tree->SetBranchAddress("GenPart_phi",&GenPart_phi);  
Int_t Gen_MomId[size_max2]; tree->SetBranchAddress("GenPart_genPartIdxMother",&Gen_MomId);
    
Int_t Gen_Id[size_max2]; tree->SetBranchAddress("GenPart_pdgId",&Gen_Id);    
Int_t GenFatJet_Id[size_max2]; tree->SetBranchAddress("FatJet_genJetAK8Idx",&GenFatJet_Id);    

Float_t FatJet_msoftdrop[size_max]; tree->SetBranchAddress("FatJet_msoftdrop",&FatJet_msoftdrop);
Float_t FatJet_particleNetMD_Xbb[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_Xbb",&FatJet_particleNetMD_Xbb);
Float_t FatJet_btagDDBvL[size_max]; tree->SetBranchAddress("FatJet_btagDDBvL",&FatJet_btagDDBvL);


UInt_t nFatJet = tree->SetBranchAddress("nFatJet",&nFatJet);
UInt_t nGenPart = tree->SetBranchAddress("nGenPart",&nGenPart);

TH1F *true_DB = new TH1F("true_DB","true_DB",60,0,300);
TH1F *false_DB = new TH1F("false_DB","false_DB",60,0,300);
TH1F *true_PN = new TH1F("true_PN","true_PN",60,0,300);
TH1F *false_PN = new TH1F("false_PN","false_PN",60,0,300);

 float nH_true=0;
 float nH_false=0;
 float nH_trueMcut=0;
 float nH_falseMcut=0;
 float nH_true_PN[101]={};
 float nH_false_PN[101]={};
 float nH_true_DB[101]={};
 float nH_false_DB[101]={};
 float nH_true_PNMcut[101]={};
 float nH_false_PNMcut[101]={};
 float nH_true_DBMcut[101]={};
 float nH_false_DBMcut[101]={};


float nH_W=0;
float nH_WMcut=0;
float nH_W_PN[101]={};
float nH_W_DB[101]={};
float nH_W_PNMcut[101]={};
float nH_W_DBMcut[101]={};

 bool isH= false,isW=false;
 int nb=0;
 int evt_had=0;
if(nentries>60000) nentries=60000;
  for(int i=0; i<nentries;i++){
    tree->GetEntry(i);
    int new_evt=true;
    if(i%10000==0) std::cout<<i<<std::endl;
    for(int k=0; k<nFatJet;k++){
      isH=false;
      isW=false;
      nb=0;
      for(int t =0; t<nGenPart;t++){
        if((abs(Gen_Id[t])==5 )  && Gen_MomId[t]>=0){
        if(Gen_Id[Gen_MomId[t]]==25 ){  
          float dPhi =(FatJet_phi[k]-GenPart_phi[t]);
          if (dPhi>3.14) dPhi = dPhi-6.28;
          else if(dPhi<-3.14) dPhi = dPhi+6.28;
          float dR = sqrt(pow((FatJet_eta[k] -GenPart_eta[t]),2)+pow(dPhi,2));
          if(dR<0.8) nb++;
          if(nb>=1)isH=true;
        }
        }
        if((abs(Gen_Id[t])==24 )  && Gen_MomId[t]>=0){
        if(abs(Gen_Id[Gen_MomId[t]])==6 ){  
          float dPhi =(FatJet_phi[k]-GenPart_phi[t]);
          if (dPhi>3.14) dPhi = dPhi-6.28;
          else if(dPhi<-3.14) dPhi = dPhi+6.28;
          float dR = sqrt(pow((FatJet_eta[k] -GenPart_eta[t]),2)+pow(dPhi,2));
          if(dR<0.8) isW=true;
        }
        }
      }
      if(isH){
        nH_true=nH_true+1;
        if(FatJet_particleNetMD_Xbb[k]>=0.88) true_PN->Fill(FatJet_msoftdrop[k]);
        if(FatJet_btagDDBvL[k]>=0.88) true_DB->Fill(FatJet_msoftdrop[k]);
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_trueMcut=nH_trueMcut+1;
        for(int u=0;u<101;u++){
        if( FatJet_particleNetMD_Xbb[k]>cut_PN[u]){ 
          nH_true_PN[u]=nH_true_PN[u]+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140)  nH_true_PNMcut[u]=nH_true_PNMcut[u]+1;
          }
        if( FatJet_btagDDBvL[k]>cut_DB[u]){
          nH_true_DB[u]=nH_true_DB[u]+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140)  nH_true_DBMcut[u]=nH_true_DBMcut[u]+1;
        }
        }
      }

      else{
        if(FatJet_particleNetMD_Xbb[k]>=0.88) false_PN->Fill(FatJet_msoftdrop[k]);
        if(FatJet_btagDDBvL[k]>=0.88) false_DB->Fill(FatJet_msoftdrop[k]);
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_falseMcut=nH_falseMcut+1;
        nH_false=nH_false+1;
        for(int u=0;u<101;u++){
        
        if( FatJet_btagDDBvL[k]>cut_DB[u]){
         nH_false_DB[u]=nH_false_DB[u]+1; 
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_false_DBMcut[u]=nH_false_DBMcut[u]+1;
        }

        if( FatJet_particleNetMD_Xbb[k]>cut_PN[u]){
         nH_false_PN[u]=nH_false_PN[u]+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_false_PNMcut[u]=nH_false_PNMcut[u]+1;
        }
      }
    }
      if(isW){
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_WMcut=nH_WMcut+1;
        nH_W=nH_W+1;
        for(int u=0;u<101;u++){
        
        if( FatJet_btagDDBvL[k]>cut_DB[u]){
         nH_W_DB[u]=nH_W_DB[u]+1; 
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_W_DBMcut[u]=nH_W_DBMcut[u]+1;
        }

        if( FatJet_particleNetMD_Xbb[k]>cut_PN[u]){
         nH_W_PN[u]=nH_W_PN[u]+1;
        if(FatJet_msoftdrop[k]>105 && FatJet_msoftdrop[k]<140) nH_W_PNMcut[u]=nH_W_PNMcut[u]+1;
        }
      }
      }
    
    }
  



}//end of loop entries
/*std::cout<<"False rate DB: "<< nH_false_DB/nH_false<<std::endl;
std::cout<<"True rate DB: "<< nH_true_DB/nH_true<<std::endl;
std::cout<<"False rate PN: "<< nH_false_PN/nH_false<<std::endl;
std::cout<<"True rate PN: "<< nH_true_PN/nH_true<<std::endl;
std::cout<<"True rate: "<< evt_had/float(nentries)<<std::endl;  

*/
for(int g=0; g<101; g++)
{
  ep_sPN[g]=nH_true_PN[g]/nH_true;
  ep_bPN[g]=nH_false_PN[g]/nH_false;
  ep_sPNMcut[g]=nH_true_PNMcut[g]/nH_true;
  ep_sDBMcut[g]=nH_true_DBMcut[g]/nH_true;
  ep_bDBMcut[g]=nH_false_DBMcut[g]/nH_false;
  ep_bPNMcut[g]=nH_false_PNMcut[g]/nH_false;
  ep_sDB[g]=nH_true_DB[g]/nH_true;
  ep_bDB[g]=nH_false_DB[g]/nH_false;

  ep_sPNMcut_norm[g]=nH_true_PNMcut[g]/nH_trueMcut;
  ep_sDBMcut_norm[g]=nH_true_DBMcut[g]/nH_trueMcut;
  ep_bDBMcut_norm[g]=nH_false_DBMcut[g]/nH_falseMcut;
  ep_bPNMcut_norm[g]=nH_false_PNMcut[g]/nH_falseMcut;

  ep_WPN[g]=nH_W_PN[g]/nH_W;
  ep_WDB[g]=nH_W_DB[g]/nH_W;
  ep_WDBMcut[g]=nH_W_DBMcut[g]/nH_W;
  ep_WPNMcut[g]=nH_W_PNMcut[g]/nH_W;
  ep_WDBMcut_norm[g]=nH_W_DBMcut[g]/nH_WMcut;
  ep_WPNMcut_norm[g]=nH_W_PNMcut[g]/nH_WMcut;
  if(ep_bPN[g]<=0.2) std::cout<<g<<"  "<<ep_bPN[g]<<"  "<<ep_sPN[g]<<std::endl; 
  //if(g==88)std::cout<<g<<"  "<<ep_bPN[g]<<"  "<<ep_sPN[g]<<std::endl;
  //if(ep_bDB[g]<=0.11) std::cout<<g<<" "<<ep_bDB[g]<<" "<<ep_sDB[g]<<" "<<ep_sPN[g]<<std::endl;

}

TGraph* rocPN = new TGraph(101,ep_bPN,ep_sPN);
TGraph* rocDB = new TGraph(101,ep_bDB,ep_sDB);
TGraph* rocPNMcut = new TGraph(101,ep_bPNMcut,ep_sPNMcut);
TGraph* rocDBMcut = new TGraph(101,ep_bDBMcut,ep_sDBMcut);

TGraph* rocPNMcut_norm = new TGraph(101,ep_bPNMcut_norm,ep_sPNMcut_norm);
TGraph* rocDBMcut_norm = new TGraph(101,ep_bDBMcut_norm,ep_sDBMcut_norm);


TGraph* rocWPN = new TGraph(101,ep_WPN,ep_sPN);
TGraph* rocWDB = new TGraph(101,ep_WDB,ep_sDB);
TGraph* rocWPNMcut = new TGraph(101,ep_WPNMcut,ep_sPNMcut);
TGraph* rocWDBMcut = new TGraph(101,ep_WDBMcut,ep_sDBMcut);
TGraph* rocWPNMcut_norm = new TGraph(101,ep_WPNMcut_norm,ep_sPNMcut_norm);
TGraph* rocWDBMcut_norm = new TGraph(101,ep_WDBMcut_norm,ep_sDBMcut_norm);



TCanvas *c1 = new TCanvas();
c1->SetLogx();
rocPN->SetLineColor(kRed);
rocDB->SetLineColor(kBlue);
rocPNMcut->SetLineColor(kRed);
rocDBMcut->SetLineColor(kBlue);
rocPNMcut->SetLineStyle(2);
rocDBMcut->SetLineStyle(2);

rocWPN->SetLineColor(kBlack);
rocWPN->SetLineWidth(2);
rocWDB->SetLineColor(kGreen);
rocWDB->SetLineWidth(2);
rocWPNMcut->SetLineColor(kBlack);
rocWPNMcut->SetLineWidth(2);
rocWDBMcut->SetLineColor(kGreen);
rocWDBMcut->SetLineWidth(2);
rocWPNMcut->SetLineStyle(2);
rocWDBMcut->SetLineStyle(2);

rocDB->SetTitle("ROC Curve");
rocDB->GetXaxis()->SetTitle("#epsilon_{b}");
rocDB->GetYaxis()->SetTitle("#epsilon_{s}");
rocDB->GetXaxis()->SetTitleSize(0.05);
rocDB->GetYaxis()->SetTitleSize(0.05);
rocPN->SetLineWidth(2);
rocDB->SetLineWidth(2);
rocPNMcut->SetLineWidth(2);
rocDBMcut->SetLineWidth(2);
rocDB->Draw("AL");
rocPN->Draw("L same");

//rocPNMcut->Draw("L same");
//rocDBMcut->Draw("L same");
rocWPN->Draw("L same");
rocWDB->Draw("L same");
//rocWPNMcut->Draw("L same");
//rocWDBMcut->Draw("L same");

rocPN->GetXaxis()->SetRangeUser(0.,1);
rocPN->GetYaxis()->SetRangeUser(0.,1);

TLegend *l1 = new TLegend(0.12,0.5,0.6,0.9);
l1->SetNColumns(2);
l1->AddEntry(rocPN,"ParticleNet");
l1->AddEntry(rocDB,"DoubleB");
l1->AddEntry(rocWPN,"ParticleNet [H vs W]");
l1->AddEntry(rocWDB,"DoubleB  [H vs W]");
//l1->AddEntry(rocPNMcut,"ParticleNet 105<M_{SD}<140");
//l1->AddEntry(rocDBMcut,"DoubleB 105<M_{SD}<140");
//l1->AddEntry(rocWPNMcut,"ParticleNet 105<M_{SD}<140 [H vs W]");
//l1->AddEntry(rocWDBMcut,"DoubleB 105<M_{SD}<140 [H vs W]");

l1->Draw();

c1->SaveAs("rocH.C");


TCanvas *c2= new TCanvas();
c2->SetLogx();
rocDBMcut_norm->SetTitle("ROC Curve 105<M_{SD}<140");
rocDBMcut_norm->GetXaxis()->SetTitle("#epsilon_{b}");
rocDBMcut_norm->GetYaxis()->SetTitle("#epsilon_{s}");
rocDBMcut_norm->GetXaxis()->SetTitleSize(0.05);
rocDBMcut_norm->GetYaxis()->SetTitleSize(0.05);
rocPNMcut_norm->SetLineColor(kRed);
rocDBMcut_norm->SetLineColor(kBlue);
rocPNMcut_norm->SetLineWidth(2);
rocDBMcut_norm->SetLineWidth(2);
rocDBMcut_norm->Draw("AL");
rocPNMcut_norm->Draw("L same");
rocWPNMcut_norm->SetLineColor(kBlack);
rocWPNMcut_norm->SetLineWidth(2);
rocWDBMcut_norm->SetLineColor(kGreen);
rocWDBMcut_norm->SetLineWidth(2);
rocWPNMcut_norm->Draw("L same");
rocWDBMcut_norm->Draw("L same");


TLegend *l2 = new TLegend(0.12,0.5,0.4,0.7);
l2->AddEntry(rocPNMcut_norm,"ParticleNet");
l2->AddEntry(rocDBMcut_norm,"DoubleB");
l2->AddEntry(rocWPNMcut_norm,"ParticleNet [HvsW]");
l2->AddEntry(rocWDBMcut_norm,"DoubleB [HvsW]");
l2->Draw();
c2->SaveAs("rocH_cutmass.C");

TCanvas *c3=new TCanvas();
true_PN->Draw();
true_DB->Draw("same");
false_PN->Draw("same");
false_DB->Draw("same");

c3->SaveAs("mass_H.C");


}// end of main 

void H_roc(){
  float cuts[101]={};
  for (int i=0; i<101;i++)cuts[i]=i/100.;
  #cuts[99]=0.983;
  #cuts[100]=0.985;

  Tprime_top1("/../../eos/user/f/fcarneva/public/signal_noskimmed_notop_TH/1600/798880A0-CA3F-924E-BE4C-0EB9EE43070A.root",cuts,cuts);
}


