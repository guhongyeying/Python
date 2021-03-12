# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 10:46
# @Author  : WR
# @Email   : wwwwangren@163.com
# @File    : Observer.py
# @Software: OA
from abc import ABCMeta, abstractmethod


class NewPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x) for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()


    def add_New(self, news):
        self.__latestNews = news


    def get_new(self):
        return "Got News:", self.__latestNews


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):

    def __init__(self, publicsher):
        self.publicsher = publicsher
        self.publicsher.attach(self)

    def update(self):
        print(type(self).__name__, self.publicsher.get_new())


class EmailSubscriber(Subscriber):

    def __init__(self, publicsher):
        self.publicsher = publicsher
        self.publicsher.attach(self)

    def update(self):
        print(type(self).__name__, self.publicsher.get_new())


if __name__ == '__main__':
    newPublisher = NewPublisher()

    for subscriber in [SMSSubscriber, EmailSubscriber]:
        subscriber(newPublisher)
    print("=",newPublisher.subscribers())
    newPublisher.add_New("hellll world")
    newPublisher.notify_subscribers()

    print()





