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

def possible_telemarketers(texts, calls):
    """ Return list of possible telemarketers"""
    not_telemarketers = []
    possible_telemarketers = []
    telemarketers = []

    for text in texts:
        not_telemarketers += text[:2]
    for call in calls:
        not_telemarketers += call[1:2]
    for call in calls:
        possible_telemarketers += call[0:1]

    not_telemarketers = set(not_telemarketers)
    possible_telemarketers = set(possible_telemarketers)

    for pt in possible_telemarketers:
        if pt not in not_telemarketers:
            telemarketers.append(pt)

    return set(telemarketers)

print("These numbers could be telemarketers:\n" \
     + "\n".join(sorted(possible_telemarketers(texts, calls))))