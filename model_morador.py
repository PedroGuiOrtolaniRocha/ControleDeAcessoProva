import hashlib

class Morador:
    
    def __init__(self, nome: str, bloco: str, ap: int, senha: str, id: int = None):
        self.id = id
        self.nome = nome
        self.bloco = bloco
        self.ap = ap
        self.senha = hashlib.sha256(senha.encode()).hexdigest()
    

    
