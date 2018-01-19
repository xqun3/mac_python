# -*-coding:utf-8-*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.text import Annotation

label = ['N','CA','C','O','CB','SG','N','CA','C','O','CB','SG']
class Annotation3D(Annotation):
    '''Annotate the point xyz with text s'''

    def __init__(self, s, xyz, *args, **kwargs):
        Annotation.__init__(self,s, xy=(0,0), *args, **kwargs)
        self._verts3d = xyz        

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.xy=(xs,ys)
        Annotation.draw(self, renderer)

def annotate3D(ax, s, *args, **kwargs):
    '''add anotation text s to to Axes3d ax'''

    tag = Annotation3D(s, *args, **kwargs)
    ax.add_artist(tag)

def find_cord(args):
	mutate_cord = np.load(args[0])
	mutate_cord_id = np.load(args[1])
	wt_cord = np.load(args[2])
	wt_cord_id = np.load(args[3])
	find_cord_pos = [args[4],args[5]]
	print('find ssbond pos is :',find_cord_pos)
	print(args)

	print(len(mutate_cord),len(wt_cord))
	assert len(mutate_cord) == len(mutate_cord_id),'mutate map does not equal to mutate id'
	assert len(wt_cord) == len(wt_cord_id),'wt map does not equal to wt id'

	mutate_pos_ord = [None for i in range(len(mutate_cord_id))]
	wt_pos_ord = [None for i in range(len(wt_cord_id))]
	for i in range(len(mutate_cord_id)):
		mutate_pos_ord[i] = [filter(str.isdigit,mutate_cord_id[i][0]),filter(str.isdigit,mutate_cord_id[i][1])]
	for i in range(len(wt_cord_id)):
		wt_pos_ord[i] = [filter(str.isdigit,wt_cord_id[i][0]),filter(str.isdigit,wt_cord_id[i][1])]

	m_cord_map = mutate_cord[mutate_pos_ord.index(find_cord_pos)]
	w_cord_map = wt_cord[wt_pos_ord.index(find_cord_pos)]

	return w_cord_map, m_cord_map, find_cord_pos


def draw_cord_map(wt, mutate, find_cord_pos):
	pos  = args[4]+'_'+args[5]

	np.save('/Users/dongxq/Desktop/disulfide/predict_cord_analysis/%sm_cord_map.npy'%pos, m_cord_map)
	np.save('/Users/dongxq/Desktop/disulfide/predict_cord_analysis/%sw_cord_map.npy'%pos, w_cord_map)
	x1 = (wt[1][0],wt[4][0],wt[5][0],wt[11][0],wt[10][0],wt[7][0])
	y1 = (wt[1][1],wt[4][1],wt[5][1],wt[11][1],wt[10][1],wt[7][1])
	z1 = (wt[1][2],wt[4][2],wt[5][2],wt[11][2],wt[10][2],wt[7][1])

	# print(x1)
	# print(y1)
	# print(z1)
	x2 = [mutate[1][0],mutate[4][0],mutate[5][0],mutate[11][0],mutate[10][0],mutate[7][0]]
	y2 = [mutate[1][1],mutate[4][1],mutate[5][1],mutate[11][1],mutate[10][1],mutate[7][1]]
	z2 = [mutate[1][2],mutate[4][2],mutate[5][2],mutate[11][2],mutate[10][2],mutate[7][2]]

	group = [1, 1, 1, 2, 2, 2]
	# edges = [()]
	xyz1 = zip(x1,y1,z1)
	xyz2 = zip(x2,y2,z2)
	fig=plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.title('wt %s cordinate map'%pos)
	zdir1 = ('wt_%sCA'%find_cord_pos[0],'wt_%sCB'%find_cord_pos[0],'wt_%sSG'%find_cord_pos[0],'wt_%sSG'%find_cord_pos[1],'wt_%sCB'%find_cord_pos[1],'wt_%sCA'%find_cord_pos[1])
	
	print(zdir1)
	# zdir1 = ['wt 14 CA','wt 14 CB','wt 14 SG', 'wt 14 CA','wt 14 CB','wt 14 SG']
	# ssbond_distance_map = ssd.squareform(ten_map[i]) 
	# plt.scatter(x1,y1,z1,label='wt')
	# plt.scatter(x2,y2,z2,label='mutate')
	ax.plot(x1,y1,z1, '-o',label='wt')

	for j, xyz_ in enumerate(xyz1): 
	    annotate3D(ax, s=zdir1[j], xyz=xyz_, fontsize=10, xytext=(-3,3),textcoords='offset points', ha='right',va='bottom')  

	plt.legend()
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_cord_analysis/wt_%s_cordinate_map.png'%pos,bbox_inches='tight')
	
	fig=plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	plt.title('mt %s cordinate map'%pos)
	
	zdir2 = ('mt_%sCA'%find_cord_pos[0],'mt_%sCB'%find_cord_pos[0],'mt_%sSG'%find_cord_pos[0],'mt_%sSG'%find_cord_pos[1],'mt_%sCB'%find_cord_pos[1],'mt_%sCA'%find_cord_pos[1])

	ax.plot(x2,y2,z2,'-o',label='mutate')
	
	for j, xyz_ in enumerate(xyz2): 
	    annotate3D(ax, s=zdir2[j], xyz=xyz_, fontsize=10, xytext=(-3,3),textcoords='offset points', ha='right',va='bottom')  

	# plt.plot(wt,label='wt')
	# plt.plot(mutate,label='mutate')
	plt.legend()
	
	plt.savefig('/Users/dongxq/Desktop/disulfide/predict_cord_analysis/mt_%s_cordinate_map.png'%pos,bbox_inches='tight')
	plt.show()
if __name__ == '__main__':
	args = sys.argv[1:]
	# find_cord(args)
	w_cord_map, m_cord_map, find_cord_pos = find_cord(args)
	draw_cord_map(w_cord_map, m_cord_map, find_cord_pos)
