*** Pickle Rick ***

After deploying the machine I first ran the masscan to check for open ports. I do that because its fast and then run nmap for only the open ports.

![image](https://user-images.githubusercontent.com/45536407/123010740-37814400-d38d-11eb-9a3b-ade118d48e29.png)


![image](https://user-images.githubusercontent.com/45536407/123010783-45cf6000-d38d-11eb-9318-f3240f5a1875.png)


From the port scan we can see that only 2 posts are running so we have to find vulnerabilities in the web server. On to the website:

Its just a plain website with some text on it.

![image](https://user-images.githubusercontent.com/45536407/123010923-862ede00-d38d-11eb-8cf7-ee9fc841ab49.png)

I started looking around the website.

robots.txt:

![image](https://user-images.githubusercontent.com/45536407/123011096-cc843d00-d38d-11eb-8510-397f356e377d.png)

looking at the source code, I got the username:

![image](https://user-images.githubusercontent.com/45536407/123011208-f63d6400-d38d-11eb-9525-85cdf4e79d50.png)

while looking at the website I had ran gobuster seperately to find hidden directories and found login.php file which is the login portal.

![image](https://user-images.githubusercontent.com/45536407/123011346-2b49b680-d38e-11eb-8aba-c1cb7a6f3e0c.png)


![image](https://user-images.githubusercontent.com/45536407/123011432-5d5b1880-d38e-11eb-8360-0daa51205501.png)


We already have the username so I thought I'll try bruteforcing through hydra but it did not work.

![image](https://user-images.githubusercontent.com/45536407/123011530-90051100-d38e-11eb-88e6-35d96bbdecd3.png)

I was looking around and I thought of trying the string found in robots.txt as the password, it worked and we got a text prompt to execute a command.

![image](https://user-images.githubusercontent.com/45536407/123011613-c2167300-d38e-11eb-84b5-97d6274d8493.png)


first command I executed was "ls"

![image](https://user-images.githubusercontent.com/45536407/123011654-d490ac80-d38e-11eb-8513-377c388efd27.png)

as you can see we the first super secret ingredient is in the same directory. You can read the fiie by navigating to <machine_ip>/Sup3rS3cretPickl3Ingred.txt
but since we had the ability to execute command to I wanted to read it using it. I tried cat but it was not allowed, then I tried more but that was also not allowed.

I was able to read the flag using less

![image](https://user-images.githubusercontent.com/45536407/123346628-bbbaff00-d526-11eb-88cd-e105342b4233.png)


Looking into clue.txt we got the hint lo looh around the file system.

![image](https://user-images.githubusercontent.com/45536407/123347022-e60cbc80-d526-11eb-831a-d9a444738005.png)

I checked for the users present and the second ingrediant was in the home directory of rick

![image](https://user-images.githubusercontent.com/45536407/123347751-15bbc480-d527-11eb-8499-4e6dcd6d44df.png)

![image](https://user-images.githubusercontent.com/45536407/123347987-279d6780-d527-11eb-945b-f437a979aadc.png)

![image](https://user-images.githubusercontent.com/45536407/123348351-43087280-d527-11eb-9808-396288c74efc.png)

since this was our user.txt I thought last flag will be root.txt so I started ways to escalate priviledges.
Before trying anything else I checked sudo priviledges of our user.

![image](https://user-images.githubusercontent.com/45536407/123349949-fb361b00-d527-11eb-83b2-379164252699.png)


It means we can run all the commands without the need of password.

so I checked for the flag in the root directory and found our flag there

![image](https://user-images.githubusercontent.com/45536407/123350017-24ef4200-d528-11eb-897c-7d7432c33b12.png)

![image](https://user-images.githubusercontent.com/45536407/123350079-42241080-d528-11eb-84e8-d5e5e542c5db.png)





