# -*- coding:utf-8 -*-

import os

count = 0
# with open('/Users/xiangxilun/Desktop/DataSet/pdb7.txt','r') as f:
# 	for line in f:
# 		line = line.strip()
# 		temps = line.split()
# 		print temps
# 		for temp in temps:
# 			temp = temp[:3]
# 			print temp
# 			os.system('cp /Users/xiangxilun/Desktop/DataSet/pdb/pdb%s.ent /Users/xqdong/Desktop/pdb_disulfide/'%temp.lower())
# 			count += 1
# 			print count

names = np.load('validation_name.npy')

for name in names:
	os.system('cp pdb/%s valisation_set/'%temp.lower())
