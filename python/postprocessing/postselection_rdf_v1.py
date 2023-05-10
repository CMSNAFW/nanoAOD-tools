import ROOT
import os
ROOT.gInterpreter.Declare('#include "ROOT/RDataFrame.hxx"')
ROOT.gInterpreter.Declare('#include "ROOT/RVec.hxx"')
from samples.samples import *
from CMS_lumi import CMS_lumi
from variables import *
import copy
import optparse
import math
from tqdm import tqdm
import pickle as pkl
import numpy as np
from datetime import datetime

usage = 'python3 postselection_rdf.py'
parser = optparse.OptionParser(usage)
parser.add_option('-p', '--plots', dest='plots', default = False, action='store_true', help='Default make no histos')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default make no stacks')
parser.add_option('--samples', dest='samples', default = False, action='store_true', help='Default do not import files and Ntot')
parser.add_option('-C', '--cut', dest='cut', type='string', default = '', help='Default no cut')
parser.add_option('-r', '--recreate', dest='recreate', default = False, action='store_true', help='Default append histos')
parser.add_option('-m', '--mergesamples', dest='mergesamples', default = False, action='store_true', help='Default do not create a single file for bkg datasets')
parser.add_option('-d', '--dataset', dest='dataset', default = '', help='make histos of this dataset if present')
(opt, args) = parser.parse_args()

ROOT.gROOT.SetBatch()

nfiles_max = 5
lumi = 1#137#fb

folder = "/eos/home-a/acagnott/DarkMatter/nosynch/v2/"
if not os.path.exists(folder):
    os.mkdir(folder)
repohisto = folder+"plots/"
if not os.path.exists(repohisto):
    os.mkdir(repohisto)
repostack = folder+"stacks/"
if not os.path.exists(repostack):
    os.mkdir(repostack)


distributed = False
text_file = open("postselection.h", "r")
data = text_file.read()

def my_initialization_function():
    print(ROOT.gInterpreter.ProcessLine(".O"))
    ROOT.gInterpreter.Declare('{}'.format(data))
    #from urllib import request
    #print("creating TMVA object")
    #modelName = "optimized_model_SM_allBKGs_UL_vUL025_optimization_balancing_redoAN_reduced_simplified"
    #request.urlretrieve("https://vbs-pg-support.web.cern.ch/models/{}.hxx".format(modelName), "{}.hxx".format(modelName))
    #request.urlretrieve("https://vbs-pg-support.web.cern.ch/models/{}.dat".format(modelName), "{}.dat".format(modelName))
    #ROOT.gInterpreter.Declare('#include "' + modelName + '.hxx"')
    #ROOT.gInterpreter.Declare('auto sofie_functor = TMVA::Experimental::SofieFunctor<28,TMVA_SOFIE_'+modelName+'::Session>(0);')
    print("end of initialization")

# set up everything properly
if distributed == True:
    RDataFrame = ROOT.RDF.Experimental.Distributed.Dask.RDataFrame
    client = Client(address="tcp://127.0.0.1:"+str(sched_port))
    client.restart()
    client.register_worker_plugin(UploadFile("./proxy"))
    client.run(set_proxy)
    ROOT.RDF.Experimental.Distributed.initialize(my_initialization_function)
else:
    RDataFrame = ROOT.RDataFrame
    my_initialization_function()

################### utils ###################
def cut_string(cut):
    return cut.replace(" ", "").replace("&&","_").replace(">","_g_").replace(".","_").replace("==","_e_")

def get_files_string(d):
    folder_files = "../../crab/macros/files/"
    infile_string = open(folder_files+d.label+".txt")
    strings = infile_string.readlines()
    for s in strings: s.replace('\n', '')
    return strings

############### trigger selection #####################
def trigger_filter(df):
    #HLT_PFHT780 || HLT_PFHT890 || HLT_Mu50 || HLT_OldMu100 || HLT_TkMu100 || HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200 || HLT_Ele35_WPTight_Gsf
    #preso da MET_HLT_filter 
    df_trig = df.Filter("HLT_PFHT780 || HLT_PFHT890 || HLT_Mu50 || HLT_OldMu100 || HLT_TkMu100 || HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Photon200 || HLT_Ele35_WPTight_Gsf")
    return df_trig

############### top selection ########################

