from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)
resposta = llm("O que é LangChain?")
print("Resposta do LLM:", resposta)