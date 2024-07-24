from gen_radar import *

def gen_scatter_plot(model_name, mtb_score, align_score):
    
    plt.figure()
    models = ["GPT-4-0613", "GPT-3.5-Turbo-0613", "ChatGLM-6B", "Qwen-7B-chat", "LLaMA2-Chat-7B"] + model_name
    mt_bench_scores = [9.18, 8.39, 4.5, 5.08, 5.43] + mtb_score
    align_bench_scores = [6.83, 5.68, 6.24, 4.91, 3.57] + align_score
    
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
    markers = ['o', 's', 'v', '^', 'x', 'p', 'D', 'h']
    for i in range(len(models)):
        plt.scatter(mt_bench_scores[i], align_bench_scores[i], color=colors[i % 8], marker=markers[i % 8], label=models[i])
        if models[i] == "GPT-4-0613":
            plt.text(mt_bench_scores[i] - 0.8, align_bench_scores[i] - 0.2, models[i])
        elif models[i] == "GPT-3.5-Turbo-0613":
            plt.text(mt_bench_scores[i] - 0.8, align_bench_scores[i] + 0.1, models[i])
        else:
            plt.text(mt_bench_scores[i] + 0.1, align_bench_scores[i] + 0.1, models[i])
    
    plt.title("MT-Bench v.s. Alignbench Performance of Various Model")
    plt.xlabel("MT-Bench Score")
    plt.ylabel("Alignbench Score")
    
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d-%H%M%S")
    plt.savefig(f'result{formatted_time}.png')