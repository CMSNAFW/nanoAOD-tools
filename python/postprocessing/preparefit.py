import os
import shutil
import optparse
import copy
from symmetry import symmetry,nnpdfeval
from repos import histosr,histocr,extrasr,extracr
from fit_utils import shift,smoothing,scale
from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *

pi = '/afs/cern.ch/work/o/oiorio/Wprimean/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing/newtest5/v17_explin/'
po = '/afs/cern.ch/work/o/oiorio/Wprimean/CMSSW_10_5_0/src/PhysicsTools/NanoAODTools/python/postprocessing/newtest5/v17_explin_fit/'

usage = "python preparefit.py -l muon,electron -i pathinput -o pathoutput -v v17 -y 2016,2017,2018"
parser = optparse.OptionParser(usage)
parser.add_option('--years','-y', dest='years', default = '2016,2017,2018', type='string', help='years to run')
parser.add_option('-l', '--lep', dest='leptons', default = 'muon,electron', type='string', help='lepton to run')
parser.add_option('-v', '--version', dest='version', default = 'v18', type='string', help='analysis version')
parser.add_option('-i', '--inputpath', dest='inputpath', default = pi, type='string', help='file in , not working yet!')
parser.add_option('-o', '--outputpath', dest='outputpath', default = po, type='string', help='file in , not working yet!')
parser.add_option('-n', '--dryrun', dest='dryrun', action= 'store_true' , default = False, help='if called not running the command')
parser.add_option('-m', '--mode', dest='mode',default = 'sum symmetrize smooth' , type='string', help='"sum" splits systs per years, "symmetrize" symmetrizes DD uncertainties, "smooth" smooths QCD histograms')
parser.add_option('--parallel', dest='parallel', type='int', default=1 , help='if called run on more than 1 plot simultaneously')
parser.add_option('-r', '--refresh', dest='refresh', action= 'store_true' , default = False, help='if called empty the output folders first')
parser.add_option('-e','--extraregions', dest='extraregions', action="store_true", default = False, help='use extra regions for later recorrection')
#parser.add_option('--cut','-c', dest='cuts', default = '', type='string', help='years to run')
(opt, args) = parser.parse_args()

extended = opt.extraregions
#extended=True

version = opt.version
pathin = opt.inputpath 
pathout = opt.outputpath
dryrun = opt.dryrun

signals = {}

signals['RH2020'] = [sample.label.replace('_2016', '') for sample in sample_dict['WP_RH_2016'].components]
signals['RH2016'] = [sample.label.replace('_2016', '') for sample in sample_dict['WP_RH_2016'].components]
signals['RH2017'] = [sample.label.replace('_2017', '') for sample in sample_dict['WP_RH_2017'].components]
signals['RH2018'] = [sample.label.replace('_2018', '') for sample in sample_dict['WP_RH_2018'].components]
signals['LHSMinter2020'] = [sample.label.replace('_2016', '') for sample in sample_dict['WP_LHSMinter_2016'].components]
signals['LHSMinter2016'] = [sample.label.replace('_2016', '') for sample in sample_dict['WP_LHSMinter_2016'].components]
signals['LHSMinter2017'] = [sample.label.replace('_2017', '') for sample in sample_dict['WP_LHSMinter_2017'].components]
signals['LHSMinter2018'] = [sample.label.replace('_2018', '') for sample in sample_dict['WP_LHSMinter_2018'].components]
#simple case

basesigs = ["WP_M2000W20_RH", "WP_M3000W30_RH", "WP_M4000W40_RH", "WP_M5000W50_RH", "WP_M6000W60_RH"]
signals={}
for ye in ["2016","2017","2018","2020"]:
    signals["RH"+ye]= basesigs
    signals["LHSMinter"+ye]= []

#print(signals)

samples = ["DDFitWJetsTT_MttST"]
#systs = ["PF", "pu", "lep", "trig", "jes", "jer", "btag", "mistag", "pdf_total", "TT_Mtt", "WJets", "ST"]
systs = ["TT_Mtt", "WJets", "ST"]
systs_peryear = ["TF", "DD", "Alt"]
#systs = ["PF", "pu", "lep", "trig", "jes", "jer", "btag", "mistag", "pdf_total", "TT_Mtt", "WJets", "ST", "TF", "DD"]
samples2 = ["QCD"] #, "WP_M2000W20_RH", "WP_M3000W30_RH", "WP_M4000W40_RH", "WP_M5000W50_RH", "WP_M6000W60_RH"]
#samples2 = []
systs2 = ["PF", "pu", "lep", "trig", "jes", "jer", "btag", "mistag", "pdf_total"]

