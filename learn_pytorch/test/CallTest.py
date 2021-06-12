# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : CallTest.py
@Author  : JamyXe
@Time    : 2021-06-09 14:05:30
@Desc    : __Call__ from transforms
"""

class Person:
    def __call__(self, name):
        print("__Call__ " + " Hello " + name)

    def hello(self, name):
        print("hello " + name)

person = Person()
person("张三")  # Ctrl + P 提示 需要什么参数
person.hello("lisi")
