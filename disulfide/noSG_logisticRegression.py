#-*- coding:utf-8 -*-
import sys
import numpy as np
from scipy.spatial.distance import pdist
from sklearn.model_selection import train_test_split
import random
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
import operator
from collections import OrderedDict
import csv
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

def find_mutate_rank(dict_result):
	print('****** The probability of the mutate pos ********')
	ssbonds_detect = np.load('/Users/dongxq/Desktop/disulfide/other_test_set/mutational_structrue_bril_flavodoxin/bril_ssbond.npy')#flavodoxin_ssbond.npy
	k = 1
	rank_dict = {}
	# print ssbonds_detect
	for item in dict_result:
		k += 1;
		# print item
		# temp = item.split('-')

		temp_list = [filter(str.isdigit,item[0]),filter(str.isdigit,item[1])]
		if temp_list in ssbonds_detect.tolist():
			print temp_list
	
	print len(dict_result)

def comput_distance(inputcord):
	print inputcord.shape
	ssbonds_distance_map = []
	for smapi in range(len(inputcord)):
		Y = pdist(inputcord[smapi], 'euclidean')
		# print Y
		ssbonds_distance_map.append(Y)
		# print ssbonds_distance_map
		# if smapi == 2:
		# 	break
		# ssbonds_distance_map.append(Y)
	ssbonds_distance_map = np.array(ssbonds_distance_map)
	print ssbonds_distance_map.shape
	return ssbonds_distance_map

def shulffle(samplelist,labels):
	samplezip = zip(samplelist.tolist(),labels.tolist())
	random.shuffle(samplezip)
	# print(samplezip[0])
	# print([x[1] for x in samplezip])
	return samplezip

def feature_name():
	featuers = ['N1','CA1','C1','O1','CB1','N2','CA2','C2','O2','CB2']
	featuers_weight = [None for i in range(45)]
	count = 0
	for i in range(9):
		for j in range(i+1, 10):
			
			featuers_weight[count] = featuers[i] +'-'+featuers[j]
			count += 1
	print featuers_weight
	return featuers_weight

def tree_features(X,y,featuers_weight):
	forest = ExtraTreesClassifier(n_estimators=250,random_state=0)
	forest.fit(X, y)
	importances = forest.feature_importances_
	print("importances")
	print(importances)
	std = np.std([tree.feature_importances_ for tree in forest.estimators_],
	             axis=0)
	indices = np.argsort(importances)[::-1]
	print("indices")
	print(indices)

	print("Feature ranking:")

	for f in range(X.shape[1]):
	    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

	# Plot the feature importances of the forest
	ax = plt.figure()
	plt.title("Feature importances")
	plt.bar(range(X.shape[1]), importances[indices],
	       color="r", yerr=std[indices], align="center")
	plt.xticks(range(X.shape[1]), [featuers_weight[i] for i in indices],rotation=45)
	plt.xlim([-1, X.shape[1]])
	plt.show()

def classfication():
	pass

if __name__ == '__main__':
	args = sys.argv[1:]
	pos_input = np.load(args[0])
	neg_input = np.load(args[1])
	pos_distance = comput_distance(pos_input)
	neg_distance = comput_distance(neg_input)
	labels = [1 for i in range(pos_distance.shape[0])]
	labels.extend([0 for j in range(neg_distance.shape[0])])
	labels = np.array(labels)
	data = np.concatenate((pos_distance, neg_distance), axis=0)
	print data.shape, labels.shape
	shulfflelist = np.array(shulffle(data,labels))
	print shulfflelist.shape	
	X = np.array(shulfflelist[:,0].tolist())
	y = np.array(shulfflelist[:,1].tolist())
	feature_name = feature_name()
	# print shulfflelist[:,0]
	# train_X , X_test, train_y,y_test = train_test_split(np.array(shulfflelist[:,0].tolist()),np.array(shulfflelist[:,1].tolist()),test_size=0.25,random_state=0) 
	# print train_X.shape
	# print train_y.shape
	# print X_test.shape
	# # print X_test
	# print y_test.shape

	# lr_model= LogisticRegression(C = 1.0,  penalty = 'l1')  
	# clf = lr_model.fit(train_X,train_y)
	# print clf.score(X_test, y_test)
	# print clf.coef_[0]
	# np.save('/Users/dongxq/Desktop/disulfide/LR_weight.npy',clf.coef_[0])


	# featuers_weight_dict = dict(zip(featuers_weight,[abs(round(i,3)) for i in clf.coef_[0]]))
	# print featuers_weight_dict
	# sorted_result_dict = sorted(featuers_weight_dict.iteritems(), key=operator.itemgetter(1), reverse=True) 
	# print sorted_result_dict
	# final_dict = OrderedDict() 
	# final_dict = sorted_result_dict
	# np.save('/Users/dongxq/Desktop/disulfide/LR_weight_dict.npy',final_dict)

	# with open('/Users/dongxq/Desktop/disulfide/LR_weight_dict.csv', "wb") as csvFile:
	# 	csvWriter = csv.writer(csvFile)
	# 	for k in final_dict:
	# 		csvWriter.writerow([k[0],k[1]])
	# 	csvFile.close()
	# flavo_predict = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/brilM_ca_noSG_ssbond_nr.npy')
	# flavo_predict_id = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/brilM_ca_noSG_ssbond_id_nr.npy').tolist()

	# flavo_predict_distance = comput_distance(flavo_predict)
	# teg = clf.predict(flavo_predict_distance)
	# # print teg
	# formed = []
	# for i in range(len(teg)):
	# 	if teg[i] == 1:
	# 		print flavo_predict_id[i]
	# 		formed.append(flavo_predict_id[i])
	# find_mutate_rank(formed)

	
	
