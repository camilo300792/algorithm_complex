import tyme

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

