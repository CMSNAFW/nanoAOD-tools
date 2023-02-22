import ROOT
import json
import array

def RecoSF_hist(jsonfile, outfile):
    with open(jsonfile) as json_file: dict_ = json.load(json_file)
    f = ROOT.TFile.Open(outfile,"RECREATE")
    x_bins=array.array("d",[0.0,1.6,2.4])
    y_bins = array.array("d",[50,100,150,200,300,400,600,1500,3500])
    hist = ROOT.TH2F("NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p","NUM_TrackerMuon_DEN_genTracks_HighPt_abseta_p",2,x_bins,8,y_bins)
    
    for i in range(len(x_bins)-1):
        #temp_dict=dict_["NUM_TrackerMuons_DEN_genTracks"]["abseta_pt"]["abseta:["+str(x_bins[i])+","+str(x_bins[i+1])+"]"]["pt:[40,60]"]
        for j in range(1,9):
            temp_dict=dict_["NUM_TrackerMuons_DEN_genTracks"]["abseta_p"]["abseta:["+str(x_bins[i])+","+str(x_bins[i+1])+"]"]["p:["+str(int(y_bins[j-1]))+","+str(int(y_bins[j]))+"]"]
            hist.SetBinContent(i+1,j,temp_dict["value"])
            hist.SetBinError(i+1,j,temp_dict["syst"])
    
    hist.Write()
    f.Close()

RecoSF_hist("muonefficiencies/Run2/UL/2018/NUM_TrackerMuons_DEN_genTracks_HighPt_abseta_p.json","Mu_2018_RECO.root")
RecoSF_hist("muonefficiencies/Run2/UL/2017/NUM_TrackerMuons_DEN_genTracks_HighPt_abseta_p.json","Mu_2017_RECO.root")
RecoSF_hist("muonefficiencies/Run2/UL/2016_preVFP/NUM_TrackerMuons_DEN_genTracks_HighPt_abseta_p.json","Mu_2016preVFP_RECO.root")
RecoSF_hist("muonefficiencies/Run2/UL/2016_postVFP/NUM_TrackerMuons_DEN_genTracks_HighPt_abseta_p.json","Mu_2016postVFP_RECO.root")
