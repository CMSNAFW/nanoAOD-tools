import ROOT
import os

base_var_top = ['electron_over_jet','nu_M','mT','pt_rel','Costheta','dR']
base_var_lep = ['dxy','dz','miniPFRelIso_all','pfRelIso03_all']
base_var_jet = ['mass','btagDeepFlavB']

class training:
	def __init__(self, label, files, var_top,var_lep,var_jet, category, lepton, cuts):
		self.label = label
		self.files = files
		self.var_top = var_top
		self.var_lep = var_lep
		self.var_jet = var_jet
		self.category = category # 1 is merged, 0 is resolved
		self.lepton = lepton # 0 is muon, 1 is electron
		self.cuts = cuts

high=[500,10000]
low=[0,500]

#variabili 1 training
var_top1=base_var_top[:2]+['nu_pt']+base_var_top[2:]
var_el1= ['dxy','dz','miniPFRelIso_all','pfRelIso03_all']
var_jet1=['mass','pt','btagDeepFlavB']

#variabili 2 training
var_top2= ['electron_over_jet','nu_M','nu_pt','M','pt','mT','pt_rel','Costheta','dR']
var_el2= ['pt','dxy','dxyerr','dz','dzerr','miniPFRelIso_all','pfRelIso03_all']
var_jet2=['mass','pt','btagDeepFlavB']


#variabili 3 training
var_top3=['electron_over_jet','nu_M','mT','pt_rel','dR']
var_el3= ['dxy','dz','miniPFRelIso_all','pfRelIso03_all']
var_jet3=['mass','btagDeepFlavB']

#variabili 4 training
var_top4=['nu_M','M','mT','pt_rel','dR']
var_el4= ['dxy','dz','miniPFRelIso_all','pfRelIso03_all']
var_jet4=['mass','pt','btagDeepFlavB']

BDT_Tprime_low_el_merg = training("BDT_Tprime_low_el_merg","low_pt_el_merged.json",var_top1,var_el1, var_jet1, 1, 1 , low)
BDT_Tprime_low_el_res = training("BDT_Tprime_low_el_res","low_pt_el_resolved.json",var_top2,var_el2, var_jet2, 0, 1 , low)
BDT_Tprime_high_el_merg = training("BDT_Tprime_high_el_merg","high_pt_el_merged.json",var_top3,var_el3, var_jet3, 1, 1 , high)
BDT_Tprime_high_el_res = training("BDT_Tprime_high_el_res","high_pt_el_resolved.json",var_top4,var_el4, var_jet4, 0, 1 , high)



training_dict = {"BDT_Tprime":[BDT_Tprime_low_el_merg,BDT_Tprime_low_el_res,BDT_Tprime_high_el_merg,BDT_Tprime_high_el_res]}


