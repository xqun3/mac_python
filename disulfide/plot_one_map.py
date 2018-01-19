# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matplotlib.pyplot as plt
import sys
import numpy as np
# label = ['N','CA','C','O','CB','SG','N','CA','C','O','CB','SG']
label = ['N','CA','C','O','CB','N','CA','C','O','CB']

def draw_map(args):
	if type(args[0]) == str:
		file = np.load(args[0])
	else:
		file = args[0]
	if type(args[1]) == list:
		name = args[1][0] + '_' + args[1][1]
	else:
		name = args[1]
	plt.figure()
	plt.title('%s'%name)
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(file)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	# plt.savefig('/Users/dongxq/Desktop/disulfide/ssbond_map_image/neg_image/%s.png'%name,bbox_inches='tight')
	plt.savefig('/Users/dongxq/Desktop/disulfide/noSG_predict_analysis/%s.png'%name,bbox_inches='tight')

def draw_compare_map(args):
	change_map = np.load(args[0])
	mutant_map = np.load(args[1])
	name = args[2]+'_'+args[3]
	diff_map = mutant_map - change_map


	plt.figure()
	plt.title('%s change map'%name)
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(change_map)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/%s_change_map.png'%name,bbox_inches='tight')

	plt.figure()
	plt.title('%s change difference map'%name)
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	plt.style.use('classic')
	plt.imshow(diff_map)
	plt.xticks(range(len(label)), label, size='small')
	plt.yticks(range(len(label)), label, size='small')
	plt.colorbar();
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_analysis/%s_change_diff_map.png'%name,bbox_inches='tight')

if __name__ == '__main__':

	args = sys.argv[1:]
	draw_map(args)
	
	# draw_compare_map(args)