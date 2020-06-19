## Vulnversity Walkthrough
This is one of the 6 getting started rooms when you join tryhackme.

**Task 1** was to deploy the machine.

**Task 2 reconnaissance.**

Inro briefs you about the Nmap and various of the flags which can be used

    * 2.1   This was a simple nmap scan
![image](https://user-images.githubusercontent.com/45536407/85080658-cfa38680-b197-11ea-9643-c18b070d9dc8.png)

    * 2.2   From the nmap scan what were the number of ports which were opened : 6

    * 2.3   From the output of nmap we can view the squid proxy server : 3.5.12

    * 2.4   ans :400

    * 2.5   "-n" in Nmap will not resolve DNS

    * 2.6   Nmap output tells us the OS as ubuntu

    * 2.7   web server is running on port 3333

    * 2.8   done


**Task 3 Locating Directories using Gobuster**

    * 3.1 read the into about gobuster

    * 3.2 run the gobuster on the deployed machine to find the hidden directory : /internal/

![image](https://user-images.githubusercontent.com/45536407/85081312-9f5ce780-b199-11ea-90ef-af9350c4ee57.png)


**Task 4 Compromise the webserver**

    * 4.1 Navigated to /internal url which was an upload page. tried a few uploads but all the uploads failed. ans .php

![image](https://user-images.githubusercontent.com/45536407/85081411-e77c0a00-b199-11ea-9be3-6a9a4adaaa69.png)

    * 4.2 I configured my burp proxy and intercepted the input to chek the allowed extensions.


![image](https://user-images.githubusercontent.com/45536407/85082096-dd5b0b00-b19b-11ea-81d3-27fc6c9566bc.png)


I used /usr/share/wordlists/wfuzz/general/extensions_common.txt wordlist for payload in intruder. this comes preloaded in Kali and started the attack


![image](https://user-images.githubusercontent.com/45536407/85082275-63775180-b19c-11ea-901f-bf27e5ff3424.png)


before starting the attack I unchecked the URL decoding checkbox as I didnot want "." in my extensions to be encoded


![image](https://user-images.githubusercontent.com/45536407/85082570-50b14c80-b19d-11ea-9789-a77f2aabbbbb.png)


from the length of the response we can infer that .phtml was successfull

![image](https://user-images.githubusercontent.com/45536407/85082725-c87f7700-b19d-11ea-82f6-c85b7702d71f.png)


    * 4.3 .phtml is the allowed extionsion

    * 4.4 I downloaded the php shell as mentioned in introduction to task and uploaded it and accessed the shell prompt

![image](https://user-images.githubusercontent.com/45536407/85083182-fe712b00-b19e-11ea-8edd-d17ca0085882.png)

    * 4.5 in /home directory I found bill folder so this must be the user who manages the serve

    * 4.6 in bill's home directory I found user.txt which contained the flag

![image](https://user-images.githubusercontent.com/45536407/85083292-514ae280-b19f-11ea-9b08-bf40d88a8e09.png)


**Task 5 : Privelege Escalation**

    * 5.1  for finding suid binaries I used :
        ** find / -perm -u=s -type f 2>/dev/null **
    
![image](https://user-images.githubusercontent.com/45536407/85083614-3e84dd80-b1a0-11ea-90c8-bc4c282eda15.png)

I started googling all the binaries in the list which could be achieve privilege escalation and I found that systemctl binary is used to intialize and run services and since its priveleges are root I can write a service to run a command from root.

So I first wrote a service to change the permission of /root/root.txt so that I can read it 


![image](https://user-images.githubusercontent.com/45536407/85084791-d637fb00-b1a3-11ea-849f-05cd16213af2.png)


![image](https://user-images.githubusercontent.com/45536407/85084726-a8eb4d00-b1a3-11ea-9d0f-40ef7c7f7f8a.png)

But I was not able to read the file so I wrote another service to copy that file.

![image](https://user-images.githubusercontent.com/45536407/85084849-0384a900-b1a4-11ea-9172-c840cdb88330.png)

![image](https://user-images.githubusercontent.com/45536407/85084914-2b740c80-b1a4-11ea-82e8-44174015d818.png)

and then I was able to read the flag

![image](https://user-images.githubusercontent.com/45536407/85084944-39299200-b1a4-11ea-95fe-cacab75117db.png)


