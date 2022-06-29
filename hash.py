import base64
import hashlib
import math
import time

def read(path):
    texto = []
    df = open(path, "r")
    lines = df.readlines()
    for line in lines:
        print(line)
        texto.append(line.split("\n")[0])
    df.close()
    return texto

def hash(texto):
    A = "Lorem ipsum dolor sit amet, consectetur adipiscing nec."
    string = ""
    if(len(texto) <=55):
        falta = 55 - len(texto)
        verificar = True
        cont = 0
        while(verificar):
            cont +=1
            if(len(string) < 55):
                string += str(falta) + texto
            else:
                verificar = False

        binario = int.from_bytes(string.encode(), 'big')
        binario2 = int.from_bytes(A.encode(), 'big')
        binario3 = bin(binario ^ binario2)
        n = int(binario3, 2)
        ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        ascii = rotate(ascii,int(falta*100/3),True)

        # Transformar base ascii a base64
        message_bytes = ascii.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        
        final = base64_message[len(base64_message)-55:]

    else:
        sobra = len(texto) - 55
        aux = texto[55:]
        aux2 = ""
        verificar = True
        for i in range(len(aux)):
            if(len(aux2) < 55):
                aux2 += str(i*sobra) + aux[i]
            else:
                verificar = False
        binario = int.from_bytes(texto.encode(), 'big')
        binario2 = int.from_bytes(aux2.encode(), 'big')
        binario3 = int.from_bytes(A.encode(), 'big')
        binario4 = int(binario ^ binario2)
        binario5 = bin(binario4 ^ binario3)

        n = int(binario5, 2)
        ascii = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        ascii = rotate(ascii,int(sobra*100/3),False)
        # Transformar base ascii a base64
        message_bytes = ascii.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        final = base64_message[len(base64_message)-55:]

    print("Mihash es: " + final)
    entropia(texto)

def rotate(input,n,d):
    if d:
        Lfirst = input[0 : n]
        Lsecond = input[n :]
        return Lsecond + Lfirst
    else:
        Rsecond = input[len(input)-n : ]
        Rfirst = input[0 : len(input)-n]
        return Rsecond + Rfirst

#la entropia se calcula como el largo de la palabra ingresada por el logaritmo en base 2 de la base utilizada:
def entropia(texto):
    entropia =55*math.log(256,2)
    print("La entropia es: " + str(entropia))

def mihash(texto):
    start = time.time()
    hash(texto)
    end = time.time()
    print("Tiempo de mihash : " + str(end-start) + "\n")
    

def md5(texto):
    start = time.time()

    md5 = hashlib.md5(texto.encode())
    entropia = 32*math.log(16,2)

    print("MD5 es: " + md5.hexdigest())
    print("Entropia MD5 es: " + str(entropia))

    end = time.time()
    print("Tiempo de MD5 : " + str(end-start) + "\n")


def sha1(texto):
    start = time.time()

    sha1 = hashlib.sha1(texto.encode())
    entropia = 40*math.log(16,2)

    print("SHA1 es: " + sha1.hexdigest())
    print("Entropia SHA1 es: " + str(entropia))

    end = time.time()
    print("Tiempo de SHA1 : " + str(end-start) + "\n")


def sha256(texto):
    start = time.time()

    sha256 = hashlib.sha256(texto.encode())
    entropia = 64*math.log(16,2)

    print("SHA256 es: " + sha256.hexdigest())
    print("Entropia SHA256 es: " + str(entropia))

    end = time.time()
    print("Tiempo de SHA256 : " + str(end-start) + "\n")

def cadena(palabras):
    largo = len(palabras)
    start = time.time()
    for palabra in palabras:
        mihash(palabra)
    end = time.time()
    print("Tiempo de cadena " +str(largo)+ " con mihash : " + str(end-start) + "\n")

    start = time.time()
    for palabra in palabras:
        md5(palabra)
    end = time.time()
    print("Tiempo de cadena " +str(largo)+ " con md5 : " + str(end-start) + "\n")

    start = time.time()
    for palabra in palabras:
        sha1(palabra)
    end = time.time()
    print("Tiempo de cadena " +str(largo)+ " con sha1 : " + str(end-start) + "\n")

    start = time.time()
    for palabra in palabras:
        sha256(palabra)
    end = time.time()
    print("Tiempo de cadena " +str(largo)+ " con sha256 : " + str(end-start) + "\n")

def hashFile(path):
    with open(path, 'rb') as f:
        content = f.read()
        print("\n")
        mihash(str(content))
        md5(str(content))
        sha1(str(content))
        sha256(str(content))

def main():
    print("Se recibe un string en ascii y luego con las distintas operaciones que se realizan, se retorna un hash en base64.\n")
    print("Elija una opción:")
    print("1) Ingresar texto por consola.")
    print("2) Realizar hash al contenido del archivo de extensión .txt.")
    print("3) Realizar hash a un archivo.")
    choice = int(input("Ingrese una opcion: "))
    if(choice == 1):
        palabra = input("Ingrese la palabra: ")
        print("\n")
        mihash(palabra)
        md5(palabra)
        sha1(palabra)
        sha256(palabra)
    elif choice == 2:
        path = input("Ingrese el path de archivo a leer: ")
        palabras = read(path)
        cadena(palabras)
    elif choice == 3:
        path = input("Ingrese el path de archivo al cual desee realizar el hash: ")
        hashFile(path)
    else:
        print("Número no valido.")

main()