void el_res_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n10/c1_n10
//=========  (Tue Oct 31 17:49:27 2023) by ROOT version 6.12/07
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
   0.9964665,
   0.9931853,
   0.9856133,
   0.9727411,
   0.954316,
   0.9293286,
   0.9096416,
   0.8871782,
   0.8599193,
   0.8346795,
   0.8107017,
   0.7864715,
   0.7657748,
   0.7438163,
   0.7241292,
   0.7054518,
   0.6908127,
   0.6733973,
   0.6534578,
   0.6390712,
   0.6272085,
   0.6143362,
   0.5991923,
   0.5890964,
   0.5759717,
   0.5636042,
   0.5492176,
   0.5340737,
   0.525997,
   0.5174155,
   0.5053003,
   0.4934376,
   0.4843513,
   0.4745078,
   0.4666835,
   0.4586067,
   0.4510348,
   0.4439677,
   0.4341242,
   0.4245331,
   0.4149419,
   0.40737,
   0.4005553,
   0.3934881,
   0.3849066,
   0.3778395,
   0.3707723,
   0.36421,
   0.3568905,
   0.3513377,
   0.3450278,
   0.3402322,
   0.3344271,
   0.3283695,
   0.3225644,
   0.3162544,
   0.3109541,
   0.3036345,
   0.2970722,
   0.2905098,
   0.2839475,
   0.2776376,
   0.2695608,
   0.2632509,
   0.2574457,
   0.2521454,
   0.2458354,
   0.2397779,
   0.2332155,
   0.227158,
   0.2226148,
   0.2168097,
   0.2115093,
   0.2069662,
   0.2009086,
   0.1945987,
   0.1862696,
   0.180212,
   0.1736497,
   0.1660777,
   0.159263,
   0.1527007,
   0.1466431,
   0.1420999,
   0.1347804,
   0.1287229,
   0.1241797,
   0.116103,
   0.1102978,
   0.1037355,
   0.09262998,
   0.08657244,
   0.07824331,
   0.07092378,
   0.06007067,
   0.05022716,
   0.03836446,
   0.01968703,
   0.004290762,
   0};
   Double_t _fy9[102] = {
   1,
   1,
   0.9999586,
   0.9999586,
   0.9998345,
   0.9997932,
   0.9997932,
   0.9995863,
   0.9995036,
   0.9994208,
   0.9990898,
   0.9987589,
   0.9984693,
   0.9980142,
   0.9975591,
   0.9970213,
   0.9966077,
   0.9960698,
   0.9955734,
   0.9952424,
   0.9947873,
   0.9942082,
   0.9935049,
   0.9926775,
   0.9921811,
   0.9915605,
   0.9908572,
   0.9901953,
   0.9896161,
   0.989161,
   0.9887887,
   0.9881681,
   0.9871339,
   0.9866788,
   0.9861823,
   0.9854791,
   0.9848171,
   0.9843621,
   0.9837829,
   0.9830382,
   0.9822108,
   0.9811766,
   0.9806387,
   0.9799355,
   0.9787357,
   0.9778669,
   0.9769982,
   0.9762121,
   0.9750952,
   0.9742677,
   0.9732749,
   0.972282,
   0.9712064,
   0.9700066,
   0.9693033,
   0.9677726,
   0.9666142,
   0.9652491,
   0.9642562,
   0.9633046,
   0.962229,
   0.9606156,
   0.959209,
   0.9578024,
   0.9561476,
   0.9544928,
   0.9526725,
   0.9511418,
   0.9487837,
   0.9474185,
   0.9462188,
   0.9441089,
   0.9414198,
   0.93931,
   0.9362899,
   0.9342628,
   0.9312014,
   0.9285951,
   0.9257405,
   0.9224723,
   0.9188317,
   0.9154807,
   0.9125434,
   0.9086133,
   0.9031938,
   0.8976088,
   0.8921893,
   0.8849909,
   0.8775029,
   0.8673258,
   0.8565696,
   0.8431656,
   0.8292239,
   0.8117657,
   0.7901704,
   0.7631971,
   0.7250952,
   0.6761543,
   0.5967235,
   0.4614016,
   0.179588,
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
   TLine *line = new TLine(0.1102978,0,0.1102978,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01968703,0,0.01968703,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n10->Modified();
   c1_n10->cd();
   c1_n10->SetSelected(c1_n10);
}
