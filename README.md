# udacity-data-structures

### Problem 1: LRU Cache

The time complexity for each operation (`get` and `set`) is O(1). The space complexity is O(n). In order to achieve constant time, we need to maintain two data structures. A dictionary (hash map) allows constant time lookup of each element. But we also need a doubly linked list to keep track of the recently-used property, in order to avoid scanning in linear time. The dictionary stores references to the linked list nodes.

### Problem 2: File Recursion

In this problem we just pass a storage array to a recursive function (`find_files_inner`). The function adds all files it encounters to the array, or recurses if it encounters directories. The file system is a tree structure where files are leaves and directories are internal nodes. The time complexity is O(n) in the total number of files and directories. The space complexity is O(n). We have to store an array of matching file paths, which may scale up linearly as the file system grows. But also, we must account for the space required by the call stack of the recursive function. This reduces down to O(n) in the worst case of _n_ nested directories:

```
 Dir 1
 '- Dir 2
    '- Dir 3
       '- ...
          '- Dir n
```

### Problem 3: Huffman Coding

This problem requires us to build a Huffman tree (binary tree), but in order to do that efficiently, we can use a priority queue. The Huffman tree building process (combine the smallest two nodes, add the result back to the pool) sounds like the perfect job for a priority queue. We also use a dictionary to create a lookup table from characters to Huffman codes so that we can construct the encoded string in linear time.

The time complexity to build the tree is O(n). During tree construction, we do some heap pop operations on the character table, but this only scales up with the number of _unique_ characters. We do a linear scan on the input, with a constant time lookup in the dictionary of Huffman codes, to encode the output in O(n) time. 

The time complexity to decode the tree is O(n), since it requires a fixed number of operations (traversal) per input bit. Again, the depth of the Huffman tree depends only on the size of the character set, not on the input size.

The space complexity is O(m) where m is the size of the character set. In practical terms, I think this is O(1). 

### Problem 4: Active Directory

This problem is very similar to the file recursion problem. Instead of files and directories, we are working with users and groups. We return true if we find the user, else  traverse all the subgroups. The runtime is O(n\*k^m) where n is number of users per group, k is number of subgroups per group, m is the depth of subgroups. Or, O(n) where n is the total number of users and groups.

The space needed to create the call stack is also O(n) in the worst case of _n_ nested groups.

### Problem 5: Blockchain

The blockchain is a linked list. Creating the "toy" blockchain requires O(m\*n) time, where _m_ is the size of input data, and _n_ is the number of blocks. Time to hash the data (sha256) will grow linearly with the data size, and `add_block` is otherwise a constant time operation. The sha256 hash depends on all previous nodes, but it is stored and updated incrementally.

The space complexity is O(m\*n) because the additional data (linked list nodes, timestamp, etc.) are constant factors. For example, each block has the same 28 byte overhead.

### Problem 6: Union and Intersection

For both union and intersection operations, we convert the linked lists to a set. The set uses a hash in its underlying implementation, so adding or checking for existence of an element is constant time. The runtime of both `union` and `intersection` is O(m+n) where m and n are the length of each input list.

Space complexity is O(m+n) because we are internally copying the data into new structures.
