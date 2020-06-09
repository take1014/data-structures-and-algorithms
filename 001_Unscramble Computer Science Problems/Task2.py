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

def updateDicList( calls, dic_list ):
    # O(n)
    for call in calls:
        if( str(call[0]) in dic_list ):
            dic_list[str(call[0])] += int(call[3])  # update dic_list value
        else:
            dic_list[str(call[0])] = int(call[3])   # add dic_list and update dic_list_value

        if( str(call[1]) in dic_list ):
            dic_list[str(call[1])] += int(call[3])  # update dic_list value
        else:
            dic_list[str(call[1])] = int(call[3])   # add dic_list and update dic_list_value

if __name__ == '__main__':

    dic_list = {}
    updateDicList( calls, dic_list )

    max_tel_num = ''    # string
    max_call_total_time = 0
    # O(n)
    for dic_idx in dic_list:
        if dic_list[dic_idx] >= max_call_total_time:
            max_call_total_time = dic_list[dic_idx]
            max_tel_num = dic_idx

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        max_tel_num,            # telephone number
        max_call_total_time))   # total call time