samples_smooth = {"QCD":["h_jets_best_Wprime_m_SR2B"]}
samples_smooth["QCD"].append("h_jets_best_Wprime_m_selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag_AND_best_top_m_G_340_AND_deltaR_bestWAK4_closestAK8_L_0p4_AND_WprAK8_mSD_G_30")
samples_smooth["QCD"].append("h_jets_best_Wprime_m_SR2B_I")
systs_smooth = systs2

samples_symmetrize = copy.deepcopy(samples)
samples_pdfeval = []
samples_pdfeval = signals["RH2020"]

#samples_pdfeval 
#samples_symmetrize.append("QCD")
systs_symmetrize = systs
systs_symmetrize = ["TF_2020", "DD_2020", "Alt_2020", "AltTF_2020"]+["TT_Mtt", "WJets", "ST"]+["jes","btag"]+["jer","lep","pu"]

versus = ['Up', 'Down']
leps = ['muon', 'electron']
#leps = ['muon']
years = ['2016', '2017', '2018']

leps = opt.leptons.split(',')
years = opt.years.split(',')
mode = opt.mode

allhistos = histosr+histocr
if(extended):
    allistos = allhistos+extrasr+extracr

if opt.refresh:
    os.system(" rm -rf "+pathout+"/*")
    
if os.path.exists(pathout):
    #os.popen('rm -r '+ pathout + '/*')
    print 'ciao'
else:
    os.makedirs(pathout)

summedyears = False
splityears = False
smooth = False
symmetrize = False
pdfeval = False
reducebins=False
if 'sum' in mode: 
    summedyears = True
if 'splityears' in mode: 
    splityears = True
if 'smooth' in mode:
    smooth = True
if 'symmetrize' in mode:
    symmetrize = True
if 'pdfeval' in mode:
    pdfeval = True
if 'reduce' in mode:
    reducebins = True

