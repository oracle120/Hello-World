#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(requests.get("https://global.ishadowx.net").text, "html.parser")
#print(soup.find_all("div",{"class","hover-text"}))

#for x in soup.find_all("div", {"class", "hover-text"}):
#    print("ip:",x.h4.span.string)
#    print("ip:",x.select('#ipusb'))
#    print("ip:",x.find(id="ipusb"))
#    print("port:",x.find(id="portusb"))
#    print("password:",x.find(id="pwusb"))

#for all_div in soup.find_all('div',attrs={'class':'hover-text'},limit=1):
#    print(all_div)
#    ip1=all_div.h4.strings
#    for str in ip1:
#        print("---",str)
#    ip=all_div.find('span',attrs={'id':'ipusb'})
#    print("ip:",ip)
#    port=all_div.find('span',attrs={'id':'portusb'})
#    print(port)

for span in soup.find_all('span',attrs={'id':re.compile("usb")}):
    if len(span.string) > 0 and span.string is not None:
        print(span.string)
