import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def generate_radar(labels, datas, top_label=None, font_prop=""):
    plt.figure()
    # 为每个维度设定不同的最大值
    # max_values = [max(ZTEAIM_SATURN[i], ZTEAIM_Mars[i], ChatGPT_3_5[i]) for i in range(len(labels))]
    max_values = []
    for i in range(len(datas[0]["score"])):
        max_values.append(float(max(datas[j]["score"][i] for j in range(len(datas)))))
    
    # 获取每个模型每个项目得分对于最大值的比例
    for i in range(len(datas)):
        datas[i]["norm"] = [float(datas[i]["score"][j]) / max_values[j] for j in range(len(labels))]
    # 转换为角度
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles = [angle + 30 / 180 * np.pi for angle in angles]
    angles += angles[:1]
    
    # 使雷达图闭合，把第一个元素加到最后一个元素后
    # ZTEAIM_SATURN_norm += ZTEAIM_SATURN_norm[:1]
    for i in range(len(datas)):
        datas[i]["norm"] += datas[i]["norm"][:1]

    # 设置画布
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
    
    # 设置旋转角度，让总分在最上方
    if (top_label != None):
        label_angles = list(zip(labels, angles))
        target_angle = next(angle for label, angle in label_angles if label == top_label)
        rotation_angle = np.degrees(np.pi/2 - target_angle)
        ax.set_theta_offset(np.radians(rotation_angle))

    # 配色方案
    colors = [
        "tomato",
        "dodgerblue",
        "green",
        "lightsalmon",
        "lightblue",
        "lightgreen",
        "chocolate",
        "lightyellow",
    ]
    for i in range(len(datas)):
        # 绘制雷达图
        # ax.fill(angles, ZTEAIM_SATURN_norm, color=colors['fill_ZTEAIM_SATURN'], alpha=0.25)
        # ax.plot(angles, ZTEAIM_SATURN_norm, color=colors['ZTEAIM_SATURN'], linewidth=2, label='ZTEAIM-Saturn')
        ax.fill(angles, datas[i]["norm"], color=colors[i % len(colors)], alpha=0.25)
        ax.plot(
            angles,
            datas[i]["norm"],
            color=colors[i % len(colors)],
            linewidth=2,
            label=datas[i]["model"],
        )

    # 添加中文标签并将它们移到外部
    theta_labels = ax.set_thetagrids(
        np.degrees(angles[:-1]), labels, fontproperties=font_prop
    )
    
    for label in theta_labels[1]:  # 获取角度标签
        label.set_position(
            (label.get_position()[0], label.get_position()[1] - 0.1)
        )  # 调整距离

    # 为每个维度设置实际分数标签
    for i, angle in enumerate(angles[:-1]):
        ticks = np.linspace(0, max_values[i], num=6, endpoint=True)
        ticks_norm = ticks / max_values[i]
        for tick, tick_norm in zip(ticks[1:], ticks_norm[1:]):
            ax.text(
                angle,
                tick_norm,
                f"{tick:.1f}",
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=10,
                color="grey",
            )

    # 隐藏刻度线和标签
    ax.set_yticklabels([])

    # 设置图例在底部平铺
    legend = ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,
        frameon=False,
        fontsize=26,
        prop={"weight": "bold"},
    )

    plt.subplots_adjust(bottom=0.25)
    
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d-%H%M%S")
    plt.savefig(f'result{formatted_time}.png')
    # plt.show()