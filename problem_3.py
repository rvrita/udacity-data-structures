import sys
from collections import defaultdict
from pprint import pprint

class BinaryNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node" + repr(vars(self))

# Let's implement a heap from scratch
class Heap(object):
    def __init__(self):
        self.arr = []
        self.size = 0

    def insert(self, tuple):
        # tuple[0] will be used for value comparison
        self.arr.append(tuple)
        self.bubble_up(self.size)
        self.size += 1

    def delete(self):
        # swap first and last values in heap
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        val = self.arr.pop(-1)
        self.size -= 1
        self.sift_down(0)
        return val

    def bubble_up(self, i):
        parent = int((i - 1) / 2);
        if (self.arr[parent]):
            if (self.arr[i][0] < self.arr[parent][0]):
                # swap
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                self.bubble_up(parent)

    def sift_down(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        arr = self.arr
        size = self.size

        if left < size and arr[left][0] < arr[largest][0]:
            largest = left
        if right < size and arr[right][0] < arr[largest][0]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.sift_down(largest)

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

    # Method One: implicit Huffman tree from heap
    # heap = Heap()
    # for char, freq in char2freq.items():
    #     # freq will be used as value for comparison
    #     heap.insert([freq, [char, ""]])

    # pprint(heap.arr)

    # while heap.size > 1:
    #     lo = heap.delete()
    #     hi = heap.delete()
    #     print(lo, hi)
    #     for pair in lo[1:]:
    #         pair[1] = '0' + pair[1]
    #     for pair in hi[1:]:
    #         pair[1] = '1' + pair[1]
    #     heap.insert([lo[0] + hi[0]] + lo[1:] + hi[1:])

    # pprint(heap.arr)

    # lookup = {}
    # pairs = heap.delete()[1:]
    # for char, binary in pairs:
    #     lookup[char] = binary

    # encoded_data = ""
    # for char in data:
    #     encoded_data += lookup[char]

    # pprint(lookup)
    # print(encoded_data)

    # Method Two: build explicit Huffman tree
    pq = Heap() # priority queue
    for char, freq in char2freq.items():
        pq.insert([freq, BinaryNode(char)])

    while pq.size > 1:
        left = pq.delete()
        right = pq.delete()
        freq = left[0] + right[0]
        parent = BinaryNode(None, left[1], right[1])
        pq.insert([freq, parent])

    tree = pq.delete()[1]

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

encoded_data, tree = huffman_encoding("heeelllo world")

print(encoded_data)

decoded_data = huffman_decoding(encoded_data, tree)

print(decoded_data)

# if __name__ == "__main__":
#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))
