void el_mer_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n12/c1_n12
//=========  (Wed Oct 18 17:37:13 2023) by ROOT version 6.12/07
   TCanvas *c1_n12 = new TCanvas("c1_n12", "c1_n12",6,27,700,500);
   c1_n12->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n12->SetFillColor(0);
   c1_n12->SetBorderMode(0);
   c1_n12->SetBorderSize(2);
   c1_n12->SetFrameBorderMode(0);
   c1_n12->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Merged Top(e,jet), High p_{T}");
   
   Double_t _fx11[102] = {
   1,
   1,
   0.4884509,
   0.407761,
   0.3627964,
   0.3350785,
   0.3113643,
   0.2965814,
   0.2833385,
   0.2697875,
   0.2587003,
   0.2476132,
   0.2408377,
   0.2331383,
   0.2282107,
   0.2217432,
   0.2143517,
   0.2069603,
   0.2026486,
   0.198029,
   0.1937173,
   0.1897136,
   0.184786,
   0.1807823,
   0.1780105,
   0.1740068,
   0.170619,
   0.1672313,
   0.1629196,
   0.1589159,
   0.1564521,
   0.1524484,
   0.1499846,
   0.1472128,
   0.1456729,
   0.1425932,
   0.1401294,
   0.1367416,
   0.1358177,
   0.1342778,
   0.1305821,
   0.1268864,
   0.1256544,
   0.1250385,
   0.1228827,
   0.1219587,
   0.1173391,
   0.1151832,
   0.1124115,
   0.1111796,
   0.1090237,
   0.1068679,
   0.104712,
   0.1031722,
   0.1007083,
   0.09855251,
   0.09670465,
   0.09454881,
   0.09270096,
   0.09054512,
   0.08869726,
   0.08623344,
   0.08376963,
   0.08130582,
   0.07945796,
   0.07853403,
   0.07730213,
   0.07483831,
   0.07329843,
   0.07175855,
   0.06991069,
   0.06775485,
   0.06529104,
   0.06436711,
   0.0631352,
   0.06036341,
   0.05728365,
   0.05420388,
   0.05327995,
   0.05174007,
   0.04989221,
   0.04619649,
   0.04280875,
   0.04126886,
   0.0381891,
   0.03603326,
   0.03387742,
   0.03172159,
   0.02925778,
   0.02802587,
   0.02617801,
   0.02433015,
   0.02279027,
   0.02125039,
   0.02032646,
   0.01755466,
   0.01539883,
   0.01231906,
   0.009547275,
   0.006775485,
   0.002771789,
   0};
   Double_t _fy11[102] = {
   1,
   1,
   0.9994197,
   0.9989845,
   0.9982591,
   0.9978239,
   0.9976788,
   0.9975337,
   0.9975337,
   0.9973887,
   0.9972436,
   0.9969534,
   0.9965182,
   0.9963731,
   0.996228,
   0.9959379,
   0.9955027,
   0.9952126,
   0.9950675,
   0.9950675,
   0.9946322,
   0.9943421,
   0.994197,
   0.9934716,
   0.9931815,
   0.9928913,
   0.9927463,
   0.9926012,
   0.992166,
   0.9920209,
   0.9914406,
   0.9910054,
   0.99028,
   0.9898448,
   0.9895546,
   0.9892645,
   0.9891194,
   0.9888293,
   0.9882489,
   0.9876686,
   0.9867982,
   0.9867982,
   0.9866531,
   0.9862179,
   0.9854925,
   0.9847671,
   0.9837517,
   0.9830263,
   0.9827361,
   0.982446,
   0.9821558,
   0.9818656,
   0.9814304,
   0.9809952,
   0.9798346,
   0.9792543,
   0.9782388,
   0.9769331,
   0.9757725,
   0.9743218,
   0.9730161,
   0.9720006,
   0.9718555,
   0.9711301,
   0.9701146,
   0.9688089,
   0.9677934,
   0.9661976,
   0.9643116,
   0.9625707,
   0.9606848,
   0.9583635,
   0.9560423,
   0.9535761,
   0.9519803,
   0.9505295,
   0.9473379,
   0.9451618,
   0.9412447,
   0.9386334,
   0.9364573,
   0.9334107,
   0.930074,
   0.9257218,
   0.9204991,
   0.914551,
   0.9081677,
   0.9023647,
   0.8959814,
   0.8872769,
   0.877702,
   0.8672566,
   0.852459,
   0.8359205,
   0.8150297,
   0.7906572,
   0.7575802,
   0.7156535,
   0.6500798,
   0.5501233,
   0.3567387,
   0};
   TGraph *graph = new TGraph(102,_fx11,_fy11);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph11 = new TH1F("Graph_Graph11","",102,0,1.1);
   Graph_Graph11->SetMinimum(0);
   Graph_Graph11->SetMaximum(1.1);
   Graph_Graph11->SetDirectory(0);
   Graph_Graph11->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph11->SetLineColor(ci);
   Graph_Graph11->GetXaxis()->SetLabelFont(42);
   Graph_Graph11->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph11->GetXaxis()->SetTitleFont(42);
   Graph_Graph11->GetYaxis()->SetLabelFont(42);
   Graph_Graph11->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph11->GetYaxis()->SetTitleOffset(0);
   Graph_Graph11->GetYaxis()->SetTitleFont(42);
   Graph_Graph11->GetZaxis()->SetLabelFont(42);
   Graph_Graph11->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph11->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph11);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Merged Top(e,jet), High p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.03172159,0,0.03172159,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.006775485,0,0.006775485,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n12->Modified();
   c1_n12->cd();
   c1_n12->SetSelected(c1_n12);
}