def select_top(df):
    df_goodtopMer = df.Define("GoodTopMer_idx", "select_TopMer(FatJet_deepTag_TvsQCD, FatJet_pt, FatJet_eta, FatJet_phi)") 
    # ritorna gli indici dei FatJet che superano la trs del Top Merged (no overlap)
    df_goodtopMix = df_goodtopMer.Define("GoodTopMix_idx", "select_TopMix(TopHighPt_score2, TopHighPt_pt, TopHighPt_eta, TopHighPt_phi)") 
    # ritorna gli indici dei FatJet che superano la trs del Top Merged (no overlap)
    df_goodtopRes = df_goodtopMix.Define("GoodTopRes_idx", "select_TopRes(TopLowPt_scoreDNN, TopLowPt_pt, TopLowPt_eta, TopLowPt_phi)") 
    # ritorna gli indici dei Fatche superano la trs del Top Merged (no overlap)
    df_topcategory = df_goodtopRes.Define("EventTopCategory", "select_TopCategory(GoodTopMer_idx, GoodTopMix_idx, GoodTopRes_idx)") 
    # return:  0- no top sel, 1- top merged, 2- top mix, 3- top resolved
    df_topselected = df_topcategory.Define("Top_idx", 
                                           "select_bestTop(EventTopCategory, GoodTopMer_idx, GoodTopMix_idx, GoodTopRes_idx, FatJet_deepTag_TvsQCD, TopHighPt_score2, TopLowPt_scoreDNN)") 
    # return best top idx wrt category --> the idx is referred to the list of candidates fixed by the EventTopCategory
    df_topvariables = df_topselected.Define("Top_pt", "select_TopVar(EventTopCategory, Top_idx, FatJet_pt, TopHighPt_pt, TopLowPt_pt)")\
                        .Define("Top_eta", "select_TopVar(EventTopCategory, Top_idx, FatJet_eta, TopHighPt_eta, TopLowPt_eta)")\
                        .Define("Top_phi", "select_TopVar(EventTopCategory, Top_idx, FatJet_phi, TopHighPt_phi, TopLowPt_phi)")\
                        .Define("Top_mass", "select_TopVar(EventTopCategory, Top_idx, FatJet_mass, TopHighPt_mass, TopLowPt_mass)")\
                        .Define("Top_score", "select_TopVar(EventTopCategory, Top_idx, FatJet_deepTag_TvsQCD, TopHighPt_score2, TopLowPt_scoreDNN)")
    
    return df_topvariables

############ histos ###########
    
def makehistos(samples, var, cut):
    print(samples.keys())
    ROOT.TH1.SetDefaultSumw2()
    h = {}
    for s in samples.keys():
        c_ = cut
        print("Booking histos for  ", s)
        if nfiles_max > len(samples[s]['strings']): nfiles = len(samples[s]['strings'])
        else: nfiles = nfiles_max
        print("# root files attached:", nfiles)
        df = ROOT.RDataFrame("Events", samples[s]['strings'][:nfiles])
        df_trigger=df#df_trigger = trigger_filter(df)
        df_seltop = select_top(df_trigger)
        df_mt = df_seltop.Define("Mt", "sqrt(2 * Top_pt * MET_pt * (1 - cos(Top_phi - MET_phi)))")
        
        s_cut = cut_string(cut)#cut.replace(" ", "").replace("&&","_").replace(">","g").replace(".","_").replace("==","e")
        print(s_cut)
        if 'leptonveto' in cut:
            df_lepveto = df_mt.Define("goodmuon", "Muon_pt>30 && Muon_eta<2.4 && Muon_looseId==1").Define("goodelectron", "Electron_pt>30 && Electron_mvaFall17V1Iso_WPL==1")
            df_lepveto = df_lepveto.Filter("ROOT::VecOps::Sum(goodelectron) == 0").Filter("ROOT::VecOps::Sum(goodmuon) == 0")
            
            if "&& leptonveto" in cut:
                c_ = c_.replace("&& leptonveto","")
            elif "leptonveto &&" in cut:
                c_ = c_.replace("leptonveto &&","")
        else: df_lepveto = df_mt
        print("requirements: "+c_)
        if cut=="": df_plot = df_lepveto#.Filter(c_)
        else: df_plot = df_lepveto.Filter(c_)
        
        h[s] = {}
        for v in var:
            h[s][v._name]= (df_plot.Histo1D((v._name+"_"+s_cut," ;"+v._title+"", v._nbins, v._xmin, v._xmax), v._name))#.GetValue())
            #h.Write()
        #ofile.Close()
        print("Done "+s+" !")
    #print(h)
    return h


