# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : nn_maxpool.py
@Author  : JamyXe
@Time    : 2021-06-17 14:55:06
@Desc    : P19 神经网络 最大池化操作 图片
"""

import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../dataset", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)

dataloader = DataLoader(dataset, batch_size=64)

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
# print(output)

writer = SummaryWriter("../maxpool_logs")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input_maxpool", imgs, step)
    output_imgs = mpNNtest(imgs)
    step += 1
    # output_imgs = torch.reshape(output_imgs, (-1, 1, 10, 10)) # 根据图像的大小进行设定
    # 池化之后不会出现多个channel，因此不需要使用reshape
    writer.add_images("output", output_imgs, step, dataformats='NCHW')

writer.close()