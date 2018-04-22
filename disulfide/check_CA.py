# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# data = np.load('/Users/dongxq/Desktop/disulfide/noSG_neuro_input/pos_noSG_distance_ssbond.npy')
count = 0
# data1 = np.load('/Users/dongxq/Desktop/disulfide/neuro_input/full_ssbond_distance_map.npy')
data1 = np.load('/Users/dongxq/Desktop/disulfide/checkCA/new_pos_cord.npy')
data2 = np.load('/Users/dongxq/Desktop/disulfide/checkCA/new_pos_cord_distance.npy')

print len(data1),len(data2)
with open('check_ca.txt','w') as wf:
	for i in range(len(data2[:,1,6])):
		# print i
		if data2[i,1,6] == 0:
			count += 1
			print i
			print data1[i]
			# np.savetxt(wf, data2[i])
			wf.write('\n')
print count
plt.hist(data2[:,1,6],bins=np.arange(0,10,0.5))
plt.show()

