import sympy as sm

lbd = sm.Symbol("lambda", positive = True)
mu = sm.Symbol("mu", positive = True)
rho = sm.Symbol("rho", positive = True)

l1 = [0 for i in range(9)]
l1[3] = l1[3] - 1/rho
l2 = [0 for i in range(9)]
l2[4] = l2[4] - 1/rho
l3 = [0 for i in range(9)]
l3[5] = l3[5] - 1/rho
l4 = [0 for i in range(9)]
l4[0] = l4[0] - 1 - 2*mu
l5 = [0 for i in range(9)]
l5[1] = l5[1] - mu
l6 = [0 for i in range(9)]
l6[2] = l6[2] - mu
l7 = [0 for i in range(9)]
l7[0] = -1
l8 = [0 for i in range(9)]
l9 = [0 for i in range(9)]
l9[0] = -1

A = sm.Matrix([l1, l2, l3, l4, l5, l6, l7, l8, l9])

B = A.eigenvals()
print(B)
