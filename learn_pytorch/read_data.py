# -*- coding: utf-8 -*-
"""
@Project : learn_pytorch
@File    : read_data.py
@Author  : JamyXe
@Time    : 2021-06-03 19:57:23
@Desc    : 
"""
import os.path

from torch.utils.data import Dataset
from PIL import Image


class MyData(Dataset):  # 创建一个Mydata类继承Dataset
    def __init__(self, root_dir, label_dir):  # label_dir 上一级文件夹的名称
        self.root_dir = root_dir  # 指定类中的全局变量,self相当于this指针
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, ind):
        img_name = self.img_path[ind]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants_image"
bees_label_dir = "bees_image"
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)

train_dataset = ants_dataset + bees_dataset  # 数据集的拼接，按顺序
