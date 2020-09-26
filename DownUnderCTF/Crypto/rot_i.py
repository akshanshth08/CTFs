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
