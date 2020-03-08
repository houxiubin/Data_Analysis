import random

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=10)

x = range(0, 120)
y1 = [random.randint(20, 25) for i in range(120)]
y2 = [random.randint(20, 25) for k in range(120)]
x_lable = ["{}:{}".format(10 + int(i / 60), (i % 60 if i % 60 >= 10 else '0' + str(i % 60))) for i in x]
# 大小
plt.figure(figsize=(30, 8), dpi=100)
# 设置x轴上显示的字符(可以把数字转换成字符串)
plt.xticks(list(x)[::2], x_lable[::2], rotation=0, fontproperties=my_font)
# 折线图
plt.plot(x, y1, label='北京', color='r', linestyle='-.')
# 散点图
plt.scatter(x, y2, label='阳泉', color='y')
# 条形图
plt.bar(x, y1, color='g')
# 横着的条形图
plt.barh(x, y1, color='g', height=0.8)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度 单位(℃)', fontproperties=my_font)
plt.title('10点到12点每分钟的气温变化情况', fontproperties=my_font)
# 网格
plt.grid(alpha=0.4, color='g', linestyle=':')
# 图例
plt.legend(prop=my_font, loc='upper left')
# plt.show()
plt.savefig('./t2.png')
