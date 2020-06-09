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

if __name__ == '__main__':
    #print(texts[0][0])  incoming number
    #print(texts[0][1])  answering number
    #print(texts[0][2])  time
    print("First record of texts, {} texts {} at time {}".format(
        texts[0][0],    #incoming number
        texts[0][1],    #answering number
        texts[0][2]) )  #time

    #print(calls[0][0])  incoming number
    #print(calls[0][1])  answering number
    #print(calls[0][2])  time
    #print(calls[0][3])  during
    last_idx = len(calls)-1
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
        calls[last_idx][0],     #incoming number
        calls[last_idx][1],     #answering number
        calls[last_idx][2],     #time
        calls[last_idx][3]) )   #during

