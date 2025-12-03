from PhysicsTools.NanoAODTools.postprocessing.modules.MET_HLT_Filter import *
from PhysicsTools.NanoAODTools.postprocessing.modules.electronSF import *
from PhysicsTools.NanoAODTools.postprocessing.modules.eleScaleRes import *
from PhysicsTools.NanoAODTools.postprocessing.modules.muonSF import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jetCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jetID import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jetVetoMap import *
from PhysicsTools.NanoAODTools.postprocessing.modules.puWeightProducer import *



def get_SF_modules():
    corr_repo = "/cvmfs/cms-griddata.cern.ch/cat/metadata/"
    corr_tag = "Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15"

    # Muon SF
    mu_idisosf_2024 = MuonSF(f"{corr_repo}MUO/{corr_tag}/latest/muon_Z.json.gz")
    mu_idisosf_2024.addCorrection("NUM_TightID_DEN_TrackerMuons", 'nominal', "IDSF")
    mu_idisosf_2024.addCorrection("NUM_TightID_DEN_TrackerMuons", 'systup', "ISDFUp")
    mu_idisosf_2024.addCorrection("NUM_TightID_DEN_TrackerMuons", 'systdown', "IDSFDown")

    # Electron SF
    reco24 = lambda pt: 'RecoAbove75' if pt>=75 else 'Reco20to75' 
    era24 = '2024Prompt'
    egm_corr_name = 'Electron-ID-SF'
    ele_recosf_2024 = ElectronSF(f"{corr_repo}EGM/{corr_tag}/latest/electron.json.gz")
    ele_recosf_2024.addCorrection(egm_corr_name, era24, reco24, 'sf', "RecoSF")
    ele_recosf_2024.addCorrection(egm_corr_name, era24, reco24, 'sfdown', "RecoSFDown")
    ele_recosf_2024.addCorrection(egm_corr_name, era24, reco24, 'sfup', "RecoSFUp")
    
    ele_idsf_2024 = ElectronSF(f"{corr_repo}EGM/{corr_tag}/latest/electronID.json.gz")
    ele_idsf_2024.addCorrection(egm_corr_name, '2024', 'wp80noiso', 'sf', "IDSF")
    ele_idsf_2024.addCorrection(egm_corr_name, '2024', 'wp80noiso', 'sfdown', "IDSFDown")
    ele_idsf_2024.addCorrection(egm_corr_name, '2024', 'wp80noiso', 'sfup', "IDSFUp")
   
    #Electron Scale resolution 
    ele_scale_res_2024 = eleScaleRes(
        json=f"{corr_repo}EGM/{corr_tag}/latest/electronSS_EtDependent.json.gz",
        scaleKey="Scale",
        smearKey="SmearAndSyst",
        overwritePt=False
    )    



    # Work in progress - 02/12/25
    """
    #Muon Scale resolution 
    mu_scale_res_2024 = muonScaleRes(
    json=f"{corr_repo}MUO/{corr_tag}/latest/muon_scalesmearing.json.gz",
    is_mc=True,      
    overwritePt=False,
    minPt=15.0        
    )
    """

    #MET HLT and pu_weight
    met_filter = MET_HLT_Filter_2024()
    pu_weight = puWeightProducer_2024()

    #JEC
    json_JERC = f"{corr_repo}JME/{corr_tag}/latest/jet_jerc.json.gz"
    json_JERsmear = f"{corr_repo}JME/JER-Smearing/latest/jer_smear.json.gz"

    #For now MC 
    year = 2024

    jes_systematics_11split = [
        "Regrouped_Absolute",
        "Regrouped_Absolute_{year}",
        "Regrouped_BBEC1",
        "Regrouped_BBEC1_{year}",
        "Regrouped_EC2",
        "Regrouped_EC2_{year}",
        "Regrouped_FlavorQCD",
        "Regrouped_HF",
        "Regrouped_HF_{year}",
        "Regrouped_RelativeBal",
        "Regrouped_RelativeSample_{year}",
    ]

    key = 'Summer24Prompt24_V2' #On 02/12/2025 there was and update, from V1 to V2
    L1Key = f"{key}_MC_L1FastJet_AK4PFPuppi"
    L2Key = f"{key}_MC_L2Relative_AK4PFPuppi"
    L3Key = f"{key}_MC_L3Absolute_AK4PFPuppi"
    L2L3Key = f"{key}_MC_L2L3Residual_AK4PFPuppi"
    scaleTotalKey = f"{key}_MC_Total_AK4PFPuppi"
    scaleKeyRegrouped11 = [f"{key}_MC_{label.format(year='2024')}_AK4PFPuppi" for label in jes_systematics_11split] # 11-source JES uncertainties
    smearKey = "JERSmear" # 1 Total source JES uncertainties
    JERKey = "Summer23BPixPrompt23_RunD_JRV1_MC_PtResolution_AK4PFPuppi"
    JERsfKey = "Summer23BPixPrompt23_RunD_JRV1_MC_ScaleFactor_AK4PFPuppi"
    overwritePt = True
    usePhiDependentJEC = True
    useRunDependentJEC = False
    useJesSplittingScheme11 = True
    scaleKey = scaleKeyRegrouped11 if useJesSplittingScheme11 else scaleTotalKey

    jetCorrected = jetJERC(json_JERC, json_JERsmear, L1Key, L2Key, L3Key, L2L3Key, scaleKey, smearKey, JERKey, JERsfKey, overwritePt, usePhiDependentJEC, useRunDependentJEC)

    #JetID:
    jetID = jetid_2024()

    #JetVeto:
    jetVeto = jetvetomaps_2024()

    return [met_filter, mu_idisosf_2024, ele_recosf_2024, ele_idsf_2024, ele_scale_res_2024, pu_weight, jetCorrected, jetID, jetVeto]
