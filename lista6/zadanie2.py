from sys import exit
import numpy as np

def generate_system_of_equations(n):
    M = []
    b = []
    
    if n < 1:
        exit("n must be > 0")
    elif n == 1:
        M.append([4])
        b.append(100)
    else:
        for i in range(n):
            row = [0] * n
            row[i] = 4
            if i > 0:
                row[i-1] = -1
            if i < n-1:
                row[i+1] = -1
            M.append(row)
            
            b.append(0)
        
        M[0][n-1] = 1
        M[n-1][0] = 1
        b[n-1] = 100

    return np.array(M), np.array(b)

# K - liczba iteracji
def solve_Gauss_Seidl(M, b, x, n, K, epsilon): 
    for k in range(K):
        x_prev = list(x) # wartości z poprzedniej iteracji
        for i in range(n):
            suma = sum( [ M[i][j] * x[j] for j in range(n) if j != i ] )
            x[i] = ( b[i] - suma ) / M[i][i]
        if sum(x) - sum(x_prev) < epsilon:
            break
    
    return np.array(x), k


def main():
    n = 20
    M, b = generate_system_of_equations(n)    
    x = [0] * n
    x, k = solve_Gauss_Seidl(M, b, x, n, 100, 0.000001)
    
    print("n:", n)
    print("A\n",M)
    print("Liczba iteracji:", k)
    print("Wynik:")
    print(x)
    
main()
