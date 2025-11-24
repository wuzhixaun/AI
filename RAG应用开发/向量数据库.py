import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

class MyVectorDBConnector:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.db = chromadb.PersistentClient(path="chroma.db")
        # 创建数据库
        self.collection = self.db.get_or_create_collection(name=collection_name)

    # 获取向量
    def get_embeddings(self, texts, model="text-embedding-v4"):
        '''封装 qwen 的 Embedding 模型接口'''
        # print('texts', texts)
        data = client.embeddings.create(input=texts, model=model).data
        return [item.embedding for item in data]

    # 添加文档
    def add_document(self, instructions, outputs):
        '''向 collection 中添加文档与向量'''
        # get_embeddings(instructions)
        # 将数据向量化
        embeddings = self.get_embeddings(instructions)

        # 把向量化的数据和原文存入向量数据库
        self.collection.add(
            embeddings=embeddings,  # 每个文档的向量
            documents=outputs,  # 文档的原文
            ids=[f"id{i}" for i in range(len(outputs))]  # 每个文档的 id
        )

    # 查询
    def query_document(self, query, n_results=1):
        '''查询collection里面的数据'''
        # 查询
        results = self.collection.query(
            query_embeddings=self.get_embeddings([query]),
            n_results=n_results
        )
        return results

if __name__ == "__main__":
    # 加载环境变量
    load_dotenv()
    # 创建OpenAI客户端
    client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))
    # 创建向量数据库
    vector_db = MyVectorDBConnector(collection_name="test_collection")
    
    db = MyVectorDBConnector(collection_name="test_collection")

    # 读取文件
    with open('train_zh.json', 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]
    # print(data)
    
     # 获取前10条的问题和输出
    instructions = [entry['instruction'] for entry in data[0:10]]
    outputs = [entry['output'] for entry in data[0:10]]

    # 添加到向量数据库
    vector_db.add_document(instructions=instructions, outputs=outputs)

    user_query = '发财'
    # 查询文档
    results = vector_db.query_document(query=user_query)


    print(results)