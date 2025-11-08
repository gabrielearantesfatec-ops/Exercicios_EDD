def menu():
    print("\n=== MENU - MONTAGEM DO SANDUÍCHE ===")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche completo")
    print("5 - Finalizar pedido")

def main():
    pilha = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ingrediente = input("Digite o nome do ingrediente: ").strip()
            pilha.append(ingrediente)
            print(f"Ingrediente '{ingrediente}' adicionado ao sanduíche!")

        elif opcao == "2":
            if len(pilha) == 0:
                print("O sanduíche está vazio. Não há nada para remover. Adicione algo primeiro.")
            else:
                removido = pilha.pop()
                print(f"Ingrediente '{removido}' removido do topo do sanduíche.")

        elif opcao == "3":
            if len(pilha) == 0:
                print("O sanduíche está vazio.")
            else:
                print(f"O último ingrediente adicionado foi: {pilha[-1]}")

        elif opcao == "4":
            if len(pilha) == 0:
                print("O sanduíche está vazio.")
            else:
                print("\nSeu sanduíche (de baixo para o topo):")
                for i, ingrediente in enumerate(pilha):
                    print(f"{i + 1}. {ingrediente}")

        elif opcao == "5":
            print("\nPedido finalizado!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
