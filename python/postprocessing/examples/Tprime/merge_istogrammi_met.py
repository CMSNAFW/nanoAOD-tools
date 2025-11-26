
import glob
import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", dest="label", type=str, required=True)
options = parser.parse_args()

label = options.label


inputs = glob.glob(f"/eos/user/f/fscrivan/faseII/prova/hist_regioni_prova_{label}_*.root")


outfile = f"/eos/user/f/fscrivan/faseII/prova/uniti/histOut_prova_{label}.root"

if not inputs:
    print(f"❌ Nessun file da unire per {label}")
    exit(1)

print(f"📂 Unisco {len(inputs)} file in {outfile}")
result = subprocess.run(["hadd", "-f", outfile] + inputs)

if result.returncode != 0:
    print("❌ Errore durante il merge, i file non sono stati spostati.")
    exit(1)
"""
# 🔧 Path di destinazione per i file originali
destination_base = "eos/user/f/fscrivan/istogrammi/"  # Cambia questo path come preferisci
movedir = os.path.join(destination_base, f"merged_inputs_{label}")
os.makedirs(movedir, exist_ok=True)
# 📦 Sposta i file nella nuova cartella
for f in inputs:
    os.rename(f, os.path.join(movedir, os.path.basename(f)))

print(f"✅ Merge completato. File originali spostati in {movedir}")

import glob
import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-l", dest="label", type=str, required=True)
options = parser.parse_args()

label = options.label
inputs = []   # lista unica per accumulare tutti i file

# Loop da 0 a 19
for i in range(20):
    inputs.extend(glob.glob(f"/eos/user/f/fscrivan/istogrammi/hist_regioni_hlt_{label}_{i}.root"))

outfile = f"/eos/user/f/fscrivan/new_hlt/histOut_{label}.root"

if not inputs:
    print(f"❌ Nessun file da unire per {label}")
    exit(1)

print(f"📂 Unisco {len(inputs)} file in {outfile}")
result = subprocess.run(["hadd", "-f", outfile] + inputs)

if result.returncode != 0:
    print("❌ Errore durante il merge, i file non sono stati spostati.")
    exit(1)
"""