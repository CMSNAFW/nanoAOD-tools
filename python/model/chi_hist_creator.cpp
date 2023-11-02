#include <TFile.h>
#include <TH1F.h>
#include <TString.h>
#include <fstream>
#include <iostream>

int chi_hist_creator() {
  ifstream infile("Chi2_text.txt");
  if (!infile.is_open()) {
    cerr << "Error: Could not open the data file." << endl;
    return 1;
  }

  const char* histName = "hist";
  const char* histTitle = "Reduced Chi2";
  const int numBins = 12;
  const float minX = 0.0;
  const float maxX = 3;

  TH1F* hist = new TH1F(histName, histTitle, numBins, minX, maxX);

  string value;
  string dummy1, dummy2, dummy3,dummy4; // To skip the first three columns

  while (infile >> dummy1 >> dummy2 >> dummy3 >> value >> dummy4) {
    hist->Fill(std::stof(value));
  }

  infile.close();

  TCanvas *c1 = new TCanvas();
  hist->GetXaxis()->SetTitle("Reduced Chi2");
  hist->Draw();
    c1->SaveAs("chi2_test.pdf");
  c1->SaveAs("chi2_test.C");
  //TFile* output = new TFile("output.root", "RECREATE");
  //hist->Write();
  //output->Close();

  return 0;
}
