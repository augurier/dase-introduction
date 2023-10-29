def inference(input_tensor, is_training, train, regularizer,is_eval=False):
    with tf.variable_scope('layerl-conv'):
        convl_weight = tf.get_variable('weight',[CONV1_SIZE, CONV1_SIZE, NUM_CHANNEIS, CONV1_DEEP],initializer = tf.truncated_normal_initializer(stddev=0.01))
        convl = tf.nn.conv2d(input_tensor,convl_weight,strides=[1,1,1,1],padding="SAME")
        convl_bn = batch_norm_wrapper(convl, CONVI_DEEP, is_training,1)
        relul = tf.nn.relu(convl_bn)
    with tf.name_scope('layer1-pool'):
        pooll = tf.nn.max_pool(relul, ksize=[1,2,2,1], strides=[1,2,2,1],cpadding="SAME")
    #with tf.variable_scope('layer2-conv'):

    with tf.variable_scope('layer7-fc'):
        fc3_weights = tf.get_variable('weight', [FC_SIZE2,FC_SIZE3], initializer = tf.truncated_normal_initializer(stddev-0.1))
        fc3_biases = tf.get_variable('bias',[FC_SIZE3], initializer = tf.truncated_normal_initializer(stddev=0.1))
        if regularizer !=None:
            tf.add_to_collection('losses', regularizer(fc3_weights))
        logit = tf.matmul(fc2_final,fc3_weights) + fc3_biases