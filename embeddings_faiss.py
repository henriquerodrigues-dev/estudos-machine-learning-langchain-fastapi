from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

docs = [
    Document(page_content="O cachorro corre."),
    Document(page_content="O gato mia."),
]

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
splits = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(splits, embeddings)

query = "O que é LangChain?"
docs_similares = db.similarity_search(query)
for d in docs_similares:
    print("Doc encontrado:", d.page_content)