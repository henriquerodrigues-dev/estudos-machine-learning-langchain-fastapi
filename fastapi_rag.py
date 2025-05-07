from fastapi import FastAPI, Query
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
import os

app = FastAPI()

# Configure sua chave da OpenAI
os.environ["OPENAI_API_KEY"] = "sua-chave-aqui"

# Carrega vetor FAISS
vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings())

# Cria a chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

@app.get("/pergunta")
def responder_pergunta(query: str = Query(..., description="Pergunta do usuário")):
    result = qa_chain(query)
    return {
        "pergunta": query,
        "resposta": result["result"]
    }
