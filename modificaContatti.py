def initial(contatti):
    contacts = contatti
    startMod(contacts)
    return contacts

def startMod(contacts):
    while True:
        printContacts(contacts)
        print('Modificare un contatto esistente, eliminarlo o aggiungerne uno nuovo?')
        print('1) Modifica un contatto esistente')
        print('2) Elimina un contatto esistente')
        print('3) Aggiungi un nuovo contatto')
        print('4) Esci')
        scelta = input()
        if scelta == '1':
            ret = modificaContatti(contacts)
            if ret == -1:
                print('Nessun contatto modificato')
        elif scelta == '2':
            ret = removeContact(contacts)
            if ret == -1:
                print('Nessun contatto rimosso')
        elif scelta == '3':
            ret = addContact(contacts)
            if ret == -1:
                print('Nessun contatto aggiunto, inserire tutti i campi')
        elif scelta == '4':
            print('Modifica contatti terminata')
            return
        else:
            print('Scelta non valida')

def printContacts(contacts):
    if len(contacts) == 0:
        print('Nessun contatto presente')
        return
    print('Contatti attuali:')
    for contatto in contacts:
        print(contatto)

def modificaContatti(contacts):
    print('Inserire il nome del contatto da modificare:')
    oldname = input()
    if oldname == '':
        return -1
    for contatto in contacts:
        if contatto[0] == oldname:
            print('Inserire il nuovo nome:')
            nome = input()
            if nome == '':
                nome = contatto[0]
            print('Inserire il nuovo ip:')
            ip = input()
            if ip == '':
                ip = contatto[1]
            print('Inserire la nuova porta:')
            porta = input()
            if porta == '':
                porta = contatto[2]
            print('Inserire la nuova chiave pubblica:')
            public_key = input()
            if public_key == '':
                public_key = contatto[3]
            contacts.insert(contacts.index(contatto), [nome, ip, porta, public_key])
            contacts.remove(contatto)
            print('Contatto modificato con successo')
            return 0
    print('Contatto non trovato')
    return 0

def addContact(contacts):
    print('Inserire il nome del nuovo contatto:')
    nome = input()
    if nome == '':
        return -1
    print('Inserire l\'ip del nuovo contatto:')
    ip = input()
    if ip == '':
        return -1
    print('Inserire la porta del nuovo contatto:')
    porta = input()
    if porta == '':
        return -1
    print('Inserire la chiave pubblica del nuovo contatto:')
    public_key = input()
    if public_key == '':
        return -1
    contacts.append([nome, ip, porta, public_key])
    print('Contatto aggiunto con successo')
    return 0

def removeContact(contacts):
    print('Inserire il nome del contatto da rimuovere:')
    nome = input()
    if nome == '':
        return -1
    for contatto in contacts:
        if contatto[0] == nome:
            contacts.remove(contatto)
            print('Contatto rimosso con successo')
            return 0
    print('Contatto non trovato')
    return 0