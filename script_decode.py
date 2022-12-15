file_encrypt = open(r'C:\Users\rober\OneDrive\Documentos\Crypto\file.encode', encoding="ISO-8859-1")

string_f = ''
for x in file_encrypt:
    string_f += x

import base64
result = base64.b64decode(string_f)

from itertools import cycle
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])
result = byte_xor(result, b'string')

# resultado hex
tmp = result.decode()

all_supported_files = [
    ["jpeg","ffd8ff"],
    ["zip","504b03"],
    ["gif","474946"]
]

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

for x in all_supported_files:
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
        # lectura de datos
        quote_a = bytes.fromhex(tmp).decode("ISO-8859-1",errors='ignore')
        quote   = quote_a.replace(';', '\n- ')

        with open('example.txt', 'rb') as f:
            result = f.readlines()

        if 'first line' in result[0].decode('utf-8'):
            print('success')
        