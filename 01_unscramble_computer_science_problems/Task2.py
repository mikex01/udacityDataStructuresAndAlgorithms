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

def longest_time(calls):
    """ Return a list of the number spent the longest time """
    
    dict_calls = {}
    for call in calls:
        for num_phone in call[:2]:
            dict_calls[num_phone] = dict_calls.get(num_phone, 0) + int(call[3])
    last_tuple = sorted(dict_calls.items(), key=lambda item: item[1])[-1]
    return list(last_tuple)

print("\n{0} spent the longest time, {1} seconds, on the phone during September 2016." \
      .format(longest_time(calls)[0], longest_time(calls)[1]))