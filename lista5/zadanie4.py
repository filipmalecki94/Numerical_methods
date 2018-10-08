import numpy as np

def gauss(A, b):
    n =  len(A)
    for k in range(n-1):
        maxIndex = abs(A[k:,k]).argmax() + k
        if A[maxIndex, k] == 0:
            b[[k,maxIndex]] = b[[maxIndex, k]]
        for row in range(k+1, n):
            multiplier = A[row][k]/A[k][k]
            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            b[row] = b[row] - multiplier*b[k]
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
a=np.array([[3.50,2.77,-0.76,1.80],
    [-1.80,2.68,3.44,-0.09],
    [0.27,5.07,6.90,1.61],
    [1.71,5.45,2.68,1.71]])

b=np.array([[7.31],[4.23],[13.85],[11.55]])

print(gauss(a,b))
