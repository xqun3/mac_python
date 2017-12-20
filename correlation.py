import os
pdbfile=open('pdbname.txt')
correlation_file=open('correlation.txt','a')
pdbname=pdbfile.readlines()
N=len(pdbname)
for i in range(N-1):
	fix_=pdbname[i].split('\n')[0]
	#correlation_file.write(fix_+'\n')
	for j in range(i+1,N):
		fix_=pdbname[i].split('\n')[0]
		mov_=pdbname[j].split('\n')[0]
		os.system('sastbx.superpose fix={} mov={} | grep Correlation > log.txt'.format(fix_,mov_))
		logfile=open('log.txt')
		line=logfile.readline()
		data=line.split('\n')[0].split(' ')[-1]
		correlation_file.write(data+',')
		processfile=open('out.txt','w')
		processfile.write('{},{}'.format(i,j))
		processfile.close()
	correlation_file.write('\n')
