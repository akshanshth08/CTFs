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

