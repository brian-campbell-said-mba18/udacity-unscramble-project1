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
# First, this converts the time data from strings to integers.
for i in range(len(calls)):
    calls[i][3] = int(calls[i][3])

# Second, we create the call dictionary and append the numbers
# that originated the calls and time spent on calls from the calls list.
call_dict = {}
for i in calls:
    if i[0] not in call_dict:
        call_dict[i[0]] = i[3]
    else:
        call_dict[i[0]] += i[3]

# Third, we add the times to the numbers that received the calls.
for i in calls:
    if i[1] not in call_dict:
        call_dict[i[1]] = i[3]
    else:
        call_dict[i[1]] += i[3]

# This tests whether the call_dict was successfully created.
for keys, values in call_dict.items():
    print("Phone Numbers: {}, Times(seconds) : {}.".format(keys, values))
