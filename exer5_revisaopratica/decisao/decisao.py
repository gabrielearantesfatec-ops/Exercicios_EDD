def main():
    try:
        a, b = map(int, input("Digite dois números inteiros (a b): ").split())
    except Exception:
        print("Entrada inválida.")
        return

    media = (a + b) / 2.0

    print("\n--- Decisão ---")
    if b == 0:
        print("b é zero (cuidado).")
    elif media >= 10.0:
        print("Média >= 10.0")
    else:
        print("Média < 10.0")

    
if __name__ == "__main__":
    main()
