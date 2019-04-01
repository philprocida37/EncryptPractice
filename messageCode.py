
import random
messageCoords = []
randomizedMessage = []
decodeCoords = []
mess = []
switchBoard = {
			0 : "9",
			1 : "7",
			2 : "5",
			3 : "0",
			4 : "3",
			5 : "1",
			6 : "2",
			7 : "4",
			8 : "6",
			9 : "8"
		}
charValue = {
			"a" : "7415", "A" : "7301", "0" : "6503",
			"b" : "4606", "B" : "7872", "1" : "2308",
			"C" : "9791", "C" : "6586", "2" : "1946",
			"d" : "4758", "D" : "2821", "3" : "3453",
			"e" : "4982", "E" : "4676", "4" : "6873",
			"f" : "1331", "F" : "1140", "5" : "3979",
			"g" : "7022", "G" : "6633", "6" : "4756",
			"h" : "7222", "H" : "8516", "7" : "4882",
			"i" : "9429", "I" : "3248", "8" : "4624",
			"j" : "5112", "J" : "4644", "9" : "3687",
			"k" : "7717", "K" : "8660", "!" : "2134",
			"l" : "4361", "L" : "7328", "@" : "8670",
			"m" : "8862", "M" : "7892", "#" : "1865",
			"n" : "4553", "N" : "2485", "$" : "4649",
			"o" : "8246", "O" : "2804", "%" : "3183",
			"p" : "3044", "P" : "3353", "^" : "7654",
			"q" : "5794", "Q" : "3745", "&" : "7151",
			"r" : "2223", "R" : "8465", "*" : "5571",
			"s" : "9926", "S" : "1168", ")" : "7111",
			"t" : "6733", "T" : "6614", "(" : "8764",
			"u" : "4813", "U" : "5533", ">" : "2636",
			"v" : "8226", "V" : "1263", "<" : "5559",
			"w" : "4952", "W" : "2600", "/" : "8622",
			"x" : "1205", "X" : "1525", "," : "6159",
			"y" : "8342", "Y" : "3425", " " : "9482", #space value is a weakness, should remove
			"z" : "3571", "Z" : "1913"
}

def convertMessage(message):
	global mess
	message = list(message)
	iters = 0
	while iters < len(message):
		n = charValue.get(message[iters], "")
		mess.append(n)
		iters += 1
	return ''.join(mess)

def deConvert(message):
    size = 4
    message = [message[i:i+size] for i in range(0, len(message), size)]
    iters = 0
    deConverted = []
    while iters < len(message)/2:
        s = list(charValue.keys())[list(charValue.values()).index(message[iters])]
        deConverted.append(s)
        iters += 1
    return ''.join(deConverted)


def switch(message):
		if len(str(message)) > 1:
			print("Value too large.")
			return None
		return switchBoard.get(message, "")

def reverseLookUp(message):
	return list(switchBoard.keys())[list(switchBoard.values()).index(message)]

def encodeLayerTwo(message):
	iters = 0
	global randomizedMessage
	global decodeCoords
	global messageCoords
	message = list(message)
	while iters < len(message):
		try:
			uIn = int(message[iters])
		except:
			print("Error")
			break

		y = random.randint(1, 250)
		i = 0
		try:
			x = int(switch(uIn))
		except:
			break
		while i < y:
			x = int(switch(x))
			i += 1
		messageCoords.append([i, x])
		randomizedMessage.append(str(x))
		decodeCoords.append(i)
		iters += 1
	return messageCoords

def decodeLayerTwo(message):
	returnMessage = []
	numRev = 0
	mainArr = 0
	while mainArr < len(message):
		numRev = message[mainArr][1]
		iters = 0
		while iters < message[mainArr][0]+1:
			prev = numRev
			numRev = reverseLookUp(str(numRev))
			iters += 1
		returnMessage.append(str(numRev))
		mainArr += 1
	return ''.join(returnMessage)

y = str(input("Enter a message to encrypt: "))
n = convertMessage(y)
print("Converted message; layer one: \n\t"+str(convertMessage(y)))
m = encodeLayerTwo(n)
print("Encoding message; layer two: \n\t"+str(encodeLayerTwo(n)))
o = ''.join(randomizedMessage)
print("Encrpyted message: \n\t"+o)
p = decodeLayerTwo(m)
print("Decocding message; layer two: \n\t"+str(decodeLayerTwo(m)))
print("De-converting message; layer one: \n\t"+str(deConvert(p)))
