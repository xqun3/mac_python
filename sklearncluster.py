# -*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances


# Plot clustering results

D = np.loadtxt('diff5000.txt', delimiter=',')
model = AgglomerativeClustering(n_clusters=4,
                                linkage="complete", affinity="precomputed")
model.fit(D)
plt.figure()
plt.axes([0, 0, 1, 1])
for l, c in zip(np.arange(model.n_clusters), 'rgbk'):
    plt.plot(D[model.labels_ == l].T, c=c, alpha=.5)
plt.axis('tight')
plt.axis('off')
plt.suptitle("AgglomerativeClustering(affinity=precomputed)", size=20)


plt.show()
