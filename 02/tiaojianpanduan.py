# -*- coding: utf-8 -*-
"""
@Project : 02
@File    : tiaojianpanduan.py
@Author  : JamyXe
@Time    : 2021-05-02 16:17:27
@Desc    : 
"""


# a = True
# b = True
# if a:
#     print("True")
# elif b:
#     print("False")
# else:
#     print("Others")
# print("End Process")

# score = 81
#
# if score >= 90:
#     print("成绩优秀")
# elif 90 > score >= 60:
#     print("成绩良好")
# else:
#     print("成绩不合格")

# # if嵌套
# a = True
# b = False
#
# if a:
#     if ~b:
#         print("True")
#     else:
#         print("False")
# else:
#     print("End of Process")

# import random
#
# x = random.randint(0, 1)  # 闭区间
# print(x)

# 石头剪刀布
import random
inp_tmp = input("请输入石头剪刀布：石头（0），剪刀（1），布（2）\n")
inp = int(inp_tmp)
sys_inp = random.randint(0, 2)

if inp > 2 or inp < 0:
    print("请输入正确的数字！")
else:
    if inp == 0 and sys_inp == 1:
        print("你赢了，你是%d，系统是%d" % (inp, sys_inp))
    elif inp == 1 and sys_inp == 2:
        print("你赢了，你是%d，系统是%d" % (inp, sys_inp))
    elif inp == 2 and sys_inp == 0:
        print("你赢了，你是%d，系统是%d" % (inp, sys_inp))
    else:
        print("再来一次，你是%d，系统是%d" % (inp, sys_inp))

