from scipy.optimize import root

def fun(x):
    return [2 * x[0] + x[1] - 5, x[0] - 3 * x[1] + 1]

sol = root(fun, [0, 0])
print(sol.x)