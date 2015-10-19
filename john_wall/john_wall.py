# 1. go to 'stats.nba.com'
# 2. click on John Wall ( or any player you like )
# 3. click on tracking -> shot log
# 4. in Firefox: Tools -> Web Developer -> Toggle Tools -> Network tab -> XHR tab
# 5. Refresh
# 6. click on 'playerdashptshotlog?DateFrom........'
# 7. Headers -> Request URL: copy that url ( that's the url we're going to scrape
# 8. It's good to install JSONView for Firefox ( https://addons.mozilla.org/en-us/firefox/addon/jsonview/ )
# 9. You can do this for every player you like

import requests
import csv

url = "http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=202322&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="

html = requests.get(url)
html.raise_for_status()
data = html.json()['resultSets'][0]['rowSet']

with open('john_wall.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)



