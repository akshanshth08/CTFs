#!/bin/python

import os
cwd = os.getcwd()
key = ""
for i in cwd:
    if i == '/':
        key = key +  chr(int("0x24",0))
    elif i > '`'  and i <= 'z':
        key = key + chr(ord(i) - 0x1e)
    elif i > '@' and i <= 'Z':
        key = key + chr(ord(i) + 0x1e)
    else:
        key = key + chr(ord(i))
print(key)
        
