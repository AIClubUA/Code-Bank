


# ------------------------------------------ 3) Accuracy and Predictions -------------------------------------------------------

"""
We are so so close to having a model run from start to finish, theres just two more things we need to squeeze in:
    1) Measuring Accuracy
    2) Actually making predictions on unseen data!
"""

# ------------------------------------------------ Accuracy ----------------------------------------------------------
"""
First, lets take a look at accuracy:
This differs from the Loss, as it is the percent difference from the target and the predicted values

the easiest way to incorporate this is to use:
    tf.metrics.accuracy()

which is implemented like so:
    acc, acc_op = tf.metrics.accuracy(labels=tf.argmax(labels, 1), predictions=tf.argmax(logits))
    # Where labels are the actual values and logits are the predicted values

there are other ways, like the one below:
    #                                          axis=1                      axis=1
    correct_prediction = tf.equal(tf.argmax(labels, 1), tf.argmax(final_output, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediciton, tf.float32)))*100 
    I use this one for a sigmoid based algorithm of output structure:
        [
            [q, w, e, r, t, y], # output 1
            [q, w, e, r, t, y], # output 2
            [q, w, e, r, t, y]  # output 3
        ]

In my experience, the accuracy is cool to see and like send snapchats of, but not a super useful metric
"""


"""
What is useful though is:
    1) Being able to feed testing data to the trained model
    2) Being able to see the predictions its making on the testing data and formatting it
"""


# ------------------------------------------ Feeding Testing Data ----------------------------------
"""
Generally there will be two formats of testing data:
    1) Data you have split from the training set that you have actual labels for
        This data is called validation data and used to check how ACTUALLY accurate your model is
        (Testing accuracy on training data cant always be reliable as your network may be memorizing the data, called Overfitting)

    2) Data that you have no labels for, and are trying to make predictions and format for a sumbission to Kaggle or something


1)
For the first case, we can use the same feed_dict:{_inputs:data_x, _labels:data_y} format as we use for training
Here you can feed the model a batch_size of whatever you please. To start off, feed it batches of 1 testing input and label
so that the outputs you get will be easy to manage and dump into a pythonic structure for you to send to an output file

# Like so
#                       op1         op2
acc, pred = sess.run([accuracy, final_output_sig], feed_dict={embed:x_test, _labels:y_test})



2) 
For the second case, because we dont have labels, we drop the accuracy operation and the _labels parameter of the feed_dict

# Like so
#                  op_to_run
pred = sess.run([final_output_sig], feed_dict={embed:x_test})

Here you will just get the raw predictions from the model, nothing more, nothing less!
"""


# ------------------------------------ Formatting Predicitons --------------------------------------

"""
Manicuring your output is the culminating event of developing a predictive model!

Because there are so many different model types and data input formats, you will need to tailor these techniques
to fit your need but the fundamental tools to help with that process are:
    1) Defining WHAT you want your model to predict, the format of the label
    2) How to extract predictions from your model that reflect that format

(Note this applies to Neural Nets, not regressors)
"""
# ----------------------------------------------------- Softmax ------------------------------------------------------
"""
Say you want your network to predict whether a stock will go up or down.
Here there are two classifications that you would label your training data with, and expect testing to output:
    1)   Up:    [1, 0]
    2) Down:    [0, 1]

This type of prediction requires the classification to be singular and exclusive, aka it cant go up and down, it needs to be one or the other
For this case, a Softmax activation function should be used
    tf.nn.softmax()

Softmax ensures that the sum of the output vector is equal to 1
"""

def SoftmaxExample():
    #                 some operation function that produces logits
    final_output = tf.add(tf.matmul(_inputs, weights), biases)
    #                                logits
    final_output_soft = tf.nn.softmax(final_output) # tf.nn.softmax() is the workhorse here

    with tf.Session() as sess:
        preds = sess.run(final_output_soft, feed_dict={_inputs:test_x})
        for values in preds:
            print(values)
            # [.20, .80]
            # [.75, .25]
            # ect....

# ----------------------------------------------------- Sigmoid ------------------------------------------------------
"""
Say we have something that can be a part of multiple classifications, like text comments, which has 4 classifications:
    1) Insulting comment
    2) Threataning comment
    3) Vulgar comment
    4) Uplifting comment

our labels in this case would look like this:
[insult, threat, vulgar, uplifting]

here we can have any combination of these indexes be activated:

[1, 1, 1, 0]
[1, 0, 1, 0]
[0, 0, 0, 1]
[1, 1, 0, 0]
[1, 0, 0, 0]
etc....

For this case, where the sum of the output vector is not equal to 1, we want to use a Sigmoid activation function:
    tf.Sigmoid(logits)
"""

def SigmoidExample():
    #                 some operation function that produces logits
    final_output = tf.add(tf.matmul(_inputs, weights), biases)
    #                                logits
    final_output_sig = tf.sigmoid(final_output) # tf.Sigmoid() is the workhorse here

    with tf.Session() as sess:
        preds = sess.run(final_output_sig, feed_dict={_inputs:test_x})
        for values in preds:
            print(values)
            # [.984, .674, .892, .06]
            # [.017, .29, .15, .897]
            # ect....


"""
I know this tf-basics series has been wall of text after wall of text, but at this point, we have finally covered
every single topic and tool one needs to begin building models from scratch!

To recap our arduous journey, we have:
    1) Entered the TensorFlow headspace, where we learned what Graphs and Sessions are
    2) Learned how to make tf.Placeholders that are used to feed data to models via feed_dict
    3) Learned what tf.Variables are and how Weights and Biases are used to make predictions
    4) Learned what Loss and Optimization are and how to implement them in training a model
    5) Learned how to show accuracy, and format outputs to our models can actually become useful!

You should be very proud of yourself! 

Now the next step is putting these sweet skills to use. I find the best way to do this is finding fully operational
examples, like on TensorFlows website and various other places, and then modifying that architecture to fit the dataset at hand.
When deciding what kind of architecture you want to use, your data type and desired function are the main factors to consider.
There are some resources in /Introduction-to-Applied-AI that can help in the decision making phase. However, I personally
like applying as many different architectures to my data as possible just to see what happens. Regardless of the predictive
power of a model and if the data and data structure works well with the network style, I still get that much more experience
implementing that style of architecture. And next time I have a dataset that would be perfect for that network, I will
already have a few hours of experience under my belt!


https://www.kaggle.com/datasets
I strongly suggest parousing the above link until you find something you think looks neat. The name of the game is exposing
youself to as many different problem scenarios as possible, this forces you to learn new things to overcome those challanges.
Picking a set you find interesting is really really important because one of the largest barriers in learning this stuff is
the time committment it takes to refine your skills. Making time to work on this is no easy task, but having a really cool
dataset in your posession makes things much easier than working on something you think is dumb. 

Also, most of the cool datasets dont have very obvious predictive values in them, so it forces you to be creative about
coming up with things to predict. Dont shy away from these sets! Developing the confidence and the skillset to have
complete command and control of any dataset that you come in contact with will pay huge dividends in the future as
you venture away from the clean and easy problems into more cutting edge problem solving.

There are tons of resources about reading in and processing data in /Preprocessing-Resources, and I cannot stress enough
that supreme confidence handling data is the key to creating proper input and label structures that will harness the 
true power of these algorithms!

"""




