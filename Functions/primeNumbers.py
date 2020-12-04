

# ------------------------------
#2020-11-20
#Functions.primeNumbers
#ogracias
# ------------------------------


def isPrime(n):
    if n<= 1:
        return False
    for x in range(2, n):
        if (n % x == 0):
            return False
    else:
        return True
    
    
    
def listPrimes():
    for n in range(100):
        if isPrime(n):
            print(n)
    
    
    
if __name__ == '__main__':
    print(isPrime(5))
    listPrimes()