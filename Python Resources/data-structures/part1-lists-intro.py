"""
Before any of the great ML and AI tools can be used, you must first have
complete command and control of the data you are expecting to derive information from.

As the adage goes "Garbage in, garbage out", so the first step in learning
how to truly utilize all the advances in computing and AI, is learning how 
to take the trash out
"""

"""
I am assuming basic understanding of how to define variables, and the three
primary data types:
ints/floats -->
    int_var = 5
    flt_var = 5.5

strings -->
    str_var = "variable"

booleans -->
    bol_var = True
"""

"""
These data types are the morsels of information that make up a dataset, but
unless they are organized in the correct manner, they are next to useless.

To wrangle these bits and pieces, python has two main structures, and what
this document is dedicated to elaborating on.

The two structures are:
    Lists
    Dictionaries
"""

#Syntax:
#Lists are defined by using [] like so:
empty_list = [] # which initializes an empty list
print(empty_list)
# which returns:
# []

# lists can also be initialized with some starting variables
populated_list = [5, 5.5, "variable", True]
print(populated_list)
# [5, 5.5, 'variable', True]

somevar = 45
another = "variable"
var_list = [somevar, another]
print(var_list)
# [45, 'variable']

# Furthermore, lists can even be populated with other lists!
# here we define a new list using all three of the techniques listed above!
nest_list = [["new", "list", 4], empty_list, populated_list, var_list, [], [["nestested", "list!"], [1, "more", "level", True]]]
print(nest_list)
# [['new', 'list', 4], [], [5, 5.5, 'variable', True], [45, 'variable'], [], [['nestested', 'list!'], [1, 'more', 'level', True]]]

# Now as we can see, this length-wise visualization is not great, so to get a better view of things we use a for loop
for sub_list in nest_list:
    print(sub_list)

"""
which returns:
['new', 'list', 4]
[]
[5, 5.5, 'variable', True]
[45, 'variable']
[]
[['nestested', 'list!'], [1, 'more', 'level', True]]
"""