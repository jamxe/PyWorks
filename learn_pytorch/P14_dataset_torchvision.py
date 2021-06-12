# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : P14_dataset_torchvision.py
@Author  : JamyXe
@Time    : 2021-06-12 15:10:43
@Desc    : 
"""

import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])

train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=dataset_transform, download=True)

# print(train_set[0])
# print(train_set.classes)
#
# img, target = test_set[1]
# print(img)
# print(target)
# print(test_set.classes[target])
# img.show()

# print(train_set[0])

#  使用tensorboard
writer = SummaryWriter("p10_logs")
for i in range(1, 10):
    img, target = test_set[i]
    writer.add_image("test_set", img, i)

writer.close()
