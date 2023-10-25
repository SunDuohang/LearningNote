#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/20 16:27
# @Author : Sunx
# @Last Modified by: Sunx
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import math

class Node(object):
    '''
    树节点
    '''
    def __init__(self):
        self.father = None      # 父节点
        self.left = None        # 左子树节点
        self.right = None       # 右子树节点
        self.feature = None     # 分割元素
        self.split = None       # 现在节点值

    def __str__(self):
        return "feature: %s, split: %s" % (str(self.feature), str(self.split))

    @property
    def brother(self):
        '''
        获取兄弟节点
        '''
        if self.father == None:
            ret = None
        else:
            if self.father.left is self:
                ret = self.father.right
            else:
                ret = self.father.left
        return ret


class KDTree(object):
    def __init__(self, data=None, method="variance"):
        self._k = None
        self._root = Node()
        self._data = data
        self._method = method
        if data is not None:
            self._k = data.shape[1]
            self.build_tree(data, method=self._method)

    def __str__(self):
        ret = []
        i = 0
        que = [(self._root, -1)]     # {list}，一个元组队列
        while que:
            cur_node, idx_father = que.pop(0)
            ret.append("%d -> %d, %s" %(idx_father, i, str(cur_node)))
            if cur_node.left:
                que.append((cur_node.left, i))
            if cur_node.right:
                que.append((cur_node.right, i))
            i += 1

        return "\n".join(ret)

    def _get_median_idx(self, X, idxs, feature):
        """
        计算中位数

        Params:
            X {list} -- 2维列表
            idxs {list} -- 1维列表
            feature {int} -- Feature number
            sorted_idx_2d {list} -- 2d list with int
        Returns:

        """
        n = len(idxs)
        k = n // 2
        col = map(lambda i: (i, X[i][feature]), idxs)
        # 将数据按feature维度的大小进行排序
        sorted_idxs = map(lambda x: x[0], sorted(col, key=lambda x: x[1]))
        median_idx = list(sorted_idxs)[k]

        return median_idx

    def _get_variance(self, X, idxs, feature):
        """计算特征数据的方差, 将数据进行标准化，未标准化的数据会方差有较大的波动，减均值标准化（最大最小标准化也可以考虑）

        Params:
            X 2维或更高 数据 \n
            idxs 坐标列表 \n
        Returns:
            返回feature对应的列的方差
        """
        min_feature = min(X[:, feature])
        max_feature = max(X[:, feature])

        norm_X = (X - min_feature) / (max_feature - min_feature)
        # scaler = StandardScaler()       # 归一化
        # norm_X = scaler.fit_transform(X)
        n = len(idxs)
        col_sum = col_sum_sqr = 0
        for idx in idxs:
            xi = norm_X[idx][feature]
            col_sum += xi
            col_sum_sqr += xi ** 2

        return col_sum_sqr / n - (col_sum / n) ** 2

    def _choose_feature(self, X, idxs, method="variance"):
        """
        选择一个进行划分的维度

        Params:
            X  2维及以上数据数据 \n
            idxs \n
            mrthod 默认为方差最大法"variance"，可选"pca" \n
        Returns:
            feature
        """
        if method == "variance":
            m = len(X[0])
            variances = map(lambda j: (
                j, self._get_variance(X, idxs, j)), range(m))
            # print(list(variances))
            variances = list(variances)
        # print(max(variances, key=lambda x: x[1])[0])
            return max(variances, key=lambda x: x[1])[0]        # 返回方差最大的feature字段
        elif method == "pca":
            m = len(X[0])
            c_r = self._get_pca(idxs=idxs, X=X)       # contribution_ratio
            return c_r.index(max(c_r))


    def _get_pca(self, idxs, X=None):
        """计算主成分

        Params:

        Returns:

        """
        if X is None:
            X = self._data
        n_samples, n_features = X.shape
        # scaler = StandardScaler()       # 归一化
        # norm_X = scaler.fit_transform(X)

        data = []
        # reconstruct data
        for idx in idxs:
            data.append(X[idx, :])
        data = np.array(data)
        mean = np.array([np.mean(data[:, i]) for i in range(n_features)])
        norm_data = data - mean
        scatter_matrix = np.dot(np.transpose(norm_data), norm_data)
        eig_val, eig_vec = np.linalg.eig(scatter_matrix)
        eig_pair = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(n_features)]
        eig_pair.sort(reverse=True)

        contribution_rate = [(eig_val[i] / sum(eig_val)) for i in range(n_features)]
        return contribution_rate


    def _split_feature(self, X, idxs, feature, median_idx):
        """
        进行树划分
        """
        idxs_split = [[], []]       # 第一个行为左子树，第二行为右子树
        split_val = X[median_idx][feature]
        for idx in idxs:
            if idx == median_idx:
                continue
            # 划分数据
            xi = X[idx][feature]
            if xi < split_val:
                idxs_split[0].append(idx)
            else:
                idxs_split[1].append(idx)

        return idxs_split

    def build_tree(self, X, method="variance"):
        """
        构建k-D树
        """
        cur_node = self._root
        idxs = range(len(X))
        que = [(cur_node, idxs)]
        while que:
            cur_node, idxs = que.pop(0)
            n = len(idxs)
            if n == 1:
                cur_node.split = (X[idxs[0]])
                continue
            # 划分子树
            feature = self._choose_feature(X, idxs, method=method)
            median_idx = self._get_median_idx(X, idxs, feature)
            idxs_left, idxs_right = self._split_feature(X, idxs, feature, median_idx)

            cur_node.feature = feature
            cur_node.split = (X[median_idx])
            if idxs_left != []:
                cur_node.left = Node()
                cur_node.left.father = cur_node
                que.append((cur_node.left, idxs_left))
            if idxs_right != []:
                cur_node.right = Node()
                cur_node.right.father = cur_node
                que.append((cur_node.right, idxs_right))

    def _search(self, Xi, cur_node=None):
        """对树进行搜索

        Params:
            Xi 待搜索数据 \n
            cur_node 从该节点开始搜索
        Returns:
            cur_node 返回一个节点
        """
        if cur_node is None:
            cur_node = self._root
        while cur_node.left or cur_node.right:
            if not cur_node.left:
                cur_node = cur_node.right
            elif not cur_node.right:
                cur_node = cur_node.left
            else:
                if Xi[cur_node.feature] < cur_node.split[0][cur_node.feature]:
                    cur_node = cur_node.left
                else:
                    cur_node = cur_node.right

        return cur_node

    def _grt_eu_dist(self, Xi, cur_node=None):
        """计算数据Xi到节点cur_node的欧拉距离

        Params:

        Returns:

        """
        if cur_node is None:
            cur_node = self._root
        y = cur_node.split[0]

        eu_dist = math.sqrt((Xi[0] - y[0]) ** 2 + (Xi[1] - y[1]) ** 2)

        return eu_dist

    def _get_hyper_dist(self, Xi, cur_node=None):
        """计算Xi与节点超平面的欧拉距离

        Params:
            Xi 2维数据 待计算数据 \n
            cur_node 节点  初始化=None \n
        Returns:
            float型数据 是Xi与超平面距离值
        """
        if cur_node is None:
            cur_node = self._root
        j = cur_node.feature
        y = cur_node.split[0]
        return abs(Xi[j] - y[j])

    def neareast_neighbor_search(self, Xi):
        """ 计算Xi的最近邻居

        Params:
            Xi 2维数据
        Returns:

        """
        # dis_best = float("inf")
        node_best = self._search(Xi, self._root)
        dis_best = self._grt_eu_dist(Xi, node_best)
        que = [(self._root, node_best)]
        while que:
            node_root, cur_node = que.pop(0)
            dist = self._grt_eu_dist(Xi, self._root)

            if dist < dis_best:
                dis_best, node_best = dist, node_root
            while cur_node is not node_root:
                dist = self._grt_eu_dist(Xi, cur_node)
                if dist < dis_best:
                    dist_best, node_best = dist, cur_node

                if cur_node.brother and dist_best > \
                    self._get_hyper_plane_dist(Xi, cur_node.father):
                    _nd_best = self._search(Xi, cur_node.brother)
                    que.append((cur_node.brother, _nd_best))
                    # Back track.
                cur_node = cur_node.father

        return node_best

def main():
    datafile = r"D:\Project\PycharmProjects\OffRoadPathPlanning\ConstructRoadNetwork\1792_4608_ClusterAnalysisResult.xlsx"
    data = pd.read_excel(datafile)
    data = data.to_numpy()
    kt = KDTree(data, method="variance")
    ret = kt.__str__()
    print(ret)


if __name__ == "__main__":
    main()