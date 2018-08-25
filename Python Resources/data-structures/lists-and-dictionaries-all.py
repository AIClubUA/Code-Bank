

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


# ------------------------------------------------------ Section 2 ------------------------------------------------------

"""
While it is nice to be able to hardcode define lists, lists are best utilized when populated dynamically.

As an intro to dynamic population, we begin by defining an empty list and populating it with some values
here we are using the .append() method, which adds items to the rear of the list
"""

empty_list = []
print("List Initially:", empty_list)
for i in range(10):
    empty_list.append(i)
    print("Adding:", i, " | List Contents Now:", empty_list)

print("List Finally:", empty_list)
#   OUTPUT:
#   List Initially: []
#   Adding: 0  | List Contents Now: [0]
#   ...
#   Adding: 4  | List Contents Now: [0, 1, 2, 3, 4]
#   ...
#   Adding: 9  | List Contents Now: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   List Finally: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Simple!

# --> Now, there are a few useful things to know about each List
# 1) How big is the list?
# 2) Where are the items located in the list?

# To answer 1) we use the len(function), which returns the number of items in the list
list_len = len(empty_list)
print("Length of empty_list is:", list_len)
#   OUTPUT:
#   Length of empty_list is: 10

# --> This is useful information for retrieving specific values from a list
# Consider this list:
lit_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# we can access each value with for loops or directly
# If we decide to loop we have two options
# The first one we have already seen, iterates over each value
for item in lit_list:
    print("Raw Item:", item)

#   OUTPUT:
#   Raw Item: zero
#   ...
#   Raw Item: nine

# --> orrr we can iterate over the lists range, (len(lit_list)), and use list[i] notation to grab the values
for index in range(len(lit_list)):
    print("Index:", index, "| Corresponding lit_list[index] value:", lit_list[index])

#   OUTPUT:
#   Index: 0 | Corresponding lit_list[index] value: zero
#   ...
#   Index: 5 | Corresponding lit_list[index] value: five
#   ...
#   Index: 9 | Corresponding lit_list[index] value: nine

# Great! We now have two tools to grab all the values from a list!

# --------------------------------------------------------------------------------------------------------------------

# --> Suppose we have a different list, where
#                  [name, phone, email]
info_list = ["joe bob", 2058761234, "joe.bob@python.org"]
# We can access each piece of info like so: want = list_name[index]
name = info_list[0]
phone = info_list[1]
email = info_list[2]

print("Name:", name)
print("Phone:", phone)
print("Email:", email)

#   OUTPUT:
#   Name: joe bob
#   Phone: 2058761234
#   Email: joe.bob@python.org


# --> And if we want to be even fancier, can add another info list to a holding list
# Here we are going to string together several techniques listed above!
all_entries = [] # Initialize an empty list
all_entries.append(info_list) # adding a new entry, using the premade info_list from above

new_names = ["big al", "nick saban"]
new_phones = [2051234567, 2050162018]
new_emails = ["best.mascot@ua.edu", "god.among.men@national.champs.org"]

# --> here, we have three parallel lists all of the same size
# because there are three of them, we cannot use the
#   for item in list:
#       do_something()
# notation because it would not apply to every list
# so we need to use indexing!
for index in range(len(new_names)): # note we can use len(new_names), len(new_phones) or len(new_emails) because they all have the same length
    buffer = [] # creating an empty list that will be populated, note, makes new empty list each time it iterates !!
    buffer.append(new_names[index])
    buffer.append(new_phones[index])
    buffer.append(new_emails[index])
    print("At index:", index, "| New list to be populated:", buffer)
    all_entries.append(buffer)

print("Final all_entries:")
for i in all_entries:
    print(i)

#   OUTPUT:
#   At index: 0 | New list to be populated: ['big al', 2051234567, 'best.mascot@ua.edu']
#   At index: 1 | New list to be populated: ['nick saban', 2050162018, 'god.among.men@national.champs.org']
#   Final all_entries:
#   ['joe bob', 2058761234, 'joe.bob@python.org']
#   ['big al', 2051234567, 'best.mascot@ua.edu']
#   ['nick saban', 2050162018, 'god.among.men@national.champs.org']


