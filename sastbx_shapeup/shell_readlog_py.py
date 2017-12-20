# -*- coding:utf-8 -*-

import datetime
import numpy as np
import model_clsss
import os

def read_log(name, path, wronglist):
	cluster_num = 0
	temp_cluster_mean = 0 
	with open(path + '/' + name, "rb") as log:
		all_lines = log.readlines()
		# print log.read(1)
		# if not first:
		# 	print(name)
		# 	RMAX=0
		# 	find_RMAX=0
		# 	cluster_num=0
		# 	cluster_mean_cc=0
		# 	mean_cc=0 
		# 	wronglist.append((path.split('/')[-3], path.split('/')[-1], name))
		# 	# return -1

		if all_lines:
			for line in all_lines:
				#print path + '/' + name
				line = line.strip()
				temp = line.split()
				#print temp
				#print len(temp)
				if line.startswith('cluster'):
					cluster_num += 1
					# print 'yes'
					temp_max = float(temp[-1])
					# print temp_max
					if temp_max > temp_cluster_mean:
						temp_cluster_mean = temp_max
					# print temp_cluster_mean
				elif line.startswith('mean cc'):
					mean_cc =  temp[-1]
					#print mean_cc
				elif line.startswith('Rmax'):
					RMAX=float(temp[-1])
					find_RMAX = float(temp[-2])
					#print RMAX,find_RMAX

		else:
			print(name)
			RMAX=0
			find_RMAX=0
			cluster_num=0
			cluster_mean_cc=0
			mean_cc=0 
			wronglist.append((path.split('/')[-3], path.split('/')[-1], name))
		

			# print 'why'
			# print flag

			
		# if cluster_num > 1:
		# 	cluster_mean_cc = temp_cluster_mean/cluster_num
		# else:
		# 	cluster_mean_cc = temp_cluster_mean
		cluster_mean_cc = temp_cluster_mean
	# ID = name.split('.')[0]
	ID = name.split('_')[0]
	# print ID
	print cluster_mean_cc
	# print temp_cluster_mean
	data = model_clsss.model_search(ID,cluster_num,cluster_mean_cc,mean_cc,RMAX,find_RMAX)
	return data

if __name__ == '__main__':
	t0 = datetime.datetime.now()
	file_names = []
	wronglist = []
	wrong = 0
	root_path = '/Users/dongxq/Desktop/refinew/'
	process_file = 'dammin60000'
	file_path = root_path + process_file + '/'
	print file_path
	for dir_path1, dir_name1, file_name1 in os.walk(file_path):
		
		# name = ''.join(file_name)
		file_names.append(dir_name1)

	print file_names[0] #dimmin_o,dammmin_n
	for file_name in file_names[0]:
		second_path = file_path+''.join(file_name)+'/run'
		print second_path
		names = []
		for dir_path2, dir_name2, file_name2 in os.walk(second_path):
			
			# name = ''.join(file_name)
			names.append(dir_name2)
		#names = names[0][1:]
		print names[0] # 1,2,3,4,5,6,7,8,9,10
		if(names[0][0] == ".DS_Store"):
			names[0] = names[0][1:]

		# print len(names[0])

		for name in names[0]:
			model_list = []
			
			print name
			third_path = second_path + '/' + str(name) 
			print third_path
			txt_names = []
			for dir_path3, dir_name3, file_name3 in os.walk(third_path):
				txt_names.append(file_name3)
				print txt_names[0]
			if(txt_names[0][0] == ".DS_Store"):
				txt_names[0] = txt_names[0][1:]
			for txt_name in txt_names[0]:
				print txt_name
				# if read_log(txt_name, third_path, wronglist) == -1:
				# 	print '-1'
				# 	wrong += 1
				# 	wronglist.append((name,txt_name))
			
				data = read_log(txt_name, third_path, wronglist)
				# print name +' ' + data.ID + ' ' + str(data.RMAX)
				model_list.append(data)
				
			np.save('{}_{}_model_list.npy'.format(file_name, name),model_list)
			#np.save('wronglist.npy',wronglist)
			

	t1 = datetime.datetime.now()
	with open('%s_wronglist.txt'%process_file, 'w') as f:
		f.write(str(wronglist))	
	print wronglist
	print len(wronglist)
	print "time used " + str(t1-t0)


	# t0 = datetime.datetime.now()
	# model_list = []
	# names = []
	# for dir_path, dir_name, file_name in os.walk('/Users/dongxq/Desktop/dammin_o/shell_run2/'):
		
	# 	# name = ''.join(file_name)
	# 	names.append(file_name)
	# names = names[0][1:]
	# print names
	# print names
	# print len(names)
	# for name in names:
	# 	print name
	# 	data = read_log(name)
	# 	print name +' ' + data.ID + ' ' + str(data.RMAX)
	# 	model_list.append(data)
	# np.save('dammin_top5_model_list.npy',model_list)
	
	# t1 = datetime.datetime.now()
	# print "time used " + str(t1-t0)