void mu_res_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n11/c1_n11
//=========  (Tue Oct 31 17:49:28 2023) by ROOT version 6.12/07
   TCanvas *c1_n11 = new TCanvas("c1_n11", "c1_n11",6,27,700,500);
   c1_n11->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n11->SetFillColor(0);
   c1_n11->SetBorderMode(0);
   c1_n11->SetBorderSize(2);
   c1_n11->SetFrameBorderMode(0);
   c1_n11->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Resolved Top(#mu,jet), High p_{T}");
   
   Double_t _fx10[102] = {
   1,
   1,
   0.9982014,
   0.9933196,
   0.9812436,
   0.9583762,
   0.9290853,
   0.9023638,
   0.8764132,
   0.8450668,
   0.8170606,
   0.786999,
   0.7633607,
   0.7399794,
   0.717112,
   0.6960432,
   0.6734327,
   0.6551901,
   0.6361768,
   0.6194758,
   0.6027749,
   0.5855601,
   0.5686023,
   0.5575539,
   0.5423946,
   0.5282631,
   0.5161871,
   0.5023124,
   0.491778,
   0.4779034,
   0.4668551,
   0.4573484,
   0.4511819,
   0.4447585,
   0.4355087,
   0.4265159,
   0.4175231,
   0.4103289,
   0.4008222,
   0.3936279,
   0.3869476,
   0.3774409,
   0.3684481,
   0.3612539,
   0.3532888,
   0.3450668,
   0.3355601,
   0.3304214,
   0.3221994,
   0.3144913,
   0.3088386,
   0.3024152,
   0.2975334,
   0.2916238,
   0.2862282,
   0.27852,
   0.2720966,
   0.2669578,
   0.2602775,
   0.2543679,
   0.2479445,
   0.2407503,
   0.2358685,
   0.2317574,
   0.2263618,
   0.2199383,
   0.2135149,
   0.2096608,
   0.2045221,
   0.2001542,
   0.1937307,
   0.1898767,
   0.1831963,
   0.1795992,
   0.1749743,
   0.1718911,
   0.1667523,
   0.1603289,
   0.155704,
   0.1510791,
   0.147482,
   0.1410586,
   0.135149,
   0.131295,
   0.127184,
   0.1205036,
   0.1153648,
   0.1112539,
   0.106629,
   0.1012333,
   0.09558067,
   0.08992806,
   0.08170606,
   0.07605344,
   0.06911614,
   0.06192189,
   0.05241521,
   0.04496403,
   0.03622816,
   0.02749229,
   0.01002055,
   0};
   Double_t _fy10[102] = {
   1,
   1,
   1,
   1,
   0.9999213,
   0.9999213,
   0.9996457,
   0.999567,
   0.9993702,
   0.9992127,
   0.9987797,
   0.9985042,
   0.9983467,
   0.9977956,
   0.9974807,
   0.9970871,
   0.9964966,
   0.9959849,
   0.9955912,
   0.9951583,
   0.9944891,
   0.9940167,
   0.9934262,
   0.9929932,
   0.9923241,
   0.9915761,
   0.9911038,
   0.990907,
   0.9903558,
   0.9898047,
   0.9890962,
   0.9888207,
   0.9883089,
   0.9877579,
   0.9872068,
   0.9863801,
   0.9855141,
   0.9848055,
   0.9841757,
   0.983231,
   0.9825224,
   0.9816171,
   0.9809085,
   0.9803574,
   0.9792553,
   0.9785073,
   0.9776807,
   0.9766179,
   0.9758306,
   0.9750826,
   0.9742166,
   0.9731932,
   0.9720516,
   0.9709495,
   0.9699653,
   0.9688238,
   0.9680365,
   0.9670525,
   0.9652417,
   0.9642183,
   0.9631948,
   0.9620926,
   0.9603212,
   0.9589828,
   0.9575264,
   0.9560305,
   0.9542592,
   0.9525665,
   0.9512675,
   0.9496536,
   0.9481578,
   0.9460321,
   0.9439852,
   0.9419776,
   0.9397733,
   0.9381593,
   0.9361124,
   0.9342229,
   0.9318611,
   0.9293025,
   0.9266257,
   0.9241458,
   0.9211541,
   0.9176114,
   0.9144229,
   0.9105259,
   0.905881,
   0.9003307,
   0.8948197,
   0.8877342,
   0.8803338,
   0.8711227,
   0.862187,
   0.8500236,
   0.8336876,
   0.8166431,
   0.7920012,
   0.7556291,
   0.7036294,
   0.6111242,
   0.4002126,
   0};
   TGraph *graph = new TGraph(102,_fx10,_fy10);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph10 = new TH1F("Graph_Graph10","",102,0,1.1);
   Graph_Graph10->SetMinimum(0);
   Graph_Graph10->SetMaximum(1.1);
   Graph_Graph10->SetDirectory(0);
   Graph_Graph10->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph10->SetLineColor(ci);
   Graph_Graph10->GetXaxis()->SetLabelFont(42);
   Graph_Graph10->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph10->GetXaxis()->SetTitleFont(42);
   Graph_Graph10->GetYaxis()->SetLabelFont(42);
   Graph_Graph10->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph10->GetYaxis()->SetTitleOffset(0);
   Graph_Graph10->GetYaxis()->SetTitleFont(42);
   Graph_Graph10->GetZaxis()->SetLabelFont(42);
   Graph_Graph10->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph10->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph10);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Resolved Top(#mu,jet), High p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.106629,0,0.106629,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.02749229,0,0.02749229,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n11->Modified();
   c1_n11->cd();
   c1_n11->SetSelected(c1_n11);
}
