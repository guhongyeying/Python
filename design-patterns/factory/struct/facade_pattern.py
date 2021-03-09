# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 10:18
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : facade_pattern.py
# @Software: OA
# 面门模式


class Hotel:

    def book_hotel(self):
        print(self.__dict__)
        print("hotel book")


class Manger:

    def arrange(self):
        print(self.__dict__)
        hotel = Hotel()
        hotel.book_hotel()


class You:

    def ask_manger_envent(self):
        print(self.__dict__)
        em = Manger()
        em.arrange()


you = You()
you.ask_manger_envent()
