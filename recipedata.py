import urllib.request
import json
import pprint

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

MY_API_KEY='5dbaf09b8f4f43e0934b075ceb0d301a'
#url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={MY_API_KEY}&ingredients=apples,+flour,+sugar&number=2'
url='https://api.spoonacular.com/recipes/findByIngredients?apiKey=5dbaf09b8f4f43e0934b075ceb0d301a&ingredients=apples,+flour,+sugar&number=2'
pprint(get_json(url))
