# -*-coding:utf-8-*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import plot_cordinate_map
import sys


def find_cord(args):
	ssbond_cord = np.load(args[0])
	ssbond_cord_id = np.load(args[1])

	find_cord_pos = [args[4],args[5]]
	print('find ssbond pos is :',find_cord_pos)
	print(args)

	assert len(ssbond_cord) == len(ssbond_cord_id),'cord length does not equal to cord id'

	ssbond_pos_ord = [None for i in range(len(ssbond_cord))]
	for i in range(len(ssbond_cord_id)):
		ssbond_pos_ord[i] = [filter(str.isdigit,ssbond_cord_id[i][0]),filter(str.isdigit,ssbond_cord_id[i][1])]

	cord = ssbond_cord[ssbond_pos_ord.index(find_cord_pos)]

	return cord

if __name__ == '__main__':
	args = sys.argv[1:]
	# find_cord(args)
	# w_cord_map, m_cord_map, find_cord_pos = plot_cordinate_map.find_cord(args)

	data = np.load(args[0])
	print(data[int(args[1])])
