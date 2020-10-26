# -*- coding:utf-8 -*- 
import requests
import urllib
import os
from bs4 import BeautifulSoup
protocol="https://"
base="www.qinmanga.com"
urlp="/comic/"
urlid="25776"
postfix="/"



# def main():
handoutstr = base + urlp + urlid + postfix
handoutstr = protocol + urllib.parse.quote(handoutstr)
print("Handoutstr:",handoutstr);
req  = requests.get(handoutstr);
soup = BeautifulSoup(req.text, 'html.parser')
data = soup.find_all('a',attrs={"class":"","target":"_blank"})
print("Title:",soup.title.text)
if not os.path.exists(soup.title.text):
    os.mkdir(soup.title.text)
    
os.chdir(soup.title.text)

for i in data:
    if not os.path.exists(i['title']):
        hole=os.mkdir(i['title'])
    os.chdir(i['title'])
    if os.path.exists('_Complete'):
        print(i['title'] + " is already downloaded")
        os.chdir('..')
        continue
    tmpreq = requests.get(protocol + base + i['href'])
    tmpsoup = BeautifulSoup(tmpreq.text, 'html.parser')
    tmpdata = tmpsoup.find_all('amp-img')
    cnt = 1
    for tmpi in tmpdata:
        imgreq = ""
        while True:
            imgreq = requests.get(tmpi['src'])
            if(imgreq.status_code == 200):
                break
        print("Write:",i['title']," - ",str(cnt)+".jpg")
        f=open(str(cnt)+".jpg","wb")
        f.write(imgreq.content)
        f.close()
        cnt = cnt+1
    os.system('touch _Complete')
    os.chdir('..')
#     if(tmpreq.status_code 
# if __name__ == '__main__':
#     main()
    

