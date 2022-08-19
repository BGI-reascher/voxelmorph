#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :crop_stitch_img.py
# @Time      :2022/8/19 9:10
# @Author    :kuisu_dgut@163.com
import os

import tifffile
from sahi import slicing
import cv2
from common import tiff_read, tiff_write, ij_16_to_8

def get_dir_fils(path):
    # 获取文件夹下的所有文件
    file_names = os.listdir(path)
    with open("file_names.txt","a") as f:
        for file in file_names:
            if os.path.exists(os.path.join(path,file)):
                if os.path.exists(os.path.join(path.replace("moved","fixed"),file)):
                    f.write(str(file)+"\n")


def crop_img(image):
    # 将大图裁剪为小图并保存
    slicing.slice_image(image,
                        output_file_name= "register",
                        output_dir = "./fixed",
                        slice_height= 512,
                        slice_width= 512,
                        overlap_height_ratio=0.2,
                        overlap_width_ratio=0.2,
                        auto_slice_resolution = True,
                        min_area_ratio = 0.1,
                        verbose = True,)
    print("save successed")





if __name__ == "__main__":
    path = r"E:\sukui\IF_image\SS200000556BL_B2_NEUN_IF\3_register\SS200000556BL_B2_IF_stitched_transform.tif"
    dir_path = r"E:\sukui\datasets\register\moved"
    get_dir_fils(dir_path)
    # path = r"image.jpg"
    # image = tiff_read(path)
    # image = ij_16_to_8(image)
    # crop_img(image)

    pass
