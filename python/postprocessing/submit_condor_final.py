from samples.samples import *
from training import *
import os
import optparse
import sys

usage = 'python submit_condor.py -d dataset_name -f destination_folder'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dat', type=str, default = '', help='Please enter a dataset name')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
parser.add_option('-t', '--training', dest='training',type=str,default = 'BDT_Tprime', help='Please eneter a training name')
#parser.add_option('-u', '--user', dest='us', type='string', default = 'ade', help="")
(opt, args) = parser.parse_args()
#Insert here your uid... you can see it typing echo $uid
print("Check uid users")
uid = 0
username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'adeiorio':
    uid = 103214
elif username == 'apiccine':
    uid = 124949
elif username == 'fcarneva':
    uid = 127697
elif username == 'fabozzi':
    uid = -1
elif username == 'cdifraia':
    uid = -1

def sub_writer(sample, n, files, folder, training, train_files):
    f = open("condor.sub", "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    #f.write("transfer_input_files    = $(Proxy_path), tree_skimmer_Tprime_vers2.py, training.py, samples/samples.py, skimtree_utils.py, __init__.py, "+train_files+"\n")
    #f.write("transfer_output_remaps  = \""+ sample.label + "_part" + str(n) + ".root=/eos/user/"+inituser + "/" + username+"/Wprime/nosynch/" + folder + "/" + sample.label +"/"+ sample.label + "_part" + str(n) + ".root\"\n")
    f.write("+JobFlavour             = \"tomorrow\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write("executable              = runner_"+sample.label+"_"+str(n)+".sh \n")
    #f.write("arguments               = " + sample.label + " " + str(n) + " " + str(files) + " " + str(folder) "\n")
    #f.write("input                   = input.txt\n")
    f.write("output                  = condor/output/"+ sample.label + "_part" + str(n) + ".out\n")
    f.write("error                   = condor/error/"+ sample.label + "_part" + str(n) + ".err\n")
    f.write("log                     = condor/log/"+ sample.label + "_part" + str(n) + ".log\n")
    f.write("queue\n")

def runner_writer(sample, n, files, folder, training):
    f = open("runner_"+sample.label+"_"+str(n)+".sh", "w")
    f.write("#!/bin/bash \n")
    f.write("cd " + str(os.getcwd()) + "\n")
    f.write("eval `scramv1 runtime -sh` \n")
    f.write("python tree_skimmer_Tprime_final.py " + sample.label + " " + str(n) + " " + str(files) + " " + str(folder)+" "+str(training)+"\n")
    f.write("rm runner_"+sample.label+"_"+str(n)+".sh")

if not(opt.dat in sample_dict.keys()):
    print sample_dict.keys()
dataset = sample_dict[opt.dat]
samples = []

if hasattr(dataset, 'components'): # How to check whether this exists or not
    samples = [sample for sample in dataset.components]# Method exists and was used.
else:
    print "You are launching a single sample and not an entire bunch of samples"
    samples.append(dataset)

if not os.path.exists("condor/output"):
    os.makedirs("condor/output")
if not os.path.exists("condor/error"):
    os.makedirs("condor/error")
if not os.path.exists("condor/log"):
    os.makedirs("condor/log")

if(uid == 0):
    print("Please insert your uid")
    os.system("echo $uid")
    exit()
if not os.path.exists("/tmp/x509up_u" + str(uid)):
    os.system('voms-proxy-init --rfc --voms cms -valid 192:00')
os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")


folder = opt.folder
split = 100
training= opt.training
train = training_dict[training]
train_files =""
for i in range(len(train)): train_files+=str(train[i].files)+", "
train_files=train_files[:-2]

#Writing the configuration file
for sample in samples:
    isMC = True
    if('Data' in sample.label):
        isMC = False
    if not os.path.exists("/eos/user/" + inituser + "/" + username + "/Tprime/nosynch/" + folder + "/" + sample.label):
        os.makedirs("/eos/user/" + inituser + "/" + username +"/Tprime/nosynch/" + folder + "/" + sample.label)
    f = open("../../crab/macros/files/" + sample.label + ".txt", "r")
    files_list = f.read().splitlines()
    final_folder = "/eos/user/" + inituser + "/" + username +"/Tprime/nosynch/" + folder + "/" + sample.label
    print(str(len(files_list)))
    if(isMC):
        for i, files in enumerate(files_list):
            if(("TT" in sample.label) or ("ST" in sample.label)) and (i>50):continue
            runner_writer(sample, i, files, final_folder,training)
            sub_writer(sample, i, files, final_folder,training,train_files)
            os.popen('condor_submit condor.sub')
            print('condor_submit condor.sub')
            #os.popen("python tree_skimmer.py " " + sample.label + " " + str(i) + " " + str(files))
            print("python tree_skimmer.py " + sample.label + " " + str(i) + " " + str(files) + " " + str(final_folder)+" "+str(training))
    else:
        for i in range(len(files_list)/split+1):
            files_selected=",".join( e for e in files_list[split*i:split*(i+1)])
            runner_writer(sample, i, files_selected, final_folder,training)
            sub_writer(sample, i, files_selected, final_folder,training,train_files)
            print('condor_submit condor.sub')
            os.popen('condor_submit condor.sub')
            #os.popen("python tree_skimmer.py " + sample.label + " " + str(i) + " " + ",".join( e for e in files_list[split*i:split*(i+1)]))
            print("python tree_skimmer.py " + sample.label + " " + str(i) + " " + files_selected + " " + str(final_folder)+" "+str(training))
