import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import time
import os

def gen_HALLB(csv):
    # 读取 CSV 文件
    data = pd.read_csv(csv)

    # 提取数据
    categories = list(data.iloc[:, 0])  # 提取第一列数据，作为类别
    values = data.iloc[:, 1].astype(float)  # 取第二列数据，将其转换为浮点数

    # print(categories)
    # print(values)

    # 按数值大小排序并创建颜色映射
    sorted_indices = np.argsort(-values)  # 按降序排列
    sorted_values = values[sorted_indices]
    sorted_categories = [categories[i] for i in sorted_indices]

    # 创建自定义颜色映射，越接近1越红，越接近0越蓝
    colors = [(0.3, 1, 0.6, i/100) for i in sorted_values]  # RGBA格式，透明度为数值大小

    # 创建条形图
    plt.figure(figsize=(12, 6))
    bars = plt.barh(sorted_categories, sorted_values, color=colors)
    plt.xlabel('Accuracy')
    plt.title('Accuracy of Different Categories')
    plt.xlim(0, 100)  # 设置x轴范围为0到1
    plt.gca().invert_yaxis()  # 反转 y 轴，使最高的类别在顶部

    # 在每个条形后面添加对应的数值
    for bar, value in zip(bars, sorted_values):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.2f}', ha='left', va='center')

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
