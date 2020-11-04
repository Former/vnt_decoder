# -*- coding: utf-8 -*-

# Copyright © 2020 Alexei Bezborodov. Contacts: <AlexeiBv+vnt_dec@narod.ru>
# License: Public domain: http://unlicense.org/

import sys

def FromHex(hex_str):
    #print(hex_str)
    dec_byte = bytearray.fromhex(hex_str)
    res = dec_byte.decode('utf-8')
    #print(dec_byte, res)
    return res

def Decode_Vnt(vnt_file):
    f = open(vnt_file, 'r')
    lines = f.readlines()
    f.close()

    f = open(vnt_file+".txt", 'wb') #, encoding='utf-8')
    for line in lines:
        if line.find("CHARSET=UTF-8") == -1:
            continue
        str_to_decode = line[line.find(":") + 1:]
        
        decode_str = ""
        
        hex_char = ""
        
        i = 0
        while i < len(str_to_decode):
            cur_char = str_to_decode[i]
            #print("cur_char", cur_char)
            if cur_char == "=":
                hex_char += str_to_decode[i + 1] + str_to_decode[i + 2]
                i += 3
                continue

            decode_str += FromHex(hex_char)
            hex_char = ""
            decode_str += cur_char
            i += 1

        if len(hex_char) > 0:
            decode_str += FromHex(hex_char)
        
        #print("decode_str", decode_str)
        f.write(decode_str.encode('utf-8'))
    f.close()


files_to_decode = []

if __name__ == "__main__":
    for i in range(len(sys.argv)):
        param = sys.argv[i]
        if i > 0:
            files_to_decode.append(param)

for f in files_to_decode:
    Decode_Vnt(f)
