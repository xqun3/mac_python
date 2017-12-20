# -*- coding:utf-8 -*-

import os 
import numpy as np
import matplotlib.pyplot as plt 
import sys

def read_log(name, path, ntop):
	max_pdb = []
	max_temp = 0
	temp_list = []
	ncount = 0
	flag = True
	txt_name = ntop + '_' + name + '_log.txt'
	# print path,txt_name
	with open(path + '/' + name + '/' + txt_name, "rb") as log:
		all_lines = log.readlines()
		if all_lines:
			for line in all_lines:
				#print path + '/' + name
				line = line.strip()
				temp = line.split()
				#print temp
				#print len(temp)
				if flag:
					if line.startswith('Rank'):
						flag = False
					# for i in range(1,11):
					# 	print temp
					# 	if temp[-1] > max_pdb:
					# 		max_pdb.append(name, temp[-2], temp[-1])
				else:
					if(len(temp) > 3):
						max_pdb = [int(name.split('_')[0]), 0 , 0]
						# max_pdb = [name.split('.')[0], 0 , 0]
						break
					# print temp
					if float(temp[-1]) > max_temp:
						max_temp = float(temp[-1])
						name_temp = name
						fpdb_temp = temp[-2]
					ncount += 1
				if ncount == int(ntop):
					max_pdb.append(int(name_temp.split('_')[0]))
					# max_pdb.append(name_temp.split('.')[0])
					max_pdb.append(fpdb_temp.lower())
					max_pdb.append(max_temp)
					
					break

		else:
			# max_pdb = [name.split('.')[0], 0 , 0]
			max_pdb = [name.split('_')[0], 0 , 0]

	
	
	# print max_pdb
	return max_pdb

def fileread(root_path, process_file):
	file_path = root_path + process_file + '/'
	file_names = []
	for dir_path0, dir_name0, file_name0 in os.walk(file_path):
		file_names.append(dir_name0)

	print file_names[0] #dimmin_o,dammmin_n
	for file_name in file_names[0]:
		second_path = file_path+''.join(file_name)+'/pdb'
		print second_path
		names = []
		for dir_path1, dir_name1, file_name1 in os.walk(second_path):
			
			# name = ''.join(file_name)
			names.append(dir_name1)
		#names = names[0][1:]
		print names[0] # 1,2,3,4,5,6,7,8,9,10
		if(names[0][0] == ".DS_Store"):
			names[0] = names[0][1:]
		for name in names[0]:
			model_list = []
			
			print name
			third_path = second_path + '/' + str(name) 
			# print third_path
			txt_files = []
			for dir_path3, dir_name3, file_name3 in os.walk(third_path):
				txt_files.append(dir_name3)
			# print txt_files[0]
			if(txt_files[0][0] == ".DS_Store"):
				txt_files[0] = txt_files[0][1:]
			for txt_file in txt_files[0]:
				# print txt_file
				
				data = read_log(txt_file, third_path, name)
				# print name +' ' + data.ID + ' ' + str(data.RMAX)
				model_list.append(data)
			# print model_list
			with open( '%stop_max.txt'%name, 'a') as wf:
				wf.write('ntop = %s ----------------------------\n'%name)
				wf.write(file_name + '  ' + name + 'max list:\n')
				wf.write(str(model_list) + '\n')
			
			
			# print model_list
			np.save('{}_{}_max_list.npy'.format(name, file_name.split('_')[-1]),model_list)

def sort_model(data):
	for i in range(len(data)):
		for j in range(i,len(data)):
			# if int(data[i].ID)>int(data[j].ID):
			if data[i].ID>data[j].ID:
				temp = data[j]
				data[j] = data[i]
				data[i] = temp
			else:
				pass

def draw_line(newList, oldList, plotTilte, ntop):
	x = [i for i in range(len(newList))]
	newlistx = [newList[i][0] for i in range(len(newList))]
	# print x

	# for i in range(len(newList)):
	# 	print newList[i][0]
	plt.figure(figsize=(10,8))
	plt.title(plotTilte + ' ' + str(ntop))
	plt.plot(newList[:,2], '-o', label='highest value in new database')
	plt.plot(oldList[:,2], '-o', label='highest value in old database')
	plt.xticks(x,newlistx)
	plt.legend()
	plt.savefig('%d%smax cc.png'%(ntop,plotTilte))

