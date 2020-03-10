# Math ops
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def exp(n, p):
    return n ** p


# Prompt to get operation from user
def getOperation():
    print(
        "Enter an operation to begin -> '*' - mult | '/' - div | '+' add | '-' sub | '**' exp"
    )
    return input()


# Prompt to get terms from user, only supports 2 currently
def getTerms():
    print("Enter the first term")
    t1 = float(input())
    print("Enter the second term")
    t2 = float(input())

    return [t1, t2]


# Func to calculate based on operation, returns result
def calc(operation, num1, num2):
    ops = {
        "*": mul(num1, num2),
        "/": div(num1, num2),
        "+": add(num1, num2),
        "-": sub(num1, num2),
        "**": exp(num1, num2),
    }

    result = ops.get(operation, lambda: "Invalid operation")

    print("Result: {}".format(result))


# Main func to show prompts & results + a start over handler
def mainMenu():
    op = getOperation()
    terms = getTerms()

    print(f"Operation {op}, term A {terms[0]}, term B {terms[1]}")

    calc(op, terms[0], terms[1])

    print("Start over? [Y]es | [N]o")

    restart = input()

    mainMenu() if restart == "Y" or restart == "y" else exit()


mainMenu()