####################  makehistos test with concurrent futures######################

def makehistos_p(arg):
    makehistos(arg[0],arg[1],arg[2])

####################  merge samples of the same precess ######################

def mergSamples(dataset, var, cut):
    c_ = cut_string(cut)#cut.replace(" ", "").replace("&&","_").replace(">","g")replace("==","e")
    
    var_name = var._name+"_"+c_#'mt_'+cut  #'BestTop_pt'#"mt"#"met_pt"#
    varlabel = var._title#'m_{T}'  #"m_{T}"#"MET_{p_{T}}"#
    #print(var_name)
    
    
    for d in datasets:
        if hasattr(d,"components"):
            samples = d.components
            h_total = ROOT.TH1D(var_name, ";"+varlabel, var._nbins, var._xmin, var._xmax)
            for s in samples:
                infile = ROOT.TFile.Open(repohisto+s.label+'.root')
                h = copy.deepcopy(ROOT.TH1D(infile.Get(var_name)))
                h_total.Add(h)
                infile.Close()
            if not os.path.exists(repohisto+s.label+'.root') :
                outfile = ROOT.TFile.Open(repohisto+d.label+'.root', "RECREATE")
            else:
                outfile = ROOT.TFile.Open(repohisto+d.label+'.root', "UPDATE")
            h_total.Write()
            outfile.Close()
            h_total.Delete()

def writehistos(h, samples, dlabel, var, cut):
    print("Saving histos")
    s_cut = cut_string(cut)
    if opt.recreate :
        ofile = ROOT.TFile.Open(repohisto+dlabel+'.root', "RECREATE")
        print("Creating :", ofile)
    else:
        ofile = ROOT.TFile.Open(repohisto+dlabel+'.root', "UPDATE")
        print("Writing :", ofile)
    for v in var:
        h_tmp = ROOT.TH1D(v._name+"_"+s_cut, ";"+v._title, v._nbins, v._xmin, v._xmax)
        print(samples.keys())
        for s in samples.keys():
            if nfiles_max > len(samples[s]['strings']): nfiles = len(samples[s]['strings'])
            else: nfiles = nfiles_max
            ntot = np.sum(samples[s]['ntot'][:nfiles])
            print('Ntot =', ntot)
            w = sample_dict[s].sigma*lumi*10**3/ntot
            tmp = h[s][v._name].GetValue()
            tmp.Scale(w)
            h_tmp.Add(tmp)
        print("Saved "+v._title +" for "+ dlabel+" datasets")
        h_tmp.Write()
    ofile.Close()
#################### make stack plosts #########################

