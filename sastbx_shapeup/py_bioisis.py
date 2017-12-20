# -*- coding:utf-8 -*-

import datetime
import numpy as np
import model_clsss	
from sastbx.zernike_model import search_pdb
import sys
import os

def search_pdb_self(name):
	#search_pdb.run('target=../2_folder/iofq_data_file.dat','rmax=37','pdb=../2_folder/average_dammin_model.pdb')
	print name
  	file_list = os.listdir('/Users/dongxq/Desktop/dammin1/%s'% name)
  	os.chdir('/Users/dongxq/Desktop/dammin1/%s' % name)
  	if 'summary.txt' in file_list:

  		#Dmax = os.popen('grep \'DMAX\' \'/Users/dongxq/Desktop/parralle_test/%s/summary.txt\' | awk \'NR==1{print $2}\' '% name ).read()
		with open('summary.txt',"rb") as fd:
			for line in fd:
				if line.startswith('DMAX'):
					temp = line.split()
					DMAX = temp[1]


  	else:
  		#Dmax = os.popen('grep \'DMAX\' \'/Users/dongxq/Desktop/parralle_test/%s/summary_file.txt\' | awk \'NR==1{print $2}\' '% name ).read()
  		with open('summary_file.txt',"rb") as fd:
			for line in fd:
				if line.startswith('DMAX'):
					temp = line.split()
					DMAX = temp[1]
  	RMAX = int(DMAX)/2
  	print name + '   ' + str(RMAX)

  	dat = 'target=/Users/dongxq/Desktop/dammin1/%s/iofq_data_file.dat'%name
  	log = 'log_file=/Users/dongxq/Desktop/dammin1/%s/shapeuppisa.txt'%name
  	pdb = 'pdb=/Users/dongxq/Desktop/dammin1/%s/average_dammin_model.pdb'%name
  	rmax = 'rmax=%d'%RMAX
  	args = [dat,rmax,pdb, log]
  	print 'now'
  	print args
  	search_pdb.run(args)
  	#os.system('sastbx.shapeup target=/Users/dongxq/Desktop/dammin/{}/iofq_data_file.dat rmax={} pdb=/Users/dongxq/Desktop/dammin/{}/average_dammin_model.pdb |grep \'   Best rmax found \|cluster  #\|mean cc\' > /Users/dongxq/Desktop/test_run/{}log'.format(name,RMAX,name,name))
  	
  	cluster_num = 0
  	temp_cluster_mean = 0 
  	with open('/Users/dongxq/Desktop/dammin1/%s/shapeuppisa.txt'%name,"rb") as log:
  		for line in log:
  			line = line.strip()
  			if line.startswith('Rmax'):
  				temp = line.split()
  				print temp
  				find_RMAX = temp[-2]
  				print find_RMAX
  			elif line.startswith('cluster'):
  				cluster_num += 1
  				temp = line.split()
  				print temp
  				print cluster_num
  				temp_cluster_mean += float(temp[-1])
  				print temp_cluster_mean
  			elif line.startswith('mean cc'):
  				temp = line.split()
  				print temp
  				mean_cc =  temp[-1]
  				print mean_cc
  		if cluster_num > 1:
  			cluster_mean_cc = temp_cluster_mean/cluster_num
  		else:
  			cluster_mean_cc = temp_cluster_mean
  	ID = name.split('_')[0]
  	print ID
  	data = model_clsss.model_search(ID,cluster_num,cluster_mean_cc,mean_cc,RMAX,find_RMAX)

	return data

if __name__ == '__main__':
	t0 = datetime.datetime.now()
	model_list = []
	names = []
	for dir_path, dir_name, file_name in os.walk('/Users/dongxq/Desktop/dammin1'):
		
		# name = ''.join(file_name)
		names.append(dir_name)
	
	print names[0]
	for name in names[0]:
		print name
		#data = search_pdb_self(name)
		
		data = search_pdb_self(name)
		print name +' ' + data.ID + ' ' + str(data.RMAX)
		model_list.append(data)
		#RMAX_list.append()
	#os.chdir('~/Desktop/test_run/')
	np.save('pisa_10000model_list.npy',model_list)
	
	t1 = datetime.datetime.now()
	print "time used " + str(t1-t0)
	#search_pdb.run(['target=/Users/dongxq/Desktop/2_folder/iofq_data_file.dat','rmax=37','pdb=/Users/dongxq/Desktop/2_folder/average_dammin_model.pdb'])


