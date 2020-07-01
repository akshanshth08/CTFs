**The Code Caper**

This was an interesting room covering web enumeration, reverse shell, command execution, and buffer overflow concepts. It is a guided room, so it is more like a tutorial.
 
 
**Task 1: Intro** 

Deploy the machine
 
**Task 2: Host Enumeration**
 
Run the Nmap

![image](https://user-images.githubusercontent.com/45536407/86193151-3bcba600-bb19-11ea-84a4-1d429869e8ca.png)

 
From the Nmap output we gat :

**2.1:** 2
 
**2.3:** OpenSSH 7.2p2 Ubuntu 4ubuntu2.8

**2.4:** Apache/2.4.18
 
![image](https://user-images.githubusercontent.com/45536407/86193182-4a19c200-bb19-11ea-82b8-0a1056c6fe37.png)
 
And opening the web page we get

**2.2:** "Apache2 Ubuntu Default Page: It works"

**Task 3: Web Enumeration**

As given in the intro I ran gobuster command with suggested wordlist.
Point to note -x flag with specific extensions is very important as I ran it without the flag and after very long I found 0 files :P
But I had also run Nikto tool so it had also found administrator.php file
 
![image](https://user-images.githubusercontent.com/45536407/86193192-5271fd00-bb19-11ea-8a14-d985ec8cda24.png)

![image](https://user-images.githubusercontent.com/45536407/86193219-60278280-bb19-11ea-881e-120a4d313512.png)

 
**3.1:** administrator.php
 
**Task 4: Web Exploitation**
 
![image](https://user-images.githubusercontent.com/45536407/86193266-7d5c5100-bb19-11ea-96aa-2d11e2ec3ee7.png)

![image](https://user-images.githubusercontent.com/45536407/86193269-7f261480-bb19-11ea-9d74-507d3ef7a80d.png)
  
**4.1:** pingudad

**4.2:** secretpass

**4.4:** 3 (from the sqlmap verbose prompt)
 
 
**Task 5: Command Execution**
 
**5.1:** 3

![image](https://user-images.githubusercontent.com/45536407/86193292-8e0cc700-bb19-11ea-8451-986e7beacd31.png)
 
**5.2:** yes

![image](https://user-images.githubusercontent.com/45536407/86193314-98c75c00-bb19-11ea-99db-b3ea527faa4c.png)

For pingu's password I opened a reverse shell, Although it is mentioned that nc is installed none of the nc shells worked for me. I got the reverse shell using perl.
after getting the reverse shell I was just navigating through systems and I found a "hidden" directory which had a file called pass contain the required password
 
![image](https://user-images.githubusercontent.com/45536407/86193337-ac72c280-bb19-11ea-911c-70d2f93ae070.png)

**Task 6: Linenum**
 
Downloaded the Linenum file and used scp to transfer it to machine ran it and checked the output
 
**6.1:** /opt/secret/root


**Task 7: pwndgb**

**7.1:** read :)
 
**Task 8: Binary Exploitation : manually**

**8.1:** followed the instructions
 
**Task 9: Binary Exploitation: The pwntools way**

**9.1** Wrote the python script and ran 
 
**Task 10: Finishing the job**

From analysing the hash and referring to link given we could infer it is a 512sha hash 
I have Kali VM and hashcat is not work saying  no devices found
 
![image](https://user-images.githubusercontent.com/45536407/86193518-1723fe00-bb1a-11ea-9a3d-604c0c7a2aff.png)

So I cracked the password using John
First I copied /etc/passwd and /etc/shadow file in my local machine
And used unshadow utility
 
![image](https://user-images.githubusercontent.com/45536407/86193352-b5fc2a80-bb19-11ea-89b1-22f55076f181.png)
 
And then ran John   

![image](https://user-images.githubusercontent.com/45536407/86193397-cf04db80-bb19-11ea-8d65-3e110e8b9e20.png)
