#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:42:44 2020

@author: stevenyuan
"""
import xlwt

workbook = xlwt.Workbook(encoding = 'utf-8') #create a excel file
worksheet = workbook.add_sheet('sheet1') #create a sheet in the file
worksheet.write(0,0,'hello') #row,column,content  write into the sheet
workbook.save('test.xls') #save to current directory

#write a 9 * 9 multiplication sheet
worksheet2 = workbook.add_sheet('sheet2')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet2.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('test.xls')
        