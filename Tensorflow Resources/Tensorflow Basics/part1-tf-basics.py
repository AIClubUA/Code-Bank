


# ------------------------------------------------ Tensorflow headspace ------------------------------------------------------------
"""
The first step towards building and using models in TensorFlow is getting in the TensorFlow headspace

To kick things off, there are two key terms you need to become famillair with:
    1) Graph
    2) Session

--> Graph
Pretty much the Graph is the architecture of the operations contained within a model
    ex: Raw Data -> Layer 1 -> Layer 2 -> Output

    Within graphs, there are two Object:
        1) Operations (ops): operations take data in one form, do something to it, and spit out the new version of the data
        2) Tensors: these are the data units that flow from operation to operation, more to come on these below

--> Session
To actually use the graph and send data through it, you need to initialize a session.
The best I saw to think of this is:
    tf.Graph is like a .py file, containing instructions for what and how to do something
    tf.Session is like when you call $ python your-script.py, where tf.Session is 'python'

    .py files are useless without python to run them, and python is useless without .py files to tell it what to do
    Graph architectures are useless without a Session to run them, and Sessions are useless without a Graph architecture to tell it what to do
"""


# ----------------------------------------- Toolkit -----------------------------------------------------------------
"""
Great! The idea of graphs and sessions makes sense now right?
But what do we do with this information? And more importantly, how do we start making models?

The meat of every TF model revolves around the following components
    1) Structuring the data to feed to the model
    2) The weights and biases
    3) Model Loss and optimization
    4) Accuracy measuring
    5) Applying model to unlabeled data
"""

# 1) Structuring Data ---------------------------
"""
TF revolves around list like structures of data called Tensors.

In traditional pythonic form, we may conjure up a list, with NO PRIOR DECLARATION, like so:
"""
some_list = [
    [
        ['000', '001', '002'],
        ['010', '011', '012'],
        ['020', '021', '022'],
    ],
    [
        ['100', '101', '102'],
        ['110', '111', '112'],
        ['120', '121', '122']
    ],
    [
        ['200', '201', '202'],
        ['210', '211', '212'],
        ['220', '221', '222']
    ]
]

# Now to access the various values in this list, we use the indexing scheme:
#   val = some_list[x][y][z]

val1 = some_list[1][1][1]
print("Indexing [1][1][1]:", val1)
#   Output -->
#       Indexing [1][1][1]: 111

val2 = some_list[0][1][2]
print("Indexing [0][1][2]:", val2)
#   Output -->
#       Indexing [0][1][2]: 012

"""
Now being able to access one individual value in a 3D matrix is a cool party trick, 
but primarily, we care about the entire list of values in the "deepest" level of the matrix
here that would be the:
    some_list[x][y][deepest]

To access the group as a whole, we just drop the last index key!
"""

deep1 = some_list[0][0]
print("Deepest list[0][0]:", deep1)
#   Output -->
#       Deepest list[0][0]: ['000', '001', '002']

deep2 = some_list[2][1]
print("Deepest list[2][1]:", deep2)
#   Output -->
#       Deepest list[2][1]: ['210', '211', '212']

"""
Great! As we can see, navigating matricies is very logical!
Now, suppose we wanted slightly different structure like so
"""
target_list = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24']
] 
"""
Now suppose that we know the shape of this list, but we dont know exactly what data will occupy the list?
How can we define the list without these values?

We get a brilliant idea, and we initialize a list of the exact shape and size with empty values.
for demonstration purposes, lets take a look at the shape of the target_list:
    (remember we access values like so: list[x][y][z])
"""

# First, we will want the 'x' dimension, and we can find that out like so
x = len(target_list)
print("target_list x:", x)
#   Output -->
#       target_list x: 3

# now, how many values are in the secondary dimension, y?
y = len(target_list[0]) # note we are taking the 0th index, but in theory, we could take any index, and the y shape would be the same!
print("target_list y:", y)
#   Output -->
#       target_list y: 5

