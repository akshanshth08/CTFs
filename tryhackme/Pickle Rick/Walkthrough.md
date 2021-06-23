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

aas you can see we the first super secret ingredient is in the same directory. You can 


