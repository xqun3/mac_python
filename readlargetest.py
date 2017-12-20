# -*- coding:utf-8 -*-
'''
from openpyxl import load_workbook

wb = load_workbook(filename='diff5000new.xlsx', read_only=True)
ws = wb['dirr_col_1250']
ws1 = wb['dirr_col_2500']
'''
with open('diff10000.txt') as f:
	for line in f:
		print line

'''

for row in ws.rows:
	for cell in row:
		#print ws.title
		print cell.value


for row in ws1.rows:
	for cell in row:
		#print ws.title
		print cell.value
'''