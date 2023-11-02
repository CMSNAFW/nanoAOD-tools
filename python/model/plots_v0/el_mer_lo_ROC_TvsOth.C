void el_mer_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n16/c1_n16
//=========  (Wed Oct 18 17:37:18 2023) by ROOT version 6.12/07
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
   0.1780787,
   0.1018439,
   0.07600763,
   0.06189446,
   0.05291695,
   0.04656652,
   0.04231973,
   0.03911983,
   0.03631497,
   0.03391504,
   0.03200893,
   0.0302312,
   0.02872014,
   0.02748561,
   0.02630045,
   0.02516469,
   0.02422644,
   0.02315981,
   0.02214255,
   0.02138208,
   0.02057223,
   0.01997966,
   0.01926856,
   0.01853772,
   0.017797,
   0.01712542,
   0.01649334,
   0.01606866,
   0.01567361,
   0.01509091,
   0.01464648,
   0.01417242,
   0.01374774,
   0.01340207,
   0.01308603,
   0.01276012,
   0.01248358,
   0.01209841,
   0.01173299,
   0.01150583,
   0.01127868,
   0.01096264,
   0.0106861,
   0.01038982,
   0.01005402,
   0.009737983,
   0.009500953,
   0.009313304,
   0.009026893,
   0.008809616,
   0.008582462,
   0.008384936,
   0.008128154,
   0.007901001,
   0.00766397,
   0.007328178,
   0.007101024,
   0.006923252,
   0.006705974,
   0.006567707,
   0.006449192,
   0.00624179,
   0.006073894,
   0.005886246,
   0.005629463,
   0.005491195,
   0.005264041,
   0.00513565,
   0.004997383,
   0.00481961,
   0.004651714,
   0.004493694,
   0.004335674,
   0.004128273,
   0.003980129,
   0.003822109,
   0.003664089,
   0.003535698,
   0.003308544,
   0.0031604,
   0.003051762,
   0.002873989,
   0.002775226,
   0.002577701,
   0.002409805,
   0.002222156,
   0.002093765,
   0.001945621,
   0.001797478,
   0.001718468,
   0.001550571,
   0.001392551,
   0.00118515,
   0.001007378,
   0.0008987388,
   0.0007407188,
   0.0005629463,
   0.0002962875,
   0.0001086388,
   0};
   Double_t _fy15[102] = {
   1,
   1,
   0.9886663,
   0.980038,
   0.9748464,
   0.9711904,
   0.9679731,
   0.9649751,
   0.9627815,
   0.9603685,
   0.958248,
   0.957005,
   0.9556157,
   0.9539339,
   0.952764,
   0.9510091,
   0.9496929,
   0.9483767,
   0.9471337,
   0.9456713,
   0.9443551,
   0.943112,
   0.9419421,
   0.9407722,
   0.9393829,
   0.9382129,
   0.9374086,
   0.9363118,
   0.9352881,
   0.9343375,
   0.9332407,
   0.9317052,
   0.9303159,
   0.9290729,
   0.9273179,
   0.9251974,
   0.9234425,
   0.9221995,
   0.9210296,
   0.9194209,
   0.9178122,
   0.916496,
   0.9147412,
   0.9137906,
   0.912255,
   0.9110851,
   0.9091108,
   0.9077216,
   0.9059666,
   0.9047236,
   0.9028224,
   0.9011407,
   0.8993858,
   0.8971922,
   0.895876,
   0.8941942,
   0.89222,
   0.8900263,
   0.8881252,
   0.8860047,
   0.8842498,
   0.8814712,
   0.8787657,
   0.8762796,
   0.8740129,
   0.871088,
   0.8685288,
   0.8661889,
   0.8626791,
   0.8593156,
   0.8556595,
   0.8525885,
   0.8493711,
   0.8459345,
   0.8423516,
   0.8383299,
   0.8343814,
   0.8295555,
   0.8241445,
   0.8195379,
   0.8134689,
   0.8067417,
   0.8016964,
   0.7951887,
   0.7886809,
   0.7821,
   0.7726675,
   0.7630155,
   0.7527055,
   0.743346,
   0.7307692,
   0.7181193,
   0.7015941,
   0.6848494,
   0.6616701,
   0.6384908,
   0.6088769,
   0.5690261,
   0.5177684,
   0.4368236,
   0.2694501,
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
   TLine *line = new TLine(0.05291695,0,0.05291695,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.004651714,0,0.004651714,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n16->Modified();
   c1_n16->cd();
   c1_n16->SetSelected(c1_n16);
}
