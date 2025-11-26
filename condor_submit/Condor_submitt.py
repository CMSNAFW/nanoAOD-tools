import os
import optparse
import sys
import time
from get_file_fromdas import*
import argparse
#from sample import *
import json
#Loading the samples
from pathlib import Path
import json

#Parser of arguments
parser = argparse.ArgumentParser(description = "Script to submitt to condor")

parser.add_argument("-ds","--dataset", type = str, required = True, help = "Dataset name in Json")
parser.add_argument("-f","--output_analysis", type = str, required = True, help= "Folder on eos to analyze data")
parser.add_argument("-n","--normal_mode", default = False,  action = "store_true", help = "Normal mode for the analysis")
#parser.add_argument("-t","--test", default = False, action = "store_true", help = "Mode for test, start only 1000 jobs")
#parser.add_argument("")



#
options = parser.parse_args()

#
normal = options.normal_mode
dataset = options.dataset
folder = options.output_analysis



username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'adeiorio':
    uid = 103214
elif username == 'acagnott':
    uid = 140541
elif username == "fconfort":
    uid = 179351


def write_runner_sub(run_post_proccesor, output_path = "runner.sh"):
    with open(output_path, "w") as f:
        f.write("#!/usr/bin/bash\n")
        f.write("cd /afs/cern.ch/user/f/fconfort/CMSSW_15_1_0/src/tWb_Single_top_CKM/analysis/condor\n")
        f.write("cmsenv\n")
        f.write("export XRD_NETWORKSTACK=IPv4\n")
        f.write(f"python3 {run_post_proccesor} $1 $2 $3 $4 $5 $6\n")
    os.chmod(output_path, 0o755)



def sub_writer(path, dat_name, outname, label, folder, label_name):
    runner = "runner.sh"
    f = open("condor.sub", "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    f.write("transfer_input_files    = $(Proxy_path)\n")
    #f.write("transfer_output_remaps  = \""+outname+"_Skim.root=root://eosuser.cern.ch///eos/user/"+inituser + "/" + username+"/DarkMatter/topcandidate_file/"+dat_name+"_Skim.root\"\n")
    f.write("+JobFlavour             = \"testmatch\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write(f"executable              = {runner}\n")
    f.write("arguments               = "+path+" "+dat_name+" "+outname+" "+label+" " + folder + " " + label_name +"\n")
    #f.write("input                   = input.txt\n")
    f.write("output                  = condor/output/"+ label_name+".out\n")
    f.write("error                   = condor/error/"+ label_name+".err\n")
    f.write("log                     = condor/log/"+ label_name+".log\n")

    f.write("queue\n")

if not os.path.exists("condor/output"):
    os.makedirs("condor/output")
if not os.path.exists("condor/error"):
    os.makedirs("condor/error")
if not os.path.exists("condor/log"):
    os.makedirs("condor/log")
if(uid == 0):
    print("Please insert your uid")
    exit()
if not os.path.exists("/tmp/x509up_u" + str(uid)):
    os.system('voms-proxy-init --rfc --voms cms -valid 192:00')
os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")



#The normal standard of the Analysis. Normal procedure to start the corrections in successions. 
#dard of the Analysis. Normal procedure to start the corrections in successions. 
if normal:
    with open("run_postproccesor.py", "w") as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("import os\n")
        f.write("import sys\n")
        f.write("import ROOT\n")
        f.write("import math\n")
        f.write("import subprocess\n")
        f.write("ROOT.PyConfig.IgnoreCommandLineOptions = True\n")
        f.write("from importlib import import_module\n")
        f.write("from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor\n")
        f.write("from sf_Module_2024 import get_SF_modules\n")
        f.write("\n")
        f.write("# Important variables for the analysis\n")
        f.write("fnames = [sys.argv[1]]\n")
        f.write("final_name = sys.argv[2]\n")
        f.write("outname = sys.argv[3]\n")
        f.write("label = sys.argv[4]\n")
        f.write("folder_histo_events = sys.argv[5]\n")
        f.write("label_name = sys.argv[6]\n")
        f.write("\n")
        f.write("# Import modules for post-processor\n")
        f.write("modules = get_SF_modules()\n")
        f.write("\n")
        f.write("# Create output folder\n")
        f.write("output_analysis = folder_histo_events + '_' + label\n")
        f.write("output_path = '/eos/user/f/fconfort/tWb_CKM/' + output_analysis\n")
        f.write("os.makedirs(output_path, exist_ok=True)\n")
        f.write("\n")
        f.write("p = PostProcessor(\n")
        f.write("    '/eos/user/f/fconfort/tWb_CKM/' + output_analysis,\n")
        f.write("    fnames,\n")
        f.write("    modules = modules,\n")
        f.write("    noOut = False,\n")
        #f.write("    histFileName = 'jetId_hist.root',\n")   # <--- aggiunto per salvare istogrammi
        #f.write("    histDirName = 'plots',\n")             # <--- cartella interna ROOT
        f.write("    postfix = '_' + label_name,\n")
        f.write("    maxEntries = 100,\n")
        f.write(")\n")
        f.write("\n")
        f.write("p.run()\n")

    os.chmod("run_postproccesor.py", 0o755)
    
    cmssw_base = os.environ.get('CMSSW_BASE')
    path = Path(f"{cmssw_base}/src/PhysicsTools/NanoAODTools/condor_submit/CKM_samples24.json")
    #print(path)    path = Path(f"{cmssw_base}/src/tWb_Single_top_CKM/analysis/CKM_samples24.json")
    #print(path)
    
    with open (path) as f: 
        dataset_json = json.load(f)
    
    
    if dataset not in dataset_json:
        print(f"Dataset '{dataset}' not found in JSON")
        sys.exit(1)

    entry = dataset_json[dataset]

    #print(entry)

    class JSONDataset:
        def __init__(self, das, label, isData, year):
            self.dataset = das
            self.label = label
            self.isData = isData
            self.year = year


    run_post = "run_postproccesor.py"
    write_runner_sub(run_post)

    dataset = JSONDataset(
    entry["das"],
    entry["label"],
    entry["isData"],
    entry["year"]
    )

    #print(dataset)

    print("Getting files from DAS...")
    files = get_files_string(dataset)

    #print(files)    

    for i, f in enumerate(files):
        dat = "root://cms-xrd-global.cern.ch//" + f
        
        outname = f"{dataset.label}_{i}_Skim.root"
        final_name = f"/eos/f/fconfort/NanoAOD_outputs/{outname}"
        label_name = f"{dataset.label}_{i}"
        label = dataset.label

        sub_writer(dat, final_name, outname, label, folder, label_name)

        print(f"Submitting job for {label_name} — file {i}")
        print(dat)

        os.system("condor_submit condor.sub")
        time.sleep(2)

        # REMOVE IF YOU WANT ALL FILES
        if i == 0:
            break
