# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 14:48
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : builder.py.py
# @Software: OA
"""
建造者模式
将一个复杂对象的构建与它的表示分离, 使得同样的构建过程可以创建不同的表示
- 用户只需指定需要建造的类型, 不需要知道具体地建造过程和细节
- 建造者模式是在当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时适用的模式
- 可替换性
举例:
一篇文章, 存在很多结构, 例如title/author/content/create_time等, 系统输出时, 要分两种方式展现
text和html, 输出每一部分的实现都不一样, 此时, 上层不需要知道底层两个输出格式是如何实现的
"""
from abc import ABCMeta, abstractmethod

class Product:
    def __init__(self):
        self._parts = []

    def add(self,part):
        self._parts.append(part)

    def show(self):
        print('-'.join(item for item in self._parts))


class Builder(metaclass=ABCMeta):

    @abstractmethod
    def build_part1(self):
        pass

    @abstractmethod
    def build_part2(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

class BuilderA(Builder):

    def __init__(self):
        self._product = Product()
    def build_part1(self):
        self._product.add("part1")

    def build_part2(self):
        self._product.add("part2")

    def get_product(self):
        return  self._product


class BuilderB(Builder):

    def __init__(self):
        self._product = Product()

    def build_part1(self):
        self._product.add("part1")

    def build_part2(self):
        self._product.add("part2")

    def get_product(self):
        self._product = Product()

class Director:

    @staticmethod
    def construct(builder):
        builder.build_part1()
        builder.build_part2()

if __name__ == '__main__':
    builderA = BuilderA()
    builderB = BuilderA()

    Director.construct(builderA)
    product = builderA.get_product()
    product.show()

    Director.construct(builderB)
    product = builderB.get_product()
    product.show()



