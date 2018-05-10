# -*- coding: utf-8 -*-
"""
===========================================
 @Time    : 2018/5/9 15:26
 @Author  : allinXallin
 @Email   : sa15225038@mail.ustc.edu.cn
 @File    : test.py
 @Software: 哈哈，接受挑战吧！PyCharm 
===========================================
"""



import time

def consumer():
    r = ''
    while True:
        n = yield r  # yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始。
        if not n:
            return '21'
        print('[CONSUMER]   Consuming %s:..'%n)
        time.sleep(1)
        r='200 OK'


def produce(consumer):
    #next(consumer)  # 第一次调用时必须先next()或send(None)，否则会报错,send后之所以为None是因为这时候没有上一个yield(根据第8条)。可以认为，next()等同于send(None)。
    consumer.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER]   Produceing %s..'%n)
        r= consumer.send(n)  # send(n)与next()的区别在于send可以传递参数给yield表达式;send(n)与next()都有返回值，它们的返回值是当前迭代遇到yield时，yield后面表达式的值，其实就是当前迭代中yield后面的参数。
        print('[PRODUCER]    Consumer return: %s' % r)
    consumer.close()


def fun123():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    c=consumer()
    produce(c)
    #
    # for item in fun123():
    #     print(item)