from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda

# Estado inicial
state = {"entrada": "quero saber sobre IA"}

# Função A
def verificar_tipo_entrada(state):
    if "IA" in state["entrada"]:
        return "ia"
    else:
        return "outro"

# Fluxos
def fluxo_ia(state): return {"resposta": "Você perguntou sobre inteligência artificial."}
def fluxo_outro(state): return {"resposta": "Assunto desconhecido."}

# Cria grafo de decisão
builder = StateGraph()

builder.add_node("verifica", RunnableLambda(verificar_tipo_entrada))
builder.add_conditional_edges("verifica", {
    "ia": "responde_ia",
    "outro": "responde_outro"
})
builder.add_node("responde_ia", RunnableLambda(fluxo_ia))
builder.add_node("responde_outro", RunnableLambda(fluxo_outro))
builder.set_entry_point("verifica")

# Executa
grafo = builder.compile()
output = grafo.invoke(state)
print(output)
