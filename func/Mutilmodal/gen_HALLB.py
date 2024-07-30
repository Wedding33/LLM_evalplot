import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time

def gen_HALLB(csv, base_csv, base_model_name):
    # 读取 CSV 文件
    data = pd.read_csv(csv)
    base_data = pd.read_csv(base_csv)

    # 提取数据
    categories = list(data.iloc[:, 0])  # 提取第一列数据，作为类别
    values = data.iloc[:, 1].astype(float)  # 取第二列数据，将其转换为浮点数
    base_values = base_data.iloc[:, 1].astype(float)

    # 按数值大小排序并创建颜色映射
    sorted_indices = np.argsort(-values)  # 按降序排列
    sorted_values = values[sorted_indices]
    sorted_base_values = base_values[sorted_indices]
    sorted_categories = [categories[i] for i in sorted_indices]

    # 创建自定义颜色映射
    colors = [(0.3, 1, 0.6, 0.7) for i in sorted_values]  # RGBA格式，透明度为数值大小
    base_colors = [(0.8, 0.5, 0.9, 0.5) for i in sorted_base_values]

    # 创建条形图
    plt.figure(figsize=(12, 6))
    bar_width = 0.35  # 条形宽度
    index = np.arange(len(sorted_categories))
    bars = plt.barh(index, sorted_values, bar_width, label='Current', color=colors)
    base_bars = plt.barh(index, sorted_base_values, bar_width, label=f'{base_model_name}', color=base_colors)

    plt.xlabel('Accuracy')
    plt.title('Accuracy of Different Categories')
    plt.yticks(index + bar_width / 2, sorted_categories)
    plt.legend()
    plt.gca().invert_yaxis()  # 反转 y 轴，使最高的类别在顶部

    # 在每个条形后面添加对应的数值
    for bar, base_bar, value, base_value in zip(bars, base_bars, sorted_values, sorted_base_values):
        if value > base_value:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.3f} ({base_value:.3f})', ha='left', va='center')
        else:
            plt.text(base_bar.get_width(), base_bar.get_y() + base_bar.get_height() / 2, f'{value:.3f} ({base_value:.3f})', ha='left', va='center')

    # 创建结果目录
    timestamp = time.strftime("%Y%m%d%H%M")
    csv_folder = os.path.dirname(csv)
    result_folder = os.path.join("./result", os.path.basename(csv_folder) + "_" + timestamp)
    filename = csv.split("/")[-1].split(".")[0]

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # 保存结果图片
    result_filename = os.path.join(result_folder, f"{filename}_{timestamp}.png")
    plt.savefig(result_filename)
