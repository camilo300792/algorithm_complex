
def linear_search(needle, haystack):
    for key, value in enumerate(haystack):
        if value == needle:
            return key    
    return -1

if __name__ == '__main__':

    target = int(input('Find your number: '))

    numbers = [i for i in range(3, 90) if i % 2 == 1]
    
    result = linear_search(needle=target, haystack=numbers)
    resutlb = binary_serach(needle=target, haystack=numbers)

    if (result > -1):
        print('Number founded in %d position' % (result))
    else:
        print('Number not found')