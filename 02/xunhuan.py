# -*- coding: utf-8 -*-
"""
@Project : 02
@File    : xunhuan.py
@Author  : JamyXe
@Time    : 2021-05-02 16:46:53
@Desc    : 循环
"""

# rg = range(0, 10, 2)    # 以2为间隔
# sum_all = 0
# for i in rg:
#     sum_all += i
#
# print(sum_all)

# # 字符循环
# name = "ChenWen"
#
# for i in name:  # 注意这里没有range
#     print(i, end='\t')

# # 字符数组
# strArr = ['aa', 'bb', 'cc']
#
# for i in range(len(strArr)):
#     print(i, '\t', strArr[i])


# # while 用法
# i = 0
# while i < 5:
#     print("当前是第%d次循环" % (i+1))
#     print("i=%d" % (i+1))
#     i += 1

# # 1-100求和
# n = 100
# sums = 0
# cnt = 1
# while cnt < n:
#     sums += cnt
#     cnt += 1
#     print("1加到 %d 时的总和为 %d " % (cnt, sums))

# # while中的else用法
# cnt = 0
# while cnt < 5:
#     print(cnt, "小于5")
#     cnt += 1
# else:
#     print(cnt, "大于等于5")

# # 乘法表
# i = 1
# j = 1
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i:
#             print("%d*%d=%d" % (i, j, i*j), end='\t')
#         else:
#             continue
#     print('\t')
