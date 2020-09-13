import numbers as np
import os
import pyclbr

print("Desencryption method")

message = input("Enter your message : ")
clave = input("Enter your clave : ")

num = []
encrypt_message = []
encrypt_XOR = []
message=list(message)
clave=list(clave)


def permutacion(message):
    esPar = len(message) % 2
    if esPar == 1:
        num_veces = int(round(len(message) / 2,0))-1
        print(str(num_veces))
    else:
        num_veces = round(len(message) / 2)
    permutado = [None] * len(message)
    i=0
    j=0
    while i < num_veces:
            permutado[j] = message[j+1]
            permutado[j+1] = message[j]
            i+=1
            j+=2
    if esPar == 1:
        permutado[len(message)-1] = message[len(message)-1]
    return permutado

for i,el in enumerate(clave):
    num.append(ord(clave[i]))

print(num)
print(clave)
for i in range(8):

    print("Iteration " + str(i))
    print("message:" + str(message))


    #XOR
    for i, el in enumerate(message):
        encrypt_XOR.append(chr(ord(message[i]) ^ ord(clave[i%len(clave)])))

    encrypt_message = encrypt_XOR.copy()
    encrypt_XOR.clear()
    print("xor:" + str(encrypt_message))
    message = permutacion(message)
    encrypt_message.clear()
    print("permutacion:" + str(message))
    # Polyalphabetical rotation
    for i,el in enumerate(message):
        if(ord(message[i]) > 64 and ord(message[i]) < 91):
            encrypt_message.append(ord(message[i]) - num[i%len(num)])
            while encrypt_message[i] < 65:
                encrypt_message[i] = 91 - (65 - encrypt_message[i])
            encrypt_message[i] = chr(encrypt_message[i])

        elif(ord(message[i]) > 96 and ord(message[i]) < 123):
            encrypt_message.append(ord(message[i]) - num[i%len(num)])
            while encrypt_message[i] < 97:
                encrypt_message[i] = 123 - (97 - encrypt_message[i])
            encrypt_message[i] = chr(encrypt_message[i])

        else:
            encrypt_message.append(message[i])

    print("poly:" + str(encrypt_message))

    message.clear()
    message = encrypt_message.copy()
    encrypt_message.clear()

encrypt_message = message.copy()
#Final result
print("Desencrypted message: " + str(encrypt_message))
