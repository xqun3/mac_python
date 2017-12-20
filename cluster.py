import numpy as np
import os
#import excetptions

def restore_correlation_matrix():
	file=open('correlation1.txt')
	N=5000  #?
	correlation_matrix=[]
	for ii in range(N-1):
		file_line=file.readline()
		data_list=file_line.split('\n')[0].split(',')
		correlation_list=[]
		M=len(data_list)
		for jj in range(M-1):
			correlation_list.append(float(data_list[jj]))
		correlation_matrix.append(correlation_list)
	file.close()
	return correlation_matrix

def restore_group_list():
	file=open('pdb.txt')
	file_line=file.readlines()
	group_list=[]
	for ii in range(len(file_line)):
		group_list.append([file_line[ii].split('\n')[0]])
	return group_list

def find_most_similar(correlation_matrix):
	max=0
	for ii in range(len(correlation_matrix)):
		for jj in range(len(correlation_matrix[ii])):
			if correlation_matrix[ii][jj]>max:
				max=correlation_matrix[ii][jj]
				first_index=ii
				second_index=ii+jj+1
	return max,first_index,second_index

def clustering(correlation_matrix,group_list,first_index,second_index):

	'''
	L=len(group_list)
	cc=0
	dd=0
	for aa in range(L):
		if  '150d.pdb' in group_list[aa]:
			cc=aa
		if '177l.pdb' in group_list[aa]:
			dd=aa
	print cc,dd,correlation_matrix[cc][dd-cc-1]
	if cc!=dd:
		if correlation_matrix[cc][dd-cc-1]>0.575870:
			print cc,dd,correlation_matrix[cc][dd-cc-1]
			raise Exception('wrong')
	'''
	
	group_list[first_index]=group_list[first_index]+group_list[second_index]
	del group_list[second_index]
	M=len(correlation_matrix)

	for qq in range(M):
		if len(correlation_matrix[qq])!=M-qq:
			raise Exception('bad')

	ii=first_index-1
	jj=second_index-1 	
	for mm in range(first_index):
		'''
		if mm==30:
			print 'mm,ii',mm,ii,jj
			for ee in range(15):
				if correlation_matrix[30][ee]==correlation_matrix[30][28]:
					print 'true',ee,correlation_matrix[mm][ee]
		'''
		if correlation_matrix[mm][ii]>correlation_matrix[mm][jj]:
			correlation_matrix[mm][ii]=correlation_matrix[mm][jj]
		'''
		print 'before',correlation_matrix[30][14]
		for ee in range(15):
				if correlation_matrix[30][ee]==correlation_matrix[30][28]:
					print 'true',ee,correlation_matrix[mm][ee]
		'''
		del correlation_matrix[mm][jj]
		ii=ii-1
		jj=jj-1
	del correlation_matrix[first_index][jj]
	jj=jj-1
	ll=first_index+1
	for nn in range(second_index-first_index-1):
		if correlation_matrix[first_index][nn]>correlation_matrix[ll][jj]:
			correlation_matrix[first_index][nn]=correlation_matrix[ll][jj]

		del correlation_matrix[ll][jj]
		ll=ll+1
		jj=jj-1
	if second_index==M:
		del correlation_matrix[second_index-1]
	pp=second_index-first_index-1
	if M-second_index-1>=0:
		for zz in range(len(correlation_matrix[second_index])):
			if correlation_matrix[first_index][pp]>correlation_matrix[second_index][zz]:
				correlation_matrix[first_index][pp]=correlation_matrix[second_index][zz]
			pp=pp+1
		del correlation_matrix[second_index]
	'''
	L=len(group_list)
	cc=0
	dd=0
	for aa in range(L):
		if  '150d.pdb' in group_list[aa]:
			cc=aa
		if '177l.pdb' in group_list[aa]:
			dd=aa
	if cc!=dd:
		if correlation_matrix[cc][dd-cc-1]>0.575870:
			print cc,dd,correlation_matrix[cc][dd-cc-1]
			raise Exception('wrong')
	'''
	
	
if __name__=='__main__':
	group_list=restore_group_list() 
	correlation_matrix=restore_correlation_matrix()


	while(1):
		max,first_index,second_index=find_most_similar(correlation_matrix)
		if(max>0.6):
			clustering(correlation_matrix,group_list,first_index,second_index)
		else:
			print 'cluster complete'
			break
	#print correlation_matrix	

	for ii in range(len(group_list)):
		os.system('mkdir group%d' % ii)
		os.system('touch group%d/group%d.txt' % (ii,ii))
		for jj in group_list[ii]:
			file=open('group%d/group%d.txt' % (ii,ii),'a')
			file.write(jj)
			file.write('\n')
			os.system('cp /mnt/data2/ycshi/transfer/pisa/{} group{}'.format(jj,ii))
		print group_list[ii]

	
	
