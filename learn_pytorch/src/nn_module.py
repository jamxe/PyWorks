# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : nn_module.py
@Author  : JamyXe
@Time    : 2021-06-13 18:29:25
@Desc    : 
"""

# import torch.nn as nn
# import torch.nn.functional as F
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         self.conv1 = nn.Conv2d(1, 20, 5)
#         self.conv2 = nn.Conv2d(20, 20, 5)
#
#     def forward(self, x):
#         x = F.relu(self.conv1(x))
#         return F.relu(self.conv2(x))
import torch
from torch import nn


class littleNN(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output

lnn = littleNN()
x = torch.tensor(1.0)
output = lnn(x)
print(output)