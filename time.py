import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('result2.csv')

# 确保'次密接日期'列是datetime类型
df['次密接日期'] = pd.to_datetime(df['次密接日期'])

# 按日期分组并计算每天的记录数，同时保留日期信息
daily_counts = df.groupby(df['次密接日期'].dt.date).size().reset_index()
daily_counts.columns = ['日期', '每日记录数']  # 重命名列

# 绘制柱状图
plt.figure(figsize=(12, 6))  # 设置图形大小
plt.bar(daily_counts['日期'], daily_counts['每日记录数'], color='skyblue')  # 绘制柱状图

# 设置图表标题和坐标轴标签
plt.title('Daily count of secondary contact records')
plt.xlabel('日期')
plt.ylabel('记录条数')

# 旋转x轴的日期标签，以便于阅读
plt.xticks(rotation=45)

# 显示图形
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()
