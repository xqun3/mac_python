# -*- coding:utf-8 -*-
'''
import os

def child():
	print 'hello from child', os.getpid()
	os._exit(0)

def parent():
	for i in range(10):
		newpid = os.fork()
		if newpid == 0:
			child()
		else:
			print 'hello from parent', os.getpid(), newpid
		if raw_input == 'q':break

parent()
'''
'''

import os, time

def counter(count):
	for i in range(count):
		time.sleep(1)
		print '[%s] => %s' % (os.getpid(),i)

for i in range(5):
	pid = os.fork()
	if pid != 0:
		print 'process %d spawned' % pid
	else:
		counter(5)
		os._exit(0)

print 'Main process exiting'
'''
'''
import os 

parm = 0
while True:
	parm += 1
	pid = os.fork()
	if pid == 0:
		os.execlp('python','python','child.py',str(parm))
		assert False, 'error starting program'
	else:
		print 'child is', pid
		if raw_input() == 'q':break

'''
'''
import thread

def child(tid):
	print 'hello from thread', tid

def parent():
	i = 0
	while True:
		i += 1
		thread.start_new_thread(child, (i,))
		if raw_input() == 'q':break

parent()
'''
'''
import thread, time

def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		print('[%s] => %s' % (myId, i))

for i in range(5):
	thread.start_new_thread(counter,(i,5))

time.sleep(6)
print 'main thread exiting.'
'''
'''
import thread, time

def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		mutex.acquire()
		print('[%s] => %s' % (myId, i))
		mutex.release()

mutex = thread.allocate_lock()
for i in range(5):
	thread.start_new_thread(counter, (i,5))

time.sleep(6)
print 'main thread exiting.'
'''
'''
import thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]
def counter(myId, count): 
	for i in range(count):
		stdoutmutex.acquire() 
		print('[%s] => %s' % (myId, i)) 
		stdoutmutex.release()
	exitmutexes[myId].acquire() # signal main thread
for i in range(10): 
	thread.start_new_thread(counter, (i, 100))
for mutex in exitmutexes:
	while not mutex.locked(): 
		pass
print 'Main thread exiting.'
'''
'''
import thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10
def counter(myId, count): 
	for i in range(count):
		stdoutmutex.acquire() 
		print('[%s] => %s' % (myId, i)) 
		stdoutmutex.release()
	exitmutexes[myId] = True # signal main thread
for i in range(10): 
	thread.start_new_thread(counter, (i, 100))
while False in exitmutexes: 
	pass 
print('Main thread exiting.')

'''
'''
import thread, time
stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]
def counter(myId, count, mutex): 
	for i in range(count):
	time.sleep(1 / (myId+1)) 
	with mutex:
		print('[%s] => %s' % (myId, i)) 
	exitmutexes[myId].acquire()
# shared object passed in
# diff fractions of second
# auto acquire/release: with
# global: signal main thread
for i in range(numthreads): 
	thread.start_new_thread(counter, (i, 5, stdoutmutex))
while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25) 
print('Main thread exiting.')
'''
'''

import threading
 
class Mythread(threading.Thread):
	def __init__(self, myId, count, mutex):
		self.myId = myId
		self.count = count
		self.mutex = mutex 
		threading.Thread.__init__(self)
	def run(self):
		for i in range(self.count):
			with self.mutex:
				print('[%s] => %s' % (self.myId, i))
stdoutmutex = threading.Lock() 
threads = []
for i in range(10):
	thread = Mythread(i, 100, stdoutmutex) 
	thread.start()
	threads.append(thread)
for thread in threads: 
	thread.join()
print('Main thread exiting.')
'''

import threading, thread 

def action(i):
	print(i ** 32)
# subclass with state
class Mythread(threading.Thread): 
	def __init__(self, i):
		self.i = i
		threading.Thread.__init__(self) 
	def run(self):
		print(self.i ** 32) 

#Mythread(2).start()
# pass action in
#threads = threading.Thread(target=(lambda: action(2))) 
#threads.start()
# same but no lambda wrapper for state
#threading.Thread(target=action, args=(2,)).start()
# basic thread module
#thread.start_new_thread(action, (2,))
'''

class Power:
	def __init__(self, i):
		self.i = i 
	def action(self):
		print(self.i ** 32)
obj = Power(2) 
threading.Thread(target=obj.action).start()
# nested scope to retain state
def action(i): 
	def power():
		print(i ** 32) 
	return power
threading.Thread(target=action(2)).start()
# both with basic thread module
thread.start_new_thread(obj.action, ()) 
thread.start_new_thread(action(2), ())

'''
'''
import threading, time 
count = 0
def adder(): 
	global count
	count = count + 1 
	time.sleep(0.5) 
	count = count + 1
	print count
threads = []
for i in range(100):
# update a shared name in global scope
# threads share object memory and global names
	thread = threading.Thread(target=adder, args=()) 
	thread.start()
	threads.append(thread)

for thread in threads: 
	thread.join() 
	

print(count)
'''
'''
import threading, time

count = 0

def adder(addlock):
	global count 
	with addlock:
		count = count + 1 
	time.sleep(0.5)
	with addlock:
		count = count + 1
addlock = threading.Lock() 
threads = []
for i in range(1000):
# auto acquire/release around stmt # only 1 thread updating at once
	thread = threading.Thread(target=adder, args=(addlock,)) 
	thread.start()
	threads.append(thread)
#for thread in threads: thread.join() 
print(count)

'''

numconsumers = 2 
numproducers = 4 
nummessages = 4

import thread, queue, time 
safeprint = thread.allocate_lock() 
dataQueue = queue.Queue()
def producer(idnum):
	for msgnum in range(nummessages):
		time.sleep(idnum)
		dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))
		
def consumer(idnum): 
	while True:
		time.sleep(0.1) 
		try:
			data = dataQueue.get(block=False) 
		except queue.Empty:
			pass 
		else:
			with safeprint:
				print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
	for i in range(numconsumers):
		thread.start_new_thread(consumer, (i,)) 
	for i in range(numproducers):
		thread.start_new_thread(producer, (i,)) 
	time.sleep(((numproducers-1) * nummessages) + 1) 
	print('Main thread exit.')