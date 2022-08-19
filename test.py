import numpy as np


## 矩阵处理方法
### 对角矩阵
# a = [1,2,3]
# print(np.diag(a))
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
### 三角矩阵
# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
### 上三角函数
# print(np.triu(a, k=0))
# [[1 2 3]
#  [0 5 6]
#  [0 0 9]]
# print(np.triu(a, k=1))
# [[0 2 3]
#  [0 0 6]
#  [0 0 0]]
# print(np.triu(a, k=-1))
# [[1 2 3]
#  [4 5 6]
#  [0 8 9]]
# a = np.array(a)
# print(np.triu_indices(3, k=0))  #需要已知矩阵维度，返回对应的下标
# print(a[np.triu_indices(3, k=0)]) # 获取对应下表的数据
# a[np.triu_indices(3, k=0)]=-1 # 修改对应下标的数据
# print(a)
# (array([0, 0, 0, 1, 1, 2]), array([0, 1, 2, 1, 2, 2])) # (0,0) (0,1) (0,2) (1,1) (1,2) (2,2)
# [[1 2 3 5 6 9]]
# [[-1 -1 -1]
#  [ 4 -1 -1]
#  [ 7  8 -1]]
# 下三角函数
# np.tril(a, k=0) 同理
# np.tril_indices(3, k=0)

# s:起点位置
# i:目的地
# v:经过的清单点
# p: 路径
def dis(s, i, v):
    min_res = np.inf
    min_p = []
    if (len(v) == 0):  # 当中间点为空 s->i的距离
        return (distance_dict[s, i], [s, i])
    else:
        res = []
        for city_id in v:
            mid_res = dis(s, city_id, list(filter(lambda x: x != city_id, v)))
            mid_res[1].append(i)
            res.append((mid_res[0] + distance_dict[i,city_id], mid_res[1]))

        for item in res:
            if (item[0] < min_res):
                min_res = item[0]
                min_p = item[1]
        return (min_res, min_p)


if __name__ == '__main__':
    # 创建对称矩阵
    distance_dict = [[np.inf, 3, np.inf, 8, 9],
                     [3, np.inf, 3, 10, 5],
                     [np.inf, 3, np.inf, 4, 3],
                     [8, 10, 4, np.inf, 20],
                     [9, 5, 3, 20, np.inf]]
    distance_dict = np.array(distance_dict)
    # distance_dict = np.triu(distance_dict) + np.triu(distance_dict).T - np.diag(distance_dict.diagonal()) # 上半角+上半角转置-对角元素
    city_index_list = [0, 1, 2, 3, 4]  # 城市ID下标
    res = [dis(0, 0, list(filter(lambda x: x != 0, city_index_list))),
           dis(1, 1, list(filter(lambda x: x != 1, city_index_list))),
           dis(2, 2, list(filter(lambda x: x != 2, city_index_list))),
           dis(3, 3, list(filter(lambda x: x != 3, city_index_list))),
           dis(4, 4, list(filter(lambda x: x != 4, city_index_list)))]
    min_dis = min(res)
    print(min_dis)

## 说明
## 假设从 0 开始
# 0 0 [1,2,3,4] 从0出发经过[1,2,3,4]回到0的最短距离
# 转换为 0 1 [2,3,4] 从0出发经过[2,3,4]回到1的最短距离+ c[0,1]
#       0 2 [1,3,4] + c[0,2]
#       0 3 [1,2,3] + c[0,3]
# 同理 0 1 [2,3,4] 转换为
#     0 2 [3,4] + c[1,2]  (0 2 [3,4] 从0开始经过[3,4]回到2的最短距离 + c[1,2]到1点 + c[0,1]到0点 = 从0出发经过[1,2,3,4]回到0的最短距离)
#     0 3 [2,4] + c[1,3]
#     0 4 [2,3] + c[1,4]
