from keyGenerator import charRelsGen, charKeysGen
from encryption import convertMessage, deconvertMessage, encodeLayerTwo, decodeLayerTwo

choice = int(input("Enter 1 to generate keys & rels\nEnter 2 to encrypt\nEnter 3 to decrypt\n"))
def menu(choice):
    if(choice == 1):
        try:
            r = int(input("\nEnter a key size: "))
            charRelsGen()
            charKeysGen(r)
        except:
            print("Not a number.")
    if(choice == 2):
        try:
            r = str(input("\nEnter a message to encode: "))
            r = convertMessage(r)
            encodeLayerTwo(r)
        except:
            print("Error")

    if(choice == 3):
        try:
            print("Message: "+deconvertMessage(decodeLayerTwo()))
        except:
            print("Error")
try:
    menu(choice)
except:
    while(choice != 1 and choice != 2 and choice != 3):
        choice = int(input("Enter 1 to generate keys & rels\nEnter 2 to encrypt\nEnter 3 to decrypt "))
    menu(choice)
    
