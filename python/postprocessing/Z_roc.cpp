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



void Tprime_top1(string filename,float cut_PN[110], float cut_DB[110]){
    
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
float ep_sPN[110],ep_bPN[110],ep_sDB[110],ep_bDB[110];
float  ep_sPNMcut[110],ep_sDBMcut[110],ep_bDBMcut[110],ep_bPNMcut[110];
float  ep_sPNMcut_norm[110],ep_sDBMcut_norm[110],ep_bDBMcut_norm[110],ep_bPNMcut_norm[110];
float ep_WPN[110],ep_WDB[110],ep_WDBMcut[110],ep_WPNMcut[110],ep_WDBMcut_norm[110],ep_WPNMcut_norm[110];
    
Float_t FatJet_eta[size_max]; tree->SetBranchAddress("FatJet_eta",&FatJet_eta);    
Float_t FatJet_phi[size_max]; tree->SetBranchAddress("FatJet_phi",&FatJet_phi);  

Float_t GenPart_eta[size_max2]; tree->SetBranchAddress("GenPart_eta",&GenPart_eta);    
Float_t GenPart_phi[size_max2]; tree->SetBranchAddress("GenPart_phi",&GenPart_phi);  
Int_t Gen_MomId[size_max2]; tree->SetBranchAddress("GenPart_genPartIdxMother",&Gen_MomId);
    
Int_t Gen_Id[size_max2]; tree->SetBranchAddress("GenPart_pdgId",&Gen_Id);    
Int_t GenFatJet_Id[size_max2]; tree->SetBranchAddress("FatJet_genJetAK8Idx",&GenFatJet_Id);    

Float_t FatJet_msoftdrop[size_max]; tree->SetBranchAddress("FatJet_msoftdrop",&FatJet_msoftdrop);
Float_t FatJet_particleNetMD_Xbb[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_Xbb",&FatJet_particleNetMD_Xbb);
Float_t FatJet_particleNetMD_Xcc[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_Xcc",&FatJet_particleNetMD_Xcc);
Float_t FatJet_particleNetMD_Xqq[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_Xqq",&FatJet_particleNetMD_Xqq);
Float_t FatJet_particleNetMD_QCD[size_max]; tree->SetBranchAddress("FatJet_particleNetMD_QCD",&FatJet_particleNetMD_QCD);

Float_t FatJet_deepTagMD_ZvsQCD[size_max]; tree->SetBranchAddress("FatJet_deepTagMD_ZvsQCD",&FatJet_deepTagMD_ZvsQCD);


UInt_t nFatJet = tree->SetBranchAddress("nFatJet",&nFatJet);
UInt_t nGenPart = tree->SetBranchAddress("nGenPart",&nGenPart);

TH1F *true_DB = new TH1F("true_DB","true_DB",50,100,150);
TH1F *false_DB = new TH1F("false_DB","false_DB",50,100,150);
TH1F *true_PN = new TH1F("true_PN","true_PN",50,100,150);
TH1F *false_PN = new TH1F("false_PN","false_PN",50,100,150);

 float nZ_true=0;
 float nZ_false=0;
 float nZ_trueMcut=0;
 float nZ_falseMcut=0;
 float nZ_true_PN[110]={};
 float nZ_false_PN[110]={};
 float nZ_true_DB[110]={};
 float nZ_false_DB[110]={};
 float nZ_true_PNMcut[110]={};
 float nZ_false_PNMcut[110]={};
 float nZ_true_DBMcut[110]={};
 float nZ_false_DBMcut[110]={};

 float nZ_W=0;
float nZ_WMcut=0;
float nZ_W_PN[110]={};
float nZ_W_DB[110]={};
float nZ_W_PNMcut[110]={};
float nZ_W_DBMcut[110]={};

 bool isZ= false,isHad=false,isW=false;
 int nb=0;
 int evt_had=0;

float FatJet_particleNetMDZ=0;
if(nentries>60000) nentries=60000;
  for(int i=0; i<nentries;i++){
    tree->GetEntry(i);
    int new_evt=true;
    if(i%10000==0) std::cout<<i<<std::endl;
    for(int k=0; k<nFatJet;k++){
      isZ=false;
      isHad=false;
      isW=false;
      FatJet_particleNetMDZ=(FatJet_particleNetMD_Xbb[k]);//+FatJet_particleNetMD_Xcc[k]+FatJet_particleNetMD_Xqq[k])/(FatJet_particleNetMD_Xbb[k]+FatJet_particleNetMD_Xcc[k]+FatJet_particleNetMD_Xqq[k]+FatJet_particleNetMD_QCD[k]);
      for(int t =0; t<nGenPart;t++){
        if((abs(Gen_Id[t])==5 )  && Gen_MomId[t]>=0){
        if(Gen_Id[Gen_MomId[t]]==23 ){  
          float dPhi =(FatJet_phi[k]-GenPart_phi[t]);
          if (dPhi>3.14) dPhi = dPhi-6.28;
          else if(dPhi<-3.14) dPhi = dPhi+6.28;
          float dR = sqrt(pow((FatJet_eta[k] -GenPart_eta[t]),2)+pow(dPhi,2));
          if(dR<0.8){
            if(isZ==true && nb==-Gen_Id[t]) isHad=true;
            isZ=true;
            nb=Gen_Id[t];
          } 
          
          
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
      if(isHad){
        
        nZ_true=nZ_true+1;
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_trueMcut=nZ_trueMcut+1;
        for(int u=0;u<110;u++){
        if( FatJet_particleNetMDZ>cut_PN[u]){ 
          nZ_true_PN[u]=nZ_true_PN[u]+1;
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105)  nZ_true_PNMcut[u]=nZ_true_PNMcut[u]+1;
          }
        if( FatJet_deepTagMD_ZvsQCD[k]>cut_DB[u]){
          nZ_true_DB[u]=nZ_true_DB[u]+1;
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105)  nZ_true_DBMcut[u]=nZ_true_DBMcut[u]+1;
        }
        }
      }
      else{
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_falseMcut=nZ_falseMcut+1;
        nZ_false=nZ_false+1;
        for(int u=0;u<110;u++){
        
        if( FatJet_deepTagMD_ZvsQCD[k]>cut_DB[u]){
         nZ_false_DB[u]=nZ_false_DB[u]+1; 
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_false_DBMcut[u]=nZ_false_DBMcut[u]+1;
        }

        if( FatJet_particleNetMDZ>cut_PN[u]){
         nZ_false_PN[u]=nZ_false_PN[u]+1;
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_false_PNMcut[u]=nZ_false_PNMcut[u]+1;
        }
      }
    }

      if(isW){
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_WMcut=nZ_WMcut+1;
        nZ_W=nZ_W+1;
        for(int u=0;u<110;u++){
        
        if( FatJet_deepTagMD_ZvsQCD[k]>cut_DB[u]){
         nZ_W_DB[u]=nZ_W_DB[u]+1; 
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_W_DBMcut[u]=nZ_W_DBMcut[u]+1;
        }

        if( FatJet_particleNetMDZ>cut_PN[u]){
         nZ_W_PN[u]=nZ_W_PN[u]+1;
        if(FatJet_msoftdrop[k]>60 && FatJet_msoftdrop[k]<105) nZ_W_PNMcut[u]=nZ_W_PNMcut[u]+1;
        }
      }
      }



    }
  



}
for(int g=0; g<110; g++)
{
  ep_sPN[g]=nZ_true_PN[g]/nZ_true;
  ep_bPN[g]=nZ_false_PN[g]/nZ_false;
  ep_sPNMcut[g]=nZ_true_PNMcut[g]/nZ_true;
  ep_sDBMcut[g]=nZ_true_DBMcut[g]/nZ_true;
  ep_bDBMcut[g]=nZ_false_DBMcut[g]/nZ_false;
  ep_bPNMcut[g]=nZ_false_PNMcut[g]/nZ_false;
  ep_sDB[g]=nZ_true_DB[g]/nZ_true;
  ep_bDB[g]=nZ_false_DB[g]/nZ_false;

  ep_sPNMcut_norm[g]=nZ_true_PNMcut[g]/nZ_trueMcut;
  ep_sDBMcut_norm[g]=nZ_true_DBMcut[g]/nZ_trueMcut;
  ep_bDBMcut_norm[g]=nZ_false_DBMcut[g]/nZ_falseMcut;
  ep_bPNMcut_norm[g]=nZ_false_PNMcut[g]/nZ_falseMcut;


  ep_WPN[g]=nZ_W_PN[g]/nZ_W;
  ep_WDB[g]=nZ_W_DB[g]/nZ_W;
  ep_WDBMcut[g]=nZ_W_DBMcut[g]/nZ_W;
  ep_WPNMcut[g]=nZ_W_PNMcut[g]/nZ_W;
  ep_WDBMcut_norm[g]=nZ_W_DBMcut[g]/nZ_WMcut;
  ep_WPNMcut_norm[g]=nZ_W_PNMcut[g]/nZ_WMcut;
  std::cout<<ep_sPN[g]<<" "<<ep_bPN[g]<<" "<<cut_PN[g]<<std::endl;

}

std::cout<<ep_sPN[109]<<" "<<ep_bPN[109]<<std::endl;

TGraph* rocPN = new TGraph(110,ep_bPN,ep_sPN);
TGraph* rocDB = new TGraph(110,ep_bDB,ep_sDB);
TGraph* rocPNMcut = new TGraph(110,ep_bPNMcut,ep_sPNMcut);
TGraph* rocDBMcut = new TGraph(110,ep_bDBMcut,ep_sDBMcut);

TGraph* rocPNMcut_norm = new TGraph(110,ep_bPNMcut_norm,ep_sPNMcut_norm);
TGraph* rocDBMcut_norm = new TGraph(110,ep_bDBMcut_norm,ep_sDBMcut_norm);

TGraph* rocWPN = new TGraph(110,ep_WPN,ep_sPN);
TGraph* rocWDB = new TGraph(110,ep_WDB,ep_sDB);
TGraph* rocWPNMcut = new TGraph(110,ep_WPNMcut,ep_sPNMcut);
TGraph* rocWDBMcut = new TGraph(110,ep_WDBMcut,ep_sDBMcut);
TGraph* rocWPNMcut_norm = new TGraph(110,ep_WPNMcut_norm,ep_sPNMcut_norm);
TGraph* rocWDBMcut_norm = new TGraph(110,ep_WDBMcut_norm,ep_sDBMcut_norm);

TCanvas *c1 = new TCanvas();
c1->SetLogx();
rocPN->SetLineColor(kRed);
rocDB->SetLineColor(kBlue);
rocPNMcut->SetLineColor(kRed);
rocDBMcut->SetLineColor(kBlue);
rocPNMcut->SetLineStyle(2);
rocDBMcut->SetLineStyle(2);

rocWPN->SetLineColor(kOrange+7);
rocWPN->SetLineWidth(2);
rocWDB->SetLineColor(kGreen);
rocWDB->SetLineWidth(2);
rocWPNMcut->SetLineColor(kOrange+7);
rocWPNMcut->SetLineWidth(2);
rocWDBMcut->SetLineColor(kGreen);
rocWDBMcut->SetLineWidth(2);
rocWPNMcut->SetLineStyle(2);
rocWDBMcut->SetLineStyle(2);

rocPN->SetTitle("ROC Curve Zbb");
rocPN->GetXaxis()->SetTitle("#epsilon_{b}");
rocPN->GetYaxis()->SetTitle("#epsilon_{s}");
rocPN->GetXaxis()->SetTitleSize(0.05);
rocPN->GetYaxis()->SetTitleSize(0.05);
rocPN->SetLineWidth(2);
rocDB->SetLineWidth(2);
rocPNMcut->SetLineWidth(2);
rocDBMcut->SetLineWidth(2);
rocPN->Draw("AL");
//rocWPNMcut->Draw("L same");
//rocPNMcut->Draw("L same");
//rocDBMcut->Draw("L same");
rocWPN->Draw("L same");
rocWDB->Draw("L same");
rocDB->Draw("L same");
//rocWDBMcut->Draw("L same");
rocPN->GetXaxis()->SetRangeUser(0.,1);
rocPN->GetYaxis()->SetRangeUser(0.,1);

TLegend *l1 = new TLegend(0.52,0.1,0.9,0.4);
l1->SetNColumns(2);
l1->AddEntry(rocPN,"ParticleNet Xbb [Zbb vs All]");
l1->AddEntry(rocDB,"DeepAk8 [Zbb vs All]");
l1->AddEntry(rocWPN,"ParticleNet Xbb [Zbb vs W]");
l1->AddEntry(rocWDB,"DeepAk8 [Zbb vs W]");
//l1->AddEntry(rocPNMcut,"ParticleNet 60<M_{SD}<105");
//l1->AddEntry(rocDBMcut,"DeepAk8 60<M_{SD}<105");
//l1->AddEntry(rocWPNMcut,"ParticleNet 60<M_{SD}<105 [Zbb vs W]");
//l1->AddEntry(rocWDBMcut,"DeepAk8 60<M_{SD}<105 [Zbb vs W]");
l1->Draw();

c1->SaveAs("rocZ.C");

TCanvas *c2= new TCanvas();
c2->SetLogx();
rocDBMcut_norm->SetTitle("ROC Curve 60<M_{SD}<105 Zbb");
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
rocWPNMcut_norm->SetLineColor(kOrange+7);
rocWPNMcut_norm->SetLineWidth(2);
rocWDBMcut_norm->SetLineColor(kGreen);
rocWDBMcut_norm->SetLineWidth(2);
rocWPNMcut_norm->Draw("L same");
rocWDBMcut_norm->Draw("L same");
TLegend *l2 = new TLegend(0.12,0.6,0.4,0.9);
l2->AddEntry(rocPNMcut_norm,"ParticleNet Xbb [Zbb vs All]");
l2->AddEntry(rocDBMcut_norm,"DeepAk8 [Zbb vs All]");
l2->AddEntry(rocWPNMcut_norm,"ParticleNet Xbb [ZbbvsW]");
l2->AddEntry(rocWDBMcut_norm,"DeepAk8 [ZbbvsW]");
l2->Draw();
c2->SaveAs("rocZ_cutmass.C");


}// end of main 

void Z_roc(){
  float cuts[110]={};
  for (int i=0; i<100;i++)cuts[i]=i/100.;
  for (int i=100;i<110;i++)  cuts[i]=0.99+(i-99)/1000.;


  Tprime_top1("/../..//../../eos/user/f/fcarneva/public/signal_noskimmed_notop_TZ/1600/B6E9DE52-48C4-7D43-9FFF-1CE3E5FE80FF.root",cuts,cuts);
}


