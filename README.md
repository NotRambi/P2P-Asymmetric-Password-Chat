# P2P-Asymmetric-Password-Chat
## How to use
Download this repo on two different machines, through the zip file or using git clone:

`git clone https://github.com/NotRambi/P2P-Asymmetric-Password-Chat.git`

Now edit the [main.py](main.py) file, changing:
1. myIP with the local IP of the host.
you can see it using `hostname -I` or `ip addr`
2. myPort to one chosen arbitrarily.

Run main.py the first time to generate the txt file,

copy from the [keys.txt]() file your PublicKey to use on the second host.

Now rerun main.py and navigate to the Contacts modification page to add a second host to communicate with,
choose a name, use the IP of the second host and the Port used in his main.py file.
Lastly, specify the PublicKey generated in the key.txt of the second host.

## Documentation
- [main.py](main.py)
  - is the program's core, it lets you navigate between the various pages;
  - also, generate the Txt files and use them;
- [modificaContatti.py](modificaContatti.py)
  - is the section where you can add a new contact, or modify or remove an existing one.
- [KeyGenerator.py](KeyGenerator.py)
  - is the algorithm that generates the PrivateKey and the PublicKey.
- [chatHandler.py](chatHandler.py)
  - this script reads the information about the contact and runs the chat.
- [chat.py](chat.py)
  - is the file that handles the Chat with another host, it creates two threads one for sending the messages and one for receiving them.
- [CriptAlgorithm.py](CriptAlgorithm.py)
  - this script, called by chat.py, encrypts the data using the PublicKey of the other host or decrypts the data with the PrivateKey of the local host before sending  or after receiving the messages.

## Credit
made by NotRambi, free to use 
