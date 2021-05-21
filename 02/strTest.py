# -*- coding: utf-8 -*-
"""
@Project : 02
@File    : strTest.py
@Author  : JamyXe
@Time    : 2021-05-20 16:39:05
@Desc    : 字符串处理
"""

# word = 'word'
# sentence = "a sentence"
# para = '''
# test
# new test
# '''
# print(para)

# 字符串截取 string indices
strs = 'ChenWeiTest'
print(strs[0:len(strs):3])  # 注意这里的标点是：
print(strs[len(strs)-1]) # 最后一个
print(strs[2:]) # 到最后一个截止
print(strs[:5])
# 字符串连接，
str2 = strs + 'add'
print(str2)

print(r"hello\tworld")  # r表示不解释转义字符