#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/11 11:10
# @Author : Sunx

"""
根据高程图DEM绘制相应的三维地形图
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np
from osgeo import gdal

def TerrainPlotByMatplot(fileName):
    # 注册gdal的功能，打开tif文件，读取其中的数据
    gdal.AllRegister()
    data = gdal.Open(fileName)
    adfGeoTransform = data.GetGeoTransform()
    band = data.GetRasterBand(1)

    # 获取tif的列数XSize和行数YSize
    XSize = data.RasterXSize
    YSize = data.RasterYSize

    # DEM数据的经纬度范围
    Xmin = adfGeoTransform[0]
    Ymin = adfGeoTransform[3]
    Xmax = adfGeoTransform[0] + XSize * adfGeoTransform[1] + YSize * adfGeoTransform[2]
    Ymax = adfGeoTransform[3] + XSize * adfGeoTransform[4] + YSize * adfGeoTransform[5]

    # 依据经纬度范围， 将x，y切片
    x = np.linspace(Xmin, Xmax, XSize)
    y = np.linspace(Ymin, Ymax, YSize)
    X, Y = np.meshgrid(x, y)
    Z = band.ReadAsArray()

    # 对高程图做切片
    region = np.s_[3000: 4000, 3000:4000]
    X, Y, Z = X[region], Y[region], Z[region]

    # 只对切片内区域绘制图像
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'), figsize=(12, 10))
    ls = LightSource(270, 20)  # 设置你可视化数据的色带
    rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)

    # plt.axis('off')
    plt.show()


def main():
    tifFileName = r"D:\GIS数据\台湾_30米.tif"
    TerrainPlotByMatplot(tifFileName)
    return 1


if __name__ == "__main__":
    main()