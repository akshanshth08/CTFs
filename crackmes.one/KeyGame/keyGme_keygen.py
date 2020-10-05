#!/bin/python

import os
#cwd = os.getcwd()
#key = ""
inp = input("Enter 15 characters :")
#inp = input()
#inp = "123123123123123"
rem = 0
key =""
if len(inp) == 15 :
    for i in inp:
        if (ord(i) >= 65  and ord(i) <=90 ) or (ord(i) >=48 and ord(i) <=57):
            val = ((ord(i) + rem)>>1)+10
            rem = val
        else:
            print("invalid character")
            exit() 
    key = inp + chr(val)


    print(f"The key generated : {key}")
    print("passing the key to the binary")
    cmd = "./keyGme " + key
    os.system(cmd)
else:
    print("invalid length")
