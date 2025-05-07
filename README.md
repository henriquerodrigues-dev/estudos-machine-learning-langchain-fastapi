<h1>Projeto Pessoal: LLMs, RAG, ML e Backend com Python</h1>
<body>
  <p>
    Este projeto foi desenvolvido para fins de <strong>estudo técnico e preparação para entrevistas</strong> 
    de vagas que envolvem <strong>desenvolvimento backend com foco em IA conversacional</strong>, 
    LLMs, integração com bases vetoriais e machine learning.
  </p>

  <p>Inclui exemplos práticos com:</p>
  <ul>
    <li><strong>LangChain</strong> para RAG</li>
    <li><strong>FAISS</strong> para buscas vetoriais</li>
    <li><strong>Redis</strong> como memória (opcional)</li>
    <li><strong>FastAPI</strong> para REST API</li>
    <li><strong>scikit-learn</strong> para ML tradicional</li>
    <li><strong>LangGraph</strong> para simulação de fluxo conversacional</li>
  </ul>

  <h2>📁 Funcionalidades</h2>
  <table>
    <tr><th>Arquivo</th><th>Descrição</th></tr>
    <tr><td><code>llm_openai.py</code></td><td>Chamada simples a um LLM via OpenAI</td></tr>
    <tr><td><code>embeddings_faiss.py</code></td><td>Criação e consulta de embeddings vetoriais com FAISS</td></tr>
    <tr><td><code>rag_chain.py</code></td><td>Pipeline simples RAG com LangChain</td></tr>
    <tr><td><code>ml_sklearn.py</code></td><td>Modelo RandomForest com dataset Iris (ML clássico)</td></tr>
    <tr><td><code>fastapi_rag.py</code></td><td>API REST com pergunta/resposta via LangChain + FAISS</td></tr>
    <tr><td><code>redis_memory.py</code></td><td>Funções auxiliares para salvar conversa com Redis</td></tr>
    <tr><td><code>langgraph_example.py</code></td><td>Exemplo de fluxo com múltiplos caminhos usando LangGraph</td></tr>
    <tr><td><code>tests/test_rag.py</code></td><td>Testes com Pytest da API RAG</td></tr>
  </table>

  <h2>🚀 Como executar localmente</h2>
  <pre><code># Ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar exemplos básicos
python llm_openai.py
python rag_chain.py
python ml_sklearn.py

# Rodar API
uvicorn fastapi_rag:app --reload
  </code></pre>

  <h2>🌐 Exemplo de uso da API</h2>
  <pre><code>GET /pergunta?query=Qual animal mia?</code></pre>

  <h2>✅ Testes</h2>
  <pre><code>pytest tests/</code></pre>

  <h2>🛠️ Tecnologias</h2>
  <ul>
    <li>Python 3.10+</li>
    <li>LangChain</li>
    <li>OpenAI API</li>
    <li>FAISS</li>
    <li>Redis (opcional)</li>
    <li>FastAPI</li>
    <li>scikit-learn</li>
    <li>LangGraph</li>
    <li>Pytest</li>
  </ul>

  <h2>📌 Observação</h2>
  <p>
    🔎 <em>Este projeto é pessoal e foi desenvolvido com o objetivo de demonstrar 
    competências técnicas em entrevistas técnicas para posições de backend com foco em IA.</em>
  </p>

  <h2>👤 Autor</h2>
  <p>Feito por <strong>Henrique Rodrigues</strong></p>

</body>
</html>
