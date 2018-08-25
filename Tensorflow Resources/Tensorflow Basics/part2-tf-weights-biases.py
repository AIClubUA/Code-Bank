


# ------------------------------------------ 2) Weights and Biases -------------------------------------------------------

"""
Now that we are confidently feeding data to a tf.Session ($ python your-script.py, $ tf.Session() tf.Graph)
its time to take the first step in unleashing the pinacle of humanities math and computational achievements!

To ramp up to the juicy math, it will help to get more experience defining graphs and manipulating data
within the Graph environment.

For starters, (if you didnt know) TF utilizes Linear Algebra operations on matricies,
these operations require two things:
    1) Values to do them on
    2) Specification of what operation needs to be done

Below we will be focusing on the Values required to do operations.
"""

# ------------------------------------------------ tf.Variables ----------------------------------------------------------
"""
Into to tf.Variables:

tf.Variables are very similar to tf.placeholders, but have a few notable differences

First, tf.Variables are values that maintain their state in between callings of sess.run()
What this means is that when you call sess.run() the value a tf.Variable ends at,
will be the starting value of that tf.Variable the next time sess.run() is called.

This differs from tf.placeholders, as placeholders lose their contents at the end of a sess.run() call

If we were to look at the final example in part1-tf-basics.py, and implemented a tf.Variable and printed its contents
every time the loop iterated, the tf.Variable values would stay constant while the placeholder inputs were changing

This is interesting no doubt, but why are tf.Variables useful?
Well they serve the very important function of retaining the Weights and Biases of a model!
"""

"""
Cool.... but what the heck is the Weight and Bias?!?

We want to think of Weights and Biases in the space of
    y = mx + b
or 
    pred = Weight*x + bias

--> Weight
The weight is matrix(tensor) of values (in the context of AI model) with the shape:
    [num_output_items, num_possible_outputs]
or
    [num_neurons_out_layer, num_classes]

... the general idea is whatever the output shape of your data is X the number of possible targets
The values of these will eventually be subjected to Matrix Multiplication to extract a useful "answer" from the model!

But what IS the Weight?!
In short its how large of a number an input is multiplied by.
For example, say you want to predict if you will go to class on any given day of the week.
Lets say your model has 7 neurons, one for each day of the week.
When you want to run your model you give it a row of data like below (suppose today is Tuesday):
           s  m   t   w   t   f  s
data    = [0, 0,  1,  0,  0,  0, 0] # tuesday column is 1 to indicate today, all others 0
weights = [0, 1, .9, .8, .5, .1, 0]
d x W   = [0, 0, .9,  0,  0,  0, 0] --> .9 probability of goin to class

Now consider, that it is Sunday
           s  m   t   w   t   f  s
data    = [1, 0,  0,  0,  0,  0, 0]
weights = [0, 1, .9, .8, .5, .1, 0]
d x W   = [0, 0,  0,  0,  0,  0, 0] --> 0 probability of going to class


--> Bias
The bias is the 'y' offset value of the prediction function.
Remember
    y = mx + b
or 
    pred = Weight*x + bias

In a linear model, it would be considered the y-intercept of the plotted graph

For our purposes, it is defined in the shape of
    [num_possible_outputs]
or
    [num_classes]
depending on what makes more sense in your head.
Either way, it will have the same dimensionality as the 2nd shape dimension of the Weights!


Now, lets put this information into action and define some Weight and Bias variables below!
"""
import tensorflow as tf 

# --------- WEIGHTS ---------------
# Disclaimer! There are two ways to define variables, and some places do it one way, while others do it another
# I believe get_variable is the "better" way to do things, but both achieve the same ultimate goal
# 1) using tf.Variable(), there are two ways to init
layer_size = 52
num_classes = 2
# 1.1) Init the wights to all zeros
W = tf.Variable(tf.zeros([layer_size, num_classes]))
# 1.2) Use tf.truncated_normal to create initial values that will be modified as the model trains
W = tf.Variable(tf.truncated_normal([layer_size, num_classes], mean=0, stddev=0.1))

# 2) using tf.get_variable
# explicitly defining to zeros
W = tf.get_variable("weight1", [layer_size, num_classes], dtype=tf.int32, initializer=tf.zeros_initializer)
# definfing like this defaults initial values to tf.float32 types of random tf.glorot_uniform_initializer values
W = tf.get_variable("weight2", [layer_size, num_classes])


