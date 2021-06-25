*** Bounty Hacker ***

This is an easy machine which involves anonymous ftp enabled, bruteforcing the password and then escalting priviledges.

For finding open ports I like to run the masscan first and then run nmap on the open ports

![image](https://user-images.githubusercontent.com/45536407/123351987-5ff37480-d52c-11eb-8726-c2af3577e3d0.png)

![image](https://user-images.githubusercontent.com/45536407/123352007-6bdf3680-d52c-11eb-8b6d-6d1300d90196.png)


Only 2 ports are open 22 for ssh and 21 for ftp
I was able to login to ftp using anonymous login and found  2 files in the folder.

![image](https://user-images.githubusercontent.com/45536407/123352088-94ffc700-d52c-11eb-8fc0-27dd144ca35f.png)


I copied those files to my machine.
![image](https://user-images.githubusercontent.com/45536407/123352142-af39a500-d52c-11eb-9f6c-0f214f6af8a5.png)


from tasks.txt we got to know the name of the user
![image](https://user-images.githubusercontent.com/45536407/123352175-c6789280-d52c-11eb-8c46-3e5c2be9aac5.png)

from locks.txt we got the potential list of passwords which the user might be using

![image](https://user-images.githubusercontent.com/45536407/123352236-e019da00-d52c-11eb-8d66-f35be466798f.png)


I bruteforced the ssh login using hydra and got the password

![image](https://user-images.githubusercontent.com/45536407/123352291-fe7fd580-d52c-11eb-8b71-2fe01a9ad147.png)

user flag :

![image](https://user-images.githubusercontent.com/45536407/123352382-2838fc80-d52d-11eb-9095-986d74dad73c.png)


For escalating priviledges I checked the sudo permissions of the user and the user could run tar as sudo

![image](https://user-images.githubusercontent.com/45536407/123352442-47378e80-d52d-11eb-92b3-305ba1a94890.png)


refrenced GTFOBins ( https://gtfobins.github.io/gtfobins/tar/#sudo ) to find if I can exploit this, and yes I can

![image](https://user-images.githubusercontent.com/45536407/123352499-69311100-d52d-11eb-8e57-8920ca3e4971.png)

ran the command to get the root and read root.txt

![image](https://user-images.githubusercontent.com/45536407/123352577-92ea3800-d52d-11eb-8de5-723ac99be811.png)





