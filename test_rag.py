import pytest
from fastapi.testclient import TestClient
from fastapi_rag import app

client = TestClient(app)

def test_rag_endpoint_responde():
    response = client.get("/pergunta", params={"query": "Qual o propósito da empresa?"})
    assert response.status_code == 200
    assert "resposta" in response.json()
