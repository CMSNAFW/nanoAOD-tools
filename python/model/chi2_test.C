void chi2_test()
{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Oct 26 12:24:33 2023) by ROOT version 6.12/07
   TCanvas *c1 = new TCanvas("c1", "c1",6,27,700,500);
   c1->Range(-0.375,-1.575,3.375,14.175);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *hist__1 = new TH1F("hist__1","Reduced Chi2",12,0,3);
   hist__1->SetBinContent(2,1);
   hist__1->SetBinContent(3,8);
   hist__1->SetBinContent(4,12);
   hist__1->SetBinContent(5,10);
   hist__1->SetBinContent(6,7);
   hist__1->SetBinContent(7,7);
   hist__1->SetBinContent(8,1);
   hist__1->SetBinContent(9,1);
   hist__1->SetBinContent(10,1);
   hist__1->SetEntries(48);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("hist");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 48     ");
   ptstats_LaTex = ptstats->AddText("Mean  =  1.131");
   ptstats_LaTex = ptstats->AddText("Std Dev   = 0.4388");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   hist__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(hist__1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   hist__1->SetLineColor(ci);
   hist__1->GetXaxis()->SetTitle("Reduced Chi2");
   hist__1->GetXaxis()->SetLabelFont(42);
   hist__1->GetXaxis()->SetLabelSize(0.035);
   hist__1->GetXaxis()->SetTitleSize(0.035);
   hist__1->GetXaxis()->SetTitleFont(42);
   hist__1->GetYaxis()->SetLabelFont(42);
   hist__1->GetYaxis()->SetLabelSize(0.035);
   hist__1->GetYaxis()->SetTitleSize(0.035);
   hist__1->GetYaxis()->SetTitleOffset(0);
   hist__1->GetYaxis()->SetTitleFont(42);
   hist__1->GetZaxis()->SetLabelFont(42);
   hist__1->GetZaxis()->SetLabelSize(0.035);
   hist__1->GetZaxis()->SetTitleSize(0.035);
   hist__1->GetZaxis()->SetTitleFont(42);
   hist__1->Draw("");
   
   TPaveText *pt = new TPaveText(0.3753868,0.94,0.6246132,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("Reduced Chi2");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
