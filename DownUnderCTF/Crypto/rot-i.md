### Crypto
========================================================================================
#### rot-i
-----------------------------------------------------------------------------------------
 points 100
 
#### Description
*Author: joseph*
*ROT13 is boring!*
*Attached files:*

	• challenge.txt (sha256: ab443133665f34333aa712ab881b6d99b4b01bdbc8bb77d06ba032f8b1b6d62d)

*Challenge.txt :*
*Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :).*

-------------------------------------------------------------------------------------------

Here we can see the pattern  IAJBO{ndldie_al_aqk_jjrnsxee} and since we know the pattern of the flags which starts with DUCTF we can conclude that it follows a rot-13/ ceaser cipher with key decrementing character by character.
I first created a script only to decode the flag and then to decode the whole message.

rot_i.py
```
#/usr/bin/python3

inp_str = 'IAJBO{ndldie_al_aqk_jjrnsxee}'

full_str = "Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :)."
output_str = ""
for i in range(len(inp_str)):
    x = ord(inp_str[i])
    if (x >= 65  and x <=90 ) or (x >=97 and x <= 122):
        
        if (x >= 65  and x <=90 ): 
            offset = (x + 21  - i)
            if(offset <65):
                offset = offset +26
            elif(offset>90):
                offset = offset - 26
            y = chr(offset)
        elif (x >=97 and x <= 122):
            offset = (x + 21  - i)
            if(offset < 97):
                offset = offset +26
            elif(offset > 122):
                offset = offset -26
            y = chr(offset)
    else:
        y = inp_str[i]
    output_str = output_str + y
    #x = chr(offset)
    #print(x)
print(output_str)
```

rot_full.py
```
full_str = "Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :)."
output_str = ""
count = 0
for i in range(len(full_str)):
    x = ord(full_str[i])
    if (x >= 65  and x <=90 ) or (x >=97 and x <= 122):
        count = count % 26
        if count<0:
            key = count + 26
        else:
            key = count
        if (x >= 65  and x <=90 ): 
            offset = (x + key)
            if(offset <65):
                offset = offset +26
            elif(offset>90):
                offset = offset - 26
            y = chr(offset)
        elif (x >=97 and x <= 122):
            offset = (x + key)
            if(offset < 97):
                offset = offset +26
            elif(offset > 122):
                offset = offset -26
            y = chr(offset)
    else:
        y = full_str[i]
    output_str = output_str + y
    count = count - 1
print(output_str)
```

Flag :

![image](https://user-images.githubusercontent.com/45536407/94334962-feef3e00-ffa5-11ea-9aab-20e3a39d595d.png)
