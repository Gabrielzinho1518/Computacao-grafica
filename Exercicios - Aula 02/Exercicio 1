#Matrizes
A = [
    [1, 3, 2],
    [4, 7, 6]
]

B = [
    [2, 8],
    [3, 1],
    [5, 9]
]

# Função para imprimir matriz
def imprimir_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    for linha in matriz:
        print(linha)

# Verificação de compatibilidade
linhas_A = len(A)
colunas_A = len(A[0])

linhas_B = len(B)
colunas_B = len(B[0])

if colunas_A != linhas_B:
    print("Não é possível multiplicar as matrizes!")
else:
    # Criando matriz resultado (2x2 neste caso)
    C = []

    for i in range(linhas_A):
        linha_resultado = []
        for j in range(colunas_B):
            soma = 0
            for k in range(colunas_A):
                soma += A[i][k] * B[k][j]
            linha_resultado.append(soma)
        C.append(linha_resultado)

    # Impressão das matrizes
    imprimir_matriz(A, "A")
    imprimir_matriz(B, "B")
    imprimir_matriz(C, "Resultado (C)")
