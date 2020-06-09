import sys

def huffman_encoding(data):
    encoder_dict = {}  # encorder dictionary
    tree     = {}       # tree dictionary
    temp_str = '1'      # temporary string
    encoded_str = ""    # encoded string

    if len(data) is 0:
        print("Null value is not accepted")
        return

    for char in data:
        encoder_dict[char] = encoder_dict.get(char, 0) + 1

    for num in sorted(encoder_dict.items(), key=lambda x: x[1]):   # sorted encoder_dict
        tree[num[0]] = temp_str
        temp_str = '0' + temp_str

    for char in data:
        encoded_str += tree[char]

    return encoded_str, tree


def huffman_decoding(data, tree):
    decoder_dict = {}                  # temporary dictionary
    temp_str, decoded_str = "", ""  # temporary empty string and decoded empty string!

    # getting characters from tree
    for char in tree:
        # update decoder dict
        decoder_dict[tree[char]] = char

    for char in data:
        if char == '1':
            decoded_str += decoder_dict[temp_str + char]
            temp_str = ''
        else:
            temp_str += char

    return decoded_str

# Test case
if __name__ == "__main__":

    # Normal case
    print("========== Normal case ==========")
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 48
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 1000000100000001000000000001010000000010000000001000000000010000000000010000000010010000000000010001000000100000001000000000001000010000010000000001000000000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word


    # Edge case
    print("========== Edge case ==========")
    edge_case_sentence = "aaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(edge_case_sentence)))
    # The size of the data is: 52
    print("The content of the data is: {}\n".format(edge_case_sentence))
    # The content of the data is: aaa

    encoded_data, tree = huffman_encoding(edge_case_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 28
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 111

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 52
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: aaa

    # Null values case
    print("========== Null values case ==========")
    null_values_case_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(null_values_case_sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(null_values_case_sentence))
    # The content of the data is:

    huffman_encoding(null_values_case_sentence)
    # Null value is not accepted

