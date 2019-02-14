from newton_polynomial import Newton
import numpy as np

x = [20,21,23,24]
y = [65280,255,255,255]

poly = Newton(x, y)

C = poly.Cs

print(C)

x = list(map(lambda x: -1*x, x))

B = [
    [1,0,0,0],
    [x[0],1,0,0],
    [0,x[0],1,0],
    [0,-x[0],x[0]+x[2],1]
]

A = [
    [C[0],0,0,0],
    [0,C[1],0,0],
    [0,0,C[2],0],
    [0,0,0,C[3]],
]

A = np.matrix(A)

B = np.matrix(B)

C = np.matmul(A,B)

print(A)
print(B)

for i in range(len(C)):
    pass
    