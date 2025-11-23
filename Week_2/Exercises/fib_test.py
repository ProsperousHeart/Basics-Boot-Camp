from fib import fib


def _main():

    fib_input = input("Please provide a number for fib output:\t")
    # print(fib(100))
    print(fib(int(fib_input)))  # assumes string is always an int


if __name__ == "__main__":
    _main()
