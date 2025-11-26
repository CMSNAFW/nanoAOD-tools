"""
Compute electron SFs using correctionlib, and store in new branches.
Load as:
 eleSF = electronSF("POG/EGM/2016postVFP_UL/electron.json.gz")
 eleSF.addCorrection("NUM_TrackerMuons_DEN_genTracks", "2016postVFP", "sf")
 eleSF.addCorrection("NUM_MediumID_DEN_TrackerMuons", "2016postVFP", "sfdown", "sfsysdn")
 eleSF.addCorrection("NUM_MediumID_DEN_TrackerMuons", "2016postVFP", "sfup", "sfsysup")

See example in test/example_electronSF.py for details.
"""

from __future__ import print_function
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from correctionlib import CorrectionSet

class ElectronSF(Module):
    def __init__(self, json, collection="Electron"):
        """Electron SF correction module.
        Parameters:
            json: the correction file
            collection: name of the collection to be corrected
        Use addCorrection() to set which factors should be added.
        """
        self.collection = collection
        self.names = [ ]
        self.scenarios = [ ]
        self.wps = [ ]
        self.valtypes = [ ]
        self.varnames = [ ]
        self.evaluators = [ ]
        self._getSF_funcs = []
        self.evaluator = CorrectionSet.from_file(json)
    
    def addCorrection(self, name, scenario, wp, valtype, varname=None):
        """
        Call this method to add a correction factor.
        Parameters:
            name: name of the corrections, e.g. 'UL-Electron-ID-SF'
            scenario: year/scenario, e.g. '2016postVFP'
            wp: working point
                - string, e.g. 'Loose', 'Medium', 'wp80iso', ...
                - function of pT, e.g. lambda pt: 'RecoAbove20' if pt>=20 else 'RecoBelow20'
            valtype: type of factor, e.g. 'sf', 'sfup', 'sfdown', ...
            varname: branch name suffix (defaults to {wp}_{valtype})
        """
        if varname==None: # default suffix
          assert isinstance(wp,str), "Please use the varname option to name the branch"
          varname = wp+'_'+valtype
        self.names.append(name)
        self.scenarios.append(scenario)
        self.valtypes.append(valtype)
        self.wps.append(wp)
        self.varnames.append(f"{self.collection}_{varname}") # branch name
        
        ev = self.evaluator[name]
        self.evaluators.append(ev)
        
        varlist = [i.name for i in ev.inputs]

        if "phi" in varlist:
            self._getSF_funcs.append(lambda scenario, valtype, wp, eta, pt, phi, evaluator=ev: evaluator.evaluate(scenario, valtype, wp, eta, pt, phi))
        else:
            self._getSF_funcs.append(lambda scenario, valtype, wp, eta, pt, phi, evaluator=ev: evaluator.evaluate(scenario, valtype, wp, eta, pt))
    
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        """Add branch for every correction to output file."""
        self.out = wrappedOutputTree        
        for varname in set(self.varnames): # avoid duplicates
            self.out.branch(varname, 'F', lenVar='nElectron')

    def analyze(self, event):
        pts = [max(10.001,event.Electron_pt[i]) for i in range(event.nElectron)]
        etas = [event.Electron_eta[i] for i in range(event.nElectron)]
        phis = [event.Electron_phi[i] for i in range(event.nElectron)]
        for ic,getSF_func in enumerate(self._getSF_funcs):
            # We cannot make a single call to evaluate passing eta, pt as arrays
            # since POG JSONS are currently provided with flow="error", so we
            # have to loop to protect for values out of binning range.
            sfs = [1.]*event.nElectron
            for iEle in range(event.nElectron):
                try:
                  if isinstance(self.wps[ic],str): # WP is a simple string
                      wp = self.wps[ic]
                  else: # assume WP is a function of pT
                      wp = self.wps[ic](pts[iEle]) # evaluate WP in pT
                      if wp==None: # evaluate correction only if WP is defined
                         continue
                     
                  sfs[iEle] = getSF_func(self.scenarios[ic], self.valtypes[ic], wp, etas[iEle], pts[iEle], phis[iEle])

                     
                except:
                    #print(f"ElectronSF.analyze: Exception for {self.scenarios[ic]}, {self.valtypes[ic]}, wp={self.wps[ic]}, eta={etas[iEle]:6.4f}, pt={pts[iEle]:6.4f}, phi={phis[iEle]:6.4f}")
                    pass # default sf = 1
            self.out.fillBranch(self.varnames[ic], sfs)
        return True
