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
#define the regular expressions
find_link = re.compile(r'<a href="(.*?)">') 
find_img = re.compile(r'<img.*src="(.*?)"', re.S)
find_title = re.compile(r'<span class="title">(.*)</span>')
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
find_judge = re.compile(r'<span>(\d*)人评价</span>')
find_summary = re.compile(r'<span class="inq">(.*)</span>')
find_related = re.compile(r'<p class="">(.*?)</p>', re.S)

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
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.findAll('div', class_="item"): #search for needed String
            # store the info of one movie to a list
            data = [] 
            #do a typecasting
            item = str(item)
            link = re.findall(find_link, item)[0]
            img = re.findall(find_img, item)[0]
            title = re.findall(find_title, item) #some movies have two titles
            rating = re.findall(find_rating, item)[0]
            judge = re.findall(find_judge, item)[0]
            summary = re.findall(find_summary, item)
            related_info = re.findall(find_related, item)[0]
            # do some data optimization, let it more beautiful :)
            related_info = re.sub('<br(s\+)?/>(s\+)?', ' ', related_info)
            related_info = re.sub('(\xa0)*','', related_info)
            related_info = re.sub('(\n)*','', related_info)
            related_info = re.sub('/','', related_info)
            related_info = re.sub('\.*                             ','', related_info)
            related_info = related_info.strip()
            data.append(link)
            data.append(img)
            if(len(title) == 2):
                chinese_title = title[0]
                data.append(chinese_title)
                foriegn_title = title[1].replace("/","")
                data.append(foriegn_title.replace("\xa0",""))
            else:
                data.append(title)
                data.append(" ") # add an empty space if there is no foriegn name
            data.append(rating)
            data.append(judge)
            if(len(summary) != 0):
                summary = summary[0].replace('。', "")
                data.append(summary)
            else:
                data.append(" ") # add an empty space if there is no summary
            datalist.append(data)
            data.append(related_info)
        print(datalist)
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
    getData(baseUrl)
