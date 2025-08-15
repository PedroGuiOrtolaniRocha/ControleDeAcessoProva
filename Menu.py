import DataHandler
import os
import asyncio
from model_morador import Morador

dt_handler = DataHandler.DataHandler("PREDIO.db")

async def cadastro_morador():
    nome = input("Nome do morador: ")
    bloco = input("Bloco do morador: ")
    ap = int(input("Número do apartamento: "))
    senha = input("Senha do morador: ")
    morador = Morador(nome, bloco, ap, senha)
    await dt_handler.insert_morador(morador)
    print("Morador cadastrado com sucesso!")

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

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar morador")
        print("2. Listar moradores")
        print("3. Buscar morador por ID")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == "1":
            asyncio.run(cadastro_morador())
        elif opcao == "2":
            asyncio.run(listar_moradores())
        elif opcao == "3":
            asyncio.run(get_morador())
        elif opcao == "4":
            dt_handler.close_connection()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

        input("\n\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    menu()
