import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.ts = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def __str__(self):
        return ("timestamp: {}\n" 
            "data: {}\n"
            "hash: {}\n"
            "previous_hash: {}") \
        .format(self.ts, self.data, self.hash, self.previous_hash)

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "{} {} {}".format(self.previous_hash, self.ts, self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        output = "{}\n----------------\n".format(self.value)
        if self.next:
            return output + str(self.next) 
        else:
            return output

        return output + str(self.next) if self.next else output

        return self.next ? output + str(self.next) : output

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head:
            return str(self.head) 
        else:
            return "Empty blockchain!\n"

    def add_block(self, data):
        timestamp = datetime.datetime.now()
        head = self.head
        previous_hash = head.value.hash if head is not None else None;
        block = Block(timestamp, data, previous_hash)
        node = Node(block)
        if self.tail:
            self.tail.next = node
        if self.head is None:
            self.head = node
        self.tail = node


# Test Data

blockchain = Blockchain()
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")
print(blockchain)
# timestamp: 2019-12-04 00:44:21.641376
# data: Block 1
# hash: 06ce343e4c14e1f24ec1aa544cc40559cdcb4e306285cb91ac4ac77949eedc8f
# previous_hash: None
# ----------------
# timestamp: 2019-12-04 00:44:21.641413
# data: Block 2
# hash: 4a7330a16d02cae9e91dffbb28898d90c3f96c4aee384aaf848f728a3b7bd891
# previous_hash: 06ce343e4c14e1f24ec1aa544cc40559cdcb4e306285cb91ac4ac77949eedc8f
# ----------------
# timestamp: 2019-12-04 00:44:21.641422
# data: Block 3
# hash: 2fd8e93754b26d4ceba701b93c0a321ff6aa4c26c894c94d11674dc59f2601cf
# previous_hash: 06ce343e4c14e1f24ec1aa544cc40559cdcb4e306285cb91ac4ac77949eedc8f
# ----------------

blockchain_with_none_data = Blockchain()
blockchain_with_none_data.add_block(None)
blockchain_with_none_data.add_block("")
print(blockchain_with_none_data)
# timestamp: 2019-12-04 00:44:21.641479
# data: None
# hash: 0d66c9485ab19f7b9c071db0e475c5495c5bd90354fd31c1cec550d4d85dc95e
# previous_hash: None
# ----------------
# timestamp: 2019-12-04 00:44:21.641506
# data:
# hash: 82baea3aeb5dc8fb9c0491ae932427c7211991b95dc56a63481b62ec0de5b240
# previous_hash: 0d66c9485ab19f7b9c071db0e475c5495c5bd90354fd31c1cec550d4d85dc95e
# ----------------


empty_blockchain = Blockchain() 
print(empty_blockchain)
# Empty blockchain!
