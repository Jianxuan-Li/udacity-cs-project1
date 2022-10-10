"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import os
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
numbers = set()

for text in texts:
    numbers.add(text[0])
    numbers.add(text[1])

for call in calls:
    numbers.add(call[1])

marketers = {}
# then try to find the telemarketers
for call in calls:
    if call[0] in numbers:
        continue
    marketers[call[0]] = 1


nums_arr = list(marketers.keys())
nums_arr.sort()

print("These numbers could be telemarketers: ")
print(*nums_arr, sep=os.linesep)
