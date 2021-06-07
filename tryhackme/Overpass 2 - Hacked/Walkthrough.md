***Overpass 2 - Hacked***

This is a free room if you want to practice forensics, where you have to analyze a pcap file and answer questions which follow.

**Task 1  Forensics - Analyse the PCAP**

Download the PCAP file, open it in wireshark analyze the traffic to answer the questions:

1.1 URL of the page :
![image](https://user-images.githubusercontent.com/45536407/120569948-00022600-c3e5-11eb-958a-34625f4b4447.png)

1.2 Payload :
![image](https://user-images.githubusercontent.com/45536407/120570175-8159b880-c3e5-11eb-8ccc-328ec9343c1a.png)

1.3 Password used for privesc:
from the traffic you can see the attacker making a netcat connection and all netcat traffic is in plain text. If you follow the TCP stream you see all the command which attacker used.
![image](https://user-images.githubusercontent.com/45536407/120570344-e7ded680-c3e5-11eb-8e3e-c15c87edc31d.png)

1.4 backdoor
For setting up the backdoor, attacker downloaded a file from github
![image](https://user-images.githubusercontent.com/45536407/120570483-42783280-c3e6-11eb-9c0e-ef2feb6aa7e3.png)

1.5 Crackable system passwords :
from the netcat tcp stream we have the commands which attacker ran on the system. Among them hashes from /etc/shadow file are also visible and since we know the wordlist used we can crack them ourselves.
![image](https://user-images.githubusercontent.com/45536407/120570725-ba465d00-c3e6-11eb-9c21-2001f7244cd1.png)


**Task 2  Research - Analyse the code**
For this part you have to open the github and study the code of the backdoor

Default Hash:
![image](https://user-images.githubusercontent.com/45536407/120729901-4cfdff00-c4ae-11eb-8342-371f941b8982.png)

Hardcoded Salt:
![image](https://user-images.githubusercontent.com/45536407/120729977-71f27200-c4ae-11eb-9c53-ae9ecdb8a37d.png)

Hash that Attacker used :
![image](https://user-images.githubusercontent.com/45536407/120730110-b847d100-c4ae-11eb-905e-937bd8c5ce6c.png)

Cracking the hash :
concatenated the hash and the salt in a file:
![image](https://user-images.githubusercontent.com/45536407/120730446-7ec39580-c4af-11eb-9ae0-3dc249d62231.png)

ran hashcat
![image](https://user-images.githubusercontent.com/45536407/120730488-97cc4680-c4af-11eb-8671-f02b3aa6bffe.png)

![image](https://user-images.githubusercontent.com/45536407/120730558-bb8f8c80-c4af-11eb-99c9-75e6aecbb3bb.png)

![image](https://user-images.githubusercontent.com/45536407/120730653-f2fe3900-c4af-11eb-99f6-d1615c0629a5.png)


**Task 3  Get Back in**
Message left:
This message could be found in the wireshark packets in index.html

![image](https://user-images.githubusercontent.com/45536407/121090106-0feb8280-c7b6-11eb-97f1-79bb5aa68060.png)

User flag :
from nmap you can see there are 2 services running on the server, both ssh.
I tried connecting using different users on both the ports using the passwords cracked from the shadow file in the earlier steps none of them worked but, I was able to login with user james with the hash that was cracked in the earlier steps as the password for backdoor.

![image](https://user-images.githubusercontent.com/45536407/121090656-e848ea00-c7b6-11eb-875e-b36e371b670e.png)


read the user.txt flag
![image](https://user-images.githubusercontent.com/45536407/121090916-44ac0980-c7b7-11eb-987d-23b1ebfdd31c.png)

for root.txt flag I had to search a bit. Then I found a suid binary for bash in the user directory.

![image](https://user-images.githubusercontent.com/45536407/121091096-77ee9880-c7b7-11eb-8ce2-6dde2f1577e2.png)

ran bash with -p attrbute for running it in priviledged mode.(I didn't knew about -p then :P)
![image](https://user-images.githubusercontent.com/45536407/121091402-f3504a00-c7b7-11eb-9d53-c32b517a9901.png)




