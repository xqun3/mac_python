# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt

def compare_matrx(args):
	mutate_ssbond = np.load(args[0])
	mutate_ssbond_id = np.load(args[1])
	wt_ssbond = np.load(args[2])
	wt_ssbond_id = np.load(args[3])
	find_ssbond_pos = [args[4],args[5]]
	print('find ssbond pos is :',find_ssbond_pos)
	print(args)

	print(len(mutate_ssbond),len(mutate_ssbond_id))
	assert len(mutate_ssbond) == len(mutate_ssbond_id),'mutate map does not equal to mutate id'
	assert len(wt_ssbond) == len(wt_ssbond_id),'wt map does not equal to wt id'

	mutate_pos_ord = [None for i in range(len(mutate_ssbond_id))]
	wt_pos_ord = [None for i in range(len(wt_ssbond_id))]
	for i in range(len(mutate_ssbond_id)):
		mutate_pos_ord[i] = [filter(str.isdigit,mutate_ssbond_id[i][0]),filter(str.isdigit,mutate_ssbond_id[i][1])]
	for i in range(len(wt_ssbond_id)):
		wt_pos_ord[i] = [filter(str.isdigit,wt_ssbond_id[i][0]),filter(str.isdigit,wt_ssbond_id[i][1])]
	
	mmap = mutate_ssbond[mutate_pos_ord.index(find_ssbond_pos)]
	wmap = wt_ssbond[wt_pos_ord.index(find_ssbond_pos)]
	# norm = matplotlib.colors.Normalize(vmin=0, vmax=10) 
	label = ['N','CA','C','O','CB','SG','N','CA','C','O','CB','SG']

	difference = mmap - wmap
	plt.figure()
	plt.title('%s difference map'%(args[4]+'_'+args[5]))
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(difference)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/%sdiff_map.png'%(args[4]+'_'+args[5]),bbox_inches='tight')

	plt.figure()
	plt.title('%s mutant distance map'%(args[4]+'_'+args[5]))
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(mmap)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/%smmap.png'%(args[4]+'_'+args[5]),bbox_inches='tight')

	plt.figure()
	plt.title('%s WT distance map'%(args[4]+'_'+args[5]))
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(wmap)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/%swmap.png'%(args[4]+'_'+args[5]),bbox_inches='tight')

	np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/%smmap.npy'%((args[4]+'_'+args[5])), mmap)
	np.save('/Users/dongxq/Desktop/disulfide/predict_analysis/%swmap.npy'%((args[4]+'_'+args[5])), wmap)


if __name__ == '__main__':
	args = sys.argv[1:]
	# print(args)
	'''
	Usage:
	python ../../python_code/disulfide/compare_structure.py 
	N14C-93C_full_possible_ssbond_nr.npy 
	N14C-93C_possible_ssbond_id_nr.npy 
	flavo_full_possible_ssbond_nr.npy 
	flavo_possible_ssbond_id_nr.npy 14 93
	'''
	compare_matrx(args)