from Morador.model_morador import Morador

def create_table_morador() -> str:
    return """
        CREATE TABLE IF NOT EXISTS moradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            bloco TEXT NOT NULL,
            ap int NOT NULL,
            senha TEXT NOT NULL,
            em_casa BOOLEAN DEFAULT 1,
            data_entrada TEXT DEFAULT NULL,
            data_saida TEXT DEFAULT NULL,
            data_cadastro TEXT NOT NULL)"""

def select_morador_by_id(id: int) -> str:
    return f'SELECT * FROM moradores WHERE id = {id}'

def select_all_moradores() -> str:
    return 'SELECT * FROM moradores'

def select_moradores_by_ap(apartamento: str) -> str:
    return f'SELECT * FROM moradores WHERE ap = "{apartamento}"'

def insert_morador(m: Morador) -> str:
    return f'INSERT INTO moradores (nome, bloco, ap, senha, data_cadastro) VALUES ("{m.nome}", "{m.bloco}", {m.ap}, "{m.senha}", "{m.data_cadastro}")'

def update_morador(m: Morador) -> str:
    return f'UPDATE moradores SET nome = "{m.nome}", bloco = "{m.bloco}", ap = {m.ap}, senha = "{m.senha}" WHERE id = {m.id}'

def delete_morador(id: int) -> str:
    return f'DELETE FROM moradores WHERE id = {id}'

def registro_entrada(m: Morador) -> str:
    return f'UPDATE moradores SET em_casa = true, data_entrada = "{m.data_entrada}", data_saida = NULL WHERE id = {m.id}'

def registro_saida(m: Morador) -> str:
    return f'UPDATE moradores SET em_casa = false, data_saida = "{m.data_saida}" WHERE id = {m.id}'