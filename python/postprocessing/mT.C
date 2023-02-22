void mT()
{
//=========Macro generated from canvas: c1/c1
//=========  (Mon May 30 12:50:29 2022) by ROOT version 6.12/07
   TCanvas *c1 = new TCanvas("c1", "c1",86,92,700,500);
   c1->Range(475,-562.5,725,5062.5);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *MasssPTsQ__1 = new TH1F("MasssPTsQ__1","Mass T' (600 GeV, Width 5 GeV ) ",40,500,700);
   MasssPTsQ__1->SetBinContent(6,11);
   MasssPTsQ__1->SetBinContent(7,14);
   MasssPTsQ__1->SetBinContent(8,10);
   MasssPTsQ__1->SetBinContent(9,19);
   MasssPTsQ__1->SetBinContent(10,12);
   MasssPTsQ__1->SetBinContent(11,30);
   MasssPTsQ__1->SetBinContent(12,25);
   MasssPTsQ__1->SetBinContent(13,33);
   MasssPTsQ__1->SetBinContent(14,51);
   MasssPTsQ__1->SetBinContent(15,63);
   MasssPTsQ__1->SetBinContent(16,88);
   MasssPTsQ__1->SetBinContent(17,133);
   MasssPTsQ__1->SetBinContent(18,234);
   MasssPTsQ__1->SetBinContent(19,666);
   MasssPTsQ__1->SetBinContent(20,3718);
   MasssPTsQ__1->SetBinContent(21,3525);
   MasssPTsQ__1->SetBinContent(22,729);
   MasssPTsQ__1->SetBinContent(23,230);
   MasssPTsQ__1->SetBinContent(24,124);
   MasssPTsQ__1->SetBinContent(25,87);
   MasssPTsQ__1->SetBinContent(26,64);
   MasssPTsQ__1->SetBinContent(27,32);
   MasssPTsQ__1->SetBinContent(28,29);
   MasssPTsQ__1->SetBinContent(29,21);
   MasssPTsQ__1->SetBinContent(30,10);
   MasssPTsQ__1->SetBinContent(31,9);
   MasssPTsQ__1->SetBinContent(32,7);
   MasssPTsQ__1->SetBinContent(33,8);
   MasssPTsQ__1->SetBinContent(34,11);
   MasssPTsQ__1->SetBinContent(35,6);
   MasssPTsQ__1->SetMinimum(0);
   MasssPTsQ__1->SetMaximum(4500);
   MasssPTsQ__1->SetEntries(9999);
   
   TPaveStats *ptstats = new TPaveStats(0.722063,0.6743697,0.9799427,0.9369748,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("Mass T'");
   ptstats_LaTex->SetTextSize(0.03019958);
   ptstats_LaTex = ptstats->AddText("Entries = 9999   ");
   ptstats_LaTex = ptstats->AddText("Mean  =  599.6");
   ptstats_LaTex = ptstats->AddText("Std Dev   =  11.06");
   ptstats_LaTex = ptstats->AddText("#chi^{2} / ndf =  1252 / 27");
   ptstats_LaTex = ptstats->AddText("Constant =  4290 #pm 62.9 ");
   ptstats_LaTex = ptstats->AddText("Mean     =   600 #pm 0.0 ");
   ptstats_LaTex = ptstats->AddText("Sigma    = 4.067 #pm 0.041 ");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(1);
   ptstats->Draw();
   MasssPTsQ__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(MasssPTsQ__1);
   
   TF1 *gaus2 = new TF1("gaus","gaus",500,700, TF1::EAddToList::kNo);
   gaus2->SetFillColor(19);
   gaus2->SetFillStyle(0);
   gaus2->SetLineColor(2);
   gaus2->SetLineWidth(2);
   gaus2->SetChisquare(1251.708);
   gaus2->SetNDF(27);
   gaus2->GetXaxis()->SetLabelFont(42);
   gaus2->GetXaxis()->SetLabelSize(0.035);
   gaus2->GetXaxis()->SetTitleSize(0.035);
   gaus2->GetXaxis()->SetTitleFont(42);
   gaus2->GetYaxis()->SetLabelFont(42);
   gaus2->GetYaxis()->SetLabelSize(0.035);
   gaus2->GetYaxis()->SetTitleSize(0.035);
   gaus2->GetYaxis()->SetTitleOffset(0);
   gaus2->GetYaxis()->SetTitleFont(42);
   gaus2->SetParameter(0,4289.818);
   gaus2->SetParError(0,62.86534);
   gaus2->SetParLimits(0,0,0);
   gaus2->SetParameter(1,600.0151);
   gaus2->SetParError(1,0.04363312);
   gaus2->SetParLimits(1,0,0);
   gaus2->SetParameter(2,4.067398);
   gaus2->SetParError(2,0.04073725);
   gaus2->SetParLimits(2,0,110.6342);
   gaus2->SetParent(MasssPTsQ__1);
   MasssPTsQ__1->GetListOfFunctions()->Add(gaus2);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   MasssPTsQ__1->SetLineColor(ci);
   MasssPTsQ__1->GetXaxis()->SetTitle("Mass T' [GeV]");
   MasssPTsQ__1->GetXaxis()->SetLabelFont(42);
   MasssPTsQ__1->GetXaxis()->SetLabelSize(0.035);
   MasssPTsQ__1->GetXaxis()->SetTitleSize(0.035);
   MasssPTsQ__1->GetXaxis()->SetTitleFont(42);
   MasssPTsQ__1->GetYaxis()->SetLabelFont(42);
   MasssPTsQ__1->GetYaxis()->SetLabelSize(0.035);
   MasssPTsQ__1->GetYaxis()->SetTitleSize(0.035);
   MasssPTsQ__1->GetYaxis()->SetTitleOffset(0);
   MasssPTsQ__1->GetYaxis()->SetTitleFont(42);
   MasssPTsQ__1->GetZaxis()->SetLabelFont(42);
   MasssPTsQ__1->GetZaxis()->SetLabelSize(0.035);
   MasssPTsQ__1->GetZaxis()->SetTitleSize(0.035);
   MasssPTsQ__1->GetZaxis()->SetTitleFont(42);
   MasssPTsQ__1->Draw("");
   
   TPaveText *pt = new TPaveText(0.3610602,0.9344958,0.6389398,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("Mass T' (600 GeV, Width 5 GeV ) ");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
