void el_res_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n10/c1_n10
//=========  (Wed Oct 18 17:37:11 2023) by ROOT version 6.12/07
   TCanvas *c1_n10 = new TCanvas("c1_n10", "c1_n10",6,27,700,500);
   c1_n10->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n10->SetFillColor(0);
   c1_n10->SetBorderMode(0);
   c1_n10->SetBorderSize(2);
   c1_n10->SetFrameBorderMode(0);
   c1_n10->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Resolved Top(e,jet), High p_{T}");
   
   Double_t _fx9[102] = {
   1,
   1,
   0.5670002,
   0.4813031,
   0.4347303,
   0.4034309,
   0.3784516,
   0.3564818,
   0.3381988,
   0.3223234,
   0.3072004,
   0.2933564,
   0.2804905,
   0.2697314,
   0.2597246,
   0.2492664,
   0.2406892,
   0.2325634,
   0.2260176,
   0.2188699,
   0.2112708,
   0.2055526,
   0.2008126,
   0.196223,
   0.1905048,
   0.1868182,
   0.1823038,
   0.1777142,
   0.1725228,
   0.167256,
   0.164397,
   0.1615379,
   0.157475,
   0.153713,
   0.1507787,
   0.147393,
   0.1449101,
   0.1418253,
   0.1391167,
   0.1366338,
   0.1333985,
   0.1300128,
   0.1270785,
   0.1245204,
   0.1221879,
   0.120006,
   0.1172974,
   0.1151907,
   0.1127831,
   0.1106764,
   0.108344,
   0.106463,
   0.1044316,
   0.1027763,
   0.1009706,
   0.09916485,
   0.09728388,
   0.09532767,
   0.09374765,
   0.09141524,
   0.08930855,
   0.08727711,
   0.08524565,
   0.08336468,
   0.0808818,
   0.07900083,
   0.07719509,
   0.07561508,
   0.07365887,
   0.07185313,
   0.06989692,
   0.06809119,
   0.06666165,
   0.06485592,
   0.06320066,
   0.06184636,
   0.06004063,
   0.05815966,
   0.05567677,
   0.0537958,
   0.05183959,
   0.04950719,
   0.04747574,
   0.04551952,
   0.04371379,
   0.04235949,
   0.04017757,
   0.03837183,
   0.03701753,
   0.03460989,
   0.03287939,
   0.03092318,
   0.02761267,
   0.02580694,
   0.02332405,
   0.02114213,
   0.01790685,
   0.01497254,
   0.01143631,
   0.005868633,
   0.001279061,
   0};
   Double_t _fy9[102] = {
   1,
   1,
   0.9993853,
   0.9986067,
   0.998156,
   0.9978691,
   0.9976642,
   0.9973774,
   0.9970086,
   0.9968446,
   0.9964758,
   0.9957792,
   0.9951645,
   0.9945499,
   0.9937713,
   0.9929517,
   0.9924189,
   0.9917223,
   0.9910257,
   0.990575,
   0.9899192,
   0.9891407,
   0.9882801,
   0.9873376,
   0.9867639,
   0.9861082,
   0.9853297,
   0.984633,
   0.9840593,
   0.9835266,
   0.9829529,
   0.9822563,
   0.9810269,
   0.9805352,
   0.9800025,
   0.9791419,
   0.9784043,
   0.9777486,
   0.97697,
   0.9761505,
   0.9752489,
   0.9741426,
   0.9735688,
   0.9728312,
   0.9715609,
   0.9707003,
   0.9698398,
   0.9689792,
   0.9677089,
   0.9668483,
   0.9657829,
   0.9646765,
   0.9635291,
   0.9622997,
   0.9616031,
   0.9599639,
   0.9588165,
   0.9573823,
   0.9563988,
   0.9554153,
   0.9543089,
   0.9525878,
   0.9510716,
   0.9495554,
   0.9478343,
   0.9461132,
   0.9443101,
   0.942753,
   0.9402942,
   0.9389009,
   0.9377126,
   0.9355817,
   0.9329181,
   0.9307872,
   0.9277958,
   0.9257878,
   0.9227554,
   0.9201738,
   0.9173462,
   0.914027,
   0.9103799,
   0.9070196,
   0.9041101,
   0.9002172,
   0.894808,
   0.8892759,
   0.8839077,
   0.8767365,
   0.8692374,
   0.8591157,
   0.8484613,
   0.8351842,
   0.8213744,
   0.8040814,
   0.7826906,
   0.7559726,
   0.7182314,
   0.6697537,
   0.5910749,
   0.457034,
   0.177888,
   0};
   TGraph *graph = new TGraph(102,_fx9,_fy9);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph9 = new TH1F("Graph_Graph9","",102,0,1.1);
   Graph_Graph9->SetMinimum(0);
   Graph_Graph9->SetMaximum(1.1);
   Graph_Graph9->SetDirectory(0);
   Graph_Graph9->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph9->SetLineColor(ci);
   Graph_Graph9->GetXaxis()->SetLabelFont(42);
   Graph_Graph9->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph9->GetXaxis()->SetTitleFont(42);
   Graph_Graph9->GetYaxis()->SetLabelFont(42);
   Graph_Graph9->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph9->GetYaxis()->SetTitleOffset(0);
   Graph_Graph9->GetYaxis()->SetTitleFont(42);
   Graph_Graph9->GetZaxis()->SetLabelFont(42);
   Graph_Graph9->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph9->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph9);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Resolved Top(e,jet), High p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.03287939,0,0.03287939,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.005868633,0,0.005868633,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n10->Modified();
   c1_n10->cd();
   c1_n10->SetSelected(c1_n10);
}
