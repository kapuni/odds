import tensorflow as tf

state = tf.Variable(0, name='counter')
one = tf.constant
new_value = tf.add(state, one)
upstate = tf.assign(state, new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(upstate)
        print(sess.run(state))