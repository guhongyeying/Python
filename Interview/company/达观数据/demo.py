# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 15:12
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : demo.py
# @Software: OA


#有一个1到9范围的随机数，调用一次得到一个0.2到0.8的范围。
def rangd9():
    pass

def range0():
    x = -1
    while not 2<=x<=8:
        x = rangd9()
    return x

#快排
import time

def quit_sort(listData):
    _len = len(listData)
    if _len < 2:
        return listData

    _tempData = listData[0]
    _leftList = []
    _rightList = []

    for i in range(1,_len):
        if listData[i] <_tempData:
            _leftList.append(listData[i]);
        else:
            _rightList.append(listData[i]);
    return quit_sort(_leftList) + [_tempData] + quit_sort(_rightList)

#二分查找算法 一个是查找，另一个是排序 快排

def two_find(listData,traget):
    _len = len(listData)
    if _len >0:
        _temData = listData[_len//2]
        _mid = _len//2
        if traget == _temData or _len <=1:
            return True
        elif traget < _temData:
            return two_find(listData[:_mid],traget)
        else:
            return two_find(listData[_mid+1:],traget)
    return  False

#覆盖索引 不回表查询，建立联合索引

# 是什么算法:1. 用 python 实现栈 用list。pop

# 2. 用 python 实现链表https://www.cnblogs.com/russellluo/p/3285045.html


#给定一个字符串，找到最长子字符串的长度，要求子字符串中所有字符不重复。
class Solution(object):

    def lenStr(self ,s:str) -> int:
        pos = {}
        res = temp = 0
        i = -1
        for j in range(len(s)):
            i = pos.get(s[j],-1)
            pos[s[j]] = j
            temp = temp + 1 if temp < j-i else j-i
            res = max(temp,res)

        return res

#有两个有序链表A和B，合并A和B成为一个新的有序列表C，并去除其中的重复元素。尽量不要开辟新的存储空间，时间复杂度O(n)。

#两数之和
def bp(nums, traget):
    dp = [0]*traget

    hash = {}
    for i in range(len(nums)):

        if (traget-nums[i])  in hash.keys():
            return i,hash[traget-nums[i]]

        hash[nums[i]]  = i





