# -*- coding:utf-8 -*-

import os
import multiprocessing
import time
import model_clsss	

#dir_path, dir_name, file_name  = os.walk('bioisis')
'''
print os.getcwd()
os.chdir('/Users/dongxq/Desktop/bioisis_model')
print os.getcwd()
names = []
for dir_path, dir_name, file_name in os.walk('/Users/dongxq/Desktop/bioisis_model'):
	
	# name = ''.join(file_name)
	names.append(file_name)
	
names[0] = names[0][1:]
print names[0]
print len(names[0]) 
for name in names[0]:
	#name = ''.join(name)
	print name 
	os.system('mkdir %s_folder' % name)

for name in names[0]:
	print 'unzip {} -d {}_folder'.format(name, name)
	os.system('unzip {} -d {}_folder'.format(name, name))

grep 'cluster  # ' log.txt|awk 'NR==1{print $3}' >test




def func(msg):
  for i in xrange(3):
    print msg
    time.sleep(1)
if __name__ == "__main__":
  pool = multiprocessing.Pool(processes=4)
  for i in xrange(10):
    msg = "hello %d" %(i)
    pool.apply_async(func, (msg, ))
  pool.close()
  pool.join()
  print "Sub-process(es) done."
'''

import multiprocessing
import time
import numpy as np
import model_clsss		

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
  	
  	os.system('sastbx.shapeup target=/Users/dongxq/Desktop/dammin/{}/iofq_data_file.dat rmax={} pdb=/Users/dongxq/Desktop/dammin/{}/average_dammin_model.pdb |grep \'parameters \|   Best rmax found \|cluster  #\|mean cc\' > /Users/dongxq/Desktop/first_run/{}log'.format(name,RMAX,name,name))
  	#os.chdir('/Users/dongxq/Desktop/first_run/')
  	mean_cc = os.popen('grep \'mean cc:\' /Users/dongxq/Desktop/first_run/%slog|awk \'NR==1{print $3}\''% name).read()
  	find_RMAX = os.popen('grep \'   Best\' /Users/dongxq/Desktop/first_run/%slog|awk \'NR==1{print $5}\''% name).read()
  	cluster_num = os.popen('grep \'cluster  #\' /Users/dongxq/Desktop/first_run/%slog|wc -l'% name).read()
  	cluster_mean_cc = os.popen('grep \'cluster  #\' /Users/dongxq/Desktop/first_run/%slog|awk \'NR==1{print $5}\''% name).read()
  	print mean_cc,cluster_num,cluster_mean_cc
  	ID = name.split('_')[0]
  	print ID
  	data = model_clsss.model_search(ID,cluster_num,cluster_mean_cc,mean_cc,RMAX,find_RMAX.replace("\n", ""))
	'''
  	find_RMAX = os.popen('grep \'   Best\' {}log|awk \'NR==1{print $5}\''.format(name))
  	mean_cc = os.popen('grep \'mean cc:\' {}log|awk \'NR==1{print $3}\''.format(name))
  	cluster_num = os.popen('grep \'cluster  #\' {}log|wc -l'.format(name))
  	cluster_mean_cc = os.popen('grep \'cluster  #\' {}log|awk \'NR==1{print $5}\''.format(name))
  	print mean_cc,cluster_num,cluster_mean_cc
  	return RMAX,int(find_RMAX)
	''' 	
	#return RMAX,float(find_RMAX.replace("\n", ""))
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
	for name in names[0]:
		print name
		data = search_pdb(name)
		print name +' ' + data.ID + ' ' + str(data.RMAX)
		model_list.append(data)
		#RMAX_list.append()
	np.save('model_list.npy',model_list)
	t1 = time.time()
	print "time used %e seconds"%(t1-t0)
'''
	print 'DMAX \n'
	print DMAX
	print 'RMAX \n'
	print RMAX
'''
'''
	pool = multiprocessing.Pool(processes=4)
	for name in names:
	    
	    pool.apply_async(func, (msg, ))
	pool.close()
	pool.join()
	print "Sub-process(es) done."

'''
'''
os.system('sastbx.shapeup target=../76_folder/iofq_data_file.dat rmax=40 pdb=../76_folder/pdb_model.pdb |grep \'cluster  #\|mean cc\' > log')
Dmax = os.popen('grep \'DMAX\' \'/Users/dongxq/Desktop/76_folder/summary.txt\' | awk \'NR==1{print $2}\' ').read()
print Dmax


find_RMAX = os.popen('grep \'   Best\' \'/Users/dongxq/Desktop/first_run/{}log\'|awk \'NR==1{print $5}\''.format('2_folder'))

'''