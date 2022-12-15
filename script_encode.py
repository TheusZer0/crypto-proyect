# obtenemos el hex del archivo
import binascii

filename = r'C:\Users\rober\OneDrive\Documentos\Crypto\archivos.json'
with open(filename, 'rb') as f:
    content = f.read()
hex_file = binascii.hexlify(content)

print(hex_file)

from itertools import cycle

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])
result = byte_xor(hex_file, b'string')

import base64
base64EncodedStr = base64.b64encode(result)

with open(r"C:\Users\rober\OneDrive\Documentos\Crypto\file.encode", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(base64EncodedStr)

# print('decoded', base64.b64decode(base64EncodedStr))