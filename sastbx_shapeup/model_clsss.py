# -*- coding:utf-8 -*-

class model_search(object):
	"""docstring for model_search"""
	def __init__(self,ID, cluster_num, cluster_mean_cc, mean_cc, RMAX, find_rmax):
		self.ID = ID
		self.cluster_num = cluster_num
		self.cluster_mean_cc = cluster_mean_cc
		self.mean_cc = mean_cc
		self.RMAX = RMAX
		self.find_rmax = find_rmax