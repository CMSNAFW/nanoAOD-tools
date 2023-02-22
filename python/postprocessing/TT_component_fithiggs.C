void TT_component_fithiggs()
{
//=========Macro generated from canvas: c1/c1
//=========  (Wed Sep 28 15:36:08 2022) by ROOT version 6.12/07
   TCanvas *c1 = new TCanvas("c1", "c1",67,57,700,500);
   c1->Range(18.75,-103.4531,331.25,655.6621);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   gStyle->SetOptStat(00000000);
   
   TH1F *h__1 = new TH1F("h__1","TT components for PN SFs measurement",25,50,300);
   h__1->SetBinContent(0,371.8386);
   h__1->SetBinContent(1,53.40793);
   h__1->SetBinContent(2,134.4299);
   h__1->SetBinContent(3,394.6759);
   h__1->SetBinContent(4,536.5716);
   h__1->SetBinContent(5,265.0079);
   h__1->SetBinContent(6,78.74604);
   h__1->SetBinContent(7,33.48812);
   h__1->SetBinContent(8,24.91361);
   h__1->SetBinContent(9,18.1784);
   h__1->SetBinContent(10,12.97929);
   h__1->SetBinContent(11,10.52461);
   h__1->SetBinContent(12,8.315492);
   h__1->SetBinContent(13,7.275934);
   h__1->SetBinContent(14,3.66161);
   h__1->SetBinContent(15,1.752265);
   h__1->SetBinContent(16,2.107318);
   h__1->SetBinContent(17,0.5137027);
   h__1->SetBinContent(18,0.1694881);
   h__1->SetBinContent(20,0.5680447);
   h__1->SetBinContent(22,0.4286917);
   h__1->SetBinContent(23,0.3887618);
   h__1->SetBinContent(24,0.4042616);
   h__1->SetBinContent(25,0.1527419);
   h__1->SetBinError(0,11.91702);
   h__1->SetBinError(1,4.52458);
   h__1->SetBinError(2,7.089796);
   h__1->SetBinError(3,12.21725);
   h__1->SetBinError(4,14.26033);
   h__1->SetBinError(5,10.03221);
   h__1->SetBinError(6,5.457973);
   h__1->SetBinError(7,3.54776);
   h__1->SetBinError(8,3.098291);
   h__1->SetBinError(9,2.560549);
   h__1->SetBinError(10,2.203936);
   h__1->SetBinError(11,1.92158);
   h__1->SetBinError(12,1.755515);
   h__1->SetBinError(13,1.561099);
   h__1->SetBinError(14,1.143241);
   h__1->SetBinError(15,0.8148056);
   h__1->SetBinError(16,0.8581647);
   h__1->SetBinError(17,0.5137027);
   h__1->SetBinError(18,0.1694881);
   h__1->SetBinError(20,0.4328218);
   h__1->SetBinError(22,0.4286917);
   h__1->SetBinError(23,0.3887617);
   h__1->SetBinError(24,0.4042616);
   h__1->SetBinError(25,0.1527419);
   h__1->SetEntries(5990);
   h__1->SetLineColor(kBlue);
   h__1->SetMarkerColor(kBlue);
   h__1->SetMarkerStyle(20);
   h__1->GetXaxis()->SetTitle("AK8 SD Mass [GeV]");
   h__1->GetYaxis()->SetTitle("Events/10 GeV");

   
   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   h__1->SetLineColor(ci);
   h__1->GetXaxis()->SetLabelFont(42);
   h__1->GetXaxis()->SetLabelSize(0.035);
   h__1->GetXaxis()->SetTitleSize(0.035);
   h__1->GetXaxis()->SetTitleFont(42);
   h__1->GetYaxis()->SetLabelFont(42);
   h__1->GetYaxis()->SetLabelSize(0.035);
   h__1->GetYaxis()->SetTitleSize(0.035);
   h__1->GetYaxis()->SetTitleOffset(0);
   h__1->GetYaxis()->SetTitleFont(42);
   h__1->GetZaxis()->SetLabelFont(42);
   h__1->GetZaxis()->SetLabelSize(0.035);
   h__1->GetZaxis()->SetTitleSize(0.035);
   h__1->GetZaxis()->SetTitleFont(42);
   h__1->Draw("");
   
  
   TH1F *htemp__2 = new TH1F("htemp__2","FatJet_M_nominal {w_nominal*PFSF*puSF*w_pt*((N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_MC_nominal==201 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1))}",25,50,300);
   htemp__2->SetBinContent(0,140.5367);
   htemp__2->SetBinContent(1,33.4781);
   htemp__2->SetBinContent(2,46.79637);
   htemp__2->SetBinContent(3,79.06357);
   htemp__2->SetBinContent(4,131.3573);
   htemp__2->SetBinContent(5,154.9767);
   htemp__2->SetBinContent(6,153.2128);
   htemp__2->SetBinContent(7,141.3915);
   htemp__2->SetBinContent(8,169.2928);
   htemp__2->SetBinContent(9,198.627);
   htemp__2->SetBinContent(10,274.5148);
   htemp__2->SetBinContent(11,399.6256);
   htemp__2->SetBinContent(12,589.8564);
   htemp__2->SetBinContent(13,659.8867);
   htemp__2->SetBinContent(14,498.2754);
   htemp__2->SetBinContent(15,230.5736);
   htemp__2->SetBinContent(16,94.83482);
   htemp__2->SetBinContent(17,42.43492);
   htemp__2->SetBinContent(18,18.48824);
   htemp__2->SetBinContent(19,12.38204);
   htemp__2->SetBinContent(20,4.039294);
   htemp__2->SetBinContent(21,4.735645);
   htemp__2->SetBinContent(22,3.599227);
   htemp__2->SetBinContent(23,2.876945);
   htemp__2->SetBinContent(24,3.210481);
   htemp__2->SetBinContent(25,0.8320807);
   htemp__2->SetBinContent(26,5.832078);
   htemp__2->SetBinError(0,7.097453);
   htemp__2->SetBinError(1,3.47547);
   htemp__2->SetBinError(2,4.114126);
   htemp__2->SetBinError(3,5.301898);
   htemp__2->SetBinError(4,6.915187);
   htemp__2->SetBinError(5,7.565981);
   htemp__2->SetBinError(6,7.420691);
   htemp__2->SetBinError(7,7.000958);
   htemp__2->SetBinError(8,7.476615);
   htemp__2->SetBinError(9,7.914491);
   htemp__2->SetBinError(10,9.267928);
   htemp__2->SetBinError(11,10.99195);
   htemp__2->SetBinError(12,13.3802);
   htemp__2->SetBinError(13,13.92574);
   htemp__2->SetBinError(14,12.03084);
   htemp__2->SetBinError(15,8.114287);
   htemp__2->SetBinError(16,5.2097);
   htemp__2->SetBinError(17,3.485607);
   htemp__2->SetBinError(18,2.334707);
   htemp__2->SetBinError(19,1.785807);
   htemp__2->SetBinError(20,1.016054);
   htemp__2->SetBinError(21,1.096244);
   htemp__2->SetBinError(22,0.937216);
   htemp__2->SetBinError(23,0.7585262);
   htemp__2->SetBinError(24,0.972538);
   htemp__2->SetBinError(25,0.4935973);
   htemp__2->SetBinError(26,1.263135);
   htemp__2->SetEntries(16876);
   htemp__2->SetDirectory(0);
   htemp__2->SetLineColor(kGreen);
   htemp__2->SetMarkerColor(kGreen);
   htemp__2->SetMarkerStyle(20);




   htemp__2->Draw("esame");
   
   TH1F *htemp__3 = new TH1F("htemp__3","FatJet_M_nominal {w_nominal*PFSF*puSF*w_pt*((N_muLoose_nominal+N_elLoose_nominal)==0 && AK8_region_nominal==1  && top_region_nominal==-1 && FatJet_MC_nominal!=201 && FatJet_MC_nominal!=200 && (TightMu_Iso_nominal<0.1 && TightEl_Iso_nominal<0.1))}",25,50,300);
   htemp__3->SetBinContent(0,29867.42);
   htemp__3->SetBinContent(1,4288.917);
   htemp__3->SetBinContent(2,5453.748);
   htemp__3->SetBinContent(3,5891.542);
   htemp__3->SetBinContent(4,5361.277);
   htemp__3->SetBinContent(5,4139.425);
   htemp__3->SetBinContent(6,2943.139);
   htemp__3->SetBinContent(7,2026.106);
   htemp__3->SetBinContent(8,1414.308);
   htemp__3->SetBinContent(9,957.966);
   htemp__3->SetBinContent(10,588.972);
   htemp__3->SetBinContent(11,356.908);
   htemp__3->SetBinContent(12,217.6924);
   htemp__3->SetBinContent(13,139.2285);
   htemp__3->SetBinContent(14,101.0446);
   htemp__3->SetBinContent(15,61.30087);
   htemp__3->SetBinContent(16,40.78967);
   htemp__3->SetBinContent(17,27.41017);
   htemp__3->SetBinContent(18,16.45225);
   htemp__3->SetBinContent(19,12.75824);
   htemp__3->SetBinContent(20,6.655763);
   htemp__3->SetBinContent(21,6.370293);
   htemp__3->SetBinContent(22,5.841519);
   htemp__3->SetBinContent(23,2.40374);
   htemp__3->SetBinContent(24,4.421698);
   htemp__3->SetBinContent(25,1.291915);
   htemp__3->SetBinContent(26,5.944575);
   htemp__3->SetBinError(0,101.83);
   htemp__3->SetBinError(1,39.23427);
   htemp__3->SetBinError(2,44.54201);
   htemp__3->SetBinError(3,46.37143);
   htemp__3->SetBinError(4,44.37755);
   htemp__3->SetBinError(5,38.90528);
   htemp__3->SetBinError(6,32.77323);
   htemp__3->SetBinError(7,27.02854);
   htemp__3->SetBinError(8,22.50116);
   htemp__3->SetBinError(9,18.35786);
   htemp__3->SetBinError(10,14.29508);
   htemp__3->SetBinError(11,11.10089);
   htemp__3->SetBinError(12,8.60029);
   htemp__3->SetBinError(13,6.903664);
   htemp__3->SetBinError(14,6.00703);
   htemp__3->SetBinError(15,4.648413);
   htemp__3->SetBinError(16,3.776548);
   htemp__3->SetBinError(17,3.076302);
   htemp__3->SetBinError(18,2.39357);
   htemp__3->SetBinError(19,2.086174);
   htemp__3->SetBinError(20,1.498518);
   htemp__3->SetBinError(21,1.484439);
   htemp__3->SetBinError(22,1.451955);
   htemp__3->SetBinError(23,0.8952425);
   htemp__3->SetBinError(24,1.292509);
   htemp__3->SetBinError(25,0.7051452);
   htemp__3->SetBinError(26,1.457855);
   htemp__3->SetEntries(233412);
   htemp__3->SetDirectory(0);

   htemp__3->SetLineColor(kRed);
   htemp__3->SetMarkerColor(kRed);
   htemp__3->SetMarkerStyle(20);


   htemp__3->Draw("esame");
   h__1->GetYaxis()->SetRangeUser(0.1,10000);

   TLegend *l = new TLegend(0.56,0.77,.78,0.89);
   l->AddEntry(h__1,"TT (2q)");
   l->AddEntry(htemp__2,"TT (1b+2q)");
   l->AddEntry(htemp__3,"TT (Other)");

   l->Draw("same");



   c1->SetLogy();
   

   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
