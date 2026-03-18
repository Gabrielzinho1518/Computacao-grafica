# Matriz já preenchida
A = [
    [2, 0, 0],
    [0, 1, 0],
    [0, 0, 7]]

def imprimir_matriz(matriz):
    print("\nMatriz:")
    for linha in matriz:
        print(linha)

# Verificar se é quadrada
linhas = len(A)
colunas = len(A[0])

eh_diagonal = True

if linhas != colunas:
    eh_diagonal = False
else:
  # Verificar elementos fora da diagonal
    for i in range(linhas):
        for j in range(colunas):
            if i != j and A[i][j] != 0:
                eh_diagonal = False
                break
        if not eh_diagonal:
            break

# Impressão
imprimir_matriz(A)

if eh_diagonal:
    print("\nA matriz é DIAGONAL.")
else:
    print("\nA matriz NÃO é diagonal.")
