from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# #Prepare to feed input, i.e. feed_dict and placeholders
# w1 = tf.placeholder("float", name="w1")
# w2 = tf.placeholder("float", name="w2")
# b1= tf.Variable(2.0,name="bias")
# feed_dict ={w1:4,w2:8}

# #Define a test operation that we will restore
# w3 = tf.add(w1,w2)
# w4 = tf.multiply(w3,b1,name="op_to_restore")
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())

# #Create a saver object which will save all the variables
# saver = tf.train.Saver()

# #Run the operation by feeding input
# print sess.run(w4,feed_dict)
# #Prints 24 which is sum of (w1+w2)*b1 

# #Now, save the graph
# saver.save(sess, '/Users/dongxq/Desktop/my_test_model',global_step=1000)

# import tensorflow as tf

# sess=tf.Session()    
# #First let's load meta graph and restore weights
# saver = tf.train.import_meta_graph('/Users/dongxq/Desktop/my_test_model-1000.meta')
# saver.restore(sess,tf.train.latest_checkpoint('/Users/dongxq/Desktop/'))


# # Access saved Variables directly
# print(sess.run('bias:0'))
# # This will print 2, which is the value of bias that we saved


# # Now, let's access and create placeholders variables and
# # create feed-dict to feed new data

# graph = tf.get_default_graph()
# w1 = graph.get_tensor_by_name("w1:0")
# w2 = graph.get_tensor_by_name("w2:0")
# feed_dict ={w1:13.0,w2:17.0}

# #Now, access the op that you want to run. 
# op_to_restore = graph.get_tensor_by_name("op_to_restore:0")

# print sess.run(op_to_restore,feed_dict)
# #This will print 60 which is calculated 


import argparse
import os
import sys
import time

from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.examples.tutorials.mnist import mnist
import fully_connected_feed as fcf

# parser = fcf.parser
parser = argparse.ArgumentParser()
FLAGS = parser.parse_args()
parser.add_argument(
      '--batch_size',
      type=int,
      default=100,
      help='Batch size.  Must divide evenly into the dataset sizes.'
  )




sess=tf.Session() 
saver = tf.train.import_meta_graph('/tmp/tensorflow/mnist/logs/fully_connected_feed/model.ckpt-1999.meta')
saver.restore(sess,tf.train.latest_checkpoint('/tmp/tensorflow/mnist/logs/fully_connected_feed/'))

data_sets = input_data.read_data_sets('/Users/dongxq/MNIST_data')

graph = tf.get_default_graph()
'''

print(sess.run('softmax_linear/biases:1'))
images_placeholder, labels_placeholder = fcf.placeholder_inputs(100)

logits = mnist.inference(images_placeholder,128,32)
# Add to the Graph the Ops for loss calculation.
loss = mnist.loss(logits, labels_placeholder)

# Add to the Graph the Ops that calculate and apply gradients.
train_op = mnist.training(loss, 0.01)
'''
# Add the Op to compare the logits to the labels during evaluation.
# eval_correct = mnist.evaluation(logits, labels_placeholder)

# op_eval_correct = graph.get_tensor_by_name("op_eval_correct:0")

op = graph.get_tensor_by_name('softmax_linear/add:0')

# op = graph.get_operations()
print(op)

# fcf.do_eval(sess,op_eval_correct, images_placeholder,labels_placeholder,data_sets.validation)

# print(sess.run('softmax_linear/biases:0'))
