def collatz(number):
    if number % 2 == 0:
        print(number)
    if number & 2 == 1:
        print(3 * number + 1)


if __name__ == "__main__":
    collatz()