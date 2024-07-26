from func.Mutilmodal.gen_MMBench_CN import *
from func.Mutilmodal.gen_MMBench_EN import *
from func.Mutilmodal.gen_MMSTAR import *
from func.Mutilmodal.gen_HALLB import *
from func.Mutilmodal.gen_AI2D import *
from func.Mutilmodal.gen_MMVET import *
from func.Mutilmodal.gen_MMMU import *
from func.Mutilmodal.gen_MATHVISTA import *
from func.Mutilmodal.gen_OCRBENCH import *

if __name__ == "__main__":
    # gen_MMBench_CN("./data/MarsV/MarsV_MMBench_DEV_CN_V11_acc.csv")
    # gen_MMBench_EN("./data/MarsV/MarsV_MMBench_DEV_EN_V11_acc.csv")
    # gen_MMSTAR("./data/MarsV/MarsV_MMStar_acc.csv")
    gen_HALLB("./data/MarsV/MarsV_HallusionBench_score.csv")
    # gen_AI2D("./data/MarsV/MarsV_MMStar_acc.csv")
    # gen_MMVET("./data/MarsV/MarsV_MMStar_acc.csv")
    # gen_MMMU("./data/MarsV/MarsV_MMStar_acc.csv")
    # gen_MATHVISTA("./data/MarsV/MarsV_MMStar_acc.csv")
    # gen_OCRBENCH("./data/MarsV/MarsV_MMStar_acc.csv")
