import random, os

try:
        testerKeys = open("keys.txt", "r")
        try:
                testerRels = open("rels.txt", "r")
                try:
                        testerMessage = open("message.txt", "r")
                        testerKeys.close()
                        testerRels.close()
                        testerMessage.close()

                        messageCoords = []
                        randomizedMessage = []
                        decodeCoords = []
                        mess = []
                        # read from rels.txt
                        switchBoard = eval(open("rels.txt").read())

                        # read from keys.txt
                        charValue = eval(open("keys.txt").read())

                        def convertMessage(message):
                                global mess
                                message = list(message)
                                iters = 0
                                while iters < len(message):
                                        n = charValue.get(message[iters], "")
                                        mess.append(n)
                                        iters += 1
                                return ''.join(mess)

                        def deconvertMessage(message):
                            size = len(next(iter(charValue.values())))
                            message = [message[i:i+size] for i in range(0, len(message), size)]
                            iters = 0
                            deConverted = []
                            while iters < len(message):
                                try:
                                        s = list(charValue.keys())[list(charValue.values()).index(message[iters])]
                                        deConverted.append(str(s))
                                        iters += 1
                                except:
                                        print("Oops, wrong key.")
                                        break
                            return ''.join(deConverted)


                        def switch(message):
                                if len(str(message)) > 1:
                                        print("Value too large.")
                                        return None
                                return switchBoard.get(message, "")

                        def reverseLookUp(message):
                                try:
                                        return list(switchBoard.keys())[list(switchBoard.values()).index(message)]
                                except:
                                        return print("Oops, wrong key.")

                        def encodeLayerTwo(message):
                                # write to message.txt
                                iters = 0
                                global randomizedMessage
                                global decodeCoords
                                global messageCoords
                                message = list(message)
                                while iters < len(message):
                                    try:
                                        uIn = message[iters]
                                    except:
                                        print("Error")
                                        break
                                    y = random.randint(1, 100)
                                    i = 0
                                    try:
                                        x = switch(uIn)
                                    except:
                                        break
                                    while i < y:
                                        x = switch(x)
                                        i += 1
                                    messageCoords.append([i, x]) # write this to message.txt, each coord has a line
                                    coordsIter = 0
                                    exporter = open("message.txt", "w")
                                    while(coordsIter < len(messageCoords)):
                                        exporter.write(str(messageCoords[coordsIter][0])+" "+str(messageCoords[coordsIter][1]) + "\n")
                                        coordsIter += 1
                                    exporter.close()
                                    iters += 1
                                print("Message generated.")

                        def decodeLayerTwo():
                                # read from message.txt ; remove input requirement for function
                                # scan each line from message.txt, placing it into the gatheredMess array at the appropriate index
                                gatherMess = []
                                with open("message.txt", "r") as importer:
                                        for line in importer:
                                                splitLineItems = line.split()
                                                gatherMess.append([int(splitLineItems[0]), splitLineItems[1]])
                                returnMessage = []
                                numRev = 0
                                mainArr = 0
                                while mainArr < len(gatherMess):
                                        numRev = gatherMess[mainArr][1]
                                        iters = 0
                                        while iters < gatherMess[mainArr][0]+1:
                                                prev = numRev
                                                numRev = reverseLookUp(str(numRev))
                                                iters += 1
                                        returnMessage.append(str(numRev))
                                        mainArr += 1
                                return ''.join(returnMessage)
                        # Generate keys and rels, input message --> Encryption
                        # Use keys, rels, and coords --> Decryption
                                # Encryption: convertMessage --> encodeLayerTwo
                                # Decryption: decodeLayerTwo --> deconvertMessage               
                except:
                        print("message file not found")
        except:
                print("rels file not found")
except:
        print("keys file not found")

