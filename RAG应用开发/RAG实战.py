import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
# 切割文本
def split_windows_chunks(text, chunk_size=10, overlap=5):
    return [text[i:i+chunk_size] for i in range(0, len(text), overlap)]



# 读取PDF
def extract_text_from_pdf(pdf_path,page_nums=None,min_line_length=1):
    '''从PDF中提取文本'''
    paragraphs = []
    buffer = ''
    full_text = ''

    for i,page_layout in enumerate(extract_pages(pdf_path)):
        #print(i,page_layout)
        # 如果page_nums不为空，则只处理指定的页码
        if page_nums is not None and i not in page_nums:
            continue    
        for element in page_layout:
            # print(element)
            # 检测 element 是否为 LTTextContainer
            if isinstance(element,LTTextContainer):
                # print(element.get_text())
                # 去除行和空格
                full_text += element.get_text().replace('\n','').replace(' ','')
            
    
    if full_text:
        # 调用切割函数
        text_chunks = split_windows_chunks(full_text,chunk_size=250,overlap=100)
        for text in text_chunks:
            paragraphs.append(text)

    return paragraphs


# 封装向量数据库
class MyVectorDBConnector:

    def __init__(self, collection_name):
        # 创建向量数据库
        self.db = chromadb.PersistentClient(path="chroma.db")
        # 创建集合
        self.collection = self.db.get_or_create_collection(name=collection_name)
    

    # 获取向量
    def get_embeddings(self, texts,model="text-embedding-v4",batch_size=10):
        # 将文本向量化
        all_embeddings = []
        # 分批处理：range(0, len(texts), batch_size) 生成索引 0, 10, 20, ...
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]  # 提取当前批次
            data_embedding = client.embeddings.create(input=batch, model=model).data
            batch_embeddings = [item.embedding for item in data_embedding]
            all_embeddings.extend(batch_embeddings)  # 合并结果
        return all_embeddings

    # 添加文档
    def add_document(self, instructions):
        # 将文本向量化
        embeddings = self.get_embeddings(instructions,batch_size=10)
        # 把向量化的数据和原文存入向量数据库
        self.collection.add(
            embeddings=embeddings,  # 每个文档的向量
            documents=instructions,  # 文档的原文
            ids=[f"id{i}" for i in range(len(instructions))]  # 每个文档的 id
        )

    # 查询
    def search(self, query, n_results=1):
        '''查询向量数据库'''
        # 将查询文本向量化
        query_embedding = self.get_embeddings([query],batch_size=10)
        # 查询向量数据库
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results

class RAG_bot:
    def __init__(self,vector_db, n_results,prompt_template):
        self.vector_db = vector_db
        self.n_results = n_results
        self.prompt_template = prompt_template

    ## 调用 llm 模型
    def get_completion(self, prompt, model="qwen-plus"):
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content

    def chat(self, query):
        '''聊天'''
        # 查询向量数据库
        results = self.vector_db.search(query, self.n_results)

        # 替换提示词
        prompt = self.prompt_template.replace("__INFO__", '\n'.join(results['documents'][0])).replace("__QUERY__", query)

        # 调用 llm 模型
        response = self.get_completion(prompt=prompt)
        print('AI回复的内容：', response)
        return response

if __name__ == "__main__":
    # 加载环境变量
    load_dotenv()

    # 提示词模板
    prompt_template = """
        你是一个问答机器人。
        你的任务是根据下述给定的已知信息回答用户问题。
        确保你的回复完全依据下述已知信息。不要编造答案。
        如果下述已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。

        已知信息:
        __INFO__

        用户问：
        __QUERY__

        请用中文回答用户问题。
        """


    # 创建 Openai 客户端
    client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),base_url=os.getenv("DASHSCOPE_BASE_URL"))
    

    # 提取文本
    result = extract_text_from_pdf(pdf_path="财务管理文档.pdf",page_nums=[0,1])

    # print(result)

    # 创建向量数据库
    vector_db = MyVectorDBConnector(collection_name="rag_demo1")

    # 添加文档
    vector_db.add_document(instructions=result)
    
    # 创建 RAG 模型
    rag_bot = RAG_bot(vector_db=vector_db, n_results=2,prompt_template=prompt_template)
    
    # 知识问答
    rag_bot.chat(query="公司总经理在财务上行使下列职责")