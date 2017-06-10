import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)  # 创建图表1
plt.figure(2)  # 创建图表2
ax1 = plt.subplot(211)  # 在图表2中创建子图1
ax2 = plt.subplot(212)  # 在图表2中创建子图2

x = np.linspace(0, 3, 100)
for i in  range(5):
    plt.figure(1)  # ❶ # 选择图表1
    plt.plot(x, np.exp(i * x / 3))
    plt.sca(ax1)  # ❷ # 选择图表2的子图1
    plt.plot(x, np.sin(i * x))
    plt.sca(ax2)  # 选择图表2的子图2
    plt.plot(x, np.cos(i * x))

plt.show()
import numpy as np
import random
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']##中文编码
data1 = [random.gauss(15, 10) for i in range(500)]
data2 = [random.gauss(5, 5) for i in range(500)]
bins = np.arange(-60, 60, 2.5)
plt.xlim([min(data1 + data2) - 5, max(data1 + data2) + 5])

plt.hist(data1, bins=bins, alpha=0.3, label='class 1')
plt.hist(data2, bins=bins, alpha=0.3, label='class 2')
plt.title('企业财报')
plt.xlabel('variable X')
plt.ylabel('count')
plt.legend(loc='upper right')

plt.show()
