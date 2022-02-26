from scipy import optimize

roots = []


def f(x):
    return x ** 2 - 2 * x - 3


def find_solution():
    # if the function doesn't converge it will return a runtime error and the program will stop
    # Hence we are using a try and except block

    for guess in range(-100, 100):
        try:
            x0 = guess
            solution = round(optimize.newton(f, x0))

            if solution not in roots:
                roots.append(solution)


        except RuntimeError:
            print("No solution found")


if __name__ == "__main__":
    find_solution()

    print(roots)
