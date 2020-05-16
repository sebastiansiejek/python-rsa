from random import randint
from math import gcd as bltin_gcd
from fractions import gcd
from utils.findPrime import findPrime
from utils.isCoprime import isCoprime


class RSA:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.__findE()
        self.d = self.__findD()

    def __findE(self):
        e = 0
        while(isCoprime(e, self.phi) == False):
            e = randint(2, self.phi)
        return e

    def __findD(self):
        d = 0
        for i in range(3, self.phi):
            d = i
            if((self.e * d - 1) % self.phi is 0):
                return d
        return d

    def getPublicKey(self):
        return {
            'e': self.e,
            'n': self.n
        }

    def getPrivateKey(self):
        return {
            'd': self.d,
            'n': self.n
        }

    def encrypt(self, text):
        message = ''
        for s in text:
            message += chr(pow(ord(s), self.e) % self.n)
        return message

    def decrypt(self, encryptedText):
        message = ''
        for s in encryptedText:
            message += chr(pow(ord(s), self.d) % self.n)
        return message
