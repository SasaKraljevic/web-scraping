import requests
from bs4 import BeautifulSoup

next = range(1,2) # set how many pages you'd like to scrape
for i in next:
    i = str(i)

    url = requests.get('http://www.yellowpages.com/search?search_terms=Coffee&geo_location_terms=Los Angeles%2C CA&page=' + i)

    soup = BeautifulSoup(url.content)
    links = soup.find_all('a')
        
    g_data = soup.find_all('div', {'class': 'info'})
    for  item in g_data:
    #### 01 FIND ORDINAL NUMBER ####
        num = item.find_all('h3', {'class': 'n'})[0].text[0:3]
        print 'NO:', num
    
    #### 02 FIND NAME ####
        name = item.contents[0].find_all('a', {'class': 'business-name'})[0].text
        print 'NAME:', name
        
    #### 03 FIND CITY ####    
        try:
            city = item.contents[1].find_all('span', {'itemprop': 'addressLocality'})[0].text.replace(',', '')
            print 'CITY:', city
        except:
            print 'NO CITY'
            
    #### 04 FIND STREET ####
        try:
            street = item.contents[1].find_all('span', {'itemprop': 'streetAddress'})[0].text
            print 'STREET:', street
        except:
            print 'NO STREET'
        
    #### 05 FIND PHONE ####        
        try:
            phone = item.contents[1].find_all('div', {'itemprop': 'telephone'})[0].text
            print 'PHONE:', phone
        except:
            print 'NO PHONE'
        print '-'*50

