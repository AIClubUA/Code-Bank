
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