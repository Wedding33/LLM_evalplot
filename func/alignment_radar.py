from gen_radar import *

def gen_algnment_radar(file_path):

    # Load datas from the csv file
    with open(file_path, "r", encoding="utf-8") as csv:
        lines = csv.readlines()[2:]

    # get the title of the labels
    labels = lines[0].split(",")[1:]
    # get the datas of the models, the scores is not include 总分
    # ZTEAIM_SATURN = [92.5, 60.7, 64.7, 34.2, 39.8, 69.4]
    datas = []
    for line in lines[1:]:
        line = line.split(",")
        line[-1] = line[-1].strip("\n")
        datas.append({"model": line[0], "score": line[1:]})
    
    generate_radar(labels, datas, "总分")