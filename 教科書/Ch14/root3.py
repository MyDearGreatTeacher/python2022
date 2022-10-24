from scipy.optimize import root

def f(x):
    return (2 * x ** 2 - 4 * x + 1)

def g(x) :
    return (x - 2)

sol = root(lambda x : f(x) - g(x), 0)
print(sol.x)
print(f(sol.x))
print(g(sol.x))