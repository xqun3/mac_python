# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from libtbx import easy_pickle 


#np.set_printoptions(precision=11, suppress=True)
import scipy.spatial.distance as ssd
# convert the redundant n*n square matrix form into a condensed nC2 array

D = np.load('diff_500_np.npy')
#D = np.loadtxt('diff5000.txt', delimiter=',')
# distArray[{n choose 2}-{n-i choose 2} + (j-i-1)] is the distance between points i and j

distArray = ssd.squareform(D) 

print distArray
Z = linkage(distArray, method='single')

max_d = 0.0000135
#print D[3546]
plt.figure(figsize=(35, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')

def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.8g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

fancy_dendrogram(
    Z,
    truncate_mode='lastp',
    p=20,
    leaf_font_size=12.,
    show_contracted=True,
    annotate_above=0.00001,  # useful in small plots so annotations don't overlap
    max_d=max_d
)



clusters = fcluster(Z, max_d, criterion='distance')
print len(clusters)
print clusters

group_flag = [0 for i in range(len(clusters))]

codes = easy_pickle.load('~/Desktop/pisadb/pisaDB.codes')
pdbcodes = codes[:500]
for ii in range(500):
	pdbcodes[ii]=pdbcodes[ii]+'.pdb'
count = 0
file = []
for i,cluster in enumerate(clusters):
	if(group_flag[cluster] == 0):
		print group_flag[cluster]
		group_flag[cluster] = 1
		count = count +1
		print count
		#os.system('mkdir group%d' % cluster)
		#os.system('touch group%d/group%d.txt' % (cluster,cluster))
		#file[i]=open('group%d/group%d.txt' % (cluster,cluster),'a')
		#file[i].write(pdbcodes[i])
		#file[i].write('\n')
		#os.system('cp /mnt/data2/ycshi/transfer/pisa/{} group{}'.format(pdbcodes[i],cluster))
	else:
		print group_flag[cluster]
		#file[i].write(pdbcodes[i])
		#file[i].write('\n')
		#os.system('cp /mnt/data2/ycshi/transfer/pisa/{} group{}'.format(pdbcodes[i],cluster))



#plt.show()
plt.savefig('cluster_hy_f01.png', bbox = 'tight')