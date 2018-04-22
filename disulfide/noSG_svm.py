from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
import random
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from sklearn.model_selection import KFold


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




file_path = '/Users/dongxq/Desktop/disulfide/noSG_neuro_input/'
pos = np.load(file_path+'pos_noSG_distance_ssbond.npy')
neg = np.load(file_path+'12496_neg_noSG_distance_ssbond.npy')

flavo_predict = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/brilM_ca_full_noSG_ssbond_nr.npy')
flavo_predict_id = np.load('/Users/dongxq/Desktop/disulfide/noSG_predict_test/brilM_ca_noSG_ssbond_id_nr.npy').tolist()


pos_y = np.ones(len(pos),dtype=int)
print 'pos',pos.shape

neg_y = np.zeros(len(neg))
print 'neg',neg.shape

alltraindata = np.concatenate((pos, neg), axis=0).reshape(-1,100)
alltrainteg = np.concatenate((pos_y, neg_y), axis=0)

print alltraindata.shape
print alltrainteg.shape

# samplezip = np.array(zip(alltraindata.reshape(-1,100).tolist(),alltrainteg.tolist()))
# random.shuffle(samplezip)

# print samplezip[:,0][0].shape
# for i in samplezip[:,0]:
# 	if len(i) != 100:
# 		print 'wrong'
# 		print len(i)
# 		print i
# 		break
	# print i
# print samplezip[1][1].shape

# data = np.array(samplezip[:,0])
X_train, X_test, y_train, y_test = train_test_split(alltraindata, alltrainteg, test_size=.3, random_state=0)

# print  X_train.shape, y_train.shape,X_test.shape, y_test.shape
# print y_train
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
# clf = svm.SVC(kernel='linear', C=1)
# scores = cross_val_score(clf, alltraindata, alltrainteg, cv=5)

print clf.score(X_test, y_test)
teg = clf.predict(flavo_predict.reshape(-1,100))
# print teg
formed = []
for i in range(len(teg)):
	if teg[i] == 1:
		print flavo_predict_id[i]
		formed.append(flavo_predict_id[i])

find_mutate_rank(formed)
# print scores
# joblib.dump(clf,'svm.model')

# kf = KFold(n_splits=2)
# for train, test in kf.split(alltraindata):
# 	print("%s %s" % (train, test))


