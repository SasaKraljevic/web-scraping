#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################
# scrape several pages from Yahoo, specifically:
# http://biz.yahoo.com/research/earncal/20140414.html.
# That URL returns a list of companies, with the following data:
# Company, Symbol, Time, Conference Call
################################################################
from bs4 import BeautifulSoup
import unicodecsv as csv
from datetime import date
from dateutil.rrule import rrule, DAILY
import requests
import codecs

a = date(2010, 1, 1)
b = date(2014, 12, 31)
dates = []
names = []
symbols = []
times = []
datumi = []
confs = []

for dt in rrule(DAILY, dtstart=a, until=b):
    a = dt.strftime("%Y%m%d")
    dates.append(a)                           

for date in dates:
    try:
        url = "http://biz.yahoo.com/research/earncal/"+date+".html"
        htmlfile = requests.get(url)
        htmltext = htmlfile.text
        
        soup = BeautifulSoup (htmltext) 
        
        all_tables = soup.find_all('table')
        target_tr = all_tables[5].find_all('tr')
        
        for all_tr in range(3, len(target_tr)-2):
            target_td = target_tr[all_tr].find_all(['td'])
            if len(target_td) >3:
                name = target_td[0].text
                names.append(name)
                
                symbol = target_td[1].text
                symbols.append(symbol)
                
                time = target_td[2].text
                times.append(time)
                
                datumi.append(date)
                
                if target_td[3].text == 'Listen':
                    conference = target_td[3].find('a').get('href')
                    confs.append(conference)
                else:
                    conference = target_td[3].text
                    confs.append(conference)
                    
            else:
                name = target_td[0].text
                names.append(name)
                
                symbol = target_td[1].text
                symbols.append(symbol)
                
                time = target_td[2].text
                times.append(time)
                
                datumi.append(date)
                
                conference = ' ' 
                confs.append(conference)
  
    except:
        continue

with open('company.csv', 'w') as f:                       
    lista = zip(names, symbols, times, datumi, confs)     
    wtr = csv.writer(f)                                                      
    wtr.writerows(lista)                          
                              

