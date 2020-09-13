import numbers as np
import os
import pyclbr

# Mensaje de inicio
from typing import List

print("*************************")
print("*       Metodo ViV      *")
print("* BadWares - Actividad  *")
print("*************************")

# Inputs de Mensaje y clave:
message: str = input("Ingresa un mensaje>> ")
clave: str = input("Ingresa la calve (clave)>> ")

message = list(message)  # Separamos el mensaje en un arreglo
clave = list(clave)  # Separamos la calve en un arreglo

# Definicion de arreglos para guardado
encrypt_message = []
encrypt_XOR = []
num = []


# Funcion "Permutacion" que nos permite hacer las permutaciones en el mensaje
# @Input: Arreglo con mensaje
# @Output:  Saliad con mensaje permutado  a la derecha

def permutacion(message):
    esPar = len(message) % 2
    if esPar == 1:
        num_veces = int(round(len(message) / 2, 0)) - 1
        print(str(num_veces))
    else:
        num_veces = round(len(message) / 2)

    p1 = 0
    j = 0
    permutado = [None] * len(message)  # Instanciamos el permutado para poder agrgera X cantidad de caracteres
    while p1 < num_veces:
        permutado[j] = message[j + 1]  # Agrgar en primera posicion
        permutado[j + 1] = message[j]  # Agrgar en posicion proxima
        p1 += 1
        j += 2
    if esPar == 1:
        permutado[len(message) - 1] = message[len(message) - 1]  # Si ya esta permtutado agregamos el tamaño del mensaje
    return permutado


# ----- Fin de Funcion permutacion -------


for i, el in enumerate(clave):
    num.append(ord(clave[i]))

# Aplicacion de Rotacion Poliafabetica:
# Se puede mejorar de O(N2) a O(N)
for veces in range(8):

    rep: int
    for rep, poli in enumerate(message):
        if 64 < ord(message[rep]) < 91:  # 92 - 1 por regla de ultimo bit
            encrypt_message.append(ord(message[rep]) + num[rep % len(num)])
            while not encrypt_message[rep] <= 90:
                encrypt_message[rep] = 64 + (encrypt_message[rep] - 90)
            encrypt_message[rep] = chr(encrypt_message[rep])
        elif 96 < ord(message[rep]) < 123:
            encrypt_message.append(ord(message[rep]) + num[rep % len(num)])
            while not encrypt_message[rep] <= 122:
                encrypt_message[rep] = 96 + (encrypt_message[rep] - 122)
            encrypt_message[rep] = chr(encrypt_message[rep])
        else:
            encrypt_message.append(message[rep])

    print("Poliafabetico---->" + str(encrypt_message))
    print("***********************>>>>>")
    encrypt_message: List[None] = permutacion(encrypt_message)

    print("permutacion:" + str(encrypt_message))
    print("***********************>>>>>")

    # Uso del Primer XOR

    for xor, myxor in enumerate(encrypt_message):
        encrypt_XOR.append(chr(ord(encrypt_message[xor]) ^ ord(clave[xor % len(clave)])))

    # Fin de uso de XOR

    encrypt_message.clear()
    encrypt_message = encrypt_XOR.copy()
    encrypt_XOR.clear()
    message.clear()
    message = encrypt_message.copy()
    encrypt_message.clear()
    print("xor:" + str(message))
    print("***********************>>>>>")
encrypt_message = message.copy()

# Resultado de la encriptacion:
print("**************************************************")
print("Mensaje Encriptado: " + str(encrypt_message))
print("**************************************************")
