from collections import deque

def menu():
    print("\n--- Biblioteca ---")
    print("1 - Adicionar Livro/Mangá")
    print("2 - Retirar Livro/Mangá")
    print("3 - Mostrar Biblioteca")
    print("4 - Sair")

def main():
    biblioteca = deque()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o Título do Livro/Mangá: ").strip()
            if titulo:
                biblioteca.append(titulo)
                print(f"{titulo} foi adicionado à Biblioteca.")
            else:
                print("Título inválido. Tente novamente.")

        elif opcao == "2":
            if biblioteca:
                retirar = biblioteca.popleft()
                print(f"{retirar} foi Retirado.")
            else:
                print("A Biblioteca está vazia. Não há oque ler. Adicione algo.")

        elif opcao == "3":
            if biblioteca:
                print("\nLivros/Mangás na Biblioteca:")
                for i, livro in enumerate(biblioteca, start=1):
                    print(f"{i}. {livro}")
            else:
                print("A Biblioteca está vazia. Não há oque ler. Adicione algo.")

        elif opcao == "4":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
