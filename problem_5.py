import hashlib

class Block:
    def __init__(self, timestamp, data, prev_block):
        self.ts = timestamp
        self.data = data
        self.prev_block = prev_block
        self.hash = self.calc_hash()

    def __str__(self):
        return "[ {} {} ]-> ".format(self.data[:3], self.hash[:3]) + str(self.prev_block)

    def calc_hash(self):
        sha = hashlib.sha256()
        prev_hash = self.prev_block.hash if self.prev_block else 0
        hash_str = "{} {} {}".format(prev_hash, self.ts, self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

# Test Data
blockchain_head = None
blockchain_head = Block(10000, "Hey", blockchain_head)
blockchain_head = Block(20000, "Foo", blockchain_head)
blockchain_head = Block(20000, "Foo", blockchain_head)
blockchain_head = Block(30000, "Bar", blockchain_head)

# [ Bar 325 ]-> [ Foo 1b0 ]-> [ Foo 9a1 ]-> [ Hey 7d2 ]-> None
print(blockchain_head)
