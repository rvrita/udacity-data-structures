# udacity-data-structures

### Problem 1: LRU Cache

The time complexity for each operation (`get` and `set`) is O(1). In order to achieve constant time, we need to maintain two data structures. A dictionary (hash map) allows constant time lookup of each element. But we also need a doubly linked list to keep track of the recently-used property, in order to avoid scanning in linear time. The dictionary stores references to the linked list nodes.

### Problem 2: File Recursion

In this problem we just pass a storage array to a recursive function (`find_files_inner`). The function adds all files it encounters to the array, or recurses if it encounters directories. The time complexity is O(n) in the total number of files. Or it might be O(n+k^m) where k is the average number of folders in each directory and m is the directory depth. But, practically speaking, the depth of the file system will be bounded and the files will be the dominating factor.

### Problem 3: Huffman Coding

This problem requires us to build a Huffman tree (binary tree), but in order to do that efficiently, we can use a priority queue. The Huffman tree building process (combine the smallest two nodes, add the result back to the pool) sounds like the perfect job for a priority queue. We also use a dictionary to create a lookup table from characters to Huffman codes so that we can construct the encoded string in linear time.

The time complexity to build the tree is O(n\*log(n)) and the time complexity to decode the tree is also O(n\*log(n)), since we're using a tree to decode. We could achieve O(1) if we used a lookup table, but the problem statement asks for a tree.

### Problem 4: Active Directory

This problem is very similar to the file recursion problem. Instead of files and directories, we are working with users and groups. We return true if we find the user, else  traverse all the subgroups. The runtime is O(n\*k^m) where n is number of users per group, k is number of subgroups per group, m is the depth of subgroups.

### Problem 5: Blockchain

The blockchain is a linked list. Creating the "toy" blockchain requires O(n) time, since `append` is a constant time operation. The sha256 hash depends on all previous nodes, but it is stored and updated incrementally.

### Problem 6: Union and Intersection

For both union and intersection operations, we convert the linked lists to a set. The set uses a hash in its underlying implementation, so adding or checking for existence of an element is constant time. The runtime of both `union` and `intersection` is O(m+n) where m and n are the length of each input list.
