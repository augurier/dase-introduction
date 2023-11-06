import numpy as np
import scipy.sparse as sp
import torch
 
import pandas as pd
import numpy as np
 
# 导入数据：分隔符为空格
raw_data = pd.read_csv('./cora/cora.content', sep='\t', header=None)
num = raw_data.shape[0]  # 样本点数2708
 
# 将论文的编号转[0,2707]
a = list(raw_data.index)
b = list(raw_data[0])
c = zip(b, a)
map = dict(c)
 
# 将词向量提取为特征,第二行到倒数第二行
features = raw_data.iloc[:, 1:-1]
# 检查特征：共1433个特征，2708个样本点
print(features.shape)
 
labels = pd.get_dummies(raw_data[1434])
print(labels.head(3))
 
raw_data_cites = pd.read_csv('./cora/cora.cites', sep='\t', header=None)
 
# 创建一个规模和邻接矩阵一样大小的矩阵
matrix = np.zeros((num, num))
# 创建邻接矩阵
for i, j in zip(raw_data_cites[0], raw_data_cites[1]):
    x = map[i]
    y = map[j]  # 替换论文编号为[0,2707]
    matrix[x][y] = matrix[y][x] = 1  # 有引用关系的样本点之间取1
# 查看邻接矩阵的元素和（按每列汇总）
print(sum(matrix))

import numpy as np
import scipy.sparse as sp
import torch
 
 
def encode_onehot(labels):
    classes = set(labels)
    classes_dict = {c: np.identity(len(classes))[i, :] for i, c in enumerate(classes)}
    labels_onehot = np.array(list(map(classes_dict.get, labels)), dtype=np.int32)
    return labels_onehot
 
 
def normalize(mx):
    """Row-normalize sparse matrix"""
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    mx = r_mat_inv.dot(mx)
    return mx
 
 
def normalize_adj(adjacency):
    degree = np.array(adjacency.sum(1))
    d_hat = sp.diags(np.power(degree, -0.5).flatten())
    adj_norm = d_hat.dot(adjacency).dot(d_hat).tocoo()
    return adj_norm
 
 
def normalize_features(features):
    return features / features.sum(1)
 
 
 
def load_data(path="./cora/", dataset="cora"):
    """Load citation network dataset (cora only for now)"""
    print('Loading {} dataset...'.format(dataset))
 
    idx_features_labels = np.genfromtxt("{}{}.content".format(path, dataset),
                                        dtype=np.dtype(str))
    features = sp.csr_matrix(idx_features_labels[:, 1:-1], dtype=np.float32)
    labels = encode_onehot(idx_features_labels[:,-1])
 
    # build graph
    idx = np.array(idx_features_labels[:, 0], dtype=np.int32)
    idx_map = {j: i for i, j in enumerate(idx)}
    edges_unordered = np.genfromtxt("{}{}.cites".format(path, dataset),
                                    dtype=np.int32)
    edges = np.array(list(map(idx_map.get, edges_unordered.flatten())),
                     dtype=np.int32).reshape(edges_unordered.shape)
    adj = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:, 0], edges[:, 1])),
                        shape=(labels.shape[0], labels.shape[0]),
                        dtype=np.float32)
 
    # build symmetric adjacency matrix
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)
 
    features = normalize_features(features)
    adj = normalize_adj(adj + sp.eye(adj.shape[0]))
 
    idx_train = range(140)
    idx_val = range(200, 500)
    idx_test = range(500, 1500)
 
    features = torch.FloatTensor(np.array(features))
    labels = torch.LongTensor(np.where(labels)[1])
    adj = torch.FloatTensor(np.array(adj.todense()))
 
    idx_train = torch.LongTensor(idx_train)
    idx_val = torch.LongTensor(idx_val)
    idx_test = torch.LongTensor(idx_test)
 
    return adj, features, labels, idx_train, idx_val, idx_test
 
# Load data
adj, features, labels, idx_train, idx_val, idx_test = load_data()