
'''
1. get google maps api key
2. query searhc data of comedy clubs
3. write data to excel sheet
'''

import requests

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Comedy%20Clubs&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=AIzaSyBhY-NtxGx2Fq_W2UE0MSUW7v6w2e3ca4M"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


'''
import requests

#gmaps api key
api_key = "AIzaSyBhY-NtxGx2Fq_W2UE0MSUW7v6w2e3ca4M"
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

query = input("comedy clubs: ")

req = requests.get(url + 'query=' + query + '&key=' + api_key)

json_format = req.json()

store_dict = json_format['results']

for i in range(len(store_dict)):
    print(store_dict[i]['name'])
'''


'''
# Initialize 
gmap = googlemaps.Client(key=API_KEY)

#gmaps search
#@@is the search being specified locationally?@@
search_query = 'comedy clubs'
search_results = gmap.places(query=search_query)

#create excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "results"

#headers/features
headers = ['Name', 'Address', 'Rating', 'User Ratings Total']
ws.append(headers)

#write to excel
for result in search_results['results']:
    name = result['']
    address = result.get('', '')
    rating = result.get('', '')
    user_ratings_total = result.get('', '')
    ws.append([name, address, rating, user_ratings_total])

#save
wb.save('gmaps-search-result.csv')
wb.save('gmaps-search-result.json')
'''