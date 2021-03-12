# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 15:18
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : state.py
# @Software: OA

class ComputerState:
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name  in self.allowed:
            self.__class__ = state
            print("allowed")
        else:
            print("not all")

    def __str__(self):
        return self.name


class Off(ComputerState):
    name =  "off"
    allowed = ['on']


class On(ComputerState):
    name =  "on"
    allowed = ['off', "suspend", "hibernate"]


class Suspend(ComputerState):
    name =  "suspend"
    allowed = ['on']

class Hibernate(ComputerState):
    name =  "hibernate"
    allowed = ['on']


class Computer:
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()

    comp.change(On)
    comp.change(Off)