def makestack(datasets, var, cut):
    
    c_ = cut_string(cut)#cut.replace(" ", "").replace("&&","_").replace(">","g").replace(".","_").replace("==","e")
    #"lepveto"  #""#+"_isMerged"#+"_isMix"#+"_isResolved"
    for v in var: 
        #var_name = var._name+"_"+c_#'mt_'+cut  #'BestTop_pt'#"mt"#"met_pt"#
        #varlabel = var._title#'m_{T}'  #"m_{T}"#"MET_{p_{T}}"#
        print(v._name)
        stack = ROOT.THStack(v._name+"_"+c_, v._name+"_"+c_)
        leg_stack = ROOT.TLegend(0.45,0.88,0.9,0.75)
        leg_stack.SetNColumns(2)
        leg_stack.SetFillColor(0)
        leg_stack.SetFillStyle(0)
        leg_stack.SetTextFont(42)
        leg_stack.SetBorderSize(0)
        leg_stack.SetTextSize(0.03)
    
        h_sgn = []
        for d in datasets:
            infile = ROOT.TFile.Open(repohisto+d.label+'.root')
            h = copy.deepcopy(ROOT.TH1D(infile.Get(v._name+"_"+c_)))#copy.deepcopy(ROOT.TH1D(infile.Get(var._name+"_"+c_)))
            h.GetXaxis().SetTitle(v._title)
            #if 'mt_' in var._name : h.Rebin(4)
            #if 'MET_pt_' in var_name:  h.Rebin()
            #if 'Top_pt_' in var_name:  h.Rebin()
            h.SetName(d.leglabel)
            if not 'Tp' in d.label:
                h.SetLineColor(d.color)
                h.SetFillColor(d.color)
                stack.Add(h)
            else:
                h.SetLineColor(d.color)
                h_sgn.append(h)
                leg_stack.AddEntry(h, d.leglabel, "l")
            infile.Close()
            if not 'Tp' in d.label : leg_stack.AddEntry(h, d.leglabel, "f")
    
        c1 = ROOT.TCanvas("c_"+v._name+"_"+c_,"c_"+v._name+"_"+c_,50,50,700,600)
        c1.SetLogy()
        c1.SetFillColor(0)
        c1.SetBorderMode(0)
        c1.SetFrameFillStyle(0)
        c1.SetFrameBorderMode(0)
        c1.SetLeftMargin( 0.12 )
        c1.SetRightMargin( 0.9 )
        c1.SetTopMargin( 1 )
        c1.SetBottomMargin(-1)
        c1.SetTickx(1)
        c1.SetTicky(1)
        c1.cd()

        pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
        pad1.SetTopMargin(0.1)
        pad1.SetBottomMargin(-0.9)
        pad1.SetLeftMargin(0.12)
        pad1.SetRightMargin(0.05)
        pad1.SetBorderMode(0)
        pad1.SetTickx(1)
        pad1.SetTicky(1)
        pad1.Draw()
        pad1.cd()
        pad1.SetLogy()
        c1.Draw()
        stack.Draw("HIST")
        #print(stack)
        stackmaximum = stack.GetHistogram().GetMaximum()#*10000
        stackminimum = stack.GetHistogram().GetMinimum()#10**(-7)#min([h.GetMinimum() for h in h_sgn])#*0.1
        print(stackminimum, stackmaximum)
        stack.SetMinimum(stackminimum*10**(-5))
        stack.SetMaximum(stackmaximum*10000)
        stack.GetYaxis().SetTitle("# Events")
        stack.GetXaxis().SetTitle(v._title)
        #stack.GetXaxis().SetLabelOffset(0.0)
        stack.GetYaxis().SetTitleOffset(0.85)
        stack.GetXaxis().SetLabelSize(0.03)
        stack.GetYaxis().SetLabelSize(0.05)
        stack.GetYaxis().SetTitleSize(0.07)
        stack.GetXaxis().SetTitleSize(0.05)    
        stack.SetTitle("")

        stack.Draw("HIST")
        for h in h_sgn : 
            h.Draw("same")
        leg_stack.Draw("same")
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = ""
        lumi_sqrtS = "%s fb^{-1}  (13 TeV)"%(lumi)
     
        iPeriod = 0
        iPos = 10
        CMS_lumi(pad1, lumi_sqrtS, iPos, "")
    
        c1.Print(repostack+"stack_"+v._name+"_"+c_+".png","png")
        c1.Print(repostack+"stack_"+v._name+"_"+c_+".pdf","pdf")

########### plotting varibles definition ##############
cut = opt.cut
var = []

