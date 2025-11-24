from langchain_community.document_loaders import PyPDFLoader



# 创建pdf加载器
loader = PyPDFLoader(r"/Users/wuzhixuan/code/project/AI/财务管理文档.pdf")

# # 加载pdf文件
# pdf_docs = loader.load()

# # 打印pdf文件
# # print(pdf_docs)
# i = 1
# for page in pdf_docs:
#     print(f"第{i}页")
#     print(page.page_content)
#     i += 1
#     print("-"*100)

# 加载pdf文件并分割
pdf_docs = loader.load_and_split()

# 打印pdf文件
print(pdf_docs[0])

for page in pdf_docs:
    print(f"第{page.metadata['page_label']}页")
    print(page.page_content)
    print("-"*100)