# Inclusion 
### https://tryhackme.com/room/inclusion


It is a beginner level room focusing on Local file inclusion vulnerability.

ran masscan to check the open ports on the server.

![image](https://user-images.githubusercontent.com/45536407/123497053-68fe4780-d5f9-11eb-8d66-ce7a4eda433a.png)

Only 2 ports running 1 for ssh and other for web server.

I checked the website.

![image](https://user-images.githubusercontent.com/45536407/123497082-87644300-d5f9-11eb-9224-87044544bc4a.png)

looking around the website you find that it is using a variable called "name" to fetch the contents of the page and that might be vulnerable to LFI

![image](https://user-images.githubusercontent.com/45536407/123497127-c85c5780-d5f9-11eb-9e73-55d889d3c837.png)

I exploit that vulnerability to read /etc/passwd file and get the passwd for the user which is present in that file

![image](https://user-images.githubusercontent.com/45536407/123497166-fc377d00-d5f9-11eb-87bc-38acce391a0c.png)

Since I know I can read the files manipulating the variable in the URL and I know the home directory of the user from /etc/passwd I read the user flag from the browser

![image](https://user-images.githubusercontent.com/45536407/123497210-3bfe6480-d5fa-11eb-8dd8-d36ccd02ee41.png)

for the root flag I ssh'd to the machine using the password found above.

![image](https://user-images.githubusercontent.com/45536407/123497255-6bad6c80-d5fa-11eb-8cb2-3e141e2e25c9.png)


For escalating priviledges checked the sudo priviledges for the user and it could run socat without password

![image](https://user-images.githubusercontent.com/45536407/123497287-9e576500-d5fa-11eb-944d-99a23fe0b957.png)

Checked GTFOBins (https://gtfobins.github.io/gtfobins/socat/#sudo) to see if I can exploit this binary, which I can

![image](https://user-images.githubusercontent.com/45536407/123497333-f4c4a380-d5fa-11eb-9bd3-717e1dda7b0f.png)


using this esclated to root and read the flag
![image](https://user-images.githubusercontent.com/45536407/123497376-2f2e4080-d5fb-11eb-9024-538d36cd57d3.png)


