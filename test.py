import requests
from data import Location
url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)

json_content = html_content.json()
print(json_content)

records = json_content.get('records')
location = records.get('location')

location = []

for l in location:
    location_site = Location()
    location_site.from_json(l)
    location.append(l)
    print(Location)