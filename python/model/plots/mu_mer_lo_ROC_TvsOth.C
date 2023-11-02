void mu_mer_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n17/c1_n17
//=========  (Tue Oct 31 17:44:45 2023) by ROOT version 6.12/07
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
   0.6051005,
   0.4707532,
   0.3859124,
   0.3246918,
   0.2795253,
   0.2444214,
   0.2141952,
   0.1915351,
   0.1732918,
   0.156508,
   0.1445251,
   0.1333487,
   0.122902,
   0.1139532,
   0.1059262,
   0.09836002,
   0.09233014,
   0.08660752,
   0.08169144,
   0.07712102,
   0.0736644,
   0.07039981,
   0.06725045,
   0.06352498,
   0.06022199,
   0.05737988,
   0.05557476,
   0.05327035,
   0.05150363,
   0.0496601,
   0.04777816,
   0.0463187,
   0.04455198,
   0.0435534,
   0.04232438,
   0.04113377,
   0.03944387,
   0.03836847,
   0.03748512,
   0.03591044,
   0.03498867,
   0.03383647,
   0.03268426,
   0.03195453,
   0.03103276,
   0.03022622,
   0.02926604,
   0.02861313,
   0.02780658,
   0.02707685,
   0.02630872,
   0.0256558,
   0.02481085,
   0.02415793,
   0.02369705,
   0.02319776,
   0.02262165,
   0.02162308,
   0.02112379,
   0.02047087,
   0.0200868,
   0.01928025,
   0.01885778,
   0.01832008,
   0.01735991,
   0.01682222,
   0.01643815,
   0.01593886,
   0.01532435,
   0.01490187,
   0.01470984,
   0.01421055,
   0.01382648,
   0.01332719,
   0.01275108,
   0.01213657,
   0.0117141,
   0.01121481,
   0.01086915,
   0.01044667,
   0.009947383,
   0.009332872,
   0.008718362,
   0.007988632,
   0.007566156,
   0.006990053,
   0.006375542,
   0.006068287,
   0.005684219,
   0.005108115,
   0.004724047,
   0.004147943,
   0.003840688,
   0.003418213,
   0.003072551,
   0.002534854,
   0.002150785,
   0.001881937,
   0.001075393,
   0};
   Double_t _fy16[102] = {
   1,
   1,
   0.9965596,
   0.9942876,
   0.9914314,
   0.9888997,
   0.9855891,
   0.9820837,
   0.9787082,
   0.9750081,
   0.9728659,
   0.9703992,
   0.9679974,
   0.96605,
   0.9632587,
   0.9611815,
   0.9589744,
   0.9567673,
   0.9550146,
   0.953197,
   0.951704,
   0.9496917,
   0.9478092,
   0.9459267,
   0.9441091,
   0.9424213,
   0.9405388,
   0.938851,
   0.9374878,
   0.9360597,
   0.9348913,
   0.9338527,
   0.9326842,
   0.9309315,
   0.9293736,
   0.9280104,
   0.9271016,
   0.9257384,
   0.9243752,
   0.9225576,
   0.9213892,
   0.9195716,
   0.9180136,
   0.9167153,
   0.9152223,
   0.9139889,
   0.912431,
   0.9113924,
   0.9095099,
   0.9080818,
   0.9064589,
   0.9047062,
   0.9027588,
   0.9008763,
   0.8993184,
   0.8977605,
   0.8962675,
   0.8949692,
   0.8926972,
   0.8904901,
   0.8881532,
   0.8865303,
   0.8843882,
   0.8823758,
   0.8810127,
   0.8791301,
   0.8772476,
   0.874716,
   0.8725089,
   0.8695878,
   0.8673158,
   0.8640701,
   0.8608893,
   0.8576436,
   0.8543979,
   0.8511522,
   0.8477118,
   0.8440117,
   0.84148,
   0.8373256,
   0.8337553,
   0.8299254,
   0.8261603,
   0.8212269,
   0.8162285,
   0.8097371,
   0.8046738,
   0.7986368,
   0.7913665,
   0.7837066,
   0.7761766,
   0.7671535,
   0.7582603,
   0.7470951,
   0.7330087,
   0.7145732,
   0.6943849,
   0.6669263,
   0.630964,
   0.5729958,
   0.4512171,
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
   TLine *line = new TLine(0.1059262,0,0.1059262,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01044667,0,0.01044667,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n17->Modified();
   c1_n17->cd();
   c1_n17->SetSelected(c1_n17);
}
