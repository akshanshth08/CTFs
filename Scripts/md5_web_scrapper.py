!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import urllib
import hashlib

#############way 1################################
# with urllib.request.urlopen('http://docker.hackthebox.eu:30689/') as response:
#    html_file = response.read()

################for local html file ####################################
# with open('') as html_file:
url = input("URL :")
r = requests.session()
source = r.get(url).text

#source = r.get('http://docker.hackthebox.eu:30689/').text
soup = BeautifulSoup(source, 'lxml')
#print(soup)
#print(soup.prettify())
to_hash = soup.body.h3.text
print(to_hash)
hashed = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
#print(dir(hashed))
print(f"after hashing : {hashed}")
payload = {'hash': hashed}
post_req = r.post(url, data=payload)
#post_req = r.post('http://docker.hackthebox.eu:30689/', data=payload)

print(post_req.text)
