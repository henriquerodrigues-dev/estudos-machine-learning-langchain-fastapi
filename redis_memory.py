import redis

# Conecta no Redis local (certifique-se de que está rodando)
r = redis.Redis(host='localhost', port=6379, db=0)

def salvar_conversa(user_id: str, mensagem: str):
    chave = f"user:{user_id}:conversa"
    r.rpush(chave, mensagem)

def obter_conversa(user_id: str):
    chave = f"user:{user_id}:conversa"
    return r.lrange(chave, 0, -1)