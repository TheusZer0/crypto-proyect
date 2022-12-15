# obtenemos el hex del archivo
import binascii

#Desde "archivos.json" se hace una transformación hexadecimal
filename = r'D:\Desktop\Escritoriu USM\2022-2\Cripto\Proyecto\crypto-project-main\Sensores\archivos.json'
with open(filename, 'rb') as f:
    content = f.read()
hex_file = binascii.hexlify(content)

#Imprime la transformación anterior.
print(hex_file)

from itertools import cycle
#Luego se le aplica el cifrado XOR
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])
result = byte_xor(hex_file, b'string')

#Y finalmente se hace una nueva transformacion pero esta vez en base64
import base64
base64EncodedStr = base64.b64encode(result)

#Luego se crea un archivo llamado: "cifrado1.encode" que será enviado a la nube, esta dirección debe ser cambiada según el usuario.
with open(r"D:\Desktop\Escritoriu USM\2022-2\Cripto\Proyecto\crypto-project-main\Sensores\cifrado1.encode", "wb") as binary_file:
    binary_file.write(base64EncodedStr)

