print("Hello Github!")
def is_prime(x):
    if x == 2:
        return False
    for i in range(sqrt(x), x+1):
        if x == i:
            return False
    return True
