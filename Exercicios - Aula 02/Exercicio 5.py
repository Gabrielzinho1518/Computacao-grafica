# matriz A
A = [
    [4, 8, 0],
    [2, 2, 4],
    [4, 5, 1]
]

x = 3  # escalar

# multiplicação
resultado = []

for linha in A:
    nova_linha = []
    for elemento in linha:
        nova_linha.append(elemento * x)
    resultado.append(nova_linha)

# saída
print("Matriz resultante:")
for linha in resultado:
    print(linha)
