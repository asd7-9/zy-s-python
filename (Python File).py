<details>
<summary>📌 点此展开代码</summary>

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from matplotlib.table import Table

# ===== 字体设置 =====
plt.rcParams['font.family'] = 'Hiragino Sans'

# ===== 数据 =====
df = pd.DataFrame({
    "年": [1995, 2000, 2005, 2010, 2015, 2020, 2024, 2030, 2040, 2060, 2070],
    "総人口（千人）": [125570, 126926, 127768, 128057, 127095, 126146, 123802, 120116, 112837, 96148, 86996],
    "65歳以上人口（千人）": [18278, 22044, 25759, 29484, 33866, 36027, 36243, 36962, 39285, 36437, 33671],
    "高齢化率（％）": [14.6, 17.4, 20.2, 23.0, 26.6, 28.6, 29.3, 30.8, 34.8, 37.9, 38.7]
})

# ===== 创建画布 =====
fig, ax = plt.subplots(figsize=(11, 5))
ax.axis('off')

# ===== 表格参数 =====
table = Table(ax, bbox=[0, 0, 1, 1])
col_widths = [0.15, 0.28, 0.32, 0.25]
columns = df.columns.tolist()
n_rows = len(df)
n_cols = len(columns)

# 表头
for col_index in range(n_cols):
    cell = table.add_cell(
        0, col_index,
        width=col_widths[col_index], height=0.5,
        text=columns[col_index], loc='center', facecolor='#d9e1f2'
    )
    cell.get_text().set_fontsize(12)
    cell.get_text().set_fontweight('bold')

# 数据行
for row in range(n_rows):
    for col in range(n_cols):
        value = df.iloc[row, col]
        cell = table.add_cell(
            row + 1, col,
            width=col_widths[col], height=0.5,
            text=str(value), loc='center', facecolor='white'
        )
        cell.get_text().set_fontsize(11)
        cell.get_text().set_fontweight('bold')

# 加入表格
ax.add_table(table)

# 出典
plt.figtext(
    0.5, 0.02,
    "出典：政府統計の総合窓口(e-Stat)『人口推計』張より作成",
    ha="center", fontsize=11, fontweight='bold'
)

plt.subplots_adjust(bottom=0.2)
plt.savefig("japan_population_table.png", dpi=300, bbox_inches="tight")
plt.show()

</details>

