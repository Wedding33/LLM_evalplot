import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import time
import os
import json

def gen_OCRBENCH(file_path, base_file_path, base_model_name):
    # 读取 CSV 文件
    with open(file_path, "r") as file1:
        data = json.load(file1)

    with open(base_file_path, "r") as file2:
        base_data = json.load(file2)

    # 提取数据
    categories = list(data.keys())
    base_categories = list(base_data.keys())
    values = list(data.values())
    base_values = list(base_data.values())
    categories.pop(-2)
    values.pop(-2)
    base_categories.pop(-2)
    base_values.pop(-2)

    # print(categories)
    # print(values)

    # 按数值大小排序并创建颜色映射
    values = np.array(values)
    base_values = np.array(base_values)
    sorted_indices = np.argsort(-values)  # 按降序排列
    sorted_values = values[sorted_indices]
    sorted_base_values = base_values[sorted_indices]
    sorted_categories = [categories[i] for i in sorted_indices]

    # 创建自定义颜色映射
    colors = [(0.3, 1, 0.6, 0.7) for i in sorted_values]  # RGBA格式，透明度为数值大小
    base_colors = [(0.8, 0.5, 0.9, 0.5) for i in sorted_base_values]

    # 创建条形图
    plt.figure(figsize=(12, 6))
    # bars = plt.barh(sorted_categories, sorted_values, color=colors)
    
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
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.3f}({base_value:.3f})', ha='left', va='center')
        else:
            plt.text(base_bar.get_width(), base_bar.get_y() + base_bar.get_height() / 2, f'{value:.3f}({base_value:.3f})', ha='left', va='center')

    # 创建结果目录
    timestamp = time.strftime("%Y%m%d%H%M")
    file_folder = os.path.dirname(file_path)
    result_folder = os.path.join("./result", os.path.basename(file_folder) + "_" + timestamp)
    filename = file_path.split("/")[-1].split(".")[0]

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # 保存结果图片
    result_filename = os.path.join(result_folder, f"{filename}_{timestamp}.png")

    plt.savefig(result_filename)
