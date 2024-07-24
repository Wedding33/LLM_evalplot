from gen_radar import *

def gen_mtbench_radar(file_path):
    # 获取数据
    with open(file_path, "r") as csv:
        lines = csv.readlines()
    
    # 解析模型名称，最后的 [1:] 是因为此次csv第一行第一个字符为 ,
    models = lines[0][1:].strip().split(",")
    datas = []
    for model in models:
        datas.append({"model": model, "score": []})
    labels = []
    for line in lines[1:]:
        line_list = line.strip("\n").split(',')
        labels.append(line_list[0])
        for i in range(len(line_list) - 1):
            datas[i]["score"].append(line_list[i+1])
    
    generate_radar(labels, datas, "total")