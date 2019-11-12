# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:07:40 2019

@author: gaura
"""

from bs4 import BeautifulSoup
import requests

for i in range(0,50,1):
    page = requests.get("https://theyfightcrime.org/")
    page.status_code
    
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find_all('p')
    full=soup.find_all('p')[1].get_text()
    split=[x for x in map(str.strip, full.split('.')) if x]

    male=split[0]
    female=split[1]
    
    f= open("Male.txt","a+")
    f.write(f"\n{male}")
    
    g= open("Female.txt","a+")
    g.write(f"\n{female}")
    i+=1
    
