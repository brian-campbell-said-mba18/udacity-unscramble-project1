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
# This creates a unique set of all the numbers.
unique_nums_set = set()

# First, numbers from the texts list are added to agg_list.
for i in texts:
    unique_nums_set.add(i[0])
    unique_nums_set.add(i[1])

# Second, numbers from the calls list are added to agg_list.
for i in calls:
    unique_nums_set.add(i[0])
    unique_nums_set.add(i[1])

# Finally this prints the count of unique phone numbers.
print("There are {} different telephone numbers in the records.".format(
        len(unique_nums_set)))