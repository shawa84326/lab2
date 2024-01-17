import requests
import time 


url = "https://visitseattle.org/events/page/1"

# CREATE -> POST
# Read -> GET
# Update -> PUT
# DELETE -> DELETE

# requests.post("https://concert.com/buy")
# requests.put("https://github.com/rgulla")
# requests.delete("https://facebook.com/ravinder.gulla/post/1")

res = requests.get(url)

# 200 -> OK
# 201 -> Created (after POST)
# 301 -> Moved Permanently
# 302
# 400 -> Bad Request (error from user)
# 404 -> Not Found (error from user)
# 500 -> Internal Server Error (error from server)
res.status_code

res.text

open("seattleevents.html", "w").write(res.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

selector = "div.search-result-preview> div > h3 > a "
a_eles = soup.select(selector)
a_eles


[x['href'] for x in a_eles]

for a_ele in a_eles:
    url = a_ele.get('href')
    print(url)



import requests
url = "https://api.weather.gov/points/39.7456,-97.0892"
res = requests.get(url)
res
res.text

point_dict.keys()

forcast_url = point_dict['properties']['forecast']
forcast_url
res = requests.get(forcast_url)
res.json()
# location name to lat lon

# Option 1: just string manipulation
base_url = "https://nominatim.openstreetmap.org/search.php"
query_params_str = "?q=Wallingford%2C+Seattle&format=jsonv2"
ful_url = base_url + query_params_str

# Option 2: use dictionary to represent query params
#           use requests.get(url, params=query_params) to attach the query param dict
query_params = {
    "q": "Wallingford, Seattle",
    "format": "jsonv2"
}

res = requests.get(base_url, params=query_params)
res.json()