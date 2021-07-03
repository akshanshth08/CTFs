# Attacktive Directory
## https://tryhackme.com/room/attacktivedirectory

This was a very intresting room. I learned a lot. All the tasks involved in this room required me to google all the tools and how to use them.


## Task.1
Deploy the machine

## Task.2 Setup 
Install the tools

## Task.3 Enumeration Welcome to Attacktive Directory

Ran the Nmap on the IP and go the answeres to the ques in this section from the output of it.

![image](https://user-images.githubusercontent.com/45536407/124339611-a759b080-db7d-11eb-9f56-4449e73f0e13.png)


### 3.1 What tool will allow us to enumerate port 139/445?
Enum4Linux 

### 3.2 What is the NetBIOS-Domain Name of the machine?

### 3.3 What invalid TLD do people commonly use for their Active Directory Domain?

## Task.4 Enumeration Enumerating Users via Kerberos

### 4.1 What command within Kerbrute will allow us to enumerate valid usernames?

![image](https://user-images.githubusercontent.com/45536407/124339716-57c7b480-db7e-11eb-8802-2ebb0def8bef.png)


### 4.2 What notable account is discovered? (These should jump out at you)

### 4.3 What is the other notable account is discovered? (These should jump out at you)

![image](https://user-images.githubusercontent.com/45536407/124339755-8cd40700-db7e-11eb-80a9-243b870e0e6b.png)


## Task 5  Exploitation Abusing Kerberos

### 5.1 extracting the hash for the user

![image](https://user-images.githubusercontent.com/45536407/124339899-78443e80-db7f-11eb-8b81-3848db5eb8be.png)

lookup the type of the hash from hashcat wiki to solve below 2 questions.

![image](https://user-images.githubusercontent.com/45536407/124342554-a3845900-db92-11eb-91e3-cf3aedbe7fb0.png)


### 5.2 what type of Kerberos hash did we retrieve from the KDC?

### 5.3 What mode is the hash?

### 5.4 Cracked the hash.

![image](https://user-images.githubusercontent.com/45536407/124339981-edb00f00-db7f-11eb-8c98-03504beab068.png)

![image](https://user-images.githubusercontent.com/45536407/124339995-091b1a00-db80-11eb-8531-2e9b89496df9.png)


## Task 6  Enumeration Back to the Basics

### 6.1 What utility can we use to map remote SMB shares?
smbclient

### 6.2 Which option will list shares?
-L

### 6.3 number of shares
6

### 6.4 There is one particular share that we have access to that contains a text file. Which share is it?

![image](https://user-images.githubusercontent.com/45536407/124340193-5e0b6000-db81-11eb-903b-19313db921ff.png)

### 6.5 What is the content of the file?

![image](https://user-images.githubusercontent.com/45536407/124340196-78ddd480-db81-11eb-8770-58a0ad15bf3b.png)

![image](https://user-images.githubusercontent.com/45536407/124340208-9448df80-db81-11eb-9fb5-cb844c31d57d.png)

### 6.6 decode the code:

For decoding the code I used cyberchef (https://gchq.github.io/CyberChef/) magic

![image](https://user-images.githubusercontent.com/45536407/124342258-9f573c00-db90-11eb-9185-85fff1ff5bfe.png)


## Task 7  Domain Privilege Escalation Elevating Privileges within the Domain

used secretsdump.py from impacket to get the hashes. and anser of questions for this task.

![image](https://user-images.githubusercontent.com/45536407/124342365-74b9b300-db91-11eb-812d-43ecc2c7fb29.png)


### 7.1 What method allowed us to dump NTDS.DIT?
DRSUAPI

### 7.2 What is the Administrators NTLM hash?

### 7.3 What method of attack could allow us to authenticate as the user without the password?
Pass the hash

### 7.4 Using a tool called Evil-WinRM what option will allow us to use a hash?

![image](https://user-images.githubusercontent.com/45536407/124342388-a763ab80-db91-11eb-8d52-b82db3b66501.png)

## Task 8  Flag Submission Flag Submission Panel

### 8.1 

![image](https://user-images.githubusercontent.com/45536407/124342417-d5e18680-db91-11eb-9a2f-c3d7fdde7be7.png)


### 8.2

![image](https://user-images.githubusercontent.com/45536407/124342434-ef82ce00-db91-11eb-80e6-065a2cf8d8a8.png)


### 8.3

![image](https://user-images.githubusercontent.com/45536407/124342443-06c1bb80-db92-11eb-8bfc-26081c0e6709.png)








