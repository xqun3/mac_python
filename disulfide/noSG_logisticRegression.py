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
from sklearn.ensemble import RandomForestClassifier
from pandas import Series, DataFrame  
from numpy import array

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

def find_mutate_rank_pro(dict_result, outteg):
	print('****** The probability of the mutate pos ********')
	ssbonds_detect = np.load('/Users/dongxq/Desktop/disulfide/other_test_set/mutational_structrue_bril_flavodoxin/flavodoxin_ssbond.npy')#flavodoxin_ssbond.npy
	k = 1
	rank_dict = {}
	# print ssbonds_detect
	for item in dict_result:
		k += 1;
		# print item
		# temp = item.split('-')

		temp_list = [filter(str.isdigit,item[0]),filter(str.isdigit,item[1])]
		if temp_list in ssbonds_detect.tolist():
			print temp_list, outteg[k-1]
	
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

def tree_features(X,y,feature_name):
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
	plt.xticks(range(X.shape[1]), [feature_name[i] for i in indices],rotation=45)
	plt.xlim([-1, X.shape[1]])
	plt.show()

def classfication(train_X , X_test, train_y, y_test,feature_names):
	
	clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=250)
	clf = clf.fit(train_X, train_y)
	print clf.score(X_test, y_test)
	print clf.feature_importances_
	std = np.std([tree.feature_importances_ for tree in clf.estimators_],  axis=0)
	draw_feature_importance(feature_names, clf.feature_importances_ ,std)
	store_weight(feature_names, clf.feature_importances_)
	predict_real_data_del(clf)

def draw_feature_importance(feature_name, importances, std):
	indices = np.argsort(importances)[::-1]
	print("Feature ranking:")

	for f in range(len(feature_name)):
	    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

	# Plot the feature importances of the forest
	ax = plt.figure()
	plt.title("Feature importances")
	plt.bar(range(len(feature_name)), importances[indices],
	       color="r", yerr=std[indices], align="center")
	plt.xticks(range(len(feature_name)), [feature_name[i] for i in indices],rotation=45)
	plt.xlim([-1, len(feature_name)])
	plt.show()

def store_weight(feature_name, featuers_weight):
	featuers_weight_dict = dict(zip(feature_name,[round(i,4) for i in featuers_weight]))
	# print featuers_weight_dict
	sorted_result_dict = sorted(featuers_weight_dict.iteritems(), key=operator.itemgetter(1), reverse=True) 
	# print sorted_result_dict
	final_dict = OrderedDict() 
	final_dict = sorted_result_dict
	np.save('/Users/dongxq/Desktop/disulfide/weight_dict.npy',final_dict)
	with open('/Users/dongxq/Desktop/disulfide/weight_dict.csv', "wb") as csvFile:
		csvWriter = csv.writer(csvFile)
		for k in final_dict:
			csvWriter.writerow([k[0],k[1]])
		# csvFile.close()
# brilM_ca_noSG_ssbond_nr.npy
# brilM_ca_noSG_ssbond_id_nr.npy
def predict_real_data(clf):
	flavo_predict = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/flavo_ca_noSG_ssbond_nr.npy')
	flavo_predict_id = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/flavo_ca_noSG_ssbond_id_nr.npy').tolist()

	flavo_predict_distance = comput_distance(flavo_predict)
	teg = clf.predict_proba(flavo_predict_distance)
	# print teg
	# formed = []
	# for i in range(len(teg)):
	# 	if teg[i] == 1:
	# 		print flavo_predict_id[i]
	# 		formed.append(flavo_predict_id[i])
	# find_mutate_rank(formed)

	formed = []
	outteg = []
	for i in range(len(teg)):
		if teg[i][1] > teg[i][0]:
			# print teg[i]
			formed.append(flavo_predict_id[i])
			outteg.append(teg[i])
	find_mutate_rank_pro(formed, outteg)

def predict_real_data_del(clf):
	flavo_predict = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/flavo_ca_noSG_ssbond_nr.npy')
	flavo_predict_id = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/flavo_ca_noSG_ssbond_id_nr.npy').tolist()

	flavo_predict_distance = comput_distance(flavo_predict)
	or_feature_name = feature_name()

	dfs = DataFrame(flavo_predict_distance, columns=or_feature_name) 
	del dfs['N1-CB1']
	del dfs['C1-CB1']
	del dfs['CA1-O1']
	del dfs['CA2-O2']
	del dfs['N2-O2']
	del dfs['CA2-C2']
	del dfs['N1-CA1']
	del dfs['O2-CB2']
	del dfs['N2-CB2']
	del dfs['N2-C2']
	del dfs['CA1-C1']
	del dfs['CA1-CB1']
	del dfs['C1-O1']
	del dfs['N1-O1']
	del dfs['N1-C1']
	del dfs['O1-CB1']
	del dfs['C2-CB2']
	del dfs['C2-O2']
	del dfs['CA2-CB2']
	del dfs['N2-CA2']
	teg = clf.predict_proba(array(dfs))
	
	# print teg
	# formed = []
	# for i in range(len(teg)):
	# 	if teg[i] == 1:
	# 		print flavo_predict_id[i]
	# 		formed.append(flavo_predict_id[i])
	# find_mutate_rank(formed)

	formed = []
	outteg = []
	for i in range(len(teg)):
		if teg[i][1] > teg[i][0]:
			# print teg[i]
			formed.append(flavo_predict_id[i])
			outteg.append(teg[i])
	find_mutate_rank_pro(formed, outteg)

def LR_classification(train_X , X_test, train_y, y_test,feature_names):
	lr_model= LogisticRegression(C = 1.0,  penalty = 'l1')  
	clf = lr_model.fit(train_X,train_y)
	print clf.score(X_test, y_test)
	predict_real_data_del(clf)

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
	feature_names = feature_name()
	df = DataFrame(X,columns=feature_names)  
	# print df
	del df['N1-CB1']
	del df['C1-CB1']
	del df['CA1-O1']
	del df['CA2-O2']
	del df['N2-O2']
	del df['CA2-C2']
	del df['N1-CA1']
	del df['O2-CB2']
	del df['N2-CB2']
	del df['N2-C2']
	del df['CA1-C1']
	del df['CA1-CB1']
	del df['C1-O1']
	del df['N1-O1']
	del df['N1-C1']
	del df['O1-CB1']
	del df['C2-CB2']
	del df['C2-O2']
	del df['CA2-CB2']
	del df['N2-CA2']
	# print df
	# print type(array(df))
	feature_names = df.columns.values
	print feature_names

	# df.to_csv('/Users/dongxq/Desktop/disulfide/OneDimensionSet.csv', index=False)
	train_X , X_test, train_y,y_test = train_test_split(array(df),y,test_size=0.25,random_state=0) 
	classfication(train_X , X_test, train_y, y_test,feature_names)



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


	
	
