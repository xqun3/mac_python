# -*- coding:utf-8 -*-

import numpy as np

a = 'S193C-M233C L183C-W243C A162C-403C S352C-L401C S186C-A239C Y148C-S392C 193C-L232C F156C-A191C C226-C296# A162C-A399C L218C-L224C A158C-A399C I317C-G361C* V246C-Y269C I147C-S389C L218C-S223C Y152C-A191C M340C-D344C S155C-L396C L144C-F385C'

a = a.split()
print a 

for ai in a:
	ai = ai.split('-')
alist = [None for i in range(len(a))]
for i in range(len(a)):
	temp = a[i].split('-')
	print i
	# if i%2== 0:
	alist[i] = (filter(str.isdigit,temp[0]),filter(str.isdigit,temp[1]))
		# alist[i+1] = (temp[1][1:-1],(temp[0][1:-1]))
	# else:
	# 	print 'hi'
	# 	alist[i+2] = (temp[0][1:-1],(temp[1][1:-1]))
	# 	alist[i+3] = (temp[1][1:-1],(temp[0][1:-1]))
	# print alist
print alist
for i in range(len(a)):
	temp = a[i].split('-')
	alist.insert(i,(filter(str.isdigit,temp[1]),filter(str.isdigit,temp[0])))
print alist
np.save('GLP1R_ssbond.npy',alist)

# print a
# alist = [None for i in range(len(a))]
# for i in range(len(a)):
# 	if i%2 == 0:
# 		alist[i] = (a[i],a[i+1])
# 		alist[i+1] = (a[i+1],a[i])
# print alist