# --> now say we wanted to see all the names in our all_entries:
# there are two ways we can do this
# 1)
for entry in all_entries:
    #                      0     1      2
    # Remember, entry = [name, phone, email]
    name = entry[0]
    print("Name:", name) # grabs the names

#   OUTPUT:
#   Name: joe bob
#   Name: big al
#   Name: nick saban


# or 2)
for index in range(len(all_entries)):
    # to look at each entry
    each_entry = all_entries[index]
    name = each_entry[0] # hmmm, this looks very similar to the for loop above!
    print("Name:", name)

    # now, we can combine some of the lines above
    combined_name = all_entries[index][0]
    print("Combined:", combined_name) # and we get the same answer

#   OUTPUT:
#   Name: joe bob
#   Combined: joe bob
#   Name: big al
#   Combined: big al
#   Name: nick saban
#   Combined: nick saban


"""
You might be thinking, this takes a good bit of work structuring and indexing all these lists
and isnt it confusing using two index values and iterating?!

And you would be correct, it gets out of hand quickly!
That is why the python creators blessed us with Dictionaries
"""



















#--------------------------------------- D*I*C*T*I*O*N*A*R*I*E*S -------------------------------------------------
"""
Dictionaries seek to simplify data organization and allow better handles for grabbing the data you want

They structure around:
    key: value pairs

Where by specifying a key, you are returned a value that is associated with it.

Similar to driving to McDonalds and barking "big mac" into the speaker (key)
and receiving a cheeseburger (value) a few minutes later

to define dictionaries, we use the {} characters like so:
"""

empty_dict = {}

# To initialize with variables, we use the following { key: value } notation
# keys MUST BE UNIQUE and can either be strings or numbers
# Note, using numbers slightly defeats the purpose of using a dictionary, and makes it less human readable

populated_dict = {
    "key": "value",
    "zero": 0,
    "list": ["a", "list", "keyed", "from", "a", "dictionary"],
    "awesome": True,
    "nest": {
        "nested": True,
        "useful": "very",
        "levels": 2,
        "capture": "the flag"
    }
}

# As you can see, every data type and structure can be keyed in a dictionary

# And this is all fine an dandy, but how to we retrieve this information?!

# For starters, it can be useful to know all the possible key values
all_keys = populated_dict.keys()
print(all_keys)
#   OUTPUT:
#   dict_keys(['key', 'zero', 'list', 'awesome', 'nest'])

# We can then use the keys with the following syntax
# retrieved_value = populated_dict["key"]

for key in populated_dict.keys():
    print("Key:", key, "| Value:", populated_dict[key])

#   OUTPUT:
#   Key: key | Value: value
#   Key: zero | Value: 0
#   Key: list | Value: ['a', 'list', 'keyed', 'from', 'a', 'dictionary']
#   Key: awesome | Value: True
#   Key: nest | Value: {'nested': True, 'useful': 'very', 'levels': 2, 'capture':'the flag'}


# Another way to get the same result is:
for key, value in populated_dict.items():
    print("Key:", key, "| Value:", value)

# However, if we just wanted a specific item, we could do

want = populated_dict["list"]
print(want)
# now we can treat want like any other list!
print("Contents of list at index 2:", want[2])
#   OUTPUT:
#   ['a', 'list', 'keyed', 'from', 'a', 'dictionary']
#   Contents of list at index 2: keyed

# Also, Im sure it was noticed that there was another dictionary within populated_dict, keyed by "nest"
# Here, if we wanted to access "the flag"
# We could do so like this
the_flag = populated_dict["nest"]["capture"]
print("Found the flag:", the_flag)
#   OUTPUT:
#   Found the flag: the flag



