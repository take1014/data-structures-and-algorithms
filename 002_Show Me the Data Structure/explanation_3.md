# Problem 3 : Huffman Coding
I used Queue and tree structures to solve the Huffman coding problem.
1. 'huffman_encoding'
First, if the data length is 0, a warning sentence is returned.
Second, decompose the string into characters, count the number of characters, and save. I sort and take this out to create a tree.
Finally I save the character of the encoded word stored in the tree for the output variable.

2. 'huffman_decoding'
First and foremost, I take a letter out of the tree and store it in the dictionary.
Finally, I take the characters in the encoded string and create the decoded string.

# Time complexity
Huffman Coding's time complexity is `O(nlogn)` and Huffman Decoding's time complexity is 'O(n)', so all time complexity is 'O(nlogn)'. Space complexity is `O(logn)`.