'''
EGM_repo = "/cvmfs/cms-griddata.cern.ch/cat/metadata/EGM/"
set = 'Electron-ID-SF'
# Add electron reconstruction scale factor
reco = lambda pt: 'RecoAbove75' if pt>=75 else 'Reco20to75' if pt<75 and pt>=20 else 'RecoBelow20'
era22 = '2022Re-recoBCD'
ele_recoidsf_2022 = lambda : ElectronSF(f"{EGM_repo}22CDSep23-Summer22-NanoAODv12/latest/electronID.json.gz")
ele_recoidsf_2022.addCorrection(set, era22, reco, 'sf', 'Electron_RecoSF')
ele_recoidsf_2022.addCorrection(set, era22, reco, 'sfdown', 'Electron_RecoSFDown')
ele_recoidsf_2022.addCorrection(set, era22, reco, 'sfup', 'Electron_RecoSFUp')
ele_recoidsf_2022.addCorrection(set, era22, 'wp80noiso', 'sf', 'Electron_IDSF')
ele_recoidsf_2022.addCorrection(set, era22, 'wp80noiso', 'sfdown', 'Electron_IDSFDown')
ele_recoidsf_2022.addCorrection(set, era22, 'wp80noiso', 'sfup', 'Electron_IDSFUp')
era22EE = '2022Re-recoE+PromptFG'
ele_recoidsf_2022EE = lambda : ElectronSF(f"{EGM_repo}22EFGSep23-Summer22EE-NanoAODv12/latest/electronID.json.gz")
ele_recoidsf_2022.addCorrection(set, era22EE, reco, 'sf', 'Electron_RecoSF')
ele_recoidsf_2022.addCorrection(set, era22EE, reco, 'sfdown', 'Electron_RecoSFDown')
ele_recoidsf_2022.addCorrection(set, era22EE, reco, 'sfup', 'Electron_RecoSFUp')
ele_recoidsf_2022.addCorrection(set, era22EE, 'wp80noiso', 'sf', 'Electron_IDSF')
ele_recoidsf_2022.addCorrection(set, era22EE, 'wp80noiso', 'sfdown', 'Electron_IDSFDown')
ele_recoidsf_2022.addCorrection(set, era22EE, 'wp80noiso', 'sfup', 'Electron_IDSFUp')
era23 = '2023PromptC'
ele_recoidsf_2023 = lambda : ElectronSF(f"{EGM_repo}23CSep23-Summer23-NanoAODv12/latest/electronID.json.gz")
ele_recoidsf_2022.addCorrection(set, era23, reco, 'sf', 'Electron_RecoSF')
ele_recoidsf_2022.addCorrection(set, era23, reco, 'sfdown', 'Electron_RecoSFDown')
ele_recoidsf_2022.addCorrection(set, era23, reco, 'sfup', 'Electron_RecoSFUp')
ele_recoidsf_2022.addCorrection(set, era23, 'wp80noiso', 'sf', 'Electron_IDSF')
ele_recoidsf_2022.addCorrection(set, era23, 'wp80noiso', 'sfdown', 'Electron_IDSFDown')
ele_recoidsf_2022.addCorrection(set, era23, 'wp80noiso', 'sfup', 'Electron_IDSFUp')
era23BP = '2023PromptD'
ele_recoidsf_2023BP = lambda : ElectronSF(f"{EGM_repo}23DSep23-Summer23BPix-NanoAODv12/latest/electronID.json.gz")
ele_recoidsf_2022.addCorrection(set, era23BP, reco, 'sf', 'Electron_RecoSF')
ele_recoidsf_2022.addCorrection(set, era23BP, reco, 'sfdown', 'Electron_RecoSFDown')
ele_recoidsf_2022.addCorrection(set, era23BP, reco, 'sfup', 'Electron_RecoSFUp')
ele_recoidsf_2022.addCorrection(set, era23BP, 'wp80noiso', 'sf', 'Electron_IDSF')
ele_recoidsf_2022.addCorrection(set, era23BP, 'wp80noiso', 'sfdown', 'Electron_IDSFDown')
ele_recoidsf_2022.addCorrection(set, era23BP, 'wp80noiso', 'sfup', 'Electron_IDSFUp')

#reco = lambda pt: 'RecoAbove75' if pt>=75 else 'Reco20to75' if pt<75 and pt>=20 else 'RecoBelow20'
reco24 = lambda pt: 'RecoAbove75' if pt>=75 else 'Reco20to75' 
era24 = '2024Prompt'
ele_recosf_2024 = lambda : ElectronSF(f"{EGM_repo}24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/electron.json.gz")
ele_recosf_2024.addCorrection(set, era24, reco24, 'sf', 'Electron_RecoSF')
ele_recosf_2024.addCorrection(set, era24, reco24, 'sfdown', 'Electron_RecoSFDown')
ele_recosf_2024.addCorrection(set, era24, reco24, 'sfup', 'Electron_RecoSFUp')
ele_idsf_2024 = lambda : ElectronSF(f"{EGM_repo}24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/latest/electronID.json.gz")
ele_idsf_2024.addCorrection(set, era24, 'wp80noiso', 'sf', "Electron_IDSF")
ele_idsf_2024.addCorrection(set, era24, 'wp80noiso', 'sfdown', "Electron_IDSFDown")
ele_idsf_2024.addCorrection(set, era24, 'wp80noiso', 'sfup', "Electron_IDSFUp")
'''