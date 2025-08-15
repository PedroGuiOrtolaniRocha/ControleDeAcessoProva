import sqlite3
import querys
from model_morador import Morador
from model_morador import new_from_db

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
            senha TEXT NOT NULL,
            em_casa BOOLEAN DEFAULT 1,
            data_entrada TEXT DEFAULT NULL,
            data_saida TEXT DEFAULT NULL,
            data_cadastro TEXTNOT NULL)""")
        
        self.connection.commit()

    async def insert_morador(self, morador: Morador) -> None:
        self.cursor.execute(
            querys.insert_morador(morador)
        )
        self.connection.commit()
    

    async def get_moradores(self) -> list [Morador]:
        response = self.cursor.execute(
            querys.select_all_moradores()
        ).fetchall()

        moradores = []
        for m in response:
            moradores.append(new_from_db(m))
        
        return moradores 
    
    
    async def get_morador(self, id: str) -> Morador:
        response = self.cursor.execute(
            querys.select_morador_by_id(int(id))
        ).fetchone()
        
        if response is None:
            return None
        
        return new_from_db(response) 
    
    async def insert_visita(self, nome: str, data: str):
        self.cursor.execute("INSERT INTO visitas (nome, data) VALUES (?, ?)", (nome, data))
        self.connection.commit()

    async def get_visitas(self):
        self.cursor.execute("SELECT * FROM visitas")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
