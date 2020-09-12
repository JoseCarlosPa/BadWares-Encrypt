

print("Desencryption method")

mssg = input("Enter your message : ")
key = input("Enter your key : ")
rotations = 4
numbs = []
encmssg = []
encmssgXOR = []
mssg=list(mssg)
key=list(key)


def permutation(mssg):
    pair = len(mssg) % 2
    if pair == 1:
        times = int(round(len(mssg) / 2,0))-1
        print(str(times))
    else:
        times = round(len(mssg) / 2)
    newarr = [None] * len(mssg)
    i=0
    j=0
    while i < times:
            newarr[j] = mssg[j+1]
            newarr[j+1] = mssg[j]
            i+=1
            j+=2
    if pair == 1:
        newarr[len(mssg)-1] = mssg[len(mssg)-1]
    return newarr

for i,el in enumerate(key):
    numbs.append(ord(key[i]))

print(numbs)
print(key)
for i in range(rotations):

    print("Iteration " + str(i))
    print("mssg:" + str(mssg))


    #XOR
    for i, el in enumerate(mssg):
        encmssgXOR.append(chr(ord(mssg[i]) ^ ord(key[i%len(key)])))

    encmssg = encmssgXOR.copy()
    encmssgXOR.clear()
    print("xor:" + str(encmssg))
    mssg = permutation(encmssg)
    encmssg.clear()
    print("permutation:" + str(mssg))
    # Polyalphabetical rotation
    for i,el in enumerate(mssg):
        if(ord(mssg[i]) > 64 and ord(mssg[i]) < 91):
            encmssg.append(ord(mssg[i]) - numbs[i%len(numbs)])
            while encmssg[i] < 65:
                encmssg[i] = 91 - (65 - encmssg[i])
            encmssg[i] = chr(encmssg[i])

        elif(ord(mssg[i]) > 96 and ord(mssg[i]) < 123):
            encmssg.append(ord(mssg[i]) - numbs[i%len(numbs)])
            while encmssg[i] < 97:
                encmssg[i] = 123 - (97 - encmssg[i])
            encmssg[i] = chr(encmssg[i])

        else:
            encmssg.append(mssg[i])

    print("poly:" + str(encmssg))

    mssg.clear()
    mssg = encmssg.copy()
    encmssg.clear()

encmssg = mssg.copy()
#Final result
print("Desencrypted message: " + str(encmssg))
