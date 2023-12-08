from os import path
import math
import json

year="2017"
path = "SF_" + year + "v6.json"
with open(path,"r") as json_file:
    SFs = json.load(json_file)
print(' \\begin{table}[h!] \n \\resizebox{\columnwidth}{!}{ \n \\begin{tabular}{|c|c|c|c|} \n \hline \n & SF & $\Delta$ SF & Backgrounds  \\\ \hline \n Top True (el) & '+str(round(SFs["SF_TT_Te"][0],2))+' & '+str(round(SFs["SF_TT_Te"][1],2)-round(SFs["SF_TT_Te"][0],2))+' & $t\\bar{t}$, ST  \\\ \n Top Other (el) &  '+str(round(SFs["SF_WJ_e"][0],2))+' & '+str(round(SFs["SF_WJ_e"][1],2)-round(SFs["SF_WJ_e"][0],2))+'  & $t\\bar{t}$, ST, Wjets \\\ \n QCD (el) & 1 & 0 & QCD \\\ \n Top True ($\mu$) &  '+str(round(SFs["SF_TT_Tm"][0],2))+' & '+str(round(SFs["SF_TT_Tm"][1],2)-round(SFs["SF_TT_Tm"][0],2))+'  & $t\\bar{t}$, ST  \\\ \n Top Other ($\mu$) &  '+str(round(SFs["SF_WJ_m"][0],2))+' & '+str(round(SFs["SF_WJ_m"][1],2)-round(SFs["SF_WJ_m"][0],2))+' & $t\\bar{t}$, ST, Wjets \\\ \n QCD ($\mu$) &  '+str(round(SFs["SF_QCD_m"][0],2))+' & '+str(round(SFs["SF_QCD_m"][1],2)-round(SFs["SF_QCD_m"][0],2))+'  & QCD \\\ \n FatJet2q1b (pass) &  '+str(round(SFs["SF_TTFJ"][0],2))+' & '+str(round(SFs["SF_TTFJ"][1],2)-round(SFs["SF_TTFJ"][0],2))+'  & $t\\bar{t}$, ST \\\ \n FatJet2q (pass) &  '+str(round(SFs["SF_TT2q"][0],2))+' & '+str(round(SFs["SF_TT2q"][1],2)-round(SFs["SF_TT2q"][0],2))+' &  $t\\bar{t}$, ST\\\ \n FatJetOther (pass) &  '+str(round(SFs["SF_Oth"][0],2))+' & '+str(round(SFs["SF_Oth"][1],2)-round(SFs["SF_Oth"][0],2))+'  & All \\\ \n FatJet2q1b (fail) &  '+str(round(SFs["SF_TTFJV"][0],2))+' & '+str(round(SFs["SF_TTFJV"][1],2)-round(SFs["SF_TTFJV"][0],2))+'  & $t\bar{t}$, ST \\\ \n FatJet2q (fail) &  '+str(round(SFs["SF_TT2qV"][0],2))+' & '+str(round(SFs["SF_TT2qV"][1],2)-round(SFs["SF_TT2qV"][0],2))+'  &  $t\\bar{t}$, ST\\\ \n FatJetOther (fail) &  '+str(round(SFs["SF_OthV"][0],2))+' & '+str(round(SFs["SF_OthV"][1],2)-round(SFs["SF_OthV"][0],2))+'  & All \\\ \n $\\alpha$ &  '+str(round(SFs["alpha"][0],2))+' & '+str(round(SFs["alpha"][1],2)-round(SFs["alpha"][0],2))+'  & All \\\ \n $\\beta_{el}$ &  '+str(round(SFs["betae"][0],2))+' & '+str(round(SFs["betae"][1],2)-round(SFs["betae"][0],2))+'  & All  \\\ \n $\\beta_{\mu}$ &  '+str(round(SFs["betam"][0],2))+' & '+str(round(SFs["betam"][1],2)-round(SFs["betam"][0],2))+'  & All \\\ \n \hline \n \end{tabular} \n } \n %\label{tab:topsf} \n \caption{Top tagger and ParticleNet tagger scale factors and related uncertainties determined from the fit in the control regions in '+year+'} \n \label{tab:topsf_'+year+'} \n \end{table}\n')