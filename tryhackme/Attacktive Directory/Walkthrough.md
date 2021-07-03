# Attacktive Directory
## https://tryhackme.com/room/attacktivedirectory

This was a very intresting room. I learned a lot. All the tasks involved in this room required me to google all the tools and how to use them.


### Task.1
Deploy the machine

### Task.2 Setup 
Install the tools

### Task.3 Enumeration Welcome to Attacktive Directory

Ran the Nmap on the IP and go the answeres to the ques in this section from the output of it.

![image](https://user-images.githubusercontent.com/45536407/124339611-a759b080-db7d-11eb-9f56-4449e73f0e13.png)


## 3.1 What tool will allow us to enumerate port 139/445?
Enum4Linux 

## 3.2 What is the NetBIOS-Domain Name of the machine?

## 3.3 What invalid TLD do people commonly use for their Active Directory Domain?

### Task.4 Enumeration Enumerating Users via Kerberos

4.1 What command within Kerbrute will allow us to enumerate valid usernames?

![image](https://user-images.githubusercontent.com/45536407/124339716-57c7b480-db7e-11eb-8802-2ebb0def8bef.png)


4.2 What notable account is discovered? (These should jump out at you)

4.3 What is the other notable account is discovered? (These should jump out at you)

![image](https://user-images.githubusercontent.com/45536407/124339755-8cd40700-db7e-11eb-80a9-243b870e0e6b.png)


Task 5  Exploitation Abusing Kerberos

5.1 extracting the hash for the user
![image](https://user-images.githubusercontent.com/45536407/124339899-78443e80-db7f-11eb-8b81-3848db5eb8be.png)

lookup the type of the hash from hashcat wiki to solve below 2 questions.

5.2 what type of Kerberos hash did we retrieve from the KDC?

5.3 What mode is the hash?

5.4 Cracked the hash.

![image](https://user-images.githubusercontent.com/45536407/124339981-edb00f00-db7f-11eb-8c98-03504beab068.png)

![image](https://user-images.githubusercontent.com/45536407/124339995-091b1a00-db80-11eb-8531-2e9b89496df9.png)


