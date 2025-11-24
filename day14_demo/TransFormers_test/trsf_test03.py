import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 设置模型目录
model_dir = "./my_model_cache/uer/gpt2-chinese-cluecorpussmall/models--uer--gpt2-chinese-cluecorpussmall/snapshots/c2c0249d8a2731f269414cc3b22dff021f8e07a3/"

# 设置设备：优先使用 GPU，如果没有则使用 CPU
device = 0 if torch.cuda.is_available() else 'cpu'
torch_device = torch.device(device)

# 加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

# 创建文本生成器（pipeline）
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=torch_device.index if device == 0 else -1)

# 生成文本
output = generator("你好，我是一款语言模型，", max_length=50, num_return_sequences=1, truncation=True)

# 打印输出结果
print(output)
