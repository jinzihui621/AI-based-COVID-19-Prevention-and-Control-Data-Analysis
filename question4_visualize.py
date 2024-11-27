import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

# 设置字体为中文字体（例如SimHei或者Microsoft YaHei）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 提供的数据
grid_point_id = [1671, 302, 2809, 2199, 1844, 2886, 839, 2247, 420, 183, 846, 290, 427, 2023, 179, 1729, 2790, 2710, 542]
name = ['游泳场馆29', '茶座6', '杂货铺48', '桌游室38', '网吧32', '银行49', 'KTV15', '咖啡馆39', '茶座8', '酒吧4', '健身场馆15', '银行5', '音乐厅8', '棋牌室35', '餐厅（馆）4', '体育场馆30', '棋牌室48', '教育培训机构46', '影剧院10']
x_coordinate = [13135.95, 9779.82, 8676.71, 3468.84, 10019.00, 9531.87, 16375.74, 553.80, 10497.34, 10951.71, 9491.21, 14514.67, 15692.07, 16295.71, 15542.57, 14463.88, 16081.46, 15799.45, 11099.31]
y_coordinate = [9443.10, 14951.33, 19420.23, 2963.36, 10444.89, 18772.97, 10290.31, 1843.77, 16281.69, 16450.94, 10653.90, 15059.70, 15080.36, 11469.06, 14349.47, 14517.32, 18503.29, 2402.81, 11632.67]
temperature = [36.465315, 36.464258, 36.464323, 36.466211, 36.466736, 36.465235, 36.467087, 36.466566, 36.465254, 36.466834, 36.469298, 36.465876, 36.464960, 36.464916, 36.470552, 36.466383, 36.464383, 36.465118, 36.465040]

# 创建散点图
plt.figure(figsize=(10, 8))
plt.scatter(x_coordinate, y_coordinate, c=temperature, cmap='hot', s=100, alpha=0.7, edgecolors='k')

# 添加场所名称标签
for i in range(len(name)):
    plt.text(x_coordinate[i], y_coordinate[i], name[i], fontsize=15, ha='right')

# 添加颜色条
plt.colorbar(label='Temperature (℃)')

# 设置图形标题和轴标签
plt.title('Places Requiring Priority Control')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# 显示图形
plt.grid(True)
plt.show()
