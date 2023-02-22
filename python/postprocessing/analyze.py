import ROOT as r
import sys
path = './'
filename = 'Wprimetotb_M2000W20_LH_all_nomadspin'
filename = 'Wprimetotb_M2000W20_LH_NP2_LE_2'
#filename = 'Wprimetotb_M2000W20_LH_noWp'
#filename = 'Wprimetotb_M2000W20_LH_all'
filename = 'Wprimetotb_M2000W20_LH_old'
filename = 'Wprimetotb_M2000W20_LH_NP2_E_4_decay'
filename = 'Wprimetotb_M2000W20_LH_NP2_G_0'
filename = 'Wprimetotb_M2000W20_LH_NP2_G_E_0_decay'
filename = sys.argv[1]

def analyzer(filename):
    rf = r.TFile.Open(filename + '.root')
    tree = rf.Get("t")
    evt = 0
    pre_evt = 0
    pre_mtb_SM = -1.
    W_SM = -1.
    b_W = r.TLorentzVector()
    b_W_SM = r.TLorentzVector()
    b_t = r.TLorentzVector()
    top = r.TLorentzVector()
    top_SM = r.TLorentzVector()
    mbb = r.TH1F("mbb", "b-jets system mass", 100, 0, 1000)
    bpt = r.TH1F("bpt", "W' b-jet pt", 60, 30.5, 120.5)  
    bpt_SM = r.TH1F("bpt_SM", "W' b-jet pt", 100, 0, 1000)  
    mtb = r.TH1F("mtb", "tb system mass", 40, 700, 900)
    mtb_SM = r.TH1F("mtb_SM", "tb system mass", 175, 0, 6000)
    q2 = r.TH1F("q2", "Q^{2} of the process", 600, 0, 6000)
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        evt = tree.event
        if not(evt == pre_evt):
            W = b_W + top
            W_SM = b_W_SM + top_SM
            bb = b_t + b_W
            mtb.Fill(W.M())
            mbb.Fill(bb.M())
            if not W_SM==pre_mtb_SM:
                mtb_SM.Fill(W_SM.M())
        if (abs(tree.id) == 25):
            if(tree.parent1 == 1 or tree.parent1 == 3):
                bpt.Fill(tree.p4.M())
                b_W.SetPtEtaPhiM(tree.p4.Pt(), tree.p4.Eta(), tree.p4.Phi(), tree.p4.M())
            if(tree.parent1 == 1):
                bpt_SM.Fill(tree.p4.Pt())
                b_W_SM.SetPtEtaPhiM(tree.p4.Pt(), tree.p4.Eta(), tree.p4.Phi(), tree.p4.M())
            else:
                b_t.SetPtEtaPhiM(tree.p4.Pt(), tree.p4.Eta(), tree.p4.Phi(), tree.p4.M())
        if (abs(tree.id) == 6):
            if(tree.parent1 == 1 or tree.parent1 == 3):
                top.SetPtEtaPhiM(tree.p4.Pt(), tree.p4.Eta(), tree.p4.Phi(), tree.p4.M())
            if(tree.parent1 == 1):
                top_SM.SetPtEtaPhiM(tree.p4.Pt(), tree.p4.Eta(), tree.p4.Phi(), tree.p4.M())
        pre_evt = tree.event
        pre_mtb_SM = W_SM
    rfout = r.TFile(filename + '_out.root', 'RECREATE')
    mbb.Write()
    mtb.Write()
    bpt.Write()
    mtb_SM.Write()
    bpt_SM.Write()
    rfout.Close()

if __name__ == "__main__":

    analyzer(path+filename)



