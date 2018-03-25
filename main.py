#!/usr/bin/env python
# coding:utf-8

import hashlib as hasher
import datetime as date

# 首先定义区块，包含索引位置、时间戳、每个块中数据，以及上一个块的哈希
class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.hash_block()
    def hash_block(self):
        # 用sha256进行加密
        sha=hasher.sha256()
        # python3中需要对字符串进行 encode 操作,才能进行哈希
        sha.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode('utf-8') )
        print(sha.hexdigest())
        # 以十六进制返回哈希加密结果
        return sha.hexdigest()

# 创建一个起源块
def create_genesis_block():
    #手动构造块链，索引为0或者任意先前块链的散列
    return Block(0,date.datetime.now(),'xjw first block','0')

# 起源块后续的块链都会以何种方式创建，怎么创建
def create_next_block(last_block):
    index=last_block.index+1
    datestamp=date.datetime.now()
    data="the information of transaction"+str(index)
    prehash=last_block.hash
    return Block(index,datestamp,data,prehash)


if __name__ == '__main__':
    # 创建链并添加起源块
    blockchain=[create_genesis_block()]
    pre_blocck=blockchain[0]
    # 在起源块之后，后续加几个块链
    num_of_blocck_to_add=20
    # 添加我们党的块到链上
    for i in range(num_of_blocck_to_add):
        next_block=create_next_block(pre_blocck)
        blockchain.append(next_block)
        pre_blocck=next_block
