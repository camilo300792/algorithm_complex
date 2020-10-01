import time

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n - 1)


if __name__ == '__main__':

    n = 8
    start = time.time()
    factorial(n)
    end = time.time()
    print('Factorial execution end: ' + str(end - start))

    start = time.time()
    factorial_r(n)
    end = time.time()
    print('Factorial execution end: ' + str(end - start))

