

# ------------------------------------------ 3) Loss and Optimization -------------------------------------------------------

"""
As great as it is that we have state persistant tf.Variables, the Weights and Biases,
unless we are supremely lucky, these are not anywhere near what the actual 
Weight and Bias values should be to be making correct predictions!

In order to move the Weights and Biases closer to useful values, we first need to figure out:
    1) How wrong are our current Variable values?
    2) How we going to change the values to bring the output predictions closer to actual values?

Which brings us to the terms:
    1) Loss 
    2) Optimization

These two workhorses the most critical portion of training a model, and what makes AI what it is!
"""
# ----------------------------------------------- Loss -----------------------------------------------------------
"""
--> Loss
Basically Loss is the "absolute" value of how wrong the model is, and a loss of 0 indicated the model is not wrong
This value approaching 0 is the goal of all the math behind a model, and what the OPTIMIZER seeks to achieve.
If you are interested in learning more about loss, feel free to read up on it, but for now
we are going to focus on when and where we implement this!

There are many different options to chose from when choosing a loss function, and they can be found here:
https://www.tensorflow.org/api_docs/python/tf/losses

For now, to get the idea of loss, we are just going to look at the simple tf.reduce_mean()
but, when picking a loss function for your Graph you will want to do some research into the merits of various methods

Below is a short example to show what loss is andhow to use a basic function
"""

def LossExample():
    import tensorflow as tf 

    # -------- Python Variables -------------


    # -------- TensorFlow Variables
    # because loss is used to determine the difference between a calcuated prediciton and actual value
    # we will be defining a y_actual and y_calc as our values to compare
    y_1d_actual = tf.placeholder(tf.float32, shape=[1])
    y_1d_calc = tf.placeholder(tf.float32, shape=[1])
    loss_1d = tf.reduce_mean(y_1d_actual - y_1d_calc) # taking the difference between these

    # Next, lets take a look at higher dimnension output tensor
    # say these represent two weights leaving a neural net
    y_2d_actual = tf.placeholder(tf.float32, shape=[1,2])
    y_2d_calc = tf.placeholder(tf.float32, shape=[1,2])
    loss_2d = tf.reduce_mean(y_2d_actual - y_2d_calc)

    # If we really wanted to highlight the loss, we can take the square of the differnce like so
    loss_sq = tf.reduce_mean(tf.square(y_1d_actual - y_1d_calc))

    # Finally, a more advanced loss function look something like this
    act_output = tf.placeholder(tf.float32, shape=[None, 6]) # here we are defining the output to be a tensor of 6 classifications
    calc_output = tf.placeholder(tf.float32, shape=[None, 6]) 

    # additonally, you might notice we are feeding an arg 'logits' the calcualted output, and you might be wondering, what are logits?
    # saying something is a logit just notes that the values in the Tensor ARE NOT on a 0-1 scale, and as such the values are un scaled
    #   ex: [3.27, .985, .1.27] (logits) vs [.2, .2, .6] (not logits)


    softmax = tf.nn.softmax_cross_entropy_with_logits(logits=calc_output, labels=act_output)
    cross_entropy = tf.reduce_mean(softmax) # notice we are still calling tf.reduce mean
    with tf.Session() as sess:
        
        #     Graph_output = sess.run(thing_to_do, data_to_do_it_on)
        loss = sess.run(loss_1d, feed_dict={ y_1d_actual:[7], y_1d_calc:[8] }) # 1D loss
        print("1D Loss:", loss) # 1D Loss: -1 # loss of -1 makes sense, nothing fancy

        loss = sess.run(loss_2d, feed_dict={ y_2d_actual:[[1, 4]], y_2d_calc:[[2, 9]]})
        print("2D Loss:", loss) # 2D Loss: -3.0 # cool!
        # As we can see from a loss of -3, where the difference of 1-2 and 4-9 is 6, with two values, the loss is a sum of difference!

        loss = sess.run(loss_sq, feed_dict={ y_1d_actual:[4], y_1d_calc:[10] })
        print("SQ Loss:", loss) # SQ Loss: 36.0

        loss = sess.run(cross_entropy, feed_dict={act_output:[[4, 3, 5, 6, 8, 1]], calc_output:[[6, 5, 4, 3, 2, 1]]})
        print("Softmax Loss:", loss) # Softmax Loss: 80.317215


#LossExample()
"""
^^ to run the above example ^^

Great, thats enough examples of loss, but the main idea here is there area ton of different ways to define Loss!
"""



# ---------------------------------------------- Optimization ----------------------------------------------------------

"""
Now that we are situated with that, the next step is figuring out how to get Loss as close to zero as possible!

Here is where optimization comes in!
Much like loss, there is more than one way to do this, and different network architectures respond better to different optimizers
but for now we are going to use a:
    GradientDescentOptimizer 
to change the Weights and Biases to reduce Loss

And here is where, finally, we see the word defining what all this has been leading up to: TRAINing!!
To implement an optimizer, we define something like so:
    training_step = tf.train.OptimizingFunction().minimize(loss)
"""

#---------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------- E*X*A*M*P*L*E ---------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

# linking the loss and the optimizer together is done like so:
# (note this wont run as no inputs or labels have been defined)
def LossOptimization():
    learning_rate = 0.5 # each optimizer has learning rates that work best for it, this is one of the "python" variables you can adjust
    loss = tf.reduce_mean(tf.square(y_real - y_pred))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate)
    train = optimizer.minimize(loss)

    # Sweet! Now to use this in a tf.Session(), we would do something like so
    with tf.Session() as sess:
        for training_round in range(1000):
            sess.run(train, feed_dict:{x: _inputs, y: _labels})



"""
Great! We now have the tools to train a model!

What we have done in this section is:
    0) Figured out a metric to measure how wrong our model is (Loss)
    1) Implemented a way to minimize that loss and make our predictions more accurate (Optimization)
    2) Combining these together we have created a Training sequence!

At this point, there are only two more things we need to have a fully functional start to finish model!

"""



