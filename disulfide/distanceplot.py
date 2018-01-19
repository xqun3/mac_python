# -*-coding:utf-*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial.distance as ssd
import random

ssbond_map = np.load('/Users/dongxq/Desktop/disulfide/other_set_map/brilM_full_possible_ssbond_nr.npy')
ssbond_id = np.load('/Users/dongxq/Desktop/disulfide/other_set_map/brilM_possible_ssbond_id_nr.npy')
print ssbond_map.shape
mutate_pos_ord = [None for i in range(len(ssbond_id))]
for i in range(len(ssbond_id)):
	mutate_pos_ord[i] = [filter(str.isdigit,ssbond_id[i][0]),filter(str.isdigit,ssbond_id[i][1])]

label = ['N','CA','C','O','CB','SG','N','CA','C','O','CB','SG']
# print ssbond_map[:1][0].shape
# ssbond_distance_map = ssd.squareform(ssbond_map[:1][0]) 
# print ssbond_distance_map.shape

# ten_map = random.sample(ssbond_map,10)


# print mutate_pos_ord[0]

pos = ssbond_map[mutate_pos_ord.index(['79','87'])]
print pos[1][7]

plt.figure()
plt.title('%s WT distance map'%('79_87'))
# ssbond_distance_map = ssd.squareform(ten_map[i]) 
plt.style.use('classic')
plt.imshow(pos)
plt.xticks(range(len(label)), label, size='small')
plt.yticks(range(len(label)), label, size='small')
plt.colorbar();
plt.savefig('%sssbond_map.png'%'79_87',bbox_inches='tight')

'''
for i in range(len(ssbond_map)):
	# print ten_map[i]
	plt.figure()
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(ssbond_map[i])
	plt.colorbar();
	plt.savefig('%dssbond_map.png'%i)
	# plt.show()
'''

# print temp.shape
# print temp/len(ssbond_map)
# print temp/float(len(ssbond_map)).shape
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
