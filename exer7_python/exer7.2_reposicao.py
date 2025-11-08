def menu():
    print("\nPote de Pringles virtual!")
    print("1 - Comer uma unidade de Pringles")
    print("2 - Mostrar Pringles restantes")
    print("3 - Sair")

def main():
    pringles = 100

    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            if pringles > 0:
                pringles -= 1
                print(f"Você comeu 1 Pringles. Restam {pringles} unidades.")
                if pringles == 0:
                    print("Suas Pringles acabaram! 😢 Vá comprar mais.")
            else:
                print("Você não tem mais Pringles. Vá comprar mais.")
        elif escolha == "2":
            print(f"Pringles restantes: {pringles}")
        elif escolha == "3":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida — escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()