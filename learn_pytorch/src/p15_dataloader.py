# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : p15_dataloader.py
@Author  : JamyXe
@Time    : 2021-06-12 16:18:26
@Desc    : 
"""

import torchvision

from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor())
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False)   # 注意此处L
# 需要大写，不如无法识别, drop_last 意思是最后一个数据集数目不足的时候是否舍弃
# batch_size 每次取出四个数据然后打包；shuffle ： 一般设置为True ， 第二次取出数据的时候相同step依然是同样的数据集顺序

# 测试数据集中样本的第一张图片
img, target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("../dataloader_logs")

step = 0
for data in test_loader:
    imgs, targets = data
    # print(imgs.shape)
    # print(targets)
    writer.add_images("imgs", imgs, step)  # 此处要采用复数形式；add_images
    step = step + 1

writer.close()
