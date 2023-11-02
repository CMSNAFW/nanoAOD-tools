void mu_mer_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n17/c1_n17
//=========  (Wed Oct 18 17:37:20 2023) by ROOT version 6.12/07
   TCanvas *c1_n17 = new TCanvas("c1_n17", "c1_n17",6,27,700,500);
   c1_n17->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n17->SetFillColor(0);
   c1_n17->SetBorderMode(0);
   c1_n17->SetBorderSize(2);
   c1_n17->SetFrameBorderMode(0);
   c1_n17->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Merged Top(#mu,jet), Low p_{T}");
   
   Double_t _fx16[102] = {
   1,
   1,
   0.159102,
   0.1069931,
   0.08249511,
   0.06728324,
   0.05702199,
   0.04922103,
   0.04287525,
   0.03809717,
   0.03439922,
   0.0310238,
   0.028586,
   0.02635073,
   0.02428797,
   0.02250276,
   0.02090506,
   0.01938988,
   0.01819723,
   0.01706459,
   0.01610447,
   0.01521186,
   0.01452178,
   0.0138692,
   0.01324662,
   0.01250403,
   0.01185145,
   0.01128138,
   0.01092884,
   0.01046378,
   0.01011874,
   0.009758695,
   0.00939115,
   0.009106115,
   0.008761073,
   0.008566049,
   0.00832602,
   0.008078489,
   0.007748449,
   0.007538423,
   0.007358402,
   0.007050864,
   0.006863341,
   0.006638313,
   0.006413286,
   0.006270768,
   0.006090746,
   0.005933227,
   0.005738203,
   0.005610687,
   0.005453168,
   0.00531065,
   0.005160632,
   0.005025615,
   0.004853094,
   0.004718078,
   0.004628067,
   0.004530555,
   0.004418041,
   0.004223017,
   0.004125505,
   0.00399799,
   0.003922981,
   0.003765461,
   0.003682951,
   0.003577938,
   0.003390415,
   0.003285402,
   0.003210393,
   0.003112881,
   0.002992867,
   0.002910357,
   0.002872852,
   0.00277534,
   0.002700331,
   0.002602819,
   0.002490305,
   0.00237029,
   0.00228778,
   0.002190268,
   0.00212276,
   0.00204025,
   0.001942738,
   0.001822723,
   0.001702709,
   0.001560191,
   0.001477681,
   0.001365167,
   0.001245153,
   0.001185145,
   0.001110136,
   0.0009976223,
   0.000922613,
   0.0008100992,
   0.0007500919,
   0.0006675818,
   0.0006000735,
   0.0004950606,
   0.0004200515,
   0.000367545,
   0.0002100257,
   0};
   Double_t _fy16[102] = {
   1,
   1,
   0.9930565,
   0.9888132,
   0.9848914,
   0.9818053,
   0.9781407,
   0.9742832,
   0.9708114,
   0.9670181,
   0.9648965,
   0.9623891,
   0.959946,
   0.9578887,
   0.9550598,
   0.9529381,
   0.9507522,
   0.9484377,
   0.9466375,
   0.9447731,
   0.9432943,
   0.9413013,
   0.9394368,
   0.9374437,
   0.9355793,
   0.9339077,
   0.9319789,
   0.9301788,
   0.9288286,
   0.9273499,
   0.9261926,
   0.9251639,
   0.9240067,
   0.9222708,
   0.9207278,
   0.9193776,
   0.9184775,
   0.9171274,
   0.9157773,
   0.9139771,
   0.9128199,
   0.9110197,
   0.9094766,
   0.9081908,
   0.9067121,
   0.9054906,
   0.9039475,
   0.9029189,
   0.9010544,
   0.89964,
   0.8980327,
   0.8962325,
   0.8943037,
   0.8923749,
   0.8908319,
   0.8892889,
   0.8878102,
   0.8865244,
   0.8842741,
   0.8820882,
   0.8797094,
   0.8781021,
   0.8759804,
   0.8739874,
   0.8726373,
   0.8707728,
   0.8689083,
   0.8664009,
   0.864215,
   0.8613219,
   0.8590716,
   0.855857,
   0.8527067,
   0.8494921,
   0.8462775,
   0.8429986,
   0.8395911,
   0.8359265,
   0.8334191,
   0.8293043,
   0.8257683,
   0.8219751,
   0.8182461,
   0.8133599,
   0.8084094,
   0.8019802,
   0.7969654,
   0.7909862,
   0.7837855,
   0.776199,
   0.7687411,
   0.7598045,
   0.7509965,
   0.7399383,
   0.7259869,
   0.7077279,
   0.6877331,
   0.6605375,
   0.6249197,
   0.5675067,
   0.4468947,
   0};
   TGraph *graph = new TGraph(102,_fx16,_fy16);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph16 = new TH1F("Graph_Graph16","",102,0,1.1);
   Graph_Graph16->SetMinimum(0);
   Graph_Graph16->SetMaximum(1.1);
   Graph_Graph16->SetDirectory(0);
   Graph_Graph16->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph16->SetLineColor(ci);
   Graph_Graph16->GetXaxis()->SetLabelFont(42);
   Graph_Graph16->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetXaxis()->SetTitleFont(42);
   Graph_Graph16->GetYaxis()->SetLabelFont(42);
   Graph_Graph16->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetYaxis()->SetTitleOffset(0);
   Graph_Graph16->GetYaxis()->SetTitleFont(42);
   Graph_Graph16->GetZaxis()->SetLabelFont(42);
   Graph_Graph16->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph16->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph16);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Merged Top(#mu,jet), Low p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.02090506,0,0.02090506,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.00204025,0,0.00204025,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n17->Modified();
   c1_n17->cd();
   c1_n17->SetSelected(c1_n17);
}
