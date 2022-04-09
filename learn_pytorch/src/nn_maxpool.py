# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : nn_maxpool.py
@Author  : JamyXe
@Time    : 2021-06-17 14:55:06
@Desc    : P19 神经网络 最大池化操作
"""

import torch
from torch import nn
from torch.nn import MaxPool2d

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]], dtype=float)

input = torch.reshape(input, (-1, 1, 5, 5))
print(input.shape)


class mpNN(nn.Module):
    def __init__(self):
        super(mpNN, self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output


mpNNtest = mpNN()
output = mpNNtest(input)
print(output)
