import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import time
import os
import json

def gen_OCRBENCH(file_path):
    # 读取 CSV 文件
    with open(file_path, "r") as file:
        data = json.load(file)

    # 提取数据
    categories = list(data.keys())
    values = list(data.values())
    categories.pop()
    values.pop()

    # print(categories)
    # print(values)

    # 按数值大小排序并创建颜色映射
    values = np.array(values)
    sorted_indices = np.argsort(-values)  # 按降序排列
    sorted_values = values[sorted_indices]
    sorted_categories = [categories[i] for i in sorted_indices]

    # 创建自定义颜色映射，越接近1越红，越接近0越蓝
    colors = [(0.3, 1, 0.6, i/sum(values)) for i in sorted_values]  # RGBA格式，透明度为数值大小

    # 创建条形图
    plt.figure(figsize=(12, 6))
    bars = plt.barh(sorted_categories, sorted_values, color=colors)
    plt.xlabel('Accuracy')
    plt.title('Accuracy of Different Categories')
    plt.xlim(0, 1000)  # 设置x轴范围为0到1
    plt.gca().invert_yaxis()  # 反转 y 轴，使最高的类别在顶部

    # 在每个条形后面添加对应的数值
    for bar, value in zip(bars, sorted_values):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.2f}', ha='left', va='center')

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
