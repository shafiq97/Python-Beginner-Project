from random import randint

if __name__ == "__main__":

    while 1:
        print(f"Rolling dice: {randint(1, 6)}")
        again = input("Roll again? (y/n): ")
        if again == 'y' or again == 'Y':
            continue
        else:
            break
