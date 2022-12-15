
#Se abre archivo a decodificar.
file_encrypt = open(r'D:\Desktop\Escritoriu USM\2022-2\Cripto\Proyecto\crypto-project-main\Analista\Descarga_Drive\cifrado1.encode', encoding="ISO-8859-1")

#Se obtienen todos los caracteres.
string_f = ''
for x in file_encrypt:
    string_f += x

#Se convierte a base64
import base64
result = base64.b64decode(string_f)

#Se le aplica el cifrado de tipo XOR
from itertools import cycle
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])
result = byte_xor(result, b'string')

# resultado hex
tmp = result.decode()

#Muestra todos los tipos de archivos que soporta el descifrado, ademas de mostrar sus "Magic Numbers", los primero 6 caracteres muestran el tipo de archivo.
all_supported_files = [
    ["jpeg","ffd8ff"],
    ["zip","504b03"],
    ["gif","474946"]
]

#Se obtiene el "Magic Number" del archivo.
magic_numb = ""
total = 0
for x in tmp:
    if total == 6:
        break
    else:
        if total%2==0:
            magic_numb += x
        else:
            magic_numb += x
    total += 1

import binascii
#Verifica si el "Magic Number " esta dentro del listado
for x in all_supported_files:
    #si es asi, empieza la transformacion hexadecimal y se crel el archivo "result.txt", o en el caso que sea un "jpg" regresa un "results.jpg"
    if magic_numb == x[1]:
        print("file accepted, the file is",x[0])
        data=tmp 
        data=data.strip()
        data=data.replace(' ', '')
        data=data.replace('\n', '')
        data = binascii.a2b_hex(data)
        with open('result.jpg', 'wb') as image_file:
            image_file.write(data)
    else:
        
        quote_a = bytes.fromhex(tmp).decode("ISO-8859-1",errors='ignore')
        quote   = quote_a.replace(';', '\n- ')
        my_str_as_bytes = str.encode(quote)
        with open('result.txt', 'wb') as text_file:
            text_file.write(my_str_as_bytes)
