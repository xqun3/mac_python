from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import sys
import ssbond_distance_map as sdm
import math

def removeSG(nparray,name):
	new_data = np.zeros((nparray.shape[0],10,3))
	print(new_data.shape)
	print(new_data[0])
	for i in range(nparray.shape[0]):
		for j in range(nparray.shape[1]):
			if j<5:
				new_data[i][j] = nparray[i][j][:] 
			if 5<j<11:

				new_data[i][j-1] = nparray[i][j][:] 
			if j==5 or j == 11:
				continue
	print(new_data.shape)
	print(new_data[0])
	np.save('/Users/dongxq/Desktop/disulfide/no_SG_dataset/%s_no_SG_ssbondmap.npy'%name, new_data)
	full_distance_map = sdm.convert_to_nxn_map(new_data)
	np.save('%s_noSG_distance_ssbond_.npy'%name,full_distance_map)


if __name__ == '__main__':
	args = sys.argv[1:]
	positive_data = np.load(args[0])
	negative_data = np.load(args[1])
	# assert len(positive_data) == len(negative_data),'two data length are not equal!'
	removeSG(positive_data, args[2])
	removeSG(negative_data, args[3])
	print('finish removeSG')
