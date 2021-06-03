**Overpass 2 - Hacked**
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


**Task 2  Research - Analyse the codeP**
