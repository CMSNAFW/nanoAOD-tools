void el_mer_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n16/c1_n16
//=========  (Tue Oct 31 17:44:44 2023) by ROOT version 6.12/07
   TCanvas *c1_n16 = new TCanvas("c1_n16", "c1_n16",6,27,700,500);
   c1_n16->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n16->SetFillColor(0);
   c1_n16->SetBorderMode(0);
   c1_n16->SetBorderSize(2);
   c1_n16->SetFrameBorderMode(0);
   c1_n16->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Merged Top(e,jet), Low p_{T}");
   
   Double_t _fx15[102] = {
   1,
   1,
   0.3521453,
   0.2202446,
   0.1701276,
   0.1415238,
   0.1224706,
   0.1087476,
   0.09955864,
   0.09256446,
   0.08646263,
   0.08110846,
   0.07674312,
   0.07259484,
   0.06912187,
   0.06622772,
   0.06347828,
   0.0608012,
   0.05860647,
   0.05604997,
   0.0536623,
   0.05187758,
   0.04992403,
   0.04850107,
   0.0467887,
   0.04512457,
   0.04331573,
   0.04167571,
   0.0401804,
   0.03914333,
   0.03817862,
   0.03675566,
   0.03567035,
   0.0345127,
   0.03352387,
   0.03267974,
   0.03190796,
   0.03111208,
   0.03046089,
   0.0295203,
   0.02862793,
   0.02807322,
   0.02751851,
   0.02674674,
   0.02607144,
   0.0253479,
   0.02452789,
   0.02375612,
   0.02317729,
   0.02271905,
   0.02201963,
   0.02148904,
   0.02093433,
   0.02045197,
   0.0198249,
   0.01927019,
   0.01869136,
   0.01787136,
   0.01731664,
   0.01688252,
   0.01635193,
   0.01601428,
   0.01574898,
   0.01524251,
   0.0148325,
   0.01437426,
   0.0137472,
   0.01340955,
   0.01285483,
   0.0125413,
   0.01220365,
   0.01176953,
   0.01135952,
   0.01097364,
   0.01058775,
   0.01008128,
   0.009719509,
   0.009333623,
   0.008947737,
   0.008634204,
   0.008079492,
   0.007717724,
   0.007452427,
   0.007018305,
   0.006777127,
   0.006294769,
   0.005884765,
   0.005426525,
   0.005112992,
   0.004751224,
   0.004389456,
   0.004196513,
   0.003786508,
   0.003400622,
   0.002894147,
   0.002460025,
   0.002194728,
   0.001808842,
   0.00137472,
   0.0007235367,
   0.0002652968,
   0};
   Double_t _fy15[102] = {
   1,
   1,
   0.9926057,
   0.9859509,
   0.9818841,
   0.9784827,
   0.9757468,
   0.972937,
   0.9709405,
   0.9685744,
   0.9665779,
   0.9654688,
   0.9642118,
   0.9627329,
   0.9616238,
   0.9601449,
   0.9588879,
   0.9577048,
   0.9565957,
   0.9551908,
   0.9541556,
   0.9529725,
   0.9517894,
   0.9508281,
   0.9494972,
   0.9483141,
   0.9475747,
   0.9465395,
   0.9455043,
   0.9445431,
   0.9434339,
   0.9418811,
   0.9404762,
   0.9392192,
   0.9375185,
   0.935522,
   0.9337474,
   0.9324904,
   0.9313073,
   0.9296806,
   0.9280539,
   0.9267229,
   0.9249482,
   0.923987,
   0.9224342,
   0.9212511,
   0.9192547,
   0.9178497,
   0.9160751,
   0.9148181,
   0.9128956,
   0.9111949,
   0.9094203,
   0.907202,
   0.905871,
   0.9041703,
   0.9021739,
   0.8999556,
   0.8980331,
   0.8958888,
   0.8941142,
   0.8913044,
   0.8885685,
   0.8860544,
   0.8837622,
   0.8808045,
   0.8782165,
   0.8758503,
   0.8723011,
   0.8688998,
   0.8652026,
   0.862097,
   0.8588436,
   0.8553683,
   0.8517451,
   0.8476782,
   0.8436853,
   0.8388051,
   0.8333333,
   0.828675,
   0.8225377,
   0.815735,
   0.8106329,
   0.8040521,
   0.7975451,
   0.7908903,
   0.7813517,
   0.7715912,
   0.7611653,
   0.7517007,
   0.7389826,
   0.7261904,
   0.7094795,
   0.6925466,
   0.6691068,
   0.645667,
   0.6157202,
   0.5754215,
   0.5235877,
   0.4417332,
   0.2724786,
   0};
   TGraph *graph = new TGraph(102,_fx15,_fy15);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph15 = new TH1F("Graph_Graph15","",102,0,1.1);
   Graph_Graph15->SetMinimum(0);
   Graph_Graph15->SetMaximum(1.1);
   Graph_Graph15->SetDirectory(0);
   Graph_Graph15->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph15->SetLineColor(ci);
   Graph_Graph15->GetXaxis()->SetLabelFont(42);
   Graph_Graph15->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleFont(42);
   Graph_Graph15->GetYaxis()->SetLabelFont(42);
   Graph_Graph15->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleOffset(0);
   Graph_Graph15->GetYaxis()->SetTitleFont(42);
   Graph_Graph15->GetZaxis()->SetLabelFont(42);
   Graph_Graph15->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph15);
   
   multigraph->Add(graph,"l");
   multigraph->Draw("a");
   multigraph->GetXaxis()->SetTitle("Background (TopOth) Efficiency");
   multigraph->GetXaxis()->SetRange(5,98);
   multigraph->GetXaxis()->SetLabelFont(42);
   multigraph->GetXaxis()->SetLabelSize(0.035);
   multigraph->GetXaxis()->SetTitleSize(0.035);
   multigraph->GetXaxis()->SetTitleFont(42);
   multigraph->GetYaxis()->SetTitle("Signal Efficiency");
   multigraph->GetYaxis()->SetLabelFont(42);
   multigraph->GetYaxis()->SetLabelSize(0.035);
   multigraph->GetYaxis()->SetTitleSize(0.035);
   multigraph->GetYaxis()->SetTitleOffset(0);
   multigraph->GetYaxis()->SetTitleFont(42);
   
   TPaveText *pt = new TPaveText(0.15,0.9168487,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Merged Top(e,jet), Low p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.1224706,0,0.1224706,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01135952,0,0.01135952,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n16->Modified();
   c1_n16->cd();
   c1_n16->SetSelected(c1_n16);
}
