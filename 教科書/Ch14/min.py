from scipy.optimize import minimize_scalar

def f(x):
    return (2 * x ** 2 - 4 * x + 1)

# 找出最小值
res = minimize_scalar(f)
print("當x為{0}時，函數f(x)有最小值為{1}。".format(res.x, f(res.x)))