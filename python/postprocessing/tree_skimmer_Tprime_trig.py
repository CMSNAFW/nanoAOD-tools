#d!/Bin/env python
import os
import sys
import ROOT
import math
import datetime
import copy
from array import array
from skimtree_utils import *
from tools import *
import xgboost as xgb
import numpy as np
from training_MultiClass import *
from samples.samples import *

if sys.argv[5] == None: training = training_dict["BDT_Tprime"]
else: training = training_dict[sys.argv[5]]

sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))

startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

outTreeFile = ROOT.TFile(str(sys.argv[4])+"/"+sample.label+"_part"+str(part_idx)+".root", "RECREATE")
chain = ROOT.TChain('Events')

for infile in file_list: 
    #print("Adding %s to the chain" %(infile))
    chain.Add(infile)
print("Number of events in chain " + str(chain.GetEntries()))
print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
tree = InputTree(chain)
isMC = True

if ('Data' in sample.label):
    isMC = False
scenarios = ["all"]


#++++++++++++++++++++++++++++++++++
#++   branching the new trees    ++
#++++++++++++++++++++++++++++++++++

trees = []
for i in range(10):
    trees.append(None)
#systZero = systWeights()
# defining the operations to be done with the systWeights class
maxSysts = 0
addPDF = False
addQ2 = False
addTopPt = False
addVHF = False
addTTSplit = False
addTopTagging = False
addWTagging = False
addTrigSF = False
nPDF = 0

systTree = systWeights()
systTree.prepareDefault(True, addQ2, addPDF, addTopPt, addVHF, addTTSplit)

for scenario in scenarios:
    systTree.addSelection(scenario)

systTree.initTreesSysts(trees, outTreeFile)

systTree.setWeightName("w_nominal",1.)
systTree.setWeightName("w_pt",1.)
systTree.setWeightName("w_Dcount",1.)
systTree.setWeightName("LHESF", 1.)
systTree.setWeightName("LHEUp", 1.)
systTree.setWeightName("LHEDown", 1.)
systTree.setWeightName("puSF",1.)
systTree.setWeightName("puUp",1.)
systTree.setWeightName("puDown",1.)
systTree.setWeightName("lepSF",1.)
systTree.setWeightName("lepUp",1.)
systTree.setWeightName("lepDown",1.)
systTree.setWeightName("trigSF",1.)
systTree.setWeightName("trigUp",1.)
systTree.setWeightName("trigDown",1.)
systTree.setWeightName("PFSF",1.)
systTree.setWeightName("PFUp",1.)
systTree.setWeightName("PFDown",1.)
systTree.setWeightName("btagSF",1.)
systTree.setWeightName("btagUp",1.)
systTree.setWeightName("btagDown",1.)
systTree.setWeightName("mistagUp",1.)
systTree.setWeightName("mistagDown",1.)
systTree.setWeightName("pdf_totalUp", 1.)
systTree.setWeightName("pdf_totalDown", 1.)
systTree.setWeightName("ParNetSF", 1.)
systTree.setWeightName("ParNetUp", 1.)
systTree.setWeightName("ParNetDown", 1.)
systTree.setWeightName("BDTSF", 1.)
systTree.setWeightName("BDTUp", 1.)
systTree.setWeightName("BDTDown", 1.)

