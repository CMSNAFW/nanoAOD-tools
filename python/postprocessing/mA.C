void mA()
{
//=========Macro generated from canvas: c1/c1
//=========  (Mon May 30 12:36:29 2022) by ROOT version 6.12/07
   TCanvas *c1 = new TCanvas("c1", "c1",67,57,700,500);
   c1->Range(19.25,-1312.5,131.75,11812.5);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *bpt__1 = new TH1F("Mass A","Mass A (75 GeV)",60,30.5,120.5);
   bpt__1->SetBinContent(30,10000);
   bpt__1->SetEntries(10000);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("bpt");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 10000  ");
   ptstats_LaTex = ptstats->AddText("Mean  =     75");
   ptstats_LaTex = ptstats->AddText("Std Dev   = 0.00883");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   bpt__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(bpt__1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   bpt__1->SetLineColor(ci);
   bpt__1->GetXaxis()->SetLabelFont(42);
   bpt__1->GetXaxis()->SetLabelSize(0.035);
   bpt__1->GetXaxis()->SetTitleSize(0.035);
   bpt__1->GetXaxis()->SetTitleFont(42);
   bpt__1->GetXaxis()->SetTitle("Mass A [GeV]");
   bpt__1->GetYaxis()->SetLabelFont(42);
   bpt__1->GetYaxis()->SetLabelSize(0.035);
   bpt__1->GetYaxis()->SetTitleSize(0.035);
   bpt__1->GetYaxis()->SetTitleOffset(0);
   bpt__1->GetYaxis()->SetTitleFont(42);
   bpt__1->GetZaxis()->SetLabelFont(42);
   bpt__1->GetZaxis()->SetLabelSize(0.035);
   bpt__1->GetZaxis()->SetTitleSize(0.035);
   bpt__1->GetZaxis()->SetTitleFont(42);
   bpt__1->Draw("");
   
   TPaveText *pt = new TPaveText(0.4076218,0.9344958,0.5923782,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("W' b-jet pt");
   pt->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
