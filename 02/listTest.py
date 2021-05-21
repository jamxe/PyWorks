# -*- coding: utf-8 -*-
"""
@Project : 02
@File    : listTest.py
@Author  : JamyXe
@Time    : 2021-05-20 16:52:29
@Desc    : 列表
"""

# python数组可以储存混合类型
demoList = [1, 'test']
for i in range(len(demoList)):
    print(type(demoList[i]))

nameInp = input("请输入：\n")

# 增
demoList.append(nameInp)
print("----------修改后------------------")
print(demoList)
list2 = demoList
list2.extend(demoList)  # 叠加数组
print(list2)

# 删除元素
del demoList[1]
demoList.pop()  # 弹出末尾最后一个元素
demoList.remove(1)  # 删除第一个，如果有相同元素的话只删除最前面找到的第一个

# 改
# 直接重新赋值

# 查 [in or not in]
findEle = input("输入要查找的元素：")
if findEle in demoList:
    print("in it")
else:
    print("not in")