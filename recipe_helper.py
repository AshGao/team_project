from operator import index
import urllib.request
import json
import pprint

from matplotlib.pyplot import get
from config import MY_API_KEY
from urllib.request import Request, urlopen
import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    response_data = json.loads(webpage)
    return response_data

def get_id(ingredient):
    url=f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={MY_API_KEY}&ingredients={ingredient}&number=2'
    response_data=get_json(url)
    ids=[]
    for i in range (len(response_data)):
        ids.append(response_data[i-1]['id'])
    return ids


def get_cal(id):
    url=f'https://api.spoonacular.com/recipes/{id}/nutritionWidget.json?apiKey={MY_API_KEY}'
    response_data=get_json(url)
    cal=response_data["calories"]
    cal=float(cal[0:-1])
    return cal


def get_title(id):
    url=f'https://api.spoonacular.com/recipes/{id}/summary?apiKey={MY_API_KEY}'
    response_data=get_json(url)
    return response_data["title"]


def get_steps(id):
    url=f'https://api.spoonacular.com/recipes/{id}/analyzedInstructions?apiKey={MY_API_KEY}'
    response_data=get_json(url)
    steps=''
    for i in range(len(response_data[0]['steps'])):
        steps= steps + '<br>' + f'step{i+1}' + ': ' + response_data[0]['steps'][i]['step']+ ' '
    return steps

def get_recipes_title(ingredient,cal):
    id_list=get_id(ingredient)
    title=''
    for id in id_list:
        if cal <= get_cal(id):
            pass
        else:
            title += 'The recommended recipe is: '+ get_title(id) +'<br>'
    if title=='':
        title= 'Please change the ingredient or increase calories!'
    return title


def get_recipes_steps(ingredient,cal):
    id_list=get_id(ingredient)
    steps=''
    for id in id_list:
        if cal <= get_cal(id):
            pass
        else:
            steps += 'The cooking steps of ' + get_title(id) + 'are: '+ get_steps(id) +'<br>'+'<br>'
    return steps

#print(get_recipes_title('pork',2000))
#print(get_recipes_steps('pork',2000))
#url=f'https://api.spoonacular.com/recipes/{659581}/analyzedInstructions?apiKey={MY_API_KEY}'
#print(get_json(url))
print(get_recipes_title('pork',100))