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
    gen_MMBench_CN("./data/MarsV/MarsV_MMBench_DEV_CN_V11_acc.csv", "./data/MarsVBase/MarsV_MMBench_DEV_CN_V11_acc.csv", "MarsV-Base")
    gen_MMBench_EN("./data/MarsV/MarsV_MMBench_DEV_EN_V11_acc.csv", "./data/MarsVBase/MarsV_MMBench_DEV_EN_V11_acc.csv", "MarsV-Base")
    gen_MMSTAR("./data/MarsV/MarsV_MMStar_acc.csv", "./data/MarsVBase/MarsV_MMStar_acc.csv", "MarsV-Base")
    gen_HALLB("./data/MarsV/MarsV_HallusionBench_score.csv", "./data/MarsVBase/MarsV_HallusionBench_score.csv", "MarsV-Base")
    gen_AI2D("./data/MarsV/MarsV_AI2D_TEST_acc.csv", "./data/MarsVBase/MarsV_AI2D_TEST_acc.csv", "MarsV-Base")
    gen_MMVET("./data/MarsV/MarsV_MMVet_dt_gpt_score.csv", "./data/MarsVBase/MarsV_MMVet_dt_gpt_score.csv", "MarsV-Base")
    gen_MMMU("./data/MarsV/MarsV_MMMU_DEV_VAL_acc.csv", "./data/MarsVBase/MarsV_MMMU_DEV_VAL_acc.csv", "MarsV-Base")
    gen_MATHVISTA("./data/MarsV/MarsV_MathVista_MINI_dt_gpt_score.csv", "./data/MarsVBase/MarsV_MathVista_MINI_dt_gpt_score.csv", "MarsV-Base")
    gen_OCRBENCH("./data/MarsV/MarsV_OCRBench_score.json", "./data/MarsVBase/MarsV_OCRBench_score.json", "MarsV-Base")