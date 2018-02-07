# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
import plot_one_map as pom

def draw_mean(args):
	pos_distance_map = np.load(args[0])
	neg_distance_map = np.load(args[1])
	# pos_mean_map = np.zeros(pos_distance_map.shape[0])
	# neg_mean_map = np.zeros(pos_distance_map.shape[0])

	pos_mean = np.mean(pos_distance_map, axis=0)
	neg_mean = np.mean(neg_distance_map, axis=0)
	# print(mean)
	pom.draw_map([pos_mean,args[2],args[4]])
	pom.draw_map([neg_mean,args[3],args[4]])

def find_pos_map(args):
	ssbond = np.load(args[0])
	ssbond_id = np.load(args[1])
	find_pos = [args[2],args[3]]
	assert len(ssbond) == len(ssbond_id),'ssbond map does not equal to ssbond id'
	ssbond_pos_ord = [None for i in range(len(ssbond_id))]
	for i in range(len(ssbond_id)):
		ssbond_pos_ord[i] = [filter(str.isdigit,ssbond_id[i][0]),filter(str.isdigit,ssbond_id[i][1])]
	mmap = ssbond[ssbond_pos_ord.index(find_pos)]
	pom.draw_map([mmap,find_pos])

def draw_all_map(args):
	ssbond = np.load(args[0])
	ssbond_id = np.load(args[1])
	assert len(ssbond) == len(ssbond_id),'ssbond map does not equal to ssbond id'
	ssbond_pos_ord = [None for i in range(len(ssbond_id))]
	for i in range(len(ssbond_id)):
		ssbond_pos_ord[i] = [filter(str.isdigit,ssbond_id[i][0]),filter(str.isdigit,ssbond_id[i][1])]
	for mapi in range(ssbond.shape[0]):
		pom.draw_map([ssbond[mapi],ssbond_pos_ord[mapi],args[2]])

def draw_train_map(args):
	ssbond = np.load(args[0])
	for mapi in range(ssbond.shape[0]):
		pom.draw_map([ssbond[mapi],str(mapi),arg[1]])

if __name__ == '__main__':
	args = sys.argv[1:]
	# find_pos_map(args)
	draw_all_map(args)
	# draw_train_map(args)
	# for i in range()
	# compare_matrx(args)