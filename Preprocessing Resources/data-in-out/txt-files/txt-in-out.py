
"""
.txt files are useful for storing some kinds information, and you every now and then you will be delivered data in .txt format

while not as common as .csv it is useful to have a quick tool to read them in
"""

# --------------------------- Reading In ----------------------------------

textfile = "sample-txt-infile.txt"

f = open(textfile, 'r')
data = f.read()
f.close()
readin = data.split("\n")
for line in readin:
    print(line)



# --------------------------- Writing Out ----------------------------------

# Note this works for lists of lists, not so well for dictionaries
# However, if you felt inclined, you could always convert the dictionary to a list of lists ;)
txt_outfile = "txt-write-row.txt"

out_list = [
    ["09:00:00 - 'Wake Up'"],
    ["09:30:00 - Actually get up (maybe)"],
    ["09:30:05 - Crack open first Monster of the day"],
    ["09:30:59 - Begin internal debate between playing video games and coding"],
    ["09:45:00 - Wave of motivation surges over me, dive into code"],
    ["09:52:00 - Naptime"],
    ["15:00:00 - Oof missed lunch again, guess I'll cruise Instagram until dinner"],
    ["18:24:00 - How did I fall asleep again?!?!"],
    ["18:25:00 - *Sits down at desk*"],
    ["18:27:00 - *Tries not to game*"],
    ["18:29:00 - *Games a lot*"]
]


f = open(txt_outfile, 'w')
for item in out_list:
    f.write("%s\n" % item) 
    #f.write(%s\n % item[0]) # to get rid of surrounding '[ ... ]'  brackets