"""
Awesome! Now we know the target_list is of the shape:
    x = 3
    y = 5
or
    3x5
or
     x  y
    (3, 5)

applying this same logic to some_list, the first list we indexed, we see its shape is:
    x = 3
    y = 3
    z = 3
or
     x  y  z
    (3, 3, 3)


Using this info, we can define empty_frame like so:
Remeber, we want something like this:
empty_frame = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]
"""
empty_x = 3
empty_y = 5

empty_from_scratch = [] # initialize primary holding variable
for x in range(empty_x):
    buffer = [] # create a new buffer to be populated
    for y in range(empty_y):
        buffer.append('') # add empty values to the buffer, y number of times

    empty_from_scratch.append(buffer) # add the new buffer

# Now lets check out our new empty frame!
print(empty_from_scratch)
#   Output -->
#       [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]


"""
Excellent, thats exactly what we want!

But, as I'm sure you were thinking, doesnt writing nested for loops like that have the potential to get very complicated??

And, the answer is YES! Which is why the TensorFlow creators blessed us with a super easy way to do this: with Placeholders

--> Placeholders are defined like so:
"""

import tensorflow as tf

# to accomplish what we did with the 3x5 empty variable above, we use tf.placeholder like this:
empty_Tensor = tf.placeholder(tf.float32, shape=(3, 5))

"""
So easy! But you might notice the 'tf.float32' and wonder what that is

In tensorflow, we need to explicitly define the data type we are using, like in C or C++ where we go:
    int somevar;

with tf.placeholder, the tf.float32 acts the same way as 'int' does.
    * Note there are several dtypes in tensorflow, but the primary you'll use are *
    1) tf.float32 --> for floats x.ddddd
    2) tf.int32 --> for ints x
"""


"""
Now, making empty placeholders is neat, but what purpose do they serve?

To see their utility and place in a script, we need to take a step back and start thinking about the data we 
are working with.

Say we have a fairly large dataset, 28 GB of unrealized insight, but our poor computer only has 16GB of RAM...
How the heck are we going to open up this data and work with it?

Naturally, we are going to split it into small enough bites for our RAM to handle it comfortably.
Say, for this scenario, we dont really want to test the limits of our computer, so we break the
initial 28GB set into 28 sets of 1GB, a much more manageable size!

For tensorflow, we follow the same principal for feeding data to a model. Regardless of how large your dataset is,
it is still useful to break the data into small BATCHES for processing.

Example time again, say we have read in a .csv that has 20 lines of information in it (small example, yes)
Lets go ahead and break that into smaller batches of, lets say 2 lines per batch (small example, yes)
Also, assume the row target values have been extracted and are stored elsewhere
"""
#import numpy as np
#data = np.random.random((20, 5))
data = [
    [0.03207537, 0.31540726, 0.79481086, 0.40791587, 0.416388  ], # tgt = 45
    [0.74699029, 0.20944668, 0.4484725,  0.79104556, 0.80387162], # tgt = 23
    [0.62461063, 0.3369989,  0.72660802, 0.15732972, 0.28162897], # tgt = 67
    [0.00418077, 0.28323858, 0.56115153, 0.24455153, 0.61154959], # tgt = 92
    [0.79250661, 0.05275375, 0.28365675, 0.18198024, 0.6977333 ], # tgt = 85
    [0.5364553,  0.53182525, 0.18781828, 0.45523217, 0.49799234], # tgt = 23
    [0.00250534, 0.50570076, 0.82597434, 0.32343809, 0.53880063], # tgt = 58
    [0.16538936, 0.30327205, 0.13704518, 0.12178389, 0.30945562], # tgt = 4
    [0.28903356, 0.55117588, 0.25458491, 0.92187373, 0.30331806], # tgt = 54
    [0.62817981, 0.85413413, 0.55875375, 0.49670446, 0.63467274], # tgt = 79
    [0.56938432, 0.42186234, 0.0812037,  0.46323076, 0.81502952], # tgt = 27
    [0.31704471, 0.5637259, 0.76515187, 0.42244022, 0.47009012],  # tgt = 96
    [0.55896126, 0.93913138, 0.82487874, 0.15306442, 0.26013009], # tgt = 32
    [0.23221637, 0.69698147, 0.1096115,  0.7896889,  0.37927025], # tgt = 67
    [0.96658374, 0.60069592, 0.7953301,  0.594997,   0.83516095], # tgt = 39
    [0.12118003, 0.08638434, 0.14521805, 0.58645292, 0.17690354], # tgt = 85
    [0.42378231, 0.74598203, 0.57625681, 0.3956005,  0.68914649], # tgt = 12
    [0.2017354,  0.13311782, 0.36072945, 0.85152328, 0.35036155], # tgt = 54
    [0.99495008, 0.83268242, 0.46307392, 0.29501387, 0.58712438], # tgt = 67
    [0.52076277, 0.75241017, 0.47276217, 0.71436473, 0.59246246]  # tgt = 23
]

