import tensorflow as tf

# c1 = tf.constant(3.)
c1 = tf.Variable(3.)
with tf.GradientTape() as tape:
    result = tf.square(c1)
    print(f"c1**2={result}")
    gradient = tape.gradient(result, c1)
    print(gradient)