def reco(scenario, isMC, addPDF, training):
    isNominal = False
    if scenario == 'nominal':
        isNominal = True
    print(scenario)
    BDTSF_nominal = array.array('f',[1.])
    BDTUp_nominal = array.array('f',[1.])
    BDTDown_nominal = array.array('f',[1.])

    ParNetSF_nominal = array.array('f',[1.])
    ParNetUp_nominal = array.array('f',[1.])
    ParNetDown_nominal = array.array('f',[1.])



    w_PDF_nominal = array.array('f',[0.])
    w_pt_nominal = array.array('f',[1.])
    w_nominal_nominal = array.array('f', [1.])
    w_Dcount_nominal = array.array('f',[1.])

    isdileptonic = array.array('i', [0])
    isPromptEle = array.array('i', [0])
    muon_pt = array.array('f', [0.])
    muon_eta = array.array('f', [0.])
    muon_phi = array.array('f', [0.])
    muon_m = array.array('f', [0.])
    muon_SF = array.array('f', [0.])
    electron_pt = array.array('f', [0.])
    electron_eta = array.array('f', [0.])
    electron_phi = array.array('f', [0.])
    electron_m = array.array('f', [0.])
    electron_SF = array.array('f', [0.])
    top_region_nominal = array.array('i',[0])
    HLT_Muon_nominal = array.array('f',[0.])
    HLT_Electron_nominal = array.array('f',[0.])
    HLT_Photon_nominal = array.array('f',[0.])
    HLT_PFJet_nominal = array.array('f',[0.])

    AK8_region_nominal = array.array('i',[0])
    FatJet_pt_nominal = array.array('f',[0.])
    FatJet_eta_nominal = array.array('f',[0.])
    FatJet_msd_nominal = array.array('f',[0.])
    

    systTree.branchTreesSysts(trees, "all", "isdileptonic", outTreeFile, isdileptonic)
    systTree.branchTreesSysts(trees, "all", "isPromptEle", outTreeFile, isPromptEle)
    systTree.branchTreesSysts(trees, "all", "muon_pt", outTreeFile, muon_pt)
    systTree.branchTreesSysts(trees, "all", "muon_eta", outTreeFile, muon_eta)
    systTree.branchTreesSysts(trees, "all", "muon_phi", outTreeFile, muon_phi)
    systTree.branchTreesSysts(trees, "all", "muon_m", outTreeFile, muon_m)
    systTree.branchTreesSysts(trees, "all", "muon_SF", outTreeFile, muon_SF)
    systTree.branchTreesSysts(trees, "all", "electron_pt", outTreeFile, electron_pt)
    systTree.branchTreesSysts(trees, "all", "electron_eta", outTreeFile, electron_eta)
    systTree.branchTreesSysts(trees, "all", "electron_phi", outTreeFile, electron_phi)
    systTree.branchTreesSysts(trees, "all", "electron_m", outTreeFile, electron_m)
    systTree.branchTreesSysts(trees, "all", "electron_SF", outTreeFile, electron_SF)
    systTree.branchTreesSysts(trees, "all","top_region_nominal", outTreeFile, top_region_nominal)

    systTree.branchTreesSysts(trees, "all","AK8_region_nominal", outTreeFile, AK8_region_nominal)
    systTree.branchTreesSysts(trees, "all","HLT_Muon_nominal", outTreeFile, HLT_Muon_nominal)
    systTree.branchTreesSysts(trees, "all","HLT_Electron_nominal", outTreeFile, HLT_Electron_nominal)
    systTree.branchTreesSysts(trees, "all","HLT_Photon_nominal", outTreeFile, HLT_Photon_nominal)
    systTree.branchTreesSysts(trees, "all","HLT_PFJet_nominal", outTreeFile, HLT_PFJet_nominal)
    systTree.branchTreesSysts(trees, "all","FatJet_pt_nominal", outTreeFile, FatJet_pt_nominal)
    systTree.branchTreesSysts(trees, "all","FatJet_eta_nominal", outTreeFile, FatJet_eta_nominal)
    systTree.branchTreesSysts(trees, "all","FatJet_msd_nominal", outTreeFile, FatJet_msd_nominal)

    #print("!!!!!!! Change msoftdrop con msd_nom e pt con pt_nom per i FatJet !!!!!!!")

    #print("fix w_Dcount!!!!!!!!!!!!")
    print("isMC: ", isMC)
    pdf_xsweight = 1.
    pdf_weight_sum = 0.
    
    if(isMC):
        h_genweight = ROOT.TH1F()
        h_genweight.SetNameTitle('h_genweight', 'h_genweight')
        h_PDFweight = ROOT.TH1F()
        h_PDFweight.SetNameTitle("h_PDFweight","h_PDFweight")
        for infile in file_list:
            newfile = ROOT.TFile.Open(infile)
            dirc = ROOT.TDirectory()
            dirc = newfile.Get("plots")
            h_genw_tmp = ROOT.TH1F(dirc.Get("h_genweight"))
            if(dirc.GetListOfKeys().Contains("h_PDFweight")):
                h_pdfw_tmp = ROOT.TH1F(dirc.Get("h_PDFweight"))
                if(ROOT.TH1F(h_PDFweight).Integral() < 1.):
                    for i in range(1, h_pdfw_tmp.GetXaxis().GetNbins()+1):
                        pdf_weight_sum += h_pdfw_tmp.GetBinContent(i)
                    pdf_weight_sum /= h_pdfw_tmp.GetXaxis().GetNbins()
                    print(pdf_weight_sum)
                    h_PDFweight.SetBins(h_pdfw_tmp.GetXaxis().GetNbins(), h_pdfw_tmp.GetXaxis().GetXmin(), h_pdfw_tmp.GetXaxis().GetXmax())
                    print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(ROOT.TH1F(dirc.Get("h_genweight")).GetBinContent(1), ROOT.TH1F(dirc.Get("h_PDFweight")).GetNbinsX()))
                h_PDFweight.Add(h_pdfw_tmp)
            else:
                addPDF = False
            if(ROOT.TH1F(h_genweight).Integral() < 1.):
                h_genweight.SetBins(h_genw_tmp.GetXaxis().GetNbins(), h_genw_tmp.GetXaxis().GetXmin(), h_genw_tmp.GetXaxis().GetXmax())
            h_genweight.Add(h_genw_tmp)
        print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genweight.GetBinContent(1), h_PDFweight.GetNbinsX()))
        lheweight = h_genweight.GetBinContent(2)/h_genweight.GetBinContent(1)
        pdf_xsweight = pdf_weight_sum/h_genweight.GetBinContent(1)


    ################################################################################################################################################################################################################################
    #++++++++++++++++++++++++++++++++++
    #++      Efficiency studies      ++
    #++++++++++++++++++++++++++++++++++
    nbinseff = 10
    h_eff_mu = ROOT.TH1D("h_eff_mu", "h_eff_mu", nbinseff, 0, nbinseff)
    h_eff_ele = ROOT.TH1D("h_eff_ele", "h_eff_ele", nbinseff, 0, nbinseff)
    
    for i in range(tree.GetEntries()):        
        top_region_nominal[0]=0        
        isdileptonic[0]=0
        muon_pt[0]=0
        muon_eta[0]=0
        muon_phi[0]=0
        muon_m[0]=0
        muon_SF[0]=0
        electron_pt[0]=0
        electron_eta[0]=0
        electron_phi[0]=0
        electron_m[0]=0
        electron_SF[0]=0
        top_region_nominal[0]=0
        HLT_Muon_nominal[0] = 0.
        HLT_Electron_nominal[0] = 0.
        HLT_Photon_nominal[0] = 0.
        HLT_PFJet_nominal[0] = 0.
        AK8_region_nominal[0] = 0
        FatJet_pt_nominal[0] = 0.
        FatJet_eta_nominal[0] = 0.
        FatJet_msd_nominal[0] = 0.
        isPromptEle[0]=False
        
        w_Dcount_nominal[0]=1.
        event = Event(tree,i) 
        if(i%1000==1): print(i)
        if ("TT" in sample.label): 
            genpart = Collection(event,"GenPart")
            top = list(filter(lambda x: x.pdgId==6 ,genpart))[0]
            antitop = list(filter(lambda x: x.pdgId==-6 ,genpart))[0]
            Mtt = (top.p4() + antitop.p4()).M()
            SF_t = 0.973-0.000134*top.pt+0.103*math.exp(-0.0118*top.pt)
            SF_antit = 0.973-0.000134*antitop.pt+0.103*math.exp(-0.0118*antitop.pt)
            w_pt_nominal[0]=math.sqrt(SF_t*SF_antit)
            if (Mtt>=700) and (not "Mtt" in sample.label):
                w_Dcount_nominal[0]=0.
                #print(Mtt)
                #continue
        
        jets = Collection(event, "Jet")            
        tops = Collection(event,"Top")
        met = Object(event, "MET")
        electron = Collection(event, "Electron")
        muon = Collection(event, "Muon")
        nelectron = len(electron)
        nmuon = len(muon)
        ntop = len(tops)
        fatjets = Collection(event,"FatJet")
        HLT = Object(event,"HLT")

        allmuons = list(filter(lambda x: x.pt>=-999,muon))
        allelectrons = list(filter(lambda x: x.pt>=-999,electron))
        #IsoLooseMuon = Collection(event,"IsoLooseMuon")
        #IsoLooseElectron = Collection(event,"IsoLooseElectron")

        #LooseMuon = Collection(event,"LooseMuon")
        #LooseElectron = Collection(event,"LooseElectron")
        
        #TightMuon = Collection(event,"TightMuon")
        #TightElectron = Collection(event,"TightElectron")

        
        if sample.year== 2016: 
            HLT_Muon_nominal[0] = HLT.Mu50 or HLT.IsoMu24
            HLT_PFJet_nominal[0] = HLT.AK8PFJet360_TrimMass30
            HLT_Electron_nominal[0] = HLT.Ele27_WPTight_Gsf
            HLT_Photon_nominal[0] = HLT.Photon175
        if sample.year== 2017:
            HLT_Muon_nominal[0] = HLT.Mu50 or HLT.IsoMu27
            HLT_PFJet_nominal[0] = HLT.AK8PFJet500
            HLT_Electron_nominal[0] = HLT.Ele35_WPTight_Gsf
            HLT_Photon_nominal[0] = HLT.Photon200
        if sample.year== 2018:
            HLT_Muon_nominal[0] = HLT.Mu50 or HLT.IsoMu27
            HLT_PFJet_nominal[0] = HLT.AK8PFJet400_TrimMass30
            HLT_Electron_nominal[0] = HLT.Ele32_WPTight_Gsf
            HLT_Photon_nominal[0] = HLT.Photon200

        

        if(isMC):
            doublecounting = False
        else:
            doublecounting = True
        #Double counting removal
        if('DataMu' in sample.label and HLT_Muon_nominal[0]):
            doublecounting = False
        if('DataEle'  in sample.label and (not HLT_Muon_nominal[0] and HLT_Electron_nominal[0] )):
            doublecounting = False

        if('DataPh'  in sample.label and (not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0] and HLT_Photon_nominal[0]) and sample.year!=2018):
            doublecounting = False

        if('DataEle'  in sample.label and (not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0] and HLT_Photon_nominal[0]) and sample.year==2018):
            doublecounting = False

        if('DataHT' in sample.label and (HLT_PFJet_nominal[0] and not HLT_Muon_nominal[0] and not HLT_Electron_nominal[0]  and not HLT_Photon_nominal[0])):
            doublecounting = False
                
        if doublecounting:
            continue



        chain.GetEntry(i) #this is needed for branches that are not compatible with the NANOAOD convention (e.g. )

        
        # this part take care of writing the variations of the MC weight relative to the LHE scale and the PDFs variations
        PU_SF=None
        PU_SFUp=None
        PU_SFDown=None
 

        if(isMC):
            runPeriod=None
        else:
            runPeriod=sample.runP

        passesMETHEMVeto = HEMveto(jets, electron)
        if(sample.year == 2018 and not passesMETHEMVeto):
            if(not isMC and chain.run > 319077.):
                continue
            elif(isMC):
                w_nominal_nominal[0] *= 0.354


        
        if(isMC):
            if not sample.year == 2018:
                PF_SF = chain.PrefireWeight
                PF_SFUp = chain.PrefireWeight_Up
                PF_SFDown = chain.PrefireWeight_Down
                systTree.setWeightName("PFSF", copy.deepcopy(PF_SF))
                systTree.setWeightName("PFUp", copy.deepcopy(PF_SFUp))
                systTree.setWeightName("PFDown", copy.deepcopy(PF_SFDown))

            PU_SF = chain.puWeight
            PU_SFUp = chain.puWeightUp
            PU_SFDown = chain.puWeightDown
            systTree.setWeightName("puSF", copy.deepcopy(PU_SF))
            systTree.setWeightName("puUp", copy.deepcopy(PU_SFUp))
            systTree.setWeightName("puDown", copy.deepcopy(PU_SFDown))
        


        tightMu = list(filter(lambda x : x.tightId and x.pt>30 and x.pfRelIso04_all<0.15 and abs(x.eta)<2.4,muon))
        tightEle = list(filter(lambda x : x.mvaFall17V2Iso_WP80 and x.pt>30 and abs(x.eta)<2.5, electron))

        
 
        all_coll=[]
        all_coll_wp90=[]
        all_coll_wp99=[]
        goodfatjets = []
    
        k=0
        for train in training:
            k=k+1
            new_coll=[]
            new_coll_wp90=[]
            new_coll_wp99=[]
            score=[]
            score_=-999
            if train.lepton == 1:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.pt_cut[0]) and (x.nu_pt<train.pt_cut[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.el_index != -1) and abs(electron[int(x.el_index)].eta)<2.5
                                                ,tops))
                is_el=True
            else:
                good_top = list(filter(lambda x: 
                                                (x.nu_pt>= train.pt_cut[0]) and (x.nu_pt<train.pt_cut[1])
                                                and (x.Is_dR_merg == train.category)
                                                and (x.mu_index != -1) and abs(muon[int(x.mu_index)].eta)<2.4
                                                ,tops))
                is_el=False


            for top in good_top:
                if top.TvsQCD>train.QCDcut:
                    new_coll.append(top)
                    if top.TvsOth>=train.Lcut: new_coll_wp90.append(top)
                    if top.TvsOth>=train.Tcut: new_coll_wp99.append(top)               
                
            if(len(new_coll)>0): 
                new_coll =  [x for _,x in sorted(zip([new_coll[i].TvsOth for i in range(len(new_coll))],new_coll))]
                new_coll.reverse()
    
                if(len(new_coll_wp90)>0):
                    new_coll_wp90 = [x for _,x in sorted(zip([new_coll_wp90[i].TvsOth for i in range(len(new_coll_wp90))],new_coll_wp90))] 
                    new_coll_wp90.reverse()
                    if(len(new_coll_wp99)>0):
                        new_coll_wp99 = [x for _,x in sorted(zip([new_coll_wp99[i].TvsOth for i in range(len(new_coll_wp99))],new_coll_wp99))] 
                        new_coll_wp99.reverse()
                

            all_coll = all_coll + new_coll
            all_coll_wp90 = all_coll_wp90 + new_coll_wp90
            all_coll_wp99 = all_coll_wp99 + new_coll_wp99
            
            


        if(len(all_coll)>0):
            lista= all_coll
        
            if(len(all_coll_wp99)): 
                top_region_nominal[0]=1
                lista = all_coll_wp99
            elif (len(all_coll_wp90)): 
                top_region_nominal[0]=0
                lista= all_coll_wp90

          
        
        if(len(all_coll_wp90)>0): 
            if lista[0].el_index!=-1:
                Lep_eta_nominal= electron[int(lista[0].el_index)].eta
                Lep_phi_nominal= electron[int(lista[0].el_index)].phi
                prompt_el = True
                electron_pt[0]= electron[int(lista[0].el_index)].pt
                electron_eta[0]= electron[int(lista[0].el_index)].eta
                electron_phi[0]= electron[int(lista[0].el_index)].phi
                electron_m[0]= electron[int(lista[0].el_index)].mass
                if(isMC): electron_SF[0]= electron[int(lista[0].el_index)].LooseeffSF
            else:
                Lep_eta_nominal= muon[int(lista[0].mu_index)].eta
                Lep_phi_nominal= muon[int(lista[0].mu_index)].phi
                prompt_el = False
                muon_pt[0]= muon[int(lista[0].mu_index)].pt
                muon_eta[0]= muon[int(lista[0].mu_index)].eta
                muon_phi[0]= muon[int(lista[0].mu_index)].phi
                muon_m[0]= muon[int(lista[0].mu_index)].mass
                if(isMC): muon_SF[0]= muon[int(lista[0].mu_index)].LooseeffSF
            
            goodfatjets = list(filter(lambda x: deltaR(x.eta,x.phi,lista[0].nu_eta,lista[0].nu_phi)>1.2 and 
                                                            deltaR(x.eta,x.phi,jets[int(lista[0].bjet_index)].eta,jets[int(lista[0].bjet_index)].phi)>1.2 and 
                                                            deltaR(x.eta,x.phi,Lep_eta_nominal,Lep_phi_nominal)>0.8 and 
                                                            (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or 
                                                             (x.msd_nom>=60 and x.msd_nom<=220)),fatjets))
        elif(len(tightEle)==1 and len(tightMu)==0):
            goodfatjets = list(filter(lambda x: (deltaR(x.eta,x.phi,tightEle[0].eta,tightEle[0].phi)>0.8) and 
                                      (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or 
                                       (x.msd_nom>=60 and x.msd_nom<=220)),fatjets))
            top_region_nominal[0]=-1
            prompt_el = True
            electron_pt[0]= tightEle[0].pt
            electron_eta[0]= tightEle[0].eta
            electron_phi[0]= tightEle[0].phi
            electron_m[0]= tightEle[0].mass
            if(isMC): electron_SF[0]=electron[int(allelectrons.index(tightEle[0]))].TighteffSF
        elif(len(tightEle)==0 and len(tightMu)==1):
            goodfatjets = list(filter(lambda x: (deltaR(x.eta,x.phi,tightMu[0].eta,tightMu[0].phi)>0.8)  and 
                                      (weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD)>=0.8 or 
                                       (x.msd_nom>=60 and x.msd_nom<=220)),fatjets))
            top_region_nominal[0]=-1
            prompt_el =False
            muon_pt[0]= tightMu[0].pt
            muon_eta[0]= tightMu[0].eta
            muon_phi[0]= tightMu[0].phi
            muon_m[0]= tightMu[0].mass
            if(isMC): muon_SF[0]= muon[int(allmuons.index(tightMu[0]))].TighteffSF
        elif(len(tightEle)>0 and len(tightMu)>0):
            goodfatjets = []
            continue

        if len(goodfatjets)==0: continue
        goodfatjets.sort(key=lambda x:weird_division(x.particleNetMD_Xbb,x.particleNetMD_Xbb+x.particleNetMD_QCD),reverse=True)
        if weird_division(goodfatjets[0].particleNetMD_Xbb,goodfatjets[0].particleNetMD_Xbb+goodfatjets[0].particleNetMD_QCD)<0.8: AK8_region_nominal[0]=0
        elif weird_division(goodfatjets[0].particleNetMD_Xbb,goodfatjets[0].particleNetMD_Xbb+goodfatjets[0].particleNetMD_QCD)>=0.98:AK8_region_nominal[0]=2
        else: AK8_region_nominal[0]=1
        
        FatJet_pt_nominal[0]= goodfatjets[0].pt_nom
        FatJet_msd_nominal[0]= goodfatjets[0].msd_nom
        FatJet_eta_nominal[0]= goodfatjets[0].eta
        

        if(len(all_coll_wp90)>0):
            AddMuon = list(filter(lambda x: allmuons.index(x)!=int(lista[0].mu_index) and x.looseId and x.pfRelIso04_all<0.25 and x.pt>30 and abs(x.eta)<2.4, muon))
            AddElectron = list(filter(lambda x: allelectrons.index(x)!=int(lista[0].el_index) and x.mvaFall17V2Iso_WP90==1 and x.pt>30 and abs(x.eta)<2.5, electron))

        else:
            if(len(tightMu)>0):
                AddMuon = list(filter(lambda x: allmuons.index(x)!=allmuons.index(tightMu[0]) and x.looseId and x.pfRelIso04_all<0.25 and x.pt>30 and abs(x.eta)<2.4, muon))
            else:
                AddMuon = list(filter(lambda x:  x.looseId and x.pfRelIso04_all<0.25 and x.pt>30 and abs(x.eta)<2.4, muon))

            if(len(tightEle)>0):
                AddElectron = list(filter(lambda x: allelectrons.index(x)!=allelectrons.index(tightEle[0]) and x.mvaFall17V2Iso_WP90==1 and x.pt>30 and abs(x.eta)<2.5, electron))
            else:
                AddElectron = list(filter(lambda x: x.mvaFall17V2Iso_WP90==1 and x.pt>30 and abs(x.eta)<2.5, electron))

        N_muLoose_nominal = len(AddMuon)
        N_elLoose_nominal = len(AddElectron)


        if (top_region_nominal[0]>=0):
            if (lista[0].TvsQCD<0.6): continue


            
        if( (prompt_el==True) and (N_elLoose_nominal==0) and (N_muLoose_nominal==1)):
            muon_pt[0]= AddMuon[0].pt
            muon_eta[0]= AddMuon[0].eta
            muon_phi[0]= AddMuon[0].phi
            muon_m[0]= AddMuon[0].mass
            if(isMC): muon_SF[0]= muon[int(allmuons.index(AddMuon[0]))].IsoLooseeffSF
            isdileptonic[0] = True 
        elif((prompt_el==False) and (N_muLoose_nominal==0) and (N_elLoose_nominal==1)):
            electron_pt[0]= AddElectron[0].pt
            electron_eta[0]= AddElectron[0].eta
            electron_phi[0]= AddElectron[0].phi
            electron_m[0]= AddElectron[0].mass
            if(isMC): electron_SF[0]= electron[int(allelectrons.index(AddElectron[0]))].IsoLooseeffSF
            isdileptonic[0] = True
        elif((N_elLoose_nominal==0) and (N_muLoose_nominal==0) and (top_region_nominal[0]==-1) and (AK8_region_nominal[0]==0)):
            isdileptonic[0] = False
        else: 
            continue

        #if top_region_nominal[0]>-1: print("!!!! Found It !!!!")
        isPromptEle[0]=prompt_el                            
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_nominal[0]))
        systTree.setWeightName("w_pt",copy.deepcopy(w_pt_nominal[0]))
        systTree.setWeightName("w_Dcount",copy.deepcopy(w_Dcount_nominal[0]))
        systTree.setWeightName("ParNetSF",copy.deepcopy(ParNetSF_nominal[0]))
        systTree.setWeightName("ParNetUp",copy.deepcopy(ParNetUp_nominal[0]))
        systTree.setWeightName("ParNetDown",copy.deepcopy(ParNetDown_nominal[0]))
        systTree.setWeightName("BDTSF",copy.deepcopy(BDTSF_nominal[0]))
        systTree.setWeightName("BDTUp",copy.deepcopy(BDTUp_nominal[0]))
        systTree.setWeightName("BDTDown",copy.deepcopy(BDTDown_nominal[0]))
        systTree.fillTreesSysts(trees, "all")
        

                    
    outTreeFile.cd()
    if scenario == 'all':
        trees[0].Write()
    
    if isMC:
        h_genweight.Write()
    systTree.writeTreesSysts(trees, outTreeFile)


for scenario in ["all"]:#scenarios:
    reco(scenario, isMC,addPDF, training)


endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
