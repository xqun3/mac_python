# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

'''
def func(x,a,b):
	return a * x + b

x = np.linspace(0,10,100)
y = func(x,1,2)

yn = y + 0.9 * np.random.normal(size=len(x))

popt, pcov = curve_fit(func,x,yn)

plt.plot(x,y,'y--')
plt.plot(x,yn,'ro')
plt.plot(x,func(x,*popt),'k-')

print popt
print pcov
plt.show()
'''
'''
def func(x,a,b,c):
	return a*np.exp(-(x-b)**2/(2*c**2))

x = np.linspace(0,10,100)
y = func(x,1,5,2)

yn = y + 0.2 * np.random.normal(size=len(x))

popt, pcov = curve_fit(func, x, yn)

print popt
print pcov
plt.plot(x,y,'b--',label = 'origin')
plt.plot(x,func(x,*popt),'y-',label = 'fit')
plt.legend()
plt.show()
'''
'''
def func(x, a0, b0, c0, a1, b1, c1):
	return a0*np.exp(-(x - b0) ** 2/(2*c0**2)) + a1 *np.exp(-(x-b1) **2/(2*(2*c1**2)))

x = np.linspace(0, 20, 200)
y = func(x, 1, 3, 1, -2, 15, 0.5)

yn = y + 0.2*np.random.normal(size=len(x))
guesses = [1,2,1,1,15,1]
popt, pcov = curve_fit(func, x, yn,p0=guesses)

plt.plot(x,y,label='Origin')
plt.plot(x,func(x,*popt),label='fit')
plt.legend()
print popt
plt.show()
'''
'''
from scipy.optimize import fsolve

line = lambda x:x+3
solution = fsolve(line,-2)

print solution
'''
'''
from scipy.optimize import fsolve

def findIntersection(func1, func2, x0):
	return fsolve(lambda x: func1(x)-func2(x), x0)

funky = lambda x :np.cos(x/5)*np.sin(x/2)
line = lambda x:0.01*x-0.5

x = np.linspace(0,45,10000)
result = findIntersection(funky, line, [15,20,30,35,40,45])

plt.plot(x,funky(x))
plt.plot(x,line(x) )
plt.plot(result,line(result),'ro')
print result 
print line(result)
plt.show()
'''
'''
from scipy.interpolate import interp1d

x = np.linspace(0,10*np.pi,20)
y = np.cos(x)

fl = interp1d(x,y,kind='linear')
fq = interp1d(x,y,kind='quadratic')

xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
yintq = fq(xint)

print x
print yintl
print yintq

plt.plot(xint, yintl)
plt.plot(xint, yintq)
plt.show()

'''
'''
from scipy.interpolate import UnivariateSpline

sample = 30
x = np.linspace(1,10*np.pi,sample)
y = np.cos(x) + np.log10(x) + np.random.randn(sample) /10

f = UnivariateSpline(x,y,s=1)

xint = np.linspace(x.min(),x.max(),1000)
yint = f(xint)
plt.plot(x,y)
plt.plot(xint,yint)
print yint
plt.show()
'''
'''
from scipy.interpolate import griddata

ripple = lambda x,y:np.sqrt(x**2 + y**2)+np.sin(x**2 +y**2)

grid_x,grid_y =np.mgrid[0:5:1000j,0:5:10000j]

xy = np.random.rand(1000,2)
sample = ripple(xy[:,0]*5,xy[:,1]*5)
grid_z0 = griddata(xy * 5, sample, (grid_x, grid_y), method='cubic')
'''
'''
from scipy.stats import geom
# Here set up the parameters for the geometric distribution. 
p = 0.5
dist = geom(p)
# Set up the sample range. 
x = np.linspace(0, 5, 1000)
# Retrieving geom's PMF and CDF 
pmf = dist.pmf(x)
cdf = dist.cdf(x)
# Here we draw out 500 random values. 
sample = dist.rvs(500)
print sample
plt.plot(x,pmf)
plt.plot(x,cdf)

plt.show()
'''
'''
from scipy import stats
# Generating a normal distribution sample # with 100 elements
sample = np.random.randn(100)
# normaltest tests the null hypothesis. 
out = stats.normaltest(sample) 
print('normaltest output') 
print('Z-score = ' + str(out[0])) 
print('P-value = ' + str(out[1]))
# kstest is the Kolmogorov-Smirnov test for goodness of fit.
# Here its sample is being tested against the normal distribution. 
# D is the KS statistic and the closer it is to 0 the better.
out = stats.kstest(sample, 'norm')
print('\nkstest output for the Normal distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))
# Similarly, this can be easily tested against other distributions, 
# like the Wald distribution.
out = stats.kstest(sample, 'wald')
print('\nkstest output for the Wald distribution')
print('D = ' + str(out[0])) 
print('P-value = ' + str(out[1]))
'''
'''
import numpy as np
from scipy.cluster import vq
# Creating data
c1 = np.random.randn(100, 2) + 5 
c2 = np.random.randn(30, 2) - 5 
c3 = np.random.randn(50, 2)
# Pooling all the data into one 180 x 2 array 
data = np.vstack([c1, c2, c3])
# Calculating the cluster centroids and variance 
# from kmeans
centroids, variance = vq.kmeans(data, 3)
# The identified variable contains the information 
# we need to separate the points in clusters
# based on the vq function.
identified, distance = vq.vq(data, centroids)
# Retrieving coordinates for points in each vq # identified core
vqc1 = data[identified == 0]
vqc2 = data[identified == 1]
vqc3 = data[identified == 2]


plt.subplot(121)

print centroids
print variance
print identified
print distance
plt.scatter(c1[:,0],c1[:,1])
plt.scatter(c2[:,0],c2[:,1])
plt.scatter(c3[:,0],c3[:,1])
plt.subplot(122)
plt.scatter(vqc1[:,0],vqc1[:,1])
plt.scatter(vqc2[:,0],vqc2[:,1])
plt.scatter(vqc3[:,0],vqc3[:,1])
plt.show()

'''

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, squareform 
import scipy.cluster.hierarchy as hy


