# Programa que mostra a tabuada de um número

try:
    a = int(input("Digite um número inteiro: "))
except ValueError:
    print("Entrada inválida.")
    exit()

print(f"\nTabela de {a}:")
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")
