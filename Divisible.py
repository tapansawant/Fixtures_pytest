def checkDivisibleby5(x):
    if x % 5 == 0:
        return True
    else:
        return False


def checkDivisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False


def checkDivisibleby9(x):
    if x % 9 == 0:
        return True
    else:
        return False


def checkDivisibleby11(x):
    if x % 11 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter no:"))
    print(checkDivisibleby5(num))
    print(checkDivisibleby7(num))
    print(checkDivisibleby9(num))
    print(checkDivisibleby11(num))
