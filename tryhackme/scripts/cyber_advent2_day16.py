import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://10.10.125.236'
response = requests.get(url).text
#print(response)
soup = BeautifulSoup(response,"lxml")
links = soup.findAll('a')

for i in links:
    print(i)

for i in range(1,101,2):
    req_url = url + '/api/'+str(i)
    res = requests.get(req_url).text
    sp = BeautifulSoup(res,"lxml")
    print(sp)
