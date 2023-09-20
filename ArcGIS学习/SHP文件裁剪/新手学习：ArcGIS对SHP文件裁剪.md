# 新手学习：ArcGIS对SHP文件裁剪

**新手学习**
记录每个步骤，因为有很多控件可能刚开始还不熟悉，根本不知道在哪里，所以写的比较详细。

### 1.添加要裁剪的shp文件

![添加数据](./IMG/添加数据.png)

### 2.查看shp文件的地理坐标系

双击shp文件，就可以查看shp文件的地理坐标系
![图层属性](./IMG/图层属性.png)

### 3. 新建shapefile面要素

首先需要连接到自己的数据空间。目录在软件的右侧边栏。
![连接文件夹](./IMG/文件夹连接.png)

右击想要裁剪的文件夹，在该文件夹中新建一个shapefile文件。
![新建shp面要素](./IMG/新建shp面数据.png)

选择新建shapefile文件的地理坐标系
![选择地理坐标系](./IMG/新建shp面数据文件.png)

### 4. 编辑shapefile文件

编辑新建的shapefile面要素

![编辑面要素](./IMG/ArcGIS裁剪.png)

确定好要裁剪区域后，进行保存
![保存编辑](./IMG/保存编辑内容.png)

### 5. 进行裁剪

打开ArcToolBox。
![打开ArcToolBox](./IMG/ArcToolBox.png)

进行裁剪
![裁剪](./IMG/裁剪.png)