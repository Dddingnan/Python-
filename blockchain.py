
from block import Block
import datetime

num_blocks_to_add = 30  ##區塊鏈數量

block_chain = [Block.create_genesis_block()]

print("初始區塊已建立")
print("Hash: %s" % block_chain[0].hash)

for i in range(1, num_blocks_to_add):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))   ##區塊相互鏈結
    print("區塊 #%d 建立." % i)
    print("Hash: %s" % block_chain[-1].hash)