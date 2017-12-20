# -*- coding:utf-8 -*-

import os 
import time
import numpy as np

t0 = time.time()
pdb_list = os.listdir('/Users/dongxq/Desktop/pdb_disulfide/')

print len(pdb_list)
if pdb_list[0] =='.DS_Store':
	pdb_list = pdb_list[1:]
print len(pdb_list)
np.save('pdb_name.npy', pdb_list)
pdb_ssbond = 0
all_ssbond = 0
ssbond_list = []
ssbonds_map = []
# ssbonds_map = np.array(ssbonds_map)
bigcount = 0
smallcount = 0

for pdb in pdb_list:
	flag = True
	SSBOND_flag = True
	search_list = []
	count = 0
	ssbond_map = []
	new_list = []
	# print pdb
	with open('/Users/dongxq/Desktop/pdb_disulfide/%s'%pdb,'r') as f:
		for line in f:
			line = line.strip()
			line_temp = line.split()
			
			# print line_temp
			temp = line_temp[0]
			# A = (temp != 'SSBOND')
			# # print A
			# B = (temp != 'ATOM')
			# # print B
			# if A or B:#temp != 'SSBOND' or 
			# 	# print A,B
			# 	# print count,temp
			# 	continue
			# print temp
			if (temp != 'SSBOND') and (temp != 'ATOM'):
				# print temp,
				continue
			if flag and temp == 'SSBOND':
				# print 'ssbond'
				flag = False
				pdb_ssbond += 1
			if temp == 'SSBOND':
				all_ssbond += 1
				ssbond_list.append((pdb, line_temp))
				search_list.append(line_temp[2]+line_temp[3]+line_temp[4])
				search_list.append(line_temp[5]+line_temp[6]+line_temp[7])
				# print search_list
				continue
			if SSBOND_flag:
				if (len(search_list)/2) == 1:
					ssbond_map.append([])
				else:
					ssbond_map = [ [] for i in range(len(search_list)/2)]
				# xyz_count = [ 0 for i in range(len(search_list/2))]
				SSBOND_flag = False
				# print ssbond_map
			if temp == 'ATOM' and (line_temp[3]+line_temp[4]+ line_temp[5]) in search_list:
				ssbond_num = search_list.index(line_temp[3]+line_temp[4]+ line_temp[5])
				map_index = ssbond_num/2
				# print map_index
				# xyz_count[map_index] += 1
				# print line_temp
				# print len(search_list)
				
				ssbond_map[map_index].append(line_temp[6])
				ssbond_map[map_index].append(line_temp[7])
				ssbond_map[map_index].append(line_temp[8])
		# print len(ssbond_map)

		for i in range(len(ssbond_map)):

			if len(ssbond_map[i]) > 36:
				# smap = np.array(smap)
				# print type(smap)
				# smap = smap.reshape(12,3)
				# print i
				# ssbond_map.pop(i)
				bigcount += 1
				with open('ssbond_remove.txt', 'a' ) as wf:
					wf.write('bigcount ' + pdb + ' , ' + str(i) + '\n ')
				continue
			elif len(ssbond_map[i]) < 36:
				# smap = np.array(smap)
				# print type(smap)
				# smap = smap.reshape(12,3)
				# print i
				# ssbond_map.pop(i)
				smallcount += 1
				with open('ssbond_remove.txt', 'a' ) as wf:
					wf.write('smallcount '+ pdb + ' , ' + str(i) + '\n ')
				continue
			new_list.append(ssbond_map[i])
	ssbonds_map.extend(new_list)		
	# np.append(ssbonds_map,ssbond_map)

print 'yes'
# print ssbonds_map
print len(ssbonds_map)
ssbonds_map = np.array(ssbonds_map)
print ssbonds_map
print len(ssbonds_map)
for smap in ssbonds_map:
	if len(smap) != 36:
		print 'length > or < 36'
		break
ssbonds_map = ssbonds_map.reshape(len(ssbonds_map),12,3)
print ssbonds_map
np.save('ssbonds_map.npy',ssbonds_map)
print 'there are %d pdb has ssbond'%pdb_ssbond
print 'there are %d ssbond in all pdb'%all_ssbond
t1 = time.time()
print 'time used %e seconds' %(t1-t0)