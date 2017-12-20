# -*- coding:utf-8 -*-

import os
import multiprocessing
import time
import model_clsss
import numpy as np

def search_pdb(name):
  	print name
  	file_list = os.listdir('/Users/dongxq/Desktop/dammin/%s'% name)
  	os.chdir('/Users/dongxq/Desktop/dammin/%s' % name)
  	if 'summary.txt' in file_list:

  		Dmax = os.popen('grep \'DMAX\' \'/Users/dongxq/Desktop/dammin/%s/summary.txt\' | awk \'NR==1{print $2}\' '% name ).read()
  	else:
  		Dmax = os.popen('grep \'DMAX\' \'/Users/dongxq/Desktop/dammin/%s/summary_file.txt\' | awk \'NR==1{print $2}\' '% name ).read()
  	RMAX = int(Dmax)/2
  	print name + '   ' + str(RMAX)
  	
  	os.system('sastbx.shapeup target=/Users/dongxq/Desktop/dammin/{}/iofq_data_file.dat rmax={} pdb=/Users/dongxq/Desktop/dammin/{}/average_dammin_model.pdb |grep \'parameters \|   Best rmax found \|cluster  #\|mean cc\' > /Users/dongxq/Desktop/parralle_run/{}log'.format(name,RMAX,name,name))
  	#os.chdir('/Users/dongxq/Desktop/first_run/')
  	mean_cc = os.popen('grep \'mean cc:\' /Users/dongxq/Desktop/parralle_run/%slog|awk \'NR==1{print $3}\''% name).read()
  	find_RMAX = os.popen('grep \'   Best\' /Users/dongxq/Desktop/parralle_run/%slog|awk \'NR==1{print $5}\''% name).read()
  	cluster_num = os.popen('grep \'cluster  #\' /Users/dongxq/Desktop/parralle_run/%slog|wc -l'% name).read()
  	cluster_mean_cc = os.popen('grep \'cluster  #\' /Users/dongxq/Desktop/parralle_run/%slog|awk \'NR==1{print $5}\''% name).read()
  	print mean_cc,cluster_num,cluster_mean_cc
  	ID = name.split('_')[0]
  	print ID
  	data = model_clsss.model_search(ID,cluster_num,cluster_mean_cc,mean_cc,RMAX,find_RMAX.replace("\n", ""))
  	return data

if __name__ == "__main__":

	t0 = time.time()
	model_list = []
	#DMAX_list = []
	#RMAX_list = []
	names = []
	for dir_path, dir_name, file_name in os.walk('/Users/dongxq/Desktop/dammin'):
		
		# name = ''.join(file_name)
		names.append(dir_name)
	
	print names[0]
	'''
	for name in names[0]:
		print name
		data = search_pdb(name)
		print name +' ' + data.ID + ' ' + str(data.RMAX)
		model_list.append()
		#RMAX_list.append()
	'''

	pool = multiprocessing.Pool(processes=4)
	for name in names[0]:
	    
	    pool.apply_async(search_pdb, (name, ))
	pool.close()
	pool.join()
	print "Sub-process(es) done."
	t1 = time.time()
	print "time used %e seconds"%(t1-t0)