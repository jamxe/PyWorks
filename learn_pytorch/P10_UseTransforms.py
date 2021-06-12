'''
Version      : 1.0
Autor        : jamyxe
Created on   : 2021-06-12 18:04:51
Last Modified: 2021-06-12 18:05:40
FilePath     : /undefinedd:/GitHub/PyWorks/learn_pytorch/P10_UseTransforms.py
Description  : 
'''
# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : P10_UseTransforms.py
@Author  : JamyXe
@Time    : 2021-06-08 23:15:23
@Desc    : 
"""

from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("logs")
img = Image.open(r"dataset/train/bees_image/16838648_415acd9e3f.jpg")
print(img)

# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("img_tensor", img_tensor, 0)

# Normalize
print("img_tensor[0][0][0]: ")
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([6, 3, 2], [1, 4, 7])  # 自行设置
img_norm = trans_norm(img_tensor)
print("Normalized: img_norm[0][0][0]: ")
print(img_norm[0][0][0])
writer.add_image("img_norm", img_norm, 1)

# Resize
print(img.size)
trans_resize = transforms.Resize((256, 256))
img_resize = trans_resize(img)  # PIL img -> resize
img_resize = trans_totensor(img_resize)  # img_resize PIL  -> tensor img
writer.add_image("Resized", img_resize, 0)
print(img_resize.size)

# 第二种方式：批量resize Compose -> Resize -> tensor img
trans_resize_2 = transforms.Resize(512)
# PIL -> PIL -> tensor
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])  # 现在Resize可以输入tensor类型了
img_resize_2 = trans_compose(img)
writer.add_image("Resize", img_resize_2, 1)

# Random Crop

trans_rand = transforms.RandomCrop(256)
trans_compose_2 = transforms.Compose([trans_rand, trans_totensor])
for i in range(1, 10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomCrop", img_crop, i)


writer.close()
