## FILE PRINCIPALE ###
 
# variabili globali
myIP = '0.0.0.0' # use your local IP
myPort = 8080 # decide the port to use
contatti = [] # contatto = [nome, ip, porta, public_key]

# recupero contatti da file
def recuperoContatti():
    contatti.clear()
    try:
        file = open('contatti.txt', 'r')
        for line in file:
            contatti.append(line.split())
        file.close()
    except FileNotFoundError:
        print('File contatti non trovato')
        print('Creazione di un nuovo file contatti')
        file = open('contatti.txt', 'w')
        file.close()
recuperoContatti()

# recupero chiavi da file
try:
    file = open('keys.txt', 'r')
    keys = file.readlines()
    myPrivateKey = tuple(map(int, keys[0].split()[1:]))
    myPublicKey = tuple(map(int, keys[1].split()[1:]))
    file.close()
except FileNotFoundError:
    print('File keys non trovato')
    print('Generazione di nuove chiavi')
    import KeyGenerator
    KeyGenerator.initial()
    file = open('keys.txt', 'r')
    keys = file.readlines()
    myPrivateKey = tuple(map(int, keys[0].split()[1:]))
    myPublicKey = tuple(map(int, keys[1].split()[1:]))
    file.close()

# funzione update contatti
def updateFromMod(c):
    global contatti
    contatti = c

def updateContactsFile():
    file = open('contatti.txt', 'w')
    for contatto in contatti:
        file.write(' '.join(contatto) + '\n')
    file.close()
    recuperoContatti()

# main

print('Benvenuto in ChatSecure!')
while True:
        print('Vuoi chattare con un contatto esistente o modificare i contatti?')
        print('1) Chattare con un contatto')
        print('2) Modificare i contatti')
        print('3) Esci')
        scelta = input()
        if scelta == '1':
            import chatHandler
            chatHandler.initial(contatti, myIP, myPort, myPrivateKey, myPublicKey)
        elif scelta == '2':
            import modificaContatti
            newContatti = modificaContatti.initial(contatti)
            updateFromMod(newContatti)
            updateContactsFile()
        elif scelta == '3':
            break
        else:
            print('Scelta non valida')
