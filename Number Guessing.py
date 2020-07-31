import random

if __name__ == '__main__':

    number = int(input("Guess and integer: "))
    ans = random.randint(50, 100)
    # print(ans)
    if ans % 2 == 0:
        isEven = True
    else:
        isEven = False

    while number > 100 or number < 50 or number != ans:
        print("Wrong answer guess again")

        if number > 100:
            print("Hint: number is less than 100")
        elif number < 50:
            print("Hint: number is more than 50")
        elif number != ans:
            print("Hint: Wrong number")
        if number % 2 == 0 and not isEven:
            print(f"Hint: Is the answer even? {isEven}")
        if number % 2 != 0 and isEven:
            print(f"Hint: Is the answer even? {isEven}")

        number = int(input("Guess and integer: "))

    print(f"Correct! Answer is {ans}")
