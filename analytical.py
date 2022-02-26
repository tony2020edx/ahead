from sympy import *


x = Symbol('x')

y = x**2 - 2*x - 3

solution = solve(y, x)

print("The solution to the equation is {}".format(solution))
