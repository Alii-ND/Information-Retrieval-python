import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
# load dataset
pima = pd.read_csv("data.csv",  names=col_names)
N = 40


lab1=[]
lab0=[]

for i in range(N):
    if pima['label'][i] == 0:
        lab0.append(pima['cosine'][i])
        lab1.append(0)
    else:
        lab1.append(pima['cosine'][i])
        lab0.append(0)
    

ind = np.arange(N) # the x locations for the groups
width = 0.8
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax1=ax.bar(ind, lab1, width, color='g')
ax2=ax.bar(ind, lab0, width, color='r')
ax.set_ylabel('Scores')
ax.set_title('Scores')
ax.set_xticks(ind, range(N))
ax.set_yticks(np.arange(0, 1, 0.1))
ax.legend(labels=['1', '0'])
for r1, r2 in zip(ax1, ax2):
    h1 = r1.get_height()
    h2 = r2.get_height()
    if h1 != 0:
        plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%.02f" % h1, ha="center", va="bottom", color="white", fontsize=6, fontweight="bold")
    if h2 != 0:
        plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%.02f" % h2, ha="center", va="bottom", color="white", fontsize=6, fontweight="bold")

plt.show()

