from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
resposta_rag = qa_chain.run("O cachorro late?")
print("Resposta via RAG:", resposta_rag)