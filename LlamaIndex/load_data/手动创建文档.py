from llama_index.core import Document,SimpleDirectoryReader
from pathlib import Path
import sys
import os

# 方法1: 添加父目录到 Python 路径（推荐）
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# 方法2: 使用 os.path（备选方案）
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

# 现在可以导入父级目录的LoadLLm模块
from LoadLLm import load_llm




text_list = ["text1","text2","text3"]

# 创建文档
documents = [Document(text=text,metadata={"filename": "文件名称", "category": "类别"}) for text in text_list]
print(documents)


# 自动设置元数据
def filename_fn(filename: str):
    return {
        "file_name": filename,
        "category": Path(filename).suffix,
    }

documents = SimpleDirectoryReader(input_dir="../data", file_metadata=filename_fn).load_data()
print(documents)