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

#deal with the timeout
try:
    response3 = urllib.request.urlopen("http://httpbin.org/get", timeout = 0.01)
    print(response3.read().decode('utf-8'))
except urllib.error.URLError as e:
    print(e.reason)
    
#do some basic analysis
try:
    response4 = urllib.request.urlopen("https://douban.com")
    #200 is normal situation, 405 is 'cannot access', 418 is awful camouflage
    #error418 Have been known by the website we are a spyder茶壶梗
    print(response4.status)
except urllib.error.URLError as e:
    print(e.code)

#get the header of a website
response5 = urllib.request.urlopen("http://www.baidu.com")
print(response5.getheaders())
#get any field you want
print(response5.getheader("Cache-Control"))

#to see the user agent information in your browser
#enter any website and press F12 on your keyboard - network - refresh the page

#try to do something really excited
url = "https://www.douban.com"
#camouflage yourself as a browser but not a spyder
#the more things you put into the headers, the better camouflage you will have
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
data2 = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = "utf-8")
#create a request
#actually the data and the method is not needed
#req = urllib.request.Request(url = url, data = data2, headers = headers, method = "POST")
req = urllib.request.Request(url = url, headers = headers)
#get a response
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))

















