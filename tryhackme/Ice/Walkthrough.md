# Ice Walkthrough

**Tast 1 [connect] :**

was to connect to trytryhackme using openvpn


**Task2 [Recon] :**

Ran the Nmap , command used **sudo nmap -sS -p- -oN namp_ice <machine_ip>**
![image](https://user-images.githubusercontent.com/45536407/85813978-c5066580-b732-11ea-9e20-7aeb43bdc81a.png)
 
Nmap was taking a lot a of time so I tried masscan as well.
At first it was not showing any ports then I realised it was scanning on default network interface and not on the Openvpn one so I mentioned that adapter in the command as well.

I was not getting all the ports initially but the I tried 2-3 range values and got all the ports in the end. :)
![image](https://user-images.githubusercontent.com/45536407/85813996-d18abe00-b732-11ea-84ca-3e4873829b82.png)

![image](https://user-images.githubusercontent.com/45536407/85814000-d51e4500-b732-11ea-86ce-447cb7c9f500.png)

Masscan is very quick and after finding the open ports we can run the nmap on those specific ports to know more about the services running as Nmap is slow.
![image](https://user-images.githubusercontent.com/45536407/85814012-dfd8da00-b732-11ea-97c6-d5b1b08e9878.png)


From the Nmap output we can answer most of the questions

**2.3 :** 3389

**2.4 :** Icecast

**2.5 :** DARK-PC

**Task 3 [Gain Acess]**

**3.1 :** searching cvedetails we can see the type of vulnerability as : execute code overflow
![image](https://user-images.githubusercontent.com/45536407/85814029-ebc49c00-b732-11ea-9047-a757739b4d93.png)


**3.2 :** CVE-2004-1561

**3.4 :** exploit/windows/http/icecast_header
![image](https://user-images.githubusercontent.com/45536407/85814041-f717c780-b732-11ea-9fb8-15ffb9dc7d39.png)

**3.6 :** rhosts

![image](https://user-images.githubusercontent.com/45536407/85814108-28909300-b733-11ea-858d-25fd36e24c83.png)

**Task 4 [Escalate] :**

**4.1 :** meterpreter
![image](https://user-images.githubusercontent.com/45536407/85814115-30e8ce00-b733-11ea-954c-5ec472b78175.png)

Below ans were found from the output of getuid command in kiwi session

![image](https://user-images.githubusercontent.com/45536407/85814182-5d9ce580-b733-11ea-8320-7f10c08a66f7.png)

**4.2 :** Dark

**4.3 :** 7601

**4.4 :** x64

**4.6 :** exploit/windows/local/bypassuac_eventvwr

**4.10 :** set the LHOST to ip address of the tun0(vpn network interface and not the default ip in eth0)
![image](https://user-images.githubusercontent.com/45536407/85814203-6ab9d480-b733-11ea-9381-a5c851e15787.png)

**4.14 :** SeTakeOwnershipPrivilege (getprivs)

**Task 5 [Looting]**

**5.2 :** spoolsv.exe

![image](https://user-images.githubusercontent.com/45536407/85814222-7a391d80-b733-11ea-8310-0fb0d594ade2.png)


**5.4 :** NT AUTHORITY\SYSTEM

**5.7 :** creds_all

![image](https://user-images.githubusercontent.com/45536407/85814260-88873980-b733-11ea-9aa1-f3ecbc32986c.png)

**5.8 :** 

![image](https://user-images.githubusercontent.com/45536407/85814271-9210a180-b733-11ea-80e9-6756696785cc.png)

**Task 6 [Post Exploitation]**

All these answers could be found by typing "help" in mimikatz shell
**6.2 :** hashdump

**6.3 :** screenshare

**6.4 :** record_mic

**6.5 :** timestomp

**6.6 :** golden_ticket_create

**Task 7 [Extra credit]**

I was not able to compile the exploit given in the link but on searching exploitdb I found there was another exploit present for Icecast on the same lines as that given in the link
![image](https://user-images.githubusercontent.com/45536407/85814294-9dfc6380-b733-11ea-9716-c7f042a4ac74.png)
![image](https://user-images.githubusercontent.com/45536407/85814317-a8b6f880-b733-11ea-9c60-f95eeb0bb9cf.png)


This completes the room.

In one of the steps they ass us to enable rdp services and since we knew the password for user dark I thought of accessing it using that service and was able to login to the user

![image](https://user-images.githubusercontent.com/45536407/85814349-bb313200-b733-11ea-92b7-0b4806ef238a.png)
![image](https://user-images.githubusercontent.com/45536407/85814353-bd938c00-b733-11ea-873f-076076761ecc.png)
![image](https://user-images.githubusercontent.com/45536407/85814361-bff5e600-b733-11ea-9805-78a9950dabe3.png)
![image](https://user-images.githubusercontent.com/45536407/85814366-c2f0d680-b733-11ea-9e9d-1d76b9095412.png)
