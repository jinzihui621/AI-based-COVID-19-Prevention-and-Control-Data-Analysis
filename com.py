import pandas as pd
import matplotlib.pyplot as plt

# 读取次密接CSV文件
df_secondary = pd.read_csv('result2.csv')
# 确保'次密接日期'列是datetime类型
df_secondary['次密接日期'] = pd.to_datetime(df_secondary['次密接日期'])
# 按日期分组并计算每天的次密接记录数
daily_secondary_counts = df_secondary.groupby(df_secondary['次密接日期'].dt.date).size().reset_index()
daily_secondary_counts.columns = ['日期', 'secondary contract']

# 读取密接CSV文件
df_primary = pd.read_csv('result1.csv')
# 确保'密接日期'列是datetime类型
df_primary['密接日期'] = pd.to_datetime(df_primary['密接日期'])
# 按日期分组并计算每天的密接记录数
daily_primary_counts = df_primary.groupby(df_primary['密接日期'].dt.date).size().reset_index()
daily_primary_counts.columns = ['日期', 'close contact']

# 合并两个DataFrame，以便在同一个图表中绘制
combined_data = pd.merge(daily_secondary_counts, daily_primary_counts, on='日期', suffixes=('_secondary', '_primary'))

# 绘制柱状图
plt.figure(figsize=(12, 6))  # 设置图形大小

# 绘制次密接记录数的柱状图
plt.bar(combined_data['日期'], combined_data['secondary contract'], color='skyblue', label='secondary contract')

# 绘制密接记录数的柱状图
plt.bar(combined_data['日期'], combined_data['close contact'], color='orange', alpha=0.6, label='primary contact')

# 设置图表标题和坐标轴标签
plt.title('Daily counts of primary and secondary contact records')
plt.xlabel('date')
plt.ylabel('Record number of people')
plt.legend()  # 显示图例

# 优化x轴的显示，确保每个日期都清晰可见
plt.gcf().autofmt_xdate()

# 展示图表
plt.show()