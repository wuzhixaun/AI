from langchain_community.document_loaders import PyPDFLoader


# 创建互联网加载器
loader = PyPDFLoader("https://arxiv.org/pdf/2302.03803.pdf")

# 加载文档
docs = loader.load()
print(docs[0].page_content)