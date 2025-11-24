from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 创建pdf加载器
loader = PyPDFLoader(r"/Users/wuzhixuan/code/project/AI/财务管理文档.pdf")

# 加载文档
pages = loader.load_and_split()

# 创建文本分割器
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=100,length_function=len)

# 分割文档
# print([page.page_content.replace("\n", "").replace(" ", "") for page in splitter.split_documents(pages)])

docs = [page.page_content.replace("\n", "").replace(" ", "") for page in splitter.split_documents(pages)]

# 创建段落
paragraphs = splitter.create_documents(docs)

# 打印段落
for paragraph in paragraphs:
    print(paragraph.page_content)
    print("-"*100)