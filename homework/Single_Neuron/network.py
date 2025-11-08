# 读取文件
import numpy as np
import os
import matplotlib.pyplot as plt
def load_data():
    datafile = 'AbaloneAgePrediction.txt'
    data = np.genfromtxt(datafile, delimiter=',',dtype=str)
    # 将性别（M：雄性，F：雌性，I：未成年）映射成数字 0 和 1
    sex_map = {'M': 1, 'F': 1, 'I': 0}
    for k, v in sex_map.items():
        data[data[:, 0] == k, 0] = v
    data = data.astype(np.float64)
    # 转换为nparray
    feature_names =['性别','长度','直径','高度',
                    '总重量','皮重','内脏重量','克重','年龄']
    feature_num = len(feature_names)
    ratio = 0.8
    # 将训练数据集和测试数据集按照8:2的比例分开
    offset = int(data.shape[0] * ratio)
    training_data = data[:offset]
    maximums = training_data.max(axis=0)
    minimums = training_data.min(axis=0)
    avgs = training_data.sum(axis=0) / training_data.shape[0]
    # 数据归一化
    for i in range(feature_num):
        data[:, i] = (data[:, i] - avgs[i]) / (maximums[i] - minimums[i])
    # 分割训练集、测试集
    training_data = data[:offset]
    test_data = data[offset:]
    return training_data, test_data
# 定义一个单神经元类
class Network(object):
    # 定义初始化函数
    def __init__(self,num_of_weights):
        np.random.seed(0)
        self.w = np.random.randn(num_of_weights, 1)
        self.b = 0.
        # 定义向前运算函数
    def forward(self, x):
        z = np.dot(x, self.w)+ self.b
        return z
    # 定义loss函数
    def loss(self,z,y):
        error = z - y
        cost = error *error
        cost = np.mean(cost)
        return cost
    # 定义梯度计算函数
    def gradient(self, x, y):
        z = self.forward(x)
        gradient_w = (z - y)*x
        gradient_w = np.mean(gradient_w, axis=0)
        gradient_w = gradient_w[:, np.newaxis]
        gradient_b = (z - y)
        gradient_b = np.mean(gradient_b)
        return gradient_w, gradient_b
    # 定义梯度下降法更新参数函数
    def update(self, gradient_w, gradient_b, eta=0.01):
        self.w = self.w - eta *gradient_w
        self.b = self.b - eta*gradient_b
    # 定义训练函数
    def train(self, x,y, iterations=100, eta=0.01):
        losses = []
        for i in range(iterations):
            z = self.forward(x)
            L = self.loss(z, y)
            gradient_w, gradient_b = self.gradient(x, y)
            self.update(gradient_w, gradient_b, eta)
            losses.append(L)
            if (i + 1) % 10 == 0:
                print('iter {}, loss {}'.format(i, L))
        return losses
# 主函数
if __name__=='__main__':
    train_data, test_data = load_data()
    x = train_data[:, :-1]
    y = train_data[:, -1:]
    # 定义网络对象
    net=Network(8)
    num_iterations = 1000
    # 启动训练
    losses = net.train(x, y, iterations=num_iterations, eta=0.01)
    plot_x = np.arange(num_iterations)
    plot_y = np.array(losses)
    plt.plot(plot_x, plot_y)
    # 把每轮训练的loss值用曲线形式展示出来
    plt.show()