import os
from PhysicsTools.NanoAODTools.postprocessing.samples.samples_fra import *

def get_files_string_dark(dataset):
    username = str(os.environ.get('USER'))
    inituser = str(os.environ.get('USER')[0])
    if username == 'adeiorio':
        uid = 103214
    elif username == 'acagnott':
        uid = 140541
    elif username == 'fscrivan':
        uid=172801

    """
    if not hasattr(dataset, "dataset"): 
        return "ERROR: a sample with dataset method is required"
    
    else:
    """
    #print("sta qui",dataset.dataset)
    if not os.path.exists("/tmp/x509up_u" + str(uid)):
        os.system('voms-proxy-init --rfc --voms cms -valid 192:00')
        os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")
        
    os.popen("export XRD_NETWORKSTACK=IPv4")
    #'dasgoclient -query="file dataset='+dataset.dataset+' instance=prod/phys03"'
    command = 'dasgoclient -query="file dataset='+dataset.dataset+' instance=prod/phys03"'
    #command = f'dasgoclient -query="file dataset={dataset} instance=prod/phys03"'
    #command = 'dasgoclient -query="file dataset=dataset instance=prod/phys03"'
    #command = 'dasgoclient -query="file dataset=/tDM_Mchi1MPhi200_large/oiorio-tDM_Mchi1MPhi500Run3_NANOAOD-937767ad549695a10e40fd392f6c3633/USER instance=prod/phys03" > files_mPhi500.py'
    #print("command",command)
    out_stream = os.popen(command)
    
    #out_stream = os.system(command)
    files_string = out_stream.read()
    out_stream.close()
    return files_string.split('\n')
#dataset2="/tDM_Mchi1MPhi200_large/oiorio-tDM_Mchi1MPhi500Run3_NANOAOD-937767ad549695a10e40fd392f6c3633/USER"

