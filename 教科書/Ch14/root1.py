from scipy.optimize import root

def f(x):
    return (2 * x ** 2 - 4 * x + 1)

sol1 = root(f, 0)
print(sol1.x)
sol2 = root(f, 1)
print(sol2.x)
sol3 = root(f, 2)
print(sol3.x)