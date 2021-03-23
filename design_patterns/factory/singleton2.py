# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 16:13
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : singleton.py
# @Software: OA
# -*- coding: utf-8 -*-
class Singletion0:
    pass

class Singletion:

    def __new__(cls, *args, **kwargs):
        print("==1=")
        if not hasattr(cls, "instance"):
            cls.instance = super(Singletion, cls).__new__(cls)
        return  cls.instance

class Singleton2:
    _instance = None


    def __init__(self):
        print("__init__")
        if not Singleton2._instance:
            print("init method called")
        else:
            print("create instance",self.getIntance())

    @classmethod
    def getIntance(cls):
        print("getIntance")

        if not cls._instance:
            cls._instance = Singleton2()
        return  cls._instance


# if __name__ == '__main__':
#     import Sin
#     s1 = Singletion()
#     s2 = Singletion()
#
#     print(id(s1), id(s2))