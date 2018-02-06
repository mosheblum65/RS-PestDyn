# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 14:02:36 2017

@author: moshe
"""
import csv
f = open('C:\moshe\oliveHDF_Py\olivecoor\LahavMOD11A1.csv', 'r')
reader = csv.reader(f)
headers = reader.next()
#headers
column = {}

for h in headers:
   column[h] = []
print(column.keys())
L=column.keys().len()
print(L)
#order = {} # create empty dictionary
##add orders as they come in
#order ['Peter '] = 'Pint of bitter '
#order ['Paul '] = 'Half pint of Hoegarden '
#order ['Mary '] = 'Gin Tonic '
## deliver order at bar
#for person in order . keys ():
#print person , " requests ", order [ person ]   
#for h in column.keys():
#    data
    

for row in reader:
  for h, v in zip(headers, row):
     #print(v)
     column[h].append(v)
  print(v)
#print( column)