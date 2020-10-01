def f(x):
    """
    X + 1 
    """
    for i in range(x): # x loops
        print(x % 2) # 1 Operation

def f2(x):
    """
    1 = 1
    """
    return x ** 2 # Zero loop 1 Operation

def f3(x):
    """
    X * X + 1 = X**2 + 1
    """
    for i in range(x): # x loops
        for j in range(x): # x loops
            print(i, j) # 1 Operation