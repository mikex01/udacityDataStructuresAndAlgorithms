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

def unique_records(list_of_list):
    """ Returns the number of the unique records """
    
    records = []
    for l in list_of_list:
        records += l[:2]
    return len(set(records))

all_register = texts + calls
print("\nThere are {} different telephone numbers in the records." \
      .format(unique_records(all_register)))