from keyGenerator import charRelsGen, charKeysGen
from encryption import convertMessage, deconvertMessage, encodeLayerTwo, decodeLayerTwo
from datetime import datetime as dt
def menu(choice):
    if(choice == 1):
        try:
            print("\nProceeding by entering a key size will delete any key and relation values that currently exist.")
            r = int(input("Enter a key size: "))
            start = dt.now()
            charRelsGen()
            charKeysGen(r)
            end = dt.now()-start
            print('Elapsed time: ', end)
        except:
           print("Not a number.")
    if(choice == 2):
        try:
            print("\nMake sure you created your keys and relations first.")
            r = str(input("Enter a message to encode: "))
            start = dt.now()
            r = r.replace(" ", "_")
            r = convertMessage(r)
            encodeLayerTwo(r)
            end = dt.now()-start
            print('Elapsed time: ', end)
        except:
            print("Error")
    if(choice == 3):
        try:
            start = dt.now()
            r = deconvertMessage(decodeLayerTwo())
            r = r.replace("_", " ")
            print("Message: "+r)
            end = dt.now()-start
            print('Elapsed time: ', end)
        except:
            print("Error")
try:
    choice = int(input("Enter 1 to generate keys & rels\nEnter 2 to encrypt\nEnter 3 to decrypt "))
    acceptables = [1,2,3]
    while(choice not in acceptables):
        choice = int(input("Enter 1 to generate keys & rels\nEnter 2 to encrypt\nEnter 3 to decrypt "))
except:
    print("Not a number.")
menu(choice)
    
