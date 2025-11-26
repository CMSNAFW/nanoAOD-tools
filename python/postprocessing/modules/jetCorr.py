"""Add branches for muon scale and resolution corrections.
See example in test/example_jetCorr.py for usage.
"""

###
# Useful CMStalk thread on how implementing jet corrections: https://cms-talk.web.cern.ch/t/jes-for-2022-re-reco-cde-and-prompt-fg/32873/3
# Minimal demo provided from JME POG: https://github.com/cms-jet/JECDatabase/blob/master/scripts/JERC2JSON/minimalDemo.py
# TODO:
# - Implementing JES uncertainties. TBD which scheme we want to implement
###

from __future__ import print_function
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
import os
import numpy as np
import correctionlib
import math
import itertools

class jetJERC(Module):
    def __init__(self, json_JERC, json_JERsmear, L1Key=None, L2Key=None, L3Key=None, L2L3Key=None, scaleKey=None, smearKey=None, JERKey=None, JERsfKey=None, overwritePt=False, usePhiDependentJEC=False, useRunDependentJEC=False):
        """Correct jets following recommendations of JME POG.
        Parameters:
            json_JERC: full path of json file with JERC corrections
            json_JERsmear: full path of json file with smearing terms for JER
            L1Key: key for L1 corrections
            L2Key: key for L2 corrections
            L3Key: key for L3 corrections
            L2L3Key: key for residual corrections
            scaleKey : key for JES uncertainties 1 Total source or JES uncertainties splitted in 11 sources
            smearKey: key for smearing formula (None for Data)
            JERKey: key for JER (None for Data)
            JERsfKey: key for JER scale factor (None for Data)
            overwritePt: replace value in the pt branch, and store the old one as "uncorrected_pt"
        """
        self.overwritePt = overwritePt
        self.usePhiDependentJEC = usePhiDependentJEC
        self.useRunDependentJEC = useRunDependentJEC

        self.evaluator_JERC = correctionlib.CorrectionSet.from_file(json_JERC)
        self.evaluator_jer = correctionlib.CorrectionSet.from_file(json_JERsmear)

        ## Starting from Run 3, the use of PUPPI jets eliminates the need for L1 corrections. To maintain compatibility with Run 2 scripts, a dummy file is provided.
        self.evaluator_L1 = self.evaluator_JERC[L1Key]
        ## For the next step, there is a mismatch between the terminology in the twiki and the tags in correctionlib
        ## MC-truth = L2 + L3
        self.evaluator_L2 = self.evaluator_JERC[L2Key]
        self.evaluator_L3 = self.evaluator_JERC[L3Key]
        ## L2L3residuals should be applied only to data
        ## A dummy file with all entries equal to 1 is provided for MC to have a common script for both data and MC
        self.evaluator_L2L3 = self.evaluator_JERC[L2L3Key]

        self.is_mc = False
        self.evaluator_JERsmear = None
        self.evaluator_JER = None
        self.evaluator_JERsf = None
        self.evaluator_JES = None
        self.scaleKey = scaleKey
        if smearKey != None: ## JER is applied only to MC
            self.evaluator_JERsmear = self.evaluator_jer[smearKey]
            self.evaluator_JER = self.evaluator_JERC[JERKey]
            self.evaluator_JERsf = self.evaluator_JERC[JERsfKey]
            if isinstance(self.scaleKey, list):
                # Regrouped 11-source JES
                self.evaluator_JES = {}
                for full_key in self.scaleKey:
                    label = full_key.split("_Regrouped_")[-1]
                    if label.endswith("_AK4PFPuppi"):
                        label = label[:-len("_AK4PFPuppi")]
                    label = label.replace("-", "_").replace(".", "_")
                    self.evaluator_JES[label] = self.evaluator_JERC[full_key]
            else:
                # 1 Total JES
                self.evaluator_JES = self.evaluator_JERC[self.scaleKey]
            self.is_mc = True

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        if self.overwritePt :
            self.out.branch("Jet_pt", "F", lenVar="nJet", title="pT (with JES/JER corrections)")
            self.out.branch("Jet_mass", "F", lenVar="nJet", title="mass (with JES/JER corrections)", limitedPrecision=12)
            self.out.branch("Jet_uncorrected_pt", "F", lenVar="nJet", title="original (uncorrected) pT")
            self.out.branch("Jet_uncorrected_mass", "F", lenVar="nJet", title="original (uncorrected) mass", limitedPrecision=12)
            self.out.branch("Jet_defaultpt", "F", lenVar="nJet", title="default pT (with JES/JER corrections)")
            self.out.branch("PuppiMET_pt", "F", title="MET pT (with JES/JER corrections)")
            self.out.branch("PuppiMET_phi", "F", title="MET phi (with JES/JER corrections)")
        else:
            self.out.branch("Jet_corrected_pt", "F", lenVar="nJet", title="pT (with JES/JER corrections)")
            self.out.branch("Jet_corrected_mass", "F", lenVar="nJet", title="mass (with JES/JER corrections)", limitedPrecision=12)
            self.out.branch("PuppiMET_corrected_pt", "F", title="MET pT (with JES/JER corrections)")
            self.out.branch("PuppiMET_corrected_phi", "F", title="MET phi (with JES/JER corrections)")
        if self.is_mc:
            self.out.branch("Jet_smearUp_pt", "F", lenVar="nJet", title="smearing uncertainty")
            self.out.branch("Jet_smearDn_pt", "F", lenVar="nJet", title="smearing uncertainty")
            self.out.branch("Jet_smearUp_mass", "F", lenVar="nJet", title="smearing uncertainty", limitedPrecision=12)
            self.out.branch("Jet_smearDn_mass", "F", lenVar="nJet", title="smearing uncertainty", limitedPrecision=12)
            self.out.branch("PuppiMET_pt_UnclEnUp", "F", title="MET pT unclestered energy up")
            self.out.branch("PuppiMET_phi_UnclEnUp", "F", title="MET phi unclestered energy up")
            self.out.branch("PuppiMET_pt_UnclEnDown", "F", title="MET pT unclestered energy down")
            self.out.branch("PuppiMET_phi_UnclEnDown", "F", title="MET phi unclestered energy down")
            self.out.branch("PuppiMET_pt_jerUp", "F", title="MET pT (with JER Up uncertainty)")
            self.out.branch("PuppiMET_phi_jerUp", "F", title="MET phi (with JER Up uncertainty)")
            self.out.branch("PuppiMET_pt_jerDown", "F", title="MET pT (with JER Down uncertainty)")
            self.out.branch("PuppiMET_phi_jerDown", "F", title="MET phi (with JER Down uncertainty)")

            if isinstance(self.scaleKey, list):  # Regrouped 11-source JES
                for label in self.evaluator_JES.keys():
                    self.out.branch(f"Jet_{label}_ScaleUp_pt", "F", lenVar="nJet")
                    self.out.branch(f"Jet_{label}_ScaleDn_pt", "F", lenVar="nJet")
                    self.out.branch(f"Jet_{label}_ScaleUp_mass", "F", lenVar="nJet", limitedPrecision=12)
                    self.out.branch(f"Jet_{label}_ScaleDn_mass", "F", lenVar="nJet", limitedPrecision=12)
                    self.out.branch(f"PuppiMET_{label}_ScaleUp_pt", "F", title="MET pT (with JES uncertainty)")
                    self.out.branch(f"PuppiMET_{label}_ScaleUp_phi", "F", title="MET phi (with JES uncertainty)")
                    self.out.branch(f"PuppiMET_{label}_ScaleDown_pt", "F", title="MET pT (with JES uncertainty)")
                    self.out.branch(f"PuppiMET_{label}_ScaleDown_phi", "F", title="MET phi (with JES uncertainty)")
            else:
                self.out.branch("Jet_scaleUp_pt", "F", lenVar="nJet", title="scale uncertainty")
                self.out.branch("Jet_scaleDn_pt", "F", lenVar="nJet", title="scale uncertainty")
                self.out.branch("Jet_scaleUp_mass", "F", lenVar="nJet", title="scale uncertainty", limitedPrecision=12)
                self.out.branch("Jet_scaleDn_mass", "F", lenVar="nJet", title="scale uncertainty", limitedPrecision=12)
                self.out.branch(f"PuppiMET_ScaleUp_pt", "F", title="MET pT (with JES uncertainty)")
                self.out.branch(f"PuppiMET_ScaleUp_phi", "F", title="MET phi (with JES uncertainty)")
                self.out.branch(f"PuppiMET_ScaleDown_pt", "F", title="MET pT (with JES uncertainty)")
                self.out.branch(f"PuppiMET_ScaleDown_phi", "F", title="MET phi (with JES uncertainty)")


    def fixPhi(self, phi):
        if phi > np.pi:
            phi -= 2*np.pi
        elif phi < -np.pi:
            phi += 2*np.pi
        return phi

    def analyze(self, event):
        debug = False
        jets = Collection(event, "Jet")
        lowPtJets = Collection(event, "CorrT1METJet" )
        met = Object(event, "PuppiMET")
        rawmet = Object(event, "RawPuppiMET")

        ( t1met_px,       t1met_py       ) = ( met.pt*math.cos(met.phi), met.pt*math.sin(met.phi) )
        ( met_px,         met_py         ) = ( rawmet.pt*math.cos(rawmet.phi), rawmet.pt*math.sin(rawmet.phi) )
        ( met_px_nom,     met_py_nom     ) = ( met_px, met_py )
        ( met_px_jerUp,   met_py_jerUp   ) = ( met_px, met_py )
        ( met_px_jerDown, met_py_jerDown ) = ( met_px, met_py )
        ( met_px_jesUp,   met_py_jesUp   ) = ( {}, {} )
        ( met_px_jesDown, met_py_jesDown ) = ( {}, {} )

        if self.is_mc: ## genJet info is necessary for JER
            gen_jets = Collection(event, "GenJet")
            gen_jets_pt = np.array([gen_jet.pt for gen_jet in gen_jets])
            gen_jets_eta = np.array([gen_jet.eta for gen_jet in gen_jets])
            gen_jets_phi = np.array([gen_jet.phi for gen_jet in gen_jets])

            for label in self.evaluator_JES.keys():
                met_px_jesUp[label]   = met_px
                met_py_jesUp[label]   = met_py
                met_px_jesDown[label] = met_px
                met_py_jesDown[label] = met_py

        defaultpt = []
        pt_corr = []
        pt_uncorr = []
        mass_corr = []
        mass_uncorr = []
        pt_smear_up = []
        pt_smear_dn = []
        mass_smear_up = []
        mass_smear_dn = []
        pt_scale_up = []
        pt_scale_dn = []
        mass_scale_up = []
        mass_scale_dn = []

        # For Regrouped 11-source JES, create lists of dicts
        if isinstance(self.scaleKey, list):
            pt_scale_up_list = []
            pt_scale_dn_list = []
            mass_scale_up_list = []
            mass_scale_dn_list = []

        for iJet, jet in enumerate(itertools.chain(jets, lowPtJets)):
            #### JEC ####
            ## To be applied to both data and MC
            ## Jet in NanoAOD are already corrected
            ## The correction should be removed and the latest one available should be applied
            if iJet < len(jets):
                pt_raw = jet.pt * (1 - jet.rawFactor)
                mass_raw = jet.mass * (1 - jet.rawFactor)
                defaultpt.append(jet.pt)
            else:
                pt_raw = jet.rawPt
                mass_raw = jet.rawMass
                jet.neEmEF = 0.0
                jet.chEmEF = 0.0

            if debug:
                print(f"Jet {iJet}: raw pt {pt_raw}, raw mass {mass_raw}, muonSubtrFactor {jet.muonSubtrFactor}, new jet pt {pt_raw*(1-jet.muonSubtrFactor)}")
            newjet_pt = pt_raw*(1-jet.muonSubtrFactor)

            ## The three steps of JEC corrections are provided separately
            pt_L1 = pt_raw * self.evaluator_L1.evaluate(jet.area, jet.eta, pt_raw, event.Rho_fixedGridRhoFastjetAll)
            newjet_pt_L1 = newjet_pt * self.evaluator_L1.evaluate(jet.area, jet.eta, newjet_pt, event.Rho_fixedGridRhoFastjetAll)
            jecL1 = pt_L1 / pt_raw

            if self.usePhiDependentJEC:
                pt_L2 = pt_L1 * self.evaluator_L2.evaluate(jet.eta, jet.phi, pt_L1)
                newjet_pt_L2 = newjet_pt_L1 * self.evaluator_L2.evaluate(jet.eta, jet.phi, newjet_pt_L1)
            else:
                pt_L2 = pt_L1 * self.evaluator_L2.evaluate(jet.eta, pt_L1)
                newjet_pt_L2 = newjet_pt_L1 * self.evaluator_L2.evaluate(jet.eta, newjet_pt_L1)

            pt_L3 = pt_L2 * self.evaluator_L3.evaluate(jet.eta, pt_L2)
            newjet_pt_L3 = newjet_pt_L2 * self.evaluator_L3.evaluate(jet.eta, newjet_pt_L2)
            if self.useRunDependentJEC:
                pt_JEC = pt_L3 * self.evaluator_L2L3.evaluate(float(event.run), jet.eta, pt_L3)
                newjet_pt_JEC = newjet_pt_L3 * self.evaluator_L2L3.evaluate(float(event.run), jet.eta, newjet_pt_L3)
            else:
                pt_JEC = pt_L3 * self.evaluator_L2L3.evaluate(jet.eta, pt_L3)
                newjet_pt_JEC = newjet_pt_L3 * self.evaluator_L2L3.evaluate(jet.eta, newjet_pt_L3)

            JEC = pt_JEC / pt_raw
            mass_JEC = mass_raw * JEC
            if iJet >= len(jets):
                pt_JEC = newjet_pt_JEC
                jet.pt = pt_JEC  # update jet pt for lowPtJets

            if self.is_mc:
                #### JER ####
                ## Hybrid method is implemented [https://cms-jerc.web.cern.ch/JER/#smearing-procedures]
                ## except in the eta region 2.5 < |eta| < 3.0 where the Scaling method is implemented
                ## Scaling method was introduced following JME recommendations to handle the 'Horns issue'
                ## Ref: https://gitlab.cern.ch/cms-jetmet/coordination/coordination/-/issues/113
                ## TODO: This should be removed once a JSON-level fix is implemented.

                JER = self.evaluator_JER.evaluate(jet.eta, pt_JEC, event.Rho_fixedGridRhoFastjetAll)
                METJER = self.evaluator_JER.evaluate(jet.eta, newjet_pt_JEC, event.Rho_fixedGridRhoFastjetAll)
                ## GenMatching with genJet
                delta_eta = jet.eta - gen_jets_eta
                fixPhi = np.vectorize(self.fixPhi, otypes=[float])
                delta_phi = fixPhi(jet.phi - gen_jets_phi)
                pt_gen = np.where((np.abs(pt_JEC - gen_jets_pt) < 3 * pt_JEC * JER) & (np.sqrt(delta_eta**2 + delta_phi**2)<0.2), gen_jets_pt, -1.0)
                METpt_gen = np.where((np.abs(newjet_pt_JEC - gen_jets_pt) < 3 * newjet_pt_JEC * METJER) & (np.sqrt(delta_eta**2 + delta_phi**2)<0.2), gen_jets_pt, -1.0)
                pt_gen = pt_gen[pt_gen > 0][0] if np.any(pt_gen > 0) else -1. ## If no gen-matching, simply -1
                METpt_gen = METpt_gen[METpt_gen > 0][0] if np.any(METpt_gen > 0) else -1. ## If no gen-matching, simply -1

                JERsf = self.evaluator_JERsf.evaluate(jet.eta, pt_JEC, "nom")
                JERsf_up = self.evaluator_JERsf.evaluate(jet.eta, pt_JEC, "up")
                JERsf_dn = self.evaluator_JERsf.evaluate(jet.eta, pt_JEC, "down")
                METJERsf = self.evaluator_JERsf.evaluate(jet.eta, newjet_pt_JEC, "nom")
                METJERsf_up = self.evaluator_JERsf.evaluate(jet.eta, newjet_pt_JEC, "up")
                METJERsf_dn = self.evaluator_JERsf.evaluate(jet.eta, newjet_pt_JEC, "down")
                # FIXME: prevent error where event is outside the int32 range. cf: github.com/cms-nanoAOD/correctionlib/issues/298
                JERsmear = self.evaluator_JERsmear.evaluate(pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), JER, JERsf)
                JERsmear_up = self.evaluator_JERsmear.evaluate(pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), JER, JERsf_up)
                JERsmear_dn = self.evaluator_JERsmear.evaluate(pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), JER, JERsf_dn)
                METJERsmear = self.evaluator_JERsmear.evaluate(newjet_pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), METJER, METJERsf)
                METJERsmear_up = self.evaluator_JERsmear.evaluate(newjet_pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), METJER, METJERsf_up)
                METJERsmear_dn = self.evaluator_JERsmear.evaluate(newjet_pt_JEC, jet.eta, pt_gen, event.Rho_fixedGridRhoFastjetAll, int(event.event&0x7FFFFFFF), METJER, METJERsf_dn)

                #JES
                if isinstance(self.scaleKey, list):  # Regrouped 11-source JES
                    JES_up = {}
                    JES_dn = {}
                    METJES_up = {}
                    METJES_dn = {}
                    JES_up_mass = {}
                    JES_dn_mass = {}
                    for label, evaluator in self.evaluator_JES.items():
                        u = evaluator.evaluate(jet.eta, pt_JEC)
                        METu = evaluator.evaluate(jet.eta, newjet_pt_JEC)
                        JES_up[label] = pt_JEC * (1 + u)
                        JES_dn[label] = pt_JEC * (1 - u)
                        METJES_up[label] = newjet_pt_JEC * (1 + METu)
                        METJES_dn[label] = newjet_pt_JEC * (1 - METu)
                        JES_up_mass[label] = mass_JEC * (1 + u)
                        JES_dn_mass[label] = mass_JEC * (1 - u)
                    if iJet < len(jets):
                        pt_scale_up_list.append(JES_up)
                        pt_scale_dn_list.append(JES_dn)
                        mass_scale_up_list.append(JES_up_mass)
                        mass_scale_dn_list.append(JES_dn_mass)
                else:  # single total JES
                    u = self.evaluator_JES.evaluate(jet.eta, pt_JEC)
                    pt_JES_up = pt_JEC * (1 + u)
                    pt_JES_dn = pt_JEC * (1 - u)
                    METpt_JES_up = newjet_pt_JEC * (1 + u)
                    METpt_JES_dn = newjet_pt_JEC * (1 - u)
                    mass_JES_up = mass_JEC * (1 + u)
                    mass_JES_dn = mass_JEC * (1 - u)

                if pt_gen < 0 and (2.5 < abs(jet.eta) < 3):
                    JERsmear_nominal = 1.0
                    JERsmear_up = JERsmear_up / JERsmear
                    JERsmear_dn = JERsmear_dn / JERsmear
                else:
                    JERsmear_nominal = JERsmear

                METJERsmear_nominal = METJERsmear
                METJERsmear_up = METJERsmear_up / METJERsmear
                METJERsmear_dn = METJERsmear_dn / METJERsmear

                pt_JEC_JER = pt_JEC * JERsmear_nominal
                pt_JEC_JER_up = pt_JEC * JERsmear_up
                pt_JEC_JER_dn = pt_JEC * JERsmear_dn
                METpt_JEC_JER = newjet_pt_JEC * METJERsmear_nominal
                METpt_JEC_JER_up = newjet_pt_JEC * METJERsmear_up
                METpt_JEC_JER_dn = newjet_pt_JEC * METJERsmear_dn
                mass_JEC_JER = mass_JEC * JERsmear_nominal
                mass_JEC_JER_up = mass_JEC * JERsmear_up
                mass_JEC_JER_dn = mass_JEC * JERsmear_dn
                
                if debug:
                    print(f"Jet {iJet}: pt_L1 {pt_L1}, pt_L2 {pt_L2}, pt_L3 {pt_L3}, pt_JEC {pt_JEC}, pt_JES_JER {pt_JEC_JER}, JER sf {JERsf} " )
                    print(f"Jet {iJet}: newjet_pt_L1 {newjet_pt_L1}, newjet_pt_L2 {newjet_pt_L2}, newjet_pt_L3 {newjet_pt_L3}, newjet_pt_JEC {newjet_pt_JEC}, newjet_pt_JES_JER {METpt_JEC_JER}, JER sf {METJERsf} " )

                if iJet < len(jets):
                    pt_corr.append(pt_JEC_JER)
                    pt_uncorr.append(pt_raw)
                    mass_corr.append(mass_JEC_JER)
                    mass_uncorr.append(mass_raw)
                    pt_smear_up.append(pt_JEC_JER_up)
                    pt_smear_dn.append(pt_JEC_JER_dn)
                    mass_smear_up.append(mass_JEC_JER_up)
                    mass_smear_dn.append(mass_JEC_JER_dn)

                    if not isinstance(self.scaleKey, list):
                        pt_scale_up.append(pt_JES_up)
                        pt_scale_dn.append(pt_JES_dn)
                        mass_scale_up.append(mass_JES_up)
                        mass_scale_dn.append(mass_JES_dn)
            else:
                ## Data
                ## No JER for Data
                if iJet < len(jets):
                    pt_corr.append(pt_JEC)
                    pt_uncorr.append(pt_raw)
                    mass_corr.append(mass_JEC)
                    mass_uncorr.append(mass_raw)

            # progate JER and JES corrections and uncertainties to MET. Only propagate JECs to MET if the corrected pt without the muon is above the threshold
            # Type-1 recompute (pT>15, |eta|<5.2, EM frac < 0.9)
            if debug:
               print(f"Jes variation dictionary {JES_up}")
            if METpt_JEC_JER > 15 and abs(jet.eta)<5.2 and (jet.neEmEF+jet.chEmEF) < 0.9:
                    jet_cosPhi = math.cos(jet.phi)
                    jet_sinPhi = math.sin(jet.phi)
                    met_px_nom    -= (METpt_JEC_JER  - newjet_pt_L1)*jet_cosPhi
                    met_py_nom    -= (METpt_JEC_JER  - newjet_pt_L1)*jet_sinPhi
                    if debug:
                        print(f"dpt for MET from jet {iJet}: {METpt_JEC_JER  - newjet_pt_L1}, new MET px: {met_px_nom}, py: {met_py_nom}")
                    if self.is_mc:
                      met_px_jerUp   -= (METpt_JEC_JER_up - newjet_pt_L1)*jet_cosPhi
                      met_py_jerUp   -= (METpt_JEC_JER_up - newjet_pt_L1)*jet_sinPhi
                      met_px_jerDown -= (METpt_JEC_JER_dn - newjet_pt_L1)*jet_cosPhi
                      met_py_jerDown -= (METpt_JEC_JER_dn - newjet_pt_L1)*jet_sinPhi
                      for label in self.evaluator_JES.keys():
                          met_px_jesUp[label]   -= (METJES_up[label] - newjet_pt_L1)*jet_cosPhi
                          met_py_jesUp[label]   -= (METJES_up[label] - newjet_pt_L1)*jet_sinPhi
                          met_px_jesDown[label] -= (METJES_dn[label] - newjet_pt_L1)*jet_cosPhi
                          met_py_jesDown[label] -= (METJES_dn[label] - newjet_pt_L1)*jet_sinPhi
        if self.is_mc:
          ( met_px_unclEnUp,   met_py_unclEnUp   ) = ( met_px_nom, met_py_nom )
          ( met_px_unclEnDown, met_py_unclEnDown ) = ( met_px_nom, met_py_nom )
          met_px_unclEnUp    += met.ptUnclusteredUp * math.cos(met.phiUnclusteredUp)
          met_py_unclEnUp    += met.ptUnclusteredUp * math.sin(met.phiUnclusteredUp)
          met_px_unclEnDown  -= met.ptUnclusteredDown * math.cos(met.phiUnclusteredDown)
          met_py_unclEnDown  -= met.ptUnclusteredDown * math.sin(met.phiUnclusteredDown)

        if self.overwritePt :
            self.out.fillBranch("PuppiMET_pt", math.sqrt(met_px_nom**2 + met_py_nom**2))
            self.out.fillBranch("PuppiMET_phi", math.atan2(met_py_nom, met_px_nom))
            self.out.fillBranch("Jet_uncorrected_pt", pt_uncorr)
            self.out.fillBranch("Jet_pt", pt_corr)
            self.out.fillBranch("Jet_uncorrected_mass", mass_uncorr)
            self.out.fillBranch("Jet_mass", mass_corr)
            self.out.fillBranch("Jet_defaultpt", defaultpt)
        else :
            self.out.fillBranch("Jet_corrected_pt", pt_corr)
            self.out.fillBranch("Jet_corrected_mass", mass_corr)
            self.out.fillBranch("PuppiMET_corrected_pt", math.sqrt(met_px_nom**2 + met_py_nom**2))
            self.out.fillBranch("PuppiMET_corrected_phi", math.atan2(met_py_nom, met_px_nom))

        if self.is_mc:
            self.out.fillBranch("Jet_smearUp_pt", pt_smear_up)
            self.out.fillBranch("Jet_smearDn_pt", pt_smear_dn)
            self.out.fillBranch("Jet_smearUp_mass", mass_smear_up)
            self.out.fillBranch("Jet_smearDn_mass", mass_smear_dn)
            self.out.fillBranch("PuppiMET_pt_UnclEnUp", math.sqrt(met_px_unclEnUp**2 + met_py_unclEnUp**2))
            self.out.fillBranch("PuppiMET_phi_UnclEnUp", math.atan2(met_py_unclEnUp, met_px_unclEnUp))
            self.out.fillBranch("PuppiMET_pt_UnclEnDown", math.sqrt(met_px_unclEnDown**2 + met_py_unclEnDown**2))
            self.out.fillBranch("PuppiMET_phi_UnclEnDown", math.atan2(met_py_unclEnDown, met_px_unclEnDown))
            self.out.fillBranch("PuppiMET_pt_jerUp", math.sqrt(met_px_jerUp**2 + met_py_jerUp**2))
            self.out.fillBranch("PuppiMET_phi_jerUp", math.atan2(met_py_jerUp, met_px_jerUp))
            self.out.fillBranch("PuppiMET_pt_jerDown", math.sqrt(met_px_jerDown**2 + met_py_jerDown**2))
            self.out.fillBranch("PuppiMET_phi_jerDown", math.atan2(met_py_jerDown, met_px_jerDown))
            # Fill JES branches
            if isinstance(self.scaleKey, list):  # Regrouped 11-source JES
                for label in self.evaluator_JES.keys():
                    self.out.fillBranch(f"Jet_{label}_ScaleUp_pt", [JES_up[label] for JES_up in pt_scale_up_list])
                    self.out.fillBranch(f"Jet_{label}_ScaleDn_pt", [JES_dn[label] for JES_dn in pt_scale_dn_list])
                    self.out.fillBranch(f"Jet_{label}_ScaleUp_mass", [JES_up[label] for JES_up in mass_scale_up_list])
                    self.out.fillBranch(f"Jet_{label}_ScaleDn_mass", [JES_dn[label] for JES_dn in mass_scale_dn_list])
                    self.out.fillBranch(f"PuppiMET_{label}_ScaleUp_pt", math.sqrt(met_px_jesUp[label]**2 + met_py_jesUp[label]**2))
                    self.out.fillBranch(f"PuppiMET_{label}_ScaleUp_phi", math.atan2(met_py_jesUp[label], met_px_jesUp[label]))
                    self.out.fillBranch(f"PuppiMET_{label}_ScaleDown_pt", math.sqrt(met_px_jesDown[label]**2 + met_py_jesDown[label]**2))
                    self.out.fillBranch(f"PuppiMET_{label}_ScaleDown_phi", math.atan2(met_py_jesDown[label], met_px_jesDown[label]))
            else:  # single total JES
                self.out.fillBranch("Jet_scaleUp_pt", pt_scale_up)
                self.out.fillBranch("Jet_scaleDn_pt", pt_scale_dn)
                self.out.fillBranch("Jet_scaleUp_mass", mass_scale_up)
                self.out.fillBranch("Jet_scaleDn_mass", mass_scale_dn)
                self.out.fillBranch("PuppiMET_ScaleUp_pt", math.sqrt(met_px_jesUp**2 + met_py_jesUp**2))
                self.out.fillBranch("PuppiMET_ScaleUp_phi", math.atan2(met_py_jesUp, met_px_jesUp))
                self.out.fillBranch("PuppiMET_ScaleDown_pt", math.sqrt(met_px_jesDown**2 + met_py_jesDown**2))
                self.out.fillBranch("PuppiMET_ScaleDown_phi", math.atan2(met_py_jesDown, met_px_jesDown))

        return True
