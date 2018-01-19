# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import sys
import matplotlib.pyplot as plt

p_data = np.load('/Users/dongxq/Desktop/disulfide/new-ssbond-map/full_ssbond_distance_map.npy')
n_data = np.load('/Users/dongxq/Desktop/disulfide/new-nossbond-map/full_12496nossbond_distance_map.npy')

ptemp = np.zeros(p_data[0].shape)
ntemp = np.zeros(n_data[0].shape)
label = ['N','CA','C','O','CB','SG','N','CA','C','O','CB','SG']

for pmap in p_data:
	ptemp += pmap
ptemp = ptemp/p_data.shape[0]
plt.figure()
plt.title('positve mean distance map')
# ssbond_distance_map = ssd.squareform(ten_map[i]) 
plt.style.use('classic')
plt.imshow(ptemp)
plt.xticks(range(len(label)), label, size='small')
plt.yticks(range(len(label)), label, size='small')
plt.colorbar();
plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/mean_positve_distance_map.png',bbox_inches='tight')
np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/mean_positve_distance_map.npy',ptemp)

for nmap in n_data:
	ntemp += nmap
ntemp = ntemp/n_data.shape[0]
plt.figure()
plt.title('negative mean distance map')
# ssbond_distance_map = ssd.squareform(ten_map[i]) 
plt.style.use('classic')
plt.imshow(ntemp)
plt.xticks(range(len(label)), label, size='small')
plt.yticks(range(len(label)), label, size='small')
plt.colorbar();
plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/mean_negative_distance_map.png',bbox_inches='tight')
np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/mean_negative_distance_map.npy',ntemp)

diff_map = ptemp-ntemp
plt.figure()
plt.title('positive negative difference map')
# ssbond_distance_map = ssd.squareform(ten_map[i]) 
plt.style.use('classic')
plt.imshow(diff_map)
plt.xticks(range(len(label)), label, size='small')
plt.yticks(range(len(label)), label, size='small')
plt.colorbar();
plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/diif_p_n_map.png',bbox_inches='tight')

# p_amin = 10000.0
# p_amax = 0.0
# n_amin = 10000.0
# n_amax = 0.0

# for pmap in p_data:
# 	# print(pmap)
# 	pmin = np.amin(pmap)
# 	# print(pmin)
# 	pmax = np.amax(pmap) 
# 	# print(pmax)
# 	if pmin < p_amin:
# 		p_amin = pmin
# 		# print(pmin)
# 	if pmax > p_amax:
# 		p_amax = pmax

# for nmap in n_data:
# 	nmin = np.amin(nmap)
# 	nmax = np.amax(nmap) 
# 	if nmin < n_amin:
# 		n_amin = nmin
# 	if nmax > n_amax:
# 		n_amax = nmax

# print('p_amin,p_amax,n_amin,n_amax',p_amin,p_amax,n_amin,n_amax)