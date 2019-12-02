import sys
import math
from heapq import heappush, heappop
from collections import defaultdict
from pprint import pprint

class BinaryNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node" + repr(vars(self))

    def __lt__(self, other):
        return True

def walk_tree(node, path):
    if not node:
        return {}
    if node.val:
        return { node.val: path }
    # merge left branch and right branch into a single dictionary
    return { **walk_tree(node.left, path + '0'), **walk_tree(node.right, path + '1') }

def huffman_encoding(data):
    char2freq = defaultdict(int)
    for char in data:
        char2freq[char] += 1 # without defaultdict: ... = char2freq.get(char, 0) + 1

    # Fix for input of one repeated character
    if len(char2freq.keys()) == 1:
        char2freq['dummy'] = 0

    # Build Huffman tree
    pq = [] # priority queue
    for char, freq in char2freq.items():
        # Heap operations use the first item (freq) for value comparison
        heappush(pq, [freq, BinaryNode(char)])

    while len(pq) > 1:
        left = heappop(pq)
        right = heappop(pq)
        freq = left[0] + right[0]
        parent = BinaryNode(None, left[1], right[1])
        heappush(pq, [freq, parent])

    tree = heappop(pq)[1]

    # Build dictionary
    lookup = walk_tree(tree, '')
    encoded_data = ''.join([lookup[char] for char in data])

    return encoded_data, tree

def huffman_decoding(data, tree):
    decoded_data = ''
    node = tree
    for bit in data:
        if bit == '0':
            node = node.left
        elif bit == '1':
            node = node.right
        if node.val:
            decoded_data += node.val
            node = tree

    return decoded_data

def test_encode_decode(data):
    encoded_data, tree = huffman_encoding(data)
    data_size = len(data)
    encoded_size = len(encoded_data)/8
    print ("Input:        {}".format(data))
    print ("Input size:   {} bytes".format(data_size))
    print ("Encoded:      {}".format(encoded_data))
    print ("Encoded size: {} bytes (Ratio: {})".format(encoded_size, encoded_size/data_size))

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("Input data = decoded data? {}\n".format(data == decoded_data))


if __name__ == "__main__":
    test_encode_decode("FFFFFFFFFFFFFFFF") # 1, 16
    test_encode_decode("abcdefghijklmnop") # 16, 16
    test_encode_decode("abcdefghijklmnopabcdefghijklmnop")
    test_encode_decode("FFFFFFFFFFFFFFFFabcdefghijklmnop")
    test_encode_decode("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb") # 2, 32
    test_encode_decode("aaaaaaaaaaabbbbbbbbbbbcccccccccc") # 3, 32
    test_encode_decode("aaaaaaaabbbbbbbbccccccccdddddddd") # 4, 32
    test_encode_decode("aaaaaaaabbbbbbbccccccddddddeeeee") # 5, 32
