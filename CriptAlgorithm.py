def initial(data, mode, key):
    # data: stringa da criptare o decriptare
    # mode: 'e' per criptare, 'd' per decriptare
    # key: chiave per criptare o decriptare
    if mode == 'e':
        return encrypt(data,key)
    elif mode == 'd':
        return decrypt(data,key)
    else:
        return -1

def encrypt(data, key):
    e, n = key
    # cifra
    newdata = [pow(ord(c), e, n) for c in data]
    # converti da lista a stringa
    newdata = ' '.join(map(str, newdata))
    return newdata

def decrypt(data, key):
    d, n = key
    # converti da stringa a lista
    data = data.decode()
    data = list(map(int, data.split()))
    # decifra
    newdata = ''.join([chr(pow(c, d, n)) for c in data])
    return newdata