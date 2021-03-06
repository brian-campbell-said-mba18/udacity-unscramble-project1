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

# First, this for loop creates a codes list and a unique codes_set,
# appending codes based upon a conditional statement that identifies
# fixed, telemarketer, and mobile numbers.
# The below code comes from Reference 1 in References (see bottom
# of this script).
agg_code_list = []
unique_codes = set()
for i in calls:
  if i[0].startswith("(080)"):
    if i[1].startswith('('):
      x = i[1]
      agg_code_list.append(x[1:4])
      unique_codes.add(x[1:4])
    elif i[1].startswith('1'):
      x = i[1]
      agg_code_list.append(x[0:4])
      unique_codes.add(x[0:4])
    else:
      x = i[1]
      agg_code_list.append(x[0:4])
      unique_codes.add(x[0:4])

# This sorts the list in ascending order.
# This code comes from Reference 2 in References.
unique_codes = sorted(unique_codes)

# This prints Part A.
print("The numbers called by people in Bangalore have codes:")
for i in unique_codes:
  print(i)

# This counts the number of calls to Bangalore numbers.
counter = 0
for i in agg_code_list:
  if i == "080":
    counter += 1

# This is the denominator, the total number of calls.
denominator = len(agg_code_list)

# This calculates bangalore calls/all calls and multiplies it
# by 100 for a percentage calculation.
b_answer = (counter/denominator) * 100

# This prints out the answer to problem B.
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(b_answer))

# References
# 1. https://knowledge.udacity.com/questions/70577
# 2. https://www.tutorialgateway.org/python-set-sorted-method/