import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n = len(A)
    m = len(A[0])

    ans = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            ans[j][i] = A[i][j]

    return ans

