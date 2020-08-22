#-*- coding = utf-8 -*-
#@auhotr:Steven Yuan

#import the needed module
#analyze the website
from bs4 import BeautifulSoup
#expression, text matching
import re
#input URL, get website data
import urllib.request, urllib.error
#operate Excel
import xlwt
#operate SQLite
import sqlite3


baseUrl = "https://movie.douban.com/top250?start="

#the main function to run all of functions
def main():
    #the target URL
   
    #0. Preparation
    #1. Explore the websites
    datalist = getData(baseUrl)
    #2. Analyze the data one by one
    #3. Save the data
    #save to current directory
    savePath = ".\\Douban_Top250.xls"
    saveData(savePath)
    
#Explore the websites and analyze one by one
def getData(inputURL):
    datalist = []
    #use a for loop to iterate all of the websites
    for i in range(0,10):
        url = baseUrl + str(i * 25)
        html = askURL(url)
        #analyze one by one
    return datalist

#get the info from the pointed URL
def askURL(url):
    #copy from the browser for camouflage
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html

#Save the data
def saveData(savePath):
    return 0


if __name__ == '__main__':
    print(askURL("https://movie.douban.com/top250?start="))
