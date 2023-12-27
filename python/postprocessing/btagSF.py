import ROOT
import os
from correctionlib import _core

def getReader(wp, readers, verbose):
    """
    Get btag scale factor reader.
    Convert working points: input is 'L', 'M', 'T', 'shape_corr' to 0, 1, 2, 3
    """
    wp_btv = {"l": 0, "m": 1, "t": 2,"shape_corr": 3}.get(wp.lower(), None)
    if wp_btv is None or wp_btv not in list(readers.keys()):
        if verbose > 0:
            print("WARNING: Unknown working point '%s', setting b-tagging SF reader to None!" % wp)
            return None
    return readers[wp_btv]

def getFlavorBTV(flavor, verbose=False):
    '''
    Maps hadronFlavor to BTV flavor:
    Note the flavor convention: hadronFlavor is b = 5, c = 4, f = 0
    Convert them to the btagging group convention of 0, 1, 2
    '''
    flavor_btv = None
    if abs(flavor) == 5:
        flavor_btv = 5
    elif abs(flavor) == 4:
        flavor_btv = 4
    elif abs(flavor) in [0, 1, 2, 3, 21]:
        flavor_btv = 0
    else:
        if verbose > 0:
            print( "WARNING: Unknown flavor '%s', setting b-tagging SF to -1!" % repr(flavor))
        return -1.
    #print("check_the_flavour!!!")
    return flavor_btv


def getSFs(jet_data, syst, reader, measurement_type='auto', shape_corr=False):
    for idx, (pt, eta, flavor_btv, discr) in enumerate(jet_data):
        epsilon = 1.e-3
        max_abs_eta = 2.4
        if eta <= -max_abs_eta:
            eta = -max_abs_eta + epsilon
        if eta >= +max_abs_eta:
            eta = +max_abs_eta - epsilon
        # evaluate SF
        sf = None
        
        if shape_corr:
            #sf = reader.eval_auto_bounds('central', flavor_btv, eta, pt, discr)
            sf = reader.evaluate("central", flavor_btv, abs(eta), pt, discr)
        
        # check if SF is OK
        if sf < 0.01:
            sf = 1.
        yield sf

def btagSFProducer(jet_pt, jet_eta, jet_hadronFlavour, jet_score, label, algo='deepJet', selectedWPs=['shape_corr'], sfFileName=None, verbose=1, jesSystsForShape=[""]):

    #inputFilePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/btagSF/"

    supported_btagSF = {
        'deepJet': {
            '2016preVFP_UL': {
                'inputFileName': "DeepJet_106XUL16preVFPSF.csv",
                    'measurement_types': {
                        0: "comb",  # b
                        1: "comb",  # c
                        2: "incl"   # light
                    },
                    'supported_wp': ["shape_corr"]
                },


            '2016postVFP_UL': {
                'inputFileName': "DeepJet_106XUL16postVFPSF.csv",
                    'measurement_types': {
                        0: "comb",  # b
                        1: "comb",  # c
                        2: "incl"   # light
                    },
                    'supported_wp': ["shape_corr"]
                },

            '2017_UL': {
                'inputFileName': "DeepJet_106XUL17SF.csv",
                    'measurement_types': {
                        0: "comb",  # b
                        1: "comb",  # c
                        2: "incl"   # light
                    },
                    'supported_wp': ["shape_corr"]
                },

            '2018_UL': {
                'inputFileName': "DeepJet_106XUL18SF.csv",
                    'measurement_types': {
                        0: "comb",  # b
                        1: "comb",  # c
                        2: "incl"   # light
                    },
                    'supported_wp': ["shape_corr"]
                }
            }
        }

    if "2016" in label:
        if "pre" in label: era= "2016preVFP_UL"
        else: era= "2016postVFP_UL"
    if "2017" in label: era = "2017_UL"
    if "2018" in label: era = "2018_UL"

    max_abs_eta = 2.4
    supported_algos = [algo]
    inputFileName = supported_btagSF[algo][era]['inputFileName']
    measurement_types = supported_btagSF[algo][era]['measurement_types']
    supported_wp = supported_btagSF[algo][era]['supported_wp']

    #for library in ["libCondFormatsBTauObjects", "libCondToolsBTau"]:
    #    if library not in ROOT.gSystem.GetLibraries():
    #        print("Load Library '%s'" % library.replace("lib", ""))
    #        ROOT.gSystem.Load(library)

    # define systematic uncertainties
    systs = []
    central_and_systs = ["central"]
    central_and_systs_shape_corr = ["central"]
    #print(algo,os.path.join(inputFilePath, inputFileName))
    #print(type(algo),type(os.path.join(inputFilePath, inputFileName)))
    #calibration = ROOT.BTagCalibration(algo, os.path.join(inputFilePath, inputFileName))
    btvjson = _core.CorrectionSet.from_file(os.path.join("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/", era, "btagging.json.gz"))
    
    """
    readers = {}
    for wp in selectedWPs:
        wp_btv = {"l": 0, "m": 1, "t": 2,"shape_corr": 3}.get(wp.lower(), None)
        syts = None
        systs = systs_shape_corr
        v_systs = getattr(ROOT, 'vector<string>')()
        for syst in systs:
            v_systs.push_back(syst)
        reader = ROOT.BTagCalibrationReader(wp_btv, 'central', v_systs)
        for flavor_btv in [0, 1, 2]:
            if wp == "shape_corr":
                reader.load(calibration, flavor_btv, 'iterativefit')
        readers[wp_btv] = reader
    """
    preloaded_jets = [(jet_pt, jet_eta, getFlavorBTV(jet_hadronFlavour), jet_score) ]
    reader = btvjson["%s_%s" %(algo, "shape")]
    """
    reader = getReader(wp)
    isShape = (wp == 'shape_corr')
    central_and_systs = (central_and_systs_shape_corr if isShape else self.central_and_systs)
    for central_or_syst in central_and_systs:
        scale_factors = list(getSFs(preloaded_jets, central_or_syst, reader, 'auto', isShape))
    """
    scale_factors = list(getSFs(preloaded_jets, "central", reader, 'auto', True))
    
    return scale_factors
    
