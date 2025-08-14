import sqlite3
import Morador

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

    def insert_morador(self, morador: Morador):
        self.cursor.execute("INSERT INTO moradores (nome, bloco, ap, senha) VALUES (?, ?, ?, ?)", (morador.nome , morador.bloco, morador.ap, morador.senha))
        self.connection.commit()
    
    def fetch_moradores(self):
        self.cursor.execute("SELECT * FROM moradores")
        return self.cursor.fetchall()
    
    def insert_visita(self, nome: str, data: str):
        self.cursor.execute("INSERT INTO visitas (nome, data) VALUES (?, ?)", (nome, data))
        self.connection.commit()

    def fetch_visitas(self):
        self.cursor.execute("SELECT * FROM visitas")
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
