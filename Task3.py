"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_from_Bangalore(number):
    # fixed line of Bangalore
    if re.search("\(080\)\d+", number):
        return True
    return False

def get_code(number):
    # get the area code or prefix of called numbers
    
    # Telemarketers
    if re.search("140\d+", number):
        return "140"
    
    # area code of fixed line
    test = re.findall("(\(0\d+\))\d+", number)
    if len(test) > 0:
        return test[0]
    
    # prefix of mobile
    test = re.findall("([7|8|9]\d{3})\d+\s\d+", number)
    if len(test) > 0:
        return test[0]

    return False
    
def find_all_codes():
    h = {}
    same_place = 0
    
    for call in calls:
        if not is_from_Bangalore(call[0]):
            continue
        
        c = get_code(call[1])
        if c:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1
                
        if is_from_Bangalore(call[1]):
            same_place += 1
                
    codes = list(h.keys())
    codes.sort()
    print("The numbers called by people in Bangalore have codes:")
    print(codes)
    
    percentage = round((same_place / len(calls)) * 100, 2)
    
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

find_all_codes()
