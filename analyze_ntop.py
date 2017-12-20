# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

value = np.load('/Users/dongxq/Desktop/refinew/dammin10000testwa/10/100_diff_list.npz')
print value["arr_0"]
print value["arr_1"]

log_path = '/Users/dongxq/Desktop/refinew/dammin10000testwa/'
cluster_mean_cc = []
cluster_mean_cc_diff = []
mean_cc = []
mean_cc_diff = []
for i in range(1,11):
	with open(log_path + str(i) + '/' + str(i) +'.txt', "rb") as f:
		for line in f:
			temp = line.split()
			if line.startswith('new cluster_mean_cc'):
				cluster_mean_cc.append(temp[-1]) 
			elif line.startswith('cluster_mean_cc'):
				cluster_mean_cc_diff.append(temp[-1])	
			elif line.startswith('count'):
				mean_cc.append(temp[-1])
			elif line.startswith('mean_cc'):
				mean_cc_diff.append(temp[-1])

print cluster_mean_cc
print cluster_mean_cc_diff
print mean_cc
print mean_cc_diff

plt.figure()
# plt.plot(value["arr_0"], '-o', label='new database rmax diff')
plt.plot(value["arr_0"], '-o', label='refine w rmax diff')
# plt.plot(value["arr_1"], '-o', label='old database rmax diff')
plt.plot(value["arr_1"], '-o', label='old w rmax diff')

plt.legend()
plt.title('dammin 10000 database Rmax compare')
plt.savefig('Rmax compare.jpg')
plt.show()

plt.figure()
plt.plot(value["arr_2"], '-o', label='cluster between new w and old')
plt.plot(value["arr_3"], '-o', label='mean between new w and old')
plt.legend()
plt.title('dammin 10000 database compare cluster and mean')
plt.savefig('compare cluster and mean.jpg')

plt.show()

plt.figure()
plt.plot(cluster_mean_cc, '-o', label='new cluster mean cc > old cluster meancc')
plt.plot(cluster_mean_cc_diff, '-o', label='cluster mean cc diff < -0.05')
plt.plot(mean_cc, '-o', label='new mean cc > old meancc')
plt.plot(mean_cc_diff, '-o', label='mean cc diff < -0.05')
plt.legend()
plt.title('dammin 10000 database statistic')
plt.savefig('statistic.jpg')

plt.show()