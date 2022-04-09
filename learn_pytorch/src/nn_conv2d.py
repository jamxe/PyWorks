# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : nn_conv2d.py
@Author  : JamyXe
@Time    : 2021-06-14 16:41:30
@Desc    : p18 神经网络 卷积层
"""

import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("../dataset", train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)

dataloader = DataLoader(dataset, batch_size=64)


class NewNN(nn.Module):

    def __init__(self):
        super(NewNN, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x


testnn = NewNN()
print(testnn)

writer = SummaryWriter("../conv2d_logs")
step = 0
for data in dataloader:
    imgs, targets = data
    output = testnn(imgs)
    # torch.Size([64, 3, 32,32])
    writer.add_images("input", imgs, step, dataformats='NCHW')
    # torch.Size([64, 3, 30,30])
    output = torch.reshape(output, (-1, 3, 30, 30))  # 不知道是多少的时候写成-1，会自动计算
    writer.add_images("output", output, step, dataformats='NCHW')
    step += 1
    # print(output.shape)
    # print(step)

writer.close()