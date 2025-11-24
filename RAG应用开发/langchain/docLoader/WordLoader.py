from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# 创建word加载器
loader = UnstructuredWordDocumentLoader(r"/Users/wuzhixuan/code/project/AI/人事管理流程.docx")

# print(loader)


# 加载文档并分割成段落或元素
documents = loader.load()
# print(documents)

# 输出加载的内容
for doc in documents:
    print(doc.page_content)