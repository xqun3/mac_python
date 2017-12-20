# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import time
import numpy as np
import tensorflow as tf
import argparse
import fnn
import os
import exceptions

# import tempfile

FLAGS = None

# Constants used for dealing with the files, matches convert_to_records.
# TRAIN_FILE = 'train.tfrecords'
# TEST_FILE = 'test.tfrecords'

TRAIN_FILE = 'train_shulffle.tfrecords'
TEST_FILE = 'test_shulffle.tfrecords'

def inputs(train, batch_size, num_epochs):
	"""Reads input data num_epochs times.
	Args:
	train: Selects between the training (True) and validation (False) data.
	batch_size: Number of examples per returned batch.
	num_epochs: Number of times to read the input data, or 0/None to
	   train forever.
	Returns:
	A tuple (images, labels), where:
	* images is a float tensor with shape [batch_size, mnist.IMAGE_PIXELS]
	  in the range [-0.5, 0.5].
	* labels is an int32 tensor with shape [batch_size] with the true label,
	  a number in the range [0, mnist.NUM_CLASSES).
	Note that an tf.train.QueueRunner is added to the graph, which
	must be run using e.g. tf.train.start_queue_runners().
	"""
	if not num_epochs: num_epochs = None
	filename = os.path.join(FLAGS.train_dir,
	                      TRAIN_FILE if train else TEST_FILE)

	with tf.name_scope('input'):
		filename_queue = tf.train.string_input_producer([filename],num_epochs=num_epochs)

		# Even when reading in multiple threads, share the filename
		# queue.
		image, label = fnn.read_and_decode(filename_queue)

		# Shuffle the examples and collect them into batch_size batches.
		# (Internally uses a RandomShuffleQueue.)
		# We run this in two threads to avoid being a bottleneck.
		images, sparse_labels = tf.train.shuffle_batch(
		    [image, label], batch_size=batch_size, num_threads=2,
		    capacity=1000 + 3 * batch_size,
		    # Ensures a minimum amount of shuffling of examples.
		    min_after_dequeue=1000)
		# print images, sparse_labels

	return images, sparse_labels

