import ROOT
import json
import array
import math

def RecoSF_hist(jsonfile, outfile):
    with open(jsonfile) as json_file: dict_ = json.load(json_file)
    f = ROOT.TFile.Open(outfile,"UPDATE")
    x_bins=array.array("d",[0.0,0.9,1.2,2.1,2.4])
    y_bins = array.array("d",[40,60])
    hist = ROOT.TH2F("NUM_TrackerMuon_DEN_genTracks_abseta_pt_syst","NUM_TrackerMuon_DEN_genTracks_abseta_pt_syst",4,x_bins,1,y_bins)
    
    for i in range(len(x_bins)-1):
        #temp_dict=dict_["NUM_TrackerMuons_DEN_genTracks"]["abseta_pt"]["abseta:["+str(x_bins[i])+","+str(x_bins[i+1])+"]"]["pt:[40,60]"]
        for j in range(1,2):
            temp_dict=dict_["NUM_TrackerMuons_DEN_genTracks"]["abseta_pt"]["abseta:["+str(x_bins[i])+","+str(x_bins[i+1])+"]"]["pt:["+str(int(y_bins[j-1]))+","+str(int(y_bins[j]))+"]"]
            hist.SetBinContent(i+1,j,temp_dict["value"])
            #hist.SetBinError(i+1,j,math.sqrt(temp_dict["syst"]**2+temp_dict["stat"]**2))
            hist.SetBinError(i+1,j,temp_dict["syst"])
    
    hist.Write()
    f.Close()

RecoSF_hist("2018NUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json","Mu_2018_medium_RECO.root")
RecoSF_hist("2017NUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json","Mu_2017_medium_RECO.root")
RecoSF_hist("2016preVFPNUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json","Mu_2016preVFP_medium_RECO.root")
RecoSF_hist("2016postVFPNUM_TrackerMuons_DEN_genTracks_Z_abseta_pt.json","Mu_2016postVFP_medium_RECO.root")
