import matplotlib.pyplot as plt
import numpy as np

def plot_colors(data, label_x, label_y):
    data = np.array(data)
    fig, ax = plt.subplots(figsize=(8,6))
    ax.imshow(data, cmap='binary',interpolation='nearest')
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.add_patch(plt.Rectangle((j*2-0.5, i), 2, 1, color='red' if data[i, j] == 0 else 'green'))
    for y in range(data.shape[0]+1):
        ax.hlines(y, -0.5, data.shape[1]*2, color='black', linewidth=1)
    for x in np.arange(-0.5,len(label_x)*2,2):#range(data.shape[1]+1):
        ax.vlines(x, 0, data.shape[0], color='black', linewidth=1)

    # Generate an array of locations for the x-axis labels
    xtick_locs = np.arange(0.5,len(label_x)*2,2)
    # Set the x-axis labels
    ax.set_xticks(xtick_locs)
    ax.set_xticklabels(label_x)

    # Generate an array of locations for the y-axis labels
    ytick_locs = np.arange(0.5,len(label_y),1)
    # Set the y-axis labels
    ax.set_yticks(ytick_locs)
    ax.set_yticklabels(label_y)
    ax.set_xlim(-0.5, data.shape[1]*2-0.5)
    ax.set_ylim(0, data.shape[0])
    #ax.grid(True, which='both', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.savefig("trygrid.png")
    

data = np.zeros((25,12))#[[0, 1, 0], [1, 0, 1], [0, 1, 0]]
label_x = [25,50,75,100,125,150,175,200,250,350,450,500]
label_y = np.arange(600,3100,100)#[600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000]
#data[0][0]=1

#data[0][4]=1

#data[7][10]=1
# primo numero riga Mt secondo numero colonna Mh
#MT1000_MH125
#file1="2016samples_preVFP.txt"
file1="2016samples_postVFP.txt"
#file1="2017samples.txt"
#file1="2018samples.txt"

for i in label_x:
    for j in label_y:
        string = "MT"+str(j)+"_MH"+str(i)
        #print(string)
        with open(file1) as file:
            for line in file:
                #print(line)
                if string == line.split("LH_")[1].split("_TuneCP5")[0]:
                    #print("found")
                    data[list(label_y).index(j)][list(label_x).index(i)]=1

plot_colors(data, label_x, label_y)
