
'''
1. get google maps api key
2. query searhc data of comedy clubs
3. write data to excel sheet
'''


import googlemaps
import openpyxl

#gmaps api key
API_KEY = "AIzaSyBhY-NtxGx2Fq_W2UE0MSUW7v6w2e3ca4M"

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
