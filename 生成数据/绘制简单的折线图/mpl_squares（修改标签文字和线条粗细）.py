# author：K
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# 参数linewidth决定了plot()绘制的线条的粗细
plt.plot(squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
# 设置x轴的标题
plt.xlabel("Value", fontsize=14)
# 设置y轴的标题
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
