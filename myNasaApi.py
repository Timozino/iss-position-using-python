import requests
import time


def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    print(data)
    if response.status_code == 200:
        position=data['iss_position']
        latitude = float(position['latitude'])
        longitude = float(position['longitude'])
        print(position)
        return latitude, longitude
        
    else:
        print("Failed to retrieve ISS position")
        return None, None
        

print(get_iss_position())
        
        
    