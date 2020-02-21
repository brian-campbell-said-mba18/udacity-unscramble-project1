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

# Third, this for loop creates two lists. If a number only calls,
# but never receives calls, it is put into a suspects list,
# failed_income_call_test. 
failed_income_call_test = []
for i in og_list:
    if i not in receive_list:
        failed_income_call_test.append(i)

# Fourth, I create a list of unique phone numbers that send texts.
text_senders = []
for i in texts:
    if i[0] not in text_senders:
        text_senders.append(i[0])

# Fifth, I create a test to determine of the phone numbers
# that failed the first incoming call test, which of those numbers
# also fail the text-sending test. I append these numbers to the list,
# failed_text_send_test.
failed_text_send_test = []
for i in failed_income_call_test:
    if i not in text_senders:
        failed_text_send_test.append(i)

# Sixth, I create a list of unique phone numbers that receive texts.
text_receivers = []
for i in texts:
    if i[1] not in text_receivers:
        text_receivers.append(i[1])

# Finally, I create a test to determine of the phone numbers that
# failed the text-senders test, which of these numbers fail the final
# test, the text-receiving tests. The numbers that fail are put into
# the list, flagged_suspects. I also sort the numbers in ascending order
# in flagged_suspects.
flagged_suspects = []
for i in failed_text_send_test:
    if i not in text_receivers:
        flagged_suspects.append(i)
flagged_suspects = sorted(flagged_suspects)

# This prints the results.
print("These numbers could be telemarketers: ")
for i in flagged_suspects:
    print(i)

