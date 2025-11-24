from transformers import AutoModel, AutoTokenizer

# 替换为你选择的模型名称
model_name = "bert-base-chinese"

# 指定模型保存路径
cache_dir = "/Users/wuzhixuan/code/project/AI/day14_demo/test"

# 下载并加载模型和分词器到指定文件夹
model = AutoModel.from_pretrained(model_name, cache_dir=cache_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
