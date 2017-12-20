# -*- coding:utf-8 -*-

import os
from libtbx import easy_pickle
from scitbx.array_family import flex

class represent_pdb:
	def __init__(self,code,cluster):
        self.code = code
        self.cluster = cluster
        
def file_name(file_dir):
	root_list = []
	file_ist = []
	for root, dirs, files in os.walk(file_dir):
		print root
		print files


#pdb_list = []