for lep in leps:
    if not os.path.exists(pathout+"/"+lep):os.makedirs(pathout + '/' + lep)
    if not summedyears:
        if splityears:
            for year in years:
                samples += signals['RH'+year] + signals['LHSMinter'+year]
                filename = 'Data_' + year + '_' + lep + '.root'
                print('copying ', filename)
                #shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
                for sample in samples:
                    filename = sample + '_' + year + '_' + lep + '.root'
                    print('copying ', filename)
                    shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
                    for syst in systs:
                        for vs in versus:
                            filename = sample + '_' + year + '_' + lep + '_' + syst + vs + '.root'
                            print('copying ', filename)
                            shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
                    for syst in systs_peryear:
                        for vs in versus:
                            filename = sample + '_' + year + '_' + lep + '_' + syst + '_' + year + vs + '.root'
                            if lep == 'muon':
                                fileout = sample + '_' + year + '_' + lep + '_' + syst + '_mu_' + year + vs + '.root'
                            else:
                                fileout = sample + '_' + year + '_' + lep + '_' + syst + '_ele_' + year + vs + '.root'
                            print('copying ', filename)
                            shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + fileout)

                samples2 += signals['RH'+year] + signals['LHSMinter'+year]
                for sample in samples2:
                    filename = sample + '_' + year + '_' + lep + '.root'
                    print('copying ', filename)
                    shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
                    for syst in systs2:
                        for vs in versus:
                            filename = sample + '_' + year + '_' + lep + '_' + syst + vs + '.root'
                            print('copying ', filename)
                            shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
    else:
        systs = ["jes", "jer", "btag", "mistag", "pdf_total", "pu", "PF"]#, "q2"]
        systs_DD = ["TF_2020", "DD_2020", "Alt_2020", "TT_Mtt", "WJets", "ST","AltTF_2020"]
        if extended: systs_DD.extend(["CR_2020"])
        systs_perlep = ["lep", "trig"]
        systs_perlep = []

        filename = 'Data_2020_' + lep + '.root'
        print('copying ', filename)
        shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)

        for sample in samples:
            filename = sample + '_2020_' + lep + '.root'
            print('copying ', filename)
            shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
            for syst in systs_DD:
                for vs in versus:
                    filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                    if lep == 'muon':
                        fileout = sample + '_2020_' + lep + '_' + syst + '_mu' + vs + '.root'
                    else:
                        fileout = sample + '_2020_' + lep + '_' + syst + '_ele' + vs + '.root'
                    print('copying ', filename)
                    shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + fileout)

        samples2 += signals['RH2016'] + signals['LHSMinter2016']
        for sample in samples2:
            filename = sample + '_2020_' + lep + '.root'
            print('copying ', filename)
            shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
            print(systs)
            for syst in systs:
                for vs in versus:
                    filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                    print('copying ', pathin + '/' + lep + '/' + filename, " in ", pathout +  '/' + lep + '/' + filename)
                    shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + filename)
            print(systs_perlep)
            for syst in systs_perlep:
                for vs in versus:
                    filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                    if lep == 'muon':
                        fileout = sample + '_2020_' + lep + '_' + syst + '_mu' + vs + '.root'
                    else:
                        fileout = sample + '_2020_' + lep + '_' + syst + '_ele' + vs + '.root'
                    #print('copying ', filename)
                    print('copying ', pathin + '/' + lep + '/' + filename, " in ", pathout +  '/' + lep + '/' + fileout)
                    shutil.copyfile(pathin + '/' + lep + '/' + filename, pathout +  '/' + lep + '/' + fileout)

    if(smooth):
        for sample in samples_smooth:
            #                print "sample to smooth ",sample, " histograms:"
            #                print allhistos 
            #print samples_smooth[sample]
            filename = sample + '_2020_' + lep + '.root'
            fileout = pathout+'/'+lep+'/'+filename
            print(" nominal fileout ",fileout)
            for h in allhistos:
                if not(h in samples_smooth[sample]):
                    continue
                filename = sample + '_2020_' + lep + '.root'
                fileout = pathout+'/'+lep+'/'+filename
                print("sample ",sample , " syst nominal histo ",h, " fileout ",fileout)
                smoothing(fileout,h)
                for syst in systs_smooth:
                    print("sample ",sample , " syst " , syst, " histo ",h)
                    for vs in versus:
                        if(syst in systs):
                            filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                        if(syst in systs_DD):
                            filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                            if lep == 'muon':
                                filename = sample + '_2020_' + lep + '_' + syst + '_mu' + vs + '.root'
                            else:
                                filename = sample + '_2020_' + lep + '_' + syst + '_ele' + vs + '.root'
                                    
                        if(syst in systs_perlep):
                            for vs in versus:
                                filename = sample + '_2020_' + lep + '_' + syst + vs + '.root'
                                if lep == 'muon':
                                    filename = sample + '_2020_' + lep + '_' + syst + '_mu' + vs + '.root'
                                else:
                                    filename = sample + '_2020_' + lep + '_' + syst + '_ele' + vs + '.root'
                                                        
                        fileout = pathout+'/'+lep+'/'+filename
                        print("smoothing file ", fileout)
                        smoothing(fileout,h)
    
    if(symmetrize):
        print "symmetrizing"
        if extended: systs_symmetrize.extend(["CR_2020"])
        for sample in samples_symmetrize:
            #print "sample to smooth ",sample, " histograms:"
            filename = sample + '_2020_' + lep + '.root'
            filenameUp = sample + '_2020_' + lep + '.root'
            filenameDown = sample + '_2020_' + lep + '.root'
            
            fileout = pathout+'/'+lep+'/'+filename
            symmetry(histosr,fUp=fileout,fDown=fileout,fNom=fileout,version="cureZeros")
                                
            for syst in systs_symmetrize:
                print(" symmetrizing ",histosr , sample , syst)
                if(syst in systs):
                    filenameUp = sample + '_2020_' + lep + '_' + syst + "Up" + '.root'
                    filenameDown = sample + '_2020_' + lep + '_' + syst + "Down" + '.root'
                if(syst in systs_DD):
                    if lep == 'muon':
                        filenameUp = sample + '_2020_' + lep + '_' + syst + '_mu' + "Up" + '.root'
                        filenameDown = sample + '_2020_' + lep + '_' + syst + '_mu' + "Down" + '.root'
                    else:
                        filenameUp = sample + '_2020_' + lep + '_' + syst + '_ele' + "Up" + '.root'
                        filenameDown = sample + '_2020_' + lep + '_' + syst + '_ele' + "Down" + '.root'
                if(syst in systs_perlep):
                    if lep == 'muon':
                        filenameUp = sample + '_2020_' + lep + '_' + syst + '_mu' + "Up"+ '.root'
                        filenameDown = sample + '_2020_' + lep + '_' + syst + '_mu' + "Down" + '.root'
                    else:
                        filenameUp = sample + '_2020_' + lep + '_' + syst + '_ele' + "Up" + '.root'
                        filenameDown = sample + '_2020_' + lep + '_' + syst + '_ele' + "Down" + '.root'
                fileout = pathout+'/'+lep+'/'+filename
                fileoutUp = pathout+'/'+lep+'/'+filenameUp
                fileoutDown = pathout+'/'+lep+'/'+filenameDown
                print("symmetry file,up,down ", fileoutUp,fileoutDown,fileout)
                optionsym=""
                #if("CR" in syst) or ("Alt" in syst) :optionsym="switch" 
                if("CR" in syst):optionsym="switch" 
                optionsym="switch"
                if("jes" in syst or "jer" in syst):optionsym=""
                symmetry(histosr,fUp=fileoutUp,fDown=fileoutDown,fNom=fileout,option=optionsym)

    if(pdfeval):
        print "evaluating pdf"
        for sample in samples_pdfeval:
            #print "sample to smooth ",sample, " histograms:"
            filename = sample + '_2020_' + lep + '.root'
            filenameUp = sample + '_2020_' + lep + '_pdf_totalUp.root'
            filenameDown = sample + '_2020_' + lep + '_pdf_totalDown.root'
            filenameRMS  = sample + '_2020_' + lep + '_pdf_RMS.root'
            
            fileout = pathout+'/'+lep+'/'+filename
            fileoutUp = pathout+'/'+lep+'/'+filenameUp
            fileoutDown = pathout+'/'+lep+'/'+filenameDown
            fileoutRMS = pathout+'/'+lep+'/'+filenameRMS

            filein = pathin+'/'+lep+'/'+filename
            fileinUp = pathin+'/'+lep+'/'+filenameUp
            fileinDown = pathin+'/'+lep+'/'+filenameDown
            os.system("cp "+filein+" "+fileout)
            os.system("cp "+fileinUp+" "+fileoutUp)
            os.system("cp "+fileinDown+" "+fileoutDown)
            os.system("cp "+fileoutUp+" "+fileoutRMS)

            nnpdfeval(histosr,fUp=fileoutUp,fDown=fileoutDown,fNom=fileout,fRMS=fileoutRMS)


