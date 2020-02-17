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
# This creates the list of all numbers agg_list.
agg_list = []

# First, numbers from the texts list are added to agg_list.
for i in texts:
    x = i[0]
    y = i[1]
    agg_list.append(x)
    agg_list.append(y)

# Second, numbers from the calls list are added to agg_list.
for i in calls:
    x = i[0]
    y = i[1]
    agg_list.append(x)
    agg_list.append(y)

# Third, the unique numbers from agg_list are placed into a
# new list, unique_list.
unique_list = []
for i in agg_list:
    if i not in unique_list:
        unique_list.append(i)

# Finally this prints the count of unique phone numbers.
print("There are {} different telephone numbers in the records.".format(
        len(unique_list)))