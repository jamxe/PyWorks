# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : test_tensorboard.py
@Author  : JamyXe
@Time    : 2021-06-04 20:09:29
@Desc    : 
"""

from torch.utils.tensorboard import SummaryWriter  # 查看一下help，按住Ctrl
import numpy as np
from PIL import Image

writer = SummaryWriter("../logs")
img_path = r"../dataset/train/ants_image/0013035.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)


writer.add_image("test", img_array, 1, dataformats="HWC")
# y - x
for i in range(1, 100):
    writer.add_scalar("y = 2x", 2 * i, i)

writer.close()
# add_scalar(self, tag标题, scalar_value x轴, global_step=None, walltime=None):
