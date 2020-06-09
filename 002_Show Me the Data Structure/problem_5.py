import datetime
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp     = timestamp
        self.data          = data
        self.previous_hash = previous_hash
        self.hash          = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.timestamp.encode('utf-8') + self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp_data = self.last
            self.last = Block(timestamp, data, temp_data)
            self.last.previous_hash = temp_data

    def is_empty(self):
        return self.head is None

def get_timestamp():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


# blocks
block_zero = Block(get_timestamp(), "Information A", 0)
block_one = Block(get_timestamp(), "Information B", block_zero)
block_two = Block(get_timestamp(), "Information C", block_one)

# linked list
linked_list = LinkedList()
linked_list.append(get_timestamp(), "Information X")
linked_list.append(get_timestamp(), "Information Y")

# Test case
print("Block 0")
print("Timestamp: ", block_zero.timestamp)
print("Data: ", block_zero.data)
print("SHA256 Hash: ", block_zero.hash)
print("Prev_Hash: ", 0)

print("Block 1")
print("Timestamp: ", block_one.timestamp)
print("Data: ", block_one.data)
print("SHA256 Hash: ", block_one.hash)
print("Prev_Hash: ", block_one.previous_hash.data)

print("Block 2")
print("Timestamp: ", block_two.timestamp)
print("Data: ", block_two.data)
print("SHA256 Hash: ", block_two.hash)
print("Prev_Hash: ", block_two.previous_hash.data)

print("Linked list last data : ", linked_list.last.data)
print("Linked list last's previous hash data : ", linked_list.last.previous_hash.data)


#Block 0
#Timestamp:  14/04/2020 13:48:52
#Data:  Information A
#SHA256 Hash:  f18fd54101bec05852d62e1d91c1a4042e34e7ec40bf5e988bb3e35fd19bd98d
#Prev_Hash:  0
#Block 1
#Timestamp:  14/04/2020 13:48:52
#Data:  Information B
#SHA256 Hash:  64068f26fa771e2785a29810a53a1cd19169358acad7bbc63204d6dd9adc5fbd
#Prev_Hash:  Information A
#Block 2
#Timestamp:  14/04/2020 13:48:52
#Data:  Information C
#SHA256 Hash:  0edb88e64bf55a2dcb0ecf7d79e8a59f86b714ddcd09d7f318e09bb89b85cb1d
#Prev_Hash:  Information B
#Linked list last data :  Information Y
#Linked list last's previous hash data :  Information X

print(linked_list.is_empty())
# False
linked_list2 = LinkedList()
print(linked_list2.is_empty())
# True
