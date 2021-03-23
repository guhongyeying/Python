# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 11:11
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : run.py
# @Software: OA

from design_patterns.factory.singleton2 import Singletion0, Singletion, Singleton2


if __name__ == '__main__':


    # s11 = Singletion0()
    # print("===========")
    # s22 = Singletion0()
    # print(id(s11), id(s22))


    print("|----------------------")
    # s1 = Singleton2()
    #
    # print("===========",id(s1.getIntance()))
    # s2 = Singleton2()
    #
    # print(id(s1),id(s2))
    s1 = Singleton2()
    s1.getIntance()
    s2 = Singleton2()
    print(id(s1), id(s2))