# ----------------------------------------------- Part 2 --------------------------------------------------------
# Now, returning to the final example of lists, try organizing the data with some dictionaries!
# Here, we are going to structure the data in two formats:
"""
# 1) each post will be keyed by its number, and will contain the name, phone and email fields
contents = {
    "item1": {
        "name": '',
        "phone": 0,
        "email": ''
    },
    "item2": {
        "name": '',
        "phone": 0,
        "email": ''
    },
    "item3": {
        "name": '',
        "phone": 0,
        "email": ''
    }
}

# and 2)
contents = {
    "names": [],
    "phones": [],
    "emails": []
}
"""
# Note, there are pros and cons to each, and I personally prefer using the structure of 2) as it translates
# easily into DataFrames, a very easy structure to move around and feed to models, as well as export data

# ------------------------------------------- Structure 1 -----------------------------------------------
# using data struct from above
info_list = ["joe bob", 2058761234, "joe.bob@python.org"]
new_names = ["big al", "nick saban"]
new_phones = [2051234567, 2050162018]
new_emails = ["best.mascot@ua.edu", "god.among.men@national.champs.org"]

# Creating new dictionary, initializing
contents = {
    # note, "item1" does not exist, for now!

    "item2": {
        "name": '',
        "phone": 0,
        "email": ''
    }
}
struct = {
    "name": info_list[0],
    "phone": info_list[1],
    "email": info_list[2]
}
contents["item1"] = struct # this is how we add new keys!

# We can modify existing keys like so
contents["item2"]["name"] = info_list[0] # '' --> 'joe bob'
contents["item2"]["phone"] = info_list[1]
contents["item2"]["email"] = info_list[2]

# For the other lists of new_xxxxx we can populate iteratively
for index in range(len(new_names)):
    new_struct = {
        "name": new_names[index],
        "phone": new_phones[index],
        "email": new_emails[index]
    }  
    # Now we run into an interesting dillemma...
    # To create new UNIQUE keys we have three options
    # 1) The easiest:
    #contents[i] = new_struct # here 0, 1, ... N would be the key, but, this does not match the naming scheme!
    # 2) Hack the hell out of it
    contents["item" + str(len(contents.keys()) + 1)] = new_struct # here we are smashing together a number and a string
    #                                                                   and the number is dynamically created from the number
    #                                                                   of existing keys and adding 1
    # 3) Best option
    #key_names = ["item3", "item4"] # note we would want to define this outside of the for loop
    #contents[key_names[index]] = new_struct #  here we are using the index to grab pre defined key names!
    
    # all three of the above methods are viable!!

# This first structure has some good applications, but not great for formatting into a dataframe that a model can use!
# For that we turn to structure 2) which is outlined below




#------------------------------------------- Structure 2) -----------------------------------------


info_list = ["joe bob", 2058761234, "joe.bob@python.org"]

new_names = ["big al", "nick saban"]
new_phones = [2051234567, 2050162018]
new_emails = ["best.mascot@ua.edu", "god.among.men@national.champs.org"]

# here, looking at the input data structures, we can see
# 1) some info is already grouped by its data type, name, phone, email
# 2) some is not (info_list)

# here, we get to put our skills to the test!
"""
# remember the format we want is
content = {
    "names": [],
    "phones": [],
    "emails": []
}
"""
# For the sake of brevity (at line ~400, lmao)
# we are going to say the order of the data in the name, phones, emails "columns" does not matter
# so we can go ahead and create the raw data format like so!

content = {
    "names": new_names,
    "phones": new_phones,
    "emails": new_emails
}

# yet we still need to add the data in "info_list"
# so we do
content["names"].append(info_list[0])
content["phones"].append(info_list[1])
content["emails"].append(info_list[2])

# using the dict["key"].append(data) method directly above is very very useful and my primary means of populating
# dictionaries if I dont have preformatted lists handy


"""
I know this is a wall of text, but like I noted in the introduction of this series,
having COMPLETE COMMAND and CONTROL of your data is imerative for scaling comfortably
to implementing more complex algorithms.

One of the most heartbreaking things that can happen is building a model around a 
supposed data structure, that you had in your head, only to find out way down the line
that all the predictive infrastrucure you implemented is not looking at the piece of data
you wanted it to be looking at, because youre feeding structure is wrong.

So please take the time to practice transferring data from lists to dictionaries and vice versa,
and I promise you after a while it becomes second nature!
"""





