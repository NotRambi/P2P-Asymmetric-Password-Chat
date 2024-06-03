import socket
import threading
import CriptAlgorithm as cript

def sendMsg(s, myIP, myPort, hisIP, hisPort, hisPublicKey, myPublicKey):
    while True:
        msg = input()
        msgC = cript.initial(msg,'e', hisPublicKey)
        s.sendto(msgC.encode(), (hisIP, hisPort))
        if msg == 'exit':
            autoMsgC = cript.initial(msg,'e', myPublicKey)
            s.sendto(autoMsgC.encode(), (myIP, myPort))
            break
    
def recvMsg(s, myPrivateKey):
    while True:
        msg = s.recv(1024)
        msg = cript.initial(msg,'d', myPrivateKey)
        if msg == 'exit':
            print('$ Utente scollegato')
            break
        print('>',msg)

    
def initial(myIP, myPort, myPrivateKey, myPublicKey, hisIP, hisPort, hisPublicKey):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((myIP, myPort))
    print('$ Chat avviata')
    print('$ attesa collegamento...')
    s.sendto('connectionACK1'.encode(), (hisIP, hisPort))
    while True:
        s.settimeout(5)
        try:
            msg= s.recv(1024)
        except socket.timeout:
            print('$ Connessione non riuscita')
            s.close()
            return
        except socket.error:
            continue 
        if msg.decode() == 'connectionACK1':
            s.sendto('connectionACK2'.encode(), (hisIP, hisPort))
            break
        if msg.decode() == 'connectionACK2':
            break
    print('$ collegamento stabilito')
    s.settimeout(None)

    t1 = threading.Thread(target=sendMsg, args=(s, myIP, myPort, hisIP, hisPort, hisPublicKey, myPublicKey))
    t2 = threading.Thread(target=recvMsg, args=(s,myPrivateKey))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('$ Chat terminata')
    s.close()