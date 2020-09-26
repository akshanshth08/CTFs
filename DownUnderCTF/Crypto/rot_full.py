#/usr/bin/python3

#inp_str = 'IAJBO{ndldie_al_aqk_jjrnsxee}'

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
