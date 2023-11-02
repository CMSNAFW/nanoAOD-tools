void el_res_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n14/c1_n14
//=========  (Tue Oct 31 17:49:32 2023) by ROOT version 6.12/07
   TCanvas *c1_n14 = new TCanvas("c1_n14", "c1_n14",6,27,700,500);
   c1_n14->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n14->SetFillColor(0);
   c1_n14->SetBorderMode(0);
   c1_n14->SetBorderSize(2);
   c1_n14->SetFrameBorderMode(0);
   c1_n14->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Resolved Top(e,jet), Low p_{T}");
   
   Double_t _fx13[102] = {
   1,
   1,
   0.9851471,
   0.9156849,
   0.8408063,
   0.775141,
   0.7193311,
   0.669077,
   0.6257747,
   0.5877771,
   0.5556703,
   0.5266626,
   0.4990508,
   0.4750963,
   0.4524541,
   0.43252,
   0.4148473,
   0.399436,
   0.3829359,
   0.3684739,
   0.3557429,
   0.3436261,
   0.3318443,
   0.3204534,
   0.3107935,
   0.3007427,
   0.2913898,
   0.2822324,
   0.2740242,
   0.2656765,
   0.2584175,
   0.2510749,
   0.2438718,
   0.2382043,
   0.231057,
   0.2249428,
   0.2191915,
   0.2134123,
   0.2074097,
   0.2018817,
   0.1964096,
   0.1913563,
   0.1862471,
   0.181473,
   0.1762522,
   0.1718968,
   0.1674577,
   0.1631861,
   0.1593891,
   0.1552013,
   0.1513764,
   0.147384,
   0.1436708,
   0.1401251,
   0.1363839,
   0.1326986,
   0.1294042,
   0.1258027,
   0.1226478,
   0.1194092,
   0.1167849,
   0.1138254,
   0.110894,
   0.1079625,
   0.1054498,
   0.1028254,
   0.0995868,
   0.0969345,
   0.09403093,
   0.09123904,
   0.08836339,
   0.08504104,
   0.08230498,
   0.07928974,
   0.07660953,
   0.07434809,
   0.07189123,
   0.0696298,
   0.06655871,
   0.06368306,
   0.06111452,
   0.05868558,
   0.05603328,
   0.05346474,
   0.0513429,
   0.04827182,
   0.04567536,
   0.04279971,
   0.04023117,
   0.03724384,
   0.03406109,
   0.03059914,
   0.02783517,
   0.02456865,
   0.02130214,
   0.01761684,
   0.01476911,
   0.01139092,
   0.007370596,
   0.003824892,
   0.0004467028,
   0};
   Double_t _fy13[102] = {
   1,
   1,
   0.9998882,
   0.9994038,
   0.9983604,
   0.9972611,
   0.9956774,
   0.9941682,
   0.9924913,
   0.9907958,
   0.988914,
   0.9870135,
   0.985467,
   0.9830076,
   0.9812748,
   0.9791321,
   0.9771571,
   0.9753684,
   0.9733748,
   0.9715489,
   0.9698533,
   0.9677666,
   0.9654748,
   0.9637048,
   0.9618788,
   0.9599597,
   0.9579288,
   0.9557862,
   0.9538112,
   0.9520597,
   0.9499916,
   0.9478117,
   0.9458181,
   0.9441971,
   0.9421102,
   0.9401539,
   0.9380857,
   0.9361107,
   0.9339122,
   0.9317695,
   0.9297013,
   0.9272605,
   0.9253228,
   0.9226398,
   0.9204971,
   0.9182799,
   0.9160813,
   0.9138268,
   0.9114792,
   0.9091874,
   0.9068957,
   0.9047717,
   0.9023868,
   0.8995547,
   0.8971884,
   0.8944868,
   0.8918224,
   0.8890463,
   0.88627,
   0.8835871,
   0.8811835,
   0.8776807,
   0.8745505,
   0.8713458,
   0.8677312,
   0.8644892,
   0.8607255,
   0.8569805,
   0.8533286,
   0.8490805,
   0.8445157,
   0.840547,
   0.8359076,
   0.830523,
   0.8254923,
   0.8209648,
   0.8153751,
   0.8094501,
   0.8038233,
   0.7969108,
   0.7899797,
   0.7823964,
   0.7746642,
   0.7661866,
   0.7567774,
   0.7468466,
   0.7352201,
   0.7229416,
   0.709303,
   0.694062,
   0.6765479,
   0.6559036,
   0.6342159,
   0.6087645,
   0.5798476,
   0.5426021,
   0.4993758,
   0.4395856,
   0.3581264,
   0.2343351,
   0.05144305,
   0};
   TGraph *graph = new TGraph(102,_fx13,_fy13);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph13 = new TH1F("Graph_Graph13","",102,0,1.1);
   Graph_Graph13->SetMinimum(0);
   Graph_Graph13->SetMaximum(1.1);
   Graph_Graph13->SetDirectory(0);
   Graph_Graph13->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph13->SetLineColor(ci);
   Graph_Graph13->GetXaxis()->SetLabelFont(42);
   Graph_Graph13->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetXaxis()->SetTitleFont(42);
   Graph_Graph13->GetYaxis()->SetLabelFont(42);
   Graph_Graph13->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetYaxis()->SetTitleOffset(0);
   Graph_Graph13->GetYaxis()->SetTitleFont(42);
   Graph_Graph13->GetZaxis()->SetLabelFont(42);
   Graph_Graph13->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph13->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph13);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Resolved Top(e,jet), Low p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.1028254,0,0.1028254,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01476911,0,0.01476911,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n14->Modified();
   c1_n14->cd();
   c1_n14->SetSelected(c1_n14);
}
