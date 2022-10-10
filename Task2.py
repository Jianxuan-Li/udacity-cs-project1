"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_dict = {}

for call in calls:
    phone_dict[call[0]] = phone_dict.get(call[0], 0) + int(call[3])
    phone_dict[call[1]] = phone_dict.get(call[1], 0) + int(call[3])

max_phone_num = max(phone_dict, key=lambda k: phone_dict[k])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    max_phone_num, phone_dict[max_phone_num]))
