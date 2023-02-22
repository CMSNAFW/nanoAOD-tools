void mas_syst(){

  gROOT->SetBatch();
  gStyle->SetOptStat(00000000);

  TFile *f = TFile::Open("../../crab/tree.root");
  TTree *evt = (TTree*) f->Get("Events");

  TH1F *nom = new TH1F("nom","",30,0,300);
  TH1F *up = new TH1F("up","",30,0,300);
  TH1F *down = new TH1F("down","",30,0,300);

  TCanvas *c1 = new TCanvas();

  nom->SetLineColor(kBlack);
  nom->SetMarkerColor(kBlack);

  up->SetLineColor(kRed);
  up->SetMarkerColor(kRed);

  down->SetLineColor(kBlue);
  down->SetMarkerColor(kBlue);

  nom->SetMarkerStyle(24);
  //up->SetMarkerStyle(26);
  //down->SetMarkerStyle(32);

  nom->SetMarkerSize(.8);
  up->SetMarkerSize(.8);
  down->SetMarkerSize(.8);

  evt->Draw("FatJet_msd_nom>>nom","","e");
  evt->Draw("FatJet_msd_jesTotalUp>>up","","histesame");
  evt->Draw("FatJet_msd_jesTotalDown>>down","","histesame");

  c1->SetLogy();
  nom->GetXaxis()->SetTitle("FatJet SoftDrop Mass");
  nom->GetYaxis()->SetTitle("Event/10 GeV");
  nom->GetYaxis()->SetRangeUser(0.1,10000);


  TLegend *l = new TLegend(0.60,0.67,0.87,0.87);
  l->AddEntry(nom,"Nominal");
  l->AddEntry(up,"JesUp");
  l->AddEntry(down,"JesDown");

  l->Draw();
  c1->SaveAs("/eos/home-f/fcarneva/Tprime/Syst_studies/NewSyst.C");
  c1->SaveAs("/eos/home-f/fcarneva/Tprime/Syst_studies/NewSyst.png");

  TCanvas *c2 = new TCanvas();

  evt->Draw("FatJet_msoftdrop>>nom","","e");
  evt->Draw("FatJet_msoftdrop_jesTotalUp>>up","","histesame");
  evt->Draw("FatJet_msoftdrop_jesTotalDown>>down","","histesame");

  c2->SetLogy();
  nom->GetXaxis()->SetTitle("FatJet SoftDrop Mass");
  nom->GetYaxis()->SetTitle("Event/10 GeV");

  TLegend *l2 = new TLegend(0.60,0.67,0.87,0.87);
  l2->AddEntry(nom,"Nominal");
  l2->AddEntry(up,"JesUp");
  l2->AddEntry(down,"JesDown");

  l->Draw();
  c2->SaveAs("/eos/home-f/fcarneva/Tprime/Syst_studies/OldNewSyst.C");
  c2->SaveAs("/eos/home-f/fcarneva/Tprime/Syst_studies/OldNewSyst.png");



}

//CreateMassHist();
