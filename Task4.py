"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# this dict save texts numbers and incoming calls
h = {}

for text in texts:
    if text[0] in h:
        h[text[0]] += 1
    else:
        h[text[0]] = 1
        
    if text[1] in h:
        h[text[1]] += 1
    else:
        h[text[1]] = 1
        
for call in calls:
    if call[1] in h:
        h[call[1]] += 1
    else:
        h[call[1]] = 1
        
marketers = {}
# then try to find the telemarketers
for call in calls:
    if call[0] in h:
        continue
    marketers[call[0]] = 1
    

arr = list(marketers.keys())
arr.sort()
print("These numbers could be telemarketers: ")
print(arr)
