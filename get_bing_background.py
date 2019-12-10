import requests
import pprint
import json
from urllib import parse
from os import path
from datetime import date

# TODO: Only download when file doesn't exist

pp = pprint.PrettyPrinter(indent=4)

r = requests.get("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")

# pp.pprint(r.json())

data = json.loads(r.text)

url = "http://www.bing.com" + data["images"][0]["url"]

print(url)

# TODO: Prefix date

today = date.today()
filename = today.strftime('%Y%m%d_') + parse.parse_qs(parse.urlparse(url).query)['id'][0]

homeFolder = path.expanduser("~")

# Save pictures to a folder
pictureLocation = homeFolder + "/Pictures/"

r = requests.get(url)

with open(pictureLocation + filename, 'wb') as f:
    f.write(r.content)

print(pictureLocation + filename)
