void el_mer_hi_ROC_TvsOth()
{
//=========Macro generated from canvas: c1_n12/c1_n12
//=========  (Tue Oct 31 17:44:39 2023) by ROOT version 6.12/07
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
   0.9524794,
   0.9059917,
   0.8698347,
   0.8347107,
   0.7892562,
   0.7665289,
   0.7438017,
   0.7200413,
   0.6983471,
   0.6756198,
   0.6673554,
   0.6487603,
   0.6404959,
   0.6291322,
   0.6105372,
   0.5919421,
   0.5836777,
   0.5743802,
   0.5661157,
   0.5578513,
   0.5475206,
   0.536157,
   0.5289256,
   0.5216942,
   0.5123967,
   0.5051653,
   0.4927686,
   0.4834711,
   0.4772727,
   0.4679752,
   0.4607438,
   0.4535124,
   0.4483471,
   0.4442149,
   0.4380165,
   0.4297521,
   0.428719,
   0.4266529,
   0.4152893,
   0.4039256,
   0.3997934,
   0.3977273,
   0.3915289,
   0.3884298,
   0.375,
   0.3688017,
   0.3595041,
   0.3553719,
   0.3491735,
   0.3429752,
   0.3357438,
   0.3305785,
   0.3233471,
   0.3171488,
   0.3119835,
   0.3047521,
   0.2985537,
   0.2913223,
   0.2871901,
   0.2789256,
   0.2716942,
   0.2644628,
   0.2582645,
   0.2551653,
   0.2510331,
   0.2427686,
   0.2376033,
   0.2334711,
   0.2272727,
   0.2200413,
   0.2128099,
   0.2097107,
   0.2055785,
   0.1973141,
   0.1869835,
   0.1776859,
   0.1745868,
   0.1694215,
   0.1632231,
   0.1518595,
   0.1404959,
   0.1353306,
   0.1260331,
   0.1188017,
   0.1126033,
   0.1053719,
   0.09710744,
   0.09297521,
   0.08780992,
   0.08161157,
   0.07644628,
   0.07128099,
   0.06818182,
   0.0588843,
   0.05165289,
   0.04132231,
   0.03202479,
   0.02272727,
   0.009297521,
   0};
   Double_t _fy11[102] = {
   1,
   1,
   1,
   1,
   0.999707,
   0.9992676,
   0.9992676,
   0.9991211,
   0.9991211,
   0.9991211,
   0.9989747,
   0.9989747,
   0.9985352,
   0.9985352,
   0.9985352,
   0.9982423,
   0.9980958,
   0.9978029,
   0.9976563,
   0.9976563,
   0.9975099,
   0.9973634,
   0.9972169,
   0.9967775,
   0.996631,
   0.9963381,
   0.9961916,
   0.9960451,
   0.9957522,
   0.9956057,
   0.9950198,
   0.9947268,
   0.9941409,
   0.9937015,
   0.9934085,
   0.9932621,
   0.9931155,
   0.9928226,
   0.9925297,
   0.9919438,
   0.9912114,
   0.9912114,
   0.9910649,
   0.9906254,
   0.9900395,
   0.9894536,
   0.9887213,
   0.9879889,
   0.9878424,
   0.9875494,
   0.987403,
   0.98711,
   0.9866706,
   0.9862311,
   0.9854987,
   0.9849129,
   0.9838875,
   0.9828622,
   0.9819833,
   0.980665,
   0.9793467,
   0.9783214,
   0.9781749,
   0.9774425,
   0.9764172,
   0.9752454,
   0.97422,
   0.9727553,
   0.971144,
   0.9696792,
   0.967775,
   0.9654314,
   0.9632342,
   0.9611835,
   0.9598652,
   0.9584005,
   0.9553245,
   0.9531273,
   0.9491724,
   0.9465358,
   0.9443387,
   0.9412627,
   0.9378936,
   0.9336458,
   0.9285191,
   0.9228065,
   0.9163615,
   0.9105024,
   0.9040574,
   0.8954152,
   0.8858942,
   0.8753479,
   0.8604072,
   0.8437088,
   0.8227625,
   0.7983009,
   0.7649041,
   0.7225721,
   0.6563644,
   0.5554416,
   0.3601875,
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
   TLine *line = new TLine(0.1053719,0,0.1053719,1);

   ci = TColor::GetColor("#0000ff");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.02272727,0,0.02272727,1);

   ci = TColor::GetColor("#ffcc00");
   line->SetLineColor(ci);
   line->SetLineWidth(2);
   line->Draw();
   c1_n12->Modified();
   c1_n12->cd();
   c1_n12->SetSelected(c1_n12);
}
