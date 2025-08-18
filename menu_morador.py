import DataHandler
import os
from Morador.model_morador import Morador

dt_handler = DataHandler.DataHandler("PREDIO.db")

async def cadastro_morador():
    nome = input("Nome do morador: ")
    bloco = input("Bloco do morador: ")
    ap = int(input("Número do apartamento: "))
    senha = input("Senha do morador: ")
    morador = Morador(nome, bloco, ap, senha)
    await dt_handler.insert_morador(morador)
    print("Morador cadastrado com sucesso!")

async def registro_entrada_saida():
    id = input("ID do morador: ")
    morador = await dt_handler.get_morador(id)

    if morador is None:
        print("Morador não encontrado.")
        return

    morador = await dt_handler.registro_entrada_saida(morador)
    if morador.em_casa:
        print(f"Morador {morador.nome} registrou entrada.")
    else:
        print(f"Morador {morador.nome} registrou saída.")

async def listar_moradores_apartamento():
    apartamento = input("Número do apartamento: ")
    moradores = await dt_handler.get_moradores_by_ap(apartamento)

    if not moradores:
        print("Nenhum morador encontrado para o apartamento especificado.")
        return

    print(f"Moradores do apartamento {apartamento}:")
    for morador in moradores:
        print(f"ID: {morador.id}, Nome: {morador.nome}, Bloco: {morador.bloco}, Ap: {morador.ap}, Em casa: {morador.em_casa}, Data de entrada: {morador.data_entrada}, Data de saída: {morador.data_saida}, Data de cadastro: {morador.data_cadastro}\n")

async def registro_entrada_senha():
    apartamento = input("Número do apartamento: ")
    senha = input("Senha do morador: ")
    acesso = await dt_handler.registro_entrada_senha(apartamento, senha)

    if acesso is not None:
        print(f"Acesso permitido, registrando entrada para o morador {acesso.nome}.")
    else:
        print("Acesso negado, senha incorreta ou morador não encontrado.")

async def listar_moradores():
    moradores = await dt_handler.get_moradores()
    if not moradores:
        print("Nenhum morador cadastrado.")
    else:
        print("Moradores cadastrados:")
        for morador in moradores:
            print(f"ID: {morador.id}, \nNome: {morador.nome}, \nBloco: {morador.bloco}, \nAp: {morador.ap}, \nEm casa: {morador.em_casa}, \nData de entrada: {morador.data_entrada}, \nData de saída: {morador.data_saida}, \nData de cadastro: {morador.data_cadastro}\n\n")

async def get_morador():

    id = input("ID do morador: ")
    morador = await dt_handler.get_morador(id)

    if morador is None:
        print("Morador não encontrado.")

    else:
        print(f"ID: {morador.id}, \nNome: {morador.nome}, \nBloco: {morador.bloco}, \nAp: {morador.ap}, \nEm casa: {morador.em_casa}, \nData de entrada: {morador.data_entrada}, \nData de saída: {morador.data_saida}, \nData de cadastro: {morador.data_cadastro}\n\n")

async def delete_morador():
    id = int(input('Id do morador a ser deletado: '))
    morador = await dt_handler.get_morador(id)

    if morador == None:
        print('Morador não encontrado')
        return None

    os.system('cls' if os.name == 'nt' else 'clear')
    confirm = input('Morador a ser excluido:\n' + morador.__dict__['nome'] + '\nDeseja proseeguir? S|N').capitalize()
    
    while confirm != 'S' and confirm != 'N':
        os.system('cls' if os.name == 'nt' else 'clear')
        confirm = input('Opção inválida!\n\nMorador a ser excluido:\n' + morador.__dict__['nome'] + '\nDeseja proseeguir? S|N\n')

    if confirm == 'S': 
        await dt_handler.delete_morador(id)
        print('Morador excluido com sucesso!')