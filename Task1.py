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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

h = {}

for text in texts:
    if text[0] not in h:
        h[text[0]] = True
    
    if text[1] not in h:
        h[text[1]] = True
        
for call in calls:
    if call[0] not in h:
        h[call[0]] = True
        
    if call[1] not in h:
        h[text[1]] = True
    
print("There are {} different telephone numbers in the records.".format(len(h)))