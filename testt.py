# -*- coding:utf-8 -*-

from libtbx import easy_pickle
import numpy as np

def restore_correlation_matrix():
	file=open('diff5000.txt')
	N=5000  #?
	correlation_matrix=[]
	for ii in range(N-1):
		file_line=file.readline()
		data_list=file_line.split('\n')[0].split(',')
		correlation_list=[]
		M=len(data_list)
		for jj in range(M):
			print data_list[jj]
			correlation_list.append(float(data_list[jj].split('e')[0])*pow(10,(7+float(data_list[jj].split('e')[1]))))
			print correlation_list[ii][jj]
		correlation_matrix.append(correlation_list)
	file.close()
	return correlation_matrix

if __name__=='__main__':
	restore_correlation_matrix()