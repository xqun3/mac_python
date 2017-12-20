# -*-coding:utf-8 -*-

import datetime
import os
from libtbx import easy_pickle
from scitbx.array_family import flex
import numpy as np

begin = datetime.datetime.now()
data = easy_pickle.load("~/Desktop/pisadb/pisaDB.nl")
length = len(data)

count = 0
diff_list = []

for i in range(29999):
	for j in range(i+1,30000):
		diff_listi = data[i] - data[j]
		diff_list.append(diff_listi.norm())
		print count
		count = count + 1

diff_array = np.array(diff_list)
np.save('diff30000.npy',diff_array)
end = datetime.datetime.now()
#print data
print str(end-begin)
print (data[0] - data[1]).norm()
print length