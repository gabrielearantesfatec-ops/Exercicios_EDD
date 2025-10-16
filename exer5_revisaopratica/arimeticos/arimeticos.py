def main():
    try:
        a, b = map(int, input("Digite dois números inteiros").split())
    except Exception:
        print("Entrada inválida.")
        return

    soma = a + b
    sub = a - b
    mul = a * b
    div_int = a // b if b != 0 else None
    div_real = a / b if b != 0 else None
    resto = a % b if b != 0 else None
    media = (a + b) / 2.0

    print(f"\nsoma = {soma}\nsub = {sub}\nmul = {mul}\ndiv int = {div_int}\ndiv real = {div_real}\nresto = {resto}\nmedia = {media:.2f}")

if __name__ == "__main__":
    main()