def run_training():
	"""Train MNIST for a number of steps."""

	# Tell TensorFlow that the model will be built into the default Graph.
	count = 0
	testcount = 0
	with tf.Graph().as_default():
	# Input images and labels.
		
		x, y = inputs(train=True, batch_size=FLAGS.batch_size,
                            num_epochs=FLAGS.num_epochs)
		x_test,y_test = inputs(train=False, batch_size=FLAGS.batch_size,
                            num_epochs=FLAGS.num_epochs)
		
		images = tf.placeholder(tf.float32, [None,144])
		labels = tf.placeholder(tf.int64, [None])

		# Build a Graph that computes predictions from the inference model.
		logits = fnn.inference(images,
		                         FLAGS.hidden1,
		                         FLAGS.hidden2)
		out=tf.nn.softmax(logits=logits)

		# Add to the Graph the loss calculation.


		loss = fnn.loss(logits, labels)

		# Add to the Graph operations that train the model.
		train_op = fnn.training(loss, FLAGS.learning_rate)

		# The op for initializing the variables.
		init_op = tf.group(tf.global_variables_initializer(),
		                   tf.local_variables_initializer())


		# Create a session for running operations in the Graph.
		sess = tf.Session()
		
		# Initialize the variables (the trained variables and the
		# epoch counter).
		sess.run(init_op)

		# save_path = saver.save(sess, "/Users/dongxq/Desktop/disulfide/model2.ckpt")

		# Start input enqueue threads.
		coord = tf.train.Coordinator()
		threads = tf.train.start_queue_runners(sess=sess, coord=coord)

		# print (out,labels)
		# print (labels)
		abcd=tf.one_hot(labels,axis=-1,depth=2)

		correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(abcd, 1))
		correct_prediction = tf.cast(correct_prediction, tf.float32)
		accuracy = tf.reduce_mean(correct_prediction)

		try:
			step = 0
			while not coord.should_stop():
				start_time = time.time()

				# Run one step of the model.  The return values are
				# the activations from the `train_op` (which is
				# discarded) and the `loss` op.  To inspect the values
				# of your ops or variables, you may include them in
				# the list passed to sess.run() and the value tensors
				# will be returned in the tuple from the call.
				x_,y_ = sess.run([x,y])
				y_=y_.reshape((100))

				loss_value, _ = sess.run([loss,train_op],feed_dict={images:x_,labels:y_})

				duration = time.time() - start_time
				

				# Print an overview fairly often.
				if step % 100 == 0 :
					print('Step %d: loss = %.2f (%.3f sec)' % (step, loss_value, duration))
					with open('abcd_test.txt','a') as testf:
						for testi in range(30):

							x_test_,y_test_=sess.run([x_test,y_test])
							y_test_ = y_test_.reshape((100))
							test_loss,accuracy_,abcd_,out_= sess.run([loss,accuracy,abcd,out],feed_dict={images:x_test_,labels:y_test_})
					  		print('Step %d: test loss  = %.2f (%3f sec),accuracy:%.2f'% (testi, test_loss,
						                                             duration,accuracy_))
					  	 	#print (abcd_,out_)
					  	
					  		# if [1,0] in abcd_:
					  		# 	print(abcd_,out_)
					  		# 	raise Exception('hello')
					  		testcount += 100
					  		testf.write(str(abcd_)+'\n')
							testf.write(str(testcount)+'\n')
					  		

					  	with open('abcd.txt','a') as f:
					  		count += 100
							f.write(str(abcd_)+'\n')
							f.write(str(count)+'\n')
					
					
					data = np.load(FLAGS.Validation_path)
					out_ = sess.run(out,feed_dict={images:data.reshape((len(data),144))})
					# print(out_)
					id_ord = np.load(FLAGS.Validation_ord_path)
					for outi in range(len(out_)):
						if(out_[outi][1] > out_[outi][0]):
							print(id_ord[outi],out_[outi])
					
			
				step += 1
			

				
		except tf.errors.OutOfRangeError:
			print('Done training for %d epochs, %d steps.' % (FLAGS.num_epochs, step))
		finally:
			data1 = np.load('/Users/dongxq/Desktop/disulfide/validation_ssbond/full_ssbonds_distance_map.npy')
			out_ = sess.run(out,feed_dict={images:data1.reshape((len(data1),144))})
			count = 0
			for outi in range(len(out_)):
				if(out_[outi][1] > out_[outi][0]):
					count+=1
			print(len(data1))
			print(count)
			print('accuracy is %2f'%(count/len(data1)))
			# When done, ask the threads to stop.
			coord.request_stop()

		# Wait for threads to finish.
		coord.join(threads)
		sess.close()

# def run_testing():



def main(_):
	run_training()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--learning_rate',
		type=float,
		default=0.01,
		help='Initial learning rate.'
	)
	parser.add_argument(
		'--num_epochs',
		type=int,
		default=2,
		help='Number of epochs to run trainer.'
	)
	parser.add_argument(
		'--hidden1',
		type=int,
		default=128,
		help='Number of units in hidden layer 1.'
	)
	parser.add_argument(
		'--hidden2',
		type=int,
		default=32,
		help='Number of units in hidden layer 2.'
	)
	parser.add_argument(
		'--batch_size',
		type=int,
		default=100,
		help='Batch size.'
	)
	parser.add_argument(
		'--train_dir',
		type=str,
		default='/Users/dongxq/Desktop/disulfide/neuro_input/',
		help='Directory with the training data.'
	)
	parser.add_argument(
		'--Validation_path',
		type=str,
		default='/Users/dongxq/Desktop/disulfide/other_set_map/7635_refine_4_full_possible_ssbond_nr.npy',
		help='path with the Validation data.'
	)
	parser.add_argument(
		'--Validation_ord_path',
		type=str,
		default='/Users/dongxq/Desktop/disulfide/other_set_map/7635_refine_4_possible_ssbond_id_nr.npy',
		help='path with the Validation data.'
	)
	FLAGS, unparsed = parser.parse_known_args()
	tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)