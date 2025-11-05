def main():
    try:
        a, b = map(int, input("Digite dois números inteiros (a b): ").split())
    except Exception:
        print("Entrada inválida.")
        return

    # Relacionais
    print("\n--- Relacionais ---")
    print("a > b ?", a > b)
    print("a == b ?", a == b)
    print("Ambos pares?", (a % 2 == 0 and b % 2 == 0))

    
if __name__ == "__main__":
    main()
