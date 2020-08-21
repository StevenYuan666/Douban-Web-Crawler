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

#the main function to run all of functions
def main():
    #the target URL
    baseUrl = "https://movie.douban.com/top250?start="
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
    return datalist

#Save the data
def saveData(savePath):
    return 0


if __name__ == '__main__':
    print('666')
