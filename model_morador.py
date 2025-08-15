import hashlib
from datetime import datetime

def new_from_db(row) -> 'Morador':
    id = row[0]
    nome = row[1]
    bloco = row[2]
    ap = row[3]
    senha = row[4]
    em_casa = row[5]
    data_entrada = row[6]
    data_saida = row[7]
    data_cadastro = row[8]
    return Morador(nome, bloco, ap, senha, id, em_casa, data_entrada, data_saida, data_cadastro)

class Morador:
    
    def __init__(self, nome: str, bloco: str, ap: int, senha: str, id: int = None, 
                 em_casa: bool = True, data_entrada: str = None, data_saida: str = None, 
                 data_cadastro: str = None):
        self.id = id
        self.nome = nome
        self.bloco = bloco
        self.ap = ap
        self.senha = hashlib.sha256(senha.encode()).hexdigest()
        self.em_casa = True
        self.data_entrada = datetime.now()
        self.data_saida = None
        self.data_cadastro = datetime.now()
    


    