# Creating a cluster of clusters function
def clusters(number = 20, cnumber = 5, csize = 10):
# Note that the way the clusters are positioned is Gaussian randomness. 
	rnum = np.random.rand(cnumber, 2)
	rn = rnum[:,0] * number
	rn = rn.astype(int)
	rn[np.where(rn < 5 )] = 5
	rn[np.where(rn > number/2. )] = round(number / 2., 0)
	ra = rnum[:,1] * 2.9 
	ra[np.where(ra < 1.5)] = 1.5
	cls = np.random.randn(number, 3) * csize
	# Random multipliers for central point of cluster 
	rxyz = np.random.randn(cnumber-1, 3)
	for i in xrange(cnumber-1):
		tmp = np.random.randn(rn[i+1], 3)
		x = tmp[:,0] + ( rxyz[i,0] * csize ) 
		y = tmp[:,1] + ( rxyz[i,1] * csize ) 
		z = tmp[:,2] + ( rxyz[i,2] * csize ) 
		tmp = np.column_stack([x,y,z])
		cls = np.vstack([cls,tmp])
	return cls

# Generate a cluster of clusters and distance matrix. 
cls = clusters()
print cls
D = pdist(cls[:,0:2])
D = squareform(D)
print 'hi'
print D
# Compute and plot first dendrogram. 
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6]) 
Y1 = hy.linkage(D, method='complete') 
cutoff = 0.3 * np.max(Y1[:, 2])
Z1 = hy.dendrogram(Y1, orientation='right', color_threshold=cutoff) 
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
# Compute and plot second dendrogram. 
ax2 = fig.add_axes([0.3,0.71,0.6,0.2]) 
Y2 = hy.linkage(D, method='average') 
cutoff = 0.3 * np.max(Y2[:, 2])
Z2 = hy.dendrogram(Y2, color_threshold=cutoff) 
ax2.xaxis.set_visible(False) 
ax2.yaxis.set_visible(False)
# Plot distance matrix.
ax3 = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
D = D[idx1,:]
print 'second'
print D
D = D[:,idx2]
print 'third'
print D

ax3.matshow(D, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu) 
ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)
# Plot colorbar. 
fig.savefig('cluster_hy_f01.pdf', bbox = 'tight')

'''
def group(data, index):
	number = np.unique(index) 
	groups = []
	for i in number:
		groups.append(data[index == i]) 
	return groups

# Creating a cluster of clusters 
cls = clusters()
# Calculating the linkage matrix
Y = hy.linkage(cls[:,0:2], method='complete')
# Here we use the fcluster function to pull out a
# collection of flat clusters from the hierarchical
# data structure. Note that we are using the same
# cutoff value as in the previous example for the dendrogram 
# using the 'complete' method.
cutoff = 0.3 * np.max(Y[:, 2])
index = hy.fcluster(Y, cutoff, 'distance')
# Using the group function, we group points into their 
# respective clusters.
groups = group(cls, index)
# Plotting clusters
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
colors = ['r', 'c', 'b', 'g', 'orange', 'k', 'y', 'gray'] 
for i, g in enumerate(groups):
	i = np.mod(i, len(colors))
	ax.scatter(g[:,0], g[:,1], c=colors[i], edgecolor='none', s=50) 
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)
fig.savefig('cluster_hy_f02.pdf', bbox = 'tight')

'''

