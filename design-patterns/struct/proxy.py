# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 11:30
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : proxy.py
# @Software: OA
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):

    def __init__(self):
        self.card = None
        self.acccount = None

    def __get_account(self):
        self.acccount = self.card
        return  self.acccount

    def __has_funds(self):
        print("Bank check has account", self.__get_account(),)
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print("bank paying the merchant")
            return True
        else:
            print("bank : soory, noyehnn founds")
            return False

class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card  = input("card Number")
        self.bank.set_card(card)
        return self.bank.do_pay()



class You:

    def  __init__(self):
        print("you lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("is Mine")
        else:
            print("you earn moer")
you = You()
you.make_payment()




