import requests, json

# ---------------------------#
'''
就把 要搜尋的地點丟到 origin
然後 destination 就不理他了
這樣就好 ㄎㄎ
然後回傳 經緯度
'''
# ---------------------------#
def placeToLonglat(place):
    origin = place
    destination = '成大'
    api_key = 'AIzaSyApu8_hL9odn9K9xFecSaEABJibzKC7dN4'
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request

    resp = requests.get(request)
    data = json.loads(resp.text)
    print(data)

    #print(data['routes'][0]['legs'][0]['duration']['text'])
    start_location_long_float = float(data['routes'][0]['legs'][0]['start_location']['lat'])
    end_location_lat_float = float(data['routes'][0]['legs'][0]['start_location']['lng'])
    #print(origin + '的經緯度')
    #print(start_location_long_float)
    #print(end_location_lat_float)
    r = []
    r.append(start_location_long_float)
    r.append(end_location_lat_float)
    return r
    #print(data['routes'][0]['legs'][0]['start_location']['lat'])
    #print(data['routes'][0]['legs'][0]['start_location']['lng'])
    #print(data['routes'][0]['legs'][0]['end_location']['lat'])
    #print(data['routes'][0]['legs'][0]['end_location']['lng'])