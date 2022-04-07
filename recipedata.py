import urllib.request
import json

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

MY_API_KEY='a25f06573b434ccc9a93e1fa407c5fd6'
url = f'https://api.spoonacular.com/recipes/complexSearch'
print(get_json(url))
