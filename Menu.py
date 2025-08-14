import DataHandler
import Morador

def cadastro_morador():

    nome = input("Nome do morador: ")
    bloco = input("Bloco do morador: ")
    ap = int(input("Número do apartamento: "))
    senha = input("Senha do morador: ")

    morador = Morador.Morador(nome, bloco, ap, senha)
    dt_handler.insert_morador(morador)

    return morador

dt_handler = DataHandler.DataHandler("PREDIO.db")

cadastro_morador()
print(dt_handler.fetch_moradores())


dt_handler.close_connection()

