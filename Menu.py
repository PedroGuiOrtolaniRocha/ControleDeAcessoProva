import os
import asyncio
import menu_morador

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar morador")
        print("2. Listar moradores")
        print("3. Buscar morador por ID")
        print("4. Deletar morador")
        print("5. Registrar entrada/saída")
        print("6. Registrar entrada por senha")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == "1":
            asyncio.run(menu_morador.cadastro_morador())
        elif opcao == "2":
            asyncio.run(menu_morador.listar_moradores())
        elif opcao == "3":
            asyncio.run(menu_morador.get_morador())
        elif opcao == "4":
            asyncio.run(menu_morador.delete_morador())
        elif opcao == "5":
            asyncio.run(menu_morador.registro_entrada_saida())
        elif opcao == "6":
            asyncio.run(menu_morador.registro_entrada_senha())    
        elif opcao == "7":
            menu_morador.dt_handler.close_connection()
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

        input("\n\nPressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    menu()
