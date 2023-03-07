def add(num1, num2):
    """

    :param num1: Number 1 for the addition operation
    :param num2: Number 2 for the addition operation
    :return: Addition of two number + 13 to it.
    """
    return num1 + num2 + 13


def WelcomeMsg():
    print("hello Message , Welcome U All")


print("Value of __main__", __name__)
if __name__ == '__main__':
    print(add(23, 45))
    # Calling add function
    print(add(23, 109))
    #Calling the documentation format of add method.
    print(add.__doc__)
    print("What's the tempaerature today??")
    print("I am in Banglaore, it's a pleasent weather")
    print("hope you all are doing well")
    print(WelcomeMsg())
