import os 
import time
import numpy as np
import math

# def correct_xyz(line_temp,):
# 	pass


# t0 = time.time()
pdb_list = os.listdir('/Users/dongxq/Desktop/pdb_disulfide/')
print 'pdb numbers',len(pdb_list)
if pdb_list[0] =='.DS_Store': 
	pdb_list = pdb_list[1:]
# print 'pdb numbers',len(pdb_list)

nossbond_map = []
all_ssbond = 0

for pdb in pdb_list:
	print pdb
	flag = True
	SSBOND_flag = True
	search_list = []
	count = 0
	CA_list = []
	ssbond_mol_map = []
	current_ssbond = 0
	mol_pos = 5

	with open('/Users/dongxq/Desktop/pdb_disulfide/%s'%pdb,'r') as f:
		for line in f:
			line = line.strip()
			line_temp = line.split()
			# firsts = line_temp[2]+line_temp[3]
			
			# print line_temp
			temp = line_temp[0]
			if (temp != 'SSBOND') and (temp != 'ATOM'):
				# print temp,
				continue
			# if flag and temp == 'SSBOND':
			# 	# print 'ssbond'
			# 	flag = False
			# 	pdb_ssbond += 1
			if temp == 'SSBOND':
				if line_temp[4][-1] == 'B':
					firstsn0 = line_temp[4][:-1]+'A'
					# print 'first mol',firstsn0
					firstsn1 = int(line_temp[4][:-1]) + 1
					with open('special_molpos.txt','a') as wsf:
						wsf.write(pdb+'\n')
						wsf.write(line)
				elif line_temp[4][-1] == 'A':
					firstsn0 = line_temp[4][:-1]
					# print 'first mol',firstsn0
					firstsn1 = line_temp[4][:-1] + 'B'
					with open('special_molpos.txt','a') as wsf:
						wsf.write(pdb+'\n')
						wsf.write(line)
				elif line_temp[4][-1] == 'D':
					firstsn0 = line_temp[4][:-1]+'C'
					# print 'first mol',firstsn0
					firstsn1 = int(line_temp[4][:-1])+1
					with open('special_molpos.txt','a') as wsf:
						wsf.write(pdb+'\n')
						wsf.write(line)
				elif line_temp[4][-1] == 'F':
					firstsn0 = line_temp[4][:-1]+'E'
					# print 'first mol',firstsn0
					firstsn1 = line_temp[4][:-1]+'G'
					with open('special_molpos.txt','a') as wsf:
						wsf.write(pdb+'\n')
						wsf.write(line)
				else:
					firstsn0 = int(line_temp[4])-1 
					firstsn1 = int(line_temp[4])+1 
				if line_temp[7][-1] == 'B':
					secondfn0 = line_temp[7][:-1]+'A'
					# print 'second mol',secondn0
					secondfn1 = int(line_temp[7][:-1]) + 1
				elif line_temp[7][-1] == 'A':
					secondfn0 = line_temp[7][:-1]
					# print 'second mol',secondn0
					secondfn1 = line_temp[7][:-1] + 'B'
				elif line_temp[7][-1] == 'D':
					secondfn0 = line_temp[7][:-1] + 'C'
					# print 'second mol',secondn0
					secondfn1 = int(line_temp[7][:-1]) + 1
				elif line_temp[7][-1] == 'F':
					secondfn0 = line_temp[7][:-1] + 'E'
					# print 'second mol',secondn0
					secondfn1 = line_temp[7][:-1] + 'G'
				else:
					secondn0 = int(line_temp[7])-1
					secondn1 = int(line_temp[7])+1
				# seconds = line_temp[5]+line_temp[6]
				
				all_ssbond += 1
				current_ssbond += 1
				# ssbond_list.append((pdb, line_temp))
				search_list.append(line_temp[3]+str(firstsn0))
				search_list.append(line_temp[3]+str(firstsn1))
				search_list.append(line_temp[6]+str(secondn0))
				search_list.append(line_temp[6]+str(secondn1))
				print 'search list: ', search_list


				# print search_list
				continue
			if SSBOND_flag:
				# if (len(search_list)/2) == 1:
				# 	ssbond_mol_map.append([])
				# else:
				# 	ssbond_mol_map = [ [] for i in range(len(search_list))]
				# 	CA_list = [ for i in range(len(search_list)/4)]
				ssbond_mol_map = [ [] for i in range(len(search_list))]
				CA_list = [ [[] for i in range(4)] for i in range(len(search_list)/4)]
				# xyz_count = [ 0 for i in range(len(search_list/2))]
				SSBOND_flag = False
				# print ssbond_map
			if len(line_temp[2]) == 7:
				mol_pos = 4
				with open('line_temp.txt','a') as wlf:
					wlf.write('pdb name: '+pdb +'\n')
					wlf.write(line +'\n')
			else:
				mol_pos = 5
			# print mol_pos
			# print line_temp[mol_pos]
			
			# print mol_pos
			# print line_temp[mol_pos]
			# print str(line_temp[mol_pos]) in search_list
			if temp == 'ATOM' and line_temp[mol_pos-1]+line_temp[mol_pos] in search_list:
				# print CA_list
				# print search_list
				# print line_temp
				# print 'mol_pos',mol_pos
				if line_temp[3] == 'PRO' or line_temp[3] == 'GLY':
					with open('unssbond.txt','a') as wf:
						wf.write('pdb name :' + pdb + ' has PRO or GLY near the ssbond\n')
					continue
				num = search_list.index(line_temp[mol_pos-1]+line_temp[mol_pos])
				# print 'num',num
				if line_temp[2] == 'CA':
					a2 = num/4#current_ssbond
					a3 = num%4#current_ssbond
					# print a2,a3
					# CA_list.append((num,[line_temp[6],line_temp[7],line_temp[8]]))
					CA_list[a2][a3]=[line_temp[mol_pos+1],line_temp[mol_pos+2],line_temp[mol_pos+3]]
				if line_temp[2] == 'CA' or line_temp[2] == 'N' or line_temp[2] == 'C' or line_temp[2] == 'O' or line_temp[2] == 'CB' or line_temp[2] == 'CG':
					print line_temp[mol_pos+1],line_temp[mol_pos+2],line_temp[mol_pos+3]
					if abs(len(line_temp[mol_pos+1])-len(line_temp[mol_pos+2])) <= 2:
						ssbond_mol_map[num].append(float(line_temp[mol_pos+1]))
						ssbond_mol_map[num].append(float(line_temp[mol_pos+2]))
						ssbond_mol_map[num].append(float(line_temp[mol_pos+3]))
						continue
					print len(line_temp[mol_pos+1]),len(line_temp[mol_pos+2])
					if len(line_temp[mol_pos+1])-len(line_temp[mol_pos+2]) > 3:
						pos = mol_pos+1
					else:
						pos = mol_pos+2
					print pos
					temp = line_temp[pos].split('-')
					if len(temp) == 1:
						break
					print temp
					x=0
					y=0
					z=0
					if pos == 6:
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
					print line_temp
					ssbond_mol_map[num].append(x)
					ssbond_mol_map[num].append(y)
					ssbond_mol_map[num].append(z)
					# print '********************'
					

				# print map_index
				# xyz_count[map_index] += 1
				# print line_temp
				# print len(search_list)
		print 'CA_list length : ',len(CA_list)
		print 'length of the ssbond_mol_map',len(ssbond_mol_map)
		# if CA_list
		for i in range(current_ssbond): # find all nossbond near the ssbond
			distance = [0,0,0,0]
			if CA_list[i][0] != []:
				if CA_list[i][2] != []:
					sumCA = 0
					for xyz in range(3):
						sumCA += pow((float(CA_list[i][0][xyz])-float(CA_list[i][2][xyz])), 2)
					distance[0] = math.sqrt(sumCA)
				if CA_list[i][3] != []:
					sumCA = 0
					for xyz in range(3):
						sumCA += pow((float(CA_list[i][0][xyz])-float(CA_list[i][3][xyz])), 2)
					distance[1] = math.sqrt(sumCA)
			if CA_list[i][1] != []:
				if CA_list[i][2] != []:
					sumCA = 0
					for xyz in range(3):
						sumCA += pow((float(CA_list[i][1][xyz])-float(CA_list[i][2][xyz])), 2)
					distance[2] = math.sqrt(sumCA)
				if CA_list[i][3] != []:
					sumCA = 0
					for xyz in range(3):
						sumCA += pow((float(CA_list[i][1][xyz])-float(CA_list[i][3][xyz])), 2)
					distance[3] = math.sqrt(sumCA)
			maxDistance = distance.index(max(distance))
			# print 'distance',distance
			# print 'maxDistance',maxDistance
			b1 = maxDistance/2 #mol near the first mol in the ssbond
			b2 = maxDistance%2 + 2 #mol near the second mol in the ssbond
			# print 'b1',b1
			# print 'b2',b2
			# print ssbond_mol_map
			# print i*4+b1
			# print ssbond_mol_map[i*4+b1]
			# print ssbond_mol_map[i*4+b2]
			# print ssbond_mol_map[i*4+b1]+ssbond_mol_map[i*4+b2]
			temp_nossbond = ssbond_mol_map[i*4+b1]+ssbond_mol_map[i*4+b2]
			# print temp_nossbond
			if temp_nossbond != []:
				count += 1
				with open('nossbond.txt','a') as wnf:
					wnf.write(pdb+'\n')
				nossbond_map.append(temp_nossbond)


print nossbond_map
print len(nossbond_map)
# bigcount = 0
# smallcount = 0
# for i in range(len(nossbond_map)):
# 	if len(nossbond_map[i]) > 36:
# 		print 'length more than 18'
# 		print i
# 		print nossbond_map[i]
# 		break
# 	elif len(nossbond_map[i]) < 36:
# 		print 'length less than 18'
# 		print i
# 		print nossbond_map[i]
# 		print len(nossbond_map[i])
# 		break
print all_ssbond


