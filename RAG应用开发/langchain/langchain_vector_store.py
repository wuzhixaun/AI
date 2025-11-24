# @author wuzhixuan
# @date 2025-01-27

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def faiss_conn():
    loader = WebBaseLoader(
        web_path="https://www.gov.cn/zhengce/content/202511/content_7047288.htm",
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(id="UCAP-CONTENT"))
    )
    docs = loader.load()

    embeddings = DashScopeEmbeddings(
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        model="text-embedding-v4"
    )

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(docs)

    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store


if __name__ == "__main__":
    faiss_conn()

