Project Proposal
    The main purpose of our project is to build a webapp that will generate recipes of dishes when the user inputs ingredients they have on hand.
Data Base:
    The database we are going to use is ‘https://spoonacular.com/food-api’ dataset, which provides over 5000+ recipes with 2600+ ingredients. The dataset could help us to deal with most inputs of our users. We can request an api key for free from the website.
Data:
    We found that the dataset has the function of searching recipes by ingredients. After inputting intended ingredients, the dataset could provide us a list of recipes like the picture 1.
    From the list, we are able to return id of recipes containing intended ingredients. Then, we use the id to do a search again in the dataset, which returns a list of detailed information of recipes like the picture 2. 
    We will return the summary in the list to users, which includes the name of dishes, the estimated time of making it, all the ingredients of the recipes and other key information that will help users to decide whether to make it.
Coding:
    To achieve our goals we mentioned before, we need to write many functions in python to make it work. First, we need a get_json(url) function to load the data. Second, we need a function of get_id(ingredients) to get the id of recipes. Third, we need a get_summary(id) function to return the recipes summary. Finally, we need a main function to call the functions. We will put these functions into a recipehelper.py file. Then, we will need a recipeapp.py to build our webapp. We will use flask to help our webapp. We will import the functions from the recipehelper.py to help get the results. We will adjust the html of webapp form to make our page better looking. 
Format:
    We plan to use a website to exhibit our webapp design. The website will include our mission of designing this webapp, our contact information, and instruction of using the web app.
Mission:
    Nowadays, people are more conscious about what they eat and are increasingly aware of choosing fresh and healthy options for their meals. Our main mission of designing this webapp is to help people who are interested but inexperienced at cooking to learn how to cook. Our value proposition is to provide helpful meal recommendations and give convenient access to easy-to-follow recipes to users. In addition to meal recipes, our webapp provides information about the nutritional aspects of the meal. This not only allows users to learn about the nutritional factors that go into their meals, but also allows users on certain diets to make conscious decisions about choosing their own recipes. 
