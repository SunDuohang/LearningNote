#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/12 10:03
# @Author : Sunx

'''
对DEM或灰度栅格图的裁剪处理，
读取整个灰度栅格图，
然后在这个栅格图上，做正方形栅格切分
'''

import os.path
import numpy as np
from osgeo import gdal
from osgeo import gdal_array
import cv2

def RegularClip(img, WindowSize):
    num = 0
    XSize = img.shape[1]        # 列数
    YSize = img.shape[0]        # 行数
    WS = WindowSize
    # 对列切分次数
    for i in range(0, XSize, WS):
        # 对行划分次数
        for j in range(0, YSize, WS):
            # print(i * WS, i * WS + WS, j * WS, j * WS + WS)
            # cropped = img[j * WS: j * WS + WS, i * WS: i * WS + WS]
            cropped = img[j: j + WS, i: i + WS]
            num = num + 1
            target = 'tiff_crop' + '/cropped{i}_{j}.tif'.format(i=i, j=j)
            out = gdal_array.SaveArray(cropped, target, format="GTiff")

def DrawClipTif(fileName):

    data = gdal.Open(fileName)
    map = data.ReadAsArray()
    map_min = np.min(map)
    map_max = np.max(map)
    map = map / (map_max - map_min) * 255
    color_img = cv2.cvtColor(map.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    # color_img = color_img * 255

    (path, file) = os.path.split(fileName)
    (file, ext) = os.path.splitext(file)
    # cv2.namedWindow('img', 0)  # 0 or CV_WINDOW_AUTOSIZE(default）
    # cv2.imshow('img', color_img)
    # cv2.waitKey(0)  # 0 or positive value(ms)
    target = 'tif2png_Crop' + "/{name}.png".format(name=file)
    cv2.imwrite(target, color_img)


def main():
    fileName = r"D:\Project\PycharmProjects\OffRoadPathPlanning\2.5m-tongxing_Clip.tif"
    gdal.AllRegister()
    data = gdal.Open(fileName)
    adfGeoTransform = data.GetGeoTransform()
    band = data.GetRasterBand(1)
    map = data.ReadAsArray()
    RegularClip(map, 256)
    # filePath = r"D:\Project\PycharmProjects\OffRoadPathPlanning\tiff_crop"
    # for filename in os.listdir(filePath):
    #     DrawClipTif(os.path.join(filePath, filename))


if __name__ == "__main__":
    main()