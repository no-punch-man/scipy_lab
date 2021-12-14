import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.integrate import odeint

#scipy
def dydx(y, x):
    return -y*2

x_sc = np.linspace(0, 10, 100)
y0 = 2**0.5
y_sc = np.array(odeint(dydx, y0, x_sc)).ravel()


fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.set_figheight(7)
fig.set_figwidth(14)
ax1.grid(True)
ax1.plot(x_sc, y_sc)
ax1.set_title("scipy")

#sympy
x = sp.Symbol("x", positive = True)
y = sp.Function("y")

dif = sp.Eq(y(x).diff(x) + 2*y(x), 0)
res = sp.dsolve(dif, ics = {y(0): y0}).rhs
f = sp.lambdify(x, res, 'numpy')

ax2.grid(True)
ax2.plot(x_sc, f(x_sc), 'r')
ax2.set_title("sympy")

ax3.grid(True)
ax3.plot(x_sc, f(x_sc) - y_sc, 'r', color = 'cornflowerblue')
ax3.set_title("delta")

fig.savefig("num3" + ".png")

