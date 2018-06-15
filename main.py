#!/usr/bin/env python
# coding:utf-8

import math,decimal
import hashlib as hasher
import datetime as date


# 首先定义区块，包含索引位置、时间戳、每个块中数据，以及上一个块的哈希
class Block:
    ''' 区块信息存储 '''

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # 索引
        self.timestamp = timestamp  # 时间戳
        self.data=data  # 事物列表
        self.previous_hash=previous_hash  # 前块的散列
        self.hash = self.hash_block()
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
    index = last_block.index + 1


    datestamp = date.datetime.now()
    data = "the information of transaction" + str(index)
    prehash = last_block.hash
    return Block(index,datestamp,data,prehash)


# class BlockChain(object):




if __name__ == '__main__':
    # # 创建链并添加起源块
    # blockchain = [create_genesis_block()]
    # pre_blocck = blockchain[0]
    # # 在起源块之后，后续加几个块链
    # num_of_blocck_to_add = 2
    # # 添加我们党的块到链上
    # for i in range(num_of_blocck_to_add):
    #     next_block = create_next_block(pre_blocck)
    #     blockchain.append(next_block)
    #     pre_blocck = next_block

#######################################################################################################################
#######################################################################################################################

    # 十六进制转字符串
    # str = bytes.fromhex('04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73')
    str = bytes.fromhex('04ffff001d0168')
    print(str)

    str = bytes.fromhex('9c50cee8d50e273100987bb12ec46208cb04a1d5b68c9bea84fd4a04854b5eb1')
    print(str)

    print(int(2**1424))




"""
    # 比特币挖矿难度计算的数学原理
    lg = math.log
    e = math.e
    print(0x00ffff * 2**(8*(0x1d-3))/float(0x0404cb * 2**(8*(0x1b-3))))
    print(lg(0x00ffff * 2 ** (8 * (0x1d - 3)) / float(0x0404cb * 2 ** (8 * (0x1b - 3)))))
    print(lg(0x00ffff * 2 ** (8 * (0x1d - 3))) - lg(0x0404cb * 2 ** (8 * (0x1b - 3))))
    print(lg(0x00ffff) + lg(2 ** (8 * (0x1d - 3))) - lg(0x0404cb) - lg(2 ** (8 * (0x1b - 3))))
    print(lg(0x00ffff) + (8 * (0x1d - 3))*lg(2) - lg(0x0404cb) - (8 * (0x1b - 3))*lg(2))
    print(lg(0x00ffff/float(0x0404cb))+ (8 * (0x1d - 3))*lg
    
    
    
    (2) -(8 * (0x1b - 3))*lg(2))
    print(lg(0x00ffff / float(0x0404cb)) + (0x1d - 0x1b) * lg(2**8))
"""













