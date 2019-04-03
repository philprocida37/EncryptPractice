import random, os

chars = list("!#$%&()*+,-./0123456789<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_abcdefghijklnopqrstuvwxyz") #<-- base set, 82 characters
# allow user to edit this set in UI (check for duplicates)

shuffles = 0
while(shuffles < 100):
    random.shuffle(chars)
    shuffles += 1

# second level (randomizer)
# generate relation table that is circular (any value can be reached from any other value)
# write to rels.txt ; overwrite existing rels (give warning)
def charRelsGen():
    switchBoard = []
    iters = 0
    while(iters <= len(chars)-1):
        if(iters == len(chars)-1):
            switchBoard.append([chars[iters], chars[0]])
            break
        nextIter = iters + 1
        switchBoard.append([chars[iters], chars[nextIter]]) #value, relation value
        iters += 1

    printRel = 0
    #print("switchBoard = {")
    if(os.stat("rels.txt").st_size != 0):
        exporter = open("rels.txt", "w")
        exporter.write("{")
        while(printRel < len(switchBoard)):
            exporter.write("\t\""+str(switchBoard[printRel][0]) + "\""+ ":\"" + str(switchBoard[printRel][1]) + "\", ")
            printRel += 1
        exporter.write("}")
        exporter.close()
    else:
        exporter = open("rels.txt", "a")
        exporter.write("{")
        while(printRel < len(switchBoard)):
            exporter.write("\t\""+str(switchBoard[printRel][0]) + "\""+ ":\"" + str(switchBoard[printRel][1]) + "\", ")
            printRel += 1
        exporter.write("}")
        exporter.close()

# for first level (char conversion)
# generate unique N length keys for every character value in the chars array
# write to keys.txt ; overwrite existing keys (give warning)
def charKeysGen(stringKeySize):
    exists = []
    charValues = []
    keyIter = 0
    while(keyIter < len(chars)):
        sizeIter = 0
        key = ""
        while(sizeIter < stringKeySize):
            randomIndex = random.randint(0, len(chars)-1)
            key = key + chars[randomIndex]
            sizeIter += 1
        if(key not in exists):
            charValues.append([chars[keyIter], key])
            exists.append(key)
            keyIter += 1
    print("Rels generated")
    
    printKeys = 0 # for conversion; layer one
    #print("charValue = {")
    if(os.stat("rels.txt").st_size != 0):
        exporter = open("keys.txt", "w")
        exporter.write("{")
        while(printKeys < len(charValues)):
            exporter.write("\t\""+str(charValues[printKeys][0]) + "\""+ ":\"" + str(charValues[printKeys][1]) + "\", ")
            printKeys += 1
        exporter.write("}")
        exporter.close()
    else:
        exporter = open("keys.txt", "a")
        exporter.write("{")
        while(printKeys < len(charValues)):
            exporter.write("\t\""+str(charValues[printKeys][0]) + "\""+ ":\"" + str(charValues[printKeys][1]) + "\", ")
            printKeys += 1
        exporter.write("}")
        exporter.close()
    print("Keys generate")
