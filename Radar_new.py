from mtbench_radar import *
from alignment_radar import *
from scatter_plot import *
from config import *

if __name__ == "__main__":
    gen_scatter_plot(["test_model"], [4.5], [8.8])
    gen_algnment_radar("./data/judged-by--gpt-4-turbo-capability.csv")
    gen_mtbench_radar("./data/judged-by--gpt-4-turbo-capability.csv")
