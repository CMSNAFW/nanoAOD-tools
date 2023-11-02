void mu_mer_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n13/c1_n13
//=========  (Tue Oct 31 17:49:30 2023) by ROOT version 6.12/07
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
   0.8755682,
   0.7897727,
   0.7335227,
   0.6909091,
   0.6448864,
   0.6147727,
   0.56875,
   0.5375,
   0.5159091,
   0.4892046,
   0.4715909,
   0.4494318,
   0.4306818,
   0.4142045,
   0.3943182,
   0.3772727,
   0.36875,
   0.3545454,
   0.3369318,
   0.3267045,
   0.3193182,
   0.3039773,
   0.2960227,
   0.2840909,
   0.275,
   0.2676136,
   0.2625,
   0.2539773,
   0.2488636,
   0.2420454,
   0.2357955,
   0.2295455,
   0.2261364,
   0.2204545,
   0.2142045,
   0.2113636,
   0.2056818,
   0.2011364,
   0.1988636,
   0.1954546,
   0.1909091,
   0.1852273,
   0.1806818,
   0.1772727,
   0.1738636,
   0.1693182,
   0.1653409,
   0.1625,
   0.1556818,
   0.1522727,
   0.1482954,
   0.1454545,
   0.1414773,
   0.1397727,
   0.1369318,
   0.1301136,
   0.1278409,
   0.125,
   0.1227273,
   0.1215909,
   0.11875,
   0.1176136,
   0.1153409,
   0.1142045,
   0.1130682,
   0.1107955,
   0.1073864,
   0.1017045,
   0.09886364,
   0.09715909,
   0.09602273,
   0.09431818,
   0.09090909,
   0.08693182,
   0.08579545,
   0.08238637,
   0.08011363,
   0.07897727,
   0.07386363,
   0.07159091,
   0.06875,
   0.06590909,
   0.06420454,
   0.06079546,
   0.05852273,
   0.05454545,
   0.05284091,
   0.04886364,
   0.04318182,
   0.04090909,
   0.03977273,
   0.03693182,
   0.03409091,
   0.02954545,
   0.02727273,
   0.02215909,
   0.01818182,
   0.01306818,
   0.01022727,
   0};
   Double_t _fy12[102] = {
   1,
   1,
   1,
   1,
   0.9995288,
   0.9992932,
   0.9990576,
   0.9987042,
   0.9983508,
   0.9979974,
   0.9974084,
   0.9969372,
   0.9963482,
   0.995877,
   0.9954058,
   0.994699,
   0.99411,
   0.9937567,
   0.9934033,
   0.9930498,
   0.9925786,
   0.9919896,
   0.9917541,
   0.9910473,
   0.9906939,
   0.9901049,
   0.9895158,
   0.9893981,
   0.9890447,
   0.9886913,
   0.9885734,
   0.9881023,
   0.9870421,
   0.9869242,
   0.9864531,
   0.9857463,
   0.9853929,
   0.9848039,
   0.9845682,
   0.9840971,
   0.9835081,
   0.9829191,
   0.9823301,
   0.9815055,
   0.9810343,
   0.9804453,
   0.9796207,
   0.9790317,
   0.9783249,
   0.9777359,
   0.9773825,
   0.9760867,
   0.9753799,
   0.9746731,
   0.9734951,
   0.9721993,
   0.9716103,
   0.9707857,
   0.9697255,
   0.9687831,
   0.9674873,
   0.9667805,
   0.9658381,
   0.9650136,
   0.9643068,
   0.9632466,
   0.9620686,
   0.961244,
   0.960066,
   0.9592414,
   0.9573566,
   0.9564142,
   0.9544116,
   0.952998,
   0.9514666,
   0.9495818,
   0.9485216,
   0.9455766,
   0.9427494,
   0.9405112,
   0.9378018,
   0.9352103,
   0.9321475,
   0.9294381,
   0.9255507,
   0.9216633,
   0.9170691,
   0.9120038,
   0.9063494,
   0.8996348,
   0.8942161,
   0.8866768,
   0.8785487,
   0.8692425,
   0.8574626,
   0.841913,
   0.8234186,
   0.7980917,
   0.7613382,
   0.7037342,
   0.5808694,
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
   TLine *line = new TLine(0.1017045,0,0.1017045,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01306818,0,0.01306818,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n13->Modified();
   c1_n13->cd();
   c1_n13->SetSelected(c1_n13);
}
