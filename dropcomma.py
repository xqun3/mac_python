# -*- coding:utf-8 -*-
wf = open('../diff5000dropcomma.txt','w')
count = 0

with open('../diff5000.txt') as f:
	for line in f:
		m = line[:-2]
		print m
		count = count +1 
		wf.write(m+'\n')

print count

wf.close()