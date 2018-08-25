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