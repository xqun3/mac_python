# -*-coding:utf-8 -*-
from backend import process_loadedpdb
import os

if __name__ == '__main__':
	filepath = '/Users/dongxq/Sites/project/media/brilM.pdb'
	bdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	father_path=os.path.abspath(os.path.dirname(bdir)+os.path.sep+".")
	# print(args[0])
	print filepath
	print bdir
	print father_path
	# process_loadedpdb.process_pdb(filepath)