# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:07:40 2019

@author: gaura
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
maleheroes=[]
femaleheroes=[]
for i in range (0,50,1):
    page = requests.get("https://theyfightcrime.org/")
#   page
#   page.content
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.find_all('p')
    all = list(text)
    p = all[1]
    p.get_text()
    combined = p.get_text().split('.')
    male = combined[0]
    female = combined[1]
    maleheroes.append(male)
    femaleheroes.append(female)
    
with open("Male.txt", "w") as f:
    for i in maleheroes:
        f.write("{}\n".format(i))
        
with open("Female.txt", "w") as f:
    for i in femaleheroes:
        f.write("{}\n".format(i))
    
