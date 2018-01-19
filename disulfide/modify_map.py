# -*- coding:utf-8 -*-

import numpy as np

mutant_map = np.load('/Users/dongxq/Desktop/disulfide/predict_analysis/27_79mmap.npy')
WT_map = np.load('/Users/dongxq/Desktop/disulfide/predict_analysis/27_79wmap.npy')

change_map = WT_map.copy()
for i in range(6,11):
	print i
	change_map[5][i] = mutant_map[5][i]
	change_map[i][5] = mutant_map[i][5]

np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/27_79change5_610.npy',change_map)

# change_map[11][5] = mutant_map[11][5]
# change_map[5][11] = mutant_map[5][11]

# np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/43_74change11_5.npy',change_map)
	