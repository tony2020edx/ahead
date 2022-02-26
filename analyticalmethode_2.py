from sympy import *

x = Symbol('x')

y = x ** 2 + 4 * x + 5

solution = solve(y, x)

print("The solution to the equation is {}".format(solution))
