# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : P9_transforms.py
@Author  : JamyXe
@Time    : 2021-06-08 18:43:48
@Desc    : 
"""
from torch import Tensor
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from PIL import Image


# python的用法-) tensor据类型
# 通过 transforms. Totensor去看两个问题
# 1、 transforms英如何使用( python)
# 2、为什么我们需要 Tensor据类型

img_path = r"dataset/train/ants_image/0013035.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

#  1. transforms如何使用
tensor_trans = transforms.ToTensor()
tensor_img: Tensor = tensor_trans(img)

writer.add_image("tensor_img", tensor_img)

writer.close()