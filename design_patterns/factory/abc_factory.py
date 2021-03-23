# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 11:46
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : abc_factory.py
# @Software: OA


import abc
from abc import abstractmethod, ABCMeta


class AbstractFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def prduct_car(self):
        pass

    @abc.abstractmethod
    def prduct_suv(self):
        pass


class BMW_M3(object):
    """宝马 M3
    """

    def __repr__(self):
        return "BMW: M3"


class BMW_SUV(object):
    """宝马 M3
    """

    def __repr__(self):
        return "BMW: BMW_SUV"


class BMFactory(AbstractFactory):
    def prduct_car(self):
        return BMW_M3()

    def prduct_suv(self):
        return BMW_SUV()


class MesemesFactory(AbstractFactory):
    def prduct_car(self):
        pass

    def prduct_suv(self):
        pass


if __name__ == '__main__':
    bm1 = BMFactory().prduct_car()
    bm2 = BMFactory().prduct_suv()
    print(bm1)
    print(bm2)


# 设计模式书上的

# ------------------------------------------------------------------------------------------------------------简单工厂模式


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("wan wang")


class Cat(Animal):
    def do_say(self):
        print("miao miao")


class ForesFactory:

    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


# if __name__ == '__main__':
#     ff = ForesFactory()
#     animal = input("Dog or Cat")
#     ff.make_sound(animal)

#-----------------------------------------------------------------------------------------------------------工厂方法
class section(metaclass=ABCMeta):
    @abstractmethod
    def descri(self):
        pass

class AblmSection(section):
    def descri(self):
        print("AblmSection")

class PublicSection(section):
    def descri(self):
        print("PublicSection")

class PatentSection(section):
    def descri(self):
        print("PatentSection")


class Profile(metaclass=ABCMeta):

    def __init__(self):
        self._setions = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def addSetion(self,object_type):
        self._setions.append(object_type)

    def getSection(self):
        return self._setions

class LinkProfile(Profile):

    def createProfile(self):
        self.addSetion(PatentSection)
        self.addSetion(AblmSection)
        self.addSetion(PublicSection)

class FacebookProfile(Profile):

    def createProfile(self):
        self.addSetion(PatentSection)


# if __name__ == '__main__':
#     profile_type = input("LinkProfile or FacebookProfile")
#     profile = eval(profile_type)()
#     print("create profile",type(profile).__name__)
#     print("has sections",profile.getSection())

#---------------------------------------------------------------------------------------------------------------抽象工厂

class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass

class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("prepare", type(self).__name__)

class ChickenePizza(NonVegPizza):
    def serve(self, VegPizza):
        print( type(self).__name__, "is server wihe chicken on ", type(VegPizza).__name__)


class MexicanVeggiePizza(VegPizza):
    def prepare(self):
        print("prepare", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is server wihe chicken on ", type(VegPizza).__name__)


class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonPizza(self):
        pass

class IndiaPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonPizza(self):
        return ChickenePizza()


class AmericaPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return MexicanVeggiePizza()

    def createNonPizza(self):
        return  HamPizza()


class PizzaSotre:

    def makePizzas(self):
        for factory in [IndiaPizzaFactory(),AmericaPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonPizza()
            self.vegPizzza = self.factory.createVegPizza()
            self.vegPizzza.prepare()
            self.NonVegPizza.serve(self.vegPizzza)

pizza = PizzaSotre()
pizza.makePizzas()