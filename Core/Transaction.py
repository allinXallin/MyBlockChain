# -*- coding: utf-8 -*-
"""
===========================================
 @Time    : 2018/4/25 17:47
 @Author  : allinXallin
 @Email   : sa15225038@mail.ustc.edu.cn
 @File    : Transaction.py
 @Software: 哈哈，接受挑战吧！PyCharm 
===========================================
"""


from abc import ABCMeta


# 一切交易的基类
class Transaction(metaclass=ABCMeta):

    #  Maximum number of attributes that can be contained within a transaction
    # 一个交易所能包含的最大属性数
    __MaxTransactionAttributes__ = 16

    # Reflection cache for TransactionType
    #

