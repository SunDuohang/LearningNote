#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/7 20:52
# @Author : Sunx

import GeoTransformTool as GTT
from osgeo import gdal
import pandas as pd
import numpy as np
import cv2

class Node(object):
    def __init__(self, Pos):
        """
        :param Pos 投影坐标（x，y）
        :param father 父节点
        :param gValue 评价函数g(n)
        :param fValue 评价函数值f=g+h
        """
        self.pos = Pos
        self.range = 0  #  range 表示一个窗口大小
        self.father = None
        self.gValue = 0.0
        self.fValue = 0.0

def RemoveInvalidNode(NodeXY, img):
    newNodeXY = []
    for Point in NodeXY:
        if Point[1] < 0 or Point[1] > (7889 - 1):
            continue
        if Point[0] < 0 or Point[0] > (10114 - 1):
            continue
        if img[Point[1], Point[0]] == 0:
            continue
        newNodeXY.append(Point)
    return newNodeXY


def DrawPoint(PointSet, img):
    # for Point in PointSet:
    #     for i in range(-15, 15):
    #         for j in range (-15, 15):
    #             img[Point[1] + i, Point[0] + j] = (0, 69, 255)
        # img[Point[1], Point[0]] = (0, 69, 255)
        # print(Point[1], Point[0])
    for Point in PointSet:
        if Point[1] < 0 or Point[1] > (7889 - 1):
            continue
        if Point[0] < 0 or Point[0] > (10114 - 1):
            continue
        for i in range (-3, 3):
            for j in range (-3, 3):
                img[Point[1], Point[0]] = (0, 69, 255)


def Draw(nodeXYList, img):
    """
    :brief 将路网节点绘制在图像上
    :param nodeXYList 坐标[列号， 行号]
    :param img 图像
    """
    for i in range(len(nodeXYList)):
        if nodeXYList[i][1] < 0 or nodeXYList[i][1] > (7889-1):
            continue
        if nodeXYList[i][0] < 0 or nodeXYList[i][0] > (10114-1):
            continue
        for j in range(-15, 15):
            for k in range (-15, 15):
                img[nodeXYList[i][1]+j, nodeXYList[i][0]+k] = (0, 69, 255)
        print(nodeXYList[i][1], nodeXYList[i][0])
        # img[nodeXYList[i][1], nodeXYList[i][0]] = (0, 69, 255)

def ExtractNode(tifFilename,  NodeFile):
    data = gdal.Open(tifFilename)
    data_GeoTransform = GTT.GetGeoTrans(data)
    print(data_GeoTransform)
    # 读取路网节点经纬度信息
    node_Data = pd.read_excel(NodeFile)
    node_dict = node_Data.to_dict()
    node_LonlatList = []
    # 将字典中的经纬度信息进行提取
    for i in range(len(node_dict['Lon'])):
        value1 = node_dict['Lon'][i]
        value2 = node_dict['Lat'][i]
        # node_LonlatList[[value1, value2]]
        node_LonlatList.append([value1, value2])
    node_XY = []
    for i in range(len(node_LonlatList)):
        node_XY.append(GTT.geo2projection(node_LonlatList[i][0], node_LonlatList[i][1], data_GeoTransform))
    return node_XY

def DrawRoadNetworkNode(tifFilename, NodeFile, img=None):
    data = gdal.Open(tifFilename)
    data_GeoTransform = GTT.GetGeoTrans(data)
    print(data_GeoTransform)
    # 读取路网节点经纬度信息
    node_Data = pd.read_excel(NodeFile)
    node_dict = node_Data.to_dict()
    node_LonlatList = []
    # 将字典中的经纬度信息进行提取
    for i in range(len(node_dict['Lon'])):
        value1 = node_dict['Lon'][i]
        value2 = node_dict['Lat'][i]
        # node_LonlatList[[value1, value2]]
        node_LonlatList.append([value1, value2])
    node_XY = []
    for i in range(len(node_LonlatList)):
        node_XY.append(GTT.geo2projection(node_LonlatList[i][0], node_LonlatList[i][1], data_GeoTransform))
    RemoveInvalidNode(node_XY, img)
    DrawPoint(node_XY, img)


def test():
    tifFileName = "2.5m-tongxing_Clip.tif"
    NodeFilename = "Taiwan_Lonlat.xlsx"
    data = gdal.Open(tifFileName)
    data_GeoTransform = GTT.GetGeoTrans(data)
    startPoint = [121.3190459, 25.1133656000001]
    #startPoint = [121.3795452, 25.1126075]
    print(data.RasterXSize)
    print(data.RasterYSize)
    print(GTT.geo2projection(startPoint[0], startPoint[1], data_GeoTransform))
    print(GTT.Projection2Geo(2894, 2439, data_GeoTransform))
    # nodeXY = []
    # nodeXY.append(GTT.geo2projection(startPoint[0], startPoint[1], data_GeoTransform))

    # nodeXY.append([5380, 2438])

    map = data.ReadAsArray()
    map_min = np.min(map)
    map_max = np.max(map)
    map = map / (map_max - map_min) * 255
    color_img = cv2.cvtColor(map.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    color_img = color_img * 255
    nodeXY = ExtractNode(tifFileName, NodeFilename)
    nodeXY = RemoveInvalidNode(nodeXY, map)
    DrawPoint(nodeXY, color_img)

    cv2.namedWindow('img', 0)  # 0 or CV_WINDOW_AUTOSIZE(default）
    cv2.imshow('img', color_img)
    cv2.waitKey(0)  # 0 or positive value(ms)
    cv2.imwrite("newresult.png", color_img)



def main():
    tifFileName = "2.5m-tongxing_Clip.tif"
    NodeFilename = "Taiwan_Lonlat.xlsx"
    data = gdal.Open(tifFileName)
    map = data.ReadAsArray()
    map_min = np.min(map)
    map_max = np.max(map)
    map = map / (map_max - map_min) * 255
    color_img = cv2.cvtColor(map.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    color_img = color_img * 255
    DrawRoadNetworkNode(tifFileName, NodeFilename, color_img)

    # 显示图片
    cv2.namedWindow('img', 0)  # 0 or CV_WINDOW_AUTOSIZE(default）
    cv2.imshow('img', color_img)
    cv2.waitKey(0)  # 0 or positive value(ms)
    cv2.imwrite("result.png", color_img)


if __name__ == "__main__":
    test()
    # main()
