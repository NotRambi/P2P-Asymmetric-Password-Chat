# codice necessario per generare la coppia di chiavi asimmetriche

import random

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def generatePrime():
    while True:
        p = random.randint(100, 1000)
        if isPrime(p):
            return p
        
def generateKey():
    p = generatePrime()
    q = generatePrime()
    n = p*q
    m = (p-1)*(q-1)
    e = random.randint(2, m)
    while True:
        if isPrime(e) and m % e != 0:
            break
        e = random.randint(2, m)
    d = 1
    while True:
        if (d*e) % m == 1:
            break
        d += 1
    return (e, n), (d, n)

def initial():
    public, private = generateKey()
    print('Chiave pubblica:', public)
    print('Chiave privata:', private)

    # Salva le chievi in un file
    file = open('keys.txt', 'w')
    file.write('PrivateKey: '+str(public[0]) + ' ' + str(public[1]) + '\n')
    file.write('PublicKey: '+str(private[0]) + ' ' + str(private[1]) + '\n')

if __name__ == '__main__':
    initial()