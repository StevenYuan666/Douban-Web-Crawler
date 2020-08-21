#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:28:23 2020

@author: stevenyuan
"""
#Notes for urllib
import urllib.request

#get request
#open a website and get response
response = urllib.request.urlopen("http://www.baidu.com")
#print the content of the response
#get the source code of the website, and use decode method to avoid the unreadable text
print(response.read().decode('utf-8'))

#post request
#have to pass an hashpair to do a post request
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = "utf-8")
response2 = urllib.request.urlopen("http://httpbin.org/post", data = data)
print(response2.read().decode('utf-8'))
