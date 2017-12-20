# -*- coding:utf-8 -*-

import os 
import time
import numpy as np

def correct_xyz(line_temp,mol_pos):
	# print len(line_temp[mol_pos+1]),len(line_temp[mol_pos+2])
	# print mol_pos
	if len(line_temp[mol_pos+1])-len(line_temp[mol_pos+2]) > 3:
		pos = mol_pos+1
	else:
		pos = mol_pos+2
	# print pos
	temp = line_temp[pos].split('-')
	# print temp
	if len(temp) == 1:
		print "wrong line!"
	# print temp
	print line_temp
	x=0 
	y=0
	z=0
	if pos == 6 and mol_pos == 4:
		x = float(line_temp[pos-1])
		if temp[0] == '':
			y = float('-'+temp[1])
			z = float('-'+temp[2])
		else:
			y = float(temp[0])
			z = float('-'+temp[1])
	elif pos == 6:
		z = float(line_temp[pos+1])
		if temp[0] == '':
			x = float('-'+temp[1])
			y = float('-'+temp[2])
		else:
			x = float(temp[0])
			y = float('-'+temp[1])
	else:
		if temp[0] == '':
			x = float('-'+temp[1])
			y = float('-'+temp[2])
		else:
			x = float(temp[0])
			y = float('-'+temp[1])
	# print x,y,x
	return x,y,z

# def apppendxyz(line_temp,mol_pos.):



t0 = time.time()
pdb_list = os.listdir('/Users/dongxq/Desktop/disulfide/validation_set/')

print len(pdb_list)
if pdb_list[0] =='.DS_Store':
	pdb_list = pdb_list[1:]
print len(pdb_list)
# np.save('pdb_name.npy', pdb_list)
with open('pdb_name.txt','w') as pdb_name:
	for pdb_n in pdb_list:
		pdb_name.write(pdb_n + '\n')
	
pdb_ssbond = 0
all_ssbond = 0
ssbond_list = []
ssbonds_map = []
# ssbonds_map = np.array(ssbonds_map)
bigcount = 0
smallcount = 0
mol_pos = 5