# ---------- BIASES ---------------
# Biases use the same techniques as above but lose one level of dimensionality
b = tf.Variable(tf.zeros([num_classes]))
# or
b = tf.get_variable("biases", [num_classes])
# the other two methods are applicable, just be sure to specify the shape as [num_classes] !

"""
Now the final step to using these fresh tf.Variables is to initialize them when the tf.Session() starts up!

We do that like so:

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    ################
    # everything else
    ################
"""



"""
Being able to define weights and biases is great, but how do we actually use them in the TensorFlow realm?

For starters, lets do a very simple Matrix Multiplication operation, aka 'matmul'
Below is a stand alone script
"""
#---------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------- E*X*A*M*P*L*E ---------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#import tensorflow as tf # We already imported this way far above
import numpy as np 

# ----- Python Vars --------
layer_size = 10
num_classes = 1
x_vals = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] # note len() of [0] = 10 to fit the layer_size
x_sample = np.array(x_vals) # remember, need to convert to np.array format to give to TF
x_sample2 = np.array([[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]])

#------------- TF Vars --------------
#------ aka Building the Graph ------
x = tf.placeholder(tf.float32, shape=(None, layer_size)) # note, in the previous section we had explicitly defined the shape as
#                                                          (batch_size, input_size), the batch size is not imperative, and
#                                                          you can use None as a wildcard shape
weight = tf.get_variable("weight", [layer_size, num_classes])
bias = tf.get_variable("bias", [num_classes])
#x_usable = tf.transpose(x)                  # OPERATION, here we must transpose the x into a format compatible with matmul
output = tf.matmul(x, weight) + bias # OPERATION, can also do = tf.matmul(weight, tf.transpose(x)
show_weight = tf.abs(weight)
# need  [2, 3] x [3, 2] --> maybe explain better when have energy --> tie into why x_vals is defined as [1, 10] and weight [10, 1]
# Great, we are all defined up! Time to execute the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # need to run the tf.Variable initializer so we can use them

    #     Graph_output = sess.run(thing_to_do, data_to_do_it_on)
    # op1_out, op2_out = sess.run([op1, op2], data_to_do_it_on)
    result, var = sess.run([output, show_weight], feed_dict={
                                                        x: x_sample
                                                    })
    print("\nRound 1:", x_sample)
    print("Graph tf.matmul() Output:")
    print(result)
    print("\nVars:")
    print(var)
    # !!!!!! YOUR OUTPUTS WILL DIFFER DUE TO RANDOM WEIGHTS AND BIASES !!!!!!
    """
    Round 1: [[0 1 2 3 4 5 6 7 8 9]]
    Graph tf.matmul() Output:
    [[0.34611583]]

    Vars:
    [[0.24457121]
    [0.01377606]
    [0.698994  ]
    [0.59462893]
    [0.6017857 ]
    [0.6938638 ]
    [0.4925645 ]
    [0.5015618 ]
    [0.6225916 ]
    [0.64681107]]
    """

    # ------------------- Second Excecution -------------------
    result2, var2 = sess.run([output, show_weight], feed_dict={
                                                    x: x_sample2
                                                })
    print("\nRound 2:", x_sample2)
    print("Graph tf.matmul() Output:")
    print(result2)
    print("\nVars:")
    print(var2)
    """
    Round 2: [[10 11 12 13 14 15 16 17 18 19]]
    Graph tf.matmul() Output:
    [[5.0462418]]

    Vars:
    [[0.24457121]
    [0.01377606]
    [0.698994  ]
    [0.59462893]
    [0.6017857 ]
    [0.6938638 ]
    [0.4925645 ]
    [0.5015618 ]
    [0.6225916 ]
    [0.64681107]]
    """

    # Notice how the weights stay exactly the same!! but the 'output' changes as a result of the differing input


"""
Awesome! We now have TensorFlow doing math for us!

To recap, what we have done here is:
    0) Comfortably define a tf.placeholder for feeding data to tensorflow
    1) Define state persistant tf.Variables, Weight and Bias
    2) Define simple tf.matmul operation using tf.Variables and differing input
    3) Feed data to a tf.Session and ask it to peform two Operations sess.run([op1, op2])

Sweet!

"""

