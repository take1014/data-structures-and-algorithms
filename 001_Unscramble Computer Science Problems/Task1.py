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
def addTelNumbers( datas, numbers ):

    # O(n)
    for i in range(len(datas)):
        if datas[i][0] not in numbers:
            numbers.append(datas[i][0])
        if datas[i][1] not in numbers:
            numbers.append(datas[i][1])

if __name__ == '__main__':
    numbers =[]
    addTelNumbers( texts, numbers )
    addTelNumbers( calls, numbers )
    print("There are {} different telephone numbers in the records.".format(len(numbers)))
