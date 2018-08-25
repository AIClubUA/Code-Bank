

"""
The most common data format you will see is data in .csv files with defined headers and rows
.csv stands for "comma separated values" which pretty much means the rows are delimited by commas

data is frequently delivered in this format, and is also an easy format to deliver to other people,
so knowing how to read in and write out is important
"""

# ----------------------------------------------------- Reading in ------------------------------------------------------------------------

#There are two main ways to read in .csv's which are outlined below

# 1) Using Pandas to readin into DataFrame

import pandas as pd 

infile = "sample.csv"

df = pd.read_csv(infile) # returns a dataframe, which can be treated like a suped up dictionary
print("Data Frame Representation:")
print(df) # very very easy!


# 2) Read in row by row

row_wise_list = []
column_wise_dict = {}

headers = []
deep = 0
for line in open(infile, encoding="utf8"):
    row = line.strip('\n').split(',') # first stripping \n character at end of each line, then breaking on the COMMA SEPARATEd VALUES
    row_wise_list.append(row) # builds a list of lists

    # takes first row to populate headers
    if deep == 0:
        headers = row
        for header in headers:
            column_wise_dict[header] = [] # init empty list
        
        deep = 1
    else:
        for index in range(len(row)):
            column_wise_dict[headers[index]].append(row[index])

print("\nList Representation:")
print(row_wise_list)

print("\nDictionary Representation:")
print(column_wise_dict)


# ----------------------------------------------------- Writing Out ------------------------------------------------------------------------

# For writing out, the two main ways mirror the input

# 1) Using Pandas - this is useful if we have data in a dictionary format
#import pandas as pd
pd_out_name = "pandas-outfile.csv"

out_data = {
    "vehicle": ["boat", "car", "bike"],
    "weight": [4500, 1500, 20],
    "travel on land": [False, True, True]
}

out_df = pd.DataFrame(out_data)
headers = ["vehicle", "weight", "travel on land"]
# Note, we need to specify headers if we want the output file to maintain a certain order of columns
out_df[headers].to_csv(pd_out_name, index=False)


# 2) Writing Rows - this is useful if we have a list of lists, each acting as a row

import csv

list_of_lists = []

# To ensure anybody else seeing the data can know whats going on, we specify a header column
headers = ["state", "population", "national bird"]
list_of_lists.append(headers)

# now add some data
list_of_lists.append(["virginia", 4000, "cardinal"])
list_of_lists.append(["wyoming", 25, "bald eagle"])
list_of_lists.append(["new york", 400000000, "pigeon"])

row_out = "row-outfile.csv"
with open(row_out, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in list_of_lists:
        writer.writerow(line)


