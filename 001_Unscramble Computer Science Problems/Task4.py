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
if __name__ == '__main__':
    # set call_senders and call_recivers
    call_senders  = []
    call_receivers = []
    for call in calls:
        if( call[0] not in call_senders ):
            call_senders.append(call[0])
        if( call[1] not in call_receivers ):
            call_receivers.append(call[1])
    print(call_senders)

    # set text_senders and text_recivers
    text_senders  = []
    text_receivers = []
    for text in texts:
        if( text[0] not in text_senders ):
            text_senders.append(text[0])
        if( text[1] not in text_receivers ):
            text_receivers.append(text[1])

    telemarketers = []
    for call_sender in call_senders:
        if (call_sender not in call_receivers  and
            call_sender not in text_senders    and
            call_sender not in text_receivers):
            telemarketers.append(call_sender)

    # sort
    telemarketers.sort()

    print("\n These numbers could be telemarketers:")
    for telemarketer in telemarketers:
        print(telemarketer)
