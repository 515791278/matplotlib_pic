import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']##中文编码
labels = '小孩','青年','中年','老年'
fracs = [15,30,45,10]
plt.axes(aspect=1)  #使x y轴比例相同
explode = [0,0.05,0,0]  # 突出某一部分区域
plt.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)  #autopct显示百分比
plt.show()