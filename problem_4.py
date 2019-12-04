class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "{} -> ".format(self.value) + str(self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # set uses a hash map, which will give better than O(n) insertion time
    values = set()
    for node in [llist_1.head, llist_2.head]:
        while node:
            values.add(node.value)
            node = node.next
    union = LinkedList()
    for value in values:
        union.append(value)
    return union


def intersection(llist_1, llist_2):
    set1 = set()
    node = llist_1.head
    while node:
        set1.add(node.value)
        node = node.next

    set2 = set()
    node = llist_2.head
    while node:
        if node.value in set1:
            set2.add(node.value)
        node = node.next

    intersection = LinkedList()
    for value in set2:
        intersection.append(value)
    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

elements_1 = [3,2,4,35,6,65,6,4,3,21]
elements_2 = [6,32,4,9,6,1,11,21,1]

for i in elements_1:
    linked_list_1.append(i)

for i in elements_2:
    linked_list_2.append(i)

# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> None
print (union(linked_list_1,linked_list_2))
# 4 -> 21 -> 6 -> None
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

elements_3 = [3,2,4,35,6,65,6,4,3,23]
elements_4 = [1,7,8,9,11,21,1]

for i in elements_3:
    linked_list_3.append(i)

for i in elements_4:
    linked_list_4.append(i)

# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> None
print (union(linked_list_3,linked_list_4))
# None
print (intersection(linked_list_3,linked_list_4))

# Test case 3 - union of two empty lists

linked_list_5 = LinkedList()

# None
print(union(linked_list_5, linked_list_5))

# Test case 4 -  intersection of same list

# 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> None
print(intersection(linked_list_4, linked_list_4))
