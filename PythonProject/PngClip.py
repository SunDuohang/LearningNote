#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/12 14:47
# @Author : Sunx


from PIL import Image
import os

def ImageCrop(imageFilename, CropSize):
    with Image.open(imageFilename) as img:
        width, height = img.size
        for i in range(0, width, CropSize):
            for j in range(0, height, CropSize):
                box = (i, j, i + CropSize, j + CropSize)
                cropped_img = img.crop(box)
                outputname = "png_crop/" + f"{i}_{j}.png"
                cropped_img.save(outputname)
                print(f"{i}_{j}.png")

# def crop_image(image_path, output_path, crop_size, code):
#     with Image.open(image_path) as img:
#         width, height = img.size
#         for i in range(0, width, crop_size):
#             for j in range(0, height, crop_size):
#                 box = (i, j, i + crop_size, j + crop_size)
#                 cropped_img = img.crop(box)
#                 cropped_img.save(os.path.join(output_path, code + f"{i}_{j}.png"))
#                 print(code, f"{i}_{j}.png")

def main():
    fileName = r"D:\Project\PycharmProjects\OffRoadPathPlanning\2.5m-tongxing_RoadNetwork.png"
    ImageCrop(fileName, 256)


# image_path = "label"
# output_path = "LAB"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)
# crop_size = 256
#
# count = 0
#
# for filename in os.listdir(image_path):
#     if filename.endswith(".png"):
#         count += 1
#         code = f'{count:05d}'  # 编码规则
#         image_file = os.path.join(image_path, filename)
#         crop_image(image_file, output_path, crop_size, code)

if __name__ == "__main__":
    main()