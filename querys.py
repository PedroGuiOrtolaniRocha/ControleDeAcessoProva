from model_morador import Morador

def select_morador_by_id(id: int) -> str:
    return f'SELECT * FROM moradores WHERE id = {id}'

def select_all_moradores() -> str:
    return 'SELECT * FROM moradores'

def insert_morador(m: Morador) -> str:
    return f'INSERT INTO moradores (nome, bloco, ap, senha) VALUES ("{m.nome}", "{m.bloco}", {m.ap}, "{m.senha}")'

def update_morador(id: int, m: Morador) -> str:
    return f'UPDATE moradores SET nome = "{m.nome}", bloco = "{m.bloco}", ap = {m.ap}, senha = "{m.senha}" WHERE id = {id}'

def delete_morador(id: int) -> str:
    return f'DELETE FROM moradores WHERE id = {id}'