#  -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import random

full_name_file = open('/Users/dongxq/Desktop/disulfide/pdbname.txt','r')
train_name_file = open('/Users/dongxq/Desktop/disulfide/nuero_pdb.txt','r')

full_file_lines = full_name_file.readlines()
train_name_lines = train_name_file.readlines()

full_name_file.close()
train_name_file.close()

full_name = [full_lines.strip() for full_lines in full_file_lines]
train_name = [train_lines.strip() for train_lines in train_name_lines]

print('length of the full dataset is ',len(full_name))
print('length of the train dataset is ',len(train_name))

# validation_name = [0 for i in range(10000)]

count = 0

for name in train_name:
	if name in full_name:
		count += 1
		del(full_name[full_name.index(name)])

print('repeat name count is ', count)
random.shuffle(full_name)

validation_name = random.sample(full_name,10000)
np.save('validation_name.npy',validation_name)