#versus = ['Up', 'Down']
#leps = ['muon', 'electron']
print histosr
if ( reducebins) :
    from fit_utils import behead,behead_all
    beheadprefix="beheaded"
    beheadprefix=""
    signals_r=signals["RH2020"]+signals["LHSMinter2020"]
    qcds_r=["QCD"]
    Data_r="Data"
    DDBkg_r=["DDFitWJetsTT_MttST"]

    systs_r= ["PF", "pu", "jes", "jer", "btag", "mistag", "pdf_total"]
    systs_lep_r= {"muon":["trig_mu","lep_mu"],"electron":["trig_ele","lep_ele"]}

    systs_perlep_dd=["CR_2020","AltTF_2020","Alt_2020","TF_2020","DD_2020","TT_Mtt","WJets","ST"]
    systs_lep_dd= {"muon":[x+"_mu" for x in systs_perlep_dd],
                   "electron":[x+"_ele" for x in systs_perlep_dd]}
    print "reducing head "
    for lep in leps:
        pathl=pathout +  '/' + lep + '/'

        datafile=pathl+Data_r+'_2020_' + lep + '.root'
        behead_all(datafile, histosr, beheadprefix)

        for sample in signals_r+qcds_r:

            filename = pathl+sample + '_2020_' + lep + '.root'
            print (" sample ", sample, " file nominal ",filename)
            behead_all(filename, histosr, beheadprefix)
            print(systs_r+systs_lep_r[lep])
            for syst in systs_r+systs_lep_r[lep]:
                filenameUp = pathl+sample + '_2020_' + lep + '_' + syst + "Up" + '.root'
                filenameDown = pathl+sample + '_2020_' + lep + '_' + syst + "Down" + '.root'
                print(filenameUp,filenameDown)
                behead_all(filenameUp, histosr, beheadprefix)
                behead_all(filenameDown, histosr, beheadprefix)
                
        for sample in DDBkg_r:
            filename = pathl+sample + '_2020_' + lep + '.root'
            print (" sample ", sample, " file nominal ",filename)
            print(systs_r+systs_lep_r[lep])
            behead_all(filename, histosr, beheadprefix)
            for syst in systs_lep_dd[lep]:
                filenameUp = pathl+sample + '_2020_' + lep + '_' + syst + "Up" + '.root'
                filenameDown = pathl+sample + '_2020_' + lep + '_' + syst + "Down" + '.root'
                print(filenameUp,filenameDown)
                behead_all(filenameUp, histosr, beheadprefix)
                behead_all(filenameDown, histosr, beheadprefix)

