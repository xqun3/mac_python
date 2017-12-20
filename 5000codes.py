# -*- coding:utf-8 -*-

from libtbx import easy_pickle

codes = easy_pickle.load('~/Desktop/pisadb/pisaDB.codes')
testcodes = codes[:5000]
f = open('5000_codes.txt','w')

print testcodes 
print codelist

correlation_list.append(float(data_list[jj].split('e')[0])*pow(10,(7+float(data_list[jj].split('e')[1]))))