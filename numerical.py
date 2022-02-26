from scipy import optimize


def f(x):
    return x ** 2 + 4 * x + 5


def find_solution():
    # if the function doesnt converge it will return a runtime error and the program will stop
    # Hence we are using a try and except block

    possible_guesses = [0, 1, 2, 10, 20, 30, 70, 100]  # list of possible guesses

    # I used a list of different guesses to try and find a solution because for a couple of random guesses it
    # returned no solution

    for guess in possible_guesses:

        try:
            x0 = guess
            solution = optimize.newton(f, x0)
            print("The solution is {}".format(solution))

        except RuntimeError:
            print("No solution found")


if __name__ == "__main__":
    find_solution()
