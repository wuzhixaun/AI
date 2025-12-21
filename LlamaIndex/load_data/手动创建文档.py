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

# 使用绝对路径，更可靠
# data 目录应该在 LlamaIndex 根目录下
data_dir = Path(__file__).parent.parent / "data"

# 检查目录是否存在
if not data_dir.exists():
    print(f"⚠️  警告: 目录 {data_dir} 不存在")
    print(f"📁 正在创建目录: {data_dir}")
    # 创建目录（包括父目录）
    data_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ 目录创建成功！")
    print(f"💡 提示: 请将需要加载的文件放入 {data_dir} 目录中")
    print(f"   然后重新运行此脚本即可加载文档")
else:
    print(f"📂 正在从目录加载文档: {data_dir}")
    try:
        documents = SimpleDirectoryReader(input_dir=str(data_dir), file_metadata=filename_fn).load_data()
        if documents:
            print(f"✅ 成功加载 {len(documents)} 个文档:")
            for i, doc in enumerate(documents, 1):
                print(f"   {i}. {doc.metadata.get('file_name', '未知文件')}")
            print(f"\n文档详情:")
            print(documents)
        else:
            print(f"⚠️  目录为空，没有找到任何文件")
    except Exception as e:
        print(f"❌ 加载文档时出错: {e}")