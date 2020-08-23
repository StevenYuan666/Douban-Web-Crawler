#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:37:30 2020

@author: stevenyuan
"""

#Note for regular expression
#regular expression is used to represent the regularity of Strings

import re

# . represents any character
# [] represents the range of the character, [abc] represents a,b,c [a-z] represents any letter from a to z
# [^ ] represents the range except the character in[], [^abc] represent any character except a,b,c
# * represents o time to infinite times repeatation for the previous character, abc* can be ab, abc, abccc...
# + represents 1 time to infinite times repeatation for the previous character, abc* can be abc, abcc, abccc...
# ? represents 0 time to 1 time repeatation for the previous character, abc? can be ab or abc
# | represents the string should be matched with the left part or the right part, abc|def should be abc or def
# {m} represents that it has to repeat the previous character for m times, ab{2}c is abbc
# {m,n} represents that it has to repeat the previous character for m to n times, ab{1,2}c can be abc or abbc
# ^ represents the string has to be started with such characters, ^abc  A string started with abc
# $ represents the string has to be ended with such characters, abc$ A string ended with abc
# ()group labels, (abc) represents abc (abc|def) represents abc or def, only | is allowed inside ()
# \d represents any digits, which is equal to [0-9]
# \w represents single word, which is equal to [A-Za-z0-9_], not including han characters

#some main function in re module
#re.search()
#re.match()
#re.findall()
#re.split()
#re.finditer()
#re.sub()

#some mode when using re module
#re.I unsensitive to the case of characters
#re.L
#re.M
#re.S let . including the newline character and any other characters
#re.U
#re.X

#create an object
pattern = re.compile("a{2}bc") #the regular expression here
result1 = pattern.search("aabccbsjsjs") #the text you want to compare with the regular expression
print(result1)
result2 = pattern.search("sjsjs") # the search method will return the span when it found the first matched content
print(result2) #return none if there is no matched content

#without an object
result3 = re.search(".*","abcdefg") #input the regular expression first, then the content you want to compare
print(result3)

#findall() method
result4 = re.findall(".","abcdefghijklmn")#input the regular expression first, then the content you want to compare
print(result4) #return all content matched

#sub method
result5 = re.sub("a","A","hahaha") # use the second parameter to substitute all the first parameter in the third parameter
print(result5)

#advice: add r before the content you want to compare to avoid the problem of escape characters
a = r"\aabd-88\'9"
print(a)
























