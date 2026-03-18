# Matriz original
A = [
    [4, 2, 8],
    [2, 0, 4],
    [1, 4, 7]
]

# Função para imprimir matriz
def imprimir_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    for linha in matriz:
        print(linha)

# Dimensões
linhas = len(A)
colunas = len(A[0])

# Criando matriz transposta (colunas viram linhas)
AT = []

for j in range(colunas):
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(A[i][j])
    AT.append(nova_linha)

# Impressão
imprimir_matriz(A, "A")
imprimir_matriz(AT, "A Transposta")
