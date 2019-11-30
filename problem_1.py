class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "[ {} ]-> ".format(self.value[1]) + str(self.next)


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_head(self, node):
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        if self.tail == None:
            self.tail = node
        self.head = node

    def pop_tail(self):
        tail = self.tail
        if tail != None:
            new_tail = tail.prev
            new_tail.next = None
            self.tail = new_tail
        return tail

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dict = {}
        self.queue = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            node = self.dict[key]
            self.queue.remove(node)
            self.queue.push_head(node)
            value = node.value[1]
        else:
            value = -1
        return value

    def set(self, key, value):
        # If the key is in the cache 
        if key in self.dict:
            node = self.dict[key]
            # Update the value
            node.value = (key, value)
            # Move it back to top of queue
            self.queue.remove(node)
            self.queue.push_head(node)
        else:
            # Create a node
            node = Node((key, value))
            self.dict[key] = node
            self.queue.push_head(node)
            self.capacity -= 1
            # If the cache is at capacity remove the oldest item.
            if self.capacity < 0:
                node = self.queue.pop_tail()
                self.capacity += 1
                key = node.value[0]
                del self.dict[key]


my_cache = LRU_Cache(5)

my_cache.set(1, 1)
print(my_cache.queue) # [ 1 ]-> None
my_cache.set(2, 2)
print(my_cache.queue) # [ 2 ]-> [ 1 ]-> None
my_cache.set(3, 3)
print(my_cache.queue) # [ 3 ]-> [ 2 ]-> [ 1 ]-> None
my_cache.set(4, 4)
print(my_cache.queue) # [ 4 ]-> [ 3 ]-> [ 2 ]-> [ 1 ]-> None
print(my_cache.get(1))# returns 1
print(my_cache.queue) # [ 1 ]-> [ 4 ]-> [ 3 ]-> [ 2 ]-> None
print(my_cache.get(2))# returns 2
print(my_cache.queue) # [ 2 ]-> [ 1 ]-> [ 4 ]-> [ 3 ]-> None
print(my_cache.get(9))# returns -1 because 9 is not present in the cache
my_cache.set(5, 5)
print(my_cache.queue) # [ 5 ]-> [ 2 ]-> [ 1 ]-> [ 4 ]-> [ 3 ]-> None
my_cache.set(6, 6)
print(my_cache.queue) # [ 6 ]-> [ 5 ]-> [ 2 ]-> [ 1 ]-> [ 4 ]-> None
print(my_cache.get(3))# returns -1 because the cache reached capacity and 3 was evicted
my_cache.set(4, 44)   # Update existing value
print(my_cache.queue) # [ 44 ]-> [ 6 ]-> [ 5 ]-> [ 2 ]-> [ 1 ]-> None
my_cache.set(7, 7)
print(my_cache.queue) # [ 7 ]-> [ 44 ]-> [ 6 ]-> [ 5 ]-> [ 2 ]-> None
