def fib(num):
    """"""
    result = []
    num1, num2 = 0, 1
    while num2 < num:
        result.append(num2)
        num1, num2 = num2, num1 + num2
    return result
