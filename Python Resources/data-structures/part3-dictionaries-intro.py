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