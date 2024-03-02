import numpy as np
A = np.array([3, 2, 5, 4, 1, 7])
min = 9999
M = np.array([0,0,0])
print(A)
for j in range(0,2):
    for i in range(0,A.size):
        if((A[i]<min) and (A[i]!=9999)):
            min=A[i]
    for i in range(0,A.size-1):
        if(A[i]==min):
            M[j] = i
            A[i]=9999
    min=9999
print(A)
print(M)