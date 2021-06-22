***Root_me***

This is free room and an easy ctf in which you hace to enumerate the server exploit a file upload vulnerability and then escalate the priviledges using a suid binary.

**Task 2: Reconnaissance ** 

2.1 number of open ports
I prefer running masscan first, (since it is fast and nmap is very slow) to find the open ports first and then run nmap on those ports.

![image](https://user-images.githubusercontent.com/45536407/122846847-b5354900-d2d4-11eb-9fd6-24aab30ed5b6.png)

you can see that port 80 is open. I visited the website but there was only an gif saying root_me

![image](https://user-images.githubusercontent.com/45536407/122848521-ae5c0580-d2d7-11eb-9a89-16f712d93970.png)


I ran gobuster to find hidden directories.

![image](https://user-images.githubusercontent.com/45536407/122847446-b4e97d80-d2d5-11eb-844c-9c171f5103bb.png)

if you'll visit the directories found above you can see the apache version mentioned on the page

![image](https://user-images.githubusercontent.com/45536407/122848580-d2b7e200-d2d7-11eb-9c31-ad4192c378ca.png)

This covers the answers for task 2.2 2.3 2.4 2.5

**Task 3  Getting a shell**

In the upload functionality I tried uploading a php reverse I created using weevely but it gave me an error which means php uploads are not allowed(I guess).

![image](https://user-images.githubusercontent.com/45536407/122848965-933dc580-d2d8-11eb-963f-506dab4ec07b.png)


![image](https://user-images.githubusercontent.com/45536407/122848647-fd099f80-d2d7-11eb-9142-d47eaf2d7b35.png)


I tried uploading the file using different extenstions and it seems only PHP was not allowed. I tried double extenstion , null character but all tries failed.
In the end I succeeded in uploading the file with .phtml extention from which I gained the reverse shell.

![image](https://user-images.githubusercontent.com/45536407/122848983-a355a500-d2d8-11eb-80f9-42d2499f3039.png)


![image](https://user-images.githubusercontent.com/45536407/122849063-cbdd9f00-d2d8-11eb-8c19-381f0c557d8a.png)


and got the user flag:

![image](https://user-images.githubusercontent.com/45536407/122849168-fe879780-d2d8-11eb-9b27-9a9569a4e8e5.png)


** Task 4  Privilege escalation **

For the root flag I searched for suid binaries.

![image](https://user-images.githubusercontent.com/45536407/122849233-1d862980-d2d9-11eb-9df1-cdc3b43a33d6.png)


python binary had the suid bit set
![image](https://user-images.githubusercontent.com/45536407/122849288-38f13480-d2d9-11eb-9cb9-3b46b07c589e.png)

searched how to exploit this, thanks to gtfobins : https://gtfobins.github.io/gtfobins/python/#suid 

![image](https://user-images.githubusercontent.com/45536407/122849863-507ced00-d2da-11eb-9938-1bb14e937d9f.png)


Since I was in a weevely shell I was not able to get the priviledged shell by executing python command to spawn a shell.


Inside the weevely shell I created a reverse tcp shell and then spawned the priviledged shell.

![image](https://user-images.githubusercontent.com/45536407/122849562-bd43b780-d2d9-11eb-9314-d037c5b69f0a.png)

read the root.txt file to get the flag

![image](https://user-images.githubusercontent.com/45536407/122849806-3511e200-d2da-11eb-8e08-d6433a18f3d7.png)