# Now to break this into batches:
batches = [] # final destination for the batches
batch_size = 2

batch_holder = [] # temporary holding cell
for row in data:
    batch_holder.append(row) # add a new row to the batch_holder
    if len(batch_holder) == 2: # if there are two rows in the batch
        batches.append(batch_holder) # add the new batch
        batch_holder = []   # clear the batch holder so it can accept more data to make more batches

# Lets see what our batches look like!
for batch in batches:
    print(batch)
"""
[[0.03207537, 0.31540726, 0.79481086, 0.40791587, 0.416388], [0.74699029, 0.20944668, 0.4484725, 0.79104556, 0.80387162]]
[[0.62461063, 0.3369989, 0.72660802, 0.15732972, 0.28162897], [0.00418077, 0.28323858, 0.56115153, 0.24455153, 0.61154959]]
[[0.79250661, 0.05275375, 0.28365675, 0.18198024, 0.6977333], [0.5364553, 0.53182525, 0.18781828, 0.45523217, 0.49799234]]
[[0.00250534, 0.50570076, 0.82597434, 0.32343809, 0.53880063], [0.16538936, 0.30327205, 0.13704518, 0.12178389, 0.30945562]]
[[0.28903356, 0.55117588, 0.25458491, 0.92187373, 0.30331806], [0.62817981, 0.85413413, 0.55875375, 0.49670446, 0.63467274]]
[[0.56938432, 0.42186234, 0.0812037, 0.46323076, 0.81502952], [0.31704471, 0.5637259, 0.76515187, 0.42244022, 0.47009012]]
[[0.55896126, 0.93913138, 0.82487874, 0.15306442, 0.26013009], [0.23221637, 0.69698147, 0.1096115, 0.7896889, 0.37927025]]
[[0.96658374, 0.60069592, 0.7953301, 0.594997, 0.83516095], [0.12118003, 0.08638434, 0.14521805, 0.58645292, 0.17690354]]
[[0.42378231, 0.74598203, 0.57625681, 0.3956005, 0.68914649], [0.2017354, 0.13311782, 0.36072945, 0.85152328, 0.35036155]]
[[0.99495008, 0.83268242, 0.46307392, 0.29501387, 0.58712438], [0.52076277, 0.75241017, 0.47276217, 0.71436473, 0.59246246]]
"""
# Awesome, look at this consistant structure!
# Now remember, we broke apart the data into these batches so we could look at the shape of each batch individually
batch_x = len(batches[0])
batch_y = len(batches[0][0])
print("Batch x:", batch_x, "| Batch y:", batch_y)
#   Output -->
#       Batch x: 2 | Batch y: 5

batch_size = batch_x
each_row_size = batch_y

