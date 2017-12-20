# -*-coding:utf-8 -*-

from sklearn.cluster import AgglomerativeClustering
import numpy as np
import scipy.spatial.distance as ssd
from sklearn.cluster import DBSCAN

D = np.load('../diff_500_np.npy')
distArray = ssd.squareform(D) 

'''
ac = AgglomerativeClustering(n_clusters=100,affinity='precomputed',linkage='complete')
y_ac = ac.fit_predict(distArray)

print y_ac
print len(y_ac)

print ac.children_
print ac.n_components_


'''

db = DBSCAN(eps=0.0000015,min_samples=2,metric='precomputed')
y_db = db.fit_predict(distArray)
y_center = db.core_sample_indices_

print y_db
print len(y_db)
print y_center
print len(y_center)
