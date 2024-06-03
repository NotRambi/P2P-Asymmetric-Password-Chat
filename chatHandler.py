def initial(contacts , myIP, myPort, myPrivateKey, myPublicKey):
    if len(contacts) == 0:
        print('Nessun contatto presente')
        return
    print('Contatti attuali:')
    for contatto in contacts:
        print(contatto)
    print('Inserire il nome del contatto con cui chattare:')
    nome = input()
    if nome == '':
        return
    for contatto in contacts:
        if contatto[0] == nome:
            hisIP = contatto[1]
            hisPort = int(contatto[2])
            hisPublicKey = (int(contatto[3]), int(contatto[4]))
            import chat
            chat.initial(myIP, myPort, myPrivateKey, myPublicKey, hisIP, hisPort, hisPublicKey)
    print('Contatto inesistente')