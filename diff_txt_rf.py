import datetime
import os
from libtbx import easy_pickle
from scitbx.array_family import flex

begin = datetime.datetime.now()
data = easy_pickle.load("~/Desktop/pisadb/pisaDB.nl")
length = len(data)
data_type = type(data)

count = 0
diff_txt=open('diff5000all.txt','a')

for i in range(5000):
	for j in range(5000):
		diff_list = data[i] - data[j]
		if(j==0):
			diff_txt.write(diff_list.norm())
		else:
			diff_txt.write(','+str(diff_list.norm()))
		print count
		count = count + 1
	diff_txt.write('\n')


end = datetime.datetime.now()
#print data
print str(end-begin)
print (data[0] - data[1]).norm()
print length