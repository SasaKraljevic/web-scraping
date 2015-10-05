import requests
import re
from bs4 import BeautifulSoup
import csv
 
url = ("http://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10007&symbol=NIFTY&symbol=NIFTY&instrument=OPTIDX&date=-&segmentLink=17&segmentLink=17")

htmltext = requests.get(url).text

date_regex = '<span>(.+?)<a>.+?</a></span>'
date_pattern = re.compile(date_regex)
date = re.findall(date_pattern, htmltext)

symbol = 'NIFTY' 
option1 = 'CALLS'
option2 = 'PUTS' 

soup = BeautifulSoup(htmltext)
info_table = soup.find_all('div', {'id':'octable'})
tr = soup.find_all('tr')

strike_regex = ('<td class="grybg"><a href=".+?><b>(.+?)</b></a></td>')
strike_pattern = re.compile(strike_regex)
strike = re.findall(strike_pattern, htmltext)

data = tr[5].text
for td in data:
    td = soup.find_all('td')

oi_left = td[4].text
oi_right = td[23].text

chng_left = td[5].text
chng_right = td[22].text

volume_left = td[6].text   
volume_right = td[21].text 
 
iv_left = td[7].text 
iv_right = td[20].text
   
ltp_left = td[8].text 
ltp_right = td[19].text
   
netchng_left = td[9].text
netchng_right = td[18].text

bidqty_left = td[10].text
bidqty_right = td[14].text

bidprice_left = td[11].text
bidprice_right = td[15].text

askprice_left = td[12].text
askprice_right = td[16].text

askqty_left = td[13].text
askqty_right = td[17].text

left_col = [symbol, date[0][6:18], option1, strike[0], bidqty_left, bidprice_left, askprice_left, askqty_left, netchng_left, ltp_left, iv_left, volume_left, chng_left, oi_left]

right_col = [symbol, date[0][6:18], option2, strike[0], bidqty_right, bidprice_right, askprice_right, askqty_right, netchng_right, ltp_right, iv_right, volume_right, chng_right, oi_right]

print symbol, date[0][6:18], option1, strike[0], bidqty_left, bidprice_left, askprice_left, askqty_left, netchng_left, ltp_left, iv_left, volume_left, chng_left, oi_left
print '------------------------------------------------------'
print symbol, date[0][6:18], option2, strike[0], bidqty_right, bidprice_right, askprice_right, askqty_right, netchng_right, ltp_right, iv_right, volume_right, chng_right, oi_right
    
headers = ('Symbol', 'Date', 'Option', 'StrikePrice', 'BidQty', 'BidPrice', 'AskPrice', 'AskQty', 'NetChng', 'LTP', 'IV', 'Volume', 'Chng in OI', 'OI')

with open('nseindia.csv', 'w') as f:                      
    lista = (headers, left_col, right_col)   
    to_print = headers + lista
    wtr = csv.writer(f)                                        
    wtr.writerows(lista)   