"""
Now that we know the shape of our data and batch size we can finally implement a tf.placeholder!
"""
input_data = tf.placeholder(tf.float32, shape=(batch_size, each_row_size))
"""
It may seem like we did a whole bunch of work just for one line of code, but this is a critical component of working with TF!

As of now, we just have our input data processed, but for the model to make sense of it, the model needs to see
what kind of predictions, values or classification were associated with that row of data!
Note, normally this would just be a column in the .csv and you could easily grab that column

Regardless of how the targets come into your posession, it is imperative that they remain paired to their input data
To ensure that, we do the same batch processing scheme as on the inputs, consider:
"""
targets = [
    [45], # [0.03207537, 0.31540726, 0.79481086, 0.40791587, 0.416388  ]
    [23], # [0.74699029, 0.20944668, 0.4484725,  0.79104556, 0.80387162]
    [67], # 
    [92], # 
    [85], # 
    [23], # 
    [58], # 
    [4],  # 
    [54], # 
    [79], #    you get the idea
    [27], # 
    [27], # 
    [27], # 
    [96], # 
    [32], # 
    [67], # 
    [39], # 
    [85], # 
    [12], # [0.42378231, 0.74598203, 0.57625681, 0.3956005,  0.68914649]
    [54], # [0.2017354,  0.13311782, 0.36072945, 0.85152328, 0.35036155]
    [67], # [0.99495008, 0.83268242, 0.46307392, 0.29501387, 0.58712438]
    [23]  # [0.52076277, 0.75241017, 0.47276217, 0.71436473, 0.59246246]
]

tgt_batches = []
batch_size = 2

tgt_holder = []
for tgt in targets:
    tgt_holder.append(tgt) # add a new row to the batch_holder
    if len(tgt_holder) == 2: # if there are two rows in the batch
        tgt_batches.append(tgt_holder) # add the new batch
        tgt_holder = []

tgt_x = len(tgt_batches[0])
tgt_size = len(tgt_batches[0][0])
print("tgt x:", tgt_x, "| tgt size:", tgt_size)
#   Output -->
#       tgt x: 2 | tgt size: 1

# Now we have the info to define our targets tf.placeholder!
tgt_vals = tf.placeholder(tf.int32, shape=(batch_size, tgt_size))

"""
This tf.placeholder section has gotten way out of control, but the main thing to take away from this is
these are the two placehodlers you need in your scripts!!
With these, we can begin feeding the data to the Graph!

Below is a very simple visualization meant to show how we send data from surface world to the TensorFlow Session realm:
"""


#---------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------- E*X*A*M*P*L*E ---------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#import tensorflow as tf # We already imported this way far above
import numpy as np

# first, we want a simple function to grab the batch inputs and corresponding labels!
def get_batch(batches, tgt_batches, iteration):
    x_to_feed = np.array(batches[iteration]) # note, we need the data to be in np.array format!!!
    y_to_feed = np.array(tgt_batches[iteration])
    return x_to_feed, y_to_feed

# ----- Python Vars --------
num_batches = len(batches) # 10
batch_size = 2 # note these are already defined above, just redefining them to give example of what you want in stand alone script
each_row_size = 5
tgt_size = 1

#------------- TF Vars --------------
#------ aka Building the Graph ------
_inputs = tf.placeholder(tf.float32, shape=(batch_size, each_row_size))
_targets = tf.placeholder(tf.int32, shape=(batch_size, tgt_size))

# this line right here is to show an example operation that could be done by the Graph!
sess_operation = tf.abs(_inputs) # Here we just have the Graph taking abs_val of the inputs (not fancy, but shows the data)
#                                  This is where we would (and will) define the math operations that make up models

with tf.Session() as sess: # the TF equivalent of $ python your-script.py
    for i in range(num_batches): # iterate over each batch of data
        _x, _y = get_batch(batches, tgt_batches, i) # using the function we defined
        # Graph_output = sess.run(thing_to_do, data_to_do_it_on)
        val = sess.run(sess_operation, feed_dict={
                                            _inputs: _x,
                                            _targets: _y
                                        })
        
        print("\nSession Output from the Graph:")
        print("Iteration %d:" % i, val)

"""
Awesome! We have a complete foundation layed!! While this stuff is not glamorous, it is of supreme importance!!

In this short Graph/Session implementation above, we have accomplished several critical things:
    1) Taken raw data of hypothetical .csv format, and assumed complete command and control of it
    2) Formatted that data into batches
    3) Used information from the batch dimensions to create tf.placeholders to accept data for low level processing
    4) Defined a simple operation to be done by the Graph (huuuge, building on this is the next section)
    5) Fed our naked data to the low level processing, with feed_dict!! Hardest part!!
    6) Received data back from the Session, proving we fed data correctly!!

"""

