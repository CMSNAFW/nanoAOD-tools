import os
import optparse
import sys
import time
from PhysicsTools.NanoAODTools.postprocessing.samples.samples_fra import *
from get_file_fromdas import *
from get_file_fromdas_dark import *

usage = 'python submit_condor.py -d dataset_name -f destination_folder'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dat', type=str, default = '', help='Please enter a dataset name')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
#parser.add_option('-u', '--user', dest='us', type='string', default = 'ade', help="")
(opt, args) = parser.parse_args()
#Insert here your uid... you can see it typing echo $uid

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'adeiorio':
    uid = 103214
elif username == 'acagnott':
    uid = 140541
elif username == 'fscrivan':
    uid=172801


def sub_writer(path, dat_name, outname, label, file_num, excutable):
    f = open("condor_"+excutable+".sub", "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    f.write("transfer_input_files    = $(Proxy_path)\n")
    #f.write("transfer_output_remaps  = \""+outname+"_Skim.root=root://eosuser.cern.ch///eos/user/"+inituser + "/" + username+"/DarkMatter/topcandidate_file/"+dat_name+"_Skim.root\"\n")
    f.write("+JobFlavour             = \"tomorrow\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write('+Tag                    = "'+label+'"\n') # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write("executable              = runner_fra_"+excutable+".sh\n") #passare come argomento
    f.write("arguments               = "+path+" "+dat_name+" "+outname+" "+label+" "+file_num+"\n")
    #f.write("input                   = input.txt\n")
    f.write("output                  = condor_"+excutable+"/output/"+ label+"_"+file_num+".out\n") #modificare questo con l'excutable
    f.write("error                   = condor_"+excutable+"/error/"+ label+"_"+file_num+".err\n")
    f.write("log                     = condor_"+excutable+"/log/"+ label+"_"+file_num+".log\n")

    f.write("queue\n")
#lista_excutable = ["SR_norm", "SR_Z", "CR_norm", "CR_Z"]
lista_excutable = ["regioni_new"]
for  s in lista_excutable:
    if not os.path.exists("condor_"+s+"/output"):
        os.makedirs("condor_"+s+"/output")
    if not os.path.exists("condor_"+s+"/error"):
        os.makedirs("condor_"+s+"/error")
    if not os.path.exists("condor_"+s+"/log"):
        os.makedirs("condor_"+s+"/log")
if(uid == 0):
    print("Please insert your uid")
    exit()
if not os.path.exists("/tmp/x509up_u" + str(uid)):
    os.system('voms-proxy-init --rfc --voms cms -valid 192:00')
os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")

#datasets = QCD_PT_2022.components+[DataJetMETC_2022, tDM_mPhi1000_mChi1_2025, ttDM_mPhi1000_mChi1_2025, tDM_mPhi500_mChi1_2025, ttDM_mPhi500_mChi1_2025, tDM_mPhi200_mChi1_2025, ttDM_mPhi200_mChi1_2025, tDM_mPhi50_mChi1_2025, ttDM_mPhi50_mChi1_2025, TT_hadr_2022,TT_semilep_2022, QCD_HT40to70_2022, WtoLNu_4Jets_4J_2022, WtoLNu_4Jets_2022]+ZJetsToNuNu_2022.components+QCD_2022.components  
datasets = TT_bar_2024.components + [TT_hadr_2024] + ZJetsToNuNu_2024.components
#datasets = [TT_hadr_2022]  
#datasets = [TT_hadr_2022]   
#datasets = [DataJetMETC_2022]
#datasets = [QCD_HT40to70_2022]

#datasets = [ TT_hadr_2022,TT_semilep_2022]+ZJetsToNuNu_2022.components
#datasets = [TT_hadr_2022]
#datasets =[TT_hadr_2022,TT_semilep_2022 ]
#datasets = [ZJetsToNuNu_HT800to1200_2018]
#print("ZJetsToNuNu_2022.components", ZJetsToNuNu_2022.components)

for d in datasets:
    label = d.label
    all_files = get_files_string(d)

    if (label == "tDM_mPhi1000_mChi1_2025" or label == "ttDM_mPhi1000_mChi1_2025" or label == "tDM_mPhi500_mChi1_2025" or label == "ttDM_mPhi500_mChi1_2025" or label == "tDM_mPhi200_mChi1_2025" or label == "ttDM_mPhi200_mChi1_2025" or label == "tDM_mPhi50_mChi1_2025" or label == "ttDM_mPhi50_mChi1_2025"):
            #files = get_files_string_dark(d)
            dat3=[]
    


            #all_files = get_files_string_dark(d)
            dat_i = get_files_string_dark(d)[0]
            dat_i= 'root://cms-xrd-global.cern.ch//'+dat_i
         
            dat3.append(dat_i)
            dat_string = ",".join(dat3)
            
            #outname=dat[0].split("/")[-1].replace('.root', '_output.root')
            outname = f"{label}_{0}_output.root"
            i= "0"
            
        
        
        
        
            final_name = f'/eos/user/f/fscrivan/datasets/{d.label}_Skim.root'
        
            for  s in lista_excutable:
                sub_writer(dat_string, final_name, outname, label, i, s)
                print("s")
                print("")
                print("label",d.label)
                print("")
                print("dat_string",dat_string)
                print("")
                print(d.label)
                print("")
                #print(dat)
                print("")
            
                os.popen('condor_submit condor_'+s+'.sub')
                time.sleep(5)


    #print("label",d.label)
    #print("lunghezza file", len(all_files))

    # Se la label è "spugna", usa solo i primi 2 file
    if d.label == "DataJetMETD_2022":
        print(f"Salto dataset con label: {d.label}")
        continue  # passa al prossimo dataset

    # Cicla sui file selezionati
    if not(label == "tDM_mPhi1000_mChi1_2025" or label == "ttDM_mPhi1000_mChi1_2025" or label == "tDM_mPhi500_mChi1_2025" or label == "ttDM_mPhi500_mChi1_2025" or label == "tDM_mPhi200_mChi1_2025" or label == "ttDM_mPhi200_mChi1_2025" or label == "tDM_mPhi50_mChi1_2025" or label == "ttDM_mPhi50_mChi1_2025"):
        if (label == "DataJetMETC_2022"):
            l= len(all_files)
            #l=1
        else:
            l=len(all_files)
            """
            if len(all_files) < 3:
                print("if", len(all_files), label)
                l=len(all_files)
            else:
                print("else", len(all_files), label)
                l=3
            """
            
            
        
    
           
        for i in range(l):
            dat = []
            dat=[]
            #print("dat",dat)
            #print("i",i)
            label = d.label


            
            

            if label == "WtoLNu_4Jets_4J_2022" or label == "QCD_HT70to100_2022" or label == "QCD_HT100to200_2022" or label == "QCD_HT200to400_2022" or label == "QCD_HT400to600_2022" or label == "QCD_HT600to800_2022" or label == "QCD_HT800to1000_2022" or label == "QCD_HT1000to1200_2022" or label == "QCD_HT1200to1500_2022" or label == "QCD_HT1500to2000_2022" or label == "QCD_HT2000_2022":
                dat_i = get_files_string_dark(d)[i]
            else:
                dat_i = get_files_string(d)[i]

            dat_i= 'root://cms-xrd-global.cern.ch//'+dat_i
            dat.append(dat_i)   
        
            dat_string = ",".join(dat)
            #outname=dat[0].split("/")[-1].replace('.root', '_output.root')
            outname = f"{label}_{i}_output.root"
            
            
            
            
            final_name = f'/eos/user/f/fscrivan/datasets/{d.label}_Skim.root'
            i = str(i)
            for  s in lista_excutable:
                sub_writer(dat_string, final_name, outname, label, i, s)
                print("s")
                print("")
                print("label",d.label)
                print("")
                print("dat_string",dat_string)
                print("")
                print(d.label)
                print("")
                print(dat)
                print("")
            
                os.popen('condor_submit condor_'+s+'.sub')
                time.sleep(5)

#print([d.label for d in datasets])
#mettere sub_writer fuori in modo tale che tutto quello che TT_hadr_2022 sia unito insieme 
