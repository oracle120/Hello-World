#!/usr/bin/python
from urllib import request

response = request.urlopen(r'https://global.ishadowx.net/')
page = response.read()
page = page.decode('utf-8')
print(page)
