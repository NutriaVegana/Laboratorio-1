#Laboratorio 1
#Jorge Arenas
#Diego Palma
#Sebastian Lucero

import requests
def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)

        alfabeto_a_usar = alfabeto
        limite = 97  
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        codificado += alfabeto_a_usar[posicion]
    return codificado


def decodificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)

        alfabeto_a_usar = alfabeto
        
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto

        decodificado += alfabeto_a_usar[posicion]
    return decodificado

LETRAS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def vigenere(mensaje,accion,myKey):

    if accion==1:
        traducido=cifrar_mensaje(myKey,mensaje)
    elif accion==2:
        traducido=descifrar_mensaje(myKey,mensaje)
    return traducido

def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'encriptar')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'descifrar')

def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)


x=int(input("[1] Subir cifrado (desafio 1)\n[2]Descargar cifrado (desafio 2)\n[3]Salir\nIngrese una opción: "))
if(x==1):
    key="HEROPASSWORD"
    mensaje = input("Ingrese una cadena: ")
    mensaje=mensaje.upper()
    print("El mensaje original es: ", mensaje)
    codificado = codificar(mensaje,8)
    codificado = vigenere(codificado,1,key)
    codificado = codificar(codificado,12)
    print("Codificado es: ", codificado)
    decodificado = decodificar(codificado,12)
    decodificado = vigenere(decodificado,2,key)
    decodificado = decodificar(decodificado,8)
    print("Decodificado es: ", decodificado)
    headers={'Content-Type': 'text/plain'}
    data='{"msg":"'+codificado+'"}'
    response=requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)
    
elif(x==2):
    key="FINISPASSWD"
    headers={'Content-Type': 'text/plain'}
    response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)
    mensaje = response.json()
    print(mensaje['msg'].upper())
    msg=mensaje['msg'].upper()
    decodificado = decodificar(msg,12)
    decodificado = vigenere(decodificado,2,key)
    decodificado = decodificar(decodificado,8)
    print("Mensaje decodificado: "+decodificado)
    
else:
    print("muchas gracias!")
    