for pdb in pdb_list:
	flag = True
	SSBOND_flag = True
	search_list = []
	count = 0
	ssbond_map = []
	new_list = []
	print pdb
	with open('/Users/dongxq/Desktop/disulfide/validation_set/%s'%pdb,'r') as f:
		for line in f:
			line = line.strip()
			line_temp = line.split()
			
			# print line_temp
			try:
				temp = line_temp[0]
			except IndexError:
				print 'pdb name: ',pdb
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
				# if (len(search_list)/2) == 1:
				# 	ssbond_map.append([])
				ssbond_map = [ [ [] for i in range(6)] for i in range(len(search_list))]
				# xyz_count = [ 0 for i in range(len(search_list/2))]
				SSBOND_flag = False
				# print ssbond_map
			if len(line_temp[2]) == 7 or len(line_temp[4]) == 5:
				mol_pos = 4
				with open('line_temp.txt','a') as wlf:
					wlf.write('pdb name: '+pdb +'\n')
					wlf.write(line +'\n')
			else:
				mol_pos = 5
			# print search_list
			# print line_temp
			search_mol = line_temp[3]+line_temp[4]+ line_temp[5]

			if len(line_temp[4]) == 5: #process this situation like this CYS A2085
				search_mol = line_temp[3]+line_temp[4]
				# print search_mol
			# Asearch_mol = 'A'+search_mol
			# print (line_temp[3]+line_temp[4]+ line_temp[5]) #in search_list
			# print search_list

			if temp == 'ATOM' and (search_mol in search_list or (search_mol[1:] in search_list and line_temp[3][0] == 'A')):
				# print search_mol
				# print line_temp[3][1:],search_mol
				if len(line_temp[3]) == 4 and line_temp[3][0] == 'A':
					search_mol = search_mol[1:]
					# print search_mol
				map_index = search_list.index(search_mol)
				

				# print map_index
				# xyz_count[map_index] += 1
				# print line_temp
				# print len(search_list)
				
				if abs(len(line_temp[mol_pos+1])-len(line_temp[mol_pos+2])) <= 3:
					if line_temp[2] == 'N' and ssbond_map[map_index][0] == []:
						ssbond_map[map_index][0].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][0].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][0].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][0]
						# ssbond_map[map_index][0] = float(line_temp[mol_pos+1])
						# ssbond_map[map_index][1] = float(line_temp[mol_pos+2])
					elif line_temp[2] =='CA' and ssbond_map[map_index][1] == []:
						ssbond_map[map_index][1].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][1].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][1].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][1]
					elif line_temp[2] =='C' and ssbond_map[map_index][2] == []:
						ssbond_map[map_index][2].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][2].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][2].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][2]
					elif line_temp[2] =='O' and ssbond_map[map_index][3] == []:
						ssbond_map[map_index][3].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][3].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][3].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][3]
					elif line_temp[2] =='CB' and ssbond_map[map_index][4] == []:
						ssbond_map[map_index][4].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][4].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][4].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][4]
					elif line_temp[2] =='SG' and ssbond_map[map_index][5] == []:
						ssbond_map[map_index][5].append(float(line_temp[mol_pos+1]))
						ssbond_map[map_index][5].append(float(line_temp[mol_pos+2]))
						ssbond_map[map_index][5].append(float(line_temp[mol_pos+3]))
						# print ssbond_map[map_index][5]
				else:
					
					x,y,z=correct_xyz(line_temp,mol_pos)
					if line_temp[2] == 'N' and ssbond_map[map_index][0] == []:
						ssbond_map[map_index][0].append(x)
						ssbond_map[map_index][0].append(y)
						ssbond_map[map_index][0].append(z)
						# print ssbond_map[map_index][0]
					elif line_temp[2] =='CA' and ssbond_map[map_index][1] == []:
						# ssbond_map[map_index][1].append([x,y,z])
						ssbond_map[map_index][1].append(x)
						ssbond_map[map_index][1].append(y)
						ssbond_map[map_index][1].append(z)
						# print ssbond_map[map_index][1]
					elif line_temp[2] =='C' and ssbond_map[map_index][2] == []:
						# ssbond_map[map_index][2].append([x,y,z])
						ssbond_map[map_index][2].append(x)
						ssbond_map[map_index][2].append(y)
						ssbond_map[map_index][2].append(z)
						# print ssbond_map[map_index][2]
					elif line_temp[2] =='O' and ssbond_map[map_index][3] == []:
						# ssbond_map[map_index][3].append([x,y,z])
						ssbond_map[map_index][3].append(x)
						ssbond_map[map_index][3].append(y)
						ssbond_map[map_index][3].append(z)
						# print ssbond_map[map_index][3]
					elif line_temp[2] =='CB' and ssbond_map[map_index][4] == []:
						# ssbond_map[map_index][4].append([x,y,z])
						ssbond_map[map_index][4].append(x)
						ssbond_map[map_index][4].append(y)
						ssbond_map[map_index][4].append(z)
						# print ssbond_map[map_index][4]
					elif line_temp[2] =='SG' and ssbond_map[map_index][5] == []:
						# ssbond_map[map_index][5].append([x,y,z])
						ssbond_map[map_index][5].append(x)
						ssbond_map[map_index][5].append(y)
						ssbond_map[map_index][5].append(z)
						# print ssbond_map[map_index][5]

				# map_index = ssbond_num/2
				# print map_index
				# xyz_count[map_index] += 1
				# print line_temp
				# print len(search_list)
			
			if temp == 'ENDMDL' :
				break
		for i in range(len(ssbond_map)):
			if ssbond_map[i][0] == [] and search_list[i]==search_list[search_list.index(search_list[i])]:
				# print 'copy'
				with open('copy.txt','a') as wcopyf:
					wcopyf.write(pdb + ' ' + search_list[i] + '  '+ search_list[search_list.index(search_list[i])]+ '\n')
				ssbond_map[i] = ssbond_map[search_list.index(search_list[i])]
		# print search_list
		for i in range(len(ssbond_map)):
			a = []
			correct_mol_flag = True
			if i%2 == 1:
				continue
			for j1 in ssbond_map[i]:
				if len(j1) > 3:
					bigcount += 1
					print j1
					correct_mol_flag = False
					with open('ssbond_remove.txt', 'a' ) as wf:
						wf.write('bigcount ' + pdb + ' , ' + str(j1) + '\n ')
				elif len(j1) < 3:
					smallcount += 1
					print j1
					correct_mol_flag = False
					with open('ssbond_remove.txt', 'a' ) as wf:
						wf.write('smallcount '+ pdb + ' , ' + str(ssbond_map[i]) + '\n ')
			for j2 in ssbond_map[i+1]:
				if len(j2) > 3:
					bigcount += 1
					print j2
					correct_mol_flag = False
					with open('ssbond_remove.txt', 'a' ) as wf:
						wf.write('bigcount ' + pdb + ' , ' + str(j2) + '\n ')
				elif len(j2) < 3:
					smallcount += 1
					print j2
					correct_mol_flag = False
					with open('ssbond_remove.txt', 'a' ) as wf:
						wf.write('smallcount '+ pdb + ' , ' + str(ssbond_map[i]) + '\n ')
			if correct_mol_flag :
				a.extend(ssbond_map[i])
				a.extend(ssbond_map[i+1])
				# print a 
				new_list.append(a)
			# print 'new_list',len(new_list)
			# print 'ssbond_map',len(ssbond_map)
			# print ssbond_map
			# print new_list
	ssbonds_map.extend(new_list)
	# print ssbonds_map		
	# np.append(ssbonds_map,ssbond_map)

print 'yes'
# print ssbonds_map
print len(ssbonds_map)
ssbonds_map = np.array(ssbonds_map)
# print ssbonds_map
print ssbonds_map.shape
print ssbonds_map
# print len(ssbonds_map)
for i in range(len(ssbonds_map)):
	if len(ssbonds_map[i]) != 12:
		print 'length > or < 12',i
		break
# ssbonds_map = ssbonds_map.reshape(len(ssbonds_map),12,3)
# print ssbonds_map
np.save('ssbonds_map.npy',ssbonds_map)
print 'there are %d pdb has ssbond'%pdb_ssbond
print 'there are %d ssbond in all pdb'%all_ssbond
t1 = time.time()
print 'time used %e seconds' %(t1-t0)