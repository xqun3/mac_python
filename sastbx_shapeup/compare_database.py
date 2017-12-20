# -*- coding:utf-8 -*-

from libtbx import easy_pickle
import datetime

newCodes = easy_pickle.load("~/Desktop/pisadb/pisaDB.codes")
oldCodes = easy_pickle.load("~/software/sastbx/source/sastbx/database/pisa.codes")

count = 0
print len(newCodes)
print len(oldCodes)
wf = open('/Users/dongxq/Desktop/notIn','w')
for code in oldCodes:
	if code.lower() in newCodes:
		count += 1
		print code.lower()
	else:
		wf.write(code.lower() + '\n')
wf.write('There are %d pdb in new 60000 Database \n'% count)
wf.write('There are %d pdb in old Database \n'% len(newCodes))
wf.write('There are %d pdb in old Database \n'% len(oldCodes))
	

