void mu_mer_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n13/c1_n13
//=========  (Wed Oct 18 17:37:14 2023) by ROOT version 6.12/07
   TCanvas *c1_n13 = new TCanvas("c1_n13", "c1_n13",6,27,700,500);
   c1_n13->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n13->SetFillColor(0);
   c1_n13->SetBorderMode(0);
   c1_n13->SetBorderSize(2);
   c1_n13->SetFrameBorderMode(0);
   c1_n13->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Merged Top(#mu,jet), High p_{T}");
   
   Double_t _fx12[102] = {
   1,
   1,
   0.2963845,
   0.2216018,
   0.184714,
   0.1597254,
   0.1412357,
   0.1292448,
   0.1160641,
   0.1071854,
   0.1002288,
   0.09308925,
   0.08860412,
   0.08356979,
   0.07862701,
   0.07478261,
   0.07066362,
   0.06764302,
   0.06562929,
   0.06270023,
   0.0595881,
   0.05757437,
   0.05592677,
   0.05290618,
   0.05125858,
   0.04897025,
   0.04723112,
   0.04567506,
   0.04475972,
   0.04338673,
   0.0424714,
   0.04118993,
   0.04009153,
   0.0389016,
   0.03826087,
   0.03725401,
   0.03615561,
   0.03569794,
   0.03469108,
   0.03395881,
   0.03359268,
   0.03295194,
   0.03221968,
   0.03121281,
   0.03048055,
   0.02983982,
   0.02910755,
   0.02837529,
   0.02764302,
   0.02718535,
   0.02608696,
   0.02544622,
   0.02480549,
   0.02416476,
   0.02352403,
   0.02324943,
   0.02279176,
   0.02169336,
   0.02132723,
   0.02077803,
   0.0204119,
   0.02022883,
   0.01967963,
   0.01949657,
   0.01913043,
   0.01894737,
   0.01867277,
   0.0182151,
   0.01757437,
   0.01665904,
   0.01620137,
   0.01583524,
   0.01565217,
   0.01537757,
   0.01482838,
   0.01418764,
   0.01400458,
   0.01345538,
   0.01299771,
   0.01281465,
   0.01189931,
   0.01153318,
   0.01107552,
   0.01061785,
   0.01034325,
   0.00979405,
   0.009427917,
   0.008787185,
   0.008512585,
   0.007871853,
   0.006956522,
   0.006590389,
   0.006407323,
   0.005949657,
   0.005491991,
   0.004759725,
   0.004393592,
   0.003569794,
   0.002929062,
   0.002105263,
   0.001647597,
   0};
   Double_t _fy12[102] = {
   1,
   1,
   0.9997664,
   0.9997664,
   0.9987154,
   0.9978979,
   0.9971973,
   0.9963798,
   0.9955623,
   0.9946281,
   0.993577,
   0.9931099,
   0.9922924,
   0.9917085,
   0.9911246,
   0.9904239,
   0.9896064,
   0.9890226,
   0.9884386,
   0.9880883,
   0.9875044,
   0.9869205,
   0.9866869,
   0.9857526,
   0.9852855,
   0.984468,
   0.9838842,
   0.9837674,
   0.9833003,
   0.9829499,
   0.9828331,
   0.9822492,
   0.9810814,
   0.9809646,
   0.9803807,
   0.97968,
   0.9790961,
   0.9785122,
   0.9781619,
   0.9776947,
   0.9771108,
   0.9764102,
   0.9758262,
   0.9750088,
   0.9745416,
   0.9737242,
   0.9727899,
   0.972206,
   0.9715053,
   0.9709214,
   0.970571,
   0.9692864,
   0.9685858,
   0.9678851,
   0.9667172,
   0.9653159,
   0.964732,
   0.9639145,
   0.9628635,
   0.9615789,
   0.9601775,
   0.9593601,
   0.958309,
   0.9574915,
   0.9567909,
   0.9557398,
   0.954572,
   0.9537545,
   0.9524699,
   0.9516525,
   0.949784,
   0.9487329,
   0.9466308,
   0.9451127,
   0.9434777,
   0.9416093,
   0.9405582,
   0.9376387,
   0.9347191,
   0.9325003,
   0.9298143,
   0.9272451,
   0.9242088,
   0.9215229,
   0.9176691,
   0.9138153,
   0.909144,
   0.9041224,
   0.8985169,
   0.8918603,
   0.8864884,
   0.8790144,
   0.8709564,
   0.8617307,
   0.8500525,
   0.8346374,
   0.8163027,
   0.7911947,
   0.7547588,
   0.6976527,
   0.5758496,
   0};
   TGraph *graph = new TGraph(102,_fx12,_fy12);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","",102,0,1.1);
   Graph_Graph12->SetMinimum(0);
   Graph_Graph12->SetMaximum(1.1);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph12->SetLineColor(ci);
   Graph_Graph12->GetXaxis()->SetLabelFont(42);
   Graph_Graph12->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph12->GetXaxis()->SetTitleFont(42);
   Graph_Graph12->GetYaxis()->SetLabelFont(42);
   Graph_Graph12->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph12->GetYaxis()->SetTitleOffset(0);
   Graph_Graph12->GetYaxis()->SetTitleFont(42);
   Graph_Graph12->GetZaxis()->SetLabelFont(42);
   Graph_Graph12->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph12->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph12);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Merged Top(#mu,jet), High p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.01665904,0,0.01665904,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.002105263,0,0.002105263,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n13->Modified();
   c1_n13->cd();
   c1_n13->SetSelected(c1_n13);
}
