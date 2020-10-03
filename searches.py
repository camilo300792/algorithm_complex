
def linear_search(needle, haystack):
    for key, value in enumerate(haystack):
        if value == needle:
            return key    
    return -1

def binary_serach(needle, haystack):
    left = 0
    right = len(haystack) - 1
    while (right >= left):
        index = (left + right) // 2
        if haystack[index] == needle:
            return index
        elif haystack[index] < needle:
            left = index + 1
        else:
            right = index - 1
    return -1

if __name__ == '__main__':

    target = int(input('Find your number: '))

    numbers = [i for i in range(3, 90) if i % 2 == 1]
    
    result = linear_search(needle=target, haystack=numbers)
    resultb = binary_serach(needle=target, haystack=numbers)

    if (resultb > -1):
        print('Number founded in %d position' % (resultb))
    else:
        print('Number not found')