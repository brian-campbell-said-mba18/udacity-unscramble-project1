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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# This retrieves and prints the first record
# from the texts list.
text_one = texts[0]
print("First record of texts, {} texts {} at time {}.\n".format(text_one[0], 
        text_one[1], text_one[2]))

# This retrieves and prints the last record
# from the calls list.
last_call = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds.".format(
        last_call[0], last_call[1], last_call[2], last_call[3]))