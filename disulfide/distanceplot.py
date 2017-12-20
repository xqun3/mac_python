# -*-coding:utf-*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial.distance as ssd
import random

ssbond_map = np.load('/Users/dongxq/Desktop/disulfide/other_set_map/N14C-93C_full_possible_ssbond_nr.npy')
print ssbond_map.shape
# print ssbond_map[:1][0].shape
# ssbond_distance_map = ssd.squareform(ssbond_map[:1][0]) 
# print ssbond_distance_map.shape

# ten_map = random.sample(ssbond_map,10)

for i in range(len(ssbond_map)):
	# print ten_map[i]
	plt.figure()
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(ssbond_map[i])
	plt.colorbar();
	plt.savefig('%dssbond_map.png'%i)
	# plt.show()

# temp = np.zeros(ssbond_map[0].shape)
# print temp.shape
# for smap in ssbond_map:
# 	temp += smap

# print temp.shape
# # print temp/len(ssbond_map)
# # print temp/float(len(ssbond_map)).shape
# print temp

# plt.figure()
# allssbond_distance_map = ssd.squareform(temp) 
# plt.style.use('classic')
# plt.imshow(allssbond_distance_map)
# plt.colorbar();
# plt.savefig('all_ssbond_map.png')

# plt.figure()
# allmeanssbond_distance_map = ssd.squareform((temp/len(ssbond_map))) 
# plt.style.use('classic')
# plt.imshow(allmeanssbond_distance_map)
# plt.colorbar();
# plt.savefig('all_mean_ssbond_map.png')