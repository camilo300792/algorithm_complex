

if __name__ == '__main__':

    target = int(input('Find your number: '))

    numbers = [i for i in range(3, 90) if i % 2 == 1]
    
    linear_search(needle=target, haystack=numbers)