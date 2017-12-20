# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt 
import numpy as np
import model_clsss
import os
 
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
	with open('dtestnp.txt','a') as wf:
		wf.write('************************%d************************\n'%ntop)
		for i in range(len(data)):
			# print data[i].ID,data[i].cluster_mean_cc,data[i].mean_cc
			# print 
			wf.write(data[i].ID)
			wf.write('\t')
			wf.write(str(data[i].cluster_mean_cc))
			wf.write('\t')
			wf.write(str(data[i].mean_cc))
			wf.write('\n')


def test_sort(data):
	for i in range(len(data)):
		print data[i].ID

def chang2list(data):
	data_RMAX = []
	data_find_rmax = []
	data_mul_cluster = []
	data_cluster_mean_cc = []
	data_mean_cc = []
	data_x = []
	data_ID = []

	for i in range(len(data)): 
		#print data[i].ID,data[i].cluster_num,data[i].cluster_mean_cc,data[i].mean_cc,data[i].RMAX,data[i].find_rmax
		data_RMAX.append(float(data[i].RMAX))
		data_find_rmax.append(float(data[i].find_rmax))
		data_cluster_mean_cc.append(float(data[i].cluster_mean_cc))
		# print data[i].cluster_mean_cc
		data_mean_cc.append(float(data[i].mean_cc))
		data_ID.append(data[i].ID)
		if(int(data[i].cluster_num) > 1):
			#print data[i].cluster_num
			data_x.append(i)
			data_mul_cluster.append(data[i].cluster_mean_cc)

	return data_ID,data_RMAX ,data_find_rmax ,data_mul_cluster ,data_mean_cc ,data_x ,data_cluster_mean_cc

def draw_hist(data, title):
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
	plt.title('%s'%title)
	plt.savefig('%s.png'%title, bbox = 'tight')
	#plt.show()

