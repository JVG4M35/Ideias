import numpy as np
from itertools import permutations

# Definindo a matriz
A = np.array([[1, 2, 3, 4],
              [2, 3, 4, 1],
              [1, 1, 1, 1],  # terceira linha é combinação linear das outras linhas
              [2, 3, 4, 1]])

# Definindo a função para calcular o determinante usando a fórmula de Leibniz
def determinant_leibniz(A):
    n = A.shape[0]
    perms = list(permutations(range(n)))
    sgn = lambda p: 1 if sum((p[j] > p[i]) for i in range(n) for j in range(i+1, n)) % 2 == 0 else -1
    det = sum(sgn(p) * np.prod([A[i, p[i]] for i in range(n)]) for p in perms)
    return det

# Calculando o determinante usando a fórmula de Leibniz
det_A = determinant_leibniz(A)

# Imprimindo o resultado
print("O determinante da matriz é:", det_A)
