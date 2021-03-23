# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 17:27
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : common.py
# @Software: OA

from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def excute(self):
        pass


class ConcredateCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def excute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print("recv aciton")


class Invoker:
    def command(self, cmd: ConcredateCommand):
        self.cmd =  cmd

    def excute(self):
        self.cmd.excute()

# if __name__ == '__main__':
#     rev = Receiver()
#     cmd = ConcredateCommand(rev)
#     invoker = Invoker()
#     invoker.command(cmd)
#     invoker.excute()


class StockTrade:

    def buy_stock(self):
        print("buy -----")

    def sell_stock(self):
        print("buy -----")




class Order(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class SellStockTrade(Order):
    def __init__(self, stock: StockTrade):
        self.stock = stock

    def execute(self):
        self.stock.sell_stock()


class BuyStockTrade(Order):
    def __init__(self, stock: StockTrade):
        self.stock = stock

    def execute(self):
        self.stock.buy_stock()

class Agent:

    def __init__(self):
        self.__orderQuene = []

    def place_order(self, order: Order):
        self.__orderQuene.append(order)
        order.execute()


if __name__ == '__main__':

     stock = StockTrade()

     sellStock = SellStockTrade(stock)
     buyStock = BuyStockTrade(stock)

     agt = Agent()
     agt.place_order(sellStock)
     agt.place_order(buyStock)