if __name__ == '__main__':
	#print len(mul_cluster)
	print os.getcwd()
	pisa_average_list = []
	sas_average_list = []
	cluster_average_list = []
	mean_average_list = []

	for ntop in range(10,11):
		#print i
		# print '-----------------------%d----------------------'%ntop
		count_meancc = 0
		low_meancc = 0
		count_clustercc = 0
		low_clustercc = 0
		count = 0
		count_rmax =0
		low_rmax = []
		pisa_low_count = 0
		original_low_count = 0
		low_x = []
		high_rmax = []
		high_x = []
		pisa_high_count = 0
		original_high_count = 0
		os.chdir('/Users/dongxq/Desktop/refinew/dammin60000a/')
		original = np.load('dammin_o_%d_model_list.npy'%ntop)
		pisa = np.load('dammin_n_%d_model_list.npy'%ntop)

		# print len(original)
		os.system('mkdir %d'%ntop)
		os.chdir('/Users/dongxq/Desktop/refinew/dammin60000a/%d'%ntop)

		sort_model(original)
		# test_sort(original)
		original_ID, original_RMAX ,original_find_rmax ,original_mul_cluster ,original_mean_cc ,original_x, original_cluster_mean_cc = chang2list(original)

		sort_model(pisa)
		# for i in range(len(pisa)):
		# 	print pisa[i].ID,pisa[i].cluster_mean_cc,pisa[i].mean_cc
		#test_sort(pisa)

		# with open('%ddtestnp.txt'%ntop,'w') as wf:
		# 	wf.write('************************%d************************\n'%ntop)
		# 	for i in range(len(pisa)):
		# 		print pisa[i].ID,pisa[i].cluster_mean_cc,pisa[i].mean_cc
		# 		# print 
		# 		wf.write(pisa[i].ID)
		# 		wf.write('\t')
		# 		wf.write(str(pisa[i].cluster_mean_cc))
		# 		wf.write('\t')
		# 		wf.write(str(pisa[i].mean_cc))
		# 		wf.write('\n')
		# 	print '--------------------------old---------------------------'
		# 	wf.write('-----------------------old-------------------------------\n')
		# 	for i in range(len(original)):
		# 		print original[i].ID,original[i].cluster_mean_cc,original[i].mean_cc
		# 		wf.write(original[i].ID)
		# 		wf.write('\t')
		# 		wf.write(str(original[i].cluster_mean_cc))
		# 		wf.write('\t')
		# 		wf.write(str(original[i].mean_cc))
		# 		wf.write('\n')

		pisa_ID, pisa_RMAX ,pisa_find_rmax ,pisa_mul_cluster ,pisa_mean_cc ,pisa_x, pisa_cluster_mean_cc = chang2list(pisa)

		pisa_average = 0
		sas_average = 0
		cluster_average = 0
		mean_average = 0
		for i in range(len(pisa_RMAX)):
			# print original_ID[i],pisa_ID[i]
			if original_ID[i] != pisa_ID[i]:
				break
			if pisa_RMAX[i] == 0 or original_RMAX[i] == 0:
				if(original_cluster_mean_cc[i] == 0):

					print pisa_ID[i], 
				continue
			temp_value = pisa_find_rmax[i] - pisa_RMAX[i]
			count_rmax += 1
			pisa_average += temp_value
			if pisa_find_rmax[i] < pisa_RMAX[i]:
				low_x.append(i)
				low_rmax.append(pisa_cluster_mean_cc[i])
				pisa_low_count += 1
			if pisa_find_rmax[i] > pisa_RMAX[i]:
				high_x.append(i)
				high_rmax.append(pisa_cluster_mean_cc[i])
				pisa_high_count += 1

			if original_find_rmax[i] < original_RMAX[i]:
				original_low_count += 1
			if original_find_rmax[i] > original_RMAX[i]:
				original_high_count += 1
			#pisa_average += pisa_find_rmax[i] - pisa_RMAX[i]
			temp_value = original_find_rmax[i] - original_RMAX[i]
			sas_average += temp_value
			#sas_average += original_find_rmax[i] - original_RMAX[i]
		pisa_average_list.append(pisa_average/count_rmax)
		sas_average_list.append(sas_average/count_rmax)
		# print original_cluster_mean_cc
		for i in range(len(pisa_RMAX)):
			if original_ID[i] != pisa_ID[i]:
				break
			if pisa_cluster_mean_cc[i] == 0 or original_cluster_mean_cc[i] == 0:
				if(original_cluster_mean_cc[i] == 0):
					print 'old'
					print pisa_ID[i] 
				continue
			temp_value = pisa_cluster_mean_cc[i] - original_cluster_mean_cc[i]
			count += 1
			if temp_value > 0:
				count_clustercc += 1
			elif temp_value < -0.05:
				low_clustercc += 1
			cluster_average += temp_value
			#cluster_average += pisa_cluster_mean_cc[i] - original_cluster_mean_cc[i]
			temp_value += pisa_mean_cc[i] - original_mean_cc[i]
			if temp_value > 0:
				count_meancc += 1
			elif temp_value < -0.05:
				low_meancc += 1
			mean_average += temp_value
			#mean_average += pisa_mean_cc[i] - original_mean_cc[i]
		print count
		cluster_average_list.append(cluster_average/count)
		mean_average_list.append(mean_average/count)


		with open('%d.txt'% ntop, 'w') as f:
			f.write('pisa_average diff = '+ str(pisa_average/count) + '\n')
			f.write('sas_average diff = '+ str(sas_average/count) + '\n')
			f.write('cluster_average diff = '+ str(cluster_average/count) + '\n')
			f.write('mean_average diff = '+ str(mean_average/count) + '\n')
			f.write('new cluster_mean_cc > old cluster_mean_cc  = '+ str(count_clustercc) + '\n')
			f.write('cluster_mean_cc < -0.05 = '+ str(low_clustercc) + '\n')
			f.write('count new mean_cc > old mean_cc = '+ str(count_meancc) + '\n')
			f.write('mean_cc < -0.05 = '+ str(low_meancc) + '\n')
			f.write('no error count =  '+ str(count) + '\n')
			f.write('no error RMAX count =  '+ str(count_rmax) + '\n')
			f.write('new low RMAX count =  '+ str(pisa_low_count) + '\n')
			f.write('new high error RMAX count =  '+ str(pisa_high_count) + '\n')
			f.write('old low RMAX count =  '+ str(original_low_count) + '\n')
			f.write('old high RMAX count =  '+ str(original_high_count) + '\n')
			# f.write('low RMAX : '+ str(low_rmax) + '\n')
			# f.write('high RMAX : '+ str(high_rmax) + '\n')

		x = [i for i in range(len(pisa_ID))]
		plt.figure(figsize=(18,6))
		plt.plot(original_RMAX, '-o' , label='original')
		plt.plot(original_find_rmax, '-o', label='old database find max')
		plt.plot(pisa_find_rmax, '--o', label='new database find max')

		# plt.ylim(0,130)
		# plt.xlim(-1,40)
		plt.legend()
		plt.xticks(x,pisa_ID,rotation=90)
		plt.title('compare the rmax(dammin ntop=%d)'%ntop)
		plt.savefig('compare_dammin_rmax_%d.jpg'%ntop)

		#plt.show()
		'''
		f, (ax, ax2) = plt.subplots(2, 1, sharex=True,figsize=(18,6),gridspec_kw={'height_ratios':[4,1]})

		f.suptitle('compare cluster_mean_cc ntop=%d'%ntop)
		ax.plot(low_x,low_rmax,'ro',label='low find rmax', color='yellow', markersize=10)
		ax.plot(high_x,high_rmax ,'ro',label='high find rmax', color='black', markersize=10)
		ax.plot(original_cluster_mean_cc, '-o' , label='old database cluster_mean_cc')
		ax.plot(pisa_cluster_mean_cc, '-o' , label='new database cluster_mean_cc')
		ax.plot(original_x,original_mul_cluster, 'ro',label='old database cluster number > 1', color='red')
		ax.plot(pisa_x,pisa_mul_cluster, 'ro',label='new database cluster number > 1', color='green')

		ax2.plot(low_x,low_rmax,'ro',label='low find rmax', color='yellow', markersize=12)
		ax2.plot(high_x,high_rmax ,'ro',label='high find rmax', color='black', markersize=12)
		ax2.plot(original_cluster_mean_cc, '-o' , label='old database cluster_mean_cc')
		ax2.plot(pisa_cluster_mean_cc, '-o' , label='new database cluster_mean_cc')
		ax2.plot(original_x,original_mul_cluster, 'ro',label='old database cluster number > 1', color='red')
		ax2.plot(pisa_x,pisa_mul_cluster, 'ro',label='new database cluster number > 1', color='green')

		ax.set_ylim(.7, 1.)  # outliers only
		ax2.set_ylim(-0.1, .2) 
		ax.spines['bottom'].set_visible(False)
		ax2.spines['top'].set_visible(False)
		ax.xaxis.set_visible(False)
		ax.tick_params(labeltop='off')  # don't put tick labels at the top
		ax2.xaxis.tick_bottom()
		d = .005  # how big to make the diagonal lines in axes coordinates
		# arguments to pass plot, just so we don't keep repeating them
		kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
		ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
		ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

		kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
		ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
		ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
		'''
		plt.figure(figsize=(18,6))
		plt.title('compare the cluster mean cc(dammin ntop=%d)'%ntop)
		plt.plot(low_x,low_rmax,'ro',label='low find rmax', color='yellow', markersize=12)
		plt.plot(high_x,high_rmax ,'ro',label='high find rmax', color='black', markersize=12)
		plt.plot(original_cluster_mean_cc, '-o' , label='old database cluster_mean_cc')
		plt.plot(pisa_cluster_mean_cc, '-o' , label='new database cluster_mean_cc')
		plt.plot(original_x,original_mul_cluster, 'ro',label='old database cluster number > 1', color='red')
		plt.plot(pisa_x,pisa_mul_cluster, 'ro',label='new database cluster number > 1', color='green')
		plt.legend()

		
		# plt.xlim(-1,100)
		# plt.ylim(0.6,1)
		
		plt.xticks(x,pisa_ID,rotation=90)
		plt.savefig('cluster_mean_cc_%d.jpg'%ntop)
		#plt.show()

		plt.figure(figsize=(18,6))
		plt.plot(original_mean_cc, '-o', label='old database mean_cc')
		plt.plot(pisa_mean_cc, '-o', label='new database mean_cc')

		plt.legend()
		plt.xticks(x,pisa_ID,rotation=90)
		plt.title('compare mean_cc ntop=%d'%ntop)
		plt.savefig('mean_cc_%d.jpg'%ntop)
		#plt.show()

		# plt.figure(figsize=(18,6))
		# plt.plot(low_x,low_rmax,'ro',label='low find rmax', color='yellow', markersize=12)
		# plt.plot(high_x,high_rmax,'ro',label='high find rmax', color='black', markersize=12)
		
		# plt.legend()

		# plt.title('test ntop=%d'%ntop)
		# plt.savefig('test%d.jpg'%ntop)
		
		draw_hist(original_cluster_mean_cc, 'old database cluster_mean_cc ntop=%d'%ntop)
		draw_hist(pisa_cluster_mean_cc, 'new database cluster_mean_cc ntop=%d'%ntop)
		draw_hist(original_mean_cc, 'old database mean_cc ntop=%d'%ntop)
		draw_hist(pisa_mean_cc, 'new database mean_cc ntop=%d'%ntop)

	np.savez('100_diff_list',pisa_average_list, sas_average_list, cluster_average_list, mean_average_list,count_clustercc,low_clustercc,count_meancc,low_meancc )








	# original = np.load('dammin_old_model_list.npy')
	# pisa = np.load('dammin_new_model_list.npy')

	# print len(original)

	# sort_model(original)
	# test_sort(original)
	# original_RMAX ,original_find_rmax ,original_mul_cluster ,original_mean_cc ,original_x, original_cluster_mean_cc = chang2list(original)

	# sort_model(pisa)
	# test_sort(pisa)
	# pisa_RMAX ,pisa_find_rmax ,pisa_mul_cluster ,pisa_mean_cc ,pisa_x, pisa_cluster_mean_cc = chang2list(pisa)
	# print original_mean_cc
	# print 'cluster'
	# print original_cluster_mean_cc

	# print pisa_find_rmax
	# pisa_average = 0
	# sas_average = 0
	# for i in range(len(pisa_RMAX)):
	# 	pisa_average += pisa_find_rmax[i] - pisa_RMAX[i]
	# 	sas_average += original_find_rmax[i] - original_RMAX[i]
	# print pisa_average/36
	# print sas_average/36

	# plt.plot(original_RMAX, '-o' , label='original')
	# plt.plot(original_find_rmax, '-o', label='old database find max')
	# plt.plot(pisa_find_rmax, '--o', label='new database find max')

	# plt.ylim(0,130)
	# plt.xlim(-1,40)
	# plt.legend()
	# plt.title('compare the rmax(dammin)')
	# plt.savefig('compare_dammin_rmax.jpg')

	# plt.show()

	# plt.plot(original_cluster_mean_cc, '-o' , label='old database cluster_mean_cc')
	# plt.plot(pisa_cluster_mean_cc, '-o' , label='new database cluster_mean_cc')
	# plt.plot(original_x,original_mul_cluster, 'ro',label='old database cluster number > 1', color='red')
	# plt.plot(pisa_x,pisa_mul_cluster, 'ro',label='new database cluster number > 1', color='green')
	# plt.legend()
	# plt.title('compare cluster_mean_cc')
	# plt.savefig('cluster_mean_cc.jpg')
	# plt.ylim(0.6,1)
	# plt.xlim(-1,40)
	# plt.show()

	# plt.plot(original_mean_cc, '-o', label='old database mean_cc')
	# plt.plot(pisa_mean_cc, '-o', label='new database mean_cc')

	# plt.legend()
	# plt.title('compare mean_cc')
	# plt.savefig('mean_cc.jpg')
	# plt.show()

	# draw_hist(original_cluster_mean_cc, 'old database cluster_mean_cc')
	# draw_hist(pisa_cluster_mean_cc, 'new database cluster_mean_cc')
	# draw_hist(original_mean_cc, 'old database mean_cc')
	# draw_hist(pisa_mean_cc, 'new database mean_cc')


