# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import time
import numpy as np
import tensorflow as tf
import argparse
import os
import exceptions
import cnn

FLAGS = None

parser = cnn.parser
parser.add_argument(
	'--learning_rate',
	type=float,
	default=0.01,
	help='Initial learning rate.'
)

parser.add_argument(
	'--log_dir',
	type=str,
	default=os.path.join(os.getenv('TEST_TMPDIR', '/Users/dongxq/Desktop/disulfide'),
	                   'new_train_cnn/logs/'),
	help='Directory to put the log data.'
 )
parser.add_argument(
	'--train_dir',
	type=str,
	default='/Users/dongxq/Desktop/disulfide/neuro_input/',
	help='Directory with the training data.'
)

def run_training():
	
	with tf.Graph().as_default():
	    # Generate placeholders for the images and labels.
		x,y = cnn.inputs(train=True, batch_size=FLAGS.batch_size,
			num_epochs=FLAGS.num_epochs)
		x_test,y_test = cnn.inputs(train=False, batch_size=FLAGS.batch_size,
			num_epochs=FLAGS.num_epochs)
		with tf.name_scope('input'):
			images_placeholder = tf.placeholder(tf.float32, [None,12,12,1],name='image')
			labels_placeholder = tf.placeholder(tf.int64, [None],name='labels')
			print(images_placeholder, labels_placeholder)
			tf.summary.image('images', images_placeholder)
		# print (images_placeholder,labels_placeholder)

		logits = cnn.inference(images_placeholder)
		# print('here')

		out=tf.nn.softmax(logits=logits)

		loss = cnn.loss(logits, labels_placeholder)
		# Add to the Graph operations that train the model.
		train_op = cnn.training(loss, FLAGS.learning_rate)

		# The op for initializing the variables.
		init_op = tf.group(tf.global_variables_initializer(),
			tf.local_variables_initializer())

		# Build the summary Tensor based on the TF collection of Summaries.
		summary = tf.summary.merge_all()

		# Create a saver for writing training checkpoints.
		saver = tf.train.Saver()
		
		# Create a session for running operations in the Graph.
		sess = tf.Session()
		# Instantiate a SummaryWriter to output summaries and the Graph.
		summary_writer = tf.summary.FileWriter(FLAGS.log_dir, sess.graph)
		
		# Initialize the variables (the trained variables and the
		# epoch counter).
		sess.run(init_op)

		# Start input enqueue threads.
		coord = tf.train.Coordinator()
		threads = tf.train.start_queue_runners(sess=sess, coord=coord)

		one_hot_labels = tf.one_hot(labels_placeholder,axis=-1,depth=2)

		correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(one_hot_labels, 1))
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
				# feed_dict = fill_feed_dict(sess,images_placeholder,labels_placeholder)
				# y_=y_.reshape((100))
				#x,y = new_fnn.inputs(train=True, batch_size=FLAGS.batch_size,num_epochs=FLAGS.num_epochs)
				
				feed_dict=cnn.fill_feed_dict(images_placeholder,
					labels_placeholder,x,y,sess=sess)
				loss_value, _ = sess.run([loss,train_op],feed_dict=feed_dict)
				# print('step',loss_value)
				duration = time.time() - start_time
				# Print an overview fairly often.
				summary_str = sess.run(summary, feed_dict=feed_dict)
				summary_writer.add_summary(summary_str, step)
				summary_writer.flush()
				if step % 100 == 0 :
					print('Step %d: loss = %.2f (%.3f sec)' % (step, loss_value, duration))
					checkpoint_file = os.path.join(FLAGS.log_dir, 'model.ckpt')
					saver.save(sess, checkpoint_file, global_step=step)
					for testi in range(30):
						feed_dict = cnn.fill_feed_dict(images_placeholder,labels_placeholder,
							x_test,y_test,sess=sess)
						test_loss,accuracy_,abcd_,out_= sess.run([loss,accuracy,one_hot_labels,out],
							feed_dict=feed_dict)
						print('Step %d: test loss  = %.2f (%3f sec),accuracy:%.2f'% (testi, test_loss,
							duration,accuracy_))
				step += 1				
		except tf.errors.OutOfRangeError:
			print('Done training for %d epochs, %d steps.' % (FLAGS.num_epochs, step))
		finally:
			# When done, ask the threads to stop.
			checkpoint_file = os.path.join(FLAGS.log_dir, 'model.ckpt')
			saver.save(sess, checkpoint_file, global_step=step)
			coord.request_stop()

		# Wait for threads to finish.
		coord.join(threads)
		sess.close()


def main(_):
	print(FLAGS.log_dir)
	if tf.gfile.Exists(FLAGS.log_dir):
		tf.gfile.DeleteRecursively(FLAGS.log_dir)
	tf.gfile.MakeDirs(FLAGS.log_dir)
	run_training()

if __name__ == '__main__':
	FLAGS= parser.parse_args()
	tf.app.run()
