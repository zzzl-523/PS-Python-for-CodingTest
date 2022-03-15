import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1): # 제곱근까지만 판별하면 됨
        if x % i == 0:
            return False
    return True


print(is_prime_number(4))