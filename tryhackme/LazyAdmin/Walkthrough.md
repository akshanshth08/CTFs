# LazyAdmin
### https://tryhackme.com/room/lazyadmin

Port scan :

I first scan the open ports on the machine with masscan to get the open ports so that I can start working and then run nmap, since nmap is very slow

![image](https://user-images.githubusercontent.com/45536407/123530104-d88d3900-d6c4-11eb-97d9-133d8e9bee7d.png)


![image](https://user-images.githubusercontent.com/45536407/123530114-f2c71700-d6c4-11eb-9780-a323274a55cc.png)


As we can see that only 2 ports are open, 22 for ssh and 80 for web server so I opened the web server in the browser. It's the apache default page

![image](https://user-images.githubusercontent.com/45536407/123530159-581b0800-d6c5-11eb-9368-934dd5a49932.png)


So the first thing I did was to run gobuster to find hidden directories/files

![image](https://user-images.githubusercontent.com/45536407/123530182-9d3f3a00-d6c5-11eb-9aec-a23fb0c34b81.png)



Here we can see /content which seems intresting and on navigating there we got the following message :

![image](https://user-images.githubusercontent.com/45536407/123557883-6cacde00-d761-11eb-8d5b-da60e4dbea24.png)


I have never heard of SweetRice before so the first thing I checked was the searchsploit for existing exploits and also run the gobuster again with /content as the url

![image](https://user-images.githubusercontent.com/45536407/123557785-e7292e00-d760-11eb-89cf-64d610c1e829.png)

but since we dont know the version of it we cannot be sure which exploit will work.

coming to the output of the gobuster I visited all the directories which it found.

![image](https://user-images.githubusercontent.com/45536407/123557682-45094600-d760-11eb-85e5-7a335338caa6.png)


going to /as directory we got the login prompt, but still no version

![image](https://user-images.githubusercontent.com/45536407/123557916-91a15100-d761-11eb-8369-08aab7a72ac0.png)

looking at changelog.txt we got the version of SweetRice as 1.5.0 so we can try if the exploits above work

![image](https://user-images.githubusercontent.com/45536407/123557983-e04eeb00-d761-11eb-8b18-afbe888b0fa5.png)


![image](https://user-images.githubusercontent.com/45536407/123557785-e7292e00-d760-11eb-89cf-64d610c1e829.png)

Looking at the backup disclosure vulnerability, it tells us we can get backup dump for mysql by navigating to /inc/mysql_backup.

![image](https://user-images.githubusercontent.com/45536407/123558088-90bcef00-d762-11eb-8bc8-d29c9ea0aa40.png)

![image](https://user-images.githubusercontent.com/45536407/123558119-b813bc00-d762-11eb-9287-cd3967246c30.png)


We got the backup file and in the file we got the username and password hash of the webmaster's user.

![image](https://user-images.githubusercontent.com/45536407/123558183-ef826880-d762-11eb-8614-ebe8b9e043ec.png)

I ran hash-identify to identify the type of hash as MD5 and then cracked the hash using hashcat.

![image](https://user-images.githubusercontent.com/45536407/123558235-29ec0580-d763-11eb-97ad-713c4831fbab.png)

![image](https://user-images.githubusercontent.com/45536407/123558270-63247580-d763-11eb-92f5-e9f7e0be7bb0.png)

using these credentials I logged in to the web portal and on the left top corner we can see the current version as 1.5.1.

![image](https://user-images.githubusercontent.com/45536407/123558306-949d4100-d763-11eb-92af-b563fbe48101.png)

going back to the existing exploits we found from the searchsploit results. The File upload vulnerability seem intresting.

![image](https://user-images.githubusercontent.com/45536407/123558409-14c3a680-d764-11eb-8a19-ab0f6aae19e2.png)

It says we can upload PHP code in the ads and then access it, So I created a PHP reverse shell from pentestmonkey (https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and uploaded the file

![image](https://user-images.githubusercontent.com/45536407/123558448-450b4500-d764-11eb-88a8-1c6d22f59be3.png)

and accesed the file uploaded by navigating to /inc/ads

![image](https://user-images.githubusercontent.com/45536407/123558464-5c4a3280-d764-11eb-8ab5-71123ef18075.png)

and got the reverse shell on my system

![image](https://user-images.githubusercontent.com/45536407/123558477-75eb7a00-d764-11eb-85e7-1c9ba03c914e.png)

and read the user.txt flag

![image](https://user-images.githubusercontent.com/45536407/123558496-8ef42b00-d764-11eb-9593-9244afaa6d53.png)


For escalating priviledges I first check sudo permisions and it was running a perl file with sudo command without requiring password

![image](https://user-images.githubusercontent.com/45536407/123558586-0e81fa00-d765-11eb-83c2-a921c1d28611.png)

The backup file and it was then running a file /etc/copy.sh

![image](https://user-images.githubusercontent.com/45536407/123558610-38d3b780-d765-11eb-810f-5705302ddea2.png)

copy.sh was just executing some commands and these commands will run with root priviledges

![image](https://user-images.githubusercontent.com/45536407/123558638-5e60c100-d765-11eb-810b-995f51d3b080.png)

Since these command were running as root. I overwrote the file with /bin/sh to get me a root shell

![image](https://user-images.githubusercontent.com/45536407/123558715-be576780-d765-11eb-8e34-e41762651358.png)






