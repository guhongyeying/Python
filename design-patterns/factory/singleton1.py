# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 16:13
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : singleton.py
# @Software: OA
# -*- coding: utf-8 -*-


class singleton:
    """单列模式"""
    def __new__(cls):
        if not hasattr(cls, "instalce"):
            cls.instalce = super(singleton, cls).__new__(cls)
        return cls.instalce


# if __name__ == '__main__':
#     s1 = singleton()
#     s2 = singleton()
#     print(s1)
#     print(s2)

import  threading
class Singleton2:
    _instance = None
    def __init__(self):
        if not Singleton2._instance:
            print("init method called")
        else:
            print("instarads arj feret",self.getIntance())

    @classmethod
    def getIntance(cls):
        if not cls._instance:
            cls._instance = Singleton2()
        return  cls._instance

#----------------------------------------------------------------------------------------------------------------------
import threading
from functools import wraps


class Decotor:

    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def singleton(cls):

        @wraps(cls)
        def _wwraps(*arg, **kwras):
            with Decotor._lock:
                if not Decotor._instance:
                    Decotor._instance = cls(*arg, **kwras)

                # return Decotor._instance
            return Decotor._instance

        return _wwraps


@Decotor.singleton
class DecoratorSingleton(object):

    def __init__(self):
        print("---__init__---")


# if __name__ == '__main__':
#
#     s1 =  DecoratorSingleton()
#     s3 = DecoratorSingleton()
#     print(id(s1))
#     print(id(s3))
#

#---------------------------------------------------
class Borg:
    __shared_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state

b = Borg()
b1 = Borg()
b.x = 4

print(b.__dict__)
print(b1.__dict__)



#------------------------------------------------------------------ 元类的方式创建


class ClassKis(type):
    _instance = {}


    def __call__(cls, *args, **kwargs):
        if cls not  in cls._instance:
            cls._instance[cls] = super(ClassKis,cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Logger(metaclass=ClassKis):
    pass


logger1 = Logger()
logger2 = Logger()
print(id(logger1),id(logger2))
if id(logger1) == id(logger2):
    print("=-=-")
    print(id(logger1),id(logger2))

