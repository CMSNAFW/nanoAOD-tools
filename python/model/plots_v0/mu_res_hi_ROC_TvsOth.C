void mu_res_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n11/c1_n11
//=========  (Wed Oct 18 17:37:12 2023) by ROOT version 6.12/07
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
   0.5188335,
   0.435137,
   0.3847505,
   0.351792,
   0.3260014,
   0.3062544,
   0.2907941,
   0.2740689,
   0.2612087,
   0.2491919,
   0.2388616,
   0.2287421,
   0.2203795,
   0.2126493,
   0.2049192,
   0.1981729,
   0.1910049,
   0.1850316,
   0.1793394,
   0.173577,
   0.1678145,
   0.1637386,
   0.1587491,
   0.1540408,
   0.1499649,
   0.1456079,
   0.1422347,
   0.1383696,
   0.1348559,
   0.1314828,
   0.1295854,
   0.1274069,
   0.1245257,
   0.1218552,
   0.1190443,
   0.1167252,
   0.1139143,
   0.1112439,
   0.1091356,
   0.1062544,
   0.103584,
   0.101546,
   0.09922699,
   0.09669712,
   0.09402671,
   0.09234013,
   0.09002108,
   0.08784258,
   0.08608574,
   0.08425861,
   0.0829234,
   0.08123682,
   0.07969079,
   0.0775123,
   0.07568517,
   0.07420941,
   0.07238229,
   0.07069571,
   0.06886858,
   0.06690092,
   0.06542516,
   0.06416023,
   0.0626142,
   0.06078707,
   0.05895994,
   0.05783556,
   0.0563598,
   0.05495432,
   0.05319747,
   0.05214336,
   0.05024596,
   0.04926212,
   0.04799719,
   0.0471539,
   0.04574842,
   0.04392129,
   0.04265636,
   0.04139142,
   0.04033732,
   0.03858046,
   0.03696416,
   0.03591005,
   0.03478567,
   0.03295854,
   0.03155306,
   0.03042867,
   0.02916374,
   0.02768798,
   0.02614195,
   0.02459592,
   0.02234715,
   0.02080113,
   0.01890372,
   0.01693605,
   0.01433591,
   0.01229796,
   0.009908644,
   0.007519325,
   0.002740689,
   0};
   Double_t _fy10[102] = {
   1,
   1,
   0.999571,
   0.9991421,
   0.9987912,
   0.9987131,
   0.9981672,
   0.9977773,
   0.9972313,
   0.9968024,
   0.9961395,
   0.9957885,
   0.9953595,
   0.9946576,
   0.9942676,
   0.9937217,
   0.9929808,
   0.9924349,
   0.9919669,
   0.991382,
   0.9904851,
   0.9899002,
   0.9891202,
   0.9886133,
   0.9877554,
   0.9869365,
   0.9863906,
   0.9861176,
   0.9853377,
   0.9846748,
   0.9838558,
   0.9834659,
   0.982881,
   0.982335,
   0.9816331,
   0.9807752,
   0.9797224,
   0.9788254,
   0.9780455,
   0.9770707,
   0.9763297,
   0.9753549,
   0.974614,
   0.974029,
   0.9728202,
   0.9718453,
   0.9708704,
   0.9697395,
   0.9688426,
   0.9680627,
   0.9671658,
   0.9660349,
   0.9648261,
   0.9636172,
   0.9625254,
   0.9613945,
   0.9604976,
   0.9594837,
   0.9576509,
   0.956598,
   0.9555451,
   0.9543363,
   0.9525815,
   0.9512166,
   0.9496958,
   0.948175,
   0.9463812,
   0.9445874,
   0.9433006,
   0.9416628,
   0.9401419,
   0.9380362,
   0.9359694,
   0.9339417,
   0.9317189,
   0.9301201,
   0.9280143,
   0.9260256,
   0.9236858,
   0.9211512,
   0.9184214,
   0.9159647,
   0.9130011,
   0.9093745,
   0.9062159,
   0.9022384,
   0.8976369,
   0.8921385,
   0.8866012,
   0.8795429,
   0.8721728,
   0.8630479,
   0.8541959,
   0.8421463,
   0.8259632,
   0.8090001,
   0.784589,
   0.7485572,
   0.6970441,
   0.6054048,
   0.396467,
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
   TLine *line = new TLine(0.02916374,0,0.02916374,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.007519325,0,0.007519325,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n11->Modified();
   c1_n11->cd();
   c1_n11->SetSelected(c1_n11);
}
