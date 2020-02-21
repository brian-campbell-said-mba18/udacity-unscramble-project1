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
# First, I create a list of unique phone numbers from where the
# call originated, og_list. 
og_list= []
for i in calls:
    if i[0] not in og_list:
        og_list.append(i[0])

# Second, I create a list of unique phone numbers of the 
# receiving callers, receive_list.
receive_list = []
for i in calls:
    if i[1] not in receive_list:
        receive_list.append(i[1])

# This for loop creates two lists. If a number only calls,
# but never receives calls, it is put into the suspects_list,
# as a potential scammer. However, if a number both calls and
# receeives calls, it passes the test and is put into the
# passed_inbound_calls list.
suspects_list = []
passed_inbound_calls = []
for i in og_list:
    if i not in receive_list:
        suspects_list.append(i)
    else:
        passed_inbound_calls.append(i)



