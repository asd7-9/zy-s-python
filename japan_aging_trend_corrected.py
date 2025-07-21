import matplotlib.pyplot as plt
import pandas as pd

# 数据
years = [1995, 2000, 2005, 2010, 2015, 2020, 2024, 2030, 2040, 2060, 2070]
total_population = [125570, 126926, 127768, 128057, 127095, 126146, 123802, 120116, 112837, 96148, 86996]
senior_population = [18278, 22044, 25759, 29484, 33866, 36027, 36243, 36962, 39285, 36437, 33671]
aging_rate = [14.6, 17.4, 20.2, 23.0, 26.6, 28.6, 29.3, 30.8, 34.8, 37.9, 38.7]

# 颜色定义
color_total = '#90CAF9'
color_senior = '#FF5252'
color_rate = '#FFB300'

# 设置支持日文字体（如 Hiragino Sans / Noto Sans CJK）
plt.rcParams['font.family'] = 'Hiragino Sans'

# 图形设置
fig, ax1 = plt.subplots(figsize=(12, 6))

bar_width = 0.35
x = range(len(years))

# 左轴柱状图
ax1.bar([i - bar_width/2 for i in x], total_population, width=bar_width, label='総人口（千人）', color=color_total)
ax1.bar([i + bar_width/2 for i in x], senior_population, width=bar_width, label='65歳以上人口（千人）', color=color_senior)
ax1.set_ylabel('人口（千人）', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left', fontsize=10)

# 右轴折线图
ax2 = ax1.twinx()
ax2.plot(x, aging_rate, color=color_rate, marker='o', linewidth=2.5, label='高齢化率（％）')
ax2.set_ylabel('高齢化率（％）', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)

# 出典信息
plt.title('日本の高齢化の推移', fontsize=14, fontweight='bold')
plt.figtext(0.5, 0.01, '出典：政府統計の総合窓口(e-Stat)『人口推計』張より作成', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("japan_aging_trend_corrected.png", dpi=300, bbox_inches="tight")
plt.show()


