#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:13:59 2020

@author: stevenyuan
"""
#Note for BeautifulSoup
#BeautifulSoup4 is used for transferring the html to a complicated tree structure
#every root is a python object, and all of objects are following four types:
#Tag, NavigableString, BeautifulSoup, Comment


from bs4 import BeautifulSoup
#open the html file first
file = open("./baidu.html","rb")
#read it
html = file.read().decode("utf-8")
#create a beautifulsoup object and point a parser
bs = BeautifulSoup(html, "html.parser")


#get the title of the html after the tranformation
#get the content by the tags of the html file
print(bs.title)
print(bs.a)
#Tags and their contents found first
print(type(bs.head))

print(bs.title.string)
#NavigableString, the content in the Tags
print(type(bs.title.string))
#get all of attributes from a Tag
print(bs.a.attrs)

#BeautifulSoup, represent the whole file
print(type(bs))

#Comment is a special type of NavigableString, which will remove the syntax of comment and return the content


#-------------------HOW TO APPLY---------------------
#traversal of the file
#get all of contents in head, return as a list
#more commands listed in the document
#print(bs.head.contents)


#search of the file

#find_all()
t_list = bs.find_all("a") #return all contents with Tag "a"
print(t_list)

#regular expression:search() to find the matched contents
import re
t_list2 = bs.find_all(re.compile("a"))#return all of content if the tags including "a"
print(t_list2)

#method : input a method and search depends on the request of the method
def name_is_existed(tag):
    return tag.has_attr("name")

t_list3 = bs.find_all(name_is_existed)#return all of contents including the attribute "name"
print(t_list3)

#kwargs Parameter
t_list4 = bs.find_all(id = "head")#return all content between the tags id=head
print(t_list4)

#text Parameter
t_list5 = bs.find_all(text = "hao123")
print(t_list5)
t_list6 = bs.find_all(text = ["hao123","登陆","地图"])#if including, return it, or return null
print(t_list6)
t_list7 = bs.find_all(text = re.compile("/d"))#return all contents including digits(string of the tag)
print(t_list7)

#limit Parameter
t_list8 = bs.find_all("a", limit = 3)#return the first number of "limit" contents
print(t_list8)


#css Selector
t_list9 = bs.select("title") #select by Tags
print(t_list9)

t_list10 = bs.select(".mnav") #". + String" = class name in css, search by class name
print(t_list10)

t_list11 = bs.select("#u1") #"# + String" = id in css, search by id
print(t_list11)

t_list12 = bs.select("a[class='bri']") #search by attribute
print(t_list12)

t_list13 = bs.select("head > title") #search by sub Tags
print(t_list13)

t_list14 = bs.select(".mnav ~ .bri") #search by sibling Tags
print(t_list14)

















