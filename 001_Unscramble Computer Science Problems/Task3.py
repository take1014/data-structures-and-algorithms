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
def isBangaloreCall(call):
    if '(080)' in call:
        return True
    else:
        return False

def extractAreaCodes(call):
    if   call[0:2] == '(0':
        return call.split(sep=')')[0] + ')'

    elif call[0:3] == '140':
        return call[0:3]

    else:
        return call[0:4]

if __name__ == '__main__':
    bangalore_prefix_called = []
    total_call_cnt     = 0
    bangalore_call_cnt = 0
    for call in calls:
        if isBangaloreCall(call[0]):    # Is bangalore call?
            total_call_cnt += 1
            if extractAreaCodes(call[1]) not in bangalore_prefix_called:
                bangalore_prefix_called.append(extractAreaCodes(call[1]))

            if isBangaloreCall(call[1]): # Is bangalore call?
                bangalore_call_cnt += 1

    # sort
    bangalore_prefix_called.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    #print(bangalore_prefix_called)

    # part A
    #The list of codes should be print out one per line in lexicographic order with no duplicates.
    for prefix in bangalore_prefix_called:
        print(prefix)

    # part B
    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(bangalore_call_cnt/total_call_cnt*100, 2)))
