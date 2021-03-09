# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 11:16
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : prototype.py.py
# @Software: OA
"""
原型模式
用原型实例指定创建对象的种类, 并且通过拷贝这些原型创建新的对象
- 原型模型其实是从一个对象再创建另外一个可定制的对象, 而且不需要知道任何创建细节
- 一般在初始化信息不发生变化的情况下, 克隆是最好的办法, 既隐藏了对象创建的细节, 有提高了性能
在不指定类名的前提下生成实例
- 对象种类繁多, 无法将它们整合到一个类中
- 难以根据类生成实例时
- 解耦框架与生成实例: 让框架不依赖于具体的类, 不能指定类名来生成实例, 要实现注册一个原型
  然后, 通过复制该实例来生成新的实例
why: 一旦在代码中出现要使用的类的名字, 就无法与该类分离开来, 也就无法实现复用
示例:
"""

import copy
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):

    def __init__(self, id_value):
        self._id = id_value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @abstractmethod
    def clone(self):
        pass


class ConcreatePrototypeA(Prototype):

    def clone(self):
        return copy.copy(self)


class ConcreatePrototypeB(Prototype):

    def clone(self):
        return copy.copy(self)


class Manger:

    def __init__(self):
        self._dict = {}

    def register(self, name, value):
        self._dict[name] = value

    def create(self, name):
        return self._dict[name].clone()

if __name__ == '__main__':
    aa = ConcreatePrototypeA(1)
    bb = ConcreatePrototypeB(2)

    m = Manger()

    m.register("aa", aa)

    m.register("bb", bb)

    x = m.create("aa")
    y = m.create("bb")

    print(x.id)
    print(y.id)



