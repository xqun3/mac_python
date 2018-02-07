from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import sys
from sklearn import preprocessing

def normalization_map(args):
	training_pos_data = np.load('/Users/dongxq/Desktop/disulfide/noSG_neuro_input/pos_noSG_distance_ssbond.npy')
	training_neg_data = np.load('/Users/dongxq/Desktop/disulfide/noSG_neuro_input/12496_neg_noSG_distance_ssbond.npy')
	training_data = np.concatenate((training_pos_data,training_neg_data)).reshape((len(training_pos_data)+len(training_neg_data)),-1)
	print(training_data.shape)
	scaler = preprocessing.StandardScaler().fit(training_data)
	name = args[0].split('.')[0]
	print(scaler.mean_)
	data = np.load(args[0])
	data = data.reshape(data.shape[0],-1)
	print(data.shape)
	data_scaled = scaler.transform(data)
	data_scaled = data_scaled.reshape(data_scaled.shape[0],10,10)
	np.save('/Users/dongxq/Desktop/disulfide/noSG_predict_test/nor_%s.npy'%name,data_scaled)
	# np.save('/Users/dongxq/Desktop/disulfide/noSG_neuro_input/nor_%s.npy'%name,data_scaled)
	

if __name__ == '__main__':
	args = sys.argv[1:]
	normalization_map(args)