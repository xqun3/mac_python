# -*-coding:utf-8-*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import plot_cordinate_map

if __name__ == '__main__':
	args = sys.argv[1:]
	# find_cord(args)
	w_cord_map, m_cord_map, find_cord_pos = plot_cordinate_map.find_cord(args)
	print(w_cord_map)
