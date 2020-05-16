from utils.isPrime import isPrime


def findPrime(max):
    for x in range(max, 3, -1):
        if(isPrime(x)):
            return x
