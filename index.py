from RSA import RSA
from utils.findPrime import findPrime
from utils.randomString import randomString

# 1
p = findPrime(999)
q = findPrime(888)

# 2
rsa = RSA(p, q)
publicKey = rsa.getPublicKey()
privateKey = rsa.getPrivateKey()

# 3
message = randomString(50)
print('message:', message)

# 4
encryptedMessage = rsa.encrypt(message)
print('encrypt:', encryptedMessage)

# 5
decryptedMessage = rsa.decrypt(encryptedMessage)
print('decrypt:', decryptedMessage)
