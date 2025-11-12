import random
from operator import truediv


def generateRandom(upper):
    """

    :param upper:
    :return: int
    """

    r = random.randint(1,upper)
    return r

def main():

    run = True
    number1 = generateRandom(5)
    number2 = generateRandom(5)
    result = number1 + number2
    while run:
        ans = input("What is " + str(number1) + " and " + str(number2) + "? ")

        if ans.isdigit():
            if int(ans) == result:
                print("Tama!")
                run = False
            else:
                print("Wrong! Try again!!")

        else:
            print("Answer must be a positive integer!")

times = 10

for x in range(times):
    main()