def draw_hist(data, title, ntop):
	plt.figure()
	ax = plt.axes(facecolor='#E6E6E6') 
	ax.set_axisbelow(True)
	# draw solid white grid lines
	plt.grid(color='w', linestyle='solid')
	# hide axis spines
	for spine in ax.spines.values(): 
	    spine.set_visible(False)
	# hide top and right ticks
	ax.xaxis.tick_bottom()
	ax.yaxis.tick_left()
	ax.set_title('%s'%title)
	# lighten ticks and labels
	ax.tick_params(colors='gray', direction='out') 
	for tick in ax.get_xticklabels():
	    tick.set_color('gray')
	for tick in ax.get_yticklabels():
	    tick.set_color('gray')
	# control face and edge color of histogram
	ax.hist(data,bins = 30,edgecolor='#E6E6E6', color='#EE6666');
	plt.title('%s%d'%(title,ntop))
	plt.savefig('%s%d.png'%(title,ntop), bbox = 'tight')

def countNUm(newList, oldList, ntop):
	count = 0
	diff_temp = 0
	count0 = 0
	length = len(newList)
	print length
	print '-----------------'
	for i in range(length):
		# print newList[i][0],oldList[i][0]
		if newList[i][0] != oldList[i][0]:
			print 'name is different!'
			break
		if float(newList[i][2]) == 0:
			count0 += 1
			print 'nzero', newList[i][0],float(oldList[i][2]) 
			continue
		elif float(oldList[i][2]) == 0:
			count0 += 1
			print 'ozero', oldList[i][0],float(oldList[i][2])
			continue
		
		temp = float(newList[i][2]) - float(oldList[i][2])
		if temp >= 0:
			count += 1
		diff_temp += temp
	print diff_temp
	with open( 'top_max.txt', 'a') as wf:
		wf.write('***********************%s************************\n'%ntop)
		wf.write('new max cc higher than old max cc count is : %d \n'%count)
		wf.write('average diff is :%f\n'%(diff_temp/float(length-count0)))
		wf.write('zero count :%d\n'%count0)


if __name__ == '__main__':
	args = sys.argv[1:]
	print args #python ../../python_code/compare_top.py /Users/dongxq/Desktop/refinew/ dammin60000

	# root_path = '/Users/dongxq/Desktop/file/'
	# process_file = 'dammin_10000'	
	root_path = args[0]
	process_file = args[1]

	fileread(root_path, process_file)
	file_names = []
	for dir_path, dir_name, file_name in os.walk(os.getcwd()):
		# print file_name
		# print ''.join(file_name).split('.')[-1]
		# if ''.join(file_name).split('.')[-1] == 'npy':
		file_names.append(file_name)
	if file_names[0][0] == '.DS_Store':
		file_names[0] = file_names[0][1:]
	# print file_names
	num = len(file_names[0])/3
	print len(file_names[0])
	print num
	a = 0
	if num == 10:
		a = 1
	else:
		print 'yes'
		a = 10
	print a
	for i in range(a,11):
		ndata = np.load('%d_n_max_list.npy'%i)
		odata = np.load('%d_o_max_list.npy'%i)
		# ndata = ndata.tolist()
		# odata = odata.tolist()
		# for ii in range(len(ndata)):
		# 	for jj in range(ii,len(ndata)):
		# 		# if int(ndata[i][0])>int(ndata[j][0]):
		# 		if ndata[ii][0]>ndata[jj][0]:
		# 			# print ndata[i],ndata[j]
		# 			temp = ndata[jj]
		# 			ndata[jj] = ndata[ii]
		# 			ndata[ii] = temp
		# 			# print ndata[i],ndata[j]
		# 		else:
		# 			pass
		# for i_i in range(len(odata)):
		# 	for j_j in range(i,len(odata)):
		# 		# if int(odata[i][0])>int(odata[j][0]):
		# 		if odata[i_i][0]>odata[j_j][0]:
		# 			temp = odata[j_j]
		# 			odata[j_j] = odata[i_i]
		# 			odata[i_i] = temp
		# 		else:
		# 			pass

		print '``````````````%d````````````'%i
		# print ndata
		# print odata
		countNUm(ndata, odata, i)
		draw_line(ndata, odata, process_file, i)
		# print ndata[:,2]
		# nd=[float(ndata[:,2][i]) for i in range(len(ndata))]
		# print nd
		nd=[float(ndata[:,2][j]) for j in range(len(ndata))]
		od=[float(odata[:,2][j]) for j in range(len(odata))]
		print nd
		print '---------------------'
		print od
		draw_hist(nd, process_file+'_n', i)
		draw_hist(od, process_file+'_o', i)
	# for file_name in file_names:
		



