# Matriz já preenchida
A = [
    [2, 0, 0],
    [0, 3, 0],
    [0, 0, 5]
]

# Função para imprimir matriz
def imprimir_matriz(matriz):
    print("\nMatriz:")
    for linha in matriz:
        print(linha)

# Verificação
linhas = len(A)
colunas = len(A[0])

eh_identidade = True

# Verifica se é quadrada
if linhas != colunas:
    eh_identidade = False
else:
    for i in range(linhas):
        for j in range(colunas):
            if i == j:
                # Diagonal principal deve ser 1
                if A[i][j] != 1:
                    eh_identidade = False
                    break
            else:
                # Fora da diagonal deve ser 0
                if A[i][j] != 0:
                    eh_identidade = False
                    break
        if not eh_identidade:
            break

# Impressão
imprimir_matriz(A)

if eh_identidade:
    print("\nA matriz é IDENTIDADE.")
else:
    print("\nA matriz NÃO é identidade.")
