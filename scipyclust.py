# -*-coding:utf-8 -*-

import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np
import matplotlib.pylab as plt

disMat = np.genfromtxt('../diff5000dropcomma.txt', delimiter=',', filling_values=np.nan)
Z=sch.linkage(disMat,method='average')

P=sch.dendrogram(Z)
plt.savefig('plot_dendrogram.png')
cluster= sch.fcluster(Z, 'inconsistent', t=1)
print "Original cluster by hierarchy clustering:\n",cluster