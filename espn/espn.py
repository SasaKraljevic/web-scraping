# list of players from espn.com
import urllib2
from bs4 import BeautifulSoup

f = open('outespn.txt', 'w')

x = 0
while (x < 200): # how many players? 40,80,120....
    soup = BeautifulSoup(urllib2.urlopen('http://games.espn.go.com/ffl/tools/projections?startIndex='+str(x)).read(), 'html')
    tablestats = soup.find("table", {"class" : "playerTableTable tableBody"})
    for row in tablestats:        
        player_row = row.findAll('td', {'class': 'playertablePlayerName'})
        for row in player_row:
            name = row.find('a').text
            # print name
            f.write(name+'\n')
    x = x + 40
    
f.close

