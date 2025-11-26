LABELS=(


  TT_hadr_2024
  TT_Semilep_2024
  TT_Dilep_2024
  ZJetsToNuNu_HT100to200_2024
  ZJetsToNuNu_HT200to400_2024
  ZJetsToNuNu_HT400to800_2024
  ZJetsToNuNu_HT800to1500_2024
  ZJetsToNuNu_HT1500to2500_2024
  ZJetsToNuNu_HT2500_2024
)

for label in "${LABELS[@]}"; do
  echo "Mergio $label"
  python3 merge_istogrammi_met.py -l "$label"
done