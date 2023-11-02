void mu_res_lo_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n2/c1_n2
//=========  (Tue Oct 31 17:47:16 2023) by ROOT version 6.12/07
   TCanvas *c1_n2 = new TCanvas("c1_n2", "c1_n2",6,27,700,500);
   c1_n2->Range(-0.1335784,-0.1275,1.133578,1.1475);
   c1_n2->SetFillColor(0);
   c1_n2->SetBorderMode(0);
   c1_n2->SetBorderSize(2);
   c1_n2->SetFrameBorderMode(0);
   c1_n2->SetFrameBorderMode(0);
   
   TMultiGraph *multigraph = new TMultiGraph();
   multigraph->SetName("");
   multigraph->SetTitle("ROC Curve TvsOth Resolved Top(#mu,jet), Low p_{T}");
   
   Double_t _fx1[102] = {
   1,
   1,
   0.9830368,
   0.904608,
   0.8174907,
   0.7468711,
   0.6836212,
   0.633585,
   0.5905565,
   0.5516394,
   0.5185922,
   0.4887774,
   0.4629189,
   0.4403186,
   0.4188043,
   0.4001862,
   0.3836626,
   0.3687164,
   0.3542356,
   0.339548,
   0.3263602,
   0.3150341,
   0.3045614,
   0.2940112,
   0.2841332,
   0.275212,
   0.2663167,
   0.258585,
   0.250543,
   0.2436647,
   0.2353641,
   0.2294166,
   0.222771,
   0.2164874,
   0.2109019,
   0.2051872,
   0.1995242,
   0.1936802,
   0.1882499,
   0.1833368,
   0.178553,
   0.1735106,
   0.1688043,
   0.1644342,
   0.1604003,
   0.1561078,
   0.1520221,
   0.14729,
   0.1431009,
   0.1392222,
   0.1357313,
   0.1321887,
   0.1287495,
   0.1250776,
   0.1218453,
   0.1181475,
   0.1148376,
   0.1116312,
   0.1085281,
   0.1054251,
   0.1026841,
   0.0997621,
   0.09704696,
   0.09394394,
   0.09115122,
   0.0883585,
   0.08595366,
   0.08329023,
   0.08080782,
   0.07804096,
   0.07576541,
   0.07338643,
   0.07139532,
   0.06883533,
   0.06671494,
   0.06415495,
   0.0614398,
   0.05885395,
   0.05683699,
   0.05443215,
   0.05182044,
   0.04949317,
   0.04721763,
   0.04520066,
   0.0425631,
   0.04064957,
   0.03845159,
   0.0363312,
   0.03371949,
   0.03157323,
   0.02968556,
   0.027229,
   0.02482416,
   0.02192801,
   0.0196266,
   0.01701489,
   0.01427389,
   0.01163633,
   0.008248862,
   0.004783823,
   0.001577369,
   0};
   Double_t _fy1[102] = {
   1,
   1,
   0.9999502,
   0.9991202,
   0.9981905,
   0.9968957,
   0.9954846,
   0.9940403,
   0.9923304,
   0.9903051,
   0.9883628,
   0.9863541,
   0.9842624,
   0.9822039,
   0.980162,
   0.9781533,
   0.9761612,
   0.9744015,
   0.9723098,
   0.9706498,
   0.9685913,
   0.9667485,
   0.9648229,
   0.9632126,
   0.9613533,
   0.959245,
   0.9575351,
   0.9555264,
   0.9535509,
   0.9515588,
   0.9498323,
   0.9480727,
   0.9461967,
   0.9443707,
   0.9425943,
   0.9407351,
   0.9388758,
   0.9369999,
   0.934709,
   0.9326505,
   0.9305422,
   0.9286165,
   0.9271058,
   0.9248813,
   0.9225904,
   0.9205319,
   0.9185398,
   0.9162323,
   0.9139414,
   0.9116837,
   0.9093263,
   0.9071516,
   0.9049105,
   0.9019888,
   0.8996481,
   0.8970583,
   0.8948836,
   0.8926259,
   0.890169,
   0.8874133,
   0.8847239,
   0.882101,
   0.8793951,
   0.8762907,
   0.8735682,
   0.870165,
   0.8669112,
   0.8638069,
   0.8607026,
   0.8573492,
   0.8533982,
   0.8496796,
   0.8466085,
   0.8425578,
   0.8383911,
   0.8340417,
   0.8294598,
   0.8249112,
   0.8201966,
   0.8153325,
   0.8097547,
   0.8038116,
   0.7976028,
   0.7906803,
   0.7835585,
   0.775308,
   0.7665759,
   0.7569807,
   0.7463727,
   0.7347189,
   0.7216873,
   0.7077426,
   0.6905774,
   0.6722999,
   0.6496232,
   0.6225306,
   0.5894618,
   0.5462333,
   0.4840632,
   0.3884591,
   0.2036256,
   0};
   TGraph *graph = new TGraph(102,_fx1,_fy1);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","",102,0,1.1);
   Graph_Graph1->SetMinimum(0);
   Graph_Graph1->SetMaximum(1.1);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph1->SetLineColor(ci);
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleOffset(0);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
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
   TText *pt_LaTex = pt->AddText("ROC Curve TvsOth Resolved Top(#mu,jet), Low p_{T}");
   pt->Draw();
   TLine *line = new TLine(0.1026841,0,0.1026841,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.01427389,0,0.01427389,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n2->Modified();
   c1_n2->cd();
   c1_n2->SetSelected(c1_n2);
}
