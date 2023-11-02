void el_res_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n14/c1_n14
//=========  (Wed Oct 18 17:37:16 2023) by ROOT version 6.12/07
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
   0.780664,
   0.6593347,
   0.5731573,
   0.5093914,
   0.4611315,
   0.4193775,
   0.3860639,
   0.3583292,
   0.3356779,
   0.3160957,
   0.2978564,
   0.2823825,
   0.2674841,
   0.2545678,
   0.2433141,
   0.2336749,
   0.223668,
   0.2148281,
   0.2071231,
   0.19961,
   0.1924165,
   0.1856067,
   0.179772,
   0.1737296,
   0.1681187,
   0.1626676,
   0.1577441,
   0.1528366,
   0.1485365,
   0.1442844,
   0.1401282,
   0.1367713,
   0.132631,
   0.1290983,
   0.1257733,
   0.1224483,
   0.1189795,
   0.1157504,
   0.1126013,
   0.109692,
   0.1067506,
   0.1040171,
   0.1010119,
   0.09851815,
   0.09597647,
   0.09348274,
   0.09130873,
   0.08889493,
   0.08668894,
   0.08440302,
   0.08227696,
   0.08024681,
   0.07810477,
   0.07599469,
   0.07409243,
   0.07203031,
   0.07022396,
   0.06836965,
   0.06686702,
   0.06517256,
   0.06349409,
   0.06181562,
   0.06037693,
   0.05887431,
   0.05702,
   0.05550138,
   0.0538389,
   0.05224036,
   0.05059386,
   0.04869159,
   0.04712502,
   0.0453986,
   0.043864,
   0.04256918,
   0.04116246,
   0.03986764,
   0.03810924,
   0.03646275,
   0.03499209,
   0.03360135,
   0.03208274,
   0.03061208,
   0.02939719,
   0.02763879,
   0.02615215,
   0.02450565,
   0.02303499,
   0.02132455,
   0.01950221,
   0.01752002,
   0.01593746,
   0.01406717,
   0.01219688,
   0.0100868,
   0.008456288,
   0.006522052,
   0.004220151,
   0.002190003,
   0.0002557667,
   0};
   Double_t _fy13[102] = {
   1,
   1,
   0.9991876,
   0.9980984,
   0.9962706,
   0.994332,
   0.9920242,
   0.9896795,
   0.9874825,
   0.9855254,
   0.9833284,
   0.9812422,
   0.979359,
   0.9766081,
   0.9746141,
   0.9722509,
   0.9701647,
   0.9682446,
   0.9660476,
   0.9640167,
   0.9622627,
   0.9600472,
   0.9576471,
   0.9558378,
   0.9539546,
   0.9519792,
   0.9498929,
   0.9477143,
   0.945702,
   0.9439111,
   0.9418249,
   0.9396093,
   0.9375784,
   0.9359168,
   0.9338306,
   0.9318551,
   0.9297504,
   0.9277749,
   0.9255964,
   0.9234732,
   0.9214239,
   0.9190052,
   0.9170852,
   0.9143712,
   0.912248,
   0.9100509,
   0.9078724,
   0.9055646,
   0.9032383,
   0.9009489,
   0.8986781,
   0.8965734,
   0.8942102,
   0.8914039,
   0.8890591,
   0.8863821,
   0.883742,
   0.880991,
   0.8782402,
   0.8755816,
   0.8731999,
   0.8697105,
   0.8666088,
   0.8634333,
   0.8598515,
   0.8566391,
   0.8529097,
   0.8491803,
   0.8455616,
   0.8413522,
   0.8368289,
   0.8328964,
   0.8282992,
   0.8229636,
   0.8179787,
   0.8134924,
   0.8079536,
   0.8020825,
   0.7965069,
   0.7896574,
   0.7827893,
   0.7752751,
   0.7676132,
   0.7592127,
   0.7498893,
   0.7400488,
   0.7285282,
   0.7163614,
   0.7028469,
   0.6877446,
   0.67039,
   0.6499335,
   0.6284432,
   0.6032236,
   0.5745698,
   0.5376634,
   0.4948305,
   0.4355845,
   0.3548667,
   0.2322022,
   0.05097482,
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
   TLine *line = new TLine(0.05887431,0,0.05887431,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.008456288,0,0.008456288,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n14->Modified();
   c1_n14->cd();
   c1_n14->SetSelected(c1_n14);
}
