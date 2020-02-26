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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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

# First, this creates the unique_codes list, which contains all the
# unique codes from the callers dialing from an area code in Bangalore.
# unique_codes = ['(080)']

# Second, this prints a message for my Udacity Instructor.
# print("While a fixed area code is '(080)' it is unclear what the mobile ",
# "and telemarketer area codes are.")

# First, this for loop creates a codes list and a unique codes_set,
# appending codes based upon a conditional statement that identifies
# fixed, telemarketer, and mobile numbers.
agg_code_list = []
unique_codes = set()
for i in calls:
  if i[0].startswith("(") == True:
    x = i[1]
    agg_code_list.append(x[1:4])
    unique_codes.add(x[1:4])
  elif i[0].startswith('1') == True:
    x = i[1]
    agg_code_list.append(x[0:4])
    unique_codes.add(x[0:4])
  else:
    x = i[1]
    agg_code_list.append(x[0:5])
    unique_codes.add((x[0:5])

