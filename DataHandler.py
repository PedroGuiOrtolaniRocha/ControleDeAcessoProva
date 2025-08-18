import sqlite3
import Morador.morador_querys as morador_querys
from datetime import datetime
from Morador.model_morador import Morador
from Morador.model_morador import new_from_db, hash_senha


class DataHandler:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        
        self.cursor.execute(morador_querys.create_table_morador())
        
        self.connection.commit()

    async def insert_morador(self, morador: Morador) -> int:
        self.cursor.execute(
            morador_querys.insert_morador(morador)
        )
        self.connection.commit()
        return self.cursor.lastrowid 

    async def get_moradores(self) -> list [Morador]:
        response = self.cursor.execute(
            morador_querys.select_all_moradores()
        ).fetchall()

        moradores = []
        for m in response:
            moradores.append(new_from_db(m))
        
        return moradores 
    
    async def get_moradores_by_ap(self, apartamento: str) -> list[Morador]:

        response = self.cursor.execute(
            morador_querys.select_moradores_by_ap(apartamento)
        ).fetchall()
        
        print(f"SELECT * FROM moradores WHERE ap = {apartamento}")
        print(f"Response: {response}")

        moradores = []

        for row in response:
            moradores.append(new_from_db(row))
        
        return moradores
        
    async def get_morador(self, id: str) -> Morador:
        response = self.cursor.execute(
            morador_querys.select_morador_by_id(int(id))
        ).fetchone()
        
        if response is None:
            return None
        
        return new_from_db(response) 
    
    async def update_morador(self, morador: Morador) -> Morador:
        self.cursor.execute(
            morador_querys.update_morador(morador)
        )
        self.connection.commit()

        return await self.get_morador(str(morador.id))

    async def registro_entrada_saida(self, morador: Morador) -> Morador:
        
        if morador.em_casa:
            morador.registro_saida()

            self.cursor.execute(
                morador_querys.registro_saida(morador)
            )

                    
        else:
            morador.registro_entrada()
            self.cursor.execute(
                morador_querys.registro_entrada(morador)
            )


        self.connection.commit()

        return await self.get_morador(str(morador.id))

    async def registro_entrada_senha(self, ap: str, senha: str) -> Morador:
        
        moradores = await self.get_moradores_by_ap(ap)
        if not moradores:
            return None

        for morador in moradores:
            print(f"{morador.senha}\n{hash_senha(senha)}")
            if morador.senha == hash_senha(senha, 2):
                morador.registro_entrada()
                self.cursor.execute(
                    morador_querys.registro_entrada(morador)
                )
                self.connection.commit()
                return morador
        
        return None

    async def delete_morador(self, id: str):
        self.cursor.execute(
            morador_querys.delete_morador(int(id))
        )
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
