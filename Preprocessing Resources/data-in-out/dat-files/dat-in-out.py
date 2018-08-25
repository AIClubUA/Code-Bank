

"""
Very frequently, its useful to save a list, dictionary or Class to use later on, after your script has terminated.

Something I do regularly is preprocess and clean some raw data from a .csv, then save it in its processed form
as a dictionary or list of lists, for use later. That way, every time I want to operate on it, I can just read 
it right into pythonic form, and not deal with re-processing anything
"""

import pickle


data_to_save = {
    "any": "structure",
    "of": "anything is totally cool to save",
    "numbers": 45,
    "lists": [1, 2, 3, 45, 56],
    "dictionaries": {
        "yep": "even these"
    }
}

print("\nWritten Structure:")
print(data_to_save) # as you can see, this is the form of data

# ------------- Writing Out ----------------
# now we are going to save it:
filename = "dat-saved-file.dat"
pickle.dump(data_to_save, open(filename, 'wb'), -1)


# -------------- Reading In ----------------
# next, we are going to read it in to new variable
data_read_in = pickle.load(open(filename, 'rb'))

print("\nRead In Structure:")
print(data_read_in) # the exact same!

