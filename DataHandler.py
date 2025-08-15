import sqlite3
from model_morador import Morador

class DataHandler:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL)""")
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS moradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            bloco TEXT NOT NULL,
            ap int NOT NULL,
            senha TEXT NOT NULL)""")
        
        self.connection.commit()

    async def insert_morador_async(self, morador: Morador) -> None:
        self.cursor.execute("INSERT INTO moradores (nome, bloco, ap, senha) VALUES (?, ?, ?, ?)", (morador.nome , morador.bloco, morador.ap, morador.senha))
        self.connection.commit()
    
    def insert_morador(self, morador: Morador) -> None:
        self.cursor.execute("INSERT INTO moradores (nome, bloco, ap, senha) VALUES (?, ?, ?, ?)", (morador.nome , morador.bloco, morador.ap, morador.senha))
        self.connection.commit()

    async def get_moradores_async(self) -> list [Morador]:
        response = self.cursor.execute("SELECT * FROM moradores").fetchall()

        moradores = []
        for m in response:
            moradores.append(Morador(m[1], m[2], m[3], m[4], m[0]))
        
        return moradores 
    
    def get_moradores(self) -> list [Morador]:
        response = self.cursor.execute("SELECT * FROM moradores").fetchall()

        moradores = []
        for m in response:
            moradores.append(Morador(m[1], m[2], m[3], m[4], m[0]))
        
        return moradores 
    
    def get_morador(self, id: str) -> Morador:
        response = self.cursor.execute("SELECT * FROM moradores WHERE id = ?", (id)).fetchone()
        
        if response is None:
            return None
        
        return Morador(response[1], response[2], response[3], response[4], response[0]) 
    
    async def get_morador_async(self, id: str) -> Morador:
        response = self.cursor.execute("SELECT * FROM moradores WHERE id = ?", (id)).fetchone()
        
        if response is None:
            return None
        
        return Morador(response[1], response[2], response[3], response[4], response[0]) 
    
    async def insert_visita(self, nome: str, data: str):
        self.cursor.execute("INSERT INTO visitas (nome, data) VALUES (?, ?)", (nome, data))
        self.connection.commit()

    async def get_visitas(self):
        self.cursor.execute("SELECT * FROM visitas")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
