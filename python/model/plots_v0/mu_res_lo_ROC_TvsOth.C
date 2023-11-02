void mu_res_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n15/c1_n15
//=========  (Wed Oct 18 17:37:17 2023) by ROOT version 6.12/07
   TCanvas *c1_n15 = new TCanvas("c1_n15", "c1_n15",6,27,700,500);
   c1_n15->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n15->SetFillColor(0);
   c1_n15->SetBorderMode(0);
   c1_n15->SetBorderSize(2);
   c1_n15->SetFrameBorderMode(0);
   c1_n15->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Resolved Top(#mu,jet), Low p_{T}");
   
   Double_t _fx14[102] = {
   1,
   1,
   0.7524856,
   0.6315016,
   0.5444938,
   0.4826407,
   0.4312687,
   0.392998,
   0.3613072,
   0.3334595,
   0.3106485,
   0.2906034,
   0.2736152,
   0.2589999,
   0.2453745,
   0.2334085,
   0.2229711,
   0.2136109,
   0.2047165,
   0.1956329,
   0.1875973,
   0.1807992,
   0.1745105,
   0.1682364,
   0.162268,
   0.1570129,
   0.1517432,
   0.1472305,
   0.1425431,
   0.1385545,
   0.1337215,
   0.1302861,
   0.1263556,
   0.1226581,
   0.1193828,
   0.1161365,
   0.1129194,
   0.109615,
   0.1064852,
   0.1036902,
   0.100968,
   0.0979984,
   0.09531989,
   0.09280151,
   0.09051605,
   0.08809957,
   0.08575588,
   0.08309193,
   0.08069,
   0.07849188,
   0.07651212,
   0.07450324,
   0.07256714,
   0.07048548,
   0.06866584,
   0.06658418,
   0.06470631,
   0.06288667,
   0.06112526,
   0.05937841,
   0.05783536,
   0.05619041,
   0.05466191,
   0.05291506,
   0.05131378,
   0.04974161,
   0.0483878,
   0.04688842,
   0.04549094,
   0.04393333,
   0.04265231,
   0.04131305,
   0.04019215,
   0.038751,
   0.03755732,
   0.03611616,
   0.03458767,
   0.03313196,
   0.03199651,
   0.0306427,
   0.02917243,
   0.02786229,
   0.02658127,
   0.02544581,
   0.02396099,
   0.02288376,
   0.02164641,
   0.02045273,
   0.01898246,
   0.01777422,
   0.01671155,
   0.01532863,
   0.01397482,
   0.01234442,
   0.01104884,
   0.009578572,
   0.008035519,
   0.006550695,
   0.004643715,
   0.002693064,
   0.0008879831,
   0};
   Double_t _fy14[102] = {
   1,
   1,
   0.9994078,
   0.9979764,
   0.9963971,
   0.99439,
   0.9924158,
   0.9903758,
   0.9882206,
   0.9856212,
   0.9834496,
   0.9811463,
   0.9787773,
   0.9764411,
   0.9741215,
   0.9719499,
   0.9697618,
   0.9677382,
   0.9655172,
   0.9637569,
   0.9615853,
   0.9595617,
   0.9575546,
   0.9558107,
   0.9539353,
   0.9517307,
   0.9500033,
   0.9479304,
   0.9459068,
   0.9438339,
   0.9420407,
   0.9402474,
   0.9383226,
   0.9364471,
   0.934621,
   0.9327455,
   0.9308535,
   0.9288958,
   0.9265761,
   0.9245196,
   0.9224138,
   0.9205054,
   0.9190083,
   0.9167873,
   0.914517,
   0.912477,
   0.9105028,
   0.9081995,
   0.9059292,
   0.9036753,
   0.9013227,
   0.8991346,
   0.8969136,
   0.8940017,
   0.8916656,
   0.8890991,
   0.8869439,
   0.88469,
   0.8822552,
   0.8795242,
   0.8768262,
   0.8742267,
   0.8715451,
   0.8684687,
   0.8657706,
   0.862398,
   0.8591735,
   0.856097,
   0.8530205,
   0.8496973,
   0.8457489,
   0.8420637,
   0.8390201,
   0.8350059,
   0.8308765,
   0.8265498,
   0.8220091,
   0.8175013,
   0.812829,
   0.8080087,
   0.8024809,
   0.7965912,
   0.7904383,
   0.7835779,
   0.7765201,
   0.7683436,
   0.75969,
   0.750181,
   0.7396683,
   0.7281193,
   0.7152047,
   0.7013853,
   0.6843742,
   0.6662608,
   0.6437879,
   0.6169387,
   0.5841669,
   0.5413266,
   0.479715,
   0.3849697,
   0.2017965,
   0};
   TGraph *graph = new TGraph(102,_fx14,_fy14);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph14 = new TH1F("Graph_Graph14","",102,0,1.1);
   Graph_Graph14->SetMinimum(0);
   Graph_Graph14->SetMaximum(1.1);
   Graph_Graph14->SetDirectory(0);
   Graph_Graph14->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph14->SetLineColor(ci);
   Graph_Graph14->GetXaxis()->SetLabelFont(42);
   Graph_Graph14->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetXaxis()->SetTitleFont(42);
   Graph_Graph14->GetYaxis()->SetLabelFont(42);
   Graph_Graph14->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetYaxis()->SetTitleOffset(0);
   Graph_Graph14->GetYaxis()->SetTitleFont(42);
   Graph_Graph14->GetZaxis()->SetLabelFont(42);
   Graph_Graph14->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph14->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph14);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Resolved Top(#mu,jet), Low p_{T}");
   pt->Draw();
   TLine *line = new TLine(1,0,1,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.008035519,0,0.008035519,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n15->Modified();
   c1_n15->cd();
   c1_n15->SetSelected(c1_n15);
}