if "EventTopCategory==1" in cut:
    var.append(variable(name = "Top_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 10, xmin = 500, xmax=1000))
    var.append(variable(name = "Top_score", title= "Top score", taglio = cut, nbins = 10, xmin = 0.8, xmax=1))
elif "EventTopCategory==2" in cut:
    #var.append(variable(name = "BestTop_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 30, xmin = 400, xmax=500))
    var.append(variable(name = "Top_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 4, xmin = 300, xmax=500))
    var.append(variable(name = "Top_score", title= "Top score", taglio = cut, nbins = 8, xmin = 0.3, xmax=1))
elif "EventTopCategory==3" in cut:
    #var.append(variable(name = "BestTop_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 30, xmin = 0, xmax=400))
    var.append(variable(name = "Top_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 6, xmin = 0, xmax=300))
    var.append(variable(name = "Top_score", title= "Top score", taglio = cut, nbins = 6, xmin = 0.5, xmax=1))
else:
    #var.append(variable(name = "BestTop_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 30, xmin = 0, xmax=1000))
    var.append(variable(name = "Top_pt", title= "Top p_{T} [GeV]", taglio = cut, nbins = 20, xmin = 0, xmax=1000))
    var.append(variable(name = "Top_score", title= "Top score", taglio = cut, nbins = 8, xmin = 0.3, xmax=1))

var.append(variable(name = "MET_pt", title= "MET p_{T} [GeV]", taglio = cut, nbins = 15, xmin = 150, xmax=1000))
var.append(variable(name = "MET_phi", title= "MET #phi [GeV]", taglio = cut, nbins = 6, xmin = -math.pi, xmax=math.pi))
var.append(variable(name = "Mt", title="M_{T} [GeV]", taglio = cut, nbins = 15, xmin = 0, xmax=2000))
var.append(variable(name = "Top_phi", title= "Top #phi", taglio = cut, nbins = 6, xmin = -math.pi, xmax=math.pi))
var.append(variable(name = "Top_eta", title= "Top #eta", taglio = cut, nbins = 9, xmin = -4, xmax=4))
var.append(variable(name = "Top_mass", title= "Top mass [GeV]", taglio = cut, nbins = 15, xmin = 0, xmax=500))

print("plotting varibales : ", [v._title for v in var])
############ dataset import ########
if not opt.dataset in sample_dict.keys():
    datasets = [ QCD_2018,#QCDHT_300to500_2018#, 
                 ZJetsToNuNu_2018, 
                 TT_2018,
                 TprimeToTZ_700_2018, 
                 TprimeToTZ_1000_2018,TprimeToTZ_1800_2018
             ]
else : datasets = [sample_dict[opt.dataset]]

print(datasets)
#import concurrent.futures
if opt.samples:
    print("Producing samples dict")
    samples = {}
    for d in datasets:
        samples[d.label] = {}
        print("... loading ",d.label)
        if hasattr(d, "components"):
            #samples[d] = d.components
            tmp_samples = d.components
        else:
            #samples[d] = [d]
            tmp_samples = [d]
        
        for s in tqdm(tmp_samples):#samples[d]:
            strings = get_files_string(s)
            hist = ROOT.TH1F()
            ntot = [] 
            #if len(strings)>5: strings = strings[:3]
            print("looping on strings: ", len(strings))
            for f in strings: 
                #chain.Add(f)
                ifile = ROOT.TFile.Open(f)
                h_genweight = ROOT.TH1F(ifile.Get("plots/h_genweight"))
                #print("N event single file:", h_genweight.GetBinContent(1))
                ntot.append(h_genweight.GetBinContent(1))
                ifile.Close()
            samples[d.label][s.label] = {'strings': strings, 'ntot': ntot}
    print(samples)
    sample_file = open("samples/dict_samples.pkl", "wb")
    pkl.dump(samples, sample_file)
    sample_file.close()

if opt.plots:
    t1 = datetime.now()
    print(t1)
    sample_file = open("samples/dict_samples.pkl", "rb")
    samples = pkl.load(sample_file)
    sample_file.close()
    #print(samples['QCD_2018'])
    for d in datasets:
        
        c = opt.cut
        #print(samples[d.label])
        if hasattr(d, "components"): # con i bkgs ho samples['QCD_2018'][component]
            h = makehistos(samples[d.label], var, c)
            writehistos(h, samples[d.label], d.label, var, c)
        elif hasattr(d, "process"):
            h = makehistos(samples[d.process][d.label], var, c)
            writehistos(h, samples[d.label][d.label], d.label, var, c)
        else: # con i file di segnale ho samples['Tprime...']['Tprime...']
            h = makehistos(samples[d.label], var, c)
            writehistos(h, samples[d.label], d.label, var, c)
        #arglocal=(samples[d.label], var, c)
        #with concurrent.futures.ProcessPoolExecutor() as executor:
        #    future=executor.submit(makehistos_p,arglocal)
        #    print(future.result())
        
            
    t2 = datetime.now()
    print(t2-t1)

if opt.stack:
    datasets = [ QCD_2018,#QCDHT_300to500_2018#,
                 ZJetsToNuNu_2018,
                 TT_2018,
                 TprimeToTZ_700_2018,
                 TprimeToTZ_1000_2018,TprimeToTZ_1800_2018
             ]
    makestack(datasets, var, cut